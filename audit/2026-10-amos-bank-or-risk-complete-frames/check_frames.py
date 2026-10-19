"""Reject incomplete board transitions in every decoded native video frame."""

from __future__ import annotations

import argparse
import functools
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent

PALETTE = [
    (0, 0, 0),
    (17, 17, 34),
    (255, 255, 238),
    (68, 255, 255),
    (255, 102, 187),
    (255, 238, 68),
    (34, 34, 68),
    (119, 255, 153),
    (187, 170, 221),
]


@functools.lru_cache(maxsize=65536)
def colour(rgb: bytes) -> int:
    return min(
        range(len(PALETTE)),
        key=lambda i: sum((a - b) ** 2 for a, b in zip(rgb, PALETTE[i], strict=True)),
    )


def board(path: Path) -> bytes:
    width, height = 1536, 576
    data = subprocess.check_output(
        [
            "ffmpeg",
            "-v",
            "error",
            "-i",
            str(path),
            "-frames:v",
            "1",
            "-f",
            "rawvideo",
            "-pix_fmt",
            "rgb24",
            "pipe:1",
        ],
        timeout=10,
    )
    assert len(data) == width * height * 3
    # The 320x200 logical screen occupies x164..1443 and y48..447 in this profile.
    return bytes(
        colour(
            data[
                (48 + y * 2 + 1) * width * 3 + (164 + x * 4 + 2) * 3 : (48 + y * 2 + 1)
                * width
                * 3
                + (164 + x * 4 + 2) * 3
                + 3
            ]
        )
        for y in range(200)
        for x in range(320)
    )


def check(frames: Path, before: Path, after: Path) -> dict:
    paths = sorted(frames.glob("*.png"))
    assert len(paths) >= 40, "A continuous transition recording is required"
    a, b = board(before), board(after)
    # The preview changes only the die and busy/footer line. All other fields
    # must match one complete game state, after quantising the near-lossless codec output to the native palette.
    mask = [
        y * 320 + x
        for y in range(184)
        for x in range(320)
        if not (244 <= x <= 312 and 52 <= y <= 118)
    ]
    assert any(a[i] != b[i] for i in mask)
    observed_after = 0
    results = []
    for path in paths:
        data = board(path)
        errors = [sum(data[i] != reference[i] for i in mask) for reference in [a, b]]
        assert min(errors) == 0, (path.name, errors)
        observed_after += errors[1] == 0
        results.append({"frame": path.name, "mismatched_cells": min(errors)})
    assert observed_after > 0, "Recording never reached the settled result"
    return {
        "settled_frames": observed_after,
        "frames": len(paths),
        "codec_tolerance_cells": 0,
        "results": results,
    }


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("frames", type=Path)
    p.add_argument("before", type=Path)
    p.add_argument("after", type=Path)
    args = p.parse_args()
    print(json.dumps(check(args.frames, args.before, args.after), indent=2))
