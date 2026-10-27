"""Actual pinned AD graph versus ordinary pre-operation branching.

Importing this module does not import NumPy/Autograd or evaluate the target.
The collapsed graph is the only graph tested; first derivatives only.
"""
from __future__ import annotations

from email.parser import BytesParser
from fractions import Fraction
import hashlib
import math
import json
import importlib.metadata
import os
from pathlib import Path
import sys
import time
import warnings
import zipfile

from .ad_reference import analytic, finite_differences, agrees, residual, judge_valid
from .attempts import record_progress, set_execution_phase


def checked_wheel(path, expected_hash):
    path = Path(path).resolve()
    if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != expected_hash:
        raise ValueError("Pinned Autograd wheel missing or hash mismatch")
    return path


def verified_imports(path, member_hashes):
    imported = {}
    for name, module in sorted(sys.modules.items()):
        if name == "autograd" or name.startswith("autograd."):
            source = getattr(module, "__file__", "")
            prefix = str(path) + "/"
            if not source.startswith(prefix):
                raise RuntimeError("Imported Autograd escaped pinned wheel: " + name)
            member = source[len(prefix):]
            body = module.__loader__.get_data(source)
            if member not in member_hashes or hashlib.sha256(body).hexdigest() != member_hashes[member]:
                raise RuntimeError("Imported source mismatch: " + name)
            imported[name] = {"member": member, "sha256": member_hashes[member]}
    return imported


def numpy_pin(spec):
    root = Path(__file__).resolve().parents[2]
    declaration = spec["external_runtime"]["numpy_observed_pin"]
    path = (root / declaration["path"]).resolve()
    if not path.is_relative_to(root) or hashlib.sha256(path.read_bytes()).hexdigest() != declaration["sha256"]:
        raise RuntimeError("Frozen NumPy installation pin changed")
    pin = json.loads(path.read_text())
    with open(sys.executable, "rb") as stream:
        if hashlib.file_digest(stream, "sha256").hexdigest() != pin["python_executable_sha256"]:
            raise RuntimeError("Frozen interpreter executable differs")
    return pin


def verified_numpy_imports(pin):
    distribution = importlib.metadata.distribution("numpy")
    if distribution.version != pin["version"]:
        raise RuntimeError("NumPy distribution metadata differs")
    site = Path(distribution.locate_file("")).resolve()
    imported = {}
    for name, module in sorted(sys.modules.items()):
        if name == "numpy" or name.startswith("numpy."):
            source = getattr(module, "__file__", None)
            if not source or not Path(source).is_file():
                raise RuntimeError("Cannot bind required NumPy module file: " + name)
            path = Path(source).resolve()
            if not path.is_relative_to(site):
                raise RuntimeError("NumPy module escaped declared installation: " + name)
            member = str(path.relative_to(site))
            with path.open("rb") as stream:
                observed_hash = hashlib.file_digest(stream, "sha256").hexdigest()
            if member not in pin["files"] or observed_hash != pin["files"][member]["sha256"]:
                raise RuntimeError("NumPy module differs from pre-target observed pin: " + name)
            imported[name] = {"file": source, "member": member, "sha256": observed_hash}
    return imported


