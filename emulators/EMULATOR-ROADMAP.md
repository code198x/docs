# Emulator Roadmap

This document outlines the plan for building a suite of retro platform emulators for Code Like It's 198x. These emulators provide automated screenshot/video capture, input script injection, and interactive play - both as native binaries and WASM bundles for browser embedding.

## Design Principles

Based on the proven architecture from `spectrum-emu`:

1. **Library-first**: Emulator core has no UI, no threads, no real-time limiting. Caller drives execution.
2. **Frame-based execution**: `run_frame()` executes exactly one frame's worth of cycles. Deterministic.
3. **Bus abstraction**: All CPU memory/IO through trait for testability.
4. **Observable state**: Full memory/register inspection at any point.
5. **Input scripts**: Frame-indexed actions for reproducible demos.
6. **Audio event recording**: Store state changes during frame, generate PCM at frame end.

## Technology Stack

### Core (Platform-agnostic)
- **Language**: Rust 2024 edition
- **Dependencies**: Minimal - `flate2` for compression, optional `png` for screenshots

### Interactive Shell (Shared native + WASM)
- **Windowing**: `winit` (works native and browser)
- **Rendering**: `wgpu` (WebGPU native, WebGL2 fallback in browser)
- **Audio (native)**: `cpal`
- **Audio (WASM)**: Web Audio API via `wasm-bindgen`
- **Input (native)**: `gilrs` for gamepads
- **Input (WASM)**: Web Gamepad API

### Build/Package
- **WASM**: `wasm-pack` + `wasm-bindgen`
- **Video capture**: FFmpeg (external process)

## Repository Structure

Separate repositories with shared crates as dependencies:

```
Shared Crates (publish to crates.io or git dependencies):
├── emulator-core       # Bus trait, AudioBackend, InputScript, capture helpers
├── emulator-shell      # winit+wgpu+cpal unified shell
├── debug-core          # Debugger traits, breakpoints, tracing
│
├── cpu-z80             # ~10 platforms
├── cpu-6502            # ~12 platforms
├── cpu-65816           # SNES, Apple IIGS (extends 6502)
├── cpu-68000           # ~6 platforms
├── cpu-6809            # Dragon, CoCo, Vectrex, Thomson
├── cpu-sm83            # Game Boy (Z80 variant)
├── cpu-arm             # Archimedes, GBA, 3DO
├── cpu-sh              # Saturn, Dreamcast
└── cpu-mips            # PlayStation, N64

Emulator Repositories (each follows same pattern):
├── spectrum-emu        # Refactored to use shared crates
├── c64-emu
├── nes-emu
├── amiga-emu
├── snes-emu
├── mega-drive-emu
├── game-boy-emu
└── ... (60+ more potential platforms)
```

### Per-Emulator Repository Structure

```
<system>-emu/
├── Cargo.toml              # Depends on emulator-core, emulator-shell, cpu-*
├── src/
│   ├── lib.rs              # Core emulator (library-first, no deps on shell)
│   ├── chipset/            # Platform-specific chips (VIC-II, SID, PPU, etc.)
│   ├── memory.rs           # Memory map, banking
│   ├── formats/            # File format loaders (PRG, D64, NES, ADF, etc.)
│   └── bin/
│       ├── <system>.rs              # Interactive player (native + WASM)
│       ├── <system>-screenshot.rs   # PNG capture tool
│       └── <system>-video.rs        # MP4/audio capture tool
└── wasm/
    └── package.json        # npm package for browser embedding
```

## CPU Architecture Coverage

| CPU Crate | Platforms Covered |
|-----------|-------------------|
| `cpu-z80` | Spectrum, ZX81, MSX, Amstrad CPC, Master System, Game Gear, ColecoVision, SAM Coupé, + co-processor in Mega Drive, Neo Geo |
| `cpu-sm83` | Game Boy, Game Boy Color |
| `cpu-6502` | C64, VIC-20, PET, Plus/4, NES, Atari 2600/800/5200/7800, Apple II, BBC Micro, Electron, Oric |
| `cpu-65816` | SNES, Apple IIGS |
| `cpu-6809` | Dragon 32, Tandy CoCo, Vectrex, Thomson MO5 |
| `cpu-68000` | Amiga, Atari ST, Mega Drive, X68000, Neo Geo, Macintosh |
| `cpu-arm` | Archimedes, GBA, 3DO |
| `cpu-sh` | Saturn, Dreamcast |
| `cpu-mips` | PlayStation, N64, PS2 |

