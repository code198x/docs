"""Validate retained interpreter-trace evidence and source identities."""

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
    model = json.loads((here / "model-trace.json").read_text())
    native = json.loads((here / "native-trace.json").read_text())
    browser = json.loads((here / "browser.json").read_text())

    def source(hashes: dict[str, str]) -> None:
        need(bool(hashes), "Empty baseline source set")
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
    for name, expected in ids["docs_source_sha256"].items():
        need(sha(docs / name) == expected, "Docs source hash mismatch")
    need(
        sha(here / "verify-trace.py") == native["verifier_sha256"],
        "Native verifier hash mismatch",
    )
    for key in [
        "rom_sha256",
        "emulator_sha256",
        "driver_sha256",
        "opening_driver_sha256",
    ]:
        need(native[key] == ids[key], "Tool identity mismatch: " + key)
    need(
        model["status"] == "passed" and len(model["cases"]) == 6,
        "Model count/status mismatch",
    )
    cases = model["cases"]
    need(
        [c["final"] for c in cases] == [1000, 3, 13, 10, 16, 11],
        "Independent selected results differ",
    )
    for case in cases:
        need(len(case["trace"]) == case["visits"], "Visit count mismatch")
        need(
            case["final"] == case["initial"] + case["visits"] * case["increment"],
            "Final formula mismatch",
        )
        for visit, row in enumerate(case["trace"], start=1):
            need(
                row
                == {
                    "visit": visit,
                    "before": case["initial"] + (visit - 1) * case["increment"],
                    "after": case["initial"] + visit * case["increment"],
                },
                "Partial sum formula mismatch",
            )
    wanted = {case["label"]: [str(case["final"])] for case in cases}
    wanted.update(
        {"question-repeat": ["13"], "instrumented": ["11", "12", "13", "FINAL 13"]}
    )

    def transcripts(data: dict[str, Any]) -> None:
        need(
            data["status"] == "passed" and len(data["checks"]) == 8,
            "Native count/status mismatch",
        )
        need(
            [c["label"] for c in data["checks"]]
            == [
                "original",
                "short",
                "question",
                "question-repeat",
                "empty",
                "changed-increment",
                "one",
                "instrumented",
            ],
            "Native labels/order mismatch",
        )
        for check in data["checks"]:
            fixture = here / check["source"]
            need(sha(fixture) == check["source_sha256"], "Fixture hash mismatch")
            numbers = [
                int(line.split(" ", 1)[0]) for line in fixture.read_text().splitlines()
            ]
            before, after = check["before"], check["after"]
            need(
                before == after
                and [line["number"] for line in before["lines"]] == numbers,
                "Stored records changed or line numbers differ",
            )
            raw = bytearray()
            for line in before["lines"]:
                body = bytes(line["body"])
                need(bool(body) and body[-1] == 13, "Stored line terminator missing")
                raw.extend(line["number"].to_bytes(2, "big"))
                raw.extend(len(body).to_bytes(2, "little"))
                raw.extend(body)
            need(
                list(raw) == before["bytes"]
                and len(raw) == before["end"] - before["start"],
                "Stored byte reconstruction differs",
            )
            need(
                before["leading_tokens"]
                == [241, 235, 241]
                + ([245] if check["label"] == "instrumented" else [])
                + [243, 245],
                "Stored keyword tokens differ",
            )
            output = wanted[check["label"]]
            rows = check["rows"]
            need(
                check["expected_output"] == output
                and len(rows) == 24
                and rows[: len(output)] == output
                and not any(rows[len(output) : 23])
                and rows[-1].startswith("0 OK"),
                "Native complete transcript mismatch",
            )
        first, repeated = data["checks"][2:4]
        need(
            first["before"] == repeated["before"]
            and first["source_sha256"] == repeated["source_sha256"]
            and first["installed"]
            and not repeated["installed"],
            "Unchanged repeat-run evidence missing",
        )

    transcripts(native)
    controls = {}
    for label in ["wrong_source_hash", "missing_native_rows"]:
        try:
            if label == "wrong_source_hash":
                bad = dict(ids["baseline_website_sha256"])
                bad[next(iter(bad))] = "0" * 64
                source(bad)
            else:
                corrupt = copy.deepcopy(native)
                corrupt["checks"][0]["rows"] = []
                transcripts(corrupt)
        except ValueError as error:
            controls[label] = str(error)
        else:
            raise ValueError("Corrupt evidence accepted: " + label)
    red = json.loads((here / "known-red/rejection.json").read_text())
    wrong = json.loads((here / "known-red/native-trace.json").read_text())
    need(
        red["exit_code"] != 0
        and "Complete ROM output differs: wrong-reset" in red["actual_failure"],
        "Wrong reset not rejected",
    )
    need(
        wrong["status"] == "failed" and wrong["checks"][0]["rows"][0] == "11",
        "Wrong-reset observation missing",
    )
    fixture = here / "known-red" / wrong["checks"][0]["source"]
    need(
        sha(fixture) == wrong["checks"][0]["source_sha256"],
        "Wrong-reset fixture mismatch",
    )
    need(
        browser["status"] == "passed"
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
            view["http"] == 200
            and view["outputs"] == ["1000"]
            and view["responseSha256"] == ids["built_lesson_sha256"],
            "Served output/build mismatch",
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
    need(
        all(
            len(view["scroll"]["numericLines"]) == 8
            and all(cell["lines"] == 1 for cell in view["scroll"]["numericLines"])
            for view in browser["viewports"]
        ),
        "Numeric trace cells wrap",
    )
    before = json.loads((here / "tables-before.json").read_text())
    after = json.loads((here / "tables-after.json").read_text())
    need(
        before["status"] == after["status"] == "passed"
        and len(before["cases"]) == len(after["cases"]) == 14,
        "Table consumer matrix incomplete",
    )
    need(not before["errors"] and not after["errors"], "Table consumer page errors")
    for old, new in zip(before["cases"], after["cases"], strict=True):
        need(
            old["geometry"]["client"] > 0 and new["geometry"]["client"] > 0,
            "Hidden table accepted",
        )
        need(
            (old["route"], old["width"], old["index"], old["geometry"]["cells"])
            == (new["route"], new["width"], new["index"], new["geometry"]["cells"]),
            "Table consumer contents changed",
        )
        need(
            new["geometry"]["tableDisplay"] == "table"
            and new["geometry"]["wrap"] == "normal",
            "Natural table sizing missing",
        )
        if new["geometry"]["total"] > new["geometry"]["client"] + 1:
            need(
                new["keyboard"]["left"] > 0
                and new["keyboard"]["lastRight"] <= new["keyboard"]["right"] + 2,
                "Keyboard final column missing",
            )
        need(
            not new["axe"]["violations"] and not new["axe"]["incomplete"],
            "Table accessibility finding unresolved",
        )
    synthetic = after["syntheticOverflow"]
    need(
        synthetic["total"] > synthetic["client"]
        and synthetic["left"] > 0
        and synthetic["lastRight"] <= synthetic["right"] + 2,
        "Positive synthetic overflow control missing",
    )
    try:
        need(
            all(case["geometry"]["wrap"] == "normal" for case in before["cases"]),
            "Original cell-wrapping policy rejected",
        )
    except ValueError as error:
        controls["original_cell_wrapping"] = str(error)
    else:
        raise ValueError("Original wrapping policy was not rejected")
    observed = json.loads((here / "browser-narrow-trace-failure.json").read_text())
    need(
        observed["status"] == "failed"
        and "Expected narrow trace scrolling" in observed["failure"],
        "Before-table rejection missing",
    )
    website = json.loads((here / "website-results.json").read_text())
    need(
        website["build_exit"] == website["check_exit"] == 0
        and website["tests_passed"] == 237,
        "Website checks missing",
    )
    targets = []
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
            targets.append(destination)
            if destination not in [here / "validation.json", here / "SHA256SUMS"]:
                need(destination.exists(), "Missing local link: " + target)
    report = {
        "status": "passed evidence checks",
        "finite_traces": 6,
        "fresh_rom_runs": 8,
        "browser_viewports": 2,
        "keyboard_behaviour_groups": 6,
        "table_consumer_viewports": 14,
        "local_links": len(targets),
        "negative_controls_rejected": controls,
        "wrong_reset_exit": red["exit_code"],
        "limits": "Retained source/evidence agreement, not independent execution, instruction counting, timing or learner validation.",
    }
    (here / "validation.json").write_text(json.dumps(report, indent=2) + "\n")
    files = sorted(
        p
        for p in here.rglob("*")
        if p.is_file() and p.name != "SHA256SUMS" and "__pycache__" not in p.parts
    )
    need(len(files) >= 25, "Unexpectedly small evidence set")
    (here / "SHA256SUMS").write_text(
        "".join(sha(p) + "  " + str(p.relative_to(here)) + "\n" for p in files)
    )
    need(all(p.exists() for p in targets), "Generated evidence link missing")
    print(json.dumps(report, indent=2))
    print("Manifest entries:", len(files))


if __name__ == "__main__":
    main()
