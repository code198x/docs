# Media Capture Pipeline

Screenshots, video, and audio captures verify that every code sample produces the expected output. The pipeline drives Emu198x's headless / script mode (and increasingly the MCP equivalent) directly from per-platform shell scripts.

This page reflects the Spectrum pipeline as of 2026-05-14, with the snapshot-driven flow that landed after Emu198x commit `ff02827` taught `LoadSnapshot` to accept portable `.sna` / `.z80` / `.zip` formats. The other three platforms are post-October work; their pipelines lag behind and will catch up as the curriculum reaches each one.

## Scripts by platform and medium

| Platform | Screenshot | Video | Audio |
|---|---|---|---|
| **ZX Spectrum** | `scripts/emu-screenshot-spectrum.sh` + `code-samples/scripts/capture-spectrum-screenshot.sh` | `scripts/emu-video-spectrum.sh` | `scripts/emu-audio-spectrum.sh` |
| C64 | `scripts/emu-screenshot-c64.sh` | `scripts/emu-video-c64.sh` | _to do_ |
| NES | `scripts/emu-screenshot-nes.sh` | `scripts/emu-video-nes.sh` | _to do_ |
| Amiga | `scripts/emu-screenshot-amiga.sh` | `scripts/emu-video-amiga.sh` | _to do_ |

The `scripts/` directory at the project root holds the modern Emu198x-script-driven wrappers (one binary, one JSON, headless). The older platform-specific dev directories (`{platform}-dev/scripts/`) hold a previous generation of scripts using xdotool / X displays / Docker; they predate the unified Emu198x scripting model and will be retired as each platform's pipeline migrates.

The `code-samples/scripts/capture-spectrum-screenshot.sh` script is a higher-level wrapper that resolves Code198x's `game-NN-name/unit-NN/` directory convention into the right `.sna` and `.png` paths and calls Emu198x. Use it as the per-unit entry point; the lower-level `scripts/emu-*.sh` scripts are useful for one-off captures or ad-hoc work.

## Spectrum pipeline (current)

### Input

`.sna` (or `.z80`, or `.zip` wrapping either). Built by pasmonext from the unit's `.asm` source via the Makefile in each unit directory.

`.tap` remains a Makefile target because it's the canonical format for real-hardware loading (Spectrum Next loads from tape). It is no longer the screenshot-pipeline input.

### Flow

1. `LoadSnapshot` step restores the snapshot directly into the live machine. No tape loader animation; no `Bytes: <name>` header on screen.
2. `RunFrames` step gives the program time to execute (default 10 frames is enough for any unit's settle).
3. `SaveScreenshot` / `StartVideoRecording` + `RunFrames` + `StopVideoRecording` / `SaveAudioCapture` writes the artefact.

### Output paths

| Medium | Output path |
|---|---|
| Screenshot | `website/public/images/sinclair-zx-spectrum/<game>/<unit>/screenshot.png` |
| Video | `website/public/videos/sinclair-zx-spectrum/<game>/<unit>/<name>.mp4` (H.264 + AAC, browser-embeddable) |
| Audio | `website/public/audio/sinclair-zx-spectrum/<game>/<unit>/<name>.wav` (16-bit PCM, 44.1 kHz mono) |

### Timing guidelines

| Scenario | Settle frames | Capture frames |
|---|---|---|
| Static screen, no animation | 5–10 | n/a (screenshot only) |
| Animation loop, screenshot mid-loop | match the cycle | n/a |
| Video — short demo | 10 | 250–500 (5–10 sec @ 50Hz) |
| Video — gameplay | 10–30 | 500–1500 (10–30 sec) |
| Audio — title theme loop | 0–10 | 1500–3000 (30–60 sec) |
| Audio — SFX clip | 0 | 50–200 (1–4 sec) |

Frame counts are native 50Hz video frames; 50 frames = 1 second of PAL.

## Other platforms (legacy)

Until each platform's pipeline migrates to the Emu198x-script model, the existing legacy scripts apply. The previous version of this page documented those; the key historical facts:

- **C64**: Docker-driven (`commodore-64-dev/scripts/c64-screenshot.sh`). ROMs symlinked from `~/Projects/Reference/commodore/c64/extracted/`.
- **Amiga**: Docker-driven (`commodore-amiga-dev/scripts/amiga-screenshot.sh`). Kickstart ROM required, not distributable, lives at `~/Projects/Reference/amiga/Firmware/`.
- **NES**: Docker command (`nes-screenshot`). No ROMs needed.

These will be replaced by `scripts/emu-{screenshot,video,audio}-{c64,nes,amiga}.sh` calling Emu198x's per-platform headless binaries (already present in the Emu198x release directory) as each platform's curriculum work begins.

## ROM requirements

- **ZX Spectrum**: 48K ROM at `~/.emu198x/roms/sinclair-zx-spectrum-48k/48.rom`. Emu198x picks it up automatically from this conventional path.
- **C64**: ROMs at `~/Projects/Reference/commodore/c64/extracted/` (symlinked from `commodore-64-dev/roms/`).
- **Amiga**: Kickstart ROM at `~/Projects/Reference/amiga/Firmware/` (not distributable).
- **NES**: no ROMs needed (the NES has no system ROM).

The earlier claim on this page that Spectrum "no ROMs needed" was wrong. The Spectrum has a 16 KB BASIC/system ROM, and Emu198x needs a copy of it to boot.

## Tooling requirements

- **Emu198x binaries** at `~/Projects/Emu198x/target/release/emu198x-{platform}`. Build with `cargo build --release --bin emu198x-{platform}` (add `--no-default-features` for a headless-only build that skips winit/wgpu/muda).
- **pasmonext** in the Spectrum Docker image (`ghcr.io/code198x/sinclair-zx-spectrum:latest`) used by the per-unit Makefile. Native install would let the Makefile skip Docker; pasmonext is Apple Silicon native.
- **ffmpeg** on PATH for video capture only. The Emu198x binary spawns ffmpeg for the H.264 + AAC mux.

## Key rule

**Every captured media artefact must be verified with the Read tool before use.** Check for rendering errors, audio glitches, video corruption — and document what you see. The capture script returning success is necessary but not sufficient; the output file is what ships.

## See also

- `code-samples/scripts/capture-spectrum-screenshot.sh` — per-unit Spectrum screenshot wrapper.
- `scripts/emu-{screenshot,video,audio}-spectrum.sh` — lower-level Spectrum wrappers.
- [`decisions/real-retro-games.md`](../decisions/real-retro-games.md) — multi-disciplinary commitment that makes video and audio capture part of every unit's Definition of Done.
- The `.claude/skills/{screenshot,video}-spectrum/SKILL.md` skills — MCP-driven alternative to these shell scripts; same underlying Emu198x capability, different driver.
