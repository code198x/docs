"""Check this retained source inventory against the pinned Git objects, not HEAD."""

from __future__ import annotations

import argparse
import csv
import json
import re
import subprocess
from pathlib import Path


def require(value: bool, message: str) -> None:
    if not value:
        raise AssertionError(message)


def tree(repo: Path, revision: str) -> set[str]:
    result = subprocess.run(
        ["git", "-C", str(repo), "ls-tree", "-r", "--name-only", revision],
        check=True,
        capture_output=True,
        text=True,
        timeout=30,
    )
    names = set(result.stdout.splitlines())
    require(bool(names), f"Empty tree: {repo} {revision}")
    return names


def check_paths(paths: set[str], expected: set[str], label: str) -> None:
    require(bool(paths), f"No paths checked: {label}")
    require(paths <= expected, f"{label}: missing {sorted(paths - expected)}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ["website", "samples", "docs", "emulator"]:
        parser.add_argument("--" + name, type=Path, required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    load = lambda name: json.loads((root / (name + ".json")).read_text())
    baselines = load("baselines")
    repos = {
        "website": args.website,
        "code-samples": args.samples,
        "docs": args.docs,
        "emulator_source": args.emulator,
        "website-prototype": args.website,
        "samples-prototype": args.samples,
    }
    trees = {k: tree(repos[k], b["revision"]) for k, b in baselines.items()}
    for name in ["patterns", "lessons", "modules", "sample-sources", "capabilities"]:
        records = load(name)
        require(bool(records), f"Empty {name}")
        with (root / (name + ".csv")).open(newline="") as f:
            csv_records = list(csv.DictReader(f))
        require(len(records) == len(csv_records), f"CSV count mismatch: {name}")
        for row, csv_row in zip(records, csv_records, strict=True):
            for key, value in row.items():
                expected = (
                    "; ".join(value)
                    if isinstance(value, list)
                    else ""
                    if value is None
                    else str(value)
                )
                require(csv_row[key] == expected, f"CSV value mismatch: {name}/{key}")
    patterns, lessons, samples, cells = (
        load(n) for n in ["patterns", "lessons", "sample-sources", "capabilities"]
    )
    for label, rows, base, prefix, suffix in [
        ("patterns", patterns, "website", "src/content/patterns/", ".mdx"),
        ("lessons", lessons, "website", "src/content/curriculum/", ".mdx"),
    ]:
        paths = {row["path"] for row in rows}
        expected = {
            p
            for p in trees[base]
            if p.startswith(prefix)
            and p.endswith(suffix)
            and (label != "lessons" or Path(p).name.startswith("unit-"))
        }
        require(paths == expected, f"Enumeration differs from pinned tree: {label}")
    check_paths({r["path"] for r in samples}, trees["code-samples"], "sample manifest")
    includes = {p for row in patterns + lessons for p in row["includes"]}
    check_paths(includes, trees["code-samples"], "CodeFromFile references")
    require(len(cells) == 68, "Expected 17 areas across four core systems")
    require(
        len({(r["system"], r["family"]) for r in cells}) == len(cells),
        "Duplicate matrix cell",
    )
    check_paths(
        {r["lesson_anchor"] for r in cells if r["lesson_anchor"]},
        trees["website"],
        "lesson anchors",
    )
    check_paths(
        {p for r in cells for p in r["source_anchors"]},
        trees["code-samples"],
        "sample anchors",
    )
    for row in load("wider-systems"):
        paths = row["runtime_test_sources"] + (
            [row["profile_source"]] if row["profile_source"] else []
        )
        if paths:
            check_paths(set(paths), trees["emulator_source"], row["system"])
        expected = {
            p for p in trees["code-samples"] if p.startswith(row["sample_prefix"] + "/")
        }
        require(
            len(expected) == row["tracked_sample_files"], "Wider sample count mismatch"
        )
        require(
            len([p for p in expected if not p.endswith(".gitkeep")])
            == row["authored_sample_files"],
            "Authored wider sample count mismatch",
        )
    links = re.findall(
        r"https://github.com/([^/]+/[^/]+)/blob/([a-f0-9]{40})/([^\s)]+)",
        (root / "README.md").read_text(),
    )
    require(len(links) > 20, "Expected source-linked audit, not a link-free summary")
    for repository, revision, path in links:
        key = next(
            k
            for k, b in baselines.items()
            if b["repository"] == repository and b["revision"] == revision
        )
        require(path in trees[key], f"Broken source permalink: {path}")
    try:
        check_paths(
            {"__deliberately_missing_inventory_source__"},
            trees["website"],
            "negative control",
        )
    except AssertionError:
        pass
    else:
        raise AssertionError("Missing-source negative control was accepted")
    print(
        f"PASS {len(patterns)} patterns, {len(lessons)} unit files, {len(samples)} source files, {len(cells)} cells, {len(includes)} include paths, {len(links)} source links; missing-source control rejected"
    )


if __name__ == "__main__":
    main()
