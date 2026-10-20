"""Replay one retained Emu198x phase; inspect captures to judge its outcome."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent


def substitute(value: object, replacements: dict[str, str]) -> object:
    if isinstance(value, str):
        for token, replacement in replacements.items():
            value = value.replace(token, replacement)
        return value
    if isinstance(value, list):
        return [substitute(item, replacements) for item in value]
    if isinstance(value, dict):
        return {key: substitute(item, replacements) for key, item in value.items()}
    return value


def replay(emulator: Path, kickstart: Path, amos: Path, root: Path, phase: str) -> None:
    if Path(phase).name != phase:
        raise ValueError("Choose a phase filename from scripts/")
    expected = json.loads((HERE / "inputs.json").read_text())["inputs"]
    for name, path in [("kickstart.rom", kickstart), ("amos-system.adf", amos)]:
        assert hashlib.sha256(path.read_bytes()).hexdigest() == expected[name]["sha256"]
    data = json.loads((HERE / "scripts" / phase).read_text())
    rendered = substitute(data, {"${RUN}": str(root), "${AMOS}": str(amos)})
    args = [str(emulator), "--model", "a1200", "--kickstart", str(kickstart)]
    if phase.endswith("-export-requests.json"):
        assert isinstance(rendered, list) and rendered
        args += ["--mcp"]
        result = subprocess.run(
            args,
            input="\n".join(map(json.dumps, rendered)) + "\n",
            capture_output=True,
            text=True,
            timeout=50,
            check=False,
        )
        responses = [json.loads(line) for line in result.stdout.splitlines()]
        assert len(responses) == len(rendered)
        assert all(
            "error" not in item and not item["result"].get("isError", False)
            for item in responses
        )
    else:
        target = root / phase
        target.write_text(json.dumps(rendered, indent=2) + "\n")
        args += ["--script", str(target)]
        if phase == "boot.json":
            args += ["--disk", str(amos)]
        result = subprocess.run(
            args, capture_output=True, text=True, timeout=50, check=False
        )
    (root / f"{Path(phase).stem}-report.txt").write_text(result.stdout)
    (root / f"{Path(phase).stem}-stderr.txt").write_text(result.stderr)
    result.check_returncode()
    print(f"{phase}: emulator completed; inspect the resulting frame captures.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("phase")
    parser.add_argument("--emulator", type=Path, required=True)
    parser.add_argument("--kickstart", type=Path, required=True)
    parser.add_argument("--amos", type=Path, required=True)
    parser.add_argument("--run-root", type=Path, required=True)
    args = parser.parse_args()
    replay(
        args.emulator.resolve(),
        args.kickstart.resolve(),
        args.amos.resolve(),
        args.run_root.resolve(),
        args.phase,
    )
