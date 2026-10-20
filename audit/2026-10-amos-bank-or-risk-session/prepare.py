"""Prepare session sources using the qualified AMOS runtime filesystem builder."""

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
    sources = samples / "stages/session"
    actual = {
        p.name: hashlib.sha256(p.read_bytes()).hexdigest()
        for p in sources.glob("*.amos")
    }
    assert actual == expected["sources"] and len(actual) == 8
    previous = HERE.parent / "2026-10-amos-bank-or-risk-sound/prepare.py"
    runpy.run_path(str(previous))["prepare"](tool, amos, samples / "prototype", root)
    args = [str(tool), "create", str(root / "session.adf"), "--label", "Session"]
    for p in sorted(sources.glob("*.amos")):
        args += ["--add", f"{p}={p.stem}.asc"]
    variants = json.loads((HERE / "variant-hashes.json").read_text())
    assert set(variants) == {p.stem for p in (HERE / "variants").glob("*.asc")}
    for p in sorted((HERE / "variants").glob("*.asc")):
        assert hashlib.sha256(p.read_bytes()).hexdigest() == variants[p.stem]
        args += ["--add", f"{p}={p.name}"]
    subprocess.run(args, check=True)
    subprocess.run([str(tool), "verify", str(root / "session.adf")], check=True)


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
