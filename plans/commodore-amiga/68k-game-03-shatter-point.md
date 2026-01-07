# Shatter Point: 64-Unit Outline

**Game:** 3 of 16 (68000 Assembly)
**Platform:** Commodore Amiga
**Language:** 68000 Assembly
**Units:** 64 (4 phases)
**Concept:** Breakout clone with Copper gradients and sampled sound.

---

## Why This Game Third?

Shatter Point introduces fixed-point maths and Copper gradients:

1. **Fixed-point maths** - Precise ball physics
2. **Blitter fills** - Brick rendering
3. **Copper gradients** - Beautiful backgrounds
4. **Power-up system** - Special effects
5. **Sample mixing** - Multiple sounds

Expands Copper and Blitter skills from previous games.

---

## Skills Applied from Previous Games

| Skill | From | Application |
|-------|------|-------------|
| Copper lists | Signal | Gradient backgrounds |
| Hardware sprites | Both | Ball, paddle |
| Blitter operations | Both | Bricks, effects |
| Object management | Blast Zone | Power-ups |
| Paula audio | Both | Sound effects |

## New Skills Introduced

| Skill | Phase | Description |
|-------|-------|-------------|
| Fixed-point maths | 1 | Ball velocity |
| Blitter fills | 2 | Brick drawing |
| Copper gradients | 2 | Sky backgrounds |
| Reflection physics | 1 | Bounce angles |
| Power-up effects | 3 | Game modifiers |

---

## Phase 1: Ball Physics (Units 1-16)
*Fixed-point movement and reflection.*

### Units 1-4: Fixed-Point Maths
- **Unit 1:** Fixed-point concept - fractional values
- **Unit 2:** 16.16 format - integer.fraction
- **Unit 3:** Fixed-point operations - multiply, divide
- **Unit 4:** Converting to screen coordinates

### Units 5-8: Ball Movement
- **Unit 5:** Ball sprite - design
- **Unit 6:** Ball velocity - X and Y components
- **Unit 7:** Ball position - fixed-point tracking
- **Unit 8:** Smooth movement - per-frame update

### Units 9-12: Paddle
- **Unit 9:** Paddle sprite - design
- **Unit 10:** Paddle movement - joystick/mouse
- **Unit 11:** Paddle boundaries - screen edges
- **Unit 12:** Ball launch - from paddle

### Units 13-16: Reflection
- **Unit 13:** Wall reflection - X flip
- **Unit 14:** Ceiling reflection - Y flip
- **Unit 15:** Paddle reflection - angle by position
- **Unit 16:** Ball demo - bouncing physics

**Phase Goal:** Ball with proper physics.

---

## Phase 2: Bricks and Display (Units 17-32)
*Blitter brick field and Copper gradients.*

### Units 17-20: Copper Gradients
- **Unit 17:** Gradient concept - colour per line
- **Unit 18:** Copper colour changes - wait/move
- **Unit 19:** Smooth gradients - interpolation
- **Unit 20:** Background gradient - sky effect

### Units 21-24: Blitter Fills
- **Unit 21:** Blitter fill mode - BLTCON1
- **Unit 22:** Area fill - solid rectangles
- **Unit 23:** Brick drawing - filled blocks
- **Unit 24:** Brick colours - per row

### Units 25-28: Brick Field
- **Unit 25:** Brick array - tracking state
- **Unit 26:** Brick positions - grid layout
- **Unit 27:** Drawing brick field
- **Unit 28:** Brick collision - ball/brick

### Units 29-32: Brick Destruction
- **Unit 29:** Brick removal - Blitter clear
- **Unit 30:** Bounce direction - which side hit
- **Unit 31:** Brick scoring - points
- **Unit 32:** Field complete - all destroyed

**Phase Goal:** Destructible brick field.

---

## Phase 3: Power-ups and Levels (Units 33-48)
*Special effects and level design.*

### Units 33-36: Power-up System
- **Unit 33:** Power-up sprites - falling items
- **Unit 34:** Power-up dropping - from bricks
- **Unit 35:** Power-up collision - paddle catch
- **Unit 36:** Power-up types - different effects

### Units 37-40: Power-up Effects
- **Unit 37:** Wide paddle - expand sprite
- **Unit 38:** Multi-ball - spawn copies
- **Unit 39:** Laser paddle - direct shooting
- **Unit 40:** Extra life - bonus life

### Units 41-44: Level Design
- **Unit 41:** Level data - brick patterns
- **Unit 42:** Level 1 - simple layout
- **Unit 43:** Level 2 - harder pattern
- **Unit 44:** Unbreakable bricks - gold blocks

### Units 45-48: Level Progression
- **Unit 45:** Level complete - transition
- **Unit 46:** Speed increase - per level
- **Unit 47:** New patterns - variety
- **Unit 48:** Level selection

**Phase Goal:** Power-ups and levels.

---

## Phase 4: Audio and Polish (Units 49-64)
*Sound and completion.*

### Units 49-52: Enhanced Audio
- **Unit 49:** Bounce sounds - wall, paddle
- **Unit 50:** Brick break sounds - pitched
- **Unit 51:** Power-up sounds - collect
- **Unit 52:** Mixing multiple sounds

### Units 53-56: Presentation
- **Unit 53:** Title screen - gradient background
- **Unit 54:** Level intro - pattern preview
- **Unit 55:** Lives display - ball icons
- **Unit 56:** Score display - Blitter text

### Units 57-60: Game Features
- **Unit 57:** High score system
- **Unit 58:** Continue option
- **Unit 59:** Difficulty levels
- **Unit 60:** Two-player alternating

### Units 61-64: Release
- **Unit 61:** Game over sequence
- **Unit 62:** Victory sequence
- **Unit 63:** Full testing
- **Unit 64:** Release build - ADF

**Phase Goal:** Complete Breakout clone.

---

## Summary

**Shatter Point** teaches fixed-point maths and Copper gradients.

### Technical Specifications

- **Display:** 320×256, 5 bitplanes
- **Ball/Paddle:** Hardware sprites
- **Bricks:** Blitter-filled rectangles
- **Background:** Copper gradient
- **Physics:** 16.16 fixed-point
- **Power-ups:** 4+ types
- **Audio:** Multi-channel effects
- **Distribution:** Bootable ADF

### Skills for Next Game

- Fixed-point mathematics
- Copper gradient effects
- Blitter fill operations
- Power-up systems
- Multi-sound mixing
