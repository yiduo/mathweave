"""Fresh-process attempts and crash evidence; never application-validity evidence."""
from __future__ import annotations

import gzip
import hashlib
import json
import math
import os
import platform
import signal
from pathlib import Path
import subprocess
import sys
import time
import traceback
import uuid
from datetime import datetime, timezone


def packed_json(path: Path, value) -> dict:
    raw = (json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode()
    packed = gzip.compress(raw, mtime=0)
    assert gzip.decompress(packed) == raw
    path.write_bytes(packed)
    return {"sha256": hashlib.sha256(packed).hexdigest(),
            "uncompressed_sha256": hashlib.sha256(raw).hexdigest()}


def rss_metadata(observed: int, system: str) -> dict:
    if system not in {"darwin", "linux"}:
        raise RuntimeError("RSS units not qualified for platform " + system)
    return {"raw": observed, "source_unit": "bytes" if system == "darwin" else "KiB",
            "bytes": observed if system == "darwin" else observed * 1024,
            "platform": system, "scope": "whole-process lifecycle high-water; excludes children"}


def peak_process_rss() -> dict:
    import resource
    return rss_metadata(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss, sys.platform)


def within_frozen_resources(manifest: dict, spec: dict) -> bool:
    """Validate measured limits, including legacy receipts without a verdict.

    Missing requested RSS never inherits a pass. An explicit failed verdict
    also cannot be replaced with a recalculation of only some of its limits.
    """
    if manifest.get("resource_envelope_met") is False:
        return False
    limits = [("elapsed_seconds", spec["resource_limit_seconds"]),
              ("peak_traced_python_bytes", spec["resource_limit_mb"]*1024**2)]
    if spec.get("resource_limit_rss_mb"):
        limits.append(("process_peak_rss_bytes", spec["resource_limit_rss_mb"]*1024**2))
    for key, limit in limits:
        measured = manifest.get(key)
        if not isinstance(measured,(int,float)) or not math.isfinite(measured) or not 0 <= measured <= limit:
            return False
    return True


_progress_index = 0


def record_progress(value) -> None:
    """Independent gzip members survive a later worker exception or signal."""
    global _progress_index
    name = os.environ.get("MATHWEAVE_ATTEMPT_DIR")
    if not name:
        return  # Archived scientific replay needs no new attempt journal.
    folder = Path(name) / "progress"
    folder.mkdir(exist_ok=True)
    target = folder / ("row-%06d.json.gz" % _progress_index)
    if target.exists():
        raise FileExistsError("Progress is append-only: " + str(target))
    temporary = target.with_suffix(target.suffix + ".incomplete")
    raw = (json.dumps(value, ensure_ascii=False, sort_keys=True) + "\n").encode()
    packed = gzip.compress(raw, mtime=0)
    assert gzip.decompress(packed) == raw
    with temporary.open("xb") as stream:
        stream.write(packed)
        stream.flush()
        os.fsync(stream.fileno())
    temporary.rename(target)
    _progress_index += 1


def set_execution_phase(phase: str, monotonic_started: float) -> None:
    """Single atomic clock signal for a parent watchdog, not scientific data."""
    name = os.environ.get("MATHWEAVE_PHASE_FILE")
    if not name:
        return
    path = Path(name)
    previous = json.loads(path.read_text()) if path.exists() else {}
    history = previous.get("history", [])
    history.append({"phase": phase, "monotonic_started": monotonic_started})
    temporary = path.with_suffix(".incomplete")
    temporary.write_text(json.dumps({"phase": phase, "monotonic_started": monotonic_started,
                                     "history": history}) + "\n")
    temporary.replace(path)


def phase_timeout_reason(phase, elapsed_since_launch, now, spec):
    """Return an expired frozen stage; malformed clock signals fail closed."""
    limits = spec["phase_watchdog"]
    if phase is None:
        return "setup" if elapsed_since_launch > limits["setup_seconds"] else None
    if (not isinstance(phase, dict) or phase.get("phase") not in {"calculation", "archive", "worker_exited"}
            or not isinstance(phase.get("monotonic_started"), (int, float))
            or not math.isfinite(phase["monotonic_started"])
            or phase["monotonic_started"] > now):
        return "invalid_phase_clock"
    history = phase.get("history", [{"phase": phase["phase"],
                                      "monotonic_started": phase["monotonic_started"]}])
    launch = now - elapsed_since_launch
    prior_name, prior_started = "setup", launch
    for item in history:
        name, started = item.get("phase"), item.get("monotonic_started")
        if (name not in {"calculation", "archive", "worker_exited"}
                or not isinstance(started, (int, float)) or not math.isfinite(started)
                or started < prior_started or started > now):
            return "invalid_phase_clock"
        limit = spec["resource_limit_seconds"] if prior_name == "calculation" else limits[prior_name + "_seconds"]
        if started - prior_started > limit:
            return prior_name
        prior_name, prior_started = name, started
    if prior_name == "worker_exited":
        return None
    limit = spec["resource_limit_seconds"] if prior_name == "calculation" else limits[prior_name + "_seconds"]
    return prior_name if now - prior_started > limit else None


def run_attempt(root: Path, experiment_id: str, *, command=None, timeout=None) -> dict:
    """Retain source, stderr and progress even when a worker cannot return a run.

    The optional command is used by software-only failure-path tests. Those
    tests have temporary UNIT IDs and do not enter the research graph.
    """
    started = time.perf_counter()
    root = root.resolve()
    spec_path = root / "experiments/specs" / (experiment_id + ".json")
    spec = json.loads(spec_path.read_text())
    names = [spec_path, root / "configs/research.json"]
    names += sorted((root / "src/ai_value").glob("*.py"))
    names += [root / p for p in spec.get("additional_source_paths", [])]
    wrapper = root / "scripts/run_experiment_attempt.py"
    if wrapper.exists():
        names.append(wrapper)
    baseline = root / "data/corpus/baseline.json"
    if baseline.exists():
        names.append(baseline)
    if any(not p.resolve().is_relative_to(root) or not p.is_file() for p in names):
        raise ValueError("Invalid source snapshot path")
    snapshot = {str(p.relative_to(root)): p.read_text() for p in names}
    hashes = {name: hashlib.sha256(text.encode()).hexdigest() for name, text in snapshot.items()}
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    folder = root / "experiments/attempts" / (experiment_id + "-" + stamp + "-" + uuid.uuid4().hex[:8])
    folder.mkdir(parents=True, exist_ok=False)
    snapshot_hashes = packed_json(folder / "source.json.gz", snapshot)
    cmd = command or [sys.executable, "-m", "ai_value.cli", "experiment", experiment_id]
    record = {"experiment_id": experiment_id, "attempt_id": folder.name,
              "started_utc": datetime.now(timezone.utc).isoformat(), "state": "prepared",
              "command": cmd, "source_hashes": hashes, "snapshot": snapshot_hashes,
              "python": sys.version, "platform": platform.platform(),
              "target_completed": False, "scientific_credit": False}
    (folder / "attempt.json").write_text(json.dumps(record, indent=2) + "\n")
    env = dict(os.environ, PYTHONPATH=str(root / "src"), PYTHONDONTWRITEBYTECODE="1",
               MATHWEAVE_ATTEMPT_DIR=str(folder))
    if spec.get("phase_watchdog"):
        env["MATHWEAVE_PHASE_FILE"] = str(folder / "phase.json")
        env["MATHWEAVE_CHILD_USAGE_FILE"] = str(folder / "child-usage.json")
    prepared = time.perf_counter()
    timed_out = False
    returncode = None
    process = None
    launched_monotonic = None
    observer_command = cmd
    if spec.get("phase_watchdog"):
        supervisor = root / "scripts/measure_experiment_worker.py"
        if not supervisor.is_file():
            raise ValueError("Phase-watched worker requires its frozen wait4 supervisor")
        observer_command = [sys.executable, str(supervisor), *cmd]
        record["observer_command"] = observer_command
    try:
        launched_monotonic = time.monotonic()
        process = subprocess.Popen(observer_command, cwd=root, env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                   start_new_session=bool(spec.get("phase_watchdog")))
        record.update(state="running", worker_pid=process.pid if not spec.get("phase_watchdog") else None)
        if spec.get("phase_watchdog"):
            record["supervisor_pid"] = process.pid
        (folder / "attempt.json").write_text(json.dumps(record, indent=2) + "\n")
        try:
            if spec.get("phase_watchdog") and timeout is None:
                launched = launched_monotonic
                while True:
                    try:
                        stdout, stderr = process.communicate(timeout=0.1)
                        break
                    except subprocess.TimeoutExpired:
                        phase_path = folder / "phase.json"
                        try:
                            phase = json.loads(phase_path.read_text()) if phase_path.exists() else None
                        except (OSError, ValueError):
                            phase = {"phase": "invalid"}
                        expired = phase_timeout_reason(phase, time.monotonic() - launched,
                                                       time.monotonic(), spec)
                        if expired:
                            record["watchdog_expired_phase"] = expired
                            raise
            else:
                stdout, stderr = process.communicate(timeout=timeout or spec["resource_limit_seconds"] + 60)
        except subprocess.TimeoutExpired:
            timed_out = True
            if spec.get("phase_watchdog"):
                try:
                    os.killpg(process.pid, signal.SIGKILL)
                except ProcessLookupError:
                    pass
            else:
                process.kill()
            stdout, stderr = process.communicate()
        returncode = process.returncode
    except Exception:
        error = traceback.format_exc().encode()
        stdout, stderr = b"", b""
        if process is not None:
            try:
                if spec.get("phase_watchdog"):
                    try:
                        os.killpg(process.pid, signal.SIGKILL)
                    except ProcessLookupError:
                        pass
                else:
                    process.kill()
                stdout, stderr = process.communicate()
            except Exception:
                stderr += traceback.format_exc().encode()
            returncode = process.returncode
        stderr += error
        record["worker_launch_or_communication_error"] = True
    child_finished = time.perf_counter()
    phase_path = folder / "phase.json"
    phase_value = None
    if phase_path.exists():
        phase = phase_path.read_bytes()
        try:
            phase_value = json.loads(phase)
        except ValueError:
            phase_value = {"phase": "invalid"}
        packed = gzip.compress(phase, mtime=0)
        assert gzip.decompress(packed) == phase
        (folder / "phase.json.gz").write_bytes(packed)
        phase_path.unlink()
        record["phase_clock_evidence"] = {"sha256": hashlib.sha256(packed).hexdigest(),
                                          "uncompressed_sha256": hashlib.sha256(phase).hexdigest()}
    if spec.get("phase_watchdog") and launched_monotonic is not None:
        expired = phase_timeout_reason(phase_value, time.monotonic() - launched_monotonic,
                                       time.monotonic(), spec)
        record["terminal_phase_violation"] = expired
        record["stage_history"] = phase_value.get("history", []) if isinstance(phase_value, dict) else []
    usage_path = folder / "child-usage.json"
    lifecycle_usage = None
    if usage_path.exists():
        raw_usage = usage_path.read_bytes()
        lifecycle_usage = json.loads(raw_usage)
        packed = gzip.compress(raw_usage, mtime=0)
        assert gzip.decompress(packed) == raw_usage
        (folder / "child-usage.json.gz").write_bytes(packed)
        usage_path.unlink()
        record["child_lifecycle_usage"] = lifecycle_usage
        record["worker_pid"] = lifecycle_usage["worker_pid"]
    logs = {}
    for name, raw in (("stdout", stdout), ("stderr", stderr)):
        packed = gzip.compress(raw, mtime=0)
        assert gzip.decompress(packed) == raw
        (folder / (name + ".log.gz")).write_bytes(packed)
        logs[name] = {"sha256": hashlib.sha256(packed).hexdigest(),
                      "uncompressed_sha256": hashlib.sha256(raw).hexdigest(), "bytes": len(raw)}
    progress = []
    for path in sorted((folder / "progress").glob("*")):
        data = path.read_bytes()
        row = {"path": str(path.relative_to(folder)), "sha256": hashlib.sha256(data).hexdigest()}
        try:
            raw = gzip.decompress(data)
            json.loads(raw)
            row.update(gzip_json_valid=True, uncompressed_sha256=hashlib.sha256(raw).hexdigest())
        except Exception as exc:
            row.update(gzip_json_valid=False, error=repr(exc))
        progress.append(row)  # An interrupted member is retained, never discarded.
    unchanged = all((root / n).is_file() and hashlib.sha256((root / n).read_bytes()).hexdigest() == h
                    for n, h in hashes.items())
    record.update(state="worker_exited", worker_exit_code=returncode, timed_out=timed_out,
                  preparation_seconds=prepared-started, worker_wall_seconds=child_finished-prepared,
                  log_and_evidence_archive_seconds=time.perf_counter()-child_finished,
                  end_to_end_seconds=time.perf_counter()-started, logs=logs, progress=progress,
                  source_hashes_unchanged=unchanged, finished_utc=datetime.now(timezone.utc).isoformat())
    if returncode == 0 and unchanged:
        try:
            manifest = json.loads(stdout)
            run_folder = root / "experiments/runs" / manifest["run_id"]
            if not run_folder.resolve().is_relative_to((root / "experiments/runs").resolve()):
                raise ValueError("Invalid run directory")
            if json.loads((run_folder / "manifest.json").read_text()) != manifest:
                raise ValueError("Printed and saved manifests differ")
            for name, expected in manifest["outputs"].items():
                if hashlib.sha256((run_folder / name).read_bytes()).hexdigest() != expected:
                    raise ValueError("Changed worker output: " + name)
            if spec.get("phase_watchdog"):
                if manifest.get("measurement_state") == "awaiting_parent_child_lifecycle":
                    if not lifecycle_usage or manifest.get("worker_pid") != lifecycle_usage["worker_pid"]:
                        raise ValueError("Cannot bind terminated-worker usage to provisional run")
                    packed_json(folder / "worker-manifest-before-lifecycle.json.gz", manifest)
                    manifest["worker_rss_before_final_serialization"] = manifest.get("process_rss_measurement")
                    manifest["process_peak_rss_bytes"] = lifecycle_usage["bytes"]
                    manifest["process_rss_measurement"] = lifecycle_usage
                    manifest["measurement_state"] = "parent_child_lifecycle_finalized"
                    manifest["rss_measurement_timing"] = "Supervisor os.wait4 after exact CLI worker termination"
                    manifest["stage_history"] = record["stage_history"]
                    manifest["terminal_phase_violation"] = record["terminal_phase_violation"]
                    checked = {**manifest, "resource_envelope_met": True}
                    envelope = (manifest["provisional_resource_envelope_met"]
                                and not record.get("watchdog_expired_phase")
                                and not record["terminal_phase_violation"]
                                and within_frozen_resources(checked, spec))
                    manifest["resource_envelope_met"] = bool(envelope)
                    manifest["result"] = (manifest["prediction_result_without_resource_gate"] if envelope
                                          else "resource_envelope_exceeded")
                    (run_folder / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
                elif manifest.get("measurement_state") == "parent_child_lifecycle_finalized":
                    record["cached_run_reused_not_new_target_execution"] = True
                else:
                    raise ValueError("Phase-watched run lacks complete lifecycle measurement state")
                record["execution_qualified"] = within_frozen_resources(manifest, spec)
            record["run_id"] = manifest["run_id"]
            record["run_result"] = manifest["result"]
            record["target_completed"] = True
        except (OSError, ValueError, KeyError, TypeError) as exc:
            record["manifest_error"] = repr(exc)
    (folder / "attempt.json").write_text(json.dumps(record, indent=2) + "\n")
    return record
