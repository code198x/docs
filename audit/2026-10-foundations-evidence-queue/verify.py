"""Reconcile immutable source inventory and check finite fixed-point paper traces."""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
import re
import subprocess
from fractions import Fraction
from pathlib import Path
from typing import Any

WEBSITE_REVISION = "d0de348ba750cac17bfd7757a217e5b37eb28042"
SCALE = 256
MAXIMUM = 65535


def need(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def trace(initial: int, step: int, count: int, discard: bool = False) -> dict[str, Any]:
    need(
        0 <= initial <= MAXIMUM and 0 <= step <= MAXIMUM and count >= 0,
        "Invalid trace domain",
    )
    state = initial
    rows = []
    for visit in range(1, count + 1):
        updated = state + step
        if updated > MAXIMUM:
            raise OverflowError(
                f"Update {visit} needs stored {updated}, outside unsigned 16-bit range"
            )
        drawn = updated // SCALE
        retained = drawn * SCALE if discard else updated
        rows.append(
            {
                "update": visit,
                "before": state,
                "updated": updated,
                "decoded": str(Fraction(updated, SCALE)),
                "drawn": drawn,
                "retained": retained,
            }
        )
        state = retained
    return {
        "initial": initial,
        "step": step,
        "updates": count,
        "discard_after_drawing": discard,
        "rows": rows,
        "final_retained": state,
    }


def validate_trace(case: dict[str, Any]) -> None:
    need(len(case["rows"]) == case["updates"], "Trace length mismatch")
    for visit, row in enumerate(case["rows"], start=1):
        expected = Fraction(case["initial"], SCALE) + visit * Fraction(
            case["step"], SCALE
        )
        need(
            row["decoded"] == str(expected) and row["retained"] == expected * SCALE,
            "Retained state disagrees with exact rational position",
        )
        need(
            row["drawn"] == expected.numerator // expected.denominator,
            "Whole coordinate disagrees with rational floor",
        )
    need(
        case["final_retained"] == case["initial"] + case["updates"] * case["step"],
        "Final state formula mismatch",
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--website", type=Path)
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument("--wrong-only", action="store_true")
    args = parser.parse_args()
    out = args.output.resolve()
    out.mkdir(parents=True, exist_ok=True)
    if args.wrong_only:
        wrong = trace(0, 128, 4, discard=True)
        (out / "wrong-trace.json").write_text(json.dumps(wrong, indent=2) + "\n")
        need(
            [row["drawn"] for row in wrong["rows"]] == [0, 1, 1, 2],
            "Wrong policy loses a later whole-pixel move",
        )
        raise ValueError("Wrong policy unexpectedly accepted")
    need(args.website is not None, "Supply website Git repository")
    here = Path(__file__).resolve().parent
    docs = here.parent.parent
    baseline = json.loads(
        (docs / "audit/2026-10-foundations-objectives/units.json").read_text()
    )
    original = baseline["units"] + baseline["modules"]

    def git(*arguments: str) -> bytes:
        return subprocess.check_output(["git", *arguments], cwd=args.website)

    paths = (
        git(
            "ls-tree",
            "-r",
            "--name-only",
            WEBSITE_REVISION,
            "src/content/curriculum/foundations",
        )
        .decode()
        .splitlines()
    )
    paths = sorted(p for p in paths if p.endswith(".mdx"))
    need(
        set(paths) == {item["path"] for item in original} and len(paths) == 49,
        "Inventory source-set mismatch",
    )
    records = []
    previous = {item["path"]: item for item in original}
    for path in paths:
        data = git("show", WEBSITE_REVISION + ":" + path)
        old = previous[path]
        need(
            sha(git("show", baseline["website_revision"] + ":" + path))
            == old["sha256"],
            "Frozen inventory source hash mismatch",
        )
        prompts = re.findall(
            r"<summary>.*?</summary>|<Question\b[^>]*>", data.decode(), re.DOTALL
        )
        records.append(
            {
                "path": path,
                "baseline_sha256": old["sha256"],
                "current_sha256": sha(data),
                "changed": old["sha256"] != sha(data),
                "unit": bool(re.search(r"/unit-\d+\.mdx$", path)),
                "explicit_prompt_markers": len(prompts),
                "prompts": prompts,
            }
        )
    units = [item for item in records if item["unit"]]
    missing_before = sorted(
        item["id"] for item in baseline["units"] if not item["explicit_prompt_evidence"]
    )
    need(
        len(units) == 39 and len(missing_before) == 4,
        "Unit or earlier prompt count mismatch",
    )
    need(
        all(item["explicit_prompt_markers"] > 0 for item in units),
        "Current unit lacks explicit prompt marker",
    )
    inventory = {
        "website_revision": WEBSITE_REVISION,
        "frozen_inventory_revision": baseline["website_revision"],
        "units": len(units),
        "overviews": len(records) - len(units),
        "earlier_units_with_explicit_prompt_markup": 35,
        "current_units_with_explicit_prompt_markup": len(units),
        "earlier_missing_prompt_units": missing_before,
        "records": records,
        "limits": "Exact source-set/hash/markup reconciliation, not a fresh full-body review or a measure of assessment quality.",
    }
    (out / "inventory.json").write_text(json.dumps(inventory, indent=2) + "\n")
    cases = []
    for label, initial, step, count in [
        ("half-step", 0, 128, 4),
        ("quarter-step", 0, 64, 4),
        ("one-and-half", 768, 384, 4),
        ("zero-updates", 768, 128, 0),
        ("stationary-fraction", 384, 0, 3),
        ("last-fitting", 65407, 128, 1),
    ]:
        case = trace(initial, step, count)
        validate_trace(case)
        case["label"] = label
        cases.append(case)
    need(len(cases) == 6, "Missing finite trace cases")
    wrong = trace(0, 128, 4, discard=True)
    correct_draws = [row["drawn"] for row in cases[0]["rows"]]
    wrong_draws = [row["drawn"] for row in wrong["rows"]]
    need(
        correct_draws[0] == wrong_draws[0] == 0 and correct_draws[1] != wrong_draws[1],
        "One-update false positive or second-update distinction missing",
    )
    boundaries = []
    for initial, step, count in [(65535, 1, 1), (65408, 128, 1), (65407, 128, 2)]:
        try:
            trace(initial, step, count)
        except OverflowError as error:
            boundaries.append(
                {
                    "initial": initial,
                    "step": step,
                    "updates": count,
                    "rejected": str(error),
                }
            )
        else:
            raise ValueError("Out-of-range update accepted")
    models = {
        "status": "passed finite model checks",
        "scale": SCALE,
        "maximum": MAXIMUM,
        "cases": cases,
        "wrong_policy": wrong,
        "first_drawing_divergence": 2,
        "overflow_rejections": boundaries,
        "limits": "Selected exact-rational/integer paper models. No target execution, renderer, timing, original hardware or learner trial.",
    }
    (out / "models.json").write_text(json.dumps(models, indent=2) + "\n")
    identities = {
        "website_revision": WEBSITE_REVISION,
        "docs_baseline": "04f4fd048893b130b886d17ed339fa41c4475b6a",
        "python": platform.python_version(),
        "verifier_sha256": sha(Path(__file__).read_bytes()),
        "docs_source_sha256": {},
    }
    for path in [
        "PROJECT.md",
        "specifications/pseudocode.md",
        "specifications/unit.md",
        "specifications/curriculum.md",
        "specifications/experiments/synthesis-and-transfer.md",
        "audit/2026-10-foundations-objectives/units.json",
        "audit/2026-10-foundations-objectives/MAP.md",
        "audit/2026-10-structure-pilot/REPORT.md",
        "audit/2026-10-structure-pilot/LEARNER-TASKS.md",
        "audit/2026-10-fractions-pilot/REPORT.md",
        "audit/2026-10-fractions-pilot/LEARNER-TASKS.md",
        "audit/2026-10-numbers-pilot/REPORT.md",
        "audit/2026-10-numbers-pilot/LEARNER-TASKS.md",
        "audit/2026-10-interpreter-trace/REPORT.md",
    ]:
        identities["docs_source_sha256"][path] = sha((docs / path).read_bytes())
    (out / "identities.json").write_text(json.dumps(identities, indent=2) + "\n")
    print(
        f"PASS {len(units)} units, ten overviews, four resolved markup gaps; six finite traces and three overflow rejections"
    )


if __name__ == "__main__":
    main()
