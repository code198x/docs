# Highway AGA: 32-Unit Outline

**Game:** 12 AGA Enhancement
**Platform:** Commodore Amiga (A1200/A4000)
**Language:** 68000 Assembly
**Units:** 32 (2 phases)
**Prerequisite:** Highway (OCS) complete
**Concept:** AGA-enhanced pseudo-3D racer with smoother road rendering.

---

## Overview

Highway AGA transforms the racing experience. The Copper road tricks that defined OCS racing games give way to smooth 256-colour gradients. The road, sky, and scenery all benefit from the expanded palette.

Commercial example: Lotus III had notable visual differences between OCS and AGA.

---

## AGA Enhancements

| Feature | OCS Version | AGA Version |
|---------|-------------|-------------|
| Road colours | Copper tricks | True gradients |
| Sky gradient | ~16 colours | 256 colours |
| Sprite scaling | Limited | More sizes |
| Horizon | Banded | Smooth |

---

## Phase 1: Road and Sky (Units 1-16)
*Core visual upgrade.*

### Units 1-4: Road Rendering
- **Unit 1:** AGA road approach - no Copper needed
- **Unit 2:** Road gradient - smooth colour bands
- **Unit 3:** Road markings - enhanced detail
- **Unit 4:** Rumble strips - more colours

### Units 5-8: Sky and Horizon
- **Unit 5:** Sky gradient - 256 colours smooth
- **Unit 6:** Horizon blend - road meets sky
- **Unit 7:** Mountain silhouettes - detailed
- **Unit 8:** Cloud layers - enhanced depth

### Units 9-12: Environment Themes
- **Unit 9:** Coastal track - blue gradients
- **Unit 10:** Forest track - green richness
- **Unit 11:** Mountain track - purple/orange
- **Unit 12:** Night track - dark gradients

### Units 13-16: Display Setup
- **Unit 13:** Per-line colour - AGA method
- **Unit 14:** Bitplane setup - road display
- **Unit 15:** Scroll coordination - layers
- **Unit 16:** Core conversion complete

**Phase Goal:** Racer running in AGA.

---

## Phase 2: Sprites and Effects (Units 17-32)
*Enhanced objects and atmosphere.*

### Units 17-20: Vehicle Sprites
- **Unit 17:** Player car - more detail
- **Unit 18:** Traffic cars - variety, colours
- **Unit 19:** Sprite scaling - more size steps
- **Unit 20:** Sprite shading - depth cues

### Units 21-24: Roadside Objects
- **Unit 21:** Trees - richer foliage
- **Unit 22:** Buildings - detailed
- **Unit 23:** Signs - readable, colourful
- **Unit 24:** Trackside variety - enhanced

### Units 25-28: Atmospheric Effects
- **Unit 25:** Heat haze - colour shimmer
- **Unit 26:** Rain effect - enhanced drops
- **Unit 27:** Sunset transitions - smooth
- **Unit 28:** Tunnel lighting - dramatic

### Units 29-32: Release
- **Unit 29:** All tracks testing
- **Unit 30:** Split-screen testing - AGA
- **Unit 31:** Final polish
- **Unit 32:** Release build - AGA ADF

**Phase Goal:** Complete AGA racer.

---

## Summary

**Highway AGA** demonstrates pseudo-3D enhancement.

### Technical Specifications

- **Display:** 256-colour road rendering
- **Gradients:** True colour, no Copper tricks
- **Tracks:** 3 with unique palettes
- **Scaling:** Enhanced sprite sizes
- **Modes:** Time trial, versus, championship
- **Target:** A1200, A4000
- **Distribution:** Separate AGA ADF

### Skills Learned

- AGA road rendering techniques
- Gradient without Copper
- Enhanced sprite scaling
- Atmospheric colour effects
