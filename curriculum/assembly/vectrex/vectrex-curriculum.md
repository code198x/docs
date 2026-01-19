# Vectrex Assembly Curriculum

**Status:** Future — Stub Entry
**Priority:** Medium
**CPU:** Motorola 6809

---

## Why This Platform?

- Unique vector display — unlike any other platform
- 6809 is a sophisticated 8-bit CPU worth learning
- Teaches fundamentally different graphics concepts
- Small but dedicated homebrew community
- Only vector-based home console

## Hardware Overview

| Component | Description |
|-----------|-------------|
| CPU | Motorola 6809 @ 1.5 MHz |
| Graphics | Vector CRT (built-in display) |
| Sound | AY-3-8912 (same as CPC/Spectrum 128K) |
| RAM | 1 KB |
| ROM | 8 KB BIOS + cartridge |
| Display | 9" vector monitor, monochrome |

## Key Features

- **Vector graphics:** Lines drawn directly, no pixels
- **Built-in display:** Unique among consoles
- **Analog controller:** Precise input
- **Overlays:** Colour added via screen overlays
- **6809:** More powerful than 6502 (16-bit operations)

## Curriculum Approach (Proposed)

**Track:** Assembly (6809)
**Games:** 4 (Tier 3 platform — specialist interest)
**Units per game:** 8 or 16

Would teach unique concepts:
- 6809 architecture (new CPU family)
- Vector drawing routines
- Beam positioning and timing
- Intensity control for brightness
- BIOS usage vs direct hardware

## Toolchain

| Tool | Purpose |
|------|---------|
| AS09 | 6809 assembler |
| lwtools | Modern 6809 toolchain |
| ParaJVE | Java-based emulator |
| MAME | Accurate emulation |

## Unique Challenges

- No pixels — completely different mindset
- 1 KB RAM is extremely constraining
- Vector math required for rotations
- Small community means fewer resources

## Resources

- [Vectrex Programming](http://www.playvectrex.com/designit/chrissalo/)
- [Vectrex Wiki](https://vectopia.org/)
- [6809 Assembly Guide](http://www.maddes.net/m6809pm/)

---

*This is a stub entry for a future curriculum. Content will be developed when this platform is prioritised.*
