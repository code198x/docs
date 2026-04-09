# Emulator Integration

**Last Updated:** 2026-04-09

The emulation engine for Code Like It's 198x lives in a sibling project:
**Emu198x** (`~/Projects/Emu198x`). This document describes how the two projects
relate and which capabilities are wired up *today*. For Emu198x's own
architecture, plan, and decisions, see `~/Projects/Emu198x/wiki/index.md` and
`~/Projects/Emu198x/docs/plans/2026-04-07-feat-spectrum-completeness-plan.md`.

This file was rewritten on 2026-04-09 to reflect the post-fresh-start state of
Emu198x. The previous version (2026-03-07) described an architecture that no
longer exists — the April 2026 fresh-start rewrite changed the cycle-accuracy
core, dropped the multi-system implementations, and rebuilt the workspace from
scratch. **Treat any pre-2026-04-09 claims about Emu198x as historical, not
current.** The claims below are what works as of today.

---

## What's actually shipped (2026-04-09)

### Spectrum

Emu198x's **only** production-ready system today is the Sinclair ZX Spectrum
family. Eleven variants boot:

| Variant | Status |
|---------|--------|
| ZX Spectrum 16K | Boots, no peripherals |
| ZX Spectrum 48K | Boots, tape, Kempston joystick |
| ZX Spectrum 128K | Boots, AY, tape |
| ZX Spectrum +2 | Boots, AY, tape |
| ZX Spectrum +2A / +2B / +3 | Boots, AY, +3 disk drive (read only) |
| Pentagon 128 | Boots, TR-DOS (read only) |
| Scorpion ZS-256 | Boots, TR-DOS (read only) |
| Timex TC2048 / TC2068 / TS2068 | Boots, hi-res mode |

**Disk writes are not implemented.** TR-DOS `SAVE` and +3 BASIC `SAVE *"a:..."`
silently fail. This is the current Phase 1.6/1.7 work in the Emu198x plan; it's
deferred until there's a real user need.

**Tape writes are not implemented.** BASIC `SAVE` to tape captures the audio but
nothing currently writes a `.tap` from it. Phase 1.4 work, also deferred.

### C64 / NES / Amiga

**Not implemented in Emu198x post-rewrite.** The pre-rewrite codebase had
working C64 / NES / Amiga implementations that were thrown out when the
cycle-accuracy approach changed; they have not yet been ported across.

