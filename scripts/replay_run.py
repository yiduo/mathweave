#!/usr/bin/env python3
"""Replay archived sources in a temporary directory and compare deterministic outputs."""

import argparse
import copy
import gzip
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import io
import tarfile
import traceback
import uuid
from contextlib import contextmanager
from datetime import datetime, timezone


@contextmanager
def replay_directory(folder):
    """Keep failure evidence before removing an isolated replay workspace."""
    with tempfile.TemporaryDirectory(prefix="ai-value-replay-") as temporary:
        root = Path(temporary)
        try:
            yield root
        except BaseException as exc:
            target = folder.parent.parent / "replay-failures" / (folder.name + "-" + uuid.uuid4().hex[:12])
            target.mkdir(parents=True)
            payload = {str(p.relative_to(root)): p.read_bytes() for p in root.rglob("*")
                       if p.is_file() and not p.is_symlink()}
            payload["replay-error.txt"] = traceback.format_exc().encode()
            original_inputs = {}
            if folder.is_dir():
                for path in folder.iterdir():
                    if path.is_file() and not path.is_symlink():
                        original_inputs[path.name] = {"bytes": path.stat().st_size,
                            "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
            payload["original-input-hashes-at-failure.json"] = json.dumps(original_inputs, indent=2).encode()
            for attr in ("stdout", "stderr"):
                text = getattr(exc, attr, None)
                if text is not None:
                    payload["replay-" + attr + ".log"] = text.encode() if isinstance(text, str) else text
            buffer = io.BytesIO()
            with tarfile.open(fileobj=buffer, mode="w") as archive:
                for name, data in sorted(payload.items()):
                    info = tarfile.TarInfo(name)
                    info.size = len(data)
                    info.mtime = 0
                    archive.addfile(info, io.BytesIO(data))
            raw = buffer.getvalue()
            packed = gzip.compress(raw, mtime=0)
            assert gzip.decompress(packed) == raw
            hashes = {name: hashlib.sha256(data).hexdigest() for name, data in payload.items()}
            with tarfile.open(fileobj=io.BytesIO(gzip.decompress(packed))) as archive:
                for name, expected in hashes.items():
                    assert hashlib.sha256(archive.extractfile(name).read()).hexdigest() == expected
            (target / "failure.tar.gz").write_bytes(packed)
            (target / "receipt.json").write_text(json.dumps({"at": datetime.now(timezone.utc).isoformat(),
                "original_run": folder.name, "exception": type(exc).__name__, "members": hashes,
                "archive_sha256": hashlib.sha256(packed).hexdigest(),
                "scope": "Observed replay failure files and logs; not a successful scientific replay"}, indent=2) + "\n")
            raise


def runtime_binding(identity):
    return {"autograd": identity["autograd"], "numpy": identity["numpy"],
            "wheel_sha256": identity["wheel_sha256"],
            "autograd_members": identity["verified_imported_autograd_modules"],
            "autograd_members_after_target": identity["verified_imported_autograd_modules_after_target"],
            "numpy_hashes": {k: v["sha256"] for k, v in identity["numpy_imported_file_hashes"].items()},
            "numpy_hashes_after_target": {k: v["sha256"] for k, v in identity["numpy_imported_file_hashes_after_target"].items()},
            "numpy_frozen_manifest_sha256": identity["numpy_frozen_manifest_sha256"]}


def require_replay_resources(manifest, spec, summary=None):
    # A deterministic match cannot turn a resource failure into a qualified replay.
    sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
    from ai_value.attempts import within_frozen_resources
    if spec.get("phase_watchdog") and manifest.get("measurement_state") != "parent_child_lifecycle_finalized":
        raise ValueError("Replay lacks terminated-worker lifecycle evidence")
    measured = manifest
    origin = "manifest measured fields"
    # EXP332's frozen implementation placed its actual RSS in summary.runtime,
    # rather than the manifest. Use that recorded measurement, never an assumed
    # pass or a smaller limit; keep all original files unchanged.
    if (spec.get("id") == "EXP-332-001" and manifest.get("process_peak_rss_bytes") is None
            and summary is not None):
        measured = {**manifest, "process_peak_rss_bytes": summary.get("runtime", {}).get("process_peak_rss_bytes")}
        origin = "EXP332 frozen summary.runtime.process_peak_rss_bytes; original measurement window"
    if not within_frozen_resources(measured, spec):
        raise ValueError("Replay resource envelope failed or measured fields are missing")
    return origin


def scientific_payload(experiment_id: str, name: str, payload):
    """Keep every scientific value; only EXP332's measured clocks/RSS vary.

    The frozen EXP332 specification explicitly separates timings from its
    deterministic calculation. Other archives retain exact payload comparison.
    """
    result = copy.deepcopy(payload)
    if experiment_id == 'EXP-332-001':
        if name == 'raw.json':
            for kernel in result[0]['kernels']:
                del kernel['build_seconds']
        elif name == 'summary.json':
            del result['runtime']
    return result


def replay(folder: Path) -> dict:
    with replay_directory(folder) as root:
        manifest = json.loads((folder / "manifest.json").read_text())
        for name, expected in manifest["outputs"].items():
            if hashlib.sha256((folder / name).read_bytes()).hexdigest() != expected:
                raise ValueError("Corrupted archived output: " + name)
        snapshot = json.loads(gzip.decompress((folder / "inputs.json.gz").read_bytes()))
        for relative, content in snapshot.items():
            target = root / relative
            if not target.resolve().is_relative_to(root.resolve()):
                raise ValueError("Unsafe snapshot path")
            if hashlib.sha256(content.encode()).hexdigest() != manifest["inputs"][relative]:
                raise ValueError("Corrupted archived source")
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content)
        env = dict(os.environ, PYTHONPATH=str(root / "src"), PYTHONDONTWRITEBYTECODE="1")
        spec = json.loads((root / "experiments/specs" / (manifest["experiment_id"] + ".json")).read_text())
        phase_watchdog = spec.get("phase_watchdog")
        command = ([sys.executable, "scripts/run_experiment_attempt.py", manifest["experiment_id"]]
                   if phase_watchdog else [sys.executable, "-m", "ai_value.cli", "experiment", manifest["experiment_id"]])
        timeout = (phase_watchdog["setup_seconds"] + spec["resource_limit_seconds"]
                   + phase_watchdog["archive_seconds"] + 60 if phase_watchdog else
                   max(150, spec.get("resource_limit_seconds", 120) + 60))
        process = subprocess.run(command, cwd=root, env=env, text=True, capture_output=True,
                                 timeout=timeout, check=True)
        new_manifest = json.loads(process.stdout)
        if phase_watchdog:
            if not new_manifest["target_completed"]:
                raise ValueError("Archived phase-watched target did not complete")
            new_manifest = json.loads((root / "experiments/runs" / new_manifest["run_id"] / "manifest.json").read_text())
        binding_matches = None
        if manifest.get("external_runtime_artifact"):
            binding_matches = (runtime_binding(manifest["stage_runtime_metrics"]["runtime_identity"])
                               == runtime_binding(new_manifest["stage_runtime_metrics"]["runtime_identity"]))
            if not binding_matches:
                raise ValueError("Actual external runtime source/binary binding differs")
        new_folder = root / "experiments/runs" / new_manifest["run_id"]
        matched = {}
        for name in ("raw.json", "summary.json"):
            def payload(base, name):
                packed = base / (name + ".gz")
                return json.loads(gzip.decompress(packed.read_bytes())) if packed.exists() else json.loads((base / name).read_text())
            matched[name] = (scientific_payload(manifest['experiment_id'], name, payload(folder, name))
                             == scientific_payload(manifest['experiment_id'], name, payload(new_folder, name)))
        if not all(matched.values()):
            raise ValueError("Replay differs: " + str(matched))
        resource_origin = require_replay_resources(new_manifest, spec, payload(new_folder, "summary.json"))
        result = {"run_id": manifest["run_id"], "replay_run_id": new_manifest["run_id"],
                "deterministic_outputs_match": matched,
                "comparison_scope": ("All exact inputs,outputs,risks,choices,judges and conclusions; only raw kernel build_seconds and summary runtime clocks/RSS excluded as preregistered"
                                     if manifest['experiment_id'] == 'EXP-332-001' else "Exact complete JSON payloads; no fields excluded"),
                "replay_resource_envelope_met": True,
                "recorded_worker_resource_flag": new_manifest.get('resource_envelope_met'),
                "replay_resource_measurement_source": resource_origin,
                "runtime": sys.version, "isolation": "temporary directory; " + ("pinned optional packages from caller runtime; " if manifest.get("requires_optional_runtime") else "standard library; ") + "no upstream clone or credentials"}
        if binding_matches is not None:
            result["external_runtime_source_binary_binding_matches"] = binding_matches
        return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("run_folder", type=Path)
    parser.add_argument("--receipt", type=Path)
    args = parser.parse_args()
    result = replay(args.run_folder.resolve())
    if args.receipt:
        args.receipt.parent.mkdir(parents=True, exist_ok=True)
        args.receipt.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(result, ensure_ascii=False, indent=2))
