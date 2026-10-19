"""Build palette-test media while preserving the recorded AMOS file contents."""

from __future__ import annotations

import argparse
import hashlib
import json
import runpy
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
# Reuse the previously qualified OFS reader; retain that historical audit unchanged.
PREVIOUS = HERE.parent / "2026-10-amos-bank-or-risk-emu198x"
READER = runpy.run_path(str(PREVIOUS / "prepare.py"))


def prepare(tool: Path, amos: Path, samples: Path, root: Path) -> None:
    expected = json.loads((HERE / "inputs.json").read_text())["inputs"]
    assert (
        hashlib.sha256(amos.read_bytes()).hexdigest()
        == expected["amos-system.adf"]["sha256"]
    )
    root.mkdir(parents=True, exist_ok=True)
    if any(root.iterdir()):
        raise ValueError("Use an empty run directory; existing files are preserved")
    subprocess.run(
        [sys.executable, str(samples / "prepare-probes.py"), str(root / "probes")],
        check=True,
    )
    source = samples / "bank-or-risk.amos"
    assert (
        hashlib.sha256(source.read_bytes()).hexdigest() == expected["source"]["sha256"]
    )
    metadata = READER["manifest"](tool, amos)
    image = amos.read_bytes()
    args = [
        str(tool),
        "create",
        str(root / "amos-work.adf"),
        "--label",
        "AMOSPro_System",
        "--bootable",
    ]
    original_hashes = {}
    for entry in metadata["entries"]:
        destination = entry["path"]
        target = root / "system-files" / destination
        if entry["kind"] == "dir":
            target.mkdir(parents=True, exist_ok=True)
            args += ["--mkdir", destination]
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            content = READER["payload"](image, entry)
            target.write_bytes(content)
            original_hashes[destination] = hashlib.sha256(content).hexdigest()
            args += ["--add", f"{target}={destination}"]
    args += ["--add", f"{source}=bank.asc"]
    for name, alias in [
        ("perfect-success", "perfect"),
        ("preserve-and-recover", "recover"),
    ]:
        args += ["--add", f"{root / 'probes' / (name + '.asc')}={alias}.asc"]
    subprocess.run(args, check=True)
    disk = root / "amos-work.adf"
    subprocess.run([str(tool), "verify", str(disk)], check=True)
    rebuilt = disk.read_bytes()
    retained = {}
    for entry in READER["manifest"](tool, disk)["entries"]:
        if entry["kind"] == "file" and entry["path"] in original_hashes:
            retained[entry["path"]] = hashlib.sha256(
                READER["payload"](rebuilt, entry)
            ).hexdigest()
    assert retained == original_hashes and len(retained) == 78
    (root / "media-checks.json").write_text(
        json.dumps(
            {
                "original_files_preserved": len(retained),
                "file_hashes": retained,
                "work_disk_sha256": hashlib.sha256(rebuilt).hexdigest(),
            },
            indent=2,
        )
        + "\n"
    )
    print("Verified work filesystem and all 78 original file contents.")


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
