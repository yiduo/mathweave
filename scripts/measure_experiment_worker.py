#!/usr/bin/env python3
"""Reap exactly one worker with wait4; no target imports in this supervisor."""
import json
import os
from pathlib import Path
import sys
import time
import traceback


def atomic(path, value):
    path = Path(path)
    temporary = path.with_suffix(".incomplete")
    temporary.write_text(json.dumps(value) + "\n")
    temporary.replace(path)


if __name__ == "__main__":
    if sys.platform not in {"darwin", "linux"}:
        raise RuntimeError("wait4 RSS units are not qualified on this platform")
    command = sys.argv[1:]
    if not command:
        raise ValueError("A worker command is required")
    pid = os.fork()
    if pid == 0:
        try:
            os.execvpe(command[0], command, os.environ)
        except BaseException:
            traceback.print_exc()
            os._exit(127)
    _, status, usage = os.wait4(pid, 0)
    ended = time.monotonic()
    raw = usage.ru_maxrss
    atomic(os.environ["MATHWEAVE_CHILD_USAGE_FILE"], {
        "worker_pid": pid, "worker_exit_code": os.waitstatus_to_exitcode(status),
        "raw": raw, "source_unit": "bytes" if sys.platform == "darwin" else "KiB",
        "bytes": raw if sys.platform == "darwin" else raw * 1024,
        "platform": sys.platform, "measurement": "os.wait4 for this exact terminated worker",
        "scope": "whole CLI worker lifecycle including final serialization/stdout; excludes supervisor and worker descendants",
        "worker_exited_monotonic": ended})
    phase = Path(os.environ["MATHWEAVE_PHASE_FILE"])
    previous = json.loads(phase.read_text()) if phase.exists() else {}
    history = previous.get("history", [])
    history.append({"phase": "worker_exited", "monotonic_started": ended})
    atomic(phase, {"phase": "worker_exited", "monotonic_started": ended, "history": history})
    code = os.waitstatus_to_exitcode(status)
    raise SystemExit(code if code >= 0 else 128 - code)
