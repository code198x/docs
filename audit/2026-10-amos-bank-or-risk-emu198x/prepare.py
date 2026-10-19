"""Rebuild local native-test media; licensed file contents are never retained here."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def manifest(tool: Path, disk: Path) -> dict:
    result = subprocess.run(
        [str(tool), "manifest", str(disk)], check=True, capture_output=True, text=True
    )
    return json.loads(result.stdout)


def payload(image: bytes, entry: dict) -> bytes:
    assert entry["kind"] == "file"
    assert all(block["checksum_valid"] for block in entry["file"]["ofs_linked_data"])
    result = bytearray()
    for extent in entry["file"]["logical_ranges"]:
        assert extent["start"] == len(result)
        start = extent["block"] * 512 + 24
        result += image[start : start + extent["end"] - extent["start"]]
    assert len(result) == entry["size"]
    return bytes(result)


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
        [
            sys.executable,
            str(samples / "prepare-probes.py"),
            str(root / "prefixed-probes"),
        ],
        check=True,
    )
    source = samples / "bank-or-risk.amos"
    probe_manifest = json.loads((HERE / "probe-manifest.json").read_text())
    assert (
        hashlib.sha256(source.read_bytes()).hexdigest()
        == probe_manifest["source_sha256"]
    )
    aliases = [
        ("perfect-success", "perfect"),
        ("preserve-and-recover", "recover"),
        ("range-and-limit", "range"),
        ("unreachable", "fail"),
    ]

    def create(name: str, label: str, files: list[tuple[Path, str]]) -> None:
        args = [str(tool), "create", str(root / name), "--label", label]
        for path, destination in files:
            args += ["--add", f"{path}={destination}"]
        subprocess.run(args, check=True)

    fixtures = [
        (root / "prefixed-probes" / f"{name}.asc", f"{alias}.asc")
        for name, alias in aliases
    ]
    create("prefixed.adf", "Prefixed", [(source, "bank.asc"), *fixtures])
    old = root / "original-probes"
    old.mkdir()
    for name, _ in aliases:
        (old / f"{name}.asc").write_text(
            (root / "prefixed-probes" / f"{name}.asc").read_text().replace("BR_", "")
        )
    create(
        "playtest.adf",
        "Playtest",
        [(HERE / "probes/original.amos", "bank.asc")]
        + [(old / f"{name}.asc", f"{alias}.asc") for name, alias in aliases]
        + [(HERE / "probes/random-range.amos", "random.asc")],
    )
    create(
        "labels.adf",
        "Labels",
        [(HERE / "probes/bad.asc", "bad.asc"), (HERE / "probes/good.asc", "good.asc")],
    )
    create("names.adf", "Names", [(HERE / "probes/names.asc", "names.asc")])

    metadata = manifest(tool, amos)
    image = amos.read_bytes()
    files = root / "system-files"
    files.mkdir()
    work = root / "amos-work.adf"
    args = [str(tool), "create", str(work), "--label", "AMOSPro_System", "--bootable"]
    original_hashes = {}
    for entry in metadata["entries"]:
        destination = entry["path"]
        target = files / destination
        if entry["kind"] == "dir":
            target.mkdir(parents=True, exist_ok=True)
            args += ["--mkdir", destination]
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            content = payload(image, entry)
            target.write_bytes(content)
            original_hashes[destination] = hashlib.sha256(content).hexdigest()
            args += ["--add", f"{target}={destination}"]
    args += ["--add", f"{source}=bank.asc"]
    subprocess.run(args, check=True)
    subprocess.run([str(tool), "verify", str(work)], check=True)
    rebuilt = work.read_bytes()
    for entry in manifest(tool, work)["entries"]:
        if entry["kind"] == "file" and entry["path"] in original_hashes:
            assert (
                hashlib.sha256(payload(rebuilt, entry)).hexdigest()
                == original_hashes[entry["path"]]
            )
    for name in ("amos-work.adf", "prefixed.adf"):
        assert (
            hashlib.sha256((root / name).read_bytes()).hexdigest()
            == expected[name]["sha256"]
        )
    print(
        "Rebuilt media matches the retained identities; all original file contents agree."
    )


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
