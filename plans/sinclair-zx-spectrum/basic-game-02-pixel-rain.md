# Pixel Rain: 64-Unit Outline

**Game:** 2 - Pixel Rain
**Platform:** Sinclair ZX Spectrum
**Language:** Sinclair BASIC
**Units:** 64 (4 phases)
**Prerequisite:** Guess Quest complete
**Concept:** Falling pixels creating patterns. First visual game using PLOT command.

---

## Overview

Pixel Rain creates mesmerising visual patterns as coloured pixels fall from the top of the screen. This game introduces the Spectrum's high-resolution graphics capabilities through the PLOT command and demonstrates animation through pixel manipulation.

---

## Learning Goals

By completing Pixel Rain, learners will:

- Understand screen coordinates (0-255 × 0-175)
- Use PLOT command for pixel placement
- Apply INK colours to graphics
- Create animation through plotting
- Manage multiple falling objects
- Implement timing control
- Understand attribute cells
- Control visual patterns

---

## Phase 1: PLOT Basics (Units 1-16)
*First pixels on screen.*

### Units 1-4: Screen Coordinates
- **Unit 1:** Screen resolution - 256×176 pixels
- **Unit 2:** Coordinate system - origin at bottom-left
- **Unit 3:** X coordinates - 0 to 255
- **Unit 4:** Y coordinates - 0 to 175

### Units 5-8: PLOT Command
- **Unit 5:** PLOT x,y - placing a single pixel
- **Unit 6:** Multiple PLOTs - several pixels
- **Unit 7:** Plotting in loops
- **Unit 8:** Patterns with PLOT

### Units 9-12: Colour with INK
- **Unit 9:** INK before PLOT - pixel colour
- **Unit 10:** Colour values - 0 to 7
- **Unit 11:** Colour variety in patterns
- **Unit 12:** Understanding attribute cells (8×8)

### Units 13-16: First Animation
- **Unit 13:** PLOT followed by PLOT INVERSE
- **Unit 14:** Moving a pixel down the screen
- **Unit 15:** Timing with FOR/NEXT delays
- **Unit 16:** Phase 1 complete - animated pixel

**Phase Goal:** Basic pixel plotting with colour.

---

## Phase 2: Falling Pixels (Units 17-32)
*Creating the rain effect.*

### Units 17-20: Single Raindrop
- **Unit 17:** Starting at top (Y=175)
- **Unit 18:** Falling animation - Y decreasing
- **Unit 19:** Reaching bottom - reset to top
- **Unit 20:** Random X position on reset

### Units 21-24: Multiple Raindrops
- **Unit 21:** Arrays for raindrop X positions
- **Unit 22:** Arrays for raindrop Y positions
- **Unit 23:** Initialising multiple drops
- **Unit 24:** Updating all drops each frame

### Units 25-28: Visual Variety
- **Unit 25:** Different fall speeds
- **Unit 26:** Speed arrays per drop
- **Unit 27:** Colour variety - INK per drop
- **Unit 28:** Depth illusion - speed correlates with colour

### Units 29-32: Continuous Rain
- **Unit 29:** Screen clearing strategies
- **Unit 30:** Clearing old positions
- **Unit 31:** Smooth animation loop
- **Unit 32:** Phase 2 complete - rain effect working

**Phase Goal:** Multiple falling pixels with variety.

---

## Phase 3: Patterns and Effects (Units 33-48)
*Making it visually interesting.*

### Units 33-36: Accumulation
- **Unit 33:** Pixels staying at bottom
- **Unit 34:** Building up - snow effect
- **Unit 35:** Height tracking per column
- **Unit 36:** Full screen = reset

### Units 37-40: Pattern Modes
- **Unit 37:** Mode 1: Standard rain
- **Unit 38:** Mode 2: Accumulating snow
- **Unit 39:** Mode 3: Colour waves
- **Unit 40:** Mode selection menu

### Units 41-44: DRAW Command
- **Unit 41:** DRAW introduction - lines
- **Unit 42:** DRAW dx,dy - relative drawing
- **Unit 43:** Trail effects with DRAW
- **Unit 44:** Combining PLOT and DRAW

### Units 45-48: Interactive Elements
- **Unit 45:** INKEY$ - keyboard polling
- **Unit 46:** Increase/decrease density
- **Unit 47:** Change colour scheme
- **Unit 48:** Phase 3 complete - pattern modes

**Phase Goal:** Multiple visual modes with interaction.

---

## Phase 4: Polish and Performance (Units 49-64)
*Refining the experience.*

### Units 49-52: Performance Tuning
- **Unit 49:** Counting drops - performance impact
- **Unit 50:** Optimising the main loop
- **Unit 51:** Finding the sweet spot
- **Unit 52:** BASIC speed limits observed

### Units 53-56: Visual Polish
- **Unit 53:** Border colour coordination
- **Unit 54:** Background colour per mode
- **Unit 55:** Smooth transitions between modes
- **Unit 56:** Title screen with graphics

### Units 57-60: Special Effects
- **Unit 57:** CIRCLE command introduction
- **Unit 58:** Splash effects at bottom
- **Unit 59:** Wind effect - X drift
- **Unit 60:** Combined effects

### Units 61-64: Final Demo
- **Unit 61:** All modes integrated
- **Unit 62:** Attract mode - auto demonstration
- **Unit 63:** Code cleanup
- **Unit 64:** **RELEASE: Pixel Rain complete**

**Phase Goal:** Polished visual demonstration.

---

## Summary

**Pixel Rain** introduces Spectrum graphics:

### Technical Specifications

- **Display:** High-resolution (256×176)
- **Graphics:** PLOT, DRAW, CIRCLE
- **Colour:** INK with attribute system
- **Objects:** 20-40 raindrops typical
- **Modes:** Rain, snow, colour waves

### Skills Learned

- Screen coordinate system
- PLOT command usage
- Array-based object management
- Animation timing
- DRAW for lines
- CIRCLE for curves
- Attribute cell awareness
- Performance observation

### Attribute System Introduction

| Concept | Detail |
|---------|--------|
| Cell size | 8×8 pixels |
| INK | Foreground colour (0-7) |
| PAPER | Background colour (0-7) |
| Limitation | One INK/PAPER per cell |

### Progression

This game prepares learners for **Paddle Battle** where they'll add real-time keyboard input to control game objects with INKEY$.
