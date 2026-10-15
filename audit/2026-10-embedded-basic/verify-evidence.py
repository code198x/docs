"""Validate retained browser outcomes and identities without claiming a new runtime run."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
DOCS = HERE.parent.parent


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def body(rows: list[str]) -> list[str]:
    visible = [row.rstrip() for row in rows[:22]]
    while visible and not visible[0]:
        visible.pop(0)
    if visible and visible[0] == "Program: greeting":
        visible.pop(0)
    while visible and not visible[0]:
        visible.pop(0)
    return [row for row in visible if row]


def stages(report: dict) -> None:
    require(
        report["status"] == "passed" and len(report["checks"]) == 8,
        "Missing eight positive stages",
    )
    expected = [
        ["ONE", "ONE", "TWO"],
        ["ONE"],
        ["ONE", "ONE", "TWO"],
        ["ONE", "ONE", "TWO"],
        ["ONE", "ONE", "TWO", "TWO"],
        ["ONE", "ONE", "TWO"],
        ["ONE", "ONE", "TWO"],
        ["Hello, Jo", "from the Spectrum"],
    ]
    for index, (case, values) in enumerate(
        zip(report["checks"], expected, strict=True)
    ):
        rows = case["rows"]
        require(len(rows) == 24, "Incomplete screen observation")
        require(body(rows) == values, f"Output differs at stage {index}")
        error = {1: "2 Variable not found, 30:1", 3: "2 Variable not found, 0:1"}.get(
            index
        )
        require(
            any(row.startswith(error or "0 OK") for row in rows),
            f"Missing error/completion at stage {index}",
        )
    require(
        not any(
            row.strip() == "Program: greeting" for row in report["checks"][5]["rows"]
        ),
        "RUN result was not fresh",
    )
    require(
        any(row.strip() == "Program: greeting" for row in report["checks"][6]["rows"]),
        "Restart result could be stale",
    )
    require(not report["errors"], "Page errors recorded")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--website", type=Path, required=True)
    parser.add_argument("--samples", type=Path, required=True)
    args = parser.parse_args()
    report = json.loads((HERE / "browser-results.json").read_text())
    stages(report)
    negatives = []
    for label in ["empty stages", "lost repeated read", "missing wrong-name report"]:
        damaged = json.loads(json.dumps(report))
        if label == "empty stages":
            damaged["checks"] = []
        elif label == "lost repeated read":
            damaged["checks"][0]["rows"][3] = ""
        else:
            damaged["checks"][1]["rows"][23] = "0 OK"
        try:
            stages(damaged)
        except AssertionError:
            negatives.append(label)
        else:
            raise AssertionError(f"Negative control accepted: {label}")
    require(report["knownRed"]["rejected"], "Missing browser known-red rejection")
    ids = json.loads((HERE / "identities.json").read_text())
    for path, expected in ids["website_files"].items():
        content = subprocess.check_output(
            ["git", "show", f"{ids['website_baseline']}:{path}"],
            cwd=args.website,
        )
        require(sha(content) == expected, "Website baseline identity changed")
    require(
        sha((args.website / ids["verifier"]["path"]).read_bytes())
        == ids["verifier"]["sha256"],
        "Verifier identity changed",
    )
    sample = args.samples / ids["sample"]["path"]
    require(
        sha(sample.read_bytes()) == ids["sample"]["sha256"], "Sample identity changed"
    )
    require(
        sample.read_text().rstrip() == report["originalSource"],
        "Live original listing differs from maintained sample",
    )
    require(
        sha(report["originalSource"].encode()) == report["originalSourceSha256"],
        "Live original source hash differs",
    )
    assets = report["assets"]
    require(
        len(assets) == 14
        and all(
            a.get("status") == 200
            and a.get("bytes", 0) > 0
            and len(a.get("sha256", "")) == 64
            for a in assets
        ),
        "Missing served artefact identities",
    )
    require(sum(".wasm" in a["url"] for a in assets) == 1, "Missing live WASM response")
    manifest = json.loads((HERE / "artifacts.json").read_text())
    require(len(manifest) == 23, "Missing retained artefacts")
    for path, expected in manifest.items():
        require(sha((HERE / path).read_bytes()) == expected, "Artefact hash mismatch")
    for attempt, outcome in [
        ("attempt-header", "failed"),
        ("attempt-run-display", "failed"),
        ("initial-six-stage", "passed"),
    ]:
        data = json.loads((HERE / attempt / "browser-results.json").read_text())
        require(data["status"] == outcome, "Missing attempt outcome")
    require(
        report["reconstructedPrematureAssertion"]["status"] == "rejected",
        "Missing reconstructed early-read rejection",
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
    require(links > 30, "Missing meaningful link checks")
    result = {
        "status": "passed",
        "browser_stages": 8,
        "served_assets": 14,
        "retained_artefacts": 23,
        "local_links_checked": links,
        "negative_controls_rejected": negatives,
        "browser_known_red_rejected": True,
        "historical_cause": "unknown",
        "learner_observations": 0,
    }
    (HERE / "validation.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
