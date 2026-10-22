"""Check reconciliation evidence and scope boundaries, not educational effectiveness."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from copy import deepcopy
from pathlib import Path
from typing import Any
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent
DOCS = ROOT.parents[1]
EXPECTED = {
    114: {
        "inventory",
        "sample",
        "findings",
        "assessments",
        "evidence",
        "results",
        "owners",
        "review",
        "architecture",
    },
    115: {
        "pathways",
        "execution",
        "transfer",
        "learners",
        "friction",
        "results",
        "owners",
        "review",
        "architecture",
    },
    116: {
        "inventory",
        "concepts",
        "standards",
        "constraints",
        "results",
        "owners",
        "review",
        "architecture",
    },
    124: {
        "journey",
        "coverage",
        "learner-outcomes",
        "identities",
        "priorities",
        "improvement",
        "access",
    },
}


def read_json(path: Path) -> Any:
    return json.loads(path.read_text())


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git(repo: Path, *args: str) -> bytes:
    return subprocess.check_output(["git", *args], cwd=repo)


PRIVATE_REPO = "stevehill1981/198x"


def private_hashes() -> dict[str, str]:
    """Hashes of the private umbrella issue snapshots.

    The umbrella repository is private, so its issue text is not published
    with this audit. `private-snapshots.sha256` keeps each removed snapshot's
    hash; restoring a snapshot at its path re-enables the checks that read it.
    """
    lines = (ROOT / "private-snapshots.sha256").read_text().splitlines()
    return {path: digest for digest, path in (line.split("  ", 1) for line in lines)}


def snapshot_path(repo: str, kind: str, number: int) -> str:
    return f"snapshots/{repo.replace('/', '-')}-{kind}-{number}.json"


def snapshot(repo: str, kind: str, number: int) -> dict[str, Any] | None:
    path = snapshot_path(repo, kind, number)
    if repo == PRIVATE_REPO:
        expected = private_hashes()[path]
        if not (ROOT / path).is_file():
            return None
        assert sha256((ROOT / path).read_bytes()) == expected, path
    return read_json(ROOT / path)


def check_criteria(data: dict[str, Any]) -> None:
    expected_ids = {
        f"{issue}.{key}" for issue, keys in EXPECTED.items() for key in keys
    }
    rows = data["criteria"]
    assert len(rows) == 33
    assert {r["id"] for r in rows} == expected_ids, (
        "Incomplete or unexpected criterion set"
    )
    assert len({r["id"] for r in rows}) == len(rows), "Duplicate criteria"
    assert set(data["dispositions"]) == {"114", "115", "116", "124"}, (
        "Missing issue disposition"
    )
    assert data["learnerOutcomes"] == "unknown"
    assert data["liveIssuesChanged"] is False
    allowed = {
        "met",
        "met-selected",
        "met-preparation",
        "met-reporting",
        "partial",
        "unavailable",
        "pending-review",
    }
    for row in rows:
        assert row["status"] in allowed
        issue = snapshot(PRIVATE_REPO, "issue", row["issue"])
        if issue is not None:
            assert row["requirement"] in issue["body"]
        assert row["evidence"] and row["finding"]
        assert all((DOCS / path).is_file() for path in row["evidence"])
        if row["status"] in {"partial", "unavailable"}:
            assert row["remainingOwner"] in {116, 124, 749}, row["id"]
    assert data["dispositions"]["124"]["recommendation"] == "keep-open", (
        "Unknown learner outcomes cannot close #124"
    )
    assert data["dispositions"]["116"]["recommendation"] == "keep-open", (
        "Amiga source gap remains"
    )
    assert all(
        data["dispositions"][str(n)]["recommendation"] == "close-after-review"
        for n in [114, 115]
    )
    assert all(
        next(r for r in rows if r["id"] == f"{n}.review")["status"] == "pending-review"
        for n in [114, 115, 116]
    )


def check_document(record: dict[str, str]) -> None:
    assert sha256((DOCS / record["path"]).read_bytes()) == record["sha256"], record[
        "path"
    ]


def check_pending(sources: dict[str, Any]) -> None:
    pending = sources["pendingEvidence"]
    pr = snapshot("code198x/docs", "pr", 99)
    assert pending["state"] == pr["state"] == "OPEN"
    assert pending["accepted"] is False, "Open PR evidence is not accepted evidence"
    assert pending["revision"] == pr["headRefOid"]
    assert (
        pending["url"]
        == f"https://github.com/code198x/docs/blob/{pending['revision']}/{pending['path']}"
    )
    assert (
        sha256(git(DOCS, "show", f"{pending['revision']}:{pending['path']}"))
        == pending["sha256"]
    )


def check_sources(
    sources: dict[str, Any], website: Path, samples: Path
) -> dict[str, int]:
    for record in sources["docs"]:
        check_document(record)
    assert len(sources["docs"]) == 54
    source = sources["website"]
    actual_paths = (
        git(
            website,
            "ls-tree",
            "-r",
            "--name-only",
            source["revision"],
            "src/content/curriculum",
        )
        .decode()
        .splitlines()
    )
    prefixes = [
        "foundations/",
        "craft/maths-for-games/",
        "commodore-amiga/amos/meet-amos/",
        "commodore-amiga/blitz/meet-blitz/",
    ]
    expected = {
        p
        for p in actual_paths
        if p.endswith(".mdx")
        and any(p.startswith("src/content/curriculum/" + prefix) for prefix in prefixes)
    }
    expected |= {
        f"src/content/curriculum/commodore-amiga/{track}/getting-started.mdx"
        for track in ["amos", "blitz"]
    }
    assert {r["path"] for r in source["files"]} == expected
    assert len(source["files"]) == len(expected) == 97
    for repo, kind in [(website, "website"), (samples, "code-samples")]:
        for record in sources[kind]["files"]:
            data = git(repo, "show", f"{sources[kind]['revision']}:{record['path']}")
            assert sha256(data) == record["sha256"], record["path"]
    counts = {
        "foundationsUnits": sum(
            "/foundations/" in p and "/unit-" in p for p in expected
        ),
        "foundationsOverviews": sum(
            "/foundations/" in p and p.endswith("/index.mdx") for p in expected
        ),
        "mathsUnits": sum("/maths-for-games/unit-" in p for p in expected),
        "amosUnits": sum("/meet-amos/unit-" in p for p in expected),
        "blitzUnits": sum("/meet-blitz/unit-" in p for p in expected),
    }
    assert counts == {
        "foundationsUnits": 39,
        "foundationsOverviews": 10,
        "mathsUnits": 11,
        "amosUnits": 17,
        "blitzUnits": 15,
    }
    old_foundations = read_json(
        DOCS / "audit/2026-10-foundations-publication/source.json"
    )["pages"]
    old_maths = read_json(
        DOCS / "audit/2026-10-probability-pilot/source-inventory.json"
    )["units"]
    previous = {r["path"]: r["sha256"] for r in old_foundations + old_maths}
    current = {r["path"]: r["sha256"] for r in source["files"]}
    assert len(source["comparison"]) == len(previous) == 60
    assert {r["path"] for r in source["comparison"]} == set(previous)
    for record in source["comparison"]:
        assert record["previousSha256"] == previous[record["path"]]
        assert record["currentSha256"] == current[record["path"]]
        assert record["unchanged"] is True
        assert record["previousSha256"] == record["currentSha256"]
    return counts


def check_links() -> int:
    report = (ROOT / "REPORT.md").read_text()
    count = 0
    for destination in re.findall(r"\]\(([^)]+)\)", report):
        parts = urlsplit(destination)
        if parts.scheme or parts.netloc:
            continue
        target = (ROOT / unquote(parts.path)).resolve()
        assert target.is_file(), destination
        count += 1
    assert count > 60, "No meaningful local link set"
    assert (
        "audit/2026-10-education-audit-reconciliation/REPORT.md"
        in (DOCS / "README.md").read_text()
    )
    for issue, keys in EXPECTED.items():
        for key in keys:
            assert f"{issue}.{key} —" in report
    return count


def check_github() -> int:
    records = read_json(ROOT / "github.json")["records"]
    assert len(records) == 53
    assert len({r["path"] for r in records}) == len(records)
    for record in records:
        if record["repository"] == PRIVATE_REPO:
            # Private: the hash is retained even when the text is not.
            assert record["path"] in private_hashes(), record["path"]
            if not (ROOT / record["path"]).is_file():
                continue
        data = read_json(ROOT / record["path"])
        assert (
            data["repository"] == record["repository"]
            and data["number"] == record["number"]
        )
        assert data["state"] == record["state"]
        assert data["body"] and data["url"]
    for number in [63, 78]:
        assert snapshot("code198x/docs", "issue", number)["state"] == "CLOSED"
    for number in [747, 748, 752, 763, 776]:
        assert snapshot("code198x/website", "issue", number)["state"] == "CLOSED"
    for number in [749, 766, 767]:
        assert snapshot("code198x/website", "issue", number)["state"] == "OPEN"
    assert snapshot("code198x/docs", "issue", 94)["state"] == "OPEN"
    for repo, numbers in [
        (
            "code198x/docs",
            [
                79,
                80,
                81,
                82,
                83,
                84,
                85,
                86,
                87,
                88,
                89,
                90,
                91,
                92,
                93,
                95,
                96,
                97,
                98,
                100,
            ],
        ),
        ("code198x/website", [617, 750, 751, 753, 769, 771, 775, 778]),
        ("code198x/code-samples", [95, 99, 100, 101]),
    ]:
        for number in numbers:
            data = snapshot(repo, "pr", number)
            assert (
                data["state"] == "MERGED" and data["mergeCommit"] and data["mergedAt"]
            )
    return len(records)


def private_status() -> str:
    hashes = private_hashes()
    present = sum((ROOT / path).is_file() for path in hashes)
    if present == len(hashes):
        return f"all {len(hashes)} restored and hash-checked"
    return (
        f"{len(hashes) - present} of {len(hashes)} not published (private repository); "
        "their requirement-wording checks were skipped"
    )


def expect_rejection(name: str, check: Any, value: Any) -> str:
    try:
        check(value)
    except AssertionError:
        return name
    raise AssertionError(f"Corrupted evidence accepted: {name}")


def verify(website: Path, samples: Path) -> dict[str, Any]:
    criteria = read_json(ROOT / "criteria.json")
    sources = read_json(ROOT / "sources.json")
    check_criteria(criteria)
    counts = check_sources(sources, website, samples)
    check_pending(sources)
    github_count = check_github()
    links = check_links()
    missing = deepcopy(criteria)
    missing["criteria"].pop()
    missing_issue = deepcopy(criteria)
    del missing_issue["dispositions"]["116"]
    wrong_hash = deepcopy(sources["docs"][0])
    wrong_hash["sha256"] = "0" * 64
    accepted = deepcopy(sources)
    accepted["pendingEvidence"]["accepted"] = True
    learner = deepcopy(criteria)
    learner["dispositions"]["124"]["recommendation"] = "close-after-review"
    controls = [
        expect_rejection("missing criterion", check_criteria, missing),
        expect_rejection("missing issue", check_criteria, missing_issue),
        expect_rejection("wrong source hash", check_document, wrong_hash),
        expect_rejection("pending PR counted as accepted", check_pending, accepted),
        expect_rejection(
            "learner issue closed with unknown outcomes", check_criteria, learner
        ),
    ]
    return {
        "criteria": 33,
        "issues": 4,
        "githubSnapshots": github_count,
        "privateIssueSnapshots": private_status(),
        "documentHashes": len(sources["docs"]),
        "sourceCounts": counts,
        "unchangedSourceComparisons": 60,
        "localLinks": links,
        "negativeControlsRejected": controls,
        "learnerOutcomes": "unknown",
        "freshRuntimeOrBrowserTrials": 0,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--website", type=Path, required=True)
    parser.add_argument("--samples", type=Path, required=True)
    args = parser.parse_args()
    print(json.dumps(verify(args.website, args.samples), indent=2))
