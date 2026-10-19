"""Verify native outcomes and reject error screens masquerading as successful play."""

from __future__ import annotations

import argparse
import hashlib
import json
import runpy
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
check_sources = runpy.run_path(str(HERE / "check_sources.py"))["check"]
pixels = runpy.run_path(str(HERE.parent / "2026-10-amos-bank-or-risk-arcade/pixels.py"))
measure = runpy.run_path(
    str(HERE.parent / "2026-10-amos-bank-or-risk-sound/measure_audio.py")
)["measure"]
reader = runpy.run_path(
    str(HERE.parent / "2026-10-amos-bank-or-risk-emu198x/prepare.py")
)
COLOURS = {
    (0, 0, 0),
    (17, 17, 34),
    (255, 255, 238),
    (68, 255, 255),
    (255, 102, 187),
    (255, 238, 68),
    (34, 34, 68),
    (119, 255, 153),
    (187, 170, 221),
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def game_picture(path: Path) -> str:
    unexpected = pixels["colours"](path) - COLOURS
    assert not unexpected, (path.name, sorted(unexpected))
    return digest(path)


def verify_game(root: Path, tool: Path, samples: Path, rebuilt: Path) -> dict:
    result = check_sources(samples)
    phases = json.loads((HERE / "sequence.json").read_text())
    assert phases and len(phases) == len(set(phases))
    assert set(phases) == {p.name for p in (HERE / "scripts").glob("*.json")}
    captures = {}
    recordings = set()
    for name in phases:
        stem = Path(name).stem
        assert not (root / (stem + "-stderr.txt")).read_text().strip(), name
        report = (root / (stem + "-report.txt")).read_text()
        assert report.strip(), name
        for line in report.splitlines():
            json.loads(line)
        for a in json.loads((HERE / "scripts" / name).read_text()):
            if a.get("action") == "save_screenshot":
                p = root / Path(a["path"]).name
                assert p.stat().st_size > 500
                captures[p.name] = digest(p)
            if a.get("action") == "start_audio_recording":
                recordings.add(Path(a["path"]).name)
    result["required_capture_hashes"] = captures
    names = [
        "styled-active",
        "styled-stable",
        "styled-reset",
        "styled-reset-wait",
        "styled-risk-pending",
        "styled-risk-pending-stable",
        "styled-risk-restored",
        "styled-risk-restored-stable",
        "styled-risk-spent-bust",
        "styled-risk-accepted",
        "rom-active",
        "rom-roll",
        "rom-bank",
    ] + [f"styled-{k}-{n}" for n in range(1, 6) for k in ["roll", "result"]]
    result["game_captures"] = {n: game_picture(root / (n + ".png")) for n in names}
    pairs = json.loads((HERE / "stable-picture-pairs.json").read_text())
    for a, b in pairs:
        assert (root / a).read_bytes() == (
            HERE.parent / "2026-10-amos-bank-or-risk-arcade/captures" / b
        ).read_bytes()
    result["stable_picture_pairs"] = pairs
    result["styled_static_pairs"] = []
    for suffix in ["active", "stable"] + [
        f"{k}-{n}" for n in range(1, 6) for k in ["roll", "result"]
    ]:
        a = "styled-" + suffix + ".png"
        b = "static-" + suffix + ".png"
        assert (root / a).read_bytes() == (root / b).read_bytes(), (a, b)
        result["styled_static_pairs"].append([a, b])
    for a, b in [
        ("styled-result-5", "styled-stable"),
        ("styled-reset", "styled-reset-wait"),
        ("styled-risk-pending", "styled-risk-pending-stable"),
        ("styled-risk-restored", "styled-risk-restored-stable"),
    ]:
        assert (root / (a + ".png")).read_bytes() == (
            root / (b + ".png")
        ).read_bytes(), (a, b)
    audio = {n: measure(root / n) for n in sorted(recordings)}
    for name, value in audio.items():
        assert value["clipped_samples"] == 0, name
        if "reveal" in name or "pending-invalid" in name:
            assert not value["bursts"] and value["peak_pcm"] <= 4, name
        else:
            assert len(value["bursts"]) == 1, (name, value)
    for label in ["stable", "styled", "static"]:
        bank = audio[label + "-round-1.wav"]["bursts"][0]["pitch_hz"]
        assert bank and 100 < bank < 2000
        for n in range(1, 6):
            value = audio[f"{label}-round-{n}.wav"]["bursts"][0]
            expected = 2 if n == 3 else 1
            assert abs(value["pitch_hz"] / bank - expected) < expected * 0.06, (
                label,
                n,
                value,
            )
    result["audio"] = audio
    result["rebuilt_disks"] = {}
    for name in [
        "amos-work.adf",
        "complete.adf",
        "styled.adf",
        "style-tests.adf",
        "save-data.adf",
    ]:
        assert (root / name).read_bytes() == (rebuilt / name).read_bytes(), name
        result["rebuilt_disks"][name] = digest(root / name)
    return result


def verify_storage(root: Path, tool: Path) -> dict:
    result = {}
    disk = root / "finish-settled.save.adf"
    subprocess.run([str(tool), "verify", str(disk)], check=True, capture_output=True)
    entries = reader["manifest"](tool, disk)["entries"]
    program = reader["payload"](
        disk.read_bytes(), next(e for e in entries if e["path"] == "finish.amos")
    )
    assert program.startswith(b"AMOS Basic") and len(program) > 10000
    result["saved_program"] = {
        "bytes": len(program),
        "sha256": hashlib.sha256(program).hexdigest(),
        "disk_sha256": digest(disk),
    }
    result["reopened_pictures"] = {
        n: game_picture(root / (n + ".png"))
        for n in ["reopened-active", "reopened-roll", "reopened-bank", "reopened-next"]
    }
    return result


def verify(root: Path, tool: Path, samples: Path, rebuilt: Path) -> dict:
    result = verify_game(root, tool, samples, rebuilt)
    result["storage"] = verify_storage(root, tool)
    return result


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("root", type=Path)
    for n in ["disk-tool", "samples", "rebuilt"]:
        p.add_argument("--" + n, type=Path, required=True)
    a = p.parse_args()
    print(json.dumps(verify(a.root, a.disk_tool, a.samples, a.rebuilt), indent=2))
