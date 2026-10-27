"""Protocol error controls only. No target value, gradient or AD import."""
import gzip
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest
import importlib.util
import io
import tarfile
import shutil
import copy

from ai_value.ad_composite import checked_wheel
from ai_value.ad_composite import summarize
from ai_value.attempts import run_attempt, phase_timeout_reason
from ai_value.graph import diagnostic_execution_ids


class ADProtocolTests(unittest.TestCase):
    def test_diagnostic_execution_cannot_also_count_as_initial_or_component_check(self):
        diagnostic = {"kind": "connection", "properties": {"diagnostic_run_ids": ["UNIT-DIAG"], "run_ids": []}}
        self.assertEqual(diagnostic_execution_ids([diagnostic]), {"UNIT-DIAG"})
        for key in ("run_ids", "component_run_ids"):
            duplicate = {"kind": "connection", "properties": {key: ["UNIT-DIAG"]}}
            with self.assertRaises(ValueError):
                diagnostic_execution_ids([diagnostic, duplicate])
        with self.assertRaises(ValueError):
            diagnostic_execution_ids([{"kind": "claim", "properties": {"diagnostic_run_ids": ["UNIT-DIAG"]}}])

    def test_legacy_resource_adapter_requires_the_actual_frozen_summary_measurement(self):
        module = self.replay_module()
        manifest = {"resource_envelope_met": True, "elapsed_seconds": 0.1,
                    "peak_traced_python_bytes": 10}
        spec = {"id": "EXP-332-001", "resource_limit_seconds": 1,
                "resource_limit_mb": 64, "resource_limit_rss_mb": 128}
        with self.assertRaises(ValueError):
            module.require_replay_resources(manifest, spec)
        with self.assertRaises(ValueError):
            module.require_replay_resources(manifest, spec, {"runtime": {}})
        origin = module.require_replay_resources(manifest, spec,
                    {"runtime": {"process_peak_rss_bytes": 1024}})
        self.assertIn("frozen summary.runtime", origin)
        self.assertNotIn("process_peak_rss_bytes", manifest)

    def test_parent_finalizes_exact_child_usage_without_rewriting_cached_run(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for name in ("src/ai_value", "configs", "experiments/specs", "scripts"):
                (root / name).mkdir(parents=True)
            (root / "src/ai_value/__init__.py").write_text("# software only\n")
            (root / "configs/research.json").write_text("{}")
            shutil.copyfile(Path(__file__).resolve().parents[1] / "scripts/measure_experiment_worker.py",
                            root / "scripts/measure_experiment_worker.py")
            spec = {"id": "UNIT-FINALIZE", "resource_limit_seconds": 5, "resource_limit_mb": 64,
                    "resource_limit_rss_mb": 128,
                    "phase_watchdog": {"setup_seconds": 5, "archive_seconds": 5}}
            (root / "experiments/specs/UNIT-FINALIZE.json").write_text(json.dumps(spec))
            package = str(Path(__file__).resolve().parents[1] / "src")
            program = """import os,json,time,hashlib,sys
from pathlib import Path
sys.path.insert(0,SOURCE_PACKAGE)
from ai_value.attempts import set_execution_phase
set_execution_phase('calculation',time.monotonic())
p=Path('experiments/runs/UNIT-CONTENT');p.mkdir(parents=True)
body=b'{"software_only":true}';(p/'raw.json').write_bytes(body)
set_execution_phase('archive',time.monotonic())
m={'run_id':'UNIT-CONTENT','outputs':{'raw.json':hashlib.sha256(body).hexdigest()},
 'worker_pid':os.getpid(),'measurement_state':'awaiting_parent_child_lifecycle',
 'provisional_resource_envelope_met':True,'prediction_result_without_resource_gate':'passes_preregistered_prediction',
 'result':'awaiting_parent_child_lifecycle','resource_envelope_met':False,
 'elapsed_seconds':0.01,'peak_traced_python_bytes':1,'process_peak_rss_bytes':1}
(p/'manifest.json').write_text(json.dumps(m));print(json.dumps(m))
late_allocation=bytearray(16*1024*1024)
""".replace("SOURCE_PACKAGE", repr(package))
            first = run_attempt(root, spec["id"], command=[sys.executable, "-c", program])
            self.assertTrue(first["target_completed"])
            self.assertTrue(first["execution_qualified"])
            manifest = root / "experiments/runs/UNIT-CONTENT/manifest.json"
            saved = manifest.read_bytes()
            final = json.loads(saved)
            self.assertEqual(final["measurement_state"], "parent_child_lifecycle_finalized")
            self.assertEqual(final["process_rss_measurement"]["worker_pid"], first["child_lifecycle_usage"]["worker_pid"])
            program = "from pathlib import Path;print(Path('experiments/runs/UNIT-CONTENT/manifest.json').read_text())"
            second = run_attempt(root, spec["id"], command=[sys.executable, "-c", program])
            self.assertTrue(second["cached_run_reused_not_new_target_execution"])
            self.assertEqual(manifest.read_bytes(), saved)

    def replay_module(self):
        script = Path(__file__).resolve().parents[1] / "scripts/replay_run.py"
        loader = importlib.util.spec_from_file_location("software_replay_control", script)
        module = importlib.util.module_from_spec(loader)
        loader.loader.exec_module(module)
        return module

    def test_preflight_corruption_gets_a_durable_failure_receipt(self):
        module = self.replay_module()
        with tempfile.TemporaryDirectory() as tmp:
            original = Path(tmp) / "experiments/runs/UNIT-CORRUPT-REPLAY"
            original.mkdir(parents=True)
            (original / "raw.gz").write_bytes(b"software-only corrupt artifact")
            (original / "manifest.json").write_text(json.dumps({"outputs": {"raw.gz": "wrong"}}))
            with self.assertRaises(ValueError):
                module.replay(original)
            capsule = next((Path(tmp) / "experiments/replay-failures").glob("*/failure.tar.gz"))
            with tarfile.open(fileobj=io.BytesIO(gzip.decompress(capsule.read_bytes()))) as archive:
                hashes = json.loads(archive.extractfile("original-input-hashes-at-failure.json").read())
                self.assertEqual(hashes["raw.gz"]["sha256"], hashlib.sha256((original / "raw.gz").read_bytes()).hexdigest())

    def test_resource_failed_replay_is_rejected_and_retained_even_with_equal_values(self):
        module = self.replay_module()
        with tempfile.TemporaryDirectory() as tmp:
            original = Path(tmp) / "experiments/runs/UNIT-RESOURCE-REPLAY"
            original.mkdir(parents=True)
            with self.assertRaises(ValueError):
                with module.replay_directory(original) as isolated:
                    (isolated / "equal-values.json").write_text('{"software_only":"values_equal"}')
                    module.require_replay_resources({"resource_envelope_met": False},
                        {"resource_limit_seconds": 1, "resource_limit_mb": 64})
            capsule = next((Path(tmp) / "experiments/replay-failures").glob("*/failure.tar.gz"))
            with tarfile.open(fileobj=io.BytesIO(gzip.decompress(capsule.read_bytes()))) as archive:
                self.assertIn(b"values_equal", archive.extractfile("equal-values.json").read())

    def test_finalization_allocation_is_in_terminated_worker_rss(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for name in ("src/ai_value", "configs", "experiments/specs", "scripts"):
                (root / name).mkdir(parents=True)
            (root / "src/ai_value/__init__.py").write_text("# software only\n")
            (root / "configs/research.json").write_text("{}")
            shutil.copyfile(Path(__file__).resolve().parents[1] / "scripts/measure_experiment_worker.py",
                            root / "scripts/measure_experiment_worker.py")
            spec = {"id": "UNIT-LIFECYCLE-RSS", "resource_limit_seconds": 5,
                    "resource_limit_mb": 64, "phase_watchdog": {"setup_seconds": 5, "archive_seconds": 5}}
            (root / "experiments/specs/UNIT-LIFECYCLE-RSS.json").write_text(json.dumps(spec))
            package = str(Path(__file__).resolve().parents[1] / "src")
            program = ("import sys,time;sys.path.insert(0," + repr(package) + ");"
                       "from ai_value.attempts import set_execution_phase;"
                       "set_execution_phase('calculation',time.monotonic());"
                       "set_execution_phase('archive',time.monotonic());"
                       "late_allocation=bytearray(32*1024*1024);print('software-only-not-a-manifest')")
            result = run_attempt(root, spec["id"], command=[sys.executable, "-c", program])
            self.assertFalse(result["target_completed"])
            self.assertGreaterEqual(result["child_lifecycle_usage"]["bytes"], 32 * 1024 * 1024)
            self.assertEqual(result["child_lifecycle_usage"]["worker_exit_code"], 0)
            self.assertIsNone(result["terminal_phase_violation"])

    def test_invalid_or_missing_judges_cannot_publish_baseline_sufficiency(self):
        observed = {k: {"classification": "finite", "score": {"within_tolerance": True}}
                    for k in ("value", "dr", "dz")}
        row = {"index": 0, "n": 99, "z": "1", "judge_checks": {"software_control": False},
               "methods": {"naive_factored": copy.deepcopy(observed),
                           "old_preoperation_branch": copy.deepcopy(observed)}}
        for rows, count in (([], 1), ([row], 1), ([{**row, "judge_checks": {"software_control": True}}], 2)):
            outcome = summarize(rows, count)
            self.assertFalse(outcome["meets_prediction"])
            self.assertIsNone(outcome["old_correct_branch_suffices"])
            self.assertTrue(all(v is None for v in outcome["primary_conjuncts"].values()))

    def test_completed_stage_overruns_are_not_lost_on_transition_or_exit(self):
        spec = {"resource_limit_seconds": 1, "phase_watchdog": {"setup_seconds": 1, "archive_seconds": 1}}
        phase = {"phase": "calculation", "monotonic_started": 12,
                 "history": [{"phase": "calculation", "monotonic_started": 12}]}
        self.assertEqual(phase_timeout_reason(phase, 2.1, 12.1, spec), "setup")
        phase = {"phase": "worker_exited", "monotonic_started": 12.3,
                 "history": [{"phase": "calculation", "monotonic_started": 10.2},
                             {"phase": "archive", "monotonic_started": 10.3},
                             {"phase": "worker_exited", "monotonic_started": 12.3}]}
        self.assertEqual(phase_timeout_reason(phase, 2.4, 12.4, spec), "archive")
    def test_replay_failure_survives_temporary_workspace_removal(self):
        script = Path(__file__).resolve().parents[1] / "scripts/replay_run.py"
        loader = importlib.util.spec_from_file_location("software_replay_control", script)
        module = importlib.util.module_from_spec(loader)
        loader.loader.exec_module(module)
        with tempfile.TemporaryDirectory() as tmp:
            original = Path(tmp) / "experiments/runs/UNIT-REPLAY-FAILURE"
            original.mkdir(parents=True)
            with self.assertRaises(RuntimeError):
                with module.replay_directory(original) as isolated:
                    (isolated / "software-only.txt").write_text("partial software evidence")
                    raise RuntimeError("intentional replay software control")
            self.assertFalse(isolated.exists())
            capsule = next((Path(tmp) / "experiments/replay-failures").glob("*/failure.tar.gz"))
            with tarfile.open(fileobj=io.BytesIO(gzip.decompress(capsule.read_bytes()))) as archive:
                self.assertEqual(archive.extractfile("software-only.txt").read(), b"partial software evidence")
                self.assertIn(b"intentional replay software control", archive.extractfile("replay-error.txt").read())

    def test_tampered_runtime_artifact_is_rejected_before_import(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "software-only.whl"
            path.write_bytes(b"original software-only artifact")
            wanted = hashlib.sha256(path.read_bytes()).hexdigest()
            self.assertEqual(checked_wheel(path, wanted), path.resolve())
            path.write_bytes(b"changed software-only artifact")
            with self.assertRaises(ValueError):
                checked_wheel(path, wanted)

    def phase_control(self, phase):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "src/ai_value").mkdir(parents=True)
            (root / "src/ai_value/__init__.py").write_text("# software control\n")
            (root / "configs").mkdir()
            (root / "configs/research.json").write_text("{}")
            (root / "experiments/specs").mkdir(parents=True)
            (root / "scripts").mkdir()
            shutil.copyfile(Path(__file__).resolve().parents[1] / "scripts/measure_experiment_worker.py",
                            root / "scripts/measure_experiment_worker.py")
            spec = {"id": "UNIT-AD-WATCHDOG", "resource_limit_seconds": 0.15,
                    "resource_limit_mb": 64,
                    "phase_watchdog": {"setup_seconds": 0.15, "archive_seconds": 0.15}}
            (root / "experiments/specs/UNIT-AD-WATCHDOG.json").write_text(json.dumps(spec))
            package = str(Path(__file__).resolve().parents[1] / "src")
            script = ("import sys,time;sys.path.insert(0," + repr(package) + ");"
                      "from ai_value.attempts import record_progress,set_execution_phase;"
                      "record_progress({'software_only':'before-intentional-timeout'});")
            if phase:
                script += "set_execution_phase(" + repr(phase) + ",time.monotonic());"
            script += "time.sleep(5)"
            record = run_attempt(root, spec["id"], command=[sys.executable, "-c", script])
            self.assertTrue(record["timed_out"])
            self.assertFalse(record["target_completed"])
            self.assertEqual(record["watchdog_expired_phase"], phase or "setup")
            folder = root / "experiments/attempts" / record["attempt_id"]
            self.assertEqual(len(record["progress"]), 1)
            self.assertTrue(record["progress"][0]["gzip_json_valid"])
            if phase:
                self.assertFalse((folder / "phase.json").exists())
                self.assertEqual(json.loads(gzip.decompress((folder / "phase.json.gz").read_bytes()))["phase"], phase)
            self.assertTrue((folder / "source.json.gz").is_file())
            self.assertFalse(record["scientific_credit"])

    def test_live_calculation_timeout_preserves_partial_evidence(self):
        self.phase_control("calculation")

    def test_live_setup_timeout_preserves_partial_evidence(self):
        self.phase_control(None)

    def test_live_archive_timeout_preserves_partial_evidence(self):
        self.phase_control("archive")
