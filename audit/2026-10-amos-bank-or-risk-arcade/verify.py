"""Verify unchanged game rules, native palette/motion evidence, cues and storage."""

from __future__ import annotations

import argparse
import hashlib
import json
import runpy
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
READER = runpy.run_path(
    str(HERE.parent / "2026-10-amos-bank-or-risk-emu198x/prepare.py")
)
measure = runpy.run_path(
    str(HERE.parent / "2026-10-amos-bank-or-risk-sound/measure_audio.py")
)["measure"]
pixels = runpy.run_path(str(HERE / "pixels.py"))
contrast = runpy.run_path(str(HERE / "contrast.py"))


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def routine(source: str, name: str) -> str:
    return source.split(name + ":\n", 1)[1].split("\nReturn", 1)[0] + "\nReturn\n"


def check_sources(samples: Path) -> None:
    expected = json.loads((HERE / "inputs.json").read_text())
    folder = samples / "stages/arcade"
    assert {p.name: digest(p.read_bytes()) for p in folder.glob("*.amos")} == expected[
        "sources"
    ]
    source = {p.stem: p.read_text() for p in folder.glob("*.amos")}
    assert all("Curs Off\nFlash Off\nPalette " in t for t in source.values())
    old = (samples / "stages/replay-value/feedback.amos").read_text()

    def game(text: str) -> str:
        return (
            text.split("Repeat\n   Play Off\n   BR_BANKED=0\n", 1)[1]
            .split("\nBR_DRAW_STATE:", 1)[0]
            .replace("Locate 1,23", "Locate 1,21")
        )

    for name, text in source.items():
        assert game(text) == game(old), name
        assert routine(text, "BR_READ_FRESH") == routine(old, "BR_READ_FRESH"), name
        assert routine(text, "BR_SOUND_RESULT") == routine(old, "BR_SOUND_RESULT"), name
        assert text.count("BR_FACE=Rnd(5)+1") == 1
        renderer = routine(text, "BR_DRAW_STATE")
        for value in [
            "BR_BANKED",
            "BR_DONE",
            "BR_AWARD",
            "BR_BEST",
            "BR_RESCUE",
            "BR_RESCUEASK",
            "BR_MARK",
        ]:
            assert not any(
                line.strip().startswith(value + "=") for line in renderer.splitlines()
            ), (name, value)
    for name in ["arcade-colours", "arcade-layout"]:
        assert routine(source[name], "BR_ROLL_PICTURE") == routine(
            old, "BR_ROLL_PICTURE"
        )
    rolling = source["rolling-die"]
    motion = routine(rolling, "BR_ROLL_PICTURE")
    assert "For BR_SPIN=1 To 6" in motion and "For BR_TICK=1 To BR_SPIN" in motion
    assert "If BR_ANIMATE" in motion and 'If BR_ANIMKEY$="Q"' in motion
    assert all(
        word not in motion
        for word in [
            "Rnd(",
            "BR_TOTAL=",
            "BR_BANKED=",
            "BR_DONE=",
            "BR_RESCUE=",
            "BR_BEST=",
            "BR_MARK(",
        ]
    )
    assert motion.endswith("BR_DX=248\nBR_DY=56\nPaper 0\nPen 1\nReturn\n")
    die = routine(rolling, "BR_DRAW_DIE")
    assert "Bar 244,52 To 308,116" in die
    assert all(f"If BR_LASTROLL={face}" in die for face in range(7))
    variants = json.loads((HERE / "variants.json").read_text())
    assert set(variants) == {p.stem for p in (HERE / "variants").glob("*.asc")}
    for name, entry in variants.items():
        text = (samples / "stages" / (entry["stage"] + ".amos")).read_text()
        if "rolls" in entry:
            text = text.replace("BR_FACE=Rnd(5)+1", "Read BR_FACE").replace(
                "   BR_BANKED=0\n", "   BR_BANKED=0\n   Restore\n", 1
            )
            text += "\nData " + ",".join(map(str, entry["rolls"])) + "\n"
        else:
            text = text.replace("BR_FACE=Rnd(5)+1", f"BR_FACE={entry['roll']}")
        if entry.get("gray"):
            text = text.replace(
                "Palette $112,$FFE,$4FF,$F6B,$FE4,$224,$7F9,$BAD",
                "Palette $000,$FFF,$FFF,$FFF,$FFF,$FFF,$FFF,$FFF",
            )
        if "motion" in entry:
            text = text.replace("BR_ANIMATE=1", "BR_ANIMATE=0")
        if "volume" in entry:
            text = text.replace("Volume 24", "Volume 0")
        assert (HERE / "variants" / (name + ".asc")).read_text() == text, name
        assert digest(text.encode()) == entry["sha256"], name
    assert json.loads(json.dumps(contrast["checks"]())) == json.loads(
        (HERE / "contrast.json").read_text()
    )


