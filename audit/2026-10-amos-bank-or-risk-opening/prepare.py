"""Prepare the opening checkpoints on verified, separate native-test media."""

from __future__ import annotations

import argparse
import hashlib
import json
import runpy
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
PREVIOUS = HERE.parent / "2026-10-amos-bank-or-risk-sound"


def prepare(tool: Path, amos: Path, samples: Path, root: Path) -> None:
    expected = json.loads((HERE / "inputs.json").read_text())
    opening = samples / "stages/opening"
    actual = {
        p.name: hashlib.sha256(p.read_bytes()).hexdigest()
        for p in sorted(opening.glob("*.amos"))
    }
    assert actual == expected["sources"] and len(actual) == 10
    runpy.run_path(str(PREVIOUS / "prepare.py"))["prepare"](
        tool, amos, samples / "prototype", root
    )
    variants = json.loads((HERE / "variant-hashes.json").read_text())
    assert set(variants) == {p.stem for p in (HERE / "variants").glob("*.asc")}
    extra = {"roll-one", "roll-six", "sum-ten", "white-pip", "cyan-pip"}
    for disk, label in (("opening.adf", "Opening"), ("edits.adf", "Edits")):
        args = [str(tool), "create", str(root / disk), "--label", label]
        if disk == "opening.adf":
            for source in sorted(opening.glob("*.amos")):
                args += ["--add", f"{source}={source.stem}.asc"]
        paths = (
            [
                HERE / "variants" / f"{name}.asc"
                for name in ("roll-one", "roll-six", "sum-ten", "white-pip", "cyan-pip")
            ]
            if disk == "edits.adf"
            else sorted((HERE / "variants").glob("*.asc"))
        )
        for source in paths:
            assert (
                hashlib.sha256(source.read_bytes()).hexdigest() == variants[source.stem]
            )
            if (source.stem in extra) == (disk == "edits.adf"):
                args += ["--add", f"{source}={source.name}"]
        subprocess.run(args, check=True)
        subprocess.run([str(tool), "verify", str(root / disk)], check=True)
    print("Verified opening source identities and derived filesystem.")


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
