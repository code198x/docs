# Ascent: 64-Unit Outline

**Game:** 4 of 16 (68000 Assembly)
**Platform:** Commodore Amiga
**Language:** 68000 Assembly
**Units:** 64 (4 phases)
**Concept:** Single-screen platformer. Climb upward through hazards.

---

## Why This Game Fourth?

Ascent introduces platformer fundamentals:

1. **Gravity physics** - Falling and jumping
2. **Platform collision** - Bitplane-based detection
3. **Cookie-cut masking** - Proper BOB compositing
4. **Enemy patterns** - Simple AI
5. **Level structures** - Data-driven design

Foundation for scrolling platformers later.

---

## Skills Applied from Previous Games

| Skill | From | Application |
|-------|------|-------------|
| Fixed-point maths | Shatter Point | Physics |
| Blitter operations | All | Player, platforms |
| Copper lists | All | Display |
| Hardware sprites | All | Player option |
| Audio | All | Sound effects |

## New Skills Introduced

| Skill | Phase | Description |
|-------|-------|-------------|
| Gravity simulation | 1 | Falling physics |
| Jump mechanics | 1 | Velocity jumping |
| Platform collision | 2 | Bitplane testing |
| Cookie-cut mask | 2 | BOB compositing |
| Enemy patterns | 3 | Simple AI |

---

## Phase 1: Player Physics (Units 1-16)
*Gravity, jumping, movement.*

### Units 1-4: Gravity
- **Unit 1:** Gravity concept - acceleration
- **Unit 2:** Y velocity - falling speed
- **Unit 3:** Terminal velocity - max fall
- **Unit 4:** Gravity constant - tuning

### Units 5-8: Jumping
- **Unit 5:** Jump initiation - button press
- **Unit 6:** Jump velocity - upward force
- **Unit 7:** Jump arc - gravity affects
- **Unit 8:** Variable jump - hold for height

### Units 9-12: Horizontal Movement
- **Unit 9:** Run speed - X velocity
- **Unit 10:** Acceleration - speed up
- **Unit 11:** Deceleration - slow down
- **Unit 12:** Air control - move while jumping

### Units 13-16: Player Sprite
- **Unit 13:** Player BOB - multi-frame
- **Unit 14:** Animation states - idle, run, jump
- **Unit 15:** Direction facing - flip
- **Unit 16:** Physics demo - jumping player

**Phase Goal:** Player with full physics.

---

## Phase 2: Platforms and Collision (Units 17-32)
*Platform detection and rendering.*

### Units 17-20: Cookie-Cut Masking
- **Unit 17:** Cookie-cut concept - transparent areas
- **Unit 18:** Mask data - separate bitplane
- **Unit 19:** Blitter setup - A, B, C, D channels
- **Unit 20:** Proper compositing - no background damage

### Units 21-24: Platform Rendering
- **Unit 21:** Platform tiles - bob graphics
- **Unit 22:** Level data - platform positions
- **Unit 23:** Drawing platforms - to background
- **Unit 24:** Background buffer - playfield

### Units 25-28: Collision Detection
- **Unit 25:** Collision concept - feet checking
- **Unit 26:** Bitplane testing - BTST on pixel
- **Unit 27:** Ground detection - standing
- **Unit 28:** Wall detection - blocking

### Units 29-32: Platform Mechanics
- **Unit 29:** Landing - stop falling
- **Unit 30:** Platform edges - can fall off
- **Unit 31:** Head collision - ceiling
- **Unit 32:** Collision demo - player on platforms

**Phase Goal:** Player walking on platforms.

---

## Phase 3: Enemies and Hazards (Units 33-48)
*Obstacles and threats.*

### Units 33-36: Enemy Basics
- **Unit 33:** Enemy BOBs - designs
- **Unit 34:** Enemy array - tracking
- **Unit 35:** Enemy rendering - BOBs
- **Unit 36:** Enemy animation - frame cycling

### Units 37-40: Enemy AI
- **Unit 37:** Patrol behaviour - walk back/forth
- **Unit 38:** Platform aware - stay on platform
- **Unit 39:** Edge turning - don't fall
- **Unit 40:** Chase behaviour - follow player

### Units 41-44: Hazards
- **Unit 41:** Static hazards - spikes
- **Unit 42:** Moving hazards - projectiles
- **Unit 43:** Hazard collision - damage
- **Unit 44:** Death handling - respawn

### Units 45-48: Combat
- **Unit 45:** Player attack - stomp or projectile
- **Unit 46:** Enemy collision - damage player
- **Unit 47:** Enemy defeat - remove
- **Unit 48:** Lives system - 3 lives

**Phase Goal:** Enemies and hazards working.

---

## Phase 4: Levels and Completion (Units 49-64)
*Level design and polish.*

### Units 49-52: Level Design
- **Unit 49:** Level 1 - tutorial
- **Unit 50:** Level 2 - climbing
- **Unit 51:** Level 3 - hazards
- **Unit 52:** Level goal - reach top

### Units 53-56: Audio
- **Unit 53:** Jump sound
- **Unit 54:** Land sound
- **Unit 55:** Enemy sounds
- **Unit 56:** Background music

### Units 57-60: Presentation
- **Unit 57:** Title screen
- **Unit 58:** Level intro
- **Unit 59:** Score display
- **Unit 60:** Lives display

### Units 61-64: Release
- **Unit 61:** Level progression
- **Unit 62:** Game over
- **Unit 63:** Full testing
- **Unit 64:** Release build - ADF

**Phase Goal:** Complete single-screen platformer.

---

## Summary

**Ascent** teaches platformer physics and collision.

### Technical Specifications

- **Display:** 320×256, 5 bitplanes
- **Player:** Cookie-cut BOB
- **Platforms:** Blitter-rendered tiles
- **Enemies:** BOBs with AI
- **Physics:** Gravity, jumping
- **Collision:** Bitplane testing
- **Levels:** 3+ single-screen
- **Distribution:** Bootable ADF

### Skills for Next Game

- Gravity and jump physics
- Platform collision detection
- Cookie-cut BOB rendering
- Simple enemy AI
- Level data structures