Additional oddball CPUs (lower priority):
- TMS9900 (TI-99/4A)
- CP1610 (Intellivision)
- Intel 8080 (Altair, IMSAI)
- CDP1802 (RCA Studio II)
- V810 (Virtual Boy, PC-FX)
- i386 (FM Towns, Tandy 1000, IBM PC)

## Emulator API Standard

All emulators implement a common trait for tooling compatibility:

```rust
pub trait Emulator {
    fn run_frame(&mut self) -> u32;
    fn step(&mut self) -> u32;
    fn capture_screen_rgba(&self) -> Vec<u8>;
    fn screen_dimensions(&self) -> (u32, u32);
    fn apply_input(&mut self, action: &InputAction);
    fn frame_count(&self) -> u32;
    fn reset(&mut self);
}

pub trait EmulatorWithAudio: Emulator {
    fn run_frame_with_audio(&mut self, buffer: &mut AudioBuffer) -> u32;
    fn sample_rate(&self) -> u32;
}

pub trait EmulatorWithDebug: Emulator {
    fn cpu_state(&self) -> CpuState;
    fn read_memory(&self, addr: u32) -> u8;
    fn set_breakpoint(&mut self, bp: Breakpoint);
    fn disassemble(&self, addr: u32, count: usize) -> Vec<Instruction>;
}
```

---

## Phase 1: Foundation

### Shared Infrastructure

- [ ] **emulator-core crate**
  - Bus trait (8-bit and 16-bit variants)
  - AudioBackend trait + AudioBuffer
  - InputScript + ScriptBuilder + text parser
  - FFmpeg video encoding helpers
  - PNG screenshot helpers

- [ ] **emulator-shell crate**
  - winit window management
  - wgpu rendering pipeline (scales pixel buffer to window)
  - cpal audio output (native)
  - Web Audio output (WASM)
  - gilrs gamepad input (native)
  - Web Gamepad input (WASM)
  - Unified event loop for native and WASM

- [ ] **cpu-z80 crate**
  - Extract from spectrum-emu
  - Bus abstraction
  - ZEXALL/ZEXDOC test harness
  - Disassembler with annotation support

- [ ] **cpu-6502 crate**
  - Full instruction set (documented + undocumented)
  - Bus abstraction
  - Klaus Dormann test suite
  - Disassembler with annotation support

- [ ] **cpu-68000 crate**
  - Full instruction set
  - Bus abstraction (16-bit data, 24-bit address)
  - Test harness
  - Disassembler with annotation support

### Spectrum Emulator Refactor

- [ ] Refactor spectrum-emu to depend on emulator-core + cpu-z80
- [ ] Add unified interactive binary (native + WASM)
- [ ] Verify existing screenshot/video capture still works

---

## Phase 2: Core Platforms

### C64 Emulator

- [ ] **c64-emu crate**
  - VIC-II graphics (320x200, sprites, raster interrupts)
  - SID audio (3 voices, filters, ring mod)
  - CIA timers and I/O
  - Memory banking (ROM/RAM switching)
  - Joystick and keyboard input

- [ ] **c64-emu binaries**
  - `c64-screenshot` - PNG capture with input scripts
  - `c64-video` - MP4 capture with audio
  - `c64` - Interactive player (native + WASM)

- [ ] **c64-emu file formats**
  - PRG (raw binary)
  - D64 (disk image)
  - T64 (tape archive)
  - CRT (cartridge)

### NES Emulator

- [ ] **nes-emu crate**
  - PPU graphics (256x240, sprites, scrolling, palettes)
  - APU audio (2 pulse, triangle, noise, DMC)
  - Mapper abstraction
  - Controller input

- [ ] **nes-emu binaries**
  - `nes-screenshot`, `nes-video`, `nes`

- [ ] **nes-emu mappers**
  - NROM (mapper 0)
  - MMC1 (mapper 1)
  - UxROM (mapper 2)
  - MMC3 (mapper 4)
  - Additional mappers as needed

- [ ] **nes-emu file formats**
  - iNES (.nes)
  - NES 2.0

### Amiga Emulator

- [ ] **amiga-emu crate**
  - Denise graphics (bitplanes, sprites, HAM, copper effects)
  - Paula audio (4 DMA channels)
  - Agnus DMA controller
  - Blitter
  - Disk controller
  - Mouse and joystick input

- [ ] **amiga-emu binaries**
  - `amiga-screenshot`, `amiga-video`, `amiga`

- [ ] **amiga-emu file formats**
  - ADF (disk image)
  - Kickstart ROM loading

---

## Phase 3: Debug and Teaching Tools

### Debug Infrastructure

- [ ] **debug-core crate**
  - Step debugger traits
  - Breakpoint system (address, value, condition)
  - Execution trace / instruction history
  - Memory inspection traits

