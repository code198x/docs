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
    "blocked_by",
]
STATUSES = {"needs-triage", "ready", "in-progress", "blocked", "covered", "published", "deferred"}
# A blocker lives with the tool that has to change; both queues name one this way.
TOOL_ISSUE = (
    r"https://github\.com/(?:emu198x|asm198x|isa198x|build198x|format198x|cat198x"
    r"|debug198x|lang198x|play198x|code198x)/[A-Za-z0-9._-]+/issues/[1-9][0-9]*"
)
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
        if row["status"] == "blocked":
            require(bool(row["blocked_by"]), "a blocked item needs the tool issue it waits on")
            require(re.fullmatch(TOOL_ISSUE, row["blocked_by"]) is not None, "invalid tool issue URL")
        else:
            require(not row["blocked_by"], "only a blocked item names a blocking issue")
    # Resolve after validating every row: planned sources can appear later in the CSV.
    candidate_ids = {row["id"] for row in rows}
    for source_id, target_id in planned_sources:
        if target_id not in candidate_ids:
            raise ValueError(
                f"{source_id}: unknown planned source candidate: {target_id}"
            )
    return rows


# Demand: how much the site already asks for a subject. A lesson that wants the
# subject counts most, because a learner is waiting on it; an existing Vault
# entry that would link to it counts once; a planned candidate counts nothing,
# because nobody can read it yet. Lessons say what they want in their own
# frontmatter (`wants`), read from a website checkout, so dropping a want drops
# the demand and nothing here goes stale. Demand alone mirrors whatever the
# Vault already covers, so world computing and early subjects get their own
# lanes (see LANES) rather than being weighted down by it.
LESSON_WEIGHT = 3
ENTRY_WEIGHT = 1
# Lanes reserve room for the scope axes plain demand would sideline. A batch
# takes a share from each lane; vault-candidates.md says how much.
LANES = {
    "world": lambda scope: scope.startswith("region:") and scope not in {"region:us", "region:uk"},
    "early": lambda scope: scope in {"period:1950s", "period:1960s"},
}
Wants = dict[str, set[str]]


def frontmatter_list(front: str, key: str) -> list[str]:
    """Read a YAML list in flow (`[a, 'b']`) or block (`- a`) form, without a YAML library."""
    flow = re.search(rf"^{key}:[ \t]*\[(.*?)\][ \t]*$", front, re.M)
    if flow:
        return [item.strip().strip("'\"") for item in flow.group(1).split(",") if item.strip()]
    block = re.search(rf"^{key}:[ \t]*\n((?:[ \t]+-[^\n]*\n?)+)", front, re.M)
    if block:
        return [line.split("-", 1)[1].strip().strip("'\"") for line in block.group(1).splitlines()]
    return []


def load_lesson_wants(website: Path) -> Wants:
    """Map each wanted Vault path or candidate ID to the lessons that want it."""
    root = website / "src/content/curriculum"
    wants: Wants = {}
    for lesson in sorted(root.rglob("unit-*.mdx")):
        parts = lesson.read_text(encoding="utf-8").split("---")
        front = parts[1] if len(parts) > 2 else ""
        for want in frontmatter_list(front, "wants"):
            wants.setdefault(want, set()).add(lesson.relative_to(root).with_suffix("").as_posix())
    return wants


def check_wants(rows: list[dict[str, str]], wants: Wants) -> None:
    """A lesson can only want a candidate that exists."""
    ids = {row["id"] for row in rows}
    for want, lessons in sorted(wants.items()):
        if re.fullmatch(r"VC-[0-9]{4,}", want) and want not in ids:
            raise ValueError(f"{min(lessons)} wants unknown candidate {want}")


def demand(row: dict[str, str], wants: Wants | None = None) -> int:
    """Score a candidate by who already asks for it; no one asking scores zero."""
    entries = {s for s in paths(row["link_from"]) if not s.startswith("candidate:")}
    lessons = (wants or {}).get(row["id"], set())
    return LESSON_WEIGHT * len(lessons) + ENTRY_WEIGHT * len(entries)


def by_demand(rows: list[dict[str, str]], wants: Wants | None = None) -> list[dict[str, str]]:
    return sorted(rows, key=lambda row: (-demand(row, wants), int(row["id"][3:])))


