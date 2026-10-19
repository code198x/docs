"""Check bridge source contracts, native picture invariants, PCM and saved media."""

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


def digest(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def routine(source: str, name: str) -> str:
    return source.split(name + ":\n", 1)[1].split("\nReturn", 1)[0] + "\nReturn\n"


def check_sources(samples: Path) -> None:
    expected = json.loads((HERE / "inputs.json").read_text())
    folder = samples / "stages/presentation"
    assert {p.name: digest(p.read_bytes()) for p in folder.glob("*.amos")} == expected[
        "sources"
    ]
    sources = {p.stem: p.read_text() for p in folder.glob("*.amos")}
    base = (samples / "stages/session/replay.amos").read_text()
    for source in sources.values():
        for name in ("BR_READ_FRESH", "BR_DRAW_DIE"):
            assert routine(source, name) == routine(base, name), name
        assert source.count("BR_BANKED=BR_BANKED+BR_AWARD") == 1
        assert source.count("BR_DONE=BR_DONE+1") == 1
        assert source.index("Until BR_HANDFIN") < source.index("BR_DONE=BR_DONE+1")
    shared = sources["shared-display"]
    # Expanding the extracted display restores the earlier complete source.
    body = shared.split("BR_DRAW_STATE:\n", 1)[1].split("\nBR_READ_FRESH:", 1)[0]
    assert body.startswith("If BR_HANDFIN\n") and body.endswith("End If\nReturn\n")
    result, active = body[len("If BR_HANDFIN\n") : -len("End If\nReturn\n")].split(
        "\nElse\n"
    )

    def indent(block: str, spaces: int) -> str:
        return (
            "\n".join(" " * spaces + line[3:] for line in block.rstrip().splitlines())
            + "\n"
        )

    restored = (
        shared.split("BR_DRAW_STATE:\n", 1)[0]
        + "BR_READ_FRESH:\n"
        + shared.split("\nBR_READ_FRESH:\n", 1)[1]
    )
    restored = restored.replace("         Gosub BR_DRAW_STATE\n", indent(active, 9), 1)
    restored = restored.replace("      Gosub BR_DRAW_STATE\n", indent(result, 6), 1)
    assert restored == base

    # Grouping changes only the renderer and the callers' control positions.
    def without_display(source: str) -> str:
        start = source.index("BR_DRAW_STATE:\n")
        end = source.index("BR_READ_FRESH:\n", start)
        return source[:start] + source[end:]

    assert without_display(sources["grouped-board"]) == without_display(shared).replace(
        "Locate 0,17", "Locate 1,21"
    )
    bank = sources["bank-cue"]
    old = (samples / "stages/bank-cue.amos").read_text()
    setup = old[old.index("Play Off\n") : old.index("BR_CAP=10")]
    stripped = bank.split("\nBR_SOUND_RESULT:\n", 1)[0]
    stripped = stripped.replace(setup, "", 1).replace("   Play Off\n", "", 1)
    stripped = stripped.replace("            Play Off\n", "", 1)
    stripped = stripped.replace(
        'Until BR_K$="Q"\nPlay Off\nShow', 'Until BR_K$="Q"\nShow', 1
    )
    stripped = stripped.replace("      Gosub BR_SOUND_RESULT\n", "", 1)
    assert stripped == sources["grouped-board"]
    for name in ("bank-cue", "bust-cue", "success-cue"):
        assert (
            sources[name].split("\nBR_SOUND_RESULT:\n")[0]
            == bank.split("\nBR_SOUND_RESULT:\n")[0]
        )
        assert routine(sources[name], "BR_SOUND_RESULT") == routine(
            (samples / "stages" / (name + ".amos")).read_text(), "BR_SOUND_RESULT"
        )
    ready = sources["ready-screen"]
    a = ready.index("Cls 0\nLocate 1,2\n")
    b = ready.index("Randomize Timer\n", a)
    assert ready[:a] + ready[b:] == sources["success-cue"]
    variants = json.loads((HERE / "variants.json").read_text())
    assert set(variants) == {p.stem for p in (HERE / "variants").glob("*.asc")}
    for name, entry in variants.items():
        text = (samples / "stages" / (entry["stage"] + ".amos")).read_text()
        assert text.count("BR_FACE=Rnd(5)+1") == 1
        text = text.replace("BR_FACE=Rnd(5)+1", f"BR_FACE={entry['roll']}")
        if "volume" in entry:
            text = text.replace("Volume 24", f"Volume {entry['volume']}")
        assert (HERE / "variants" / (name + ".asc")).read_text() == text
        assert digest(text.encode()) == entry["sha256"]


def verify(root: Path, tool: Path, samples: Path) -> dict:
    check_sources(samples)
    sequence = json.loads((HERE / "sequence.json").read_text())
    assert sequence and len(sequence) == len(set(sequence))
    assert set(sequence) == {p.name for p in (HERE / "scripts").glob("*.json")}
    source_names = {
        Path(name).stem
        for name in json.loads((HERE / "inputs.json").read_text())["sources"]
    }
    variant_names = set(json.loads((HERE / "variants.json").read_text()))
    for name in source_names | variant_names:
        assert {name + "-import.json", name + "-run.json"} <= set(sequence), name
    captures = {}
    recordings = set()
    for name in sequence:
        assert not (root / (Path(name).stem + "-stderr.txt")).read_text().strip(), name
        report = (root / (Path(name).stem + "-report.txt")).read_text()
        assert report.strip(), name
        for line in report.splitlines():
            json.loads(line)
        for action in json.loads((HERE / "scripts" / name).read_text()):
            if action.get("action") == "save_screenshot":
                p = root / Path(action["path"]).name
                content = p.read_bytes()
                assert (
                    content.startswith(b"\x89PNG\r\n\x1a\n") and len(content) > 500
                ), p.name
                captures[p.name] = digest(content)
            if action.get("action") == "start_audio_recording":
                recordings.add(Path(action["path"]).name)
    expected_recordings = {"bank.wav", "bust.wav", "chosen-bank.wav"}
    for label in ["success", "ready", "muted", "loss"]:
        expected_recordings |= {f"{label}-round-{n}.wav" for n in range(1, 4)}
        expected_recordings.add(label + "-terminal.wav")
    expected_recordings |= {"ready-replay.wav", "loss-replay.wav"}
    assert len(captures) > 100 and recordings == expected_recordings
    pairs = []

    def equal(a: str, b: str) -> None:
        assert (root / (a + ".png")).read_bytes() == (
            root / (b + ".png")
        ).read_bytes(), (a, b)
        pairs.append([a, b])

    for suffix in ["0", "1", "2", "3", "wait", "reset"]:
        equal("baseline-" + suffix, "shared-" + suffix)
    for name in ["bank", "bust"]:
        equal(name + "-result", name + "-stable")
    equal("ready-five-start", "title-stable")
    equal("fifth-result-5", "fifth-no-sixth")
    for suffix in ["held", "invalid", "stable"]:
        equal("chosen-result", "chosen-" + suffix)
    for name in ["success", "ready", "muted", "loss"]:
        for suffix in ["invalid", "ignored-roll", "ignored-space"]:
            equal(name + "-result-3", name + "-" + suffix)
    for name in ["ready", "loss"]:
        equal(name + "-active", name + "-reset")
        equal(name + "-reset", name + "-reset-wait")
    equal("ready-active", "muted-active")
    for n in range(1, 4):
        for suffix in ["roll", "result"]:
            equal(f"ready-{suffix}-{n}", f"muted-{suffix}-{n}")
    audio = {name: measure(root / name) for name in sorted(recordings)}
    bank_pitch = audio["bank.wav"]["bursts"][0]["pitch_hz"]
    assert bank_pitch is not None and 100 < bank_pitch < 2000
    for name, item in audio.items():
        silent = name.startswith("muted-") or name.endswith("-terminal.wav")
        assert item["clipped_samples"] == 0, name
        if silent:
            assert not item["bursts"] and item["peak_pcm"] <= 4, name
            continue
        assert len(item["bursts"]) == 1, (name, item)
        burst = item["bursts"][0]
        ratio = 0.25 if name == "bust.wav" or name.startswith("loss-round-") else 1
        if name in ["success-round-3.wav", "ready-round-3.wav"]:
            ratio = 2
        assert burst["pitch_hz"] is not None
        assert abs(burst["pitch_hz"] / bank_pitch - ratio) < ratio * 0.06, (name, burst)
        assert 0.1 < burst["duration_s"] < 0.3, (name, burst)
        assert min(item["channel_peaks_pcm"]) > 32, name
    expected = json.loads((HERE / "inputs.json").read_text())
    for name in ["amos-work.adf", "presentation.adf"]:
        assert digest((root / name).read_bytes()) == expected["inputs"][name]["sha256"]
        subprocess.run(
            [str(tool), "verify", str(root / name)], check=True, capture_output=True
        )
    disk = root / "integrated-settled.save.adf"
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
    program = files["integrated.amos"]
    assert program.startswith(b"AMOS Basic") and len(program) > 4000
    return {
        "sources": 6,
        "variants": len(json.loads((HERE / "variants.json").read_text())),
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
