# Snake Spectrum: 64-Unit Outline

**Game:** 5 - Snake Spectrum
**Platform:** Sinclair ZX Spectrum
**Language:** Sinclair BASIC
**Units:** 64 (4 phases)
**Prerequisite:** Dungeon Explorer complete
**Concept:** Classic snake game with User-Defined Graphics (UDGs).

---

## Overview

Snake Spectrum is the classic snake game where players guide a growing snake to eat food while avoiding collisions with walls and their own body. This game introduces User-Defined Graphics (UDGs) for custom character designs and array-based body tracking.

---

## Learning Goals

By completing Snake Spectrum, learners will:

- Create User-Defined Graphics (UDGs)
- Design custom character shapes
- Use POKE to define UDG data
- Implement arrays for body tracking
- Build self-collision detection
- Create food spawning mechanics
- Implement growth and scoring
- Manage speed progression

---

## Phase 1: UDG Fundamentals (Units 1-16)
*Creating custom graphics.*

### Units 1-4: UDG Introduction
- **Unit 1:** UDG concept - user-defined characters
- **Unit 2:** UDG memory location - USR "a"
- **Unit 3:** 8×8 pixel grid per character
- **Unit 4:** Available UDGs - A to U

### Units 5-8: UDG Design
- **Unit 5:** Graph paper design - 8×8 grid
- **Unit 6:** Binary to decimal conversion
- **Unit 7:** DATA for UDG definition
- **Unit 8:** POKE to UDG memory

### Units 9-12: Snake Characters
- **Unit 9:** Snake head design
- **Unit 10:** Snake body segment design
- **Unit 11:** Food item design
- **Unit 12:** Defining all UDGs

### Units 13-16: Displaying UDGs
- **Unit 13:** PRINT CHR$ for UDGs
- **Unit 14:** PRINT AT with UDGs
- **Unit 15:** Coloured UDGs - INK
- **Unit 16:** Phase 1 complete - custom graphics working

**Phase Goal:** Custom snake characters defined and displayed.

---

## Phase 2: Snake Movement (Units 17-32)
*Getting the snake moving.*

### Units 17-20: Head Movement
- **Unit 17:** Head position variables
- **Unit 18:** Direction variable - up/down/left/right
- **Unit 19:** Direction change with INKEY$
- **Unit 20:** Moving head in direction

### Units 21-24: Timed Movement
- **Unit 21:** System timer - PEEK(23672-23674)
- **Unit 22:** Frame timing - move every N ticks
- **Unit 23:** Consistent speed control
- **Unit 24:** Smooth snake movement

### Units 25-28: Body Tracking
- **Unit 25:** Body arrays - X and Y positions
- **Unit 26:** Body length variable
- **Unit 27:** Head becomes body - trail
- **Unit 28:** Removing tail - last segment

### Units 29-32: Body Display
- **Unit 29:** Drawing body segments
- **Unit 30:** Different UDG for body vs head
- **Unit 31:** Erasing old tail position
- **Unit 32:** Phase 2 complete - moving snake with body

**Phase Goal:** Complete moving snake with trailing body.

---

## Phase 3: Food and Growth (Units 33-48)
*Eating to survive.*

### Units 33-36: Food Spawning
- **Unit 33:** Food position variables
- **Unit 34:** Random placement
- **Unit 35:** Avoid spawning on snake
- **Unit 36:** Drawing food UDG

### Units 37-40: Eating Mechanics
- **Unit 37:** Head meets food detection
- **Unit 38:** Increment length
- **Unit 39:** Don't remove tail - growth
- **Unit 40:** Spawn new food

### Units 41-44: Self-Collision
- **Unit 41:** Check head against body array
- **Unit 42:** Loop through all segments
- **Unit 43:** Collision = game over
- **Unit 44:** Wall collision - boundaries

### Units 45-48: Scoring
- **Unit 45:** Points per food eaten
- **Unit 46:** Score display on screen
- **Unit 47:** High score tracking
- **Unit 48:** Phase 3 complete - playable snake game

**Phase Goal:** Complete snake game with food and scoring.

---

## Phase 4: Polish and Features (Units 49-64)
*Refining the experience.*

### Units 49-52: Speed Progression
- **Unit 49:** Speed variable
- **Unit 50:** Faster as snake grows
- **Unit 51:** Speed cap - maximum difficulty
- **Unit 52:** Speed display

### Units 53-56: Visual Polish
- **Unit 53:** Title screen with UDG art
- **Unit 54:** Border colour changes
- **Unit 55:** Death animation
- **Unit 56:** Game over screen

### Units 57-60: Game Options
- **Unit 57:** Difficulty settings - starting speed
- **Unit 58:** Wall mode - wraparound vs death
- **Unit 59:** Starting length option
- **Unit 60:** Menu implementation

### Units 61-64: Final Game
- **Unit 61:** All features integrated
- **Unit 62:** Balanced difficulty
- **Unit 63:** Code cleanup
- **Unit 64:** **RELEASE: Snake Spectrum complete**

**Phase Goal:** Polished snake game with options.

---

## Summary

**Snake Spectrum** demonstrates UDG programming:

### Technical Specifications

- **Display:** Character mode with UDGs
- **Characters:** Custom head, body, food
- **Input:** Four-direction INKEY$
- **Max length:** 100 segments
- **Timer:** PEEK system clock
- **Features:** Growth, speed progression

### Skills Learned

- UDG definition and design
- POKE to character memory
- Array-based game objects
- Timed movement loops
- Self-collision detection
- Food spawning logic
- Speed/difficulty progression

### UDG Definition Example

```basic
10 REM SNAKE HEAD
20 FOR i = 0 TO 7
30 READ a: POKE USR "a" + i, a
40 NEXT i
50 DATA 60, 126, 255, 255, 219, 255, 126, 60
```

### UDG Memory

| Letter | Address |
|--------|---------|
| A | USR "a" |
| B | USR "a" + 8 |
| C | USR "a" + 16 |
| ... | ... |

### Progression

This game prepares learners for **Asteroid Dodge** where they'll manage many more objects on screen and begin encountering BASIC's speed limitations.
