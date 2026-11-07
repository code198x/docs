"""Vault candidate IDs already given out, on main and on every open batch branch.

Two batches cut from the same main would otherwise give the same new IDs to
different subjects. Each batch branch is named vault-batch/<slug> on the docs
remote; this reads the queue on main and on all of them.

    python3.13 scripts/candidate_ids.py          # print the next free ID
"""

import csv
import io
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BATCH_PREFIX = "refs/heads/vault-batch/"


def git(repo: Path, *args: str) -> str:
    result = subprocess.run(["git", *args], cwd=repo, capture_output=True, text=True, check=False)
    if result.returncode != 0:
        raise ValueError(f"git {' '.join(args)}: {result.stderr.strip()}")
    return result.stdout


def batch_refs(repo: Path, remote: str = "origin") -> dict[str, str]:
    """Open batch branches on the remote: branch name to commit."""
    refs = {}
    for line in git(repo, "ls-remote", "--heads", remote, "vault-batch/*").splitlines():
        commit, ref = line.split("\t")
        if ref.startswith(BATCH_PREFIX):
            refs[ref.removeprefix("refs/heads/")] = commit
    return refs


def rows_at(repo: Path, commit: str) -> dict[str, str]:
    """ID to subject in the queue at a commit."""
    text = git(repo, "show", f"{commit}:vault-candidates.csv")
    return {row["id"]: row["subject"] for row in csv.DictReader(io.StringIO(text))}


def taken(repo: Path, remote: str = "origin") -> dict[str, dict[str, str]]:
    """Every queue that counts: main and each open batch branch, by name."""
    git(repo, "fetch", "-q", remote, "main")
    queues = {"main": rows_at(repo, git(repo, "rev-parse", f"{remote}/main").strip())}
    refs = batch_refs(repo, remote)
    if refs:
        git(repo, "fetch", "-q", remote, *refs)
    for branch, commit in refs.items():
        queues[branch] = rows_at(repo, commit)
    return queues


def number(candidate_id: str) -> int:
    return int(candidate_id[3:])


def next_id(queues: dict[str, dict[str, str]]) -> str:
    highest = max((number(i) for rows in queues.values() for i in rows if re.fullmatch(r"VC-\d{4,}", i)), default=0)
    return f"VC-{highest + 1:04d}"


def clashes(mine: dict[str, str], base: dict[str, str], others: dict[str, dict[str, str]]) -> list[str]:
    """IDs this branch adds that another open batch gives to a different subject."""
    found = []
    for candidate_id, subject in sorted(mine.items()):
        if candidate_id in base:
            continue
        for branch, rows in sorted(others.items()):
            if candidate_id in rows and rows[candidate_id] != subject:
                found.append(f"{candidate_id}: {subject!r} here, {rows[candidate_id]!r} on {branch}")
    return found


def main() -> int:
    try:
        print(next_id(taken(ROOT)))
    except ValueError as error:
        print(f"FAIL: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
