# Sega Master System Assembly Curriculum

**Status:** Future — Stub Entry
**Priority:** Medium
**CPU:** Zilog Z80

---

## Why This Platform?

- Z80 skills transfer directly from Spectrum curriculum
- Simple VDP — good console entry point before Mega Drive
- Same sound chip as Spectrum 128K (SN76489)
- Gateway to Sega development (leads to Mega Drive)
- Underrated library with strong Brazilian following

## Hardware Overview

| Component | Description |
|-----------|-------------|
| CPU | Zilog Z80 @ 3.58 MHz |
| Graphics | VDP (315-5124) — TMS9918 derivative |
| Sound | SN76489 (4 channels, same as Spectrum 128K) |
| RAM | 8 KB |
| VRAM | 16 KB |
| Resolution | 256×192 or 256×224 |
| Sprites | 64 sprites, 8 per scanline |

## Enhancement Tracks

| Variant | Focus |
|---------|-------|
| Game Gear | Portable variant, higher colour depth |
| Mark III | Japanese variant with FM sound option |

## Curriculum Approach (Proposed)

**Track:** Assembly (Z80)
**Games:** 4-8 (Tier 2-3 platform)
**Units per game:** 8, 16, or 32

Skills would build on Spectrum Z80 knowledge:
- VDP tile and sprite management
- Palette manipulation
- Horizontal/vertical interrupts
- Bank switching via mapper
- SN76489 sound (familiar from Spectrum)

## Toolchain

| Tool | Purpose |
|------|---------|
| WLA-DX | Multi-platform assembler with SMS support |
| pasmo | Z80 assembler |
| Emulicious | Debugging emulator |
| Meka | Feature-rich emulator |

## Resources

- [SMS Power](https://www.smspower.org/)
- [devkitSMS](https://github.com/sverx/devkitSMS)
- [SMS VDP Documentation](https://www.smspower.org/Development/VDPRegisters)

---

*This is a stub entry for a future curriculum. Content will be developed when this platform is prioritised.*
