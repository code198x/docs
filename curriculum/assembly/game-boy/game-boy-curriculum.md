# Game Boy Assembly Curriculum

**Status:** Future — Stub Entry
**Priority:** Medium
**CPU:** Sharp SM83 (Z80 variant)

---

## Why This Platform?

- Z80-like CPU — skills transfer from Spectrum curriculum
- Handheld constraints teach optimisation discipline
- Massive nostalgia factor (118 million units sold)
- Active homebrew scene with modern tooling
- Simple enough for focused curriculum, complex enough to be interesting

## Hardware Overview

| Component | Description |
|-----------|-------------|
| CPU | Sharp SM83 @ 4.19 MHz (Z80 subset + extras) |
| Graphics | Custom PPU, tile-based |
| Sound | 4 channels (2 pulse, 1 wave, 1 noise) |
| RAM | 8 KB |
| VRAM | 8 KB |
| Resolution | 160×144, 4 shades of green |
| Sprites | 40 sprites, 10 per scanline |

## Enhancement Tracks

| Variant | Focus |
|---------|-------|
| Game Boy Color | 32 KB RAM, 56 colours on screen, double speed |
| Game Boy Advance | ARM7TDMI (separate curriculum track) |

## Curriculum Approach (Proposed)

**Track:** Assembly (SM83/Z80-like)
**Games:** 8-16 (Tier 2 platform)
**Units per game:** 8, 16, or 32

Would teach Z80 variant with Game Boy specifics:
- SM83 differences from standard Z80
- Tile and sprite management
- Memory banking (MBC chips)
- Sound channel programming
- Serial link for multiplayer
- GBC colour extensions

## Toolchain

| Tool | Purpose |
|------|---------|
| RGBDS | Standard Game Boy assembler |
| GBDK | C development kit (reference) |
| BGB | Debugging emulator |
| SameBoy | Accuracy-focused emulator |

## Unique Constraints

- 10 sprites per scanline limit
- 8 KB RAM requires careful management
- No multiplication/division instructions
- Battery-backed SRAM for saves

## Resources

- [Pan Docs](https://gbdev.io/pandocs/)
- [GB Dev Community](https://gbdev.io/)
- [awesome-gbdev](https://github.com/gbdev/awesome-gbdev)

---

*This is a stub entry for a future curriculum. Content will be developed when this platform is prioritised.*
