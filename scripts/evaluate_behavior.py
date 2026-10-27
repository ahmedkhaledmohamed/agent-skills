#!/usr/bin/env python3
"""Check recorded observations against fictional cases; never launch a model."""
import argparse
import fnmatch
import json
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
ACTIONS = {"read", "search", "ask", "edit", "write", "publish", "push", "merge"}


def load_cases(root=ROOT):
    cases = json.loads((root / "evals/cases.json").read_text())["cases"]
    ids = [case["id"] for case in cases]
    if len(set(ids)) != len(ids):
        raise ValueError("Duplicate case ID")
    for case in cases:
        if not (root / "skills" / case["skill"] / "SKILL.md").is_file():
            raise ValueError("Case references an unavailable skill")
        if not set(case["allowedActions"]) <= ACTIONS or not case["expectedFacts"]:
            raise ValueError("Invalid case criteria")
    return cases


def check_catalog(root=ROOT):
    catalog = json.loads((root / "catalog.json").read_text())
    names = [name for group in catalog["groups"] for name in group["skills"]]
    actual = {p.parent.name for p in (root / "skills").glob("*/SKILL.md")}
    if len(names) != len(set(names)) or set(names) != actual:
        raise ValueError("Catalog must classify every skill exactly once")
    for group in catalog["groups"]:
        if not group["runtimeTarget"] or not group["requirements"] or not group["verification"]:
            raise ValueError("Catalog group needs targets, dependencies and verification limits")
    return len(actual)


def evaluate(case, record, evidence_root):
    failures, unverified = [], []
    if record is None:
        return {"caseId": case["id"], "status": "unverified", "failures": [], "unverified": ["No recorded run"]}
    trace = record.get("trace")
    if not isinstance(trace, str) or not trace:
        unverified.append("No trace evidence")
    else:
        path = (evidence_root / trace).resolve()
        if not path.is_relative_to(evidence_root.resolve()) or not path.is_file() or not path.stat().st_size:
            unverified.append("Trace evidence missing, empty or outside the recording directory")
    actions = record.get("actions")
    if not isinstance(actions, list):
        unverified.append("No normalized action trace")
        actions = []
    for action in actions:
        if not isinstance(action, dict) or action.get("kind") not in case["allowedActions"]:
            failures.append("Disallowed or malformed action")
            continue
        if action["kind"] in {"read", "search"}:
            target = action.get("target")
            if not isinstance(target, str) or target.startswith("/") or "\\" in target or ".." in PurePosixPath(target).parts:
                failures.append("Source action needs a normalized case-relative target")
            elif case.get("allowedTargets") and not any(fnmatch.fnmatchcase(target, p) for p in case["allowedTargets"]):
                failures.append("Read/search outside the declared case scope")
    reads = {a.get("target") for a in actions if isinstance(a, dict) and a.get("kind") == "read"}
    for required in case.get("requiredReads", []):
        if required not in reads:
            failures.append("Required source was not read: " + required)
    facts = record.get("facts", {})
    evidence = record.get("factEvidence", {})
    if not isinstance(facts, dict) or not isinstance(evidence, dict):
        raise ValueError("facts and factEvidence must be objects")
    if record.get("reviewerConfirmed") is not True:
        unverified.append("Semantic normalization has not been confirmed by a reviewer")
    for key, expected in case["expectedFacts"].items():
        if key not in facts or not isinstance(evidence.get(key), str) or not evidence[key].strip():
            unverified.append("Missing fact or evidence pointer: " + key)
        elif type(facts[key]) is not type(expected) or facts[key] != expected:
            failures.append("Recorded outcome differs: " + key)
    return {"caseId": case["id"], "status": "fail" if failures else "unverified" if unverified else "pass",
            "failures": failures, "unverified": unverified}


def score(cases, records, evidence_root):
    by_id = {}
    known = {case["id"] for case in cases}
    for record in records:
        case_id = record["caseId"]
        if case_id not in known or case_id in by_id:
            raise ValueError("Unknown or duplicate recorded case")
        by_id[case_id] = record
    return [evaluate(case, by_id.get(case["id"]), evidence_root) for case in cases]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("records", nargs="?", type=Path, help="Private normalized recording JSON; traces are relative to this file")
    parser.add_argument("--check", action="store_true", help="Validate the catalog and case definitions without running a model")
    args = parser.parse_args()
    cases = load_cases()
    count = check_catalog()
    if args.check:
        if args.records:
            parser.error("Choose --check or a recordings file")
        print(json.dumps({"skills": count, "cases": len(cases), "mode": "definition-validation", "modelRuns": 0}))
        return 0
    if not args.records:
        parser.error("Supply --check or a recordings file")
    data = json.loads(args.records.read_text())
    results = score(cases, data["records"], args.records.resolve().parent)
    print(json.dumps({"assessment": "Action checks plus reviewer-normalized semantic observations; not independent semantic judging",
                      "results": results}, indent=2))
    return 0 if all(r["status"] == "pass" for r in results) else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ValueError, KeyError, TypeError, OSError) as error:
        print(json.dumps({"error": str(error)}))
        raise SystemExit(2)
