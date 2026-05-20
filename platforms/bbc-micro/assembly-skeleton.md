# BBC Micro Assembly Curriculum

**Status:** Future — Stub Entry
**Priority:** High
**CPU:** MOS 6502

---

## Why This Platform?

- 6502 skills transfer directly from C64 curriculum
- British educational heritage — the machine that taught a generation
- Exceptional BASIC (BBC BASIC) provides strong gateway track
- Clean, well-documented architecture
- Active preservation and homebrew community

## Hardware Overview

| Component | Description |
|-----------|-------------|
| CPU | MOS 6502A @ 2 MHz |
| Graphics | Motorola 6845 CRTC + ULA |
| Sound | Texas Instruments SN76489 (4 channels) |
| RAM | 32 KB (Model B) |
| Modes | 8 display modes (2-8 colours, various resolutions) |

## Enhancement Tracks

| Variant | Focus |
|---------|-------|
| Master | 128 KB RAM, improved BASIC, shadow RAM |
| Archimedes | ARM processor (separate curriculum track) |

## Curriculum Approach (Proposed)

**Track:** Assembly (6502)
**Games:** 8-16 (Tier 2 platform)
**Units per game:** 8, 16, or 32

Skills would build on C64 6502 knowledge:
- Mode 7 teletext graphics (unique to BBC)
- CRTC programming for display tricks
- SN76489 sound (same chip as Master System)
- Paged ROM system
- Second processor support

## Toolchain

| Tool | Purpose |
|------|---------|
| BeebAsm | BBC Micro-specific assembler |
| ACME | Generic 6502 assembler |
| BeebEm | Accurate emulator |
| b2 | Modern emulator with debugging |

## Resources

- [BBC Micro User Guide](http://www.bbcbasic.co.uk/bbcbasic/manual/)
- [Advanced User Guide](http://www.8bs.com/othrdnld/manuals/AUG.pdf)
- [Stardot Forums](https://stardot.org.uk/forums/)

---

*This is a stub entry for a future curriculum. Content will be developed when this platform is prioritised.*
