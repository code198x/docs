# Platform-Specific Lesson Creation Skills

**Version:** 1.0
**Date:** 2025-11-05
**Status:** Summary document

---

## Overview

Platform-specific lesson creation skills extend the generic `lesson-creation-workflow` with platform-specific requirements for compilation, validation, and screenshot capture.

**Complete skill:** `c64-lesson-creation` at `/docs/skills/c64-lesson-creation/SKILL.md`

**Remaining skills:** Specifications below (full skills to be expanded as needed)

---

## Skill Structure (All Platforms)

Each platform-specific skill includes:

1. **Language rules** - Platform-specific syntax, limitations, anti-patterns
2. **Required files checklist** - Code samples, compiled binaries, screenshots, lesson MDX
3. **Compilation process** - Exact commands, flags, error handling
4. **Screenshot capture** - Emulator-specific method (automated/manual)
5. **Platform-specific validation** - Memory maps, registers, hardware limits
6. **Anti-patterns** - Common mistakes specific to platform
7. **Integration** - Which validation skills to run
8. **Complete workflow checklist** - Step-by-step from preparation to navigation update

---

## C64 BASIC (c64-lesson-creation)

✅ **Status:** Complete

**Location:** `/docs/skills/c64-lesson-creation/SKILL.md`

**Key requirements:**
- petcat compilation (`-w2` for BASIC V2)
- Lowercase keywords in .bas, uppercase in MDX
- NO indentation
- VICE x64sc screenshot capture
- Semantic validation (memory addresses, BASIC V2 limits)
- PETSCII vs screen code awareness

---

## C64 6510 Assembly (c64-6510-lesson-creation)

**Status:** Specification below (full skill TBD)

### Compilation
```bash
# Assemble with ca65
ca65 -t c64 example-1.asm -o example-1.o

# Link with ld65
ld65 -t c64 example-1.o -o example-1.prg
```

### Key Requirements
- ca65/ld65 toolchain (cc65 suite)
- 6510 instruction set (6502 + illegal opcodes optional)
- Memory map: $0801 start (BASIC stub), $1000+ for code
- Zero page usage: $FB-$FE safe, others check conflicts
- Hardware registers: Same as BASIC (VIC-II $D000, SID $D400, CIA $DC00)

### Anti-Patterns
- Not preserving registers (A/X/Y clobbered)
- Forgetting SEI/CLI around interrupt setup
- Uninitialized zero page pointers
- Busy-wait without checking interrupt flags

### Screenshot Capture
Same as C64 BASIC: x64sc with .prg autostart

---

## NES 6502 Assembly (nes-lesson-creation)

**Status:** Specification below (full skill TBD)

### Compilation
```bash
# Assemble with ca65
ca65 example-1.asm -o example-1.o

# Link with ld65 using NES config
ld65 -C nes.cfg example-1.o -o example-1.nes
```

### Key Requirements
- ca65/ld65 with NES configuration
- 6502 instruction set (no illegal opcodes)
- iNES header required (.nes file format)
- Mapper specification (NROM, MMC1, etc.)
- PPU registers: $2000-$2007
- APU registers: $4000-$4017
- Controller: $4016-$4017

### NES-Specific Validation
- VBlank timing (PPU updates only during VBlank)
- Sprite limit (8 per scanline, 64 total)
- Palette restrictions (52 colours, 4 palettes of 4 colours)
- CHR-ROM/RAM configuration
- Nametable mirroring (horizontal/vertical)

### Screenshot Capture
```bash
# FCEUX emulator (automated)
fceux --loadlua screenshot.lua example-1.nes

# Or manual: File → Screenshot
```

**Note:** FCEUX screenshot automation requires Lua script.

---

## ZX Spectrum BASIC (zx-lesson-creation)

**Status:** Specification below (full skill TBD)

### Compilation
```bash
# Compile with zmakebas
zmakebas -o example-1.tap -n LESSON example-1.bas
```

### Key Requirements
- zmakebas compiler (produces .tap files)
- Sinclair BASIC (different from Commodore BASIC)
- Case-insensitive keywords
- BEEP for sound (no sound chip)
- ULA for graphics (attribute-based colour)
- 256×192 pixels, 32×24 characters

### ZX BASIC Differences
- `LET` keyword mandatory for assignment
- `PRINT AT y,x` for positioning (note: y,x not x,y)
- `INK`, `PAPER`, `BORDER` for colours (0-7)
- `BEEP duration,pitch` for sound
- `PEEK`/`POKE` but different memory map than C64

### Screenshot Capture
```bash
# FUSE emulator (manual - automation resists)
fuse example-1.tap

# Manual: Media → Screenshot
```

**Note:** FUSE screenshot automation unreliable, manual capture preferred.

---

## ZX Spectrum Z80 Assembly (zx-z80-lesson-creation)

**Status:** Specification below (full skill TBD)

### Compilation
```bash
# Assemble with sjasmplus
sjasmplus example-1.asm --raw=example-1.bin

# Or create .tap file
sjasmplus example-1.asm --tap=example-1.tap
```

