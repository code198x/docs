"""Validate retained compound-condition evidence and deliberate failures."""

import argparse
import copy
import hashlib
import json
import re
import subprocess
from pathlib import Path
from typing import Any

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--website", type=Path, required=True)
args = parser.parse_args()
p = Path(__file__).resolve().parent
docs = p.parent.parent
site = args.website
i = json.loads((p / "identities.json").read_text())
n = json.loads((p / "native-conditions.json").read_text())
m = json.loads((p / "model-conditions.json").read_text())
b = json.loads((p / "browser-after.json").read_text())


def need(v: bool, msg: str) -> None:
    if not v:
        raise ValueError(msg)


def source(hashes: dict[str, str]) -> None:
    for name, expected in hashes.items():
        actual = subprocess.check_output(
            ["git", "show", i["website_baseline"] + ":" + name], cwd=site
        )
        need(hashlib.sha256(actual).hexdigest() == expected, "Source hash mismatch")


source(i["source_sha256"])
for name, h in i["proposed_source_sha256"].items():
    need(
        hashlib.sha256((site / name).read_bytes()).hexdigest() == h,
        "Proposed source hash mismatch",
    )
for name, h in i["specification_sha256"].items():
    need(
        hashlib.sha256((docs / name).read_bytes()).hexdigest() == h,
        "Specification hash mismatch",
    )
need(
    hashlib.sha256((p / "verify-conditions.py").read_bytes()).hexdigest()
    == n["verifier_sha256"]
    == i["native_verifier_sha256"],
    "Native verifier identity mismatch",
)
need(
    hashlib.sha256(
        (site / "scripts/verification/compound-conditions-pilot.mjs").read_bytes()
    ).hexdigest()
    == i["browser_verifier_sha256"],
    "Browser verifier identity mismatch",
)


def native(data: dict[str, Any]) -> None:
    need(
        data["status"] == "passed"
        and len(data["numeric"]) == 11
        and len(data["shooting"]) == 8,
        "Native count mismatch",
    )
    count = 0
    for actual, model in zip(data["numeric"], m["numeric"], strict=True):
        need(actual["input"] == model["input"], "Native input mismatch")
        wanted = [
            model[k] for k in ["inside", "outside", "wrong_or", "wrong_outside_and"]
        ]
        extra = [
            model[k]
            for k in ["whole_and_inside", "positive", "at_least_one", "three_or_seven"]
        ] + [1]
        for item, expected in [
            (actual, wanted),
            (actual["validation_and_shorthand"], extra),
        ]:
            need(
                item["actual"] == item["expected"] == expected, "Native result mismatch"
            )
            need(
                len(item["rows"]) == 24
                and item["rows"][0] == ",".join(map(str, expected))
                and item["rows"][-1].startswith("0 OK"),
                "Native transcript missing or different",
            )
            count += len(expected)
    for actual, model in zip(data["shooting"], m["shooting"], strict=True):
        expected = [model["grouped"], model["ungrouped"]]
        need(
            actual["actual"] == actual["expected"] == expected,
            "Native grouping mismatch",
        )
        need(
            len(actual["rows"]) == 24
            and actual["rows"][0] == ",".join(map(str, expected))
            and actual["rows"][-1].startswith("0 OK"),
            "Native transcript missing or different",
        )
        count += 2
    need(count == data["output_numbers"] == 115, "Native output count mismatch")


native(n)
red = {}
for label in ["wrong_source_hash", "missing_native_transcript"]:
    try:
        if label == "wrong_source_hash":
            bad = dict(i["source_sha256"])
            bad[next(iter(bad))] = "0" * 64
            source(bad)
        else:
            bad = copy.deepcopy(n)
            bad["numeric"][0]["rows"] = []
            native(bad)
    except ValueError as e:
        red[label] = str(e)
    else:
        raise AssertionError("Bad evidence accepted: " + label)
known = json.loads((p / "known-red-native/rejection.json").read_text())
need(known["exit_code"] != 0, "Native wrong guard did not fail")
need(
    b["status"] == "passed"
    and len(b["viewports"]) == 2
    and len(b["checks"]) == 6
    and not b["errors"],
    "Browser evidence missing",
)
need(
    len(b["contrastProbe"]["samples"]) == 8
    and all(x["ratio"] >= 4.5 for x in b["contrastProbe"]["samples"]),
    "Contrast evidence missing",
)
links = 0
for f in [
    docs / "README.md",
    docs / "audit/2026-10-foundations-coverage.md",
    p / "REPORT.md",
    p / "LEARNER-TASKS.md",
    p / "ASSESSOR.md",
]:
    for target in re.findall(r"\]\(([^)]+)\)", f.read_text()):
        if ":" in target or target.startswith("#"):
            continue
        need(
            (f.parent / target.split("#")[0]).exists(), "Local link missing: " + target
        )
        links += 1
out = {
    "status": "passed evidence checks",
    "source_files": 2,
    "specifications": 3,
    "native_printed_numbers": 115,
    "numeric_cases": 11,
    "shooting_rows": 8,
    "browser_viewports": 2,
    "keyboard_behaviour_groups": 6,
    "contrast_samples": 8,
    "local_links": links,
    "negative_evidence_controls": red,
    "native_wrong_guard_exit": known["exit_code"],
    "limits": "Retained evidence/source structure and agreement checks; not an independent runtime, screen-reader or learner trial.",
}
(p / "validation.json").write_text(json.dumps(out, indent=2) + "\n")
files = sorted(
    x
    for x in p.rglob("*")
    if x.is_file() and x.name != "SHA256SUMS" and "__pycache__" not in x.parts
)
need(len(files) > 20, "Evidence set unexpectedly empty")
(p / "SHA256SUMS").write_text(
    "".join(
        hashlib.sha256(x.read_bytes()).hexdigest() + "  " + str(x.relative_to(p)) + "\n"
        for x in files
    )
)
print(json.dumps(out, indent=2))
print("Manifest entries:", len(files))
