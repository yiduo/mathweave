#!/usr/bin/env python3
"""Run one preregistered experiment in a fresh worker and retain crash evidence."""
from pathlib import Path
import argparse
import json
import sys

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))
from ai_value.attempts import run_attempt

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("experiment_id")
    args = parser.parse_args()
    receipt = run_attempt(root, args.experiment_id)
    print(json.dumps(receipt, ensure_ascii=False, indent=2))
    raise SystemExit(0 if receipt["target_completed"] and receipt.get("execution_qualified", True) else 1)
