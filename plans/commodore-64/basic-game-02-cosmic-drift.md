# Cosmic Drift: 64-Unit Outline

**Game:** 2 - Cosmic Drift
**Platform:** Commodore 64
**Language:** BASIC V2
**Units:** 64 (4 phases)
**Prerequisite:** Number Hunter complete
**Concept:** Character-based animation with moving stars. First visual game introducing screen memory.

---

## Overview

Star Field creates a scrolling starfield effect using character graphics. Stars move across the screen creating the illusion of space travel. This game introduces direct memory access through POKE and the concept of screen memory.

---

## Learning Goals

By completing Cosmic Drift, learners will:

- Understand screen memory at $0400
- Use POKE to place characters on screen
- Understand colour memory at $D800
- Work with PETSCII character codes
- Create animation through character placement
- Manage multiple moving objects
- Implement timing with FOR/NEXT delays
- Control border and background colours

---

## Phase 1: Screen Memory Basics (Units 1-16)
*Understanding the C64 screen.*

### Units 1-4: Screen Memory
- **Unit 1:** Screen memory concept - 40×25 grid
- **Unit 2:** Memory address $0400 (1024 decimal)
- **Unit 3:** POKE to screen - placing a character
- **Unit 4:** Calculating screen positions

### Units 5-8: Character Codes
- **Unit 5:** PETSCII vs screen codes
- **Unit 6:** Common characters - letters, numbers
- **Unit 7:** Graphics characters - blocks, lines
- **Unit 8:** Star character - asterisk, custom choice

### Units 9-12: Colour Memory
- **Unit 9:** Colour memory at $D800 (55296 decimal)
- **Unit 10:** POKE to colour - changing character colour
- **Unit 11:** Colour values - 0-15
- **Unit 12:** Coloured stars - different brightnesses

### Units 13-16: First Star
- **Unit 13:** Placing a single star
- **Unit 14:** Star with colour
- **Unit 15:** Removing a star (space character)
- **Unit 16:** Phase 1 complete - static star placement

**Phase Goal:** Understand screen and colour memory.

---

## Phase 2: Movement and Animation (Units 17-32)
*Making stars move.*

### Units 17-20: Horizontal Movement
- **Unit 17:** Star position variable
- **Unit 18:** Clearing old position
- **Unit 19:** Drawing new position
- **Unit 20:** Animation loop - star moves left

### Units 21-24: Timing Control
- **Unit 21:** FOR/NEXT delay loops
- **Unit 22:** Speed control - delay length
- **Unit 23:** Consistent animation timing
- **Unit 24:** Smooth movement - appropriate delays

### Units 25-28: Screen Wrapping
- **Unit 25:** Edge detection - reaching screen boundary
- **Unit 26:** Wrap to right side
- **Unit 27:** Random vertical position on wrap
- **Unit 28:** Continuous star movement

### Units 29-32: Multiple Stars
- **Unit 29:** Array for star positions
- **Unit 30:** Initialising star array
- **Unit 31:** Moving multiple stars
- **Unit 32:** Phase 2 complete - animated starfield

**Phase Goal:** Multiple moving stars with wrapping.

---

## Phase 3: Visual Enhancement (Units 33-48)
*Creating depth and variety.*

### Units 33-36: Speed Layers
- **Unit 33:** Speed variable per star
- **Unit 34:** Fast stars - close objects
- **Unit 35:** Slow stars - distant objects
- **Unit 36:** Parallax illusion - depth effect

### Units 37-40: Colour Variety
- **Unit 37:** White stars - brightest
- **Unit 38:** Light grey stars - medium
- **Unit 39:** Dark grey stars - distant
- **Unit 40:** Speed-colour correlation

### Units 41-44: Screen Setup
- **Unit 41:** Border colour - POKE 53280
- **Unit 42:** Background colour - POKE 53281
- **Unit 43:** Black background for space
- **Unit 44:** Clean startup - clear screen first

### Units 45-48: Polish
- **Unit 45:** Star density - adjustable count
- **Unit 46:** Different star characters
- **Unit 47:** Title screen overlay
- **Unit 48:** Phase 3 complete - polished starfield

**Phase Goal:** Multi-layered parallax starfield.

---

## Phase 4: Interactivity (Units 49-64)
*Adding user control and game elements.*

### Units 49-52: Speed Control
- **Unit 49:** GET statement - keyboard polling
- **Unit 50:** Increase speed - key press
- **Unit 51:** Decrease speed - key press
- **Unit 52:** Speed display - on screen

### Units 53-56: Ship Addition
- **Unit 53:** Ship character - player vessel
- **Unit 54:** Ship position - centred
- **Unit 55:** Ship colour - distinct from stars
- **Unit 56:** Ship as focal point

### Units 57-60: Hyperdrive Effect
- **Unit 57:** Speed burst - all stars accelerate
- **Unit 58:** Speed lines - character trails
- **Unit 59:** Return to normal
- **Unit 60:** Hyperdrive sound (POKE 54296)

### Units 61-64: Final Demo
- **Unit 61:** All features integrated
- **Unit 62:** Attract mode - auto demonstration
- **Unit 63:** Code cleanup and documentation
- **Unit 64:** **RELEASE: Cosmic Drift complete**

**Phase Goal:** Interactive starfield demonstration.

---

## Summary

**Cosmic Drift** introduces visual programming concepts:

### Technical Specifications

- **Display:** Character mode (40×25)
- **Screen memory:** $0400 (1024)
- **Colour memory:** $D800 (55296)
- **Border/Background:** 53280/53281
- **Input:** Keyboard (GET)
- **Objects:** Up to 20 stars

### Skills Learned

- Direct memory access with POKE
- Screen memory calculation
- Colour memory manipulation
- Animation loops
- Multiple object management
- Timing control
- Array usage for object tracking

### Key Memory Locations Introduced

| Address | Purpose |
|---------|---------|
| 1024-2023 | Screen memory |
| 55296-56295 | Colour memory |
| 53280 | Border colour |
| 53281 | Background colour |

### Progression

This game prepares learners for **Catcher** where they'll add real-time keyboard input to control a player character catching falling objects.
