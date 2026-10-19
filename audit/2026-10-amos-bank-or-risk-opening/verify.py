"""Check source/media identities and input/result invariants; review pictures too."""

from __future__ import annotations

import argparse
import hashlib
import json
import runpy
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
READER = runpy.run_path(
    str(HERE.parent / "2026-10-amos-bank-or-risk-emu198x/prepare.py")
)


def verify(root: Path, tool: Path, samples: Path) -> dict:
    expected = json.loads((HERE / "inputs.json").read_text())
    sources = samples / "stages/opening"
    actual = {
        p.name: hashlib.sha256(p.read_bytes()).hexdigest()
        for p in sources.glob("*.amos")
    }
    assert actual == expected["sources"] and len(actual) == 10
    for name in ("amos-work.adf", "opening.adf", "edits.adf"):
        disk = root / name
        assert (
            hashlib.sha256(disk.read_bytes()).hexdigest()
            == expected["inputs"][name]["sha256"]
        )
        subprocess.run(
            [str(tool), "verify", str(disk)], check=True, capture_output=True
        )
    variants = {
        "total-10": ("total-meaning", "BR_TOTAL=9", "BR_TOTAL=10"),
        "total-11": ("total-meaning", "BR_TOTAL=9", "BR_TOTAL=11"),
        "missing-quote": ("message", 'Print "BANK OR RISK"', 'Print "BANK OR RISK'),
        "misspelt-print": ("message", 'Print "BANK OR RISK"', 'Prit "BANK OR RISK"'),
        "sum-ten": ("running-total", "BR_FACE=3", "BR_FACE=6"),
        "white-pip": ("die-colours", "Ink 2", "Ink 1"),
        "cyan-pip": ("die-colours", "$F80", "$0FF"),
        "roll-one": ("one-roll", "BR_FACE=Rnd(5)+1", "BR_FACE=1"),
        "roll-six": ("one-roll", "BR_FACE=Rnd(5)+1", "BR_FACE=6"),
        **{
            f"round-{n}": ("one-round", "BR_FACE=Rnd(5)+1", f"BR_FACE={n}")
            for n in (4, 5, 6)
        },
    }
    for name, (source, old, new) in variants.items():
        content = (sources / f"{source}.amos").read_text()
        assert content.count(old) == 1
        assert (HERE / "variants" / f"{name}.asc").read_text() == content.replace(
            old, new
        )
    required = {
        f"{name}-start.png"
        for name in (
            "message",
            "edited-message",
            "die-colours",
            "one-roll",
            "running-total",
            "total-meaning",
            "one-choice",
            "ask-again",
            "fresh-choice",
            "one-round",
            "total-10",
            "total-11",
            "sum-ten",
            "white-pip",
            "cyan-pip",
        )
    }
    required |= {f"choice-{key}.png" for key in ("R", "B", "Q", "X")}
    required |= {
        "one-roll-result.png",
        "roll-one-result.png",
        "roll-six-result.png",
        "ask-again-held.png",
        "ask-again-editor.png",
        "fresh-held.png",
        "fresh-second.png",
        "fresh-invalid.png",
        "fresh-editor.png",
        "round-quit-editor.png",
        "message-reopened-title.png",
        "message-interrupt-editor.png",
        "choice-finish-editor.png",
        "misspelt-print-syntax.png",
        "missing-quote-syntax.png",
    }
    for name in ("round-bank", "round-perfect", "round-bust", "random-round-bank"):
        required |= {name + "-stable.png", name + "-editor.png"}
    captures = {}
    for name in sorted(required):
        content = (root / name).read_bytes()
        assert content.startswith(b"\x89PNG\r\n\x1a\n") and len(content) > 500, name
        captures[name] = hashlib.sha256(content).hexdigest()

    def equal(a: str, b: str) -> None:
        assert (root / a).read_bytes() == (root / b).read_bytes(), (a, b)

    equal("fresh-second.png", "fresh-invalid.png")
    assert (root / "fresh-held.png").read_bytes() != (
        root / "fresh-second.png"
    ).read_bytes()
    equal("round-4-start.png", "round-bank-0-B.png")
    equal("round-bank-0-B.png", "round-bank-1-X.png")
    for name, final in (
        ("round-bank", "3-B"),
        ("round-perfect", "1-R"),
        ("round-bust", "1-R"),
    ):
        equal(f"{name}-{final}.png", f"{name}-stable.png")
    disk = root / "message-native.save.adf"
    subprocess.run([str(tool), "verify", str(disk)], check=True, capture_output=True)
    files = {
        e["path"]: READER["payload"](disk.read_bytes(), e)
        for e in READER["manifest"](tool, disk)["entries"]
        if e["kind"] == "file"
    }
    originals = json.loads((root / "media-checks.json").read_text())["file_hashes"]
    assert len(originals) == 78
    for name, digest in originals.items():
        assert hashlib.sha256(files[name]).hexdigest() == digest, name
    assert not any(name.endswith(".asc") for name in files)
    program = files["welcome.amos"]
    assert program.startswith(b"AMOS Basic") and len(program) > 100
    return {
        "source_count": len(actual),
        "variant_count": len(variants),
        "required_capture_hashes": captures,
        "saved_program_bytes": len(program),
        "saved_program_sha256": hashlib.sha256(program).hexdigest(),
        "saved_disk_sha256": hashlib.sha256(disk.read_bytes()).hexdigest(),
        "original_files_preserved": len(originals),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path)
    parser.add_argument("--disk-tool", type=Path, required=True)
    parser.add_argument("--samples", type=Path, required=True)
    args = parser.parse_args()
    print(json.dumps(verify(args.root, args.disk_tool, args.samples), indent=2))
