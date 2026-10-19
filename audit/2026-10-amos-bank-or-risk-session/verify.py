"""Verify source/media identities and stable input, scoring and replay pictures."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import runpy
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
READER = runpy.run_path(
    str(HERE.parent / "2026-10-amos-bank-or-risk-emu198x/prepare.py")
)


def routine(source: str, label: str) -> str:
    block = source.split(label + ":\n", 1)[1]
    return re.split(r"\nBR_[A-Z_]+:\n", block, maxsplit=1)[0].strip()


def verify(root: Path, tool: Path, samples: Path) -> dict:
    expected = json.loads((HERE / "inputs.json").read_text())
    folder = samples / "stages/session"
    sources = {p.stem: p.read_text() for p in folder.glob("*.amos")}
    assert len(sources) == 8
    assert {
        name + ".amos": hashlib.sha256(s.encode()).hexdigest()
        for name, s in sources.items()
    } == expected["sources"]
    reference = (samples / "stages/opening/one-round.amos").read_text()
    endpoint = (samples / "prototype/bank-or-risk.amos").read_text()
    read = routine(endpoint, "BR_READ_FRESH")
    draw = routine(reference, "BR_DRAW_DIE")
    for name, source in sources.items():
        if name == "keep-secured":
            continue
        assert routine(source, "BR_READ_FRESH") == read, name
        assert routine(source, "BR_DRAW_DIE") == draw, name
    # Expanding the extracted calls must restore the earlier complete program.
    body = sources["read-fresh"].split("\nBR_READ_FRESH:\n")[0].rstrip() + "\n"
    inline = read.removesuffix("Return").rstrip() + "\n"
    body = body.replace(
        "   Gosub BR_READ_FRESH\n",
        "".join("   " + line + "\n" for line in inline.splitlines()),
        1,
    )
    body = body.replace("\nGosub BR_READ_FRESH\n", "\n" + inline, 1)
    assert body == reference
    stripped = re.sub(
        r'^ *BR_BANKED=0\n|^ *BR_BANKED=BR_BANKED\+BR_AWARD\n|^ *Print "Secured: ";BR_BANKED\n',
        "",
        sources["award-once"],
        flags=re.MULTILINE,
    )
    assert stripped == sources["next-round"]
    for name in (
        "award-once",
        "count-rounds",
        "recognise-success",
        "recognise-impossibility",
        "replay",
    ):
        source = sources[name]
        assert source.count("BR_BANKED=BR_BANKED+BR_AWARD") == 1
        assert source.index("Until BR_HANDFIN") < source.index(
            "BR_BANKED=BR_BANKED+BR_AWARD"
        )
    variants = {
        "input-four": ("read-fresh", 4),
        "next-four": ("next-round", 4),
        "award-four": ("award-once", 4),
        "count-four": ("count-rounds", 4),
        "success-five": ("recognise-success", 5),
        "success-four": ("recognise-success", 4),
        "possible-six": ("recognise-impossibility", 6),
        "possible-five": ("recognise-impossibility", 5),
        "replay-five": ("replay", 5),
        "replay-six": ("replay", 6),
    }
    for name, (source, roll) in variants.items():
        assert sources[source].count("BR_FACE=Rnd(5)+1") == 1
        assert (HERE / "variants" / f"{name}.asc").read_text() == sources[
            source
        ].replace("BR_FACE=Rnd(5)+1", f"BR_FACE={roll}")
    assert (HERE / "variants/baseline-four.asc").read_text() == reference.replace(
        "BR_FACE=Rnd(5)+1", "BR_FACE=4"
    )
    for name in ("amos-work.adf", "session.adf"):
        path = root / name
        assert (
            hashlib.sha256(path.read_bytes()).hexdigest()
            == expected["inputs"][name]["sha256"]
        )
        subprocess.run(
            [str(tool), "verify", str(path)], check=True, capture_output=True
        )
    sequence = json.loads((HERE / "sequence.json").read_text())
    assert sequence and len(sequence) == len(set(sequence))
    all_names = set(sources) | set(variants) | {"baseline-four"}
    assert {name + "-run.json" for name in all_names} <= set(sequence)
    assert {name + "-import.json" for name in all_names} <= set(sequence)
    captures = {}
    for phase in sequence:
        actions = json.loads((HERE / "scripts" / phase).read_text())
        for action in actions:
            if action.get("action") == "save_screenshot":
                path = root / Path(action["path"]).name
                content = path.read_bytes()
                assert (
                    content.startswith(b"\x89PNG\r\n\x1a\n") and len(content) > 500
                ), path.name
                captures[path.name] = hashlib.sha256(content).hexdigest()
    assert len(captures) > 100
    comparisons = []

    def equal(a: str, b: str) -> None:
        assert (root / (a + ".png")).read_bytes() == (
            root / (b + ".png")
        ).read_bytes(), (a, b)
        comparisons.append([a, b])

    for n in range(4):
        equal(f"baseline-{n}", f"extracted-{n}")
    equal("next-result", "next-ignored")
    equal("next-four-start", "next-reset")
    for name in ("award-wait", "award-invalid", "award-wrong-phase"):
        equal("award-bank", name)
    for label, count in (
        ("count", 5),
        ("missed", 5),
        ("success", 3),
        ("failure", 3),
        ("possible-success", 3),
        ("replay-win", 3),
        ("replay-loss", 3),
    ):
        for suffix in ("wait", "invalid", "roll-ignored", "space-ignored"):
            equal(f"{label}-{count}", f"{label}-{suffix}")
    for label, source in (("replay-win", "replay-five"), ("replay-loss", "replay-six")):
        equal(source + "-start", label + "-reset")
        equal(label + "-reset", label + "-reset-wait")
    disk = root / "session-settled.save.adf"
    subprocess.run([str(tool), "verify", str(disk)], check=True, capture_output=True)
    image = disk.read_bytes()
    files = {
        e["path"]: READER["payload"](image, e)
        for e in READER["manifest"](tool, disk)["entries"]
        if e["kind"] == "file"
    }
    originals = json.loads((root / "media-checks.json").read_text())["file_hashes"]
    assert len(originals) == 78
    for name, digest in originals.items():
        assert hashlib.sha256(files[name]).hexdigest() == digest, name
    assert not any(name.endswith(".asc") for name in files)
    program = files["session.amos"]
    assert program.startswith(b"AMOS Basic") and len(program) > 3000
    return {
        "sources": len(sources),
        "variants": len(variants) + 1,
        "capture_hashes": captures,
        "identical_picture_pairs": comparisons,
        "saved_program_bytes": len(program),
        "saved_program_sha256": hashlib.sha256(program).hexdigest(),
        "saved_disk_sha256": hashlib.sha256(image).hexdigest(),
        "original_files_preserved": len(originals),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path)
    parser.add_argument("--disk-tool", type=Path, required=True)
    parser.add_argument("--samples", type=Path, required=True)
    args = parser.parse_args()
    print(json.dumps(verify(args.root, args.disk_tool, args.samples), indent=2))