For Code198x content production, the C64 / NES / Amiga scripts in
`/scripts/emu-screenshot-{c64,nes,amiga}.sh` and `emu-video-{c64,nes,amiga}.sh`
are **broken against current Emu198x** (they call binaries that don't exist).
They were authored against the pre-rewrite Emu198x interface and have not been
updated. Until C64 / NES / Amiga are reimplemented in Emu198x — or until we
decide to use a third-party emulator for those platforms — content production
for those systems is blocked or needs a different tool.

This is a known divergence and a real planning question — see "Open question"
at the bottom of this document.

---

## Spectrum content pipeline (working now)

The `emu198x-script-spectrum` binary is a headless content-pipeline CLI built
specifically for batch tutorial-asset production. Two ways to invoke it.

### Fast path (one-line common case)

```bash
EMU=/Users/stevehill/Projects/Emu198x/target/release/emu198x-script-spectrum

# Screenshot from a snapshot
$EMU game.sna --frames 250 --screenshot game.png

# Audio capture
$EMU game.sna --frames 250 --wav game.wav

# Video capture (requires ffmpeg on PATH)
$EMU game.sna --frames 250 --video game.mp4

# Different model
$EMU game.sna --model 128k --frames 300 --screenshot game.png
```

The positional argument is any file the runtime's `load_file` router handles:
`.tap`, `.tzx`, `.z80`, `.sna`, `.trd`, `.dsk`, or `.zip` containing one of
those.

### Script path (anything more complex)

For multi-step recipes (load + type input + screenshot + audio + video), pass
a JSON script:

```bash
$EMU --script my-recipe.json
$EMU --script - < my-recipe.json   # stdin works too
```

The script is a JSON array of method-tagged objects. Methods:

| Method | Params | What it does |
|---|---|---|
| `load` | `{"path": "..."}` | Load `.tap`/`.tzx`/`.z80`/`.sna`/`.trd`/`.dsk`/`.zip` |
| `run_frames` | `{"count": N}` | Advance N frames at native speed |
| `key_down` / `key_up` | `{"key": "Q"}` | Press / release a single key |
| `type_text` | `{"text": "RUN\n", "hold_frames": 2}` | Type a string of ASCII text |
| `joystick` | `{"state": 16}` | Set Kempston joystick (raw bitfield) |
| `screenshot` | `{"save_path": "out.png"}` | PNG of current framebuffer |
| `record_wav` | `{"save_path": "out.wav", "frames": 250}` | WAV over the next N frames |
| `record_video` | `{"save_path": "out.mp4", "frames": 500}` | MP4 over the next N frames |
| `inject_basic` | `{"source": "10 PRINT \"HI\""}` or `{"path": "prog.bas"}` | Tokenise and inject BASIC source directly into RAM (no tape loader) |

#### `inject_basic` — direct BASIC injection

The Spectrum-specific killer feature. Tokenises BASIC source via the
`format-sinclair-zx-spectrum-bas` crate (validated against the 511 `.bas`
files in `code-samples/sinclair-zx-spectrum/` — zero failures), then writes
the tokenised bytes directly into RAM at the address held by the `PROG`
sysvar. Bypasses the tape loader entirely — **no "Program: X" loading
screen**.

Example recipe — load BASIC, run, screenshot:

```json
[
  {"method": "run_frames", "params": {"count": 250}},
  {"method": "inject_basic", "params": {"path": "code-samples/sinclair-zx-spectrum/patterns/basic/screen-frame.bas"}},
  {"method": "type_text", "params": {"text": "K\n"}},
  {"method": "type_text", "params": {"text": "R\n"}},
  {"method": "run_frames", "params": {"count": 100}},
  {"method": "screenshot", "params": {"save_path": "screen-frame.png"}}
]
```

Notes on the recipe shape:

- `run_frames(250)` first to let the 48K ROM boot to the BASIC prompt. 128K
  needs more (the boot menu has to be dismissed).
- `inject_basic` writes the tokenised program at PROG and resets the BASIC
  editor's `K_CUR` cursor position so follow-up keystrokes go to the new
  edit line, not the old one. The machine doesn't see any visible change
  from this — the program is now in memory, ready to run.
- `type_text("R\n")` types `R` in K-mode, which produces the `RUN` keyword
  in one keystroke (Spectrum 48K BASIC keyword typing). Then Enter executes.
  **Don't type `RUN` letter-by-letter** — `R` already produces the entire
  RUN keyword in K-mode; the `U` and `N` would then be appended as letters,
  producing `RUNUN`.

### Available shell scripts

- `scripts/emu-screenshot-spectrum.sh` — fast-path wrapper, takes `<input>
  <output.png> [--frames N] [--model MODEL]`.
- `scripts/emu-video-spectrum.sh` — script-path wrapper, takes `<input>
  <output.mp4> [--wait N] [--frames N] [--model MODEL]`. Uses a JSON script
  internally to separate the wait-frames from the record-frames.

Both scripts override the binary path with the `EMU_SPECTRUM` environment
variable. The default points at
`~/Projects/Emu198x/target/release/emu198x-script-spectrum`.

### What this enables for Code198x today

- Take a `pasmonext --sna` output and produce screenshots / video / audio for
  every assembly tutorial step.
- Take a `.bas` file from `code-samples/sinclair-zx-spectrum/basic/` and
  produce a screenshot of its rendered output (with the LIST workaround for
  the BASIC injection follow-up).
- Drive multi-step recipes (load + type + screenshot + audio) via a JSON
  script, repeatable in CI.

---

## What's not yet wired up

These were aspirational in the previous version of this document. They are
**not** implemented today, but they're on the Emu198x plan.

| Capability | Why we want it | Status |
|---|---|---|
| WASM per-system builds | Browser-embedded interactive examples | Not started |
| Save states | Lesson checkpoints, experiment-and-restore | **Shipped 2026-04-09 in Emu198x Phase 1.1** — `Alt+S` / `Alt+L` in the SDL bin, `save_state` / `load_state` MCP tools. Not yet exposed in `emu198x-script-spectrum`. |
| Visual debugger | "Inspect the machine" teaching moments | Not started |
| MCP push events | `breakpoint_hit`, `frame_complete` for agents | Not started |
| `query` / `poke` MCP tools | Content verification ("after this code, does VIC-II border = 6?") | Spectrum-side: a different MCP tool surface ships in `emu198x-mcp-spectrum` (`get_registers`, `read_memory`, etc.). The exact `query` syntax from the previous roadmap doesn't exist. |
| C64 / NES / Amiga in Emu198x | Multi-platform content pipeline through one tool | Not started post-rewrite |

---

## Open question: multi-platform

The previous version of this document assumed Emu198x would cover all four
Code198x platforms. Today, Emu198x has only the Spectrum, and the user has
explicitly prioritised "get Spectrum content live for October" over the other
three platforms.

This leaves a real planning question for Code198x:

**For C64, NES, and Amiga content production through October, what tool do we use?**

Three options:

1. **Wait for Emu198x to grow C64 / NES / Amiga.** Multi-month effort each.
   Realistic timeline puts these well after October. Not viable for current
   content needs.
2. **Use a third-party emulator** (VICE for C64, FCEUX or Mesen for NES, FS-UAE
   or WinUAE for Amiga). The pre-rewrite Code198x scripts assumed Emu198x for
   all four; we'd need to rewrite them to call the third-party tools. Each
   tool has its own headless / scripting story to learn.
3. **Defer those platforms entirely** until Emu198x catches up. Spectrum
   tutorials ship for October; C64 / NES / Amiga tutorials wait.

The right answer depends on how much C64 / NES / Amiga content is on the
near-term Code198x roadmap and how much existing content depends on
screenshots from those platforms. As of 2026-04-09 this is undecided.

---

## Version history

| Date | Changes |
|------|---------|
| 2026-04-09 | Complete rewrite. Acknowledges the Emu198x April 2026 fresh-start rewrite. Documents the actual Spectrum content-pipeline shipped today (`emu198x-script-spectrum`, `inject_basic`, fast path + JSON script). Marks C64 / NES / Amiga as not-implemented. Surfaces the multi-platform planning question. |
| 2026-03-07 | Previous version. Described a state of Emu198x that the rewrite obsoleted. Aspirational claims about cross-platform `emu-c64`, `emu-nes`, `amiga-runner` binaries that did not survive the rewrite. |
| 2026-01-19 | Original roadmap (superseded). |