def world_region(row: dict[str, str]) -> str:
    """The first region on the row that counts for the world lane."""
    return next(s for s in paths(row["scope"]) if LANES["world"](s))


def rotate_by_region(rows: list[dict[str, str]], wants: Wants | None = None) -> list[dict[str, str]]:
    """Interleave regions, so one well-covered region can't fill the world lane.

    Each region's candidates keep their demand order. Each round takes the next
    candidate from every region that has one, strongest first. A row with two
    world regions stands in the first listed.
    """
    regions: dict[str, list[dict[str, str]]] = {}
    for row in by_demand(rows, wants):
        regions.setdefault(world_region(row), []).append(row)
    queues = sorted(regions.values(), key=lambda q: (-demand(q[0], wants), int(q[0]["id"][3:])))
    rotated: list[dict[str, str]] = []
    for depth in range(max((len(q) for q in queues), default=0)):
        rotated.extend(q[depth] for q in queues if depth < len(q))
    return rotated


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
    parser.add_argument(
        "--wanted-reviews",
        action="store_true",
        help="list unreviewed Vault entries that lessons want (needs --website)",
    )
    args = parser.parse_args()
    if args.wanted_reviews and not args.website:
        parser.error("--wanted-reviews needs --website")
    try:
        rows = load_backlog(args.file, args.website)
        wants = load_lesson_wants(args.website) if args.website else None
        if wants is not None:
            check_wants(rows, wants)
    except (OSError, UnicodeError, csv.Error, ValueError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        return 1
    print(f"PASS: {len(rows):,} candidates validated")
    for status, count in sorted(Counter(row["status"] for row in rows).items()):
        print(f"  {status}: {count:,}")
    if wants is not None:
        lessons = len({lesson for wanters in wants.values() for lesson in wanters})
        print(f"  lesson wants: {len(wants):,} subjects wanted by {lessons:,} lessons")
    if args.category or args.status or args.limit or args.lane:
        selected = [
            row
            for row in rows
            if (not args.category or row["category"] == args.category)
            and (not args.status or row["status"] == args.status)
            and (not args.lane or any(map(LANES[args.lane], paths(row["scope"]))))
        ]
        if args.lane == "world":
            selected = rotate_by_region(selected, wants)
            order = "taking regions in turn, each by demand"
        else:
            selected = by_demand(selected, wants)
            order = "highest demand first"
        lane = f" in the {args.lane} lane" if args.lane else ""
        basis = "" if wants is not None else "; pass --website to count lesson wants"
        print(
            f"\n{len(selected):,} matching candidates{lane}, {order} "
            f"(each wanting lesson weighs {LESSON_WEIGHT}, each linking entry {ENTRY_WEIGHT}{basis})"
        )
        for row in selected[: args.limit]:
            lessons = len((wants or {}).get(row["id"], ()))
            refs = len({s for s in paths(row["link_from"]) if not s.startswith("candidate:")})
            scope = f"  [{row['scope']}]" if row["scope"] else ""
            print(
                f"{row['id']}  demand {demand(row, wants):3}  {lessons:2} lessons  {refs:3} refs  "
                f"{row['category']}  {row['subject']}{scope}"
            )
    if args.wanted_reviews:
        entries = [(w, l) for w, l in wants.items() if not re.fullmatch(r"VC-[0-9]{4,}", w)]
        entries.sort(key=lambda item: (-len(item[1]), item[0]))

        def reviewed(path: str) -> bool:
            entry = args.website / "src/content/vault" / f"{path}.mdx"
            front = entry.read_text(encoding="utf-8").split("---")[1] if entry.is_file() else ""
            return re.search(r"^reviewed:[ \t]*true[ \t]*$", front, re.M) is not None

        # A reviewed entry a lesson still only wants is satisfied: the lesson
        # should link to it now. The website warns rather than fails, so a
        # review batch isn't blocked by lessons it never touched; this list is
        # where the link pass picks them up.
        for label, group in (
            ("unreviewed entries that lessons want (review demand)", [e for e in entries if not reviewed(e[0])]),
            ("reviewed entries lessons still only want (turn into links)", [e for e in entries if reviewed(e[0])]),
        ):
            print(f"\n{len(group):,} {label}, most wanted first")
            for want, lessons in group[: args.limit]:
                print(f"{len(lessons):3} lessons  {want}  ← {min(lessons)}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
