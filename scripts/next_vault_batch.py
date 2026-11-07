"""Choose the next Vault batch, or check a chosen one, and print it as JSON.

By default the batch follows the ranking in vault-candidates.md: at least a
third from the world and early lanes, taken in turn, and the rest by demand.
`--ids` replaces the choice with your own list, which must name candidates that
are still waiting for work. The vault-batch workflow reads this output.
"""

import argparse
import csv
import json
import math
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


def in_lane(row: dict[str, str], lane: str) -> bool:
    return any(map(LANES[lane], paths(row["scope"])))


def choose(rows: list[dict[str, str]], size: int, wants: Wants | None = None) -> list[tuple[dict[str, str], str]]:
    """Pick `size` candidates: a third (rounded up) from the lanes in turn, the rest by demand."""
    waiting = [row for row in rows if row["status"] in WAITING]
    lanes = {
        "world": rotate_by_region([r for r in waiting if in_lane(r, "world")], wants),
        "early": by_demand([r for r in waiting if in_lane(r, "early")], wants),
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
    for row in by_demand(waiting, wants):
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
    parser.add_argument("--size", type=positive, default=10)
    parser.add_argument("--ids", nargs="+", metavar="VC-NNNN", help="use this list instead of the ranking")
    args = parser.parse_args()
    try:
        rows = load_backlog(args.file, args.website)
        wants = load_lesson_wants(args.website) if args.website else None
        chosen = named(rows, args.ids) if args.ids else choose(rows, args.size, wants)
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
        }
        for row, reason in chosen
    ]
    json.dump(batch, sys.stdout, ensure_ascii=False, indent=2)
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
