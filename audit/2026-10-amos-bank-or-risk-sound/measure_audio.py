"""Measure native PCM evidence; these checks do not judge how pleasant a cue sounds."""

from __future__ import annotations

import argparse
import json
import math
import sys
import wave
from array import array
from itertools import pairwise
from pathlib import Path


def measure(path: Path) -> dict:
    with wave.open(str(path), "rb") as stream:
        if stream.getsampwidth() != 2 or stream.getnchannels() != 2:
            raise ValueError("Expected native stereo 16-bit PCM")
        rate = stream.getframerate()
        raw = array("h", stream.readframes(stream.getnframes()))
    if sys.byteorder != "little":
        raw.byteswap()
    if not raw:
        raise ValueError("Empty native recording")
    channels = [raw[0::2], raw[1::2]]
    signal = max(channels, key=lambda ch: sum(value * value for value in ch))
    width = max(1, rate // 200)
    rms = [
        math.sqrt(
            sum(v * v for v in signal[i : i + width]) / len(signal[i : i + width])
        )
        for i in range(0, len(signal), width)
    ]
    threshold = max(8.0, max(rms) * 0.03)
    active = [i for i, value in enumerate(rms) if value > threshold]
    groups: list[list[int]] = []
    for i in active:
        if not groups or i - groups[-1][-1] > 10:
            groups.append([i])
        else:
            groups[-1].append(i)
    bursts = []
    for group in groups:
        start = group[0] * width
        end = min(len(signal), (group[-1] + 1) * width)
        # Measure pitch away from the envelope edges; interpolate zero crossings.
        segment = signal[start + width * 3 : min(end, start + width * 15)]
        crossings = [
            i - previous / (current - previous)
            for i, (previous, current) in enumerate(pairwise(segment))
            if previous <= 0 < current
        ]
        hz = (
            rate * (len(crossings) - 1) / (crossings[-1] - crossings[0])
            if len(crossings) > 1
            else None
        )
        bursts.append(
            {
                "start_s": start / rate,
                "duration_s": (end - start) / rate,
                "pitch_hz": hz,
            }
        )
    return {
        "rate": rate,
        "frames": len(signal),
        "duration_s": len(signal) / rate,
        "peak_pcm": max(abs(v) for v in raw),
        "channel_peaks_pcm": [max(abs(v) for v in ch) for ch in channels],
        "clipped_samples": sum(abs(v) >= 32760 for v in raw),
        "bursts": bursts,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", type=Path)
    args = parser.parse_args()
    print(json.dumps({path.name: measure(path) for path in args.paths}, indent=2))
