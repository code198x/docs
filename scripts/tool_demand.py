"""Rank family tool issues by the queued work they block, and release that work when they close.

Both work queues mark an item `blocked` and name the tool issue it waits on in
`blocked_by`. This script reads both queues and:

- ranks tool issues by how many items each one blocks (the default report);
- with --check-issues, confirms every named issue exists and is an issue, not a
  pull request, by asking GitHub through the `gh` command;
- with --unblock, returns the items of issues closed as completed to work
  (`in-progress` if the item has a work issue, otherwise `ready`) and notes that
  their gates must run again; --apply writes the change;
- with --block, puts an item back to `blocked` with a note, for when that re-run
  still fails.

See plans/2026-11-06-content-factory.md, step 6.
"""

import argparse
import csv
import io
import json
import re
import subprocess
import sys
from collections.abc import Callable
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

import check_content_candidates as content
import check_vault_candidates as vault

ROOT = Path(__file__).resolve().parent.parent
# Closed as completed (or closed before GitHub recorded a reason) means fixed.
# Closed as not planned or as a duplicate leaves the work blocked: it needs a
# decision or the surviving issue, not a re-run.
FIXED = {"completed", None}
Lookup = Callable[[str], dict]


@dataclass
class Blocker:
    url: str
    items: list[str] = field(default_factory=list)
    demand: int = 0


