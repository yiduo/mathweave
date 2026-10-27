"""Software-only resource/crash controls, not scientific-validation fixtures."""
import gzip
import json
from pathlib import Path
import sys
import tempfile
import unittest

from ai_value.attempts import rss_metadata, run_attempt, within_frozen_resources
from ai_value.experiments import RUNNERS, run
from ai_value.receiver_audit import MatrixAudit


class AttemptTests(unittest.TestCase):
    def test_legacy_measurements_and_new_requested_rss_are_distinct(self):
        spec = {"resource_limit_seconds":60,"resource_limit_mb":64}
        old = {"elapsed_seconds":0.5,"peak_traced_python_bytes":500000}
        self.assertTrue(within_frozen_resources(old,spec))
        self.assertFalse(within_frozen_resources(old,{**spec,"resource_limit_rss_mb":64}))
        self.assertFalse(within_frozen_resources({**old,"resource_envelope_met":False},spec))
        self.assertFalse(within_frozen_resources({**old,"elapsed_seconds":61},spec))

    def make_root(self, folder, name, rss=None):
        root = Path(folder)
        (root / "experiments/specs").mkdir(parents=True)
        (root / "configs").mkdir()
        (root / "src/ai_value").mkdir(parents=True)
        (root / "src/ai_value/__init__.py").write_text("# software unit control\n")
        (root / "configs/research.json").write_text("{}")
        spec = {"id": name, "resource_limit_seconds": 5, "resource_limit_mb": 64}
        if rss is not None:
            spec["resource_limit_rss_mb"] = rss
        (root / ("experiments/specs/"+name+".json")).write_text(json.dumps(spec))
        return root

    def test_rss_units_are_explicit_and_unknown_units_rejected(self):
        self.assertEqual(rss_metadata(123, "darwin")["bytes"], 123)
        self.assertEqual(rss_metadata(123, "linux")["bytes"], 123*1024)
        with self.assertRaises(RuntimeError):
            rss_metadata(123, "unqualified")

    def test_real_failed_worker_preserves_progress_stderr_and_source(self):
        with tempfile.TemporaryDirectory() as folder:
            root = self.make_root(folder,"UNIT-CRASH-CONTROL")
            package = str(Path(__file__).resolve().parents[1] / "src")
            program = ("import sys;sys.path.insert(0,"+repr(package)+");"
                       "from ai_value.attempts import record_progress;"
                       "record_progress({'kind':'software-only-control','value':7});"
                       "raise RuntimeError('intentional software failure control')")
            receipt = run_attempt(root,"UNIT-CRASH-CONTROL",command=[sys.executable,"-c",program])
            self.assertNotEqual(receipt["worker_exit_code"],0)
            self.assertFalse(receipt["target_completed"])
            self.assertFalse(receipt["scientific_credit"])
            self.assertTrue(receipt["source_hashes_unchanged"])
            self.assertEqual(len(receipt["progress"]),1)
            attempt = root / "experiments/attempts" / receipt["attempt_id"]
            self.assertIn(b"intentional software failure control",gzip.decompress((attempt/"stderr.log.gz").read_bytes()))
            self.assertTrue(receipt["progress"][0]["gzip_json_valid"])
            source = json.loads(gzip.decompress((attempt/"source.json.gz").read_bytes()))
            self.assertIn("experiments/specs/UNIT-CRASH-CONTROL.json",source)

    def test_measured_rss_violation_overrides_positive_dummy_prediction(self):
        # This deliberately tiny cap tests the framework, never the GAD claim.
        with tempfile.TemporaryDirectory() as folder:
            root = self.make_root(folder,"UNIT-RESOURCE-CONTROL",rss=0.000001)
            RUNNERS["UNIT-RESOURCE-CONTROL"] = lambda spec: ([{"software_only":True}], {"meets_prediction":True})
            try:
                manifest = run(root,"UNIT-RESOURCE-CONTROL")
            finally:
                del RUNNERS["UNIT-RESOURCE-CONTROL"]
            self.assertGreater(manifest["process_peak_rss_bytes"],0)
            self.assertIn("whole-process",manifest["memory_scope"])
            self.assertIn(manifest["process_rss_measurement"]["source_unit"],{"bytes","KiB"})
            self.assertFalse(manifest["resource_envelope_met"])
            self.assertEqual(manifest["result"],"resource_envelope_exceeded")
            archive = root/"experiments/runs"/manifest["run_id"]
            self.assertTrue(json.loads(gzip.decompress((archive/"summary.json.gz").read_bytes()))["meets_prediction"])

    def test_endpoint_allowance_records_clipping_and_rejects_large_overruns(self):
        audit = MatrixAudit()
        x = 1+1e-13
        self.assertEqual(audit.endpoint(x,0.0,1.0,"software-control"),1.0)
        self.assertEqual(audit.clamps[0]["raw"],x)
        with self.assertRaises(ArithmeticError):
            audit.endpoint(1.1,0.0,1.0,"software-control")
        with self.assertRaises(ArithmeticError):
            audit.endpoint(float("nan"),0.0,1.0,"software-control")

    def test_zero_exit_without_saved_evidence_is_not_completed(self):
        with tempfile.TemporaryDirectory() as folder:
            root = self.make_root(folder,"UNIT-FALSE-RECEIPT")
            program = "print('{\"run_id\":\"nonexistent\",\"result\":\"passes_preregistered_prediction\"}')"
            receipt = run_attempt(root,"UNIT-FALSE-RECEIPT",command=[sys.executable,"-c",program])
            self.assertEqual(receipt["worker_exit_code"],0)
            self.assertFalse(receipt["target_completed"])
            self.assertIn("manifest_error",receipt)
