"""Independently validate timing statistics, successful machine states and identities."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import statistics
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
DOCS = HERE.parent.parent
LABELS = ["cold-startup", "warm-unchanged", "warm-edited"]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def body(rows: list[str]) -> list[str]:
    values = [row.rstrip() for row in rows[:22]]
    while values and not values[0]:
        values.pop(0)
    if values and values[0] == "Program: greeting":
        values.pop(0)
    return [row for row in values if row]


def validate_results(data: dict) -> None:
    require(
        data["status"] == "passed" and data["count"] == 5 and len(data["trials"]) == 5,
        "Expected five completed trials",
    )
    for index, trial in enumerate(data["trials"], 1):
        require(
            trial["index"] == index
            and trial["status"] == "passed"
            and not trial["errors"],
            "Trial failed or missing",
        )
        require(
            [m["label"] for m in trial["measurements"]] == LABELS,
            "Missing one of three stages",
        )
        for measurement in trial["measurements"]:
            m = measurement
            require(
                m["status"] == "passed"
                and 0 <= m["clickAt"] < m["matchAt"] < m["endAt"],
                "Missing positive action/result boundary",
            )
            require(
                math.isclose(m["clickToResultMs"], m["endAt"] - m["clickAt"]),
                "Click timing differs from actual timestamps",
            )
            require(
                math.isclose(m["matchToEndMs"], m["endAt"] - m["matchAt"]),
                "Match-to-end interval differs",
            )
            require(
                m["incompleteSeen"]
                and any(not o["complete"] for o in m["observations"]),
                "A stale complete transcript could pass",
            )
            require(
                any(
                    o["complete"] and o["atMs"] == m["matchAt"]
                    for o in m["observations"]
                ),
                "Missing complete-output observation",
            )
            expected = (
                f"Hello again {index}" if m["label"] == "warm-edited" else "Welcome"
            )
            require(
                m["expected"] == expected
                and len(m["rows"]) == 24
                and body(m["rows"]) == [expected, "to you", "from the Spectrum"]
                and any(row.startswith("0 OK, 20:1") for row in m["rows"]),
                "Missing actual complete greeting/ROM completion",
            )
            require(
                m["canvas"]["bytes"] == 256 * 48 * 4 and m["canvas"]["colours"] >= 2,
                "Missing rendered text region",
            )
            if m["label"] == "warm-edited":
                require(
                    m["inputAt"] <= m["clickAt"]
                    and math.isclose(m["inputToResultMs"], m["endAt"] - m["inputAt"]),
                    "Input/result boundary differs",
                )
            else:
                require(m["inputAt"] is None, "Unexpected source edit")
        cold, warm, edited = trial["measurements"]
        require(
            cold["canvas"]["fnv"] == warm["canvas"]["fnv"] != edited["canvas"]["fnv"],
            "Unchanged/changed output canvas agreement failed",
        )
        wasm = [n for n in trial["network"] if ".wasm" in n["url"]]
        require(
            len(wasm) == 1
            and wasm[0]["phase"] == "cold-startup"
            and wasm[0]["status"] == 200
            and not wasm[0]["fromDiskCache"]
            and not wasm[0]["fromServiceWorker"]
            and wasm[0]["encodedDataLength"] > 0,
            "Cold cache/network evidence differs",
        )
        require(
            not any(n["phase"].startswith("warm") for n in trial["network"]),
            "Warm same-origin responses were recorded",
        )
        require(
            len(trial["assets"]) == 12
            and all(a["bytes"] > 0 and len(a["sha256"]) == 64 for a in trial["assets"]),
            "Missing served asset identities",
        )
    for label in LABELS:
        values = [
            t["measurements"][LABELS.index(label)]["clickToResultMs"]
            for t in data["trials"]
        ]
        expected = {
            "count": 5,
            "minMs": min(values),
            "medianMs": statistics.median(values),
            "maxMs": max(values),
        }
        require(data["summary"][label] == expected, "Independent statistics disagree")
    control = data["trials"][-1]["negativeControl"]
    require(
        control["status"] == "failed"
        and control["endAt"] is None
        and "clickToResultMs" not in control,
        "Missing result became a latency value",
    )
    require(
        len(
            {
                a["sha256"]
                for t in data["trials"]
                for a in t["assets"]
                if ".wasm" in a["url"]
            }
        )
        == 1,
        "WASM changed during trials",
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--website", type=Path, required=True)
    parser.add_argument("--samples", type=Path, required=True)
    args = parser.parse_args()
    data = json.loads((HERE / "results.json").read_text())
    validate_results(data)
    negatives = []
    for label in [
        "empty trials",
        "missing completion",
        "stale observations",
        "false median",
        "fast missing result",
    ]:
        damaged = json.loads(json.dumps(data))
        if label == "empty trials":
            damaged["trials"] = []
        elif label == "missing completion":
            damaged["trials"][0]["measurements"][0]["rows"][23] = ""
        elif label == "stale observations":
            for observation in damaged["trials"][0]["measurements"][1]["observations"]:
                observation["complete"] = True
        elif label == "false median":
            damaged["summary"]["cold-startup"]["medianMs"] = 0
        else:
            damaged["trials"][-1]["negativeControl"]["clickToResultMs"] = 0
        try:
            validate_results(damaged)
        except AssertionError:
            negatives.append(label)
        else:
            raise AssertionError(f"Known-red accepted: {label}")
    ids = json.loads((HERE / "identities.json").read_text())
    for path, expected in ids["files"].items():
        content = subprocess.check_output(
            ["git", "show", f"{ids['website_baseline']}:{path}"], cwd=args.website
        )
        require(sha(content) == expected, "Source baseline identity changed")
    require(
        sha((args.website / "scripts/verification/embedded-latency.mjs").read_bytes())
        == data["verifierSha256"],
        "Executed verifier identity changed",
    )
    sample = args.samples / ids["sample"]["path"]
    require(
        sha(sample.read_bytes()) == ids["sample"]["sha256"], "Sample identity changed"
    )
    for trial in data["trials"]:
        require(
            trial["originalSource"] == sample.read_text().rstrip()
            and sha(trial["originalSource"].encode()) == trial["originalSourceSha256"],
            "Live maintained listing differs",
        )
    artefacts = json.loads((HERE / "artifacts.json").read_text())
    require(len(artefacts) == 6, "Missing retained artefacts")
    for path, expected in artefacts.items():
        require(
            sha((HERE / path).read_bytes()) == expected, "Artefact identity changed"
        )
    links = 0
    for path in [
        HERE / "REPORT.md",
        DOCS / "README.md",
        DOCS / "audit/2026-10-foundations-coverage.md",
    ]:
        for target in re.findall(r"\]\(([^)]+)\)", path.read_text()):
            if "://" not in target and not target.startswith("#"):
                require(
                    (path.parent / target.split("#")[0]).exists(),
                    f"Missing local link: {target}",
                )
                links += 1
    require(links > 30, "No meaningful link checks")
    result = {
        "status": "passed",
        "trials": 5,
        "successful_timed_stages": 15,
        "statistics_independently_recomputed": True,
        "live_wasm_responses": 5,
        "asset_identity_records": 60,
        "local_links_checked": links,
        "artefacts_hashed": 6,
        "negative_controls_rejected": negatives,
        "live_missing_result_control": "failed without latency",
        "learner_observations": 0,
    }
    (HERE / "validation.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
