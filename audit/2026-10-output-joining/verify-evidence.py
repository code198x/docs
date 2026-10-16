"""Validate retained output-joining sources, transcripts and scoped browser evidence."""

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
    model = json.loads((here / "model-output.json").read_text())
    native = json.loads((here / "native-output.json").read_text())
    browser = json.loads((here / "browser.json").read_text())

    def sources(hashes: dict[str, str]) -> None:
        need(bool(hashes), "Empty baseline source set")
        for name, expected in hashes.items():
            data = subprocess.check_output(
                ["git", "show", ids["website_baseline"] + ":" + name], cwd=args.website
            )
            need(
                hashlib.sha256(data).hexdigest() == expected,
                "Baseline source hash mismatch",
            )

    sources(ids["baseline_website_sha256"])
    for name, expected in ids["proposed_website_sha256"].items():
        need(sha(args.website / name) == expected, "Proposed source hash mismatch")
    for name, expected in ids["docs_source_sha256"].items():
        need(sha(docs / name) == expected, "Docs source hash mismatch")
    need(
        sha(here / "verify-output.py") == native["verifier_sha256"],
        "Native verifier mismatch",
    )
    need(native["rom_sha256"] == ids["rom_sha256"], "ROM identity mismatch")
    for key in ["emulator_sha256", "driver_sha256", "opening_driver_sha256"]:
        need(native[key] == ids[key], "Tool identity mismatch: " + key)
    need(
        model["status"] == "passed" and len(model["cases"]) == 11,
        "Model count/status mismatch",
    )
    wanted = []
    for case in model["cases"]:
        need(
            "".join(str(part) for part in case["parts"]) == case["output"],
            "Model join mismatch",
        )
        wanted.append((case["label"], case["basic"], [case["output"]]))
    wanted.extend(
        [
            ("comma-zone", 'PRINT "Score: ",2+3', ["Score:" + " " * 10 + "5"]),
            ("comma-letters", 'PRINT "A","B"', ["A" + " " * 15 + "B"]),
            ("continued-print", 'PRINT "A";: PRINT "B"', ["AB"]),
            ("new-print-line", 'PRINT "A": PRINT "B"', ["A", "B"]),
        ]
    )
    outputs = {case["label"]: case["output"] for case in model["cases"]}
    need(
        outputs["literal"] == "2 + 2" and outputs["sum"] == "4",
        "Literal/arithmetic contrast missing",
    )
    need(
        outputs["missing-space"] == "Score:5"
        and outputs["repaired-space"] == "Score: 5",
        "Space repair missing",
    )
    need(outputs["visible-boundary"] == " A Z", "Significant space boundary missing")

    def transcripts(data: dict[str, Any]) -> None:
        need(
            data["status"] == "passed" and len(data["checks"]) == 15,
            "Native count/status mismatch",
        )
        for check, (label, source, output) in zip(data["checks"], wanted, strict=True):
            need(
                check["label"] == label
                and check["source"] == source
                and check["expected_output"] == output,
                "Native/model case mismatch",
            )
            rows = check["rows"]
            need(
                len(rows) == 24
                and rows[: len(output)] == output
                and not any(rows[len(output) : 23])
                and rows[-1].startswith("0 OK"),
                "Native complete transcript mismatch",
            )

    transcripts(native)
    controls = {}
    for label in ["wrong_source_hash", "missing_native_rows"]:
        try:
            if label == "wrong_source_hash":
                bad = dict(ids["baseline_website_sha256"])
                bad[next(iter(bad))] = "0" * 64
                sources(bad)
            else:
                bad_native = copy.deepcopy(native)
                bad_native["checks"][0]["rows"] = []
                transcripts(bad_native)
        except ValueError as error:
            controls[label] = str(error)
        else:
            raise ValueError("Corrupt evidence accepted: " + label)
    red = json.loads((here / "known-red/rejection.json").read_text())
    wrong = json.loads((here / "known-red/native-output.json").read_text())
    need(
        red["exit_code"] != 0
        and "Complete ROM output differs: comma-is-not-immediate-join"
        in red["actual_failure"],
        "Wrong separator not rejected",
    )
    need(
        wrong["status"] == "failed"
        and wrong["checks"][0]["rows"][0] == "Score:" + " " * 10 + "5",
        "Wrong-separator observation missing",
    )
    need(
        browser["status"] == "passed"
        and len(browser["viewports"]) == 2
        and len(browser["checks"]) == 6
        and not browser["errors"],
        "Browser status/count mismatch",
    )
    need(
        [v["width"] for v in browser["viewports"]] == [1440, 390],
        "Browser viewport mismatch",
    )
    for view in browser["viewports"]:
        need(
            view["responseSha256"] == ids["built_lesson_sha256"],
            "Served build hash mismatch",
        )
        need(
            view["http"] == 200
            and view["outputs"] == ["2 + 2\n4", "Two plus two is 4"],
            "Rendered output mismatch",
        )
        need(
            view["dimensions"]["document"] <= view["width"],
            "Recorded document overflow",
        )
        for state in ["closed", "revealed"]:
            need(
                not view[state]["violations"] and not view[state]["incomplete"],
                "Browser finding unresolved",
            )
    website = json.loads((here / "website-results.json").read_text())
    need(
        website["build_exit"] == website["check_exit"] == 0
        and website["tests_passed"] == 237,
        "Website checks missing",
    )
    links = 0
    generated_links = []
    for path in [
        docs / "README.md",
        docs / "audit/2026-10-foundations-coverage.md",
        here / "REPORT.md",
        here / "LEARNER-TASKS.md",
        here / "ASSESSOR.md",
    ]:
        for target in re.findall(r"\]\(([^)]+)\)", path.read_text()):
            if ":" in target or target.startswith("#"):
                continue
            destination = path.parent / target.split("#")[0]
            if destination in [here / "validation.json", here / "SHA256SUMS"]:
                generated_links.append(destination)
            else:
                need(destination.exists(), "Missing local link: " + target)
            links += 1
    report = {
        "status": "passed evidence checks",
        "model_cases": 11,
        "fresh_native_commands": 15,
        "browser_viewports": 2,
        "keyboard_behaviour_groups": 6,
        "local_links": links,
        "negative_controls_rejected": controls,
        "native_wrong_separator_exit": red["exit_code"],
        "limits": "Source and retained evidence agreement; not independent execution or learner validation.",
    }
    (here / "validation.json").write_text(json.dumps(report, indent=2) + "\n")
    files = sorted(
        p
        for p in here.rglob("*")
        if p.is_file() and p.name != "SHA256SUMS" and "__pycache__" not in p.parts
    )
    need(len(files) >= 20, "Unexpectedly small evidence set")
    (here / "SHA256SUMS").write_text(
        "".join(sha(p) + "  " + str(p.relative_to(here)) + "\n" for p in files)
    )
    need(
        all(path.exists() for path in generated_links),
        "Generated evidence link missing",
    )
    print(json.dumps(report, indent=2))
    print("Manifest entries:", len(files))


if __name__ == "__main__":
    main()
