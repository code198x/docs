"""Validate this bounded live-publication record and its retained inputs."""

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent
REPORTS = {
    "compound/browser-after.json": 6,
    "loops/browser-counted.json": 6,
    "output/browser.json": 6,
    "interpreter/browser.json": 6,
    "fixed/browser.json": 10,
}


def read(path: str) -> Any:
    return json.loads((ROOT / path).read_text())


def check_record(data: dict[str, Any], count: int) -> None:
    assert data["status"] == "passed"
    assert data["errors"] == []
    assert len(data["checks"]) == count
    assert sorted(view["width"] for view in data["viewports"]) == [390, 1440]
    for view in data["viewports"]:
        assert view["http"] == 200
        assert re.fullmatch(r"[a-f0-9]{64}", view["responseSha256"])


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--website", required=True, type=Path)
    args = parser.parse_args()
    identities = read("identities.json")
    assert identities["base"] == "https://code198x.com"
    for path, expected in identities["files"].items():
        assert hashlib.sha256((args.website / path).read_bytes()).hexdigest() == expected, path
    model_path = ROOT.parent / "2026-10-foundations-evidence-queue/models.json"
    assert hashlib.sha256(model_path.read_bytes()).hexdigest() == identities["acceptedModelsSha256"]
    for path, count in REPORTS.items():
        check_record(read(path), count)
    fixed = read("fixed/browser.json")
    assert fixed["acceptedModelsSha256"] == identities["acceptedModelsSha256"]
    models = json.loads(model_path.read_text())
    half = next(case for case in models["cases"] if case["label"] == "half-step")
    rows = [[str(row["update"]), str(row["updated"]), str(row["updated"] / 256).removesuffix(".0"), str(row["drawn"])] for row in half["rows"]]
    for view in fixed["viewports"]:
        assert view["rows"] == rows
        assert view["outputs"] == ["1.5", "512"]
    guide = read("guide/results.json")
    assert guide["status"] == "passed" and guide["mode"] == "pages"
    assert len(guide["pages"]) == 12 and len(guide["checks"]) == 2 and not guide["errors"]
    expected_routes = {"/try/", "/try/spectrum-basic/", "/try/spectrum-assembly/", "/try/parents-and-teachers/", "/try/session-sheet/", "/try/feedback/"}
    assert {(page["route"], page["width"]) for page in guide["pages"]} == {(route, width) for route in expected_routes for width in [390, 1440]}
    assert all(not page["overflow"] and not page["violations"] and not page["incomplete"] for page in guide["pages"])
    samples = read("compound/browser-after.json")["contrastProbe"]["samples"]
    assert len(samples) == 8 and min(item["ratio"] for item in samples) >= 4.5
    samples = read("fixed/contrast.json")["samples"]
    assert len(samples) == 2 and min(item["ratio"] for item in samples) >= 4.5
    assert samples[1]["scrollLeft"] > samples[0]["scrollLeft"]
    runs = read("runs.json")
    assert len(runs) == 7 and all(run["exit"] == 0 for run in runs)
    negative = read("known-red/rejection.json")
    assert negative["exit"] != 0
    assert "Rendered state/full/drawn values differ from accepted model" in negative["stderr"]
    assert read("known-red/browser.json")["status"] == "failed"
    deployment = read("deployment.json")
    assert deployment["headSha"] == identities["websiteMain"]
    assert deployment["status"] == "completed" and deployment["conclusion"] == "success"
    # A missing viewport must fail the record validator, even with a green status.
    broken = dict(fixed, viewports=fixed["viewports"][:1])
    try:
        check_record(broken, 10)
    except AssertionError:
        pass
    else:
        raise AssertionError("Missing viewport accepted")
    manifest = (ROOT / "SHA256SUMS").read_text().splitlines()
    assert manifest
    for line in manifest:
        digest, path = line.split("  ", 1)
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest, path
    print(json.dumps({"status": "passed", "lessonViewportCases": 10, "guideViewportCases": 12, "behaviourGroups": 36, "manifestEntries": len(manifest), "negativeControls": ["wrong live table expectation rejected", "missing viewport rejected"]}))


if __name__ == "__main__":
    main()
