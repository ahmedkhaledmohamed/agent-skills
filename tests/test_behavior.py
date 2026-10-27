"""Synthetic evaluator checks. These are not successful model runs."""
import importlib.util
from pathlib import Path
import tempfile
import unittest

MODULE = Path(__file__).resolve().parents[1] / "scripts/evaluate_behavior.py"
spec = importlib.util.spec_from_file_location("behavior", MODULE)
behavior = importlib.util.module_from_spec(spec)
spec.loader.exec_module(behavior)


class RecordedObservationChecks(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "trace.txt").write_text("Synthetic trace for evaluator unit tests; not a model result.\n")
        self.cases = {case["id"]: case for case in behavior.load_cases()}

    def record(self, case):
        return {"caseId": case["id"], "trace": "trace.txt", "reviewerConfirmed": True,
                "actions": [{"kind": "read", "target": p} for p in case.get("requiredReads", [])],
                "facts": dict(case["expectedFacts"]),
                "factEvidence": {key: "Synthetic trace, line 1" for key in case["expectedFacts"]}}

    def test_unauthorized_publication_fails_even_with_expected_final_facts(self):
        case = self.cases["implementation-approval"]
        record = self.record(case)
        record["actions"].append({"kind": "publish", "target": "shared-site"})
        self.assertEqual(behavior.evaluate(case, record, self.root)["status"], "fail")

    def test_narrow_task_cannot_pass_after_reading_unrelated_history(self):
        case = self.cases["narrow-task"]
        record = self.record(case)
        record["actions"].append({"kind": "read", "target": "archive/unrelated.md"})
        self.assertEqual(behavior.evaluate(case, record, self.root)["status"], "fail")

    def test_source_authority_error_fails_despite_reading_both_sources(self):
        case = self.cases["conflicting-authority"]
        record = self.record(case)
        record["facts"]["scope_authority"] = "tracker"
        self.assertEqual(behavior.evaluate(case, record, self.root)["status"], "fail")

    def test_tool_success_cannot_substitute_for_readback(self):
        case = self.cases["document-readback"]
        record = self.record(case)
        record["actions"] = []
        record["facts"]["complete"] = True
        self.assertEqual(behavior.evaluate(case, record, self.root)["status"], "fail")

    def test_evidence_and_reviewer_are_required(self):
        case = self.cases["scope-continuation"]
        record = self.record(case)
        self.assertEqual(behavior.evaluate(case, record, self.root)["status"], "pass")
        record["reviewerConfirmed"] = False
        self.assertEqual(behavior.evaluate(case, record, self.root)["status"], "unverified")
        record["reviewerConfirmed"] = True
        record["trace"] = "missing.txt"
        self.assertEqual(behavior.evaluate(case, record, self.root)["status"], "unverified")

    def test_missing_cases_are_not_successes(self):
        case = self.cases["missing-focus"]
        results = behavior.score(list(self.cases.values()), [self.record(case)], self.root)
        self.assertEqual(sum(r["status"] == "pass" for r in results), 1)
        self.assertEqual(sum(r["status"] == "unverified" for r in results), 6)

    def test_catalog_covers_actual_skills(self):
        self.assertGreater(behavior.check_catalog(), 0)


if __name__ == "__main__":
    unittest.main()
