"""Bounded entrance check; supply a locally built ODWY0350 executable.

No game source, executable or complete transcript is distributed. The output
retains command identity, a response hash and two short critical extracts.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path

COMMANDS = [
    "n",
    "in",
    "take keys",
    "take lamp",
    "out",
    "south",
    "south",
    "south",
    "down",
    "unlock grate",
    "down",
    "west",
    "on lamp",
    "inventory",
    "quit",
    "y",
]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("executable", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    result = subprocess.run(
        [str(args.executable.resolve())],
        input="\n".join(COMMANDS) + "\n",
        capture_output=True,
        text=True,
        timeout=5,
        check=True,
    )
    checks = {
        "blocked_before_unlock": 0
        <= result.stdout.find("You can't go through a locked steel grate!")
        < result.stdout.find("The grate is now unlocked."),
        "unlocked_after_keys": "The grate is now unlocked." in result.stdout,
        "reached_below_grate": "You're below the grate." in result.stdout
        or "You are in a small chamber beneath" in result.stdout,
        "lamp_on": "Your lamp is now on." in result.stdout,
        "both_objects_carried": " Set of keys\n Brass lantern" in result.stdout,
        "clean_exit": not result.stderr,
    }
    if not all(checks.values()):
        raise AssertionError(checks)
    args.output.write_text(
        json.dumps(
            {
                "implementation": "Quuxplusone/Advent ODWY0350",
                "source_commit": "142b61f37063cb00bc9037f67b19411f257099b1",
                "commands": COMMANDS,
                "checks": checks,
                "stdout_sha256": hashlib.sha256(result.stdout.encode()).hexdigest(),
                "critical_extracts": [
                    "You can't go through a locked steel grate!",
                    "The grate is now unlocked.",
                ],
                "limits": "Modern C port; bounded entrance only; no original-hardware, complete-game or human play-session verification.",
            },
            indent=2,
        )
        + "\n"
    )


if __name__ == "__main__":
    main()
