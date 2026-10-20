"""Check stage contracts, native evidence invariants, result cues and saved media."""

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


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def routine(source: str, name: str) -> str:
    return source.split(name + ":\n", 1)[1].split("\nReturn", 1)[0] + "\nReturn\n"


def check_sources(samples: Path) -> None:
    folder = samples / "stages/replay-value"
    expected = json.loads((HERE / "inputs.json").read_text())
    assert {p.name: digest(p.read_bytes()) for p in folder.glob("*.amos")} == expected[
        "sources"
    ]
    source = {p.stem: p.read_text() for p in folder.glob("*.amos")}
    previous = (samples / "stages/presentation/ready-screen.amos").read_text()
    for text in source.values():
        for name in ["BR_READ_FRESH", "BR_DRAW_DIE"]:
            assert routine(text, name) == routine(previous, name), name
        assert text.count("BR_BANKED=BR_BANKED+BR_AWARD") == 1
        assert text.count("BR_DONE=BR_DONE+1") == 1
        assert text.index("Until BR_HANDFIN") < text.index("BR_DONE=BR_DONE+1")
        assert 'Until BR_DONE=BR_MAXTURN Or BR_K$="Q"\n' in text
        assert "If BR_DONE<BR_MAXTURN\n" in text
    five = source["five-rounds"]
    # Rules inside one ordinary round remain the original code.
    a = '         If BR_K$="R"\n'
    b = "      Until BR_HANDFIN\n"
    assert five.split(a, 1)[1].split(b, 1)[0] == previous.split(a, 1)[1].split(b, 1)[0]
    for name in ["personal-best", "scorecard", "rescue", "feedback"]:
        text = source[name]
        assert (
            text.index("BR_BEST=0")
            < text.index("BR_MAXTURN=5")
            < text.index("   BR_BANKED=0")
        )
        assert text.count("BR_BEST=BR_BANKED") == 1
        assert "If BR_DONE=BR_MAXTURN\n         If BR_BANKED>BR_BEST\n" in text
        assert text.index("BR_DONE=BR_DONE+1") < text.index("BR_BEST=BR_BANKED")
        assert text.count('Print "New personal best!";') == 1
    for name in ["scorecard", "rescue", "feedback"]:
        text = source[name]
        assert text.count("BR_MARK(BR_DONE)=BR_AWARD") == 1
        assert "BR_DONE=BR_DONE+1\n      BR_MARK(BR_DONE)=BR_AWARD" in text
        assert text.index("Dim BR_MARK(BR_MAXTURN)") < text.index("   BR_BANKED=0")
        assert "   For BR_SLOT=1 To BR_MAXTURN\n      BR_MARK(BR_SLOT)=0\n" in text
        renderer = routine(text, "BR_DRAW_STATE")
        assert "If BR_SLOT<=BR_DONE\n      Print BR_MARK(BR_SLOT)" in renderer
        assert "BR_SLOT=BR_DONE+1 And BR_HANDFIN=0" in renderer
        assert "=BR_AWARD" not in renderer and "BR_BEST=" not in renderer
    for name in ["rescue", "feedback"]:
        text = source[name]
        assert text.count("   BR_RESCUE=1\n") == 1
        pending = text.split('         If BR_RESCUEASK\n            If BR_K$="U"\n', 1)[
            1
        ].split("         Else\n", 1)[0]
        undo, accept = pending.split('            If BR_K$="B"\n')
        assert (
            "BR_RESCUE=0" in undo
            and "BR_TOTAL=BR_BEFORE" in undo
            and "BR_LASTROLL=BR_BEFOREFACE" in undo
        )
        assert "BR_AWARD=" not in undo and "BR_HANDFIN=" not in undo
        assert (
            "BR_AWARD=0" in accept
            and "BR_HANDFIN=-1" in accept
            and "BR_RESCUE=" not in accept
        )
        assert "BR_BANKED=" not in pending and "BR_DONE=" not in pending
        assert text.index('If BR_K$="Q"') < text.index(
            'If BR_RESCUEASK\n            If BR_K$="U"'
        )
    feedback = source["feedback"]
    reveal = routine(feedback, "BR_ROLL_PICTURE")
    assert reveal.count("Wait Vbl") == 2 and "For BR_SPIN=1 To 3" in reveal
    assert all(
        word not in reveal
        for word in [
            "Rnd(",
            "BR_BANKED",
            "BR_TOTAL",
            "BR_DONE",
            "BR_MARK",
            "BR_BEST",
            "Play ",
        ]
    )
    assert "BR_BANKED>=BR_GOAL And BR_REACHED=0" in feedback
    assert routine(feedback, "BR_SOUND_RESULT").startswith("If BR_TARGETCUE\n")
    assert feedback.count("BR_FACE=Rnd(5)+1") == 1
    variants = json.loads((HERE / "variants.json").read_text())
    assert set(variants) == {p.stem for p in (HERE / "variants").glob("*.asc")}
    for name, entry in variants.items():
        text = (samples / "stages" / (entry["stage"] + ".amos")).read_text()
        assert text.count("BR_FACE=Rnd(5)+1") == 1
        if "rolls" in entry:
            text = text.replace("BR_FACE=Rnd(5)+1", "Read BR_FACE").replace(
                "   BR_BANKED=0\n", "   BR_BANKED=0\n   Restore\n", 1
            )
            text += "\nData " + ",".join(map(str, entry["rolls"])) + "\n"
        else:
            text = text.replace("BR_FACE=Rnd(5)+1", f"BR_FACE={entry['roll']}")
        if "volume" in entry:
            text = text.replace("Volume 24", f"Volume {entry['volume']}")
        assert (HERE / "variants" / (name + ".asc")).read_text() == text
        assert digest(text.encode()) == entry["sha256"]


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
        assert {name + "-import.json", name + "-run.json"} <= set(sequence)
    captures = {}
    recordings = set()
    for name in sequence:
        stem = Path(name).stem
        assert not (root / (stem + "-stderr.txt")).read_text().strip(), name
        report = (root / (stem + "-report.txt")).read_text()
        assert report.strip(), name
        for line in report.splitlines():
            json.loads(line)
        for action in json.loads((HERE / "scripts" / name).read_text()):
            if action.get("action") == "save_screenshot":
                p = root / Path(action["path"]).name
                data = p.read_bytes()
                assert data.startswith(b"\x89PNG\r\n\x1a\n") and len(data) > 500, p.name
                captures[p.name] = digest(data)
            if action.get("action") == "start_audio_recording":
                recordings.add(Path(action["path"]).name)
    required_audio = {
        f"{label}-round-{n}.wav" for label in ["live", "muted"] for n in range(1, 6)
    }
    required_audio |= {
        "live-terminal.wav",
        "muted-terminal.wav",
        "pending.wav",
        "pending-invalid.wav",
        "undo.wav",
        "rescue-bank.wav",
        "accept.wav",
        "reveal.wav",
    }
    required_audio |= {f"risk-round-{n}.wav" for n in range(2, 6)}
    assert recordings == required_audio and len(captures) > 120
    pairs = []

    def equal(a: str, b: str) -> None:
        assert (root / (a + ".png")).read_bytes() == (
            root / (b + ".png")
        ).read_bytes(), (a, b)
        pairs.append([a, b])

    equal("live-active", "muted-active")
    for n in range(1, 6):
        for kind in ["roll", "result"]:
            equal(f"live-{kind}-{n}", f"muted-{kind}-{n}")
    equal("risk-pending", "risk-pending-stable")
    equal("risk-restored", "risk-restored-stable")
    equal("live-result-5", "live-stable")
    equal("muted-result-5", "muted-stable")
    equal("live-reset", "live-reset-wait")
    equal("live-roll-1", "reveal-committed")
    assert (root / "reveal-preview.png").read_bytes() != (
        root / "reveal-committed.png"
    ).read_bytes()
    audio = {name: measure(root / name) for name in sorted(recordings)}
    bank_pitch = audio["live-round-1.wav"]["bursts"][0]["pitch_hz"]
    assert bank_pitch is not None and 100 < bank_pitch < 2000
    for name, item in audio.items():
        assert item["clipped_samples"] == 0, name
        silent = name.startswith("muted-") or name in [
            "live-terminal.wav",
            "pending.wav",
            "pending-invalid.wav",
            "undo.wav",
            "reveal.wav",
        ]
        if silent:
            assert not item["bursts"] and item["peak_pcm"] <= 4, name
        else:
            assert len(item["bursts"]) == 1, (name, item)
            burst = item["bursts"][0]
            ratio = (
                0.25 if name.startswith("risk-round-") or name == "accept.wav" else 1
            )
            if name == "live-round-3.wav":
                ratio = 2
            assert burst["pitch_hz"] is not None
            assert abs(burst["pitch_hz"] / bank_pitch - ratio) < ratio * 0.06, (
                name,
                burst,
            )
            assert 0.1 < burst["duration_s"] < 0.3, (name, burst)
            assert min(item["channel_peaks_pcm"]) > 32, name
    for name in ["amos-work.adf", "value.adf", "varied.adf"]:
        assert digest((root / name).read_bytes()) == expected["inputs"][name]["sha256"]
        subprocess.run(
            [str(tool), "verify", str(root / name)], check=True, capture_output=True
        )
    disk = root / "replay-value-settled.save.adf"
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
    program = files["replay-value.amos"]
    assert program.startswith(b"AMOS Basic") and len(program) > 6000
    return {
        "sources": 5,
        "variants": len(names) - 5,
        "capture_hashes": captures,
        "identical_picture_pairs": pairs,
        "audio": audio,
        "saved_program_bytes": len(program),
        "saved_program_sha256": digest(program),
        "saved_disk_sha256": digest(image),
        "original_files_preserved": len(originals),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path)
    parser.add_argument("--disk-tool", type=Path, required=True)
    parser.add_argument("--samples", type=Path, required=True)
    args = parser.parse_args()
    print(json.dumps(verify(args.root, args.disk_tool, args.samples), indent=2))
