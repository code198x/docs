"""Choose the next Vault batch, or check a chosen one, and print it as JSON.

By default the batch follows the ranking in vault-candidates.md: at least a
third from the world and early lanes, taken in turn, and the rest by demand.
Everywhere, the machines of the 1980s and earlier (systems and hardware) come
first, then everything else from those decades, because that is the project's
centre; later subjects follow once those run out.
`--ids` replaces the choice with your own list, which must name candidates that
are still waiting for work. With `--website`, each candidate also carries a
length guide: the median and 90th-percentile article length of the published
entries in its category. The vault-batch workflow reads this output.
"""

import argparse
import csv
import json
import math
import re
import statistics
import sys
from pathlib import Path

from check_vault_candidates import (
    LANES,
    ROOT,
    Wants,
    by_demand,
    demand,
    load_backlog,
    load_lesson_wants,
    paths,
    positive,
    rotate_by_region,
)

# Waiting for work: not yet triaged, or triaged and not yet written.
WAITING = {"needs-triage", "ready"}
# The project's centre of gravity is the 1970s and 1980s, with the 1960s (and the
# 1950s machines before them) as its roots. A batch takes these first.
OLD = {"period:1950s", "period:1960s", "period:1970s", "period:1980s"}


MACHINES = {"systems", "hardware"}


def is_old(row: dict[str, str]) -> bool:
    return any(scope in OLD for scope in paths(row["scope"]))


def tier(row: dict[str, str]) -> int:
    """0: an old machine; 1: anything else old; 2: everything later or undated."""
    if not is_old(row):
        return 2
    return 0 if row["category"] in MACHINES else 1


def oldest_first(ordered: list[dict[str, str]]) -> list[dict[str, str]]:
    """Old machines, then the rest of their era, then later subjects; order kept within each."""
    return sorted(ordered, key=tier)


# Categories with fewer published entries than this borrow the whole Vault's guide.
GUIDE_MINIMUM = 10


def article_words(text: str) -> int:
    """Words a reader reads: no frontmatter, imports, components or source list."""
    parts = text.split("---", 2)
    body = parts[2] if text.startswith("---") and len(parts) > 2 else text
    body = body.split("<Sources>")[0]
    body = re.sub(r"^import .*$", "", body, flags=re.M)
    body = re.sub(r"<[^>]+>", "", body)
    return len(body.split())


def guide(lengths: list[int]) -> dict[str, int]:
    ordered = sorted(lengths)
    return {
        "median": round(statistics.median(ordered)),
        "p90": ordered[int(0.9 * (len(ordered) - 1))],
        "entries": len(ordered),
    }


def length_guides(website: Path) -> dict[str, dict[str, int]]:
    """Per category, how long published entries run; "*" is the whole Vault."""
    lengths: dict[str, list[int]] = {}
    for entry in (website / "src/content/vault").glob("*/*.mdx"):
        lengths.setdefault(entry.parent.name, []).append(article_words(entry.read_text(encoding="utf-8")))
    every = [n for counts in lengths.values() for n in counts]
    guides = {category: guide(counts) for category, counts in lengths.items() if len(counts) >= GUIDE_MINIMUM}
    if every:
        guides["*"] = guide(every)
    return guides


def in_lane(row: dict[str, str], lane: str) -> bool:
    return any(map(LANES[lane], paths(row["scope"])))


def choose(rows: list[dict[str, str]], size: int, wants: Wants | None = None) -> list[tuple[dict[str, str], str]]:
    """Pick `size` candidates: a third (rounded up) from the lanes in turn, the rest by demand, oldest first."""
    waiting = [row for row in rows if row["status"] in WAITING]
    world = [r for r in waiting if in_lane(r, "world")]
    lanes = {
        # Regions take turns within each tier before the next tier starts.
        "world": [r for t in range(3) for r in rotate_by_region([r for r in world if tier(r) == t], wants)],
        "early": oldest_first(by_demand([r for r in waiting if in_lane(r, "early")], wants)),
    }
    chosen: list[tuple[dict[str, str], str]] = []
    taken: set[str] = set()

    def take(row: dict[str, str], reason: str) -> None:
        chosen.append((row, reason))
        taken.add(row["id"])

    quota = min(math.ceil(size / 3), size)
    order = ["world", "early"]
    turn = 0
    while sum(1 for _, r in chosen if r != "demand") < quota:
        live = [lane for lane in order if any(r["id"] not in taken for r in lanes[lane])]
        if not live:
            break
        lane = order[turn % len(order)]
        turn += 1
        if lane not in live:
            continue
        take(next(r for r in lanes[lane] if r["id"] not in taken), lane)
    for row in oldest_first(by_demand(waiting, wants)):
        if len(chosen) >= size:
            break
        if row["id"] not in taken:
            take(row, "demand")
    return chosen


def named(rows: list[dict[str, str]], ids: list[str]) -> list[tuple[dict[str, str], str]]:
    """Your own list, in your order; every ID must be a candidate still waiting for work."""
    if len(set(ids)) != len(ids):
        raise ValueError("an ID appears twice in the list")
    known = {row["id"]: row for row in rows}
    chosen = []
    for item in ids:
        row = known.get(item)
        if row is None:
            raise ValueError(f"unknown candidate: {item}")
        if row["status"] not in WAITING:
            raise ValueError(f"{item} is {row['status']}, not waiting for work")
        chosen.append((row, "named"))
    return chosen


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--file", type=Path, default=ROOT / "vault-candidates.csv")
    parser.add_argument("--website", type=Path, help="website checkout, to count lesson wants")
    # Five while the factory measures what a batch costs and what review changes.
    parser.add_argument("--size", type=positive, default=5)
    parser.add_argument("--ids", nargs="+", metavar="VC-NNNN", help="use this list instead of the ranking")
    args = parser.parse_args()
    try:
        rows = load_backlog(args.file, args.website)
        wants = load_lesson_wants(args.website) if args.website else None
        chosen = named(rows, args.ids) if args.ids else choose(rows, args.size, wants)
        guides = length_guides(args.website) if args.website else {}
    except (OSError, UnicodeError, csv.Error, ValueError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        return 1
    if not chosen:
        print("FAIL: no candidates are waiting for work", file=sys.stderr)
        return 1
    batch = [
        {
            "id": row["id"],
            "subject": row["subject"],
            "category": row["category"],
            "scope": row["scope"],
            "status": row["status"],
            "why": row["why"],
            "link_from": row["link_from"],
            "triage_notes": row["triage_notes"],
            "demand": demand(row, wants),
            "chosen_by": reason,
            "length_guide": guides.get(row["category"], guides.get("*")),
        }
        for row, reason in chosen
    ]
    json.dump(batch, sys.stdout, ensure_ascii=False, indent=2)
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
