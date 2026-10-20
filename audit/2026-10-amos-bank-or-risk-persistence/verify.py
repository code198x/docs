"""Check native persistence artefacts; inspect the captures separately."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import runpy
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
READER = runpy.run_path(
    str(HERE.parent / "2026-10-amos-bank-or-risk-emu198x/prepare.py")
)
SPEC = importlib.util.spec_from_file_location(
    "measure_audio", HERE.parent / "2026-10-amos-bank-or-risk-sound/measure_audio.py"
)
assert SPEC is not None and SPEC.loader is not None
AUDIO = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(AUDIO)


def verify(root: Path, tool: Path, source: Path) -> dict:
    inputs = json.loads((HERE / "inputs.json").read_text())
    assert (
        hashlib.sha256(source.read_bytes()).hexdigest()
        == inputs["inputs"]["source"]["sha256"]
    )
    original = json.loads((root / "media-checks.json").read_text())["file_hashes"]
    assert len(original) == 78
    disks = {}
    for kind in ("base", "perfect"):
        disk = root / f"{kind}-native.save.adf"
        # The verifier must reject filesystem corruption, not merely list files.
        subprocess.run(
            [str(tool), "verify", str(disk)], check=True, capture_output=True
        )
        manifest = READER["manifest"](tool, disk)
        image = disk.read_bytes()
        files = {
            entry["path"]: READER["payload"](image, entry)
            for entry in manifest["entries"]
            if entry["kind"] == "file"
        }
        for name, digest in original.items():
            assert hashlib.sha256(files[name]).hexdigest() == digest, name
        assert not any(name.lower().endswith(".asc") for name in files)
        program = files[f"{kind}.amos"]
        assert program.startswith(b"AMOS Basic") and len(program) > 3000
        assert not program.startswith(source.read_bytes()[:100])
        disks[kind] = {
            "disk_sha256": hashlib.sha256(image).hexdigest(),
            "program_bytes": len(program),
            "program_sha256": hashlib.sha256(program).hexdigest(),
            "original_files_preserved": len(original),
        }
    matches = []
    for before in sorted(root.glob("perfect-0*.png")):
        after = root / before.name.replace("perfect-", "perfect-reopened-", 1)
        assert before.read_bytes() == after.read_bytes(), before.name
        matches.append(before.name)
    assert len(matches) == 9
    audio = {}
    for name, ratios in (
        ("perfect", [1, 1, 2]),
        ("perfect-reopened", [1, 1, 2]),
        ("base-reopened-bank", [1]),
    ):
        measured = AUDIO.measure(root / f"{name}.wav")
        assert measured["clipped_samples"] == 0, name
        assert len(measured["bursts"]) == len(ratios), name
        for burst, ratio in zip(measured["bursts"], ratios, strict=True):
            assert burst["pitch_hz"] is not None
            assert abs(burst["pitch_hz"] / (525.31 * ratio) - 1) < 0.03
            assert 0.1 < burst["duration_s"] < 0.3
        audio[name] = measured
    before_audio = audio["perfect"]
    after_audio = audio["perfect-reopened"]
    assert abs(before_audio["peak_pcm"] / after_audio["peak_pcm"] - 1) < 0.02
    for before_burst, after_burst in zip(
        before_audio["bursts"], after_audio["bursts"], strict=True
    ):
        assert abs(before_burst["pitch_hz"] / after_burst["pitch_hz"] - 1) < 0.01
        assert abs(before_burst["duration_s"] - after_burst["duration_s"]) <= 0.01
    return {"disks": disks, "identical_game_captures": matches, "audio": audio}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path)
    parser.add_argument("--disk-tool", type=Path, required=True)
    parser.add_argument("--source", type=Path, required=True)
    args = parser.parse_args()
    print(json.dumps(verify(args.root, args.disk_tool, args.source), indent=2))
