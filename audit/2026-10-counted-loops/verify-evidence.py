"""Check retained counted-loop source, output and browser evidence."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
import subprocess
from pathlib import Path
from typing import Any


def need(value: bool, message: str) -> None:
    if not value:
        raise ValueError(message)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--website", type=Path, required=True)
    args = parser.parse_args()
    here = Path(__file__).resolve().parent
    docs = here.parent.parent
    ids = json.loads((here / "identities.json").read_text())
    native = json.loads((here / "native-counted.json").read_text())
    model = json.loads((here / "model-counted.json").read_text())
    browser = json.loads((here / "browser-counted.json").read_text())

    def source(hashes: dict[str, str]) -> None:
        for name, expected in hashes.items():
            data = subprocess.check_output(
                ["git", "show", ids["website_baseline"] + ":" + name], cwd=args.website
            )
            need(
                hashlib.sha256(data).hexdigest() == expected,
                "Baseline source hash mismatch",
            )

    source(ids["baseline_website_sha256"])
    for name, expected in ids["proposed_website_sha256"].items():
        need(sha(args.website / name) == expected, "Proposed source hash mismatch")
    need(
        sha(docs / "specifications/pseudocode.md") == ids["proposed_pseudocode_sha256"],
        "Specification hash mismatch",
    )
    need(
        sha(here / "verify-counted.py")
        == native["verifier_sha256"]
        == ids["native_verifier_sha256"],
        "Native verifier identity mismatch",
    )
    need(
        sha(args.website / "scripts/verification/counted-loop-pilot.mjs")
        == ids["browser_verifier_sha256"],
        "Browser verifier identity mismatch",
    )
    need(
        sha(docs / "audit/2026-10-repetition-pilot/native-repetition.json")
        == ids["earlier_native_evidence_sha256"],
        "Earlier evidence hash mismatch",
    )

    def transcripts(data: dict[str, Any]) -> None:
        need(
            data["status"] == "passed" and len(data["checks"]) == 11,
            "Native count/status mismatch",
        )
        need(len(model["cases"]) == 5, "Model count mismatch")
        wanted = []
        for case in model["cases"]:
            for position, key in [
                ("outside", "outside_after"),
                ("inside", "inside_after"),
            ]:
                wanted.append((f"{position}-{case['start']}-{case['end']}", case[key]))
        wanted.append(("reset-inside", ["BEFORE", "1", "2", "3", "TOTAL 3", "AFTER"]))
        for item, (label, output) in zip(data["checks"], wanted, strict=True):
            need(
                item["label"] == label and item["expected_output"] == output,
                "Native/model case mismatch",
            )
            need(
                sha(here / item["source"]) == item["source_sha256"],
                "Fixture hash mismatch",
            )
            rows = item["rows"]
            need(
                len(rows) == 24
                and rows[: len(output)] == output
                and not any(rows[len(output) : 22])
                and rows[-1].startswith("0 OK"),
                "Native complete transcript mismatch",
            )

    transcripts(native)
    controls = {}
    for label in ["wrong_source_hash", "missing_native_transcript"]:
        try:
            if label == "wrong_source_hash":
                bad = dict(ids["baseline_website_sha256"])
                bad[next(iter(bad))] = "0" * 64
                source(bad)
            else:
                bad = copy.deepcopy(native)
                bad["checks"][0]["rows"] = []
                transcripts(bad)
        except ValueError as error:
            controls[label] = str(error)
        else:
            raise ValueError("Corrupt evidence accepted: " + label)
    red = json.loads((here / "known-red/rejection.json").read_text())
    need(
        red["exit_code"] != 0
        and "Complete ROM output differs" in red["actual_failure"],
        "Native known-red rejection missing",
    )
    need(
        browser["status"] == "passed"
        and len(browser["viewports"]) == 2
        and len(browser["checks"]) == 6
        and not browser["errors"],
        "Browser evidence missing",
    )
    need(
        all(
            not v["violations"] and not v["incomplete"] and not v["revealedIncomplete"]
            for v in browser["viewports"]
        ),
        "Browser finding not resolved",
    )
    links = 0
    for path in [
        docs / "README.md",
        docs / "audit/2026-10-foundations-coverage.md",
        here / "REPORT.md",
        here / "LEARNER-TASKS.md",
        here / "ASSESSOR.md",
        docs / "specifications/pseudocode.md",
    ]:
        for target in re.findall(r"\]\(([^)]+)\)", path.read_text()):
            if ":" in target or target.startswith("#"):
                continue
            need(
                (path.parent / target.split("#")[0]).exists(),
                "Missing local link: " + target,
            )
            links += 1
    report = {
        "status": "passed evidence checks",
        "model_ranges": 5,
        "fresh_native_runs": 11,
        "browser_viewports": 2,
        "keyboard_behaviour_groups": 6,
        "local_links": links,
        "negative_controls_rejected": controls,
        "native_wrong_policy_exit": red["exit_code"],
        "limits": "Source/fixture/evidence agreement checks; not independent execution or learner validation.",
    }
    (here / "validation.json").write_text(json.dumps(report, indent=2) + "\n")
    files = sorted(
        p
        for p in here.rglob("*")
        if p.is_file() and p.name != "SHA256SUMS" and "__pycache__" not in p.parts
    )
    need(len(files) > 20, "Unexpectedly small evidence set")
    (here / "SHA256SUMS").write_text(
        "".join(sha(p) + "  " + str(p.relative_to(here)) + "\n" for p in files)
    )
    print(json.dumps(report, indent=2))
    print("Manifest entries:", len(files))


if __name__ == "__main__":
    main()