def verify(root: Path, tool: Path, samples: Path) -> dict:
    check_sources(samples)
    expected = json.loads((HERE / "inputs.json").read_text())
    sequence = json.loads((HERE / "sequence.json").read_text())
    assert sequence and len(sequence) == len(set(sequence))
    assert set(sequence) == {p.name for p in (HERE / "scripts").glob("*.json")}
    names = {Path(n).stem for n in expected["sources"]} | set(
        json.loads((HERE / "variants.json").read_text())
    )
    for name in names:
        assert {name + "-import.json", name + "-run.json"} <= set(sequence), name
    captures = {}
    recordings = set()
    videos = set()
    for name in sequence:
        stem = Path(name).stem
        assert not (root / (stem + "-stderr.txt")).read_text().strip(), name
        report = (root / (stem + "-report.txt")).read_text()
        assert report.strip(), name
        for line in report.splitlines():
            json.loads(line)
        for action in json.loads((HERE / "scripts" / name).read_text()):
            kind = action.get("action")
            if kind == "save_screenshot":
                p = root / Path(action["path"]).name
                data = p.read_bytes()
                assert data.startswith(b"\x89PNG\r\n\x1a\n") and len(data) > 500, p.name
                captures[p.name] = digest(data)
            if kind == "start_audio_recording":
                recordings.add(Path(action["path"]).name)
            if kind == "start_video_recording":
                videos.add(Path(action["path"]).name)
    assert len(captures) > 100
    pairs = []

    def equal(a: str, b: str) -> None:
        assert (root / (a + ".png")).read_bytes() == (
            root / (b + ".png")
        ).read_bytes(), (a, b)
        pairs.append([a, b])

    for suffix in ["active", "roll", "result"]:
        equal("baseline-" + suffix, "gray-" + suffix)
    for other in ["static", "muted"]:
        equal("live-active", other + "-active")
        for n in range(1, 6):
            for kind in ["roll", "result"]:
                equal(f"live-{kind}-{n}", f"{other}-{kind}-{n}")
    for label in ["live", "static", "muted"]:
        equal(label + "-result-5", label + "-stable")
    equal("risk-pending", "risk-pending-stable")
    equal("risk-restored", "risk-restored-stable")
    equal("live-reset", "live-reset-wait")
    equal("live-roll-1", "busy-bank-ignored")
    equal("live-roll-1", "motion-30")
    # Read actual palette pixels, not just configuration strings.
    colours = pixels["colours"](root / "live-result-5.png")
    required = {contrast["rgb"](value) for value in contrast["PALETTE"]}
    assert required <= colours, required - colours
    # All early-preview differences stay in the die region: the score and controls remain stable.
    frames = [
        pixels["read_png"](root / f"motion-{n:02}.png") for n in [2, 4, 6, 9, 12, 16]
    ]
    assert all((w, h) == (1536, 576) for w, h, _ in frames)
    assert len({data for _, _, data in frames}) >= 3
    reference = frames[0][2]
    changed = []
    for _, _, data in frames[1:]:
        for index in range(0, len(reference), 3):
            if reference[index : index + 3] != data[index : index + 3]:
                changed.append((index // 3 % 1536, index // 3 // 1536))
    assert changed
    x1 = min(x for x, _ in changed)
    x2 = max(x for x, _ in changed)
    y1 = min(y for _, y in changed)
    y2 = max(y for _, y in changed)
    assert x2 - x1 + 1 <= 264 and y2 - y1 + 1 <= 136, (x1, y1, x2, y2)
    required_audio = {
        f"{label}-round-{n}.wav" for label in ["live", "muted"] for n in range(1, 6)
    } | {"pending-invalid.wav", "spent-bust.wav", "accept.wav", "reveal.wav"}
    assert recordings == required_audio
    audio = {name: measure(root / name) for name in sorted(recordings)}
    assert len(audio["live-round-1.wav"]["bursts"]) == 1
    bank = audio["live-round-1.wav"]["bursts"][0]["pitch_hz"]
    assert bank is not None and 100 < bank < 2000
    for name, item in audio.items():
        assert item["clipped_samples"] == 0, name
        if name.startswith("muted-") or name in ["pending-invalid.wav", "reveal.wav"]:
            assert not item["bursts"] and item["peak_pcm"] <= 4, name
        else:
            assert len(item["bursts"]) == 1, (name, item)
            burst = item["bursts"][0]
            ratio = (
                0.25
                if name in ["spent-bust.wav", "accept.wav"]
                else 2
                if name == "live-round-3.wav"
                else 1
            )
            assert (
                burst["pitch_hz"] is not None
                and abs(burst["pitch_hz"] / bank - ratio) < ratio * 0.06
            ), (name, burst)
            assert 0.1 < burst["duration_s"] < 0.3, (name, burst)
    assert videos == {"roll.mp4"}
    video_path = root / "roll.mp4"
    assert video_path.stat().st_size > 1000
    probe = json.loads(
        subprocess.check_output(
            [
                "ffprobe",
                "-v",
                "error",
                "-select_streams",
                "v:0",
                "-show_entries",
                "stream=width,height,nb_frames,r_frame_rate:format=duration",
                "-of",
                "json",
                str(video_path),
            ],
            text=True,
        )
    )
    stream = probe["streams"][0]
    assert (
        stream["width"] == 1536
        and stream["height"] == 576
        and int(stream["nb_frames"]) >= 30
    )
    assert float(probe["format"]["duration"]) > 0.5
    for name in ["amos-work.adf", "arcade.adf", "varied.adf"]:
        assert digest((root / name).read_bytes()) == expected["inputs"][name]["sha256"]
        subprocess.run(
            [str(tool), "verify", str(root / name)], check=True, capture_output=True
        )
    disk = root / "arcade-settled.save.adf"
    subprocess.run([str(tool), "verify", str(disk)], check=True, capture_output=True)
    image = disk.read_bytes()
    files = {
        e["path"]: READER["payload"](image, e)
        for e in READER["manifest"](tool, disk)["entries"]
        if e["kind"] == "file"
    }
    originals = json.loads((root / "media-checks.json").read_text())["file_hashes"]
    assert len(originals) == 78
    for name, sha in originals.items():
        assert digest(files[name]) == sha, name
    program = files["arcade.amos"]
    assert program.startswith(b"AMOS Basic") and len(program) > 7000
    return {
        "sources": 3,
        "variants": len(names) - 3,
        "capture_hashes": captures,
        "identical_picture_pairs": pairs,
        "native_palette_colours": sorted(colours),
        "early_motion_change_bounds": [x1, y1, x2, y2],
        "audio": audio,
        "video": probe,
        "video_sha256": digest(video_path.read_bytes()),
        "saved_program_bytes": len(program),
        "saved_program_sha256": digest(program),
        "saved_disk_sha256": digest(image),
        "original_files_preserved": 78,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path)
    parser.add_argument("--disk-tool", type=Path, required=True)
    parser.add_argument("--samples", type=Path, required=True)
    args = parser.parse_args()
    print(json.dumps(verify(args.root, args.disk_tool, args.samples), indent=2))
