"""Build runtime, source fixtures and an empty native program data disk."""

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
    for name, sha in expected["sources"].items():
        assert (
            hashlib.sha256((samples / "stages/arcade" / name).read_bytes()).hexdigest()
            == sha
        ), name
    variants = json.loads((HERE / "variants.json").read_text())
    for n, e in variants.items():
        p = HERE / "variants" / (n + ".asc")
        assert hashlib.sha256(p.read_bytes()).hexdigest() == e["sha256"], n
        if "source" in e:
            text = (
                (samples / "stages/arcade" / e["source"])
                .read_text()
                .replace("BR_FACE=Rnd(5)+1", f"BR_FACE={e['face']}")
            )
            if e.get("static"):
                text = text.replace("BR_ANIMATE=1", "BR_ANIMATE=0")
            assert p.read_text() == text, n
    runpy.run_path(str(HERE.parent / "2026-10-amos-bank-or-risk-sound/prepare.py"))[
        "prepare"
    ](tool, amos, samples / "prototype", root)
    groups = {
        "complete.adf": [("stable-display.amos", "stable-display.asc")]
        + [(None, n + ".asc") for n in ["rom-font", "stable-five", "stable-six"]],
        "styled.adf": [
            ("rom-text.amos", "rom-text.asc"),
            ("styled-board.amos", "styled-board.asc"),
        ],
        "style-tests.adf": [
            (None, n + ".asc") for n in ["styled-five", "styled-six", "styled-static"]
        ],
        "save-data.adf": [],
    }
    for name, entries in groups.items():
        args = [
            str(tool),
            "create",
            str(root / name),
            "--label",
            {
                "complete.adf": "CompleteFrames",
                "styled.adf": "StyledBoard",
                "style-tests.adf": "StyleTests",
                "save-data.adf": "BankOrRisk",
            }[name],
        ]
        for source, dest in entries:
            path = (
                samples / "stages/arcade" / source
                if source
                else HERE / "variants" / dest
            )
            args += ["--add", str(path) + "=" + dest]
        subprocess.run(args, check=True)
        subprocess.run([str(tool), "verify", str(root / name)], check=True)


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    for n in ["disk-tool", "amos", "samples", "run-root"]:
        p.add_argument("--" + n, type=Path, required=True)
    a = p.parse_args()
    prepare(
        a.disk_tool.resolve(),
        a.amos.resolve(),
        a.samples.resolve(),
        a.run_root.resolve(),
    )
