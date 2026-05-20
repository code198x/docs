# Super Nintendo (SNES) Assembly Curriculum

**Status:** Future — Stub Entry
**Priority:** Medium
**CPU:** WDC 65816

---

## Why This Platform?

- 65816 is a 16-bit extension of 6502 — skills transfer from C64/NES
- Mode 7 is legendary and worth understanding
- Complex but rewarding hardware
- Iconic library with strong nostalgia
- Active ROM hacking and homebrew community

## Hardware Overview

| Component | Description |
|-----------|-------------|
| CPU | WDC 65816 @ 3.58 MHz |
| Graphics | PPU (2 chips) with 8 modes |
| Sound | Sony SPC700 + DSP (8 channels, samples) |
| RAM | 128 KB main |
| VRAM | 64 KB |
| Sprites | 128 sprites, 32 per scanline |

## Key Features

- **Mode 7:** Rotation, scaling, perspective effects
- **HDMA:** Scanline-by-scanline register changes
- **Enhancement chips:** SuperFX, SA-1, DSP-1, etc.
- **Sample-based audio:** CD-quality potential

## Curriculum Approach (Proposed)

**Track:** Assembly (65816)
**Games:** 8-16 (Tier 2 platform)
**Units per game:** 8, 16, or 32

Would require teaching 65816 extensions:
- 16-bit accumulator and index registers
- Bank switching (24-bit address space)
- Direct page relocation
- PPU programming (more complex than NES)
- SPC700 sound programming
- Mode 7 mathematics

## Toolchain

| Tool | Purpose |
|------|---------|
| ca65 | 65816 assembler (same as NES toolchain) |
| bass | Modern 65816 assembler |
| bsnes/higan | Accuracy-focused emulator |
| Mesen-S | Debugging-friendly emulator |

## Challenges

- More complex than NES — may need 32-unit games
- SPC700 is a separate processor requiring its own lessons
- Mode 7 requires trigonometry understanding

## Resources

- [SNES Development Wiki](https://snes.nesdev.org/)
- [65816 Programming Manual](https://www.westerndesigncenter.com/wdc/documentation/w65c816s.pdf)
- [Anomie's SNES Docs](https://www.romhacking.net/documents/226/)

---

*This is a stub entry for a future curriculum. Content will be developed when this platform is prioritised.*
