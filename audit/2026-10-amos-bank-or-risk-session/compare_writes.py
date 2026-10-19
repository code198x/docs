"""Compare the rejected early export with the completed native disk write."""

from __future__ import annotations

import argparse
import hashlib
import json
import runpy
import struct
import subprocess
from pathlib import Path

READER = runpy.run_path(
    str(
        Path(__file__).resolve().parent.parent
        / "2026-10-amos-bank-or-risk-emu198x/prepare.py"
    )
)


def compare(tool: Path, early: Path, settled: Path) -> dict:
    before, after = early.read_bytes(), settled.read_bytes()
    assert len(before) == len(after) == 901120
    rejected = subprocess.run(
        [str(tool), "verify", str(early)], check=False, capture_output=True
    )
    assert rejected.returncode != 0
    subprocess.run([str(tool), "verify", str(settled)], check=True, capture_output=True)

    def files(path: Path, image: bytes) -> dict:
        return {
            e["path"]: hashlib.sha256(READER["payload"](image, e)).hexdigest()
            for e in READER["manifest"](tool, path)["entries"]
            if e["kind"] == "file"
        }

    before_files, after_files = files(early, before), files(settled, after)
    assert len(before_files) == 79 and before_files == after_files
    changed = [
        n
        for n in range(1760)
        if before[n * 512 : (n + 1) * 512] != after[n * 512 : (n + 1) * 512]
    ]
    assert changed == [880, 881]
    before_flag = struct.unpack_from(">I", before, 880 * 512 + 78 * 4)[0]
    after_flag = struct.unpack_from(">I", after, 880 * 512 + 78 * 4)[0]
    assert before_flag == 0 and after_flag == 0xFFFFFFFF
    return {
        "additional_frames": 240,
        "changed_blocks": changed,
        "initial_bitmap_flag": before_flag,
        "settled_bitmap_flag": after_flag,
        "all_file_payloads_identical": True,
        "early_disk_sha256": hashlib.sha256(before).hexdigest(),
        "settled_disk_sha256": hashlib.sha256(after).hexdigest(),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--disk-tool", type=Path, required=True)
    parser.add_argument("early", type=Path)
    parser.add_argument("settled", type=Path)
    args = parser.parse_args()
    print(json.dumps(compare(args.disk_tool, args.early, args.settled), indent=2))
