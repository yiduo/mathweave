"""Replay-control tests with explicitly synthetic software fixtures, no science credit."""
import gzip
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import sys
import tarfile
import tempfile
import unittest


def controller():
    path = Path(__file__).resolve().parents[1] / "scripts/replay_run.py"
    spec = importlib.util.spec_from_file_location("replay_diagnostic_control", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ReplayDiagnosticTests(unittest.TestCase):
    def test_comparison_preview_is_bounded_and_does_not_relax_equality(self):
        module = controller()
        left = {"escaped/~": [1, None], "gone": None, "same": 1}
        right = {"escaped/~": [2, None, 3], "added": None, "same": 1.0}
        report = module.payload_differences(left, right, preview_limit=2)
        self.assertEqual(report["different_positions"], 4)
        self.assertEqual(len(report["preview"]), 2)
        self.assertTrue(report["preview_truncated"])
        full = module.payload_differences(left, right)
        self.assertEqual({e["path"] for e in full["preview"]},
                         {"/added", "/gone", "/escaped~1~0/0", "/escaped~1~0/2"})
        self.assertEqual(module.payload_differences(left, left)["different_positions"], 0)
        self.assertEqual(module.payload_differences(left, right, 0)["preview"], [])

    def test_real_mismatching_worker_retains_comparison_and_complete_outputs(self):
        module = controller()
        with tempfile.TemporaryDirectory() as temporary:
            folder = Path(temporary) / "experiments/runs/UNIT-REPLAY-DIFF"
            folder.mkdir(parents=True)
            spec = {"id": "UNIT-REPLAY-DIFF", "resource_limit_seconds": 2,
                    "resource_limit_mb": 64}
            # Executes in a real isolated subprocess. This is a software-only
            # mismatch, not an experiment or numerical application validation.
            program = '''import gzip,json,sys
from pathlib import Path
p=Path("experiments/runs/UNIT-OUTPUT");p.mkdir(parents=True)
(p/"raw.json.gz").write_bytes(gzip.compress(json.dumps({"value":2.0000000000000004}).encode(),mtime=0))
(p/"summary.json.gz").write_bytes(gzip.compress(b'{"software_only":true}',mtime=0))
m={"run_id":"UNIT-OUTPUT","elapsed_seconds":0.01,"peak_traced_python_bytes":1024,"resource_envelope_met":True}
(p/"manifest.json").write_text(json.dumps(m))
print("synthetic worker stderr",file=sys.stderr)
print(json.dumps(m))
'''
            inputs = {"src/ai_value/__init__.py": "",
                      "src/ai_value/cli.py": program,
                      "experiments/specs/UNIT-REPLAY-DIFF.json": json.dumps(spec)}
            outputs = {"raw.json.gz": b'{"value":2.0}',
                       "summary.json.gz": b'{"software_only":true}'}
            for name, raw in outputs.items():
                (folder / name).write_bytes(gzip.compress(raw, mtime=0))
            (folder / "inputs.json.gz").write_bytes(gzip.compress(json.dumps(inputs).encode(), mtime=0))
            manifest = {"run_id": folder.name, "experiment_id": spec["id"],
                        "inputs": {k: hashlib.sha256(v.encode()).hexdigest() for k, v in inputs.items()},
                        "outputs": {k: hashlib.sha256((folder / k).read_bytes()).hexdigest() for k in outputs}}
            (folder / "manifest.json").write_text(json.dumps(manifest))
            before = {p.name: p.read_bytes() for p in folder.iterdir()}
            with self.assertRaisesRegex(ValueError, "Replay differs"):
                module.replay(folder)
            self.assertEqual(before, {p.name: p.read_bytes() for p in folder.iterdir()})
            target = next((Path(temporary) / "experiments/replay-failures").iterdir())
            packed = (target / "failure.tar.gz").read_bytes()
            receipt = json.loads((target / "receipt.json").read_text())
            self.assertEqual(hashlib.sha256(packed).hexdigest(), receipt["archive_sha256"])
            with tarfile.open(fileobj=io.BytesIO(gzip.decompress(packed))) as archive:
                for name, digest in receipt["members"].items():
                    self.assertEqual(hashlib.sha256(archive.extractfile(name).read()).hexdigest(), digest)
                report = json.loads(archive.extractfile("replay-comparison.json").read())
                self.assertEqual(report["deterministic_outputs_match"],
                                 {"raw.json": False, "summary.json": True})
                self.assertTrue(report["comparison_rule_unchanged"])
                diff = report["differences"]["raw.json"]
                self.assertEqual(diff["different_positions"], 1)
                self.assertEqual(diff["preview"][0]["path"], "/value")
                self.assertEqual(diff["preview"][0]["actual"]["hex"], (2.0000000000000004).hex())
                self.assertEqual(report["runtime"], sys.version)
                self.assertIn(b"synthetic worker stderr", archive.extractfile("replay-worker.stderr.log").read())
                self.assertEqual(json.loads(archive.extractfile("replay-worker.stdout.log").read())["run_id"], "UNIT-OUTPUT")
                actual = json.loads(gzip.decompress(archive.extractfile("experiments/runs/UNIT-OUTPUT/raw.json.gz").read()))
                self.assertEqual(actual["value"], 2.0000000000000004)
