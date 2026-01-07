# Parallax AGA: 32-Unit Outline

**Game:** 9 AGA Enhancement
**Platform:** Commodore Amiga (A1200/A4000)
**Language:** 68000 Assembly
**Units:** 32 (2 phases)
**Prerequisite:** Parallax (OCS) complete
**Concept:** AGA-enhanced horizontal parallax shooter with 256-colour graphics.

---

## Overview

Parallax AGA transforms the OCS shooter into an AGA showcase. The same gameplay, but with the visual fidelity that A1200/A4000 owners expected from dedicated AGA releases.

Commercial examples: Alien Breed AGA, Project X AGA, Zool AGA.

---

## AGA Enhancements

| Feature | OCS Version | AGA Version |
|---------|-------------|-------------|
| Colours | 32 on-screen | 256 on-screen |
| Palette | 4,096 colours | 16.7 million |
| Gradients | Copper tricks | True gradients |
| Sprites | 3 colours + trans | More colours |
| Bitplanes | 5 | 8 |

---

## Phase 1: AGA Display Setup (Units 1-16)
*Converting display to AGA modes.*

### Units 1-4: AGA Fundamentals
- **Unit 1:** AGA chipset overview - Lisa, Alice
- **Unit 2:** AGA registers - differences from OCS
- **Unit 3:** 256-colour mode setup - 8 bitplanes
- **Unit 4:** 24-bit palette - RGB8 format

### Units 5-8: Parallax Conversion
- **Unit 5:** Background layer - 256 colours
- **Unit 6:** Foreground layer - enhanced palette
- **Unit 7:** Dual playfield in AGA - considerations
- **Unit 8:** Scroll register differences

### Units 9-12: Enhanced Graphics
- **Unit 9:** Background art - richer gradients
- **Unit 10:** Foreground art - more detail
- **Unit 11:** Enemy sprites - enhanced colours
- **Unit 12:** Player ship - upgraded graphics

### Units 13-16: Palette Management
- **Unit 13:** 256-colour palette design
- **Unit 14:** Palette allocation - layers, sprites
- **Unit 15:** Copper palette in AGA - faster
- **Unit 16:** Display conversion complete

**Phase Goal:** Game running in AGA 256-colour mode.

---

## Phase 2: Enhanced Effects (Units 17-32)
*Visual polish and optimisation.*

### Units 17-20: Enhanced Gradients
- **Unit 17:** Sky gradients - smooth 256-colour
- **Unit 18:** Water effects - more colours
- **Unit 19:** Sunset/atmosphere - rich palettes
- **Unit 20:** No Copper tricks needed - direct colour

### Units 21-24: Sprite Enhancements
- **Unit 21:** Explosion effects - more frames, colours
- **Unit 22:** Power-up effects - enhanced glow
- **Unit 23:** Boss sprites - larger, detailed
- **Unit 24:** Bullet sprites - variety

### Units 25-28: Performance
- **Unit 25:** AGA bandwidth - considerations
- **Unit 26:** Blitter in AGA - same but more data
- **Unit 27:** Frame rate maintenance - 50fps
- **Unit 28:** Memory usage - 2MB chip RAM

### Units 29-32: Release
- **Unit 29:** A1200 testing - base AGA
- **Unit 30:** A4000 testing - fast RAM
- **Unit 31:** Final polish
- **Unit 32:** Release build - AGA ADF

**Phase Goal:** Complete AGA shooter.

---

## Summary

**Parallax AGA** teaches AGA fundamentals through enhancement.

### Technical Specifications

- **Display:** 256 colours, 320×256
- **Palette:** Full 24-bit RGB
- **Gradients:** True colour, no Copper needed
- **Target:** A1200, A4000
- **RAM:** 2MB chip RAM
- **Distribution:** Separate AGA ADF

### Skills Learned

- AGA register programming
- 256-colour mode setup
- 24-bit palette management
- AGA display considerations
- OCS to AGA conversion process
