"""Verify retained identities and counts; this does not execute curriculum samples."""

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
        raise ValueError(message)


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def verify_registry(registry: dict) -> None:
    records = registry["records"]
    require(len(records) == 21, "Expected 21 retained reports")
    require(
        sum(r["kind"] == "bounded-pilot" for r in records) == 16,
        "Expected sixteen pilot reports",
    )
    require(len({r["path"] for r in records}) == 21, "Duplicate report path")
    for record in records:
        path = DOCS / record["path"]
        require(
            digest(path.read_bytes()) == record["sha256"],
            f"Report hash mismatch: {path}",
        )
        baseline = subprocess.check_output(
            ["git", "show", f"{registry['docs_revision']}:{record['path']}"],
            cwd=DOCS,
        )
        require(digest(baseline) == record["sha256"], "Docs baseline mismatch")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--website", type=Path, required=True)
    args = parser.parse_args()
    registry = json.loads((HERE / "report-registry.json").read_text())
    verify_registry(registry)
    negatives = []
    for label, mutation in [("empty registry", "empty"), ("wrong hash", "hash")]:
        damaged = json.loads(json.dumps(registry))
        if mutation == "empty":
            damaged["records"] = []
        else:
            damaged["records"][0]["sha256"] = "0" * 64
        try:
            verify_registry(damaged)
        except ValueError:
            negatives.append(label)
        else:
            raise ValueError(f"Negative control accepted: {label}")
    inventory = json.loads((HERE / "source-inventory.json").read_text())
    files = inventory["files"]
    require(len(files) == 61, "Expected 61 source files")
    require(len({f["path"] for f in files}) == 61, "Duplicate source path")
    foundation = [f for f in files if "/foundations/" in f["path"]]
    maths = [f for f in files if "/craft/maths-for-games/" in f["path"]]
    require(
        sum(Path(f["path"]).name.startswith("unit-") for f in foundation) == 39,
        "Expected 39 Foundations units",
    )
    require(
        sum(Path(f["path"]).name == "index.mdx" for f in foundation) == 10,
        "Expected ten Foundations overviews",
    )
    require(len(maths) == 12, "Expected eleven maths units and overview")
    revision = inventory["website_revision"]
    tree = subprocess.check_output(
        [
            "git",
            "ls-tree",
            "-r",
            "--name-only",
            revision,
            "--",
            "src/content/curriculum/foundations/",
            "src/content/curriculum/craft/maths-for-games/",
            "src/content/curriculum/craft/dice-roller/",
        ],
        cwd=args.website,
        text=True,
    )
    require(
        {p for p in tree.splitlines() if p.endswith(".mdx")}
        == {f["path"] for f in files},
        "Inventory differs from Git tree",
    )
    for source in files:
        content = subprocess.check_output(
            ["git", "show", f"{revision}:{source['path']}"],
            cwd=args.website,
        )
        require(digest(content) == source["sha256"], "Website source hash mismatch")
    for number in (114, 115, 124):
        issue = json.loads((HERE / f"issue-{number}.json").read_text())
        require(
            issue["number"] == number
            and issue["state"] == "OPEN"
            and len(issue["body"]) > 200,
            "Invalid parent snapshot",
        )
        live = json.loads(
            subprocess.check_output(
                [
                    "gh",
                    "issue",
                    "view",
                    str(number),
                    "-R",
                    "stevehill1981/198x",
                    "--json",
                    "body,state,url",
                ],
                text=True,
            )
        )
        require(
            all(live[k] == issue[k] for k in ("body", "state", "url")),
            "Parent criteria/state changed",
        )
    followups = json.loads((HERE / "follow-ups.json").read_text())
    require(len(followups) == 4, "Expected four follow-ups")
    for issue in followups:
        live = json.loads(
            subprocess.check_output(
                ["gh", "issue", "view", issue["url"], "--json", "body,title,state"],
                text=True,
            )
        )
        require(
            live["state"] == "OPEN"
            and live["title"] == issue["title"]
            and live["body"].strip() == (HERE / issue["body_file"]).read_text().strip(),
            "Follow-up differs from retained body",
        )
    links = []
    paths = [
        HERE / "REPORT.md",
        DOCS / "README.md",
        DOCS / "audit/2026-10-foundations-coverage.md",
    ]
    for path in paths:
        for target in re.findall(r"\]\(([^)]+)\)", path.read_text()):
            if "://" in target or target.startswith("#"):
                continue
            local = path.parent / target.split("#")[0]
            require(local.exists(), f"Missing local link: {path}: {target}")
            links.append(str(local.relative_to(DOCS)))
    require(len(links) >= 25, "Expected positive local-link coverage")
    result = {
        "status": "pass",
        "website_revision": revision,
        "docs_evidence_revision": registry["docs_revision"],
        "reports": 21,
        "bounded_pilots": 16,
        "source_files": 61,
        "foundations_units": 39,
        "foundations_modules": 10,
        "maths_units": 11,
        "parent_snapshots_verified": 3,
        "followups_verified": 4,
        "local_links_checked": len(links),
        "negative_controls_rejected": negatives,
        "runtime_checks_rerun": False,
        "learner_observations": 0,
    }
    (HERE / "validation.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
