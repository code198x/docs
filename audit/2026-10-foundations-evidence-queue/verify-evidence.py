"""Check source reconciliation, prepared task arithmetic and retained model evidence."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
import subprocess
from fractions import Fraction
from pathlib import Path
from typing import Any


def need(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--website", required=True, type=Path)
    args = parser.parse_args()
    here = Path(__file__).resolve().parent
    docs = here.parent.parent
    inventory = json.loads((here / "inventory.json").read_text())
    identities = json.loads((here / "identities.json").read_text())
    models = json.loads((here / "models.json").read_text())
    baseline = json.loads(
        (docs / "audit/2026-10-foundations-objectives/units.json").read_text()
    )
    revision = identities["website_revision"]
    need(revision == inventory["website_revision"], "Source revision mismatch")

    def git(*arguments: str) -> str:
        return subprocess.check_output(["git", *arguments], cwd=args.website, text=True)

    paths = sorted(
        p
        for p in git(
            "ls-tree",
            "-r",
            "--name-only",
            revision,
            "src/content/curriculum/foundations",
        ).splitlines()
        if p.endswith(".mdx")
    )
    current = {path: git("show", revision + ":" + path) for path in paths}
    original = {item["path"]: item for item in baseline["units"] + baseline["modules"]}
    need(
        len(paths) == 49 and set(paths) == set(original),
        "Source inventory set mismatch",
    )
    for path, expected in identities["docs_source_sha256"].items():
        need(sha(docs / path) == expected, "Docs evidence identity mismatch")
    need(
        sha(here / "verify.py") == identities["verifier_sha256"],
        "Model verifier identity mismatch",
    )

    def source_records(data: dict[str, Any]) -> None:
        records = data["records"]
        need(
            len(records) == len(paths)
            and {row["path"] for row in records} == set(paths),
            "Inventory rows missing or duplicated",
        )
        for row in records:
            need(
                row["unit"] == bool(re.search(r"/unit-\d+\.mdx$", row["path"])),
                "Unit classification mismatch",
            )
            text = current[row["path"]]
            need(
                hashlib.sha256(text.encode()).hexdigest() == row["current_sha256"],
                "Current source hash mismatch",
            )
            need(
                row["baseline_sha256"] == original[row["path"]]["sha256"],
                "Frozen source hash mismatch",
            )
            need(
                row["changed"] == (row["current_sha256"] != row["baseline_sha256"]),
                "Change classification mismatch",
            )
            markers = re.findall(
                r"<summary>.*?</summary>|<Question\b[^>]*>", text, re.DOTALL
            )
            need(
                markers == row["prompts"]
                and len(markers) == row["explicit_prompt_markers"],
                "Prompt-marker extraction mismatch",
            )
        units = [row for row in records if row["unit"]]
        need(
            len(units)
            == data["units"]
            == data["current_units_with_explicit_prompt_markup"]
            == 39
            and data["overviews"] == 10,
            "Inventory counts mismatch",
        )
        need(
            all(row["explicit_prompt_markers"] > 0 for row in units),
            "Current prompt marker missing",
        )
        need(
            data["earlier_missing_prompt_units"]
            == [
                "basics/03",
                "decisions/04",
                "from-source-to-silicon/02",
                "repeating/01",
            ],
            "Earlier prompt gap set mismatch",
        )
        need(sum(row["changed"] for row in records) == 5, "Source delta count mismatch")

    def trace_records(data: dict[str, Any]) -> None:
        need(
            data["status"] == "passed finite model checks" and len(data["cases"]) == 6,
            "Model status/count mismatch",
        )
        for case in data["cases"]:
            need(len(case["rows"]) == case["updates"], "Trace count mismatch")
            for index, row in enumerate(case["rows"], start=1):
                expected = Fraction(case["initial"] + index * case["step"], 256)
                need(
                    row["update"] == index
                    and row["retained"] == expected * 256
                    and row["decoded"] == str(expected),
                    "Fractional retained state mismatch",
                )
                need(
                    row["drawn"] == expected.numerator // expected.denominator,
                    "Drawn coordinate mismatch",
                )
            need(
                case["final_retained"]
                == case["initial"] + case["updates"] * case["step"],
                "Final position mismatch",
            )
        half, quarter = data["cases"][:2]
        need(
            [row["drawn"] for row in half["rows"]] == [0, 1, 1, 2],
            "Half-step expectation mismatch",
        )
        need(
            [row["drawn"] for row in quarter["rows"]] == [0, 0, 0, 1],
            "Quarter-step expectation mismatch",
        )
        need(
            data["first_drawing_divergence"] == 2
            and len(data["overflow_rejections"]) == 3,
            "Boundary evidence missing",
        )
        need(
            [row["drawn"] for row in data["wrong_policy"]["rows"]] == [0, 0, 0, 0],
            "Wrong-policy trace mismatch",
        )
        need(
            data["cases"][-1]["final_retained"] == 65535,
            "Last-fitting positive case missing",
        )

    source_records(inventory)
    trace_records(models)
    controls = {}
    for label in [
        "missing_inventory_row",
        "wrong_source_hash",
        "discarded_fractional_state",
    ]:
        try:
            if label == "discarded_fractional_state":
                corrupt = copy.deepcopy(models)
                corrupt["cases"][0] = corrupt["wrong_policy"]
                trace_records(corrupt)
            else:
                corrupt = copy.deepcopy(inventory)
                if label == "missing_inventory_row":
                    corrupt["records"].pop()
                else:
                    corrupt["records"][0]["current_sha256"] = "0" * 64
                source_records(corrupt)
        except ValueError as error:
            controls[label] = str(error)
        else:
            raise ValueError("Negative control accepted: " + label)
    red = json.loads((here / "known-red/rejection.json").read_text())
    wrong = json.loads((here / "known-red/wrong-trace.json").read_text())
    need(
        red["exit_code"] != 0
        and "Wrong policy loses a later whole-pixel move" in red["actual_failure"],
        "Nonzero wrong-policy rejection missing",
    )
    need(
        wrong == models["wrong_policy"], "Rejected model differs from retained contrast"
    )
    learner = (here / "LEARNER-TASKS.md").read_text()
    need(
        "LET position = 0" in learner
        and "LET step = 128" in learner
        and "1 TO 4" in learner
        and "SHIFTRIGHT 8" in learner
        and "step to 64" in learner,
        "Prepared task/model inputs differ",
    )
    assessor = (here / "ASSESSOR.md").read_text()
    for row in models["cases"][0]["rows"]:
        full = float(Fraction(row["updated"], 256))
        full_text = str(int(full)) if full.is_integer() else str(full)
        need(
            f"| {row['update']} | {row['updated']} | {full_text} | {row['drawn']} |"
            in assessor,
            "Assessor half-step row differs",
        )
    need("65663" in assessor and 65535 + 128 == 65663, "Assessor range answer differs")
    links = []
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
            links.append(destination)
            if destination not in [here / "validation.json", here / "SHA256SUMS"]:
                need(destination.exists(), "Missing local link: " + target)
    report = {
        "status": "passed source/model/evidence checks",
        "units": 39,
        "overviews": 10,
        "current_units_with_prompt_markers": 39,
        "changed_units": 4,
        "changed_overviews": 1,
        "finite_traces": 6,
        "overflow_rejections": 3,
        "wrong_policy_exit": red["exit_code"],
        "local_links": len(links),
        "negative_controls_rejected": controls,
        "limits": "Source/markup reconciliation and selected model arithmetic, not a fresh full-course review, target execution, browser run or learner trial.",
    }
    (here / "validation.json").write_text(json.dumps(report, indent=2) + "\n")
    files = sorted(
        p
        for p in here.rglob("*")
        if p.is_file() and p.name != "SHA256SUMS" and "__pycache__" not in p.parts
    )
    need(len(files) >= 10, "Unexpectedly small evidence set")
    (here / "SHA256SUMS").write_text(
        "".join(sha(p) + "  " + str(p.relative_to(here)) + "\n" for p in files)
    )
    need(all(path.exists() for path in links), "Generated evidence link missing")
    print(json.dumps(report, indent=2))
    print("Manifest entries:", len(files))


if __name__ == "__main__":
    main()