def load_backend(spec):
    pinned_numpy = numpy_pin(spec)
    path = checked_wheel(os.environ.get("MATHWEAVE_AUTOGRAD_WHEEL", ""),
                         spec["external_runtime"]["wheel_sha256"])
    if any(k == "autograd" or k.startswith("autograd.") for k in sys.modules):
        raise RuntimeError("Fresh process required; Autograd already imported")
    with zipfile.ZipFile(path) as archive:
        metadata = BytesParser().parsebytes(archive.read("autograd-1.9.1.dist-info/METADATA"))
        if metadata["Name"] != "autograd" or metadata["Version"] != "1.9.1":
            raise RuntimeError("Unexpected wheel metadata")
        member_hashes = {name: hashlib.sha256(archive.read(name)).hexdigest()
                         for name in archive.namelist() if name.endswith(".py")}
    sys.path.insert(0, str(path))
    import numpy as np
    import autograd
    from autograd import grad
    if np.__version__ != spec["optional_dependencies"]["numpy"]:
        raise RuntimeError("Actual NumPy import version mismatch")
    imported = verified_imports(path, member_hashes)
    numpy_members = verified_numpy_imports(pinned_numpy)
    identity = {"autograd": metadata["Version"], "numpy": np.__version__,
                "numpy_file": np.__file__, "wheel_path": str(path),
                "wheel_sha256": spec["external_runtime"]["wheel_sha256"],
                "verified_imported_autograd_modules": imported,
                "numpy_imported_file_hashes": numpy_members,
                "numpy_frozen_manifest_sha256": spec["external_runtime"]["numpy_observed_pin"]["sha256"],
                "numpy_installed_RECORD_mismatches": pinned_numpy["installed_RECORD_mismatches"],
                "numpy_origin_limit": "Observed installed-file pin; native RECORD mismatches unresolved, not publisher attestation or fully hermetic shared libraries"}
    return np, grad, path, identity, member_hashes, pinned_numpy


def make_target(n, safe):
    q = 2.0 / (n - 2)
    c = -(n - 2) / 2.0

    def target(r, z):
        if z <= 0 if safe else z < 0:
            return z
        return z * (1.0 + r * r * (z ** q)) ** c

    return target


def observed(call, wheel):
    records = []
    with warnings.catch_warnings(record=True) as captured:
        warnings.simplefilter("always")
        try:
            value = float(call())
            label = ("finite" if math.isfinite(value) else
                     "nan" if math.isnan(value) else
                     "positive_infinity" if value > 0 else "negative_infinity")
            result = {"classification": label, "value": value if label == "finite" else None}
        except Exception as exc:
            result = {"classification": "exception", "value": None,
                      "exception_type": type(exc).__name__, "message": str(exc)}
        for warning in captured:
            source = warning.filename
            if source.startswith(str(wheel) + "/"):
                source = "<pinned-autograd-wheel>/" + source[len(str(wheel)) + 1:]
            elif "/src/ai_value/" in source:
                source = "ai_value/" + source.split("/src/ai_value/", 1)[1]
            else:
                source = Path(source).name
            records.append({"category": warning.category.__name__, "message": str(warning.message),
                            "source": source, "line": warning.lineno})
    result["warnings"] = records
    return result


def score(result, reference, tolerance):
    if result["classification"] != "finite":
        return {"within_tolerance": False, "absolute": None, "relative": None}
    return {"within_tolerance": agrees(result["value"], reference, tolerance),
            **residual(result["value"], reference)}


