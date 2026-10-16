"""Check the fixed-point lesson against accepted models and retained browser evidence."""

from __future__ import annotations

import argparse
import copy
import hashlib
import importlib.util
import json
import re
import subprocess
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
    ids = json.loads((here / "identities.json").read_text())
    model = json.loads((here / "model-recheck.json").read_text())
    browser = json.loads((here / "browser.json").read_text())
    accepted_path = docs / "audit/2026-10-foundations-evidence-queue/models.json"
    accepted = json.loads(accepted_path.read_text())
    driver = docs / "audit/2026-10-foundations-evidence-queue/verify.py"
    need(
        sha(driver) == model["model_source_sha256"],
        "Accepted model source identity mismatch",
    )
    need(
        sha(accepted_path)
        == model["accepted_models_sha256"]
        == browser["acceptedModelsSha256"],
        "Accepted model record identity mismatch",
    )
    for name, expected in ids["baseline_website_sha256"].items():
        data = subprocess.check_output(
            ["git", "show", ids["website_baseline"] + ":" + name], cwd=args.website
        )
        need(
            hashlib.sha256(data).hexdigest() == expected,
            "Baseline source hash mismatch",
        )

    def proposed(hashes: dict[str, str]) -> None:
        need(bool(hashes), "Empty proposed source set")
        for name, expected in hashes.items():
            need(sha(args.website / name) == expected, "Proposed source hash mismatch")

    proposed(ids["proposed_website_sha256"])
    for name, expected in ids["docs_source_sha256"].items():
        need(sha(docs / name) == expected, "Docs source hash mismatch")
    need(
        model["status"] == "passed"
        and len(model["checks"]) == len(accepted["cases"]) == 6,
        "Finite model coverage mismatch",
    )
    spec = importlib.util.spec_from_file_location("accepted", driver)
    need(
        spec is not None and spec.loader is not None,
        "Cannot load accepted model functions",
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    for recheck, case in zip(model["checks"], accepted["cases"], strict=True):
        actual = module.trace(case["initial"], case["step"], case["updates"])
        module.validate_trace(actual)
        need(
            recheck["label"] == case["label"]
            and recheck["trace"]
            == actual
            == {k: v for k, v in case.items() if k != "label"},
            "Fresh/accepted finite trace mismatch",
        )
    half = accepted["cases"][0]
    expected_rows = []
    for row in half["rows"]:
        full = row["updated"] / 256
        expected_rows.append(
            [
                str(row["update"]),
                str(row["updated"]),
                str(int(full)) if full.is_integer() else str(full),
                str(row["drawn"]),
            ]
        )

    def rendered(data: dict[str, Any]) -> None:
        need(
            data["status"] == "passed"
            and len(data["checks"]) == 10
            and not data["errors"],
            "Browser count/status mismatch",
        )
        need(
            [view["width"] for view in data["viewports"]] == [1440, 390],
            "Browser viewports mismatch",
        )
        for view in data["viewports"]:
            need(
                view["http"] == 200
                and view["responseSha256"] == ids["built_lesson_sha256"],
                "Served build hash mismatch",
            )
            need(
                view["outputs"] == ["1.5", "512"] and view["rows"] == expected_rows,
                "Rendered table/output mismatch",
            )
            need(
                view["headerWrap"] == "normal"
                and len(view["numericLines"]) == 16
                and all(cell["lines"] == 1 for cell in view["numericLines"]),
                "Table label/number wrapping mismatch",
            )
            need(
                view["dimensions"]["document"] <= view["width"],
                "Document overflow recorded",
            )
            for state in ["closed", "revealed"]:
                need(not view[state]["violations"], "Scoped axe violation recorded")
                incomplete = view[state]["incomplete"]
                if view["width"] == 1440:
                    need(not incomplete, "Unexpected wide incomplete result")
                else:
                    need(
                        len(incomplete) == 1
                        and incomplete[0]["id"] == "color-contrast"
                        and len(incomplete[0]["nodes"]) == 1,
                        "Unexpected narrow incomplete result",
                    )
                    need(
                        incomplete[0]["nodes"][0]["target"]
                        == data["viewports"][1]["closed"]["incomplete"][0]["nodes"][0][
                            "target"
                        ],
                        "Answer-state contrast target changed",
                    )

    rendered(browser)
    contrast = json.loads((here / "contrast.json").read_text())
    samples = contrast["samples"]
    need(
        contrast["status"] == "passed bounded colour probe"
        and len(samples) == 2
        and [s["endpoint"] for s in samples] == ["left", "right"],
        "Contrast endpoint coverage missing",
    )
    target = browser["viewports"][1]["closed"]["incomplete"][0]["nodes"][0]["target"][0]
    need(
        all(s["selector"] == target and s["ratio"] >= 4.5 for s in samples)
        and samples[1]["scrollLeft"] > samples[0]["scrollLeft"],
        "Clipped-line contrast qualification missing",
    )
    red = json.loads((here / "known-red/rejection.json").read_text())
    wrong = json.loads((here / "known-red/wrong-trace.json").read_text())
    need(
        red["exit_code"] != 0
        and "Wrong policy loses a later whole-pixel move" in red["actual_failure"]
        and wrong == accepted["wrong_policy"],
        "Wrong policy rejection missing",
    )
    controls = {}
    for label in ["wrong_source_hash", "changed_rendered_cell"]:
        try:
            if label == "wrong_source_hash":
                bad = dict(ids["proposed_website_sha256"])
                bad[next(iter(bad))] = "0" * 64
                proposed(bad)
            else:
                bad = copy.deepcopy(browser)
                bad["viewports"][0]["rows"][0][1] = "0"
                rendered(bad)
        except ValueError as error:
            controls[label] = str(error)
        else:
            raise ValueError("Corrupt evidence accepted: " + label)
    website = json.loads((here / "website-results.json").read_text())
    need(
        website["build_exit"] == website["check_exit"] == 0
        and website["tests_passed"] == 237,
        "Website checks missing",
    )
    links = []
    for path in [
        docs / "README.md",
        docs / "audit/2026-10-foundations-coverage.md",
        here / "REPORT.md",
    ]:
        for target in re.findall(r"\]\(([^)]+)\)", path.read_text()):
            if ":" in target or target.startswith("#"):
                continue
            destination = path.parent / target.split("#")[0]
            links.append(destination)
            if destination not in [here / "validation.json", here / "SHA256SUMS"]:
                need(destination.exists(), "Missing local link: " + target)
    report = {
        "status": "passed source/model/browser evidence checks",
        "finite_model_rechecks": 6,
        "browser_viewports": 2,
        "keyboard_behaviour_groups": 10,
        "local_links": len(links),
        "wrong_policy_exit": red["exit_code"],
        "negative_controls_rejected": controls,
        "contrast_samples": 2,
        "limits": "Selected local page and retained model evidence; not target execution, physical-device/screen-reader use, motion quality or learner validation.",
    }
    (here / "validation.json").write_text(json.dumps(report, indent=2) + "\n")
    files = sorted(
        p
        for p in here.rglob("*")
        if p.is_file() and p.name != "SHA256SUMS" and "__pycache__" not in p.parts
    )
    need(len(files) >= 18, "Unexpectedly small evidence set")
    (here / "SHA256SUMS").write_text(
        "".join(sha(p) + "  " + str(p.relative_to(here)) + "\n" for p in files)
    )
    need(all(p.exists() for p in links), "Generated evidence link missing")
    print(json.dumps(report, indent=2))
    print("Manifest entries:", len(files))


if __name__ == "__main__":
    main()
