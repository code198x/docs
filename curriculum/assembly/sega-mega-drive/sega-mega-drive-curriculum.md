# Sega Mega Drive / Genesis Assembly Curriculum

**Status:** Future — Stub Entry
**Priority:** High
**CPU:** Motorola 68000 (+ Z80 for sound)

---

## Why This Platform?

- 68000 skills transfer directly from Amiga curriculum
- Different hardware philosophy (VDP vs custom chipset)
- Massive library and strong nostalgia factor
- Active homebrew community
- "Blast Processing" — understanding what it actually meant

## Hardware Overview

| Component | Description |
|-----------|-------------|
| Main CPU | Motorola 68000 @ 7.67 MHz |
| Sound CPU | Zilog Z80 @ 3.58 MHz |
| Graphics | Yamaha VDP (315-5313) |
| Sound | Yamaha YM2612 (FM) + SN76489 (PSG) |
| RAM | 64 KB main + 8 KB sound |
| VRAM | 64 KB |

## Enhancement Tracks

| Variant | Focus |
|---------|-------|
| Mega CD | CD audio, scaling/rotation hardware, extra RAM |
| 32X | Additional SH-2 processors, 32-bit graphics |

## Curriculum Approach (Proposed)

**Track:** Assembly (68000)
**Games:** 8-16 (Tier 2 platform)
**Units per game:** 8, 16, or 32

Skills would build on Amiga 68000 knowledge:
- VDP programming vs Amiga custom chips
- Tile-based graphics (different from Amiga bitplanes)
- Z80 coprocessor for sound
- YM2612 FM synthesis
- Cartridge ROM banking

## Toolchain

| Tool | Purpose |
|------|---------|
| vasm | 68000 assembler (same as Amiga) |
| SGDK | C development kit (reference) |
| Gens/Kega Fusion | Emulators |
| BlastEm | Accuracy-focused emulator |

## Resources

- [Mega Drive Technical Manual](https://segaretro.org/Mega_Drive)
- [68000 Programmer's Reference](https://www.nxp.com/docs/en/reference-manual/M68000PRM.pdf)
- [YM2612 Documentation](https://www.smspower.org/maxim/Documents/YM2612)

---

*This is a stub entry for a future curriculum. Content will be developed when this platform is prioritised.*