def summarize(rows, expected):
    if len(rows) != expected or any(not all(row["judge_checks"].values()) for row in rows):
        outcome = "inconclusive_reference_or_missing_fixture"
    elif any(value["classification"] == "exception" for row in rows
             for method in row["methods"].values() for value in method.values()):
        outcome = "inconclusive_backend_exception"
    else:
        outcome = None
    forwards = all(m["value"]["score"]["within_tolerance"]
                   for row in rows for m in row["methods"].values())
    baseline = all(v["score"]["within_tolerance"] for row in rows
                   for v in row["methods"]["old_preoperation_branch"].values())
    controls = all(row["methods"]["naive_factored"][k]["score"]["within_tolerance"]
                   for row in rows if Fraction(row["z"]) != 0 or row["n"] in (3, 4)
                   for k in ("dr", "dz"))
    naive_radial_zero = all(row["methods"]["naive_factored"]["dr"]["score"]["within_tolerance"]
                            for row in rows if Fraction(row["z"]) == 0)
    predicted_events = [row["index"] for row in rows if row["n"] >= 5 and Fraction(row["z"]) == 0
                        and row["methods"]["naive_factored"]["dz"]["classification"] != "exception"
                        and not row["methods"]["naive_factored"]["dz"]["score"]["within_tolerance"]
                        and all(row["judge_checks"].values())]
    conjuncts = {"forward_values": forwards, "old_baseline_all_components": baseline,
                 "naive_nonzero_and_smooth_controls": controls,
                 "naive_radial_zero_checked_separately": naive_radial_zero,
                 "predicted_zero_event_exists": bool(predicted_events)}
    # Radial-zero checks are separately reported; the v2 primary requires
    # forwards, old baseline, specified controls and the z-gradient event.
    meets = outcome is None and forwards and baseline and controls and bool(predicted_events)
    validated_conjuncts = conjuncts if outcome is None else {key: None for key in conjuncts}
    return {"fixtures": len(rows), "expected_fixtures": expected,
            "reference_valid_fixtures": sum(all(row["judge_checks"].values()) for row in rows),
            "primary_conjuncts": validated_conjuncts,
            "unvalidated_numeric_aggregates": conjuncts,
            "predicted_event_indices": predicted_events,
            "meets_prediction": meets,
            "outcome": outcome or ("bounded_calibration_supported" if meets else "primary_prediction_adverse"),
            "old_correct_branch_suffices": baseline if outcome is None else None,
            "incremental_2026_application_value_established": False,
            "real_network_or_library_contract_defect_established": False,
            "limits": "One frozen collapsed scalar graph; synthetic boundary inputs; shared Decimal engine; first derivatives; no prevalence,training,theorem or engineering benefit claim."}


def experiment(spec):
    setup_start = time.perf_counter()
    np, grad, wheel, identity, member_hashes, pinned_numpy = load_backend(spec)
    np.seterr(divide="warn", invalid="warn", over="warn", under="warn")
    setup_seconds = time.perf_counter() - setup_start
    record_progress({"phase": "backend_identity_verified", "identity": identity})
    start = time.monotonic()
    set_execution_phase("calculation", start)
    rows = []
    for n in spec["input"]["n"]:
        for r_text in spec["input"]["r"]:
            for z_text in spec["input"]["z"]:
                row = {"index": len(rows), "n": n, "r": r_text, "z": z_text}
                low = analytic(n, r_text, z_text, spec["reference"]["analytic_precision_low"])
                high = analytic(n, r_text, z_text, spec["reference"]["analytic_precision_high"])
                differences = [finite_differences(n, r_text, z_text, h, spec["reference"]["difference_precision"])
                               for h in spec["reference"]["steps"]]
                row.update(reference_low=low, reference_high=high, finite_differences=differences,
                           judge_checks=judge_valid(low, high, differences, spec["tolerances"]), methods={})
                r, z = float(Fraction(r_text)), float(Fraction(z_text))
                for name, safe in (("naive_factored", False), ("old_preoperation_branch", True)):
                    target = make_target(n, safe)
                    results = {"value": observed(lambda: target(r, z), wheel),
                               "dr": observed(lambda: grad(lambda rr: target(rr, z))(r), wheel),
                               "dz": observed(lambda: grad(lambda zz: target(r, zz))(z), wheel)}
                    for k, value in results.items():
                        value["score"] = score(value, high[k], spec["tolerances"]["float"])
                    row["methods"][name] = results
                rows.append(row)
                record_progress(row)
    summary = summarize(rows, spec["success"]["fixtures"])
    record_progress({"phase": "calculation_summary", "summary": summary})
    identity["verified_imported_autograd_modules_after_target"] = verified_imports(wheel, member_hashes)
    identity["numpy_imported_file_hashes_after_target"] = verified_numpy_imports(pinned_numpy)
    duration = time.monotonic() - start
    set_execution_phase("archive", time.monotonic())
    summary["_runtime_metrics"] = {"setup_import_identity_seconds": setup_seconds,
                                   "calculation_seconds": duration,
                                   "runtime_identity": identity,
                                   "calculation_scope": "All192AD/reference/controls andcompressed progress/summary persistence"}
    return rows, summary
