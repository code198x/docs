"""Validate the content factory's non-Vault work queue.

Patterns, From the Metal articles, system profiles, productions, progressions
and tracks queue here; Vault entries keep their own queue in
vault-candidates.csv. The two are linked by ID: `from` may cite a Vault
candidate (VC-…), another content candidate (CC-…), or the docs or website file
the demand came from. See plans/2026-11-06-content-factory.md.
"""

import argparse
import csv
import re
import sys
from collections import Counter
from pathlib import Path

from check_vault_candidates import load_backlog

FIELDS = [
    "id",
    "surface",
    "subject",
    "system",
    "models",
    "why",
    "from",
    "status",
    "triage_notes",
    "covered_by",
    "issue",
    "blocked_by",
]
SURFACES = {"from-the-metal", "pattern", "system-profile", "production", "progression", "track"}
NEEDS_SYSTEM = {"system-profile", "production", "track"}
STATUSES = {"needs-triage", "ready", "in-progress", "blocked", "covered", "published", "deferred"}
SLUG = r"[a-z0-9]+(?:-[a-z0-9]+)*"
# A work item is tracked where its work happens; a blocker lives with the tool.
WORK_ISSUE = r"https://github\.com/code198x/(?:website|docs|code-samples)/issues/[1-9][0-9]*"
TOOL_ISSUE = (
    r"https://github\.com/(?:emu198x|asm198x|isa198x|build198x|format198x|cat198x"
    r"|debug198x|lang198x|play198x|code198x)/[A-Za-z0-9._-]+/issues/[1-9][0-9]*"
)
ROOT = Path(__file__).resolve().parent.parent


def entries(value: str) -> list[str]:
    """Read the semicolon-separated list format the Vault queue uses."""
    return value.split(";") if value else []


def load_queue(
    source: Path,
    vault_source: Path,
    docs: Path = ROOT,
    website: Path | None = None,
) -> list[dict[str, str]]:
    """Reject malformed rows, unknown references and incomplete transitions."""
    with source.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle, strict=True)
        if reader.fieldnames != FIELDS:
            raise ValueError(f"CSV header must be {FIELDS}")
        rows = list(reader)
    if not rows:
        raise ValueError("Queue must not be empty")
    vault_ids = {row["id"] for row in load_backlog(vault_source)}
    ids: set[str] = set()
    subjects: set[tuple[str, str]] = set()
    issues: set[str] = set()
    references: list[tuple[str, str]] = []
    for number, row in enumerate(rows, 1):
        if set(row) != set(FIELDS) or any(not isinstance(v, str) for v in row.values()):
            raise ValueError(f"Record {number}: missing or extra fields")
        label = row["id"] or f"Record {number}"

        def require(condition: bool, message: str, label: str = label) -> None:
            if not condition:
                raise ValueError(f"{label}: {message}")

        require(all(v == v.strip() for v in row.values()), "trim surrounding whitespace")
        require(re.fullmatch(r"CC-[0-9]{4,}", row["id"]) is not None, "invalid ID")
        require(int(row["id"][3:]) > 0, "ID must be positive")
        identity = str(int(row["id"][3:]))
        require(identity not in ids, "duplicate ID")
        ids.add(identity)
        require(row["surface"] in SURFACES, "unknown surface")
        require(bool(row["subject"] and row["why"]), "subject and why are required")
        subject = (row["surface"], row["subject"].casefold())
        require(subject not in subjects, "duplicate subject on the same surface")
        subjects.add(subject)
        if row["surface"] in NEEDS_SYSTEM:
            require(bool(row["system"]), f"a {row['surface']} needs its system")
        if row["system"]:
            require(re.fullmatch(SLUG, row["system"]) is not None, "invalid system slug")
            if website is not None:
                require(
                    (website / "src/content/systems" / f"{row['system']}.yaml").is_file(),
                    f"unknown system: {row['system']}",
                )
        for model in entries(row["models"]):
            require(re.fullmatch(SLUG, model) is not None, f"invalid model slug: {model}")
        for ref in entries(row["from"]):
            if re.fullmatch(r"(?:VC|CC)-[0-9]{4,}", ref):
                require(ref != row["id"], "a candidate cannot come from itself")
                references.append((row["id"], ref))
            elif ref.startswith("docs:"):
                require((docs / ref.removeprefix("docs:")).is_file(), f"missing docs file: {ref}")
            elif ref.startswith("website:"):
                require(bool(ref.removeprefix("website:")), f"empty website path: {ref}")
                if website is not None:
                    require(
                        (website / ref.removeprefix("website:")).is_file(),
                        f"missing website file: {ref}",
                    )
            else:
                require(False, f"invalid from reference: {ref}")
        require(row["status"] in STATUSES, "unknown status")
        if row["status"] != "needs-triage":
            require(bool(row["triage_notes"]), "triage decision needs notes")
        if row["status"] == "needs-triage":
            require(not row["issue"], "triage must precede the work issue")
        if row["status"] in {"covered", "published"}:
            require(bool(row["covered_by"]), "resolved coverage needs website paths")
        if row["status"] == "in-progress":
            require(bool(row["issue"]), "work needs its issue URL")
        if row["status"] == "blocked":
            require(bool(row["blocked_by"]), "a blocked item needs the tool issue it waits on")
        else:
            require(not row["blocked_by"], "only a blocked item names a blocking issue")
        for path in entries(row["covered_by"]):
            require(path.startswith("src/"), f"covered_by must be a website src/ path: {path}")
            if website is not None:
                require((website / path).is_file(), f"missing covered_by file: {path}")
        if row["issue"]:
            require(re.fullmatch(WORK_ISSUE, row["issue"]) is not None, "invalid work issue URL")
            require(row["issue"] not in issues, "issue already assigned to another candidate")
            issues.add(row["issue"])
        if row["blocked_by"]:
            # Several items can wait on one tool issue; that count is its priority.
            require(re.fullmatch(TOOL_ISSUE, row["blocked_by"]) is not None, "invalid tool issue URL")
    # Resolve after validating every row: a cited candidate can appear later.
    content_ids = {row["id"] for row in rows}
    for source_id, ref in references:
        known = vault_ids if ref.startswith("VC-") else content_ids
        if ref not in known:
            raise ValueError(f"{source_id}: unknown candidate in from: {ref}")
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--file", type=Path, default=ROOT / "content-candidates.csv")
    parser.add_argument("--vault-file", type=Path, default=ROOT / "vault-candidates.csv")
    parser.add_argument("--website", type=Path)
    parser.add_argument("--surface", choices=sorted(SURFACES))
    parser.add_argument("--status", choices=sorted(STATUSES))
    args = parser.parse_args()
    try:
        rows = load_queue(args.file, args.vault_file, ROOT, args.website)
    except (OSError, UnicodeError, csv.Error, ValueError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        return 1
    print(f"PASS: {len(rows):,} content candidates validated")
    for status, count in sorted(Counter(row["status"] for row in rows).items()):
        print(f"  {status}: {count:,}")
    if args.surface or args.status:
        for row in rows:
            if (not args.surface or row["surface"] == args.surface) and (
                not args.status or row["status"] == args.status
            ):
                print(f"{row['id']}  {row['surface']}  {row['status']}  {row['subject']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
