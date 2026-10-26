"""Validate the whole Vault backlog, then display an optional filtered shortlist."""

import argparse
import csv
import re
import sys
from collections import Counter
from pathlib import Path

FIELDS = [
    "id",
    "subject",
    "category",
    "status",
    "why",
    "link_from",
    "triage_notes",
    "covered_by",
    "issue",
]
STATUSES = {"needs-triage", "ready", "in-progress", "covered", "published", "deferred"}
ROOT = Path(__file__).resolve().parent.parent


def paths(value: str) -> list[str]:
    """Read the documented semicolon-separated path format."""
    return value.split(";") if value else []


def load_backlog(source: Path, website: Path | None = None) -> list[dict[str, str]]:
    """Reject malformed records, duplicate identities and incomplete transitions."""
    with source.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle, strict=True)
        if reader.fieldnames != FIELDS:
            raise ValueError(f"CSV header must be {FIELDS}")
        rows = list(reader)
    if not rows:
        raise ValueError("Backlog must not be empty")
    vault = website / "src/content/vault" if website else None
    if vault is not None and not vault.is_dir():
        raise ValueError(f"Website Vault directory does not exist: {vault}")
    ids: set[str] = set()
    subjects: set[tuple[str, str]] = set()
    issues: set[str] = set()
    planned_sources: list[tuple[str, str]] = []
    for number, row in enumerate(rows, 1):
        if set(row) != set(FIELDS) or any(not isinstance(v, str) for v in row.values()):
            raise ValueError(f"Record {number}: missing or extra fields")
        label = row["id"] or f"Record {number}"

        def require(condition: bool, message: str, label: str = label) -> None:
            if not condition:
                raise ValueError(f"{label}: {message}")

        require(
            all(v == v.strip() for v in row.values()), "trim surrounding whitespace"
        )
        require(re.fullmatch(r"VC-[0-9]{4,}", row["id"]) is not None, "invalid ID")
        require(int(row["id"][3:]) > 0, "ID must be positive")
        # Compare numeric IDs too: VC-0001 and VC-00001 must not coexist.
        identity = str(int(row["id"][3:]))
        require(identity not in ids, "duplicate ID")
        ids.add(identity)
        require(
            bool(row["subject"] and row["why"] and row["link_from"]),
            "subject, why and link_from are required",
        )
        require(
            re.fullmatch(r"[a-z]+(?:-[a-z]+)*", row["category"]) is not None,
            "invalid category slug",
        )
        subject = (row["category"], row["subject"].casefold())
        require(subject not in subjects, "duplicate subject in the same category")
        subjects.add(subject)
        require(row["status"] in STATUSES, "unknown status")
        for field in ("link_from", "covered_by"):
            for entry in paths(row[field]):
                if entry.startswith("candidate:"):
                    require(
                        field == "link_from",
                        "planned candidate references are only allowed in link_from",
                    )
                    require(
                        re.fullmatch(r"candidate:VC-[0-9]{4,}", entry) is not None,
                        f"invalid planned source reference: {entry}",
                    )
                    target = entry.removeprefix("candidate:")
                    require(
                        target != row["id"],
                        "candidate cannot be its own planned source",
                    )
                    planned_sources.append((row["id"], target))
                    continue
                require(
                    re.fullmatch(r"[a-z0-9-]+/[a-z0-9-]+", entry) is not None,
                    f"invalid {field} path: {entry}",
                )
                if vault is not None:
                    study_page = website / "src/pages/vault" / entry / "index.astro"
                    require(
                        (vault / f"{entry}.mdx").is_file()
                        or (entry.startswith("studies/") and study_page.is_file()),
                        f"missing {field} entry: {entry}",
                    )
        if row["status"] != "needs-triage":
            require(bool(row["triage_notes"]), "triage decision needs notes")
        if row["status"] == "needs-triage":
            require(not row["issue"], "triage must precede the writing issue")
        if row["status"] in {"covered", "published"}:
            require(bool(row["covered_by"]), "resolved coverage needs entry paths")
        if row["status"] == "in-progress":
            require(bool(row["issue"]), "writing needs its issue URL")
        if row["issue"]:
            require(
                re.fullmatch(
                    r"https://github\.com/code198x/website/issues/[1-9][0-9]*",
                    row["issue"],
                )
                is not None,
                "invalid website issue URL",
            )
            require(
                row["issue"] not in issues,
                "issue already assigned to another candidate",
            )
            issues.add(row["issue"])
    # Resolve after validating every row: planned sources can appear later in the CSV.
    candidate_ids = {row["id"] for row in rows}
    for source_id, target_id in planned_sources:
        if target_id not in candidate_ids:
            raise ValueError(
                f"{source_id}: unknown planned source candidate: {target_id}"
            )
    return rows


def positive(value: str) -> int:
    number = int(value)
    if number < 1:
        raise argparse.ArgumentTypeError("must be at least 1")
    return number


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--file", type=Path, default=ROOT / "vault-candidates.csv")
    parser.add_argument("--website", type=Path)
    parser.add_argument("--status", choices=sorted(STATUSES))
    parser.add_argument("--category")
    parser.add_argument("--limit", type=positive)
    args = parser.parse_args()
    try:
        rows = load_backlog(args.file, args.website)
    except (OSError, UnicodeError, csv.Error, ValueError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        return 1
    print(f"PASS: {len(rows):,} candidates validated")
    for status, count in sorted(Counter(row["status"] for row in rows).items()):
        print(f"  {status}: {count:,}")
    if args.category or args.status or args.limit:
        selected = [
            row
            for row in rows
            if (not args.category or row["category"] == args.category)
            and (not args.status or row["status"] == args.status)
        ]
        selected.sort(
            key=lambda row: (-len(set(paths(row["link_from"]))), int(row["id"][3:]))
        )
        print(
            f"\n{len(selected):,} matching candidates; highest referring-entry counts first"
        )
        for row in selected[: args.limit]:
            count = len(set(paths(row["link_from"])))
            print(f"{row['id']}  {count:3} refs  {row['category']}  {row['subject']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
