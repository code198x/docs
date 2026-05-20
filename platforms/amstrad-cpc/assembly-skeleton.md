# Amstrad CPC Assembly Curriculum

**Status:** Future — Stub Entry
**Priority:** Medium
**CPU:** Zilog Z80

---

## Why This Platform?

- Z80 skills transfer directly from ZX Spectrum curriculum
- Strong UK following with active community
- Unique gate array architecture worth understanding
- Locomotive BASIC provides excellent gateway track
- Different design philosophy from Spectrum (all-in-one vs expansion)

## Hardware Overview

| Component | Description |
|-----------|-------------|
| CPU | Zilog Z80A @ 4 MHz |
| Graphics | Gate Array + CRTC 6845 |
| Sound | AY-3-8912 (same as Spectrum 128K) |
| RAM | 64 KB (464), 128 KB (6128) |
| Modes | Mode 0 (16 colours), Mode 1 (4), Mode 2 (2) |
| Resolution | 160×200 to 640×200 |

## Enhancement Tracks

| Variant | Focus |
|---------|-------|
| CPC Plus | ASIC with hardware sprites, DMA, enhanced palette |
| GX4000 | Console variant of Plus hardware |

## Curriculum Approach (Proposed)

**Track:** Assembly (Z80)
**Games:** 8-16 (Tier 2 platform)
**Units per game:** 8, 16, or 32

Skills would build on Spectrum Z80 knowledge:
- Gate array programming (vs Spectrum ULA)
- CRTC tricks for smooth scrolling
- Hardware sprites (Plus only)
- Firmware vs direct hardware access
- Disk-based development workflow

## Toolchain

| Tool | Purpose |
|------|---------|
| pasmo | Z80 assembler (same as Spectrum) |
| RASM | CPC-optimised assembler |
| WinAPE | Emulator with debugging |
| Caprice32 | Lightweight emulator |

## Resources

- [CPCWiki](https://www.cpcwiki.eu/)
- [Amstrad CPC Firmware Guide](http://www.cantrell.org.uk/david/tech/cpc/cpc-firm/)
- [Gate Array Documentation](https://www.cpcwiki.eu/index.php/Gate_Array)

---

*This is a stub entry for a future curriculum. Content will be developed when this platform is prioritised.*
