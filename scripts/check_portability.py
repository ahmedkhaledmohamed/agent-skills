#!/usr/bin/env python3
"""Flag publication risks without printing the matched private text.

This is a pattern check, not a disclosure or licensing clearance. Additional
organization-specific deny patterns should be supplied locally, not committed.
"""
import argparse
import json
from pathlib import Path
import re
import subprocess

RULES = {
    "personal-machine-path": r"(?<![A-Za-z0-9:/])/(?:Users|home)/[A-Za-z0-9_.-]+/",
    "credential-like-value": r"\b(?:gh[pousr]_|xox[baprs]-|sk-)[A-Za-z0-9_-]{20,}|-----BEGIN (?:[A-Z ]+ )?PRIVATE KEY-----",
    "internal-host": r"https?://[^\s/]+\.(?:internal|corp)(?:[/:\s]|$)",
    "transcript-section": r"<summary>\s*Raw Prompts\b",
}
MAX_BLOB = 2 * 1024 * 1024


def git(root, *args):
    return subprocess.check_output(["git", "-C", str(root), *args])


def inspect(data, label, rules, findings, counters):
    if len(data) > MAX_BLOB:
        findings.append({"source": label, "rule": "oversize-unreviewed"})
        return
    if b"\0" in data[:4096]:
        counters["binarySkipped"] += 1
        return
    text = data.decode("utf-8", errors="replace")
    counters["textChecked"] += 1
    for name, pattern in rules.items():
        if pattern.search(text):
            findings.append({"source": label, "rule": name})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", default=".")
    parser.add_argument("--history", action="store_true", help="Also scan reachable Git blobs and commit metadata across all local refs")
    parser.add_argument("--deny-pattern", action="append", default=[], help="Additional local-only regular expression; matched values are never printed")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    try:
        root = Path(git(root, "rev-parse", "--show-toplevel").decode().strip())
        rules = {name: re.compile(value, re.I) for name, value in RULES.items()}
        rules.update({"local-deny-" + str(i + 1): re.compile(value, re.I) for i, value in enumerate(args.deny_pattern)})
        findings = []
        counters = {"textChecked": 0, "binarySkipped": 0, "historyBlobs": 0}
        names = git(root, "ls-files", "--cached", "--others", "--exclude-standard", "-z").split(b"\0")
        for raw in sorted(set(names)):
            if not raw:
                continue
            name = raw.decode("utf-8", errors="surrogateescape")
            path = root / name
            if path.is_symlink():
                findings.append({"source": name, "rule": "symlink-review-required"})
            elif path.is_file():
                inspect(path.read_bytes(), name, rules, findings, counters)
        if args.history:
            # A persistent batch process avoids a shell/process per historical blob.
            records = git(root, "rev-list", "--objects", "--all").splitlines()
            with subprocess.Popen(["git", "-C", str(root), "cat-file", "--batch"], stdin=subprocess.PIPE, stdout=subprocess.PIPE) as batch:
                for record in records:
                    oid = record.split(b" ", 1)[0]
                    batch.stdin.write(oid + b"\n")
                    batch.stdin.flush()
                    header = batch.stdout.readline().split()
                    if len(header) != 3:
                        raise ValueError("Cannot read a historical Git object")
                    size = int(header[2])
                    data = batch.stdout.read(size)
                    batch.stdout.read(1)
                    if header[1] in (b"blob", b"commit"):
                        # Use object IDs only: paths and matched values can themselves be private.
                        inspect(data, "history:" + oid.decode()[:12], rules, findings, counters)
                        if header[1] == b"blob":
                            counters["historyBlobs"] += 1
                batch.stdin.close()
                if batch.wait():
                    raise ValueError("Historical Git object read failed")
        print(json.dumps({"scope": "working files plus all local refs" if args.history else "working files", **counters, "findings": findings, "clearance": "Pattern results only; inspect content, binaries, repository surfaces and source rights before publication."}, indent=2))
        return 1 if findings else 0
    except (OSError, ValueError, re.error, subprocess.CalledProcessError) as error:
        print(json.dumps({"error": type(error).__name__, "clearance": "Incomplete check; publication not established."}))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
