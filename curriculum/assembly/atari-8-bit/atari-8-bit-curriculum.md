# Atari 8-bit Assembly Curriculum

**Status:** Future — Stub Entry
**Priority:** Medium
**CPU:** MOS 6502

---

## Why This Platform?

- 6502 skills transfer directly from C64/NES curriculum
- ANTIC and GTIA are fascinating custom chips
- POKEY sound is distinctive and educational
- Historical importance — predates C64
- Display list concept influenced later hardware

## Hardware Overview

| Component | Description |
|-----------|-------------|
| CPU | MOS 6502 @ 1.79 MHz |
| Graphics | ANTIC (display list) + GTIA (colours/players) |
| Sound | POKEY (4 channels + I/O) |
| RAM | 16 KB (400) to 64 KB (XL/XE) |
| Resolution | Multiple modes via display lists |
| Sprites | 4 "player" objects + 4 "missiles" |

## Key Features

- **Display Lists:** CPU-controlled graphics modes per scanline
- **Player/Missile Graphics:** Hardware sprites (different from C64)
- **POKEY:** Combined sound + keyboard + serial I/O
- **Artifacting:** NTSC colour tricks for extra colours

## Curriculum Approach (Proposed)

**Track:** Assembly (6502)
**Games:** 8-16 (Tier 2 platform)
**Units per game:** 8, 16, or 32

Skills would build on 6502 knowledge:
- ANTIC display list programming
- GTIA colour modes and tricks
- Player/missile positioning and collision
- POKEY sound and distortion
- DLI (Display List Interrupts)

## Toolchain

| Tool | Purpose |
|------|---------|
| MADS | Atari-specific assembler |
| ACME | Generic 6502 assembler |
| Altirra | Accurate emulator with debugging |
| Atari800 | Portable emulator |

## Resources

- [Atari 8-bit FAQ](https://www.faqs.org/faqs/atari-8-bit/faq/)
- [Mapping the Atari](https://www.atariarchives.org/mapping/)
- [De Re Atari](https://www.atariarchives.org/dere/)

---

*This is a stub entry for a future curriculum. Content will be developed when this platform is prioritised.*
