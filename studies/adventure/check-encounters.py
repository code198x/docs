"""Observe selected encounters in a separately supplied pinned ODWY0350 port.

Bounded, fresh processes; no game source or complete transcript is retained.
Puzzle commands are spoilers for selected early/middle encounters.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import select
import subprocess
import time
from pathlib import Path

CASES = {
    "parser": [
        "n",
        "in",
        "take the lamp",
        "inventory",
        "nonsense",
        "take",
        "lamp",
        "inventory",
        "lamp",
        "drop",
        "inventory",
        "lamp take",
        "inventory",
        "take lantern",
        "save",
        "quit",
        "y",
    ],
    "bird_without_cage": [
        "n",
        "in",
        "get lamp",
        "xyzzy",
        "on",
        "w",
        "w",
        "take bird",
        "quit",
        "y",
    ],
    "bird_with_rod": [
        "n",
        "in",
        "get lamp",
        "xyzzy",
        "on",
        "get rod",
        "e",
        "get cage",
        "w",
        "w",
        "w",
        "take bird",
        "drop rod",
        "take bird",
        "inventory",
        "quit",
        "y",
    ],
    "snake": [
        "n",
        "in",
        "get lamp",
        "xyzzy",
        "on",
        "e",
        "get cage",
        "w",
        "w",
        "w",
        "get bird",
        "w",
        "d",
        "d",
        "south",
        "drop bird",
        "south",
        "inventory",
        "quit",
        "y",
    ],
    "bridge": [
        "n",
        "in",
        "get lamp",
        "xyzzy",
        "on",
        "get rod",
        "w",
        "w",
        "w",
        "d",
        "w",
        "west",
        "wave rod",
        "west",
        "wave rod",
        "look",
        "quit",
        "y",
    ],
    "gold_return": [
        "n",
        "in",
        "get lamp",
        "xyzzy",
        "on",
        "w",
        "w",
        "w",
        "d",
        "s",
        "take gold",
        "north",
        "up",
        "drop gold",
        "up",
        "quit",
        "y",
    ],
    "death": [
        "n",
        "in",
        "get lamp",
        "xyzzy",
        "w",
        "y",
        "inventory",
        "out",
        "take lamp",
        "inventory",
        "quit",
        "y",
    ],
    "maze": [
        "n",
        "in",
        "get lamp",
        "get food",
        "xyzzy",
        "on",
        "get rod",
        "w",
        "w",
        "w",
        "d",
        "w",
        "wave rod",
        "w",
        "w",
        "s",
        "drop food",
        "north",
        "look",
        "quit",
        "y",
    ],
    "keys_on_ground": [
        "n",
        "in",
        "get keys",
        "get lamp",
        "out",
        "s",
        "s",
        "s",
        "drop keys",
        "unlock grate",
        "down",
        "quit",
        "y",
    ],
}
for name, extra in {
    "control": [],
    "unknown": ["nonsense"],
    "three_words": ["take the lamp"],
    "inventory": ["inventory"],
}.items():
    CASES["time_" + name] = ["n", "in", "take lamp", "on", *extra, "quit", "y"]


def encounter(executable: Path, commands: list[str]) -> list[tuple[str | None, str]]:
    process = subprocess.Popen(
        [str(executable.resolve())],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        bufsize=0,
    )
    assert process.stdin is not None and process.stdout is not None

    def read_response() -> str:
        deadline = time.monotonic() + 3
        data = b""
        while time.monotonic() < deadline:
            ready, _, _ = select.select(
                [process.stdout], [], [], max(0, deadline - time.monotonic())
            )
            if ready:
                chunk = os.read(process.stdout.fileno(), 4096)
                if not chunk:
                    return data.decode()
                data += chunk
                if len(data) > 65_536:
                    raise RuntimeError("Encounter exceeded its output bound")
                if data.endswith(b"* "):
                    return data.decode()
        raise TimeoutError("Encounter did not reach its prompt within three seconds")

    try:
        blocks: list[tuple[str | None, str]] = [(None, read_response())]
        for command in commands:
            if process.poll() is not None:
                raise RuntimeError("Game exited before the command sequence completed")
            process.stdin.write((command + "\n").encode())
            process.stdin.flush()
            blocks.append((command, read_response()))
        process.wait(timeout=2)
        if process.returncode:
            raise RuntimeError(f"Game exited with code {process.returncode}")
        return blocks
    finally:
        if process.poll() is None:
            process.kill()
        process.wait(timeout=2)
        process.stdin.close()
        process.stdout.close()


def responses(blocks: list[tuple[str | None, str]], command: str) -> list[str]:
    return [text for entered, text in blocks if entered == command]


def turns(blocks: list[tuple[str | None, str]]) -> int:
    match = re.search(r"using (\d+) turns", blocks[-1][1])
    if not match:
        raise AssertionError("Missing final turn count")
    return int(match[1])


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("executable", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    observed = {
        name: encounter(args.executable, commands) for name, commands in CASES.items()
    }
    checks = {
        "extra_word_rejected": "2-word"
        in responses(observed["parser"], "take the lamp")[0],
        "partial_command_completes": "lantern"
        in responses(observed["parser"], "inventory")[1],
        "reversed_noun_verb_works": "lantern"
        in responses(observed["parser"], "inventory")[3],
        "noun_alias_recognised": "already"
        in responses(observed["parser"], "take lantern")[0],
        "native_build_has_no_save": "know" in responses(observed["parser"], "save")[0],
        "bird_needs_container": "carry"
        in responses(observed["bird_without_cage"], "take bird")[0],
        "rod_prevents_capture": "disturbed"
        in responses(observed["bird_with_rod"], "take bird")[0],
        "bird_captured_after_rod_dropped": "Little bird"
        in responses(observed["bird_with_rod"], "inventory")[0],
        "snake_blocks_then_route_opens": "snake"
        in responses(observed["snake"], "south")[0]
        and "jewelry" in responses(observed["snake"], "south")[1],
        "bridge_toggles_both_ways": "spans"
        in responses(observed["bridge"], "wave rod")[0]
        and "vanished" in responses(observed["bridge"], "wave rod")[1],
        "gold_changes_return_route": "unclimbable"
        in responses(observed["gold_return"], "up")[0]
        and "small pit" in responses(observed["gold_return"], "up")[1],
        "reincarnation_loses_inventory": "not carrying"
        in responses(observed["death"], "inventory")[0]
        and "lantern" in responses(observed["death"], "inventory")[1],
        "maze_self_loop_preserves_marker": "food"
        in responses(observed["maze"], "north")[0],
        "nearby_dropped_keys_suffice": "unlocked"
        in responses(observed["keys_on_ground"], "unlock grate")[0],
        "unknown_word_costs_turn": turns(observed["time_unknown"])
        == turns(observed["time_control"]) + 1,
        "inventory_costs_turn": turns(observed["time_inventory"])
        == turns(observed["time_control"]) + 1,
        "extra_word_rejection_costs_no_turn": turns(observed["time_three_words"])
        == turns(observed["time_control"]),
    }
    if not all(checks.values()):
        raise AssertionError(checks)
    record = {
        "implementation": "Quuxplusone/Advent ODWY0350; native C build without SAVE_AND_RESTORE",
        "source_commit": "142b61f37063cb00bc9037f67b19411f257099b1",
        "checks": checks,
        "cases": {
            name: {
                "commands": CASES[name],
                "turns": turns(blocks),
                "response_sha256": [
                    hashlib.sha256(text.encode()).hexdigest() for _, text in blocks
                ],
            }
            for name, blocks in observed.items()
        },
        "limits": "Selected encounters, not a full solution or human play study. Process and output bounds are enforced. Random behaviour belongs to this C build's PRNG, not original-hardware timing.",
    }
    args.output.write_text(json.dumps(record, indent=2) + "\n")
    print(f"{len(observed)} encounters and {len(checks)} outcome checks pass")


if __name__ == "__main__":
    main()