@dataclass
class Queue:
    """One work queue on disk: where it lives, its columns and how to validate it."""

    path: Path
    fields: list[str]
    validate: Callable[[], list[dict[str, str]]]
    rows: list[dict[str, str]] = field(default_factory=list)

    def load(self) -> None:
        self.rows = self.validate()

    def save(self) -> None:
        """Write the rows, then validate the file; restore the original on failure."""
        original = self.path.read_bytes()
        buffer = io.StringIO()
        writer = csv.DictWriter(buffer, fieldnames=self.fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(self.rows)
        self.path.write_text(buffer.getvalue(), encoding="utf-8")
        try:
            self.validate()
        except ValueError:
            self.path.write_bytes(original)
            raise


def queues(vault_file: Path, content_file: Path, website: Path | None) -> list[Queue]:
    return [
        Queue(vault_file, vault.FIELDS, lambda: vault.load_backlog(vault_file, website)),
        Queue(
            content_file,
            content.FIELDS,
            lambda: content.load_queue(content_file, vault_file, ROOT, website),
        ),
    ]


def blockers(rows: list[dict[str, str]], wants: vault.Wants | None = None) -> list[Blocker]:
    """Tool issues, most blocking first: by items blocked, then by the Vault demand behind them."""
    found: dict[str, Blocker] = {}
    for row in rows:
        if row["status"] != "blocked":
            continue
        blocker = found.setdefault(row["blocked_by"], Blocker(row["blocked_by"]))
        blocker.items.append(row["id"])
        if row["id"].startswith("VC-"):
            blocker.demand += vault.demand(row, wants)
    return sorted(found.values(), key=lambda b: (-len(b.items), -b.demand, b.url))


def gh_lookup(url: str) -> dict:
    """Read an issue through `gh`; raise LookupError if GitHub has no such issue."""
    match = re.fullmatch(r"https://github\.com/([^/]+)/([^/]+)/issues/([0-9]+)", url)
    if match is None:
        raise LookupError(f"not an issue URL: {url}")
    owner, repo, number = match.groups()
    result = subprocess.run(
        ["gh", "api", f"repos/{owner}/{repo}/issues/{number}"],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        raise LookupError(f"{url}: {result.stderr.strip() or 'lookup failed'}")
    return json.loads(result.stdout)


def check_issues(found: list[Blocker], lookup: Lookup) -> None:
    """Every blocker must be a real issue; a pull request or a missing number is a typo."""
    for blocker in found:
        try:
            issue = lookup(blocker.url)
        except LookupError as error:
            raise ValueError(f"{', '.join(blocker.items)}: blocking issue not found: {error}") from None
        if issue.get("pull_request"):
            raise ValueError(f"{', '.join(blocker.items)}: {blocker.url} is a pull request, not an issue")


def unblock(rows: list[dict[str, str]], lookup: Lookup, today: str) -> tuple[list[str], list[str]]:
    """Return items whose blocker closed as fixed to work; report the ones closed otherwise."""
    released: list[str] = []
    unresolved: list[str] = []
    states: dict[str, dict] = {}
    for row in rows:
        if row["status"] != "blocked":
            continue
        url = row["blocked_by"]
        if url not in states:
            states[url] = lookup(url)
        issue = states[url]
        if issue["state"] != "closed":
            continue
        if issue.get("state_reason") not in FIXED:
            unresolved.append(f"{row['id']}: {url} closed as {issue['state_reason']}; still blocked")
            continue
        row["status"] = "in-progress" if row["issue"] else "ready"
        row["blocked_by"] = ""
        row["triage_notes"] = note(
            row["triage_notes"],
            f"Unblocked on {today}: {url} closed as completed. Run the item's gates again before trusting the fix.",
        )
        released.append(row["id"])
    return released, unresolved


def block(rows: list[dict[str, str]], item: str, url: str, reason: str, today: str) -> None:
    """Put an item back to blocked, with the reason, when its gates still fail."""
    if not reason:
        raise ValueError("say why the item is blocked")
    row = next((row for row in rows if row["id"] == item), None)
    if row is None:
        raise ValueError(f"unknown item: {item}")
    if row["status"] in {"needs-triage", "covered", "published", "deferred"}:
        raise ValueError(f"{item}: only work that is ready or in progress can be blocked, not {row['status']}")
    row["status"] = "blocked"
    row["blocked_by"] = url
    row["triage_notes"] = note(row["triage_notes"], f"Blocked on {today} by {url}: {reason}")


def note(existing: str, addition: str) -> str:
    return f"{existing} {addition}" if existing else addition


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--vault-file", type=Path, default=ROOT / "vault-candidates.csv")
    parser.add_argument("--content-file", type=Path, default=ROOT / "content-candidates.csv")
    parser.add_argument("--website", type=Path, help="website checkout, to count lesson wants in Vault demand")
    action = parser.add_mutually_exclusive_group()
    action.add_argument("--check-issues", action="store_true", help="confirm every blocking issue exists on GitHub")
    action.add_argument("--unblock", action="store_true", help="return work whose blocking issue closed as completed")
    action.add_argument("--block", metavar="ID", help="put an item back to blocked")
    parser.add_argument("--by", metavar="URL", help="with --block: the tool issue it waits on")
    parser.add_argument("--note", default="", help="with --block: why the item is still blocked")
    parser.add_argument("--apply", action="store_true", help="with --unblock: write the change")
    args = parser.parse_args()
    if args.block and not args.by:
        parser.error("--block needs --by")
    if args.apply and not args.unblock:
        parser.error("--apply goes with --unblock")
    today = date.today().isoformat()
    try:
        both = queues(args.vault_file, args.content_file, args.website)
        for queue in both:
            queue.load()
        rows = [row for queue in both for row in queue.rows]
        wants = vault.load_lesson_wants(args.website) if args.website else None
        found = blockers(rows, wants)
        if args.check_issues:
            check_issues(found, gh_lookup)
            print(f"PASS: {len(found):,} blocking issues found on GitHub")
            return 0
        if args.block:
            queue = next((q for q in both if any(r["id"] == args.block for r in q.rows)), None)
            if queue is None:
                raise ValueError(f"unknown item: {args.block}")
            block(queue.rows, args.block, args.by, args.note, today)
            queue.save()
            print(f"{args.block} blocked by {args.by}")
            return 0
        if args.unblock:
            for queue in both:
                released, unresolved = unblock(queue.rows, gh_lookup, today)
                for line in unresolved:
                    print(line)
                for item in released:
                    print(f"{item}: unblocked")
                if released and args.apply:
                    queue.save()
            if not args.apply:
                print("Dry run: nothing written. Pass --apply to write.")
            return 0
    except (OSError, UnicodeError, csv.Error, ValueError, LookupError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        return 1
    blocked = sum(len(b.items) for b in found)
    print(f"{len(found):,} tool issues block {blocked:,} items, most blocking first")
    for blocker in found:
        print(f"{len(blocker.items):3} items  demand {blocker.demand:3}  {blocker.url}  ← {', '.join(blocker.items)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
