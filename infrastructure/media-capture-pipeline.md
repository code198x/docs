# Media Capture Pipeline

Screenshots, video, and audio captures verify that every code sample produces the expected output. The pipeline is **manifest-driven**: `code-samples/_capture/capture.py` reads a unit's `capture/manifest.json`, assembles each named `step-NN` program from source, expands the manifest's `timeline` into an Emu198x `--script` JSON, and runs it against a cold-booted machine. Media lands in the website's public asset dirs.

One runner covers every machine; the manifest's top-level `machine` field selects the build and input model.

## The runner

```
code-samples/_capture/capture.py <manifest.json> [--emu PATH] [--keep-build]
```

Each capture in the manifest names a runnable `program` (a `step-NN.asm`, a `.bas`, or typed source) plus a `timeline` of boot / input / record actions. `capture.py` expands that timeline into an Emu198x `--script` JSON and **saves it next to the manifest** as `<capture-id>.script.json` — the honesty artifact: read the script and see exactly how the state was reached and what input was injected. The same runnable step is what an in-page Emu198x (WASM) needs to make a step a run-it / tweak-a-value widget, so the manifest is the single source for both captured media now and the in-page runner later.

## Machines

| `machine` | Build | Input model |
|---|---|---|
| `commodore-64` | Asm198x `.asm` → `.prg` (`--dialect acme --prg`), `--load`, type RUN | joystick (port 0): up/down/left/right/fire; keys |
| `sinclair-zx-spectrum` | Asm198x `.asm` → `.sna` (`--dialect pasmonext --sna`), or `.bas` via `load_basic_program` | keys A–Z/0–9/Space/Enter/CapsShift/SymbolShift; tape autoload |
| `nintendo-entertainment-system` | Asm198x `.asm` → `.nes` (`--dialect ca65`, self-linking iNES), `--rom`, runs from power-on | controller 1 (port 1): up/down/left/right/a/b/select/start |
| `commodore-amiga` | AMOS Pro: typed into the editor, F1 to run (no host build) | joystick (port 2); keys |
| `commodore-amiga-blitz` | Blitz BASIC 2: typed into Ted, compile-and-run (no host build) | joystick; keys; mouse |
| `commodore-amiga-asm` | `.asm` → KS1.x hunkexe → bootable `.adf` (vasm + xdftool) | joystick (port 2) |

## Manifest shape

```json
{ "machine": "sinclair-zx-spectrum",
  "image_dir": "sinclair-zx-spectrum/assembly/<game>/unit-NN",
  "captures": [
    { "id": "step-01-dark", "program": "steps/step-01.asm",
      "timeline": [ {"wait": 12}, {"screenshot": "step-01-dark.png"} ] }
  ] }
```

`image_dir` is relative to `website/public/images/`. It follows the code-samples layout: `<machine>/<track>/<game>/unit-NN` (e.g. `sinclair-zx-spectrum/assembly/shadowkeep/unit-01`).

## Timeline vocabulary

A shared vocabulary, mapped per machine by each `expand_timeline_*` function:

| Action | Effect |
|---|---|
| `{"wait": N}` | run N frames |
| `{"boot_run": true}` | C64 only: wait for boot, type RUN + RETURN |
| `{"key": "SPACE", "frames": N}` | key down, run N frames, key up |
| `{"hold": "up"}` / `{"release": "up"}` | key/button down / up, held across steps |
| `{"press": "fire", "frames": N}` | C64 joystick: button down, N frames, up |
| `{"joy": "right", "frames": N}` / `{"joy_hold": …}` / `{"joy_release": …}` | Amiga joystick (port 2) |
| `{"type": "ZOG\n"}` | Spectrum: type a string (`\n` = ENTER) |
| `{"autoload": N}` | Spectrum: real pulse-driven tape load for up to N frames |
| `{"poke": addr, "value": v}` | capture-setup write to CPU memory to reach a state cheaply |
| `{"screenshot": "name.png"}` | save the current frame as PNG |
| `{"record_video": "name.mp4"}` / `{"stop_video": true}` | start / finish + mux the MP4 (H.264 + AAC) |
| `{"record_audio": "name.wav"}` / `{"stop_audio": true}` | start / finish the WAV (16-bit PCM) |

## Output paths

Media lands under `website/public/` at the `image_dir` the manifest declares:

| Medium | Output path |
|---|---|
| Screenshot | `website/public/images/<image_dir>/<name>.png` |
| Video | `website/public/images/<image_dir>/<name>.mp4` (H.264 + AAC, browser-embeddable) |
| Audio | `website/public/images/<image_dir>/<name>.wav` (16-bit PCM) |

## Timing guidelines

| Scenario | Settle frames | Capture frames |
|---|---|---|
| Static screen, no animation | 5–10 | n/a (screenshot only) |
| Animation loop, screenshot mid-loop | match the cycle | n/a |
| Video — short demo | 10 | 250–500 (5–10 sec @ 50Hz) |
| Video — gameplay | 10–30 | 500–1500 (10–30 sec) |
| Audio — title theme loop | 0–10 | 1500–3000 (30–60 sec) |
| Audio — SFX clip | 0 | 50–200 (1–4 sec) |

Frame counts are native 50Hz video frames; 50 frames = 1 second of PAL.

## ROM requirements

- **ZX Spectrum**: 48K ROM at `~/.emu198x/roms/sinclair-zx-spectrum-48k/48.rom`. Emu198x picks it up automatically. The Spectrum has a 16 KB BASIC/system ROM and needs a copy to boot.
- **C64**: ROMs at `~/Projects/Reference/commodore/c64/extracted/`.
- **Amiga**: Kickstart ROMs at `~/.emu198x/roms/commodore-amiga/` (`kick13.rom` for the assembly track, `kick204.rom` for AMOS/Blitz). Not distributable.
- **NES**: no system ROM needed.

## Tooling requirements

- **Emu198x binaries** at `~/Projects/198x/Emu198x/emu198x/target/{debug,release}/emu198x-{machine}`. Build from the `emu198x/` workspace with `cargo build --release --bin emu198x-{machine}` (add `--no-default-features` for a headless-only build that skips winit/wgpu/muda). `capture.py` resolves the binary per machine from `--emu`, then `$EMU198X_{MACHINE}`, then a default path.
- **Asm198x** at `~/Projects/198x/Asm198x/asm198x/target/release/asm198x`, or `$ASM198X`. The family assembler; the Spectrum build path since 2026-07-02.
- **ffmpeg** on PATH for video capture only. The Emu198x binary spawns ffmpeg for the H.264 + AAC mux.
- **Pillow** (optional) for screenshot re-framing on the Amiga tracks (`frame_screenshot` centres the raw raster).

## Key rule

**Every captured media artefact must be verified with the Read tool before use.** Check for rendering errors, audio glitches, video corruption — and document what you see. The capture script returning success is necessary but not sufficient; the output file is what ships.

## See also

- `code-samples/_capture/capture.py` — the manifest-driven capture runner.
- A unit's `capture/manifest.json` + generated `capture/<id>.script.json` — the per-unit capture recipe and its honesty artifacts.
- [`decisions/real-retro-games.md`](../decisions/real-retro-games.md) — the multi-disciplinary commitment that makes video and audio capture part of every unit's Definition of Done.
- [`../../decisions/code198x-dev-tooling-migration.md`](../../decisions/code198x-dev-tooling-migration.md) — the migration to Asm198x + Emu198x as the family's own toolchain.
