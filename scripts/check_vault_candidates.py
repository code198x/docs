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
    "scope",
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
        scopes = paths(row["scope"])
        require(len(scopes) == len(set(scopes)), "duplicate scope")
        for scope in scopes:
            require(
                re.fullmatch(r"region:[a-z0-9]+(?:-[a-z0-9]+)*|period:(?:19|20)[0-9]0s", scope)
                is not None,
                f"invalid scope: {scope}",
            )
        subject = (row["category"], row["subject"].casefold())
        require(subject not in subjects, "duplicate subject in the same category")
        subjects.add(subject)
        require(row["status"] in STATUSES, "unknown status")
        for field in ("link_from", "covered_by"):
            for entry in paths(row[field]):
                if entry.startswith("lesson:"):
                    require(
                        field == "link_from",
                        "lesson references are only allowed in link_from",
                    )
                    lesson = entry.removeprefix("lesson:")
                    require(
                        re.fullmatch(r"[a-z0-9-]+(?:/[a-z0-9-]+){1,3}", lesson) is not None,
                        f"invalid lesson reference: {entry}",
                    )
                    if website is not None:
                        require(
                            (website / "src/content/curriculum" / f"{lesson}.mdx").is_file(),
                            f"missing lesson: {entry}",
                        )
                    continue
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


# Demand: how much the site already asks for a subject. A lesson that wants the
# entry counts most, because a learner is waiting on it; an existing Vault entry
# counts once; a planned candidate counts nothing, because nobody can read it
# yet. Demand alone mirrors whatever the Vault already covers, so world
# computing and early subjects get their own lanes (see LANES) rather than
# being weighted down by it.
LESSON_WEIGHT = 3
ENTRY_WEIGHT = 1
# Lanes reserve room for the scope axes plain demand would sideline. A batch
# takes a share from each lane; vault-candidates.md says how much.
LANES = {
    "world": lambda scope: scope.startswith("region:") and scope not in {"region:us", "region:uk"},
    "early": lambda scope: scope in {"period:1950s", "period:1960s"},
}


def by_demand(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    return sorted(rows, key=lambda row: (-demand(row), int(row["id"][3:])))


def world_region(row: dict[str, str]) -> str:
    """The first region on the row that counts for the world lane."""
    return next(s for s in paths(row["scope"]) if LANES["world"](s))


def rotate_by_region(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    """Interleave regions, so one well-covered region can't fill the world lane.

    Each region's candidates keep their demand order. Each round takes the next
    candidate from every region that has one, strongest first. A row with two
    world regions stands in the first listed.
    """
    regions: dict[str, list[dict[str, str]]] = {}
    for row in by_demand(rows):
        regions.setdefault(world_region(row), []).append(row)
    queues = sorted(regions.values(), key=lambda q: (-demand(q[0]), int(q[0]["id"][3:])))
    rotated: list[dict[str, str]] = []
    for depth in range(max((len(q) for q in queues), default=0)):
        rotated.extend(q[depth] for q in queues if depth < len(q))
    return rotated


def demand(row: dict[str, str]) -> int:
    """Score a candidate by who already asks for it; no referrers scores zero."""
    score = 0
    for source in set(paths(row["link_from"])):
        if source.startswith("candidate:"):
            continue
        score += LESSON_WEIGHT if source.startswith("lesson:") else ENTRY_WEIGHT
    return score


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
    parser.add_argument("--lane", choices=sorted(LANES))
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
    if args.category or args.status or args.limit or args.lane:
        selected = [
            row
            for row in rows
            if (not args.category or row["category"] == args.category)
            and (not args.status or row["status"] == args.status)
            and (not args.lane or any(map(LANES[args.lane], paths(row["scope"]))))
        ]
        if args.lane == "world":
            selected = rotate_by_region(selected)
            order = "taking regions in turn, each by demand"
        else:
            selected = by_demand(selected)
            order = "highest demand first"
        lane = f" in the {args.lane} lane" if args.lane else ""
        print(
            f"\n{len(selected):,} matching candidates{lane}, {order} "
            f"(lesson links weigh {LESSON_WEIGHT}, entry links {ENTRY_WEIGHT})"
        )
        for row in selected[: args.limit]:
            refs = len({s for s in paths(row["link_from"]) if not s.startswith("candidate:")})
            scope = f"  [{row['scope']}]" if row["scope"] else ""
            print(
                f"{row['id']}  demand {demand(row):3}  {refs:3} refs  "
                f"{row['category']}  {row['subject']}{scope}"
            )
    return 0


if __name__ == "__main__":
    sys.exit(main())
