"""Check cue counts, relative pitch/volume/duration and silent controls from native WAVs."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from measure_audio import measure


def verify(root: Path) -> dict:
    names = [
        "tone",
        "lower",
        "quieter",
        "longer",
        "perfect",
        "recover",
        "fail",
        "muted",
        "bank-test",
        "bust-test",
        "held-controls",
        "rapid-next",
        "replay-tail",
        "quit-tail",
        "base-startup",
        "passive-tail",
        "tone-timing",
    ]
    result = {name: measure(root / f"{name}.wav") for name in names}
    for name in ["tone", "lower", "quieter", "longer"]:
        assert len(result[name]["bursts"]) == 1, name
        assert result[name]["clipped_samples"] == 0, name
        assert min(result[name]["channel_peaks_pcm"]) > 32, name
    pilot = result["tone"]["bursts"][0]
    bank = pilot["pitch_hz"]
    assert 0.1 < pilot["duration_s"] < 0.3
    assert 0.48 < result["lower"]["bursts"][0]["pitch_hz"] / bank < 0.52
    assert 0.4 < result["quieter"]["peak_pcm"] / result["tone"]["peak_pcm"] < 0.6
    assert 1.6 < result["longer"]["bursts"][0]["duration_s"] / pilot["duration_s"] < 2.2
    expectations = {
        "perfect": [1, 1, 2],
        "recover": [1, 0.25, 1, 1, 2],
        "fail": [0.25, 0.25, 0.25],
        "bank-test": [1, 1, 1],
        "bust-test": [1, 0.25, 1, 1, 1],
        "held-controls": [1],
        "rapid-next": [1],
    }
    for name, ratios in expectations.items():
        actual = result[name]
        assert len(actual["bursts"]) == len(ratios), (name, actual)
        assert actual["clipped_samples"] == 0, name
        for burst, ratio in zip(actual["bursts"], ratios, strict=True):
            assert burst["pitch_hz"] is not None
            assert abs(burst["pitch_hz"] / bank - ratio) < ratio * 0.06, (name, burst)
            assert 0.1 < burst["duration_s"] < 0.3, (name, burst)
    for name in ["muted", "base-startup"]:
        assert not result[name]["bursts"] and result[name]["peak_pcm"] <= 4, (
            name,
            result[name],
        )
    for name in ["replay-tail", "quit-tail"]:
        assert len(result[name]["bursts"]) == 1, (name, result[name])
        assert (
            result[name]["bursts"][0]["duration_s"]
            < result["passive-tail"]["bursts"][0]["duration_s"] * 0.75
        ), (name, result[name])
    # The next-round capture occurs after 9 of the window's 99 native frames.
    burst = result["rapid-next"]["bursts"][0]
    capture_time = result["rapid-next"]["duration_s"] * 9 / 99
    assert burst["start_s"] < capture_time < burst["start_s"] + burst["duration_s"]
    timing = result["tone-timing"]["bursts"][0]
    screen_time = result["tone-timing"]["duration_s"] * 44 / 134
    assert timing["start_s"] < screen_time < timing["start_s"] + timing["duration_s"]
    assert all(item["clipped_samples"] == 0 for item in result.values())
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path)
    args = parser.parse_args()
    print(json.dumps(verify(args.root), indent=2))
