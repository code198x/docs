"""Validate a drawing inventory against its pinned Git objects and issue ledger."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import subprocess
from pathlib import Path


def git_text(repo: Path, revision: str, path: str) -> str:
    return subprocess.check_output(
        ["git", "show", f"{revision}:{path}"], cwd=repo, text=True, timeout=20
    )


def verify(samples: Path, website: Path, audit: Path) -> dict[str, int]:
    inventory = json.loads((audit / "inventory.json").read_text())
    evidence = json.loads((audit / "evidence.json").read_text())
    registry = json.loads(
        git_text(
            samples,
            inventory["revisions"]["code-samples"],
            "docs/capability-coverage.json",
        )
    )
    rows = inventory["systems"]
    ids = [r["machine_id"] for r in rows]
    expected = {r["machine_id"] for r in registry["registry"]["systems"]}
    if len(ids) != 30 or len(set(ids)) != 30 or set(ids) != expected:
        raise ValueError("Incomplete or duplicate 30-system inventory")
    refs = {r["id"]: r for r in evidence}
    if len(refs) != len(evidence):
        raise ValueError("Duplicate evidence identity")
    repos = {"code198x/code-samples": samples, "code198x/website": website}
    for e in evidence:
        source = git_text(repos[e["repo"]], e["revision"], e["path"])
        if hashlib.sha256(source.encode()).hexdigest() != e["sha256"]:
            raise ValueError("Source hash differs: " + e["id"])
        if not 1 <= e["line"] <= len(source.splitlines()):
            raise ValueError("Invalid line anchor: " + e["id"])
        url = f"https://github.com/{e['repo']}/blob/{e['revision']}/{e['path']}#L{e['line']}"
        if e["url"] != url:
            raise ValueError("Source link differs: " + e["id"])
    for row in rows:
        if not row["evidence"] or not set(row["evidence"]) <= set(refs):
            raise ValueError("Missing machine evidence: " + row["machine_id"])
        if set(row["capabilities"]) != {
            "pixels",
            "lines_spans",
            "rectangles",
            "curves_fills",
            "grid_characters",
            "pixel_text",
            "text_layout_scale",
        }:
            raise ValueError("Missing drawing axis")
    if [sum(r["region"] == mark for r in rows) for mark in ["R", "D", "G"]] != [
        17,
        4,
        9,
    ]:
        raise ValueError("Published/draft region scopes conflated")
    with (audit / "matrix.csv").open() as f:
        matrix = list(csv.DictReader(f))
    if len(matrix) != 30 or {r["machine_id"] for r in matrix} != expected:
        raise ValueError("CSV coverage differs")
    for row in rows:
        csv_row = next(r for r in matrix if r["machine_id"] == row["machine_id"])
        if any(csv_row[k] != v for k, v in row["capabilities"].items()):
            raise ValueError("CSV status differs: " + row["machine_id"])
    issues = json.loads((audit / "issues.json").read_text())
    if len(issues["created"]) != len({i["url"] for i in issues["created"]}):
        raise ValueError("Duplicate created issue")
    expected_keys = {
        "parent",
        "pixels",
        "glyphs",
        "geometry",
        "pixel-text",
        "layout",
        "bitmap-ports",
        "glyph-ports",
        "character-alternatives",
        "raster",
        "maths",
    }
    if (
        len(issues["created"]) != 11
        or {i["key"] for i in issues["created"]} != expected_keys
    ):
        raise ValueError("Incomplete drawing-family issue ledger")
    parent = issues["drawing_parent"]["url"]
    if any(i["parent"] != parent for i in issues["created"] if i["url"] != parent):
        raise ValueError("Child parent link missing")
    return {
        "systems": 30,
        "source_records": len(evidence),
        "created_issues": len(issues["created"]),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--samples", required=True, type=Path)
    parser.add_argument("--website", required=True, type=Path)
    args = parser.parse_args()
    print(verify(args.samples, args.website, Path(__file__).resolve().parent))
