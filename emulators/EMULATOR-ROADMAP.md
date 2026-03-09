# Emulator Integration

**Last Updated:** 2026-03-07

The emulation engine for Code Like It's 198x lives in a sibling project:
**Emu198x** (`~/Projects/Emu198x`). This document describes how the two projects
relate. For emulator architecture, crate inventory, and development priorities,
see the Emu198x docs directly — `Emu198x/docs/README.md` is the entry point.

This file replaces the original `EMULATOR-ROADMAP.md` (2026-01-19), which
described a different architecture (separate repos per emulator, phase-based
plan, `emulator-core`/`emulator-shell` shared crates). That design was
superseded by the Emu198x workspace before implementation began.

---

## What Emu198x Provides

### Current capabilities (all four platforms)

| Capability | How | Status |
|------------|-----|--------|
| Headless screenshot | `--headless --frames N --screenshot out.png` | Working |
| Audio capture | `--headless --frames N --wav out.wav` | Working |
| Input scripts | `--script file.txt` (frame-indexed actions) | Working |
| MCP state inspection | `query`, `query_paths`, `query_memory`, `poke` | Working |
| Deterministic replay | Frame-exact execution from reset | Working |

### Planned capabilities (needed for content)

| Capability | Why we need it | Emu198x status |
|------------|---------------|----------------|
| WASM per-system builds | Browser-embedded interactive examples | Not started |
| Save states | Lesson checkpoints, experiment-and-restore | Not started |
| Visual debugger | "Inspect the machine" teaching moments | Not started |
| MCP push events | `breakpoint_hit`, `frame_complete` for agents | Not started |

### Per-system status

| System | Emu198x status | Content capture ready? |
|--------|---------------|----------------------|
| ZX Spectrum | Production-ready | Yes |
| Commodore 64 | Production-ready | Yes |
| NES | Usable with known gaps | Yes (cartridge software) |
| Amiga | Usable with known gaps | Partial (A500 OCS/ECS) |

See `Emu198x/docs/status.md` for the full support matrix and
`Emu198x/docs/roadmap.md` for active priorities.

---

## Replacing the Docker Screenshot Pipeline

The existing Docker-based capture scripts (`/scripts/c64-screenshot.sh`,
`/scripts/amiga-screenshot.sh`, etc.) use third-party emulators. Emu198x can
now replace these for all four platforms.

### Old workflow

```bash
# Build
docker run --rm -v $(pwd)/code-samples:/code-samples \
  ghcr.io/code198x/commodore-64:latest acme -f cbm -o out.prg program.asm

# Capture (third-party emulator inside Docker)
./scripts/c64-screenshot.sh out.prg screenshot.png --wait 50
```

### New workflow

```bash
# Build (unchanged)
docker run --rm -v $(pwd)/code-samples:/code-samples \
  ghcr.io/code198x/commodore-64:latest acme -f cbm -o out.prg program.asm

# Capture (Emu198x native binary)
cargo run -p emu-c64 --release -- --prg out.prg \
  --headless --frames 50 --screenshot screenshot.png
```

### Per-platform capture commands

```bash
# Spectrum (.sna snapshot)
cargo run -p emu-spectrum --release -- --sna program.sna \
  --headless --frames 100 --screenshot out.png

# C64 (.prg file)
cargo run -p emu-c64 --release -- --prg program.prg \
  --headless --frames 50 --screenshot out.png

# NES (.nes cartridge)
cargo run -p emu-nes --release -- program.nes \
  --headless --frames 60 --screenshot out.png

# Amiga (executable on ADF, requires Kickstart ROM)
cargo run -p amiga-runner --release -- --kick roms/kick13.rom --adf program.adf \
  --headless --frames 300 --screenshot out.png
```

### Audio capture

```bash
# C64 — capture 5 seconds of SID audio
cargo run -p emu-c64 --release -- --prg program.prg \
  --headless --frames 250 --wav audio.wav

# Spectrum — capture beeper/AY audio
cargo run -p emu-spectrum --release -- --sna program.sna \
  --headless --frames 250 --wav audio.wav
```

### Input scripts

Frame-indexed input actions for repeatable demos:

```bash
cargo run -p emu-c64 --release -- --prg program.prg \
  --script demo-inputs.txt --headless --frames 300 --screenshot out.png
```

---

## MCP Integration for Content Verification

Units teach register writes and hardware behaviour. The MCP `query` interface
lets content authors verify claims programmatically.

```
# After running code that sets VIC-II border colour:
query vic.border_colour  →  6  (blue)

# After setting up SID voice 1:
query sid.voice1.frequency  →  7217
query sid.voice1.waveform   →  triangle

# Discover available observable paths:
query_paths cpu.    →  cpu.a, cpu.x, cpu.y, cpu.sp, cpu.pc, cpu.p, ...
query_paths vic.    →  vic.line, vic.border_colour, vic.background_colour, ...
```

This means unit content can include testable assertions rather than prose-only
descriptions of expected state.

---

## What Content Work Should Reference

When writing or revising unit content:

- **Screenshots**: Use Emu198x `--headless --screenshot` instead of Docker scripts
- **Audio clips**: Use `--wav` capture for SID, AY, APU, and Paula demonstrations
- **Register explanations**: Supplement with `query` paths the learner can try
- **Expected output**: Specify the frame count and input script that reproduces it
- **Hardware behaviour**: Cross-reference `Emu198x/docs/systems/{platform}.md`
  and `Emu198x/docs/platforms/` for verified technical detail

### Future: browser embedding

When WASM builds land, unit pages will embed interactive emulators:

```html
<retro-emu
  platform="c64"
  program="/code-samples/commodore-64/game-01/unit-08/program.prg"
  input-script="/code-samples/commodore-64/game-01/unit-08/demo.txt"
  autoplay="false"
/>
```

This replaces static screenshots with live, inspectable emulation. The learner
can pause, step, query registers, and modify code — shifting explanation
overhead from prose to direct interaction with the machine.

---

## Version History

| Date | Changes |
|------|---------|
| 2026-03-07 | Complete rewrite. Replaced original architecture plan with Emu198x integration guide. |
| 2026-01-19 | Original roadmap (superseded). |
