# TurboGrafx-16 / PC Engine Assembly Curriculum

**Status:** Future — Stub Entry
**Priority:** Medium
**CPU:** Hudson HuC6280 (65C02 derivative)

---

## Why This Platform?

- 6502-family CPU — skills transfer from C64/NES
- Impressive sprite capabilities (64 sprites, 16 per line)
- Tile-based but with larger sprite counts than contemporaries
- CD-ROM² enhancement track offers expanded possibilities
- Unique position between 8-bit and 16-bit eras

## Hardware Overview

| Component | Description |
|-----------|-------------|
| CPU | HuC6280 @ 7.16 MHz (65C02 + extras) |
| Graphics | HuC6270 VDC |
| Sound | HuC6280 PSG (6 channels, wavetable) |
| RAM | 8 KB |
| VRAM | 64 KB |
| Resolution | 256×224 to 512×224 |
| Sprites | 64 sprites, 16 per scanline |

## Enhancement Tracks

| Variant | Focus |
|---------|-------|
| CD-ROM² | CD audio, extra RAM (64 KB + 256 KB) |
| Super CD-ROM² | 2 MB RAM |
| Arcade Card | 2 MB additional RAM |

## Curriculum Approach (Proposed)

**Track:** Assembly (HuC6280/6502-family)
**Games:** 4-8 (Tier 3 platform)
**Units per game:** 8, 16, or 32

Skills would build on 6502 knowledge:
- HuC6280 extensions (block moves, etc.)
- VDC sprite and background management
- Wavetable sound programming
- Memory bank switching
- CD-ROM integration

## Toolchain

| Tool | Purpose |
|------|---------|
| HuC | C compiler with inline assembly |
| PCEAS | PC Engine assembler |
| Mednafen | Accurate emulator |
| Ootake | Alternative emulator |

## Resources

- [PC Engine Dev](https://www.pcedev.net/)
- [MagicKit Documentation](https://github.com/pce-devel/huc)
- [Mednafen PCE Documentation](https://mednafen.github.io/documentation/pce.html)

---

*This is a stub entry for a future curriculum. Content will be developed when this platform is prioritised.*
