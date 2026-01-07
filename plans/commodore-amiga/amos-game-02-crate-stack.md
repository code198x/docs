# Crate Stack: 64-Unit Outline

**Game:** 2 of 8 (AMOS BASIC)
**Platform:** Commodore Amiga
**Language:** AMOS BASIC
**Units:** 64 (4 phases)
**Concept:** Single-screen platformer. Jump between platforms, collect items, reach the exit. Introduction to physics in AMOS.

---

## Why This Game Second?

Crate Stack introduces platformer fundamentals:

1. **Gravity** - Simulated physics
2. **Jumping** - Velocity-based mechanics
3. **Bobs** - Blitter Objects for backgrounds
4. **Animation** - Multi-frame player
5. **Level data** - DATA statement storage

Building on sprites from Game 1, adds physics.

---

## Skills Applied from Game 1

| Skill | Application in Crate Stack |
|-------|---------------------------|
| AMOS environment | Development workflow |
| Sprites | Player character |
| Input handling | Movement controls |
| Collision | Platform detection |
| Sound effects | Jump, collect sounds |

## New Skills Introduced

| Skill | Phase | Description |
|-------|-------|-------------|
| Gravity simulation | 1 | Falling physics |
| Jump mechanics | 1 | Velocity jumping |
| Bobs (BOB command) | 2 | Background graphics |
| Animation sequences | 2 | Multi-frame sprites |
| Level data | 3 | DATA statements |
| Multiple levels | 4 | Level progression |

---

## Phase 1: Physics Foundation (Units 1-16)
*Gravity and jumping.*

### Units 1-4: Gravity
- **Unit 1:** Velocity concept - speed over time
- **Unit 2:** Y velocity - falling speed
- **Unit 3:** Gravity constant - acceleration
- **Unit 4:** Terminal velocity - max fall speed

### Units 5-8: Jumping
- **Unit 5:** Jump initiation - button press
- **Unit 6:** Jump velocity - upward force
- **Unit 7:** Jump arc - gravity takes over
- **Unit 8:** Landing detection - ground check

### Units 9-12: Ground Collision
- **Unit 9:** Ground level - floor position
- **Unit 10:** Ground detection - stop falling
- **Unit 11:** Grounded state - can jump
- **Unit 12:** Basic physics demo

### Units 13-16: Player Movement
- **Unit 13:** Horizontal movement - left/right
- **Unit 14:** Air control - move while jumping
- **Unit 15:** Screen boundaries - keep in bounds
- **Unit 16:** Physics integration - full movement

**Phase Goal:** Player with gravity and jumping.

---

## Phase 2: Graphics and Animation (Units 17-32)
*Bobs and animation sequences.*

### Units 17-20: Bob Basics
- **Unit 17:** Bob concept - vs sprites
- **Unit 18:** GET BOB - capturing bobs
- **Unit 19:** PASTE BOB - drawing bobs
- **Unit 20:** Bob positioning - screen placement

### Units 21-24: Player Animation
- **Unit 21:** Animation frames - multiple images
- **Unit 22:** Walk cycle - alternating frames
- **Unit 23:** Jump animation - rising/falling
- **Unit 24:** Direction facing - left/right

### Units 25-28: Platform Graphics
- **Unit 25:** Platform bob - crate design
- **Unit 26:** Drawing platforms - PASTE BOB
- **Unit 27:** Background colours - scene setup
- **Unit 28:** Visual layering - depth

### Units 29-32: Collectibles
- **Unit 29:** Collectible sprites - gems, coins
- **Unit 30:** Collectible animation - spinning
- **Unit 31:** Collectible placement - on platforms
- **Unit 32:** Collection feedback - visual/audio

**Phase Goal:** Animated player with platform graphics.

---

## Phase 3: Level Design (Units 33-48)
*Data-driven level creation.*

### Units 33-36: Level Data
- **Unit 33:** DATA statements - storing levels
- **Unit 34:** READ command - loading data
- **Unit 35:** Platform data - position, size
- **Unit 36:** Level building - from data

### Units 37-40: Platform Collision
- **Unit 37:** Platform array - tracking platforms
- **Unit 38:** Collision detection - player/platform
- **Unit 39:** Standing on platforms - grounded state
- **Unit 40:** Platform edges - falling off

### Units 41-44: Level Elements
- **Unit 41:** Exit door - level goal
- **Unit 42:** Exit collision - level complete
- **Unit 43:** Hazards - spikes, gaps
- **Unit 44:** Hazard collision - lose life

### Units 45-48: Level Flow
- **Unit 45:** Level 1 design - tutorial
- **Unit 46:** Level 2 design - more challenge
- **Unit 47:** Level 3 design - advanced
- **Unit 48:** Level transitions - between levels

**Phase Goal:** Multiple playable levels.

---

## Phase 4: Game Features (Units 49-64)
*Scoring, lives, polish.*

### Units 49-52: Scoring System
- **Unit 49:** Score tracking - points
- **Unit 50:** Collectible points - value per item
- **Unit 51:** Time bonus - faster completion
- **Unit 52:** Score display - on-screen

### Units 53-56: Lives and Continues
- **Unit 53:** Lives system - 3 lives
- **Unit 54:** Death handling - restart position
- **Unit 55:** Game over - all lives lost
- **Unit 56:** Continue option - restart level

### Units 57-60: Presentation
- **Unit 57:** Title screen - game logo
- **Unit 58:** Level intro - "Level X"
- **Unit 59:** Sound effects - jump, land, collect
- **Unit 60:** Background music - level tune

### Units 61-64: Completion
- **Unit 61:** Five levels total
- **Unit 62:** Victory screen - game complete
- **Unit 63:** Full testing
- **Unit 64:** Release build

**Phase Goal:** Complete platformer.

---

## Summary

**Crate Stack** teaches platformer physics in AMOS.

### Game Specifications

- **Player:** Animated character, jump/run
- **Physics:** Gravity, velocity-based jumping
- **Platforms:** Bob-rendered crates
- **Collectibles:** Gems for points
- **Levels:** 5 single-screen levels
- **Hazards:** Spikes, gaps
- **Lives:** 3, respawn on level
- **Display:** AMOS screen, sprites + bobs
- **Sound:** Jump, collect, death sounds
- **Distribution:** AMOS source + compiled