- [ ] **Debug UI in emulator-shell**
  - Register visualisation panel
  - Memory viewer/editor
  - Memory heatmap (read/write activity)
  - Disassembly view with annotations
  - Instruction history
  - Cycle counter
  - Audio waveform visualiser (per-channel)

### Teaching Tools

- [ ] Side-by-side comparison (expected vs actual output)
- [ ] Memory diff tool (compare two states)
- [ ] Slow-motion execution mode
- [ ] Record/replay for student submissions

---

## Phase 4: Content Creation Tools

### Graphics Editors

- [ ] **sprite-editor**
  - Platform-aware (C64, Spectrum, NES, Amiga palettes/constraints)
  - Export to native formats
  - wgpu-based, WASM-compatible

- [ ] **tile-map-editor**
  - Background/tilemap editing
  - Platform-specific tile constraints
  - Export to native formats

- [ ] **charset-editor**
  - Font/character set editing
  - Platform-specific character formats

### Audio Tools

- [ ] **tracker**
  - Multi-platform music editor
  - SID (C64)
  - AY-3-8910 (Spectrum 128, MSX, Amstrad)
  - NES APU
  - Paula (Amiga)
  - YM2612 (Mega Drive)
  - Export to native formats

- [ ] **sfx-generator**
  - Sound effect creation
  - Platform-specific synthesis parameters
  - Export to native formats

---

## Phase 5: Extended Platforms

### Additional CPU Crates

- [ ] **cpu-65816** - SNES, Apple IIGS
- [ ] **cpu-6809** - Dragon 32, CoCo, Vectrex
- [ ] **cpu-sm83** - Game Boy

### Wave 2 Emulators (High leverage - shared CPUs)

- [ ] BBC Micro (6502)
- [ ] Atari 800 (6502)
- [ ] Atari 2600 (6502)
- [ ] Master System (Z80)
- [ ] Game Gear (Z80)
- [ ] Mega Drive (68000 + Z80)

### Wave 3 Emulators (New CPU investment)

- [ ] Game Boy / GBC (SM83)
- [ ] SNES (65816)
- [ ] MSX (Z80)
- [ ] Amstrad CPC (Z80)

### Wave 4+ (Complex / 32-bit era)

- [ ] Archimedes (ARM)
- [ ] GBA (ARM7TDMI)
- [ ] PlayStation (MIPS R3000)
- [ ] N64 (MIPS R4300)
- [ ] Saturn (2x SH-2)
- [ ] Dreamcast (SH-4)

---

## Assembler Strategy

**Decision**: Use existing assemblers, don't build new ones.

Current toolchain:
- `pasmonext` - Z80 (Spectrum)
- `acme` - 6502 (C64)
- `ca65` - 6502/65816 (NES, SNES)
- `vasm` - 68000 (Amiga)

Future additions as needed:
- `rgbasm` - SM83 (Game Boy)
- `asmx` - multi-platform
- Platform-specific assemblers for edge cases

**Potential future work** (not prioritised):
- LSP integration for better editor experience
- Unified error format parsing for teaching UI

---

## Integration with Code Like It's 198x

### Automated Capture Pipeline

Each emulator provides CLI tools that integrate with the existing workflow:

```bash
# Build with platform assembler (existing Docker containers)
docker run ... acme -o program.prg program.asm

# Capture with emulator (native binary)
c64-screenshot program.prg screenshot.png --wait 50 --input inputs/demo.txt
c64-video program.prg gameplay.mp4 --duration 500 --input inputs/demo.txt
```

### Browser Embedding

WASM builds enable interactive examples in lessons:

```html
<retro-emu
  platform="c64"
  program="/code-samples/c64/game-01/unit-08/symphony.prg"
  input-script="/code-samples/c64/game-01/unit-08/inputs/demo.txt"
  autoplay="false"
/>
```

### Student Verification

The deterministic, scriptable nature enables automated grading:

1. Run student code with test input script
2. Capture output at specific frames
3. Compare against reference screenshots
4. Report differences

---

## Open Questions

1. **ROM distribution**: How to handle Kickstart (Amiga), BIOS (PlayStation), etc.? Legal constraints require user-supplied ROMs.

2. **Save states**: Should we implement save/load state for teaching checkpoints?

3. **Rewind**: Useful for teaching ("let's see what just happened") but adds complexity.

4. **Performance targets**: What's acceptable for WASM? 60fps on mid-range hardware?

5. **Mobile support**: Do WASM builds need to work on tablets/phones?

---

## Version History

| Date | Changes |
|------|---------|
| 2026-01-19 | Initial roadmap created |
