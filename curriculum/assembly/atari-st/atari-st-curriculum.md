# Atari ST Assembly Curriculum

**Status:** Future — Stub Entry
**Priority:** High
**CPU:** Motorola 68000

---

## Why This Platform?

- 68000 skills transfer directly from Amiga curriculum
- Clean architecture — no custom chips to learn
- MIDI standard made it dominant in music production
- Strong demoscene heritage
- Direct comparison with Amiga teaches hardware design philosophy

## Hardware Overview

| Component | Description |
|-----------|-------------|
| CPU | Motorola 68000 @ 8 MHz |
| Graphics | Shifter chip (simple framebuffer) |
| Sound | Yamaha YM2149 (PSG, same as Spectrum 128K) |
| RAM | 512 KB - 4 MB |
| Resolution | 320×200 (16 colours), 640×200 (4 colours), 640×400 (mono) |

## Enhancement Tracks

| Variant | Focus |
|---------|-------|
| STE | Blitter, DMA sound, hardware scrolling, 4096 colours |
| Falcon | 68030, DSP, true colour, professional audio |

## Curriculum Approach (Proposed)

**Track:** Assembly (68000)
**Games:** 8-16 (Tier 2 platform)
**Units per game:** 8, 16, or 32

Skills would build on 68000 knowledge with different focus:
- Framebuffer graphics (vs Amiga playfields)
- Shifter timing tricks
- YM2149 sound programming
- GEM operating system interaction
- STE enhancements (blitter, DMA sound)

## Toolchain

| Tool | Purpose |
|------|---------|
| vasm | 68000 assembler (same as Amiga) |
| Hatari | Accurate ST/STE/Falcon emulator |
| Steem | Fast ST emulator |

## Resources

- [Atari ST Internals](https://info-coach.fr/atari/documents/books.php)
- [YM2149 Datasheet](https://www.ym2149.com/)
- [Demoscene resources](https://demozoo.org/platforms/14/)

---

*This is a stub entry for a future curriculum. Content will be developed when this platform is prioritised.*