### Key Requirements
- sjasmplus assembler (Z80 support)
- Z80 instruction set (not 6502!)
- Memory map: $4000-$57FF screen, $5800-$5AFF attributes, $5B00+ code
- No hardware sprites (software sprites only)
- ULA port $FE for border/sound
- Keyboard: port $FE with row scanning

### Z80 vs 6502 Differences
- Different registers: A, B, C, D, E, H, L (not A, X, Y)
- 16-bit operations native (HL, BC, DE pairs)
- Different instruction mnemonics
- Shadow registers (AF', BC', DE', HL')

### Screenshot Capture
Same as ZX BASIC: FUSE emulator, manual capture

---

## Amiga AMOS BASIC (amiga-lesson-creation)

**Status:** Specification below (full skill TBD)

### Compilation
```bash
# AMOS BASIC compiled with AMOS Pro (requires Amiga emulator)
# Or use AMOS tokenizer tools

# Typically .abk (AMOS bank) file format
```

### Key Requirements
- AMOS Pro or AMOS tokenizer
- Amiga-specific BASIC (sprites, bobs, screens)
- Blitter-accelerated graphics
- Paula audio (4 channels)
- Intuition GUI commands
- Amiga colour system (4096 colours, 32 on screen)

### AMOS Specifics
- `Curs Off` / `Curs On` - Hide/show cursor
- `Screen Open` - Create custom screens
- `Sprite` - Hardware sprite commands
- `Bob` - Blitter objects (software sprites)
- `Music` / `Sam Play` - Audio playback

### Screenshot Capture
```bash
# FS-UAE emulator
fs-uae --amiga-model=A1200 example-1.adf

# Manual: Screenshot via menu
```

---

## Amiga 68000 Assembly (amiga-68k-lesson-creation)

**Status:** Specification below (full skill TBD)

### Compilation
```bash
# Assemble with vasm
vasm6800_mot -Fhunkexe -o example-1 example-1.asm
```

### Key Requirements
- vasm assembler (68000 support, mot syntax)
- 68000 instruction set
- Amiga executable format (hunk)
- Copper for display effects
- Blitter for graphics
- Paula for audio
- CIA for I/O

### 68000 Specifics
- Registers: D0-D7 (data), A0-A7 (address)
- Memory-to-memory operations (unlike 6502/Z80)
- Privilege levels (user/supervisor)
- Custom chip registers: $DFFxxx
- Exec library calls
- AmigaDOS conventions

### Screenshot Capture
Same as AMOS: FS-UAE emulator, manual capture

---

## Quick Reference Matrix

| Platform | Language | Compiler | Emulator | Screenshot | Difficulty |
|----------|----------|----------|----------|------------|------------|
| C64 | BASIC V2 | petcat | x64sc (VICE) | Automated OK | Easy |
| C64 | 6510 ASM | ca65/ld65 | x64sc (VICE) | Automated OK | Medium |
| NES | 6502 ASM | ca65/ld65 | FCEUX | Lua script | Hard |
| ZX | Sinclair BASIC | zmakebas | FUSE | Manual only | Easy |
| ZX | Z80 ASM | sjasmplus | FUSE | Manual only | Medium |
| Amiga | AMOS BASIC | AMOS Pro | FS-UAE | Manual | Medium |
| Amiga | 68000 ASM | vasm | FS-UAE | Manual | Hard |

---

## Common Anti-Patterns Across Platforms

### 1. Not Verifying Compilation

**Anti-pattern:** Skip compilation, assume code works
**Fix:** Always compile and test before creating lesson

### 2. Blank/Error Screenshots

**Anti-pattern:** Accept first screenshot without verification
**Fix:** Use READ tool to verify, check for errors/blank screens

### 3. Platform Feature Confusion

**Anti-pattern:** Use C64 memory addresses in ZX code
**Fix:** Use platform-specific validation

### 4. Missing Binary Files

**Anti-pattern:** Commit .bas/.asm but not compiled .prg/.tap/.nes
**Fix:** Always include compiled binaries in code-samples

### 5. Emulator-Specific Code

**Anti-pattern:** Code only works in specific emulator
**Fix:** Test on hardware-accurate emulator (x64sc, not x64)

---

## When to Expand Full Skills

**Expand to full skill when:**
- Creating first lesson for that platform
- Platform-specific issues discovered
- Semantic validator needed
- Complex platform requirements (NES mappers, Amiga copper)

**Current priority:**
1. ✅ C64 BASIC (complete - most used)
2. NES 6502 ASM (next priority - NES expansion planned)
3. ZX BASIC (ZX Spectrum Phase 0 active)
4. Others as needed

---

## Skill Expansion Template

When expanding specification to full skill:

1. Copy structure from `c64-lesson-creation/SKILL.md`
2. Replace platform-specific sections:
   - Language rules
   - Compilation commands
   - Memory map tables
   - Screenshot methods
   - Anti-patterns
3. Add platform-specific validation
4. Test with real lesson creation
5. Refine based on issues encountered

---

## The Bottom Line

**Platform-specific skills provide:**
- Exact compilation commands and flags
- Emulator-specific screenshot capture
- Memory map validation
- Platform anti-patterns
- Integration with generic validation skills

**C64 BASIC complete, others specified. Expand additional skills as platforms become active in curriculum.**

**Every platform has unique requirements - never assume cross-platform compatibility.**
