# MSX Assembly Curriculum

**Status:** Future — Stub Entry
**Priority:** Medium
**CPU:** Zilog Z80

---

## Why This Platform?

- Z80 skills transfer directly from Spectrum curriculum
- Standardised hardware across manufacturers
- Strong Japanese market presence (Konami, etc.)
- TMS9918 VDP is same family as ColecoVision/SMS
- MSX2 provides natural enhancement track

## Hardware Overview

| Component | Description |
|-----------|-------------|
| CPU | Zilog Z80A @ 3.58 MHz |
| Graphics | TMS9918A VDP (MSX1) / V9938 (MSX2) |
| Sound | AY-3-8910 (same as Spectrum 128K) |
| RAM | 8-64 KB (MSX1), 64-512 KB (MSX2) |
| Resolution | 256×192 (15 colours + transparency) |
| Sprites | 32 sprites, 4 per scanline |

## Enhancement Tracks

| Variant | Focus |
|---------|-------|
| MSX2 | V9938 VDP, 256 colours, vertical scroll |
| MSX2+ | V9958 VDP, hardware horizontal scroll |
| MSX turbo R | R800 CPU @ 7 MHz |

## Curriculum Approach (Proposed)

**Track:** Assembly (Z80)
**Games:** 4-8 (Tier 3 platform — smaller Western audience)
**Units per game:** 8, 16, or 32

Skills would build on Spectrum Z80 knowledge:
- TMS9918 VDP programming
- Sprite patterns and collision
- BIOS vs direct hardware access
- Slot/page memory system
- MSX2 enhancements

## Toolchain

| Tool | Purpose |
|------|---------|
| pasmo | Z80 assembler (same as Spectrum) |
| Glass | MSX-specific assembler |
| openMSX | Accurate emulator |
| blueMSX | Alternative emulator |

## Resources

- [MSX.org](https://www.msx.org/)
- [MSX Assembly Page](http://map.grauw.nl/)
- [TMS9918 Datasheet](https://www.cs.columbia.edu/~sedwards/papers/TMS9918.pdf)

---

*This is a stub entry for a future curriculum. Content will be developed when this platform is prioritised.*
