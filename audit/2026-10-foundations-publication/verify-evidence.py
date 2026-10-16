"""Validate this declared live surface and reject incomplete green records."""

import argparse
import copy
import hashlib
import json
import re
import subprocess
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent


def read(name: str) -> Any:
    return json.loads((ROOT / name).read_text())


def check_live(source: dict[str, Any], report: dict[str, Any]) -> None:
    assert report["status"] == "passed" and report["mode"] == "actual"
    assert report["base"] == "https://code198x.com" and report["errors"] == []
    pages = source["pages"]
    assert len(pages) == 49 and len({page["route"] for page in pages}) == 49
    assert sum(page["kind"] == "unit" for page in pages) == 39
    assert sum(page["kind"] == "overview" for page in pages) == 10
    assert all(page["questions"] + len(page["summaries"]) > 0 for page in pages if page["kind"] == "unit")
    expected = {(page["route"], width) for page in pages for width in [390, 1440]}
    cases = report["cases"]
    assert len(cases) == 98 and {(case["route"], case["width"]) for case in cases} == expected
    by_route = {page["route"]: page for page in pages}
    for case in cases:
        page = by_route[case["route"]]
        assert case["http"] == 200 and case["questionCount"] == page["questions"]
        assert case["dimensions"]["document"] <= case["width"]
        assert re.fullmatch(r"[a-f0-9]{64}", case["responseSha256"])
        expected_opens = [{"kind": "Question", "index": index} for index in range(page["questions"])]
        expected_opens += [{"kind": "details", "summary": text} for text in page["summaries"]]
        assert case["opened"] == expected_opens
    assert sum(len(case["opened"]) for case in cases) == 104
    links = report["links"]
    assert len(links) == 385 and len({link["href"] for link in links}) == 385
    assert sum(bool(link["fragment"]) for link in links) == 274
    for link in links:
        assert link["passed"] and not link.get("error")
        assert 200 <= link["http"] < 300 and link["fragmentFound"] is not False
        assert link["from"] and set(link["from"]) <= set(by_route)
        assert re.fullmatch(r"[a-f0-9]{64}", link["responseSha256"])
        if link["fragment"]:
            assert link["fragmentFound"] is True


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--website", required=True, type=Path)
    args = parser.parse_args()
    source = read("source.json")
    for page in source["pages"]:
        data = subprocess.check_output(["git", "-C", str(args.website), "show", source["websiteRevision"] + ":" + page["path"]])
        assert hashlib.sha256(data).hexdigest() == page["sha256"], page["path"]
        text = data.decode()
        assert len(re.findall(r"<Question\b", text)) == page["questions"]
        assert len(re.findall(r"<summary[^>]*>", text)) == len(page["summaries"])
    report = read("live/results.json")
    assert report["sourceSha256"] == hashlib.sha256((ROOT / "source.json").read_bytes()).hexdigest()
    check_live(source, report)
    assert read("run.json")["exit"] == 0
    failed = read("known-red-run.json")
    assert failed["exit"] != 0 and "Question count /foundations/basics/" in failed["stderr"]
    assert read("known-red/results.json")["status"] == "failed"
    assert read("initial-run.json")["exit"] != 0
    assert "Missing/ambiguous authored disclosure" in read("initial-typography-mismatch/results.json")["failure"]
    for kind in ["case", "answer"]:
        broken = copy.deepcopy(report)
        if kind == "case":
            broken["cases"].pop()
        else:
            next(case for case in broken["cases"] if case["opened"])["opened"].pop()
        try:
            check_live(source, broken)
        except AssertionError:
            pass
        else:
            raise AssertionError("Incomplete green record accepted: " + kind)
    links = 0
    for target in re.findall(r"\]\(([^)]+)\)", (ROOT / "REPORT.md").read_text()):
        if "://" not in target and not target.startswith("#"):
            assert (ROOT / target.split("#")[0]).exists(), target
            links += 1
    assert links > 10
    manifest = (ROOT / "SHA256SUMS").read_text().splitlines()
    assert manifest
    for entry in manifest:
        digest, path = entry.split("  ", 1)
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest, path
    print(json.dumps({"status": "passed", "sourcePages": 49, "viewportCases": 98, "keyboardOpens": 104, "links": 385, "fragments": 274, "knownRedRejected": True, "missingCaseRejected": True, "missingAnswerRejected": True, "manifestEntries": len(manifest)}))


if __name__ == "__main__":
    main()
