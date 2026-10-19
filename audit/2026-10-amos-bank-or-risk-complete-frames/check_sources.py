"""Keep display changes separate from the accepted game rules."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


def routine(text: str, name: str) -> str:
    return text.split(name + ":\n", 1)[1].split("\nReturn", 1)[0] + "\nReturn\n"


def check(samples: Path) -> dict:
    folder = samples / "stages/arcade"
    old = (folder / "rolling-die.amos").read_text()
    stable = (folder / "stable-display.amos").read_text()
    restored = (
        stable.replace("Double Buffer\nAutoback 0\nBob Update Off\n", "", 1)
        .replace("BR_READ_FRESH:\nGosub BR_PRESENT\n", "BR_READ_FRESH:\n", 1)
        .replace(
            "      Gosub BR_DRAW_DIE\n      Gosub BR_PRESENT\n",
            "      Gosub BR_DRAW_DIE\n",
            1,
        )
    )
    assert (
        restored.removesuffix(
            "\nBR_PRESENT:\nScreen Swap\nWait Vbl\nScreen Copy Physic To Logic\nReturn\n"
        )
        == old
    )
    sources = {
        n: (folder / (n + ".amos")).read_text()
        for n in ["stable-display", "rom-text", "styled-board"]
    }

    def game(t: str) -> list[str]:
        body = t.split("Randomize Timer\n", 1)[1].split("\nBR_DRAW_STATE:", 1)[0]
        return [
            line
            for line in body.splitlines()
            if not line.strip().startswith(
                ("Locate ", "Print ", "BR_TX=", "BR_TY=", "BR_TEXT$=", "Gosub BR_LABEL")
            )
        ]

    for n, t in sources.items():
        assert game(t) == game(old), n
        assert routine(t, "BR_SOUND_RESULT") == routine(old, "BR_SOUND_RESULT"), n
        assert routine(t, "BR_READ_FRESH") == routine(stable, "BR_READ_FRESH"), n
        assert routine(t, "BR_PRESENT") == routine(stable, "BR_PRESENT"), n
        assert t.count("BR_FACE=Rnd(5)+1") == 1 and t.count("BR_CAP=10") == 1
    styled = sources["styled-board"]
    assert styled.count("Gosub BR_LETTERING") == 4
    for line in styled.splitlines():
        if line.startswith("BR_GLYPH$("):
            bits = line.split('="')[1][:-1]
            assert len(bits) == 35 and set(bits) <= {"0", "1"}
    expected = json.loads((HERE / "inputs.json").read_text())["sources"]
    actual = {
        n + ".amos": hashlib.sha256(t.encode()).hexdigest() for n, t in sources.items()
    }
    assert actual == expected
    return {
        "source_hashes": actual,
        "restored_original": True,
        "game_rules_identical": True,
        "sound_identical": True,
    }


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("samples", type=Path)
    args = p.parse_args()
    print(json.dumps(check(args.samples), indent=2))
