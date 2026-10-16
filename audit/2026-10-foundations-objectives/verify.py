"""Check retained source coverage and references, not educational effectiveness."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import platform
import re
import subprocess
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent


def git(site: Path, *args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=site, text=True)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def validate(record: dict[str, Any], sources: dict[str, str]) -> dict[str, int]:
    catalogue = record["catalogue"]
    require(sources[catalogue["path"]] == catalogue["text"], "Catalogue text mismatch")
    require(
        hashlib.sha256(catalogue["text"].encode()).hexdigest() == catalogue["sha256"],
        "Catalogue hash mismatch",
    )
    units = record["units"]
    modules = record["modules"]
    expected_units = {p for p in sources if re.search(r"/unit-\d+\.mdx$", p)}
    expected_modules = {p for p in sources if p.endswith("/index.mdx")}
    require(len(expected_units) == 39, "Expected 39 authored units")
    require(len(expected_modules) == 10, "Expected ten authored overviews")
    require(len(units) == len(expected_units), "Unit count mismatch")
    require(len(modules) == len(expected_modules), "Overview count mismatch")
    require({u["path"] for u in units} == expected_units, "Unit source-set mismatch")
    require(
        {m["path"] for m in modules} == expected_modules, "Module source-set mismatch"
    )
    ids = {u["id"] for u in units}
    require(len(ids) == len(units), "Duplicate unit ID")
    prompts = 0
    for item in units + modules:
        source = sources[item["path"]]
        require(
            hashlib.sha256(source.encode()).hexdigest() == item["sha256"],
            "Source hash mismatch: " + item["path"],
        )
        require(f'title: "{item["title"]}"' in source, "Title mismatch")
        expected_url = (
            "https://github.com/code198x/website/blob/"
            + record["website_revision"]
            + "/"
            + item["path"]
        )
        require(item["source_url"] == expected_url, "Source URL mismatch")
        if "id" not in item:
            require(
                item["body"] == source.split("---", 2)[2].strip(),
                "Overview body mismatch",
            )
            continue
        module = item["path"].split("/")[-2]
        number = re.search(r"unit-(\d+)\.mdx$", item["path"])
        require(number is not None, "Unit filename missing")
        require(item["id"] == module + "/" + number.group(1), "ID/path mismatch")
        for field in (
            "goal_synthesis",
            "knowledge_used_inference",
            "local_support_review",
        ):
            require(bool(item[field].strip()), "Empty reviewer field: " + field)
        require(set(item["suggested_support_units"]) <= ids, "Unknown support unit")
        require(item["opening_excerpt"] in source, "Opening excerpt mismatch")
        for excerpt in [item["objective_evidence"], *item["explicit_prompt_evidence"]]:
            require(excerpt["text"] in source, "Source excerpt mismatch")
            suffix = "\n".join(source.splitlines()[excerpt["line"] - 1 :])
            require(suffix.startswith(excerpt["text"]), "Excerpt line mismatch")
        expected_prompts = re.findall(
            r"<summary>.*?</summary>|<Question\b[^>]*>", source, re.DOTALL
        )
        require(
            sorted(expected_prompts)
            == sorted(x["text"] for x in item["explicit_prompt_evidence"]),
            "Prompt extraction mismatch",
        )
        expected_links = [
            {"label": m.group(1), "target": m.group(2)}
            for m in re.finditer(r"\[([^\]]+)\]\(([^)]+)\)", source)
        ]
        require(item["authored_links"] == expected_links, "Authored links mismatch")
        prompts += bool(expected_prompts)
    return {
        "units": len(units),
        "overviews": len(modules),
        "units_with_explicit_prompt_markup": prompts,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--website",
        type=Path,
        required=True,
        help="Existing website Git repo containing the retained revision",
    )
    args = parser.parse_args()
    record = json.loads((HERE / "units.json").read_text())
    revision = record["website_revision"]
    paths = git(
        args.website,
        "ls-tree",
        "-r",
        "--name-only",
        revision,
        "src/content/curriculum/foundations",
    ).splitlines()
    sources = {
        p: git(args.website, "show", revision + ":" + p)
        for p in paths
        if p.endswith(".mdx")
    }
    catalogue_path = record["catalogue"]["path"]
    sources[catalogue_path] = git(args.website, "show", revision + ":" + catalogue_path)
    result = validate(record, sources)
    controls: dict[str, str] = {}
    for name in ("missing_unit", "wrong_hash", "wrong_excerpt", "unknown_support"):
        bad = copy.deepcopy(record)
        if name == "missing_unit":
            bad["units"].pop()
        elif name == "wrong_hash":
            bad["units"][0]["sha256"] = "0" * 64
        elif name == "wrong_excerpt":
            bad["units"][0]["objective_evidence"]["text"] = "invented source excerpt"
        else:
            bad["units"][0]["suggested_support_units"] = ["unknown/99"]
        try:
            validate(bad, sources)
        except ValueError as error:
            controls[name] = str(error)
        else:
            raise ValueError("Negative control accepted: " + name)
    docs = HERE.parent.parent
    links = 0
    for path in [
        HERE / "MAP.md",
        HERE / "REPORT.md",
        docs / "README.md",
        docs / "audit/2026-10-foundations-coverage.md",
        docs / "plans/2026-10-16-foundations-objective-map.md",
    ]:
        for target in re.findall(r"\]\(([^)]+)\)", path.read_text()):
            if ":" in target or target.startswith("#"):
                continue
            require(
                (path.parent / target.split("#")[0]).exists(),
                "Missing local link: " + target,
            )
            links += 1
    report = {
        "status": "passed source-record checks",
        **result,
        "source_files_hashed": len(sources),
        "local_file_links": links,
        "negative_controls_rejected": controls,
        "python": platform.python_version(),
        "website_revision": revision,
        "runtime_examples_rerun": 0,
        "learner_trials": 0,
        "limits": "Coverage, provenance and reference checks only. Reviewer goals, "
        "knowledge and support judgements are not mechanically certified.",
    }
    (HERE / "validation.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
