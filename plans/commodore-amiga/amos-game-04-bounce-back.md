# Bounce Back: 64-Unit Outline

**Game:** 4 of 8 (AMOS BASIC)
**Platform:** Commodore Amiga
**Language:** AMOS BASIC
**Units:** 64 (4 phases)
**Concept:** Breakout clone. Paddle, ball, and bricks with AMOS's smooth movement and sound.

---

## Why This Game Fourth?

Bounce Back introduces ball physics:

1. **Ball physics** - Angles and reflection
2. **SCREEN SWAP** - Double buffering
3. **Power-ups** - Special brick effects
4. **Level design** - Brick patterns
5. **Music** - During gameplay

Expands physics understanding from Crate Stack.

---

## Skills Applied from Previous Games

| Skill | From | Application in Bounce Back |
|-------|------|---------------------------|
| Physics | Crate Stack | Ball movement |
| Collision | All | Brick/paddle/ball |
| Sprite arrays | Space Swarm | Brick tracking |
| Sound effects | All | Bounce, break sounds |
| Level data | Crate Stack | Brick patterns |

## New Skills Introduced

| Skill | Phase | Description |
|-------|-------|-------------|
| Angle physics | 1 | Ball reflection |
| SCREEN SWAP | 2 | Double buffering |
| Bob arrays | 2 | Brick rendering |
| Power-up system | 3 | Special effects |
| Level editor | 4 | Design concept |

---

## Phase 1: Ball and Paddle (Units 1-16)
*Core Breakout mechanics.*

### Units 1-4: Paddle
- **Unit 1:** Paddle sprite - design
- **Unit 2:** Paddle movement - left/right
- **Unit 3:** Paddle boundaries - screen edges
- **Unit 4:** Paddle response - smooth control

### Units 5-8: Ball Basics
- **Unit 5:** Ball sprite - design
- **Unit 6:** Ball velocity - X and Y components
- **Unit 7:** Ball movement - per-frame update
- **Unit 8:** Ball speed - constant velocity

### Units 9-12: Ball Reflection
- **Unit 9:** Wall bounce - left/right walls
- **Unit 10:** Ceiling bounce - top wall
- **Unit 11:** Paddle bounce - angle by position
- **Unit 12:** Bottom exit - ball lost

### Units 13-16: Core Loop
- **Unit 13:** Ball launch - from paddle
- **Unit 14:** Lives system - ball lost = life lost
- **Unit 15:** Ball reset - after loss
- **Unit 16:** Basic demo - paddle and ball

**Phase Goal:** Playable ball and paddle.

---

## Phase 2: Bricks and Display (Units 17-32)
*Brick field rendering.*

### Units 17-20: SCREEN SWAP
- **Unit 17:** Double buffering concept - flicker-free
- **Unit 18:** SCREEN SWAP command - buffer flip
- **Unit 19:** Drawing to back buffer
- **Unit 20:** Smooth display - no tearing

### Units 21-24: Brick Graphics
- **Unit 21:** Brick bobs - coloured blocks
- **Unit 22:** Brick array - tracking all
- **Unit 23:** Brick positioning - grid layout
- **Unit 24:** Drawing bricks - PASTE BOB

### Units 25-28: Brick Collision
- **Unit 25:** Ball/brick collision - detection
- **Unit 26:** Brick destruction - mark removed
- **Unit 27:** Bounce direction - which side hit
- **Unit 28:** Brick scoring - points

### Units 29-32: Visual Polish
- **Unit 29:** Brick colours - by row
- **Unit 30:** Break effect - visual feedback
- **Unit 31:** Score display - on screen
- **Unit 32:** Lives display - remaining

**Phase Goal:** Destructible brick field.

---

## Phase 3: Power-ups and Levels (Units 33-48)
*Special effects and progression.*

### Units 33-36: Power-up System
- **Unit 33:** Power-up concept - special bricks
- **Unit 34:** Power-up drop - falls when brick breaks
- **Unit 35:** Power-up catch - paddle collision
- **Unit 36:** Power-up types - different effects

### Units 37-40: Power-up Effects
- **Unit 37:** Wide paddle - expand size
- **Unit 38:** Multi-ball - split into three
- **Unit 39:** Slow ball - reduced speed
- **Unit 40:** Extra life - bonus life

### Units 41-44: Level Design
- **Unit 41:** Level data - brick patterns
- **Unit 42:** Level 1 - simple pattern
- **Unit 43:** Level 2 - harder pattern
- **Unit 44:** Level 3 - complex pattern

### Units 45-48: Level Progression
- **Unit 45:** Level complete - all bricks gone
- **Unit 46:** Level transition - next level
- **Unit 47:** Increasing difficulty - speed up
- **Unit 48:** Total levels - 5+

**Phase Goal:** Power-ups and multiple levels.

---

## Phase 4: Polish and Completion (Units 49-64)
*Music, presentation, finish.*

### Units 49-52: Audio
- **Unit 49:** Bounce sounds - wall, paddle, brick
- **Unit 50:** Break sounds - brick destruction
- **Unit 51:** Power-up sounds - collect, activate
- **Unit 52:** Background music - gameplay tune

### Units 53-56: Presentation
- **Unit 53:** Title screen - game logo
- **Unit 54:** Level intro - pattern preview
- **Unit 55:** Game over screen
- **Unit 56:** Victory screen - game complete

### Units 57-60: Features
- **Unit 57:** High score system
- **Unit 58:** Two-player alternating
- **Unit 59:** Difficulty settings
- **Unit 60:** Level select (unlocked)

### Units 61-64: Completion
- **Unit 61:** Level editor concept - design tool
- **Unit 62:** Custom levels - load from data
- **Unit 63:** Full testing
- **Unit 64:** Release build

**Phase Goal:** Complete Breakout clone.

---

## Summary

**Bounce Back** teaches ball physics and double buffering.

### Game Specifications

- **Paddle:** Sprite, horizontal movement
- **Ball:** Angle-based physics
- **Bricks:** Bob-rendered, coloured by row
- **Power-ups:** Wide, multi-ball, slow, extra life
- **Levels:** 5+ with unique patterns
- **Display:** Double-buffered with SCREEN SWAP
- **Scoring:** Points per brick, power-up bonuses
- **Lives:** 3, ball loss = life loss
- **Sound:** Bounce, break, music
- **Distribution:** AMOS source + compiled
