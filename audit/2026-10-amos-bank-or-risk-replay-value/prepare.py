"""Prepare the replay-value stages using the qualified runtime filesystem builder."""

from __future__ import annotations

import argparse
import hashlib
import json
import runpy
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent


def prepare(tool: Path, amos: Path, samples: Path, root: Path) -> None:
    expected = json.loads((HERE / "inputs.json").read_text())
    sources = samples / "stages/replay-value"
    actual = {
        p.name: hashlib.sha256(p.read_bytes()).hexdigest()
        for p in sources.glob("*.amos")
    }
    assert actual == expected["sources"] and len(actual) == 5
    variants = json.loads((HERE / "variants.json").read_text())
    assert set(variants) == {p.stem for p in (HERE / "variants").glob("*.asc")}
    for name, entry in variants.items():
        content = (samples / "stages" / (entry["stage"] + ".amos")).read_text()
        assert content.count("BR_FACE=Rnd(5)+1") == 1
        if "rolls" in entry:
            content = content.replace("BR_FACE=Rnd(5)+1", "Read BR_FACE").replace(
                "   BR_BANKED=0\n", "   BR_BANKED=0\n   Restore\n", 1
            )
            content += "\nData " + ",".join(map(str, entry["rolls"])) + "\n"
        else:
            content = content.replace("BR_FACE=Rnd(5)+1", f"BR_FACE={entry['roll']}")
        if "volume" in entry:
            content = content.replace("Volume 24", f"Volume {entry['volume']}")
        supplied = HERE / "variants" / (name + ".asc")
        assert supplied.read_text() == content
        assert hashlib.sha256(supplied.read_bytes()).hexdigest() == entry["sha256"]
    previous = HERE.parent / "2026-10-amos-bank-or-risk-sound/prepare.py"
    runpy.run_path(str(previous))["prepare"](tool, amos, samples / "prototype", root)
    args = [
        str(tool),
        "create",
        str(root / "value.adf"),
        "--label",
        "ReplayValue",
    ]
    for p in sorted(sources.glob("*.amos")):
        args += ["--add", f"{p}={p.stem}.asc"]
    for p in sorted((HERE / "variants").glob("*.asc")):
        if p.stem != "varied":
            args += ["--add", f"{p}={p.name}"]
    subprocess.run(args, check=True)
    subprocess.run([str(tool), "verify", str(root / "value.adf")], check=True)
    subprocess.run(
        [
            str(tool),
            "create",
            str(root / "varied.adf"),
            "--label",
            "Varied",
            "--add",
            f"{HERE / 'variants/varied.asc'}=varied.asc",
        ],
        check=True,
    )
    subprocess.run([str(tool), "verify", str(root / "varied.adf")], check=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--disk-tool", type=Path, required=True)
    parser.add_argument("--amos", type=Path, required=True)
    parser.add_argument("--samples", type=Path, required=True)
    parser.add_argument("--run-root", type=Path, required=True)
    args = parser.parse_args()
    prepare(
        args.disk_tool.resolve(),
        args.amos.resolve(),
        args.samples.resolve(),
        args.run_root.resolve(),
    )
