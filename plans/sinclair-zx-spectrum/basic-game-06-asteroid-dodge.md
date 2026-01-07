# Asteroid Dodge: 64-Unit Outline

**Game:** 6 - Asteroid Dodge
**Platform:** Sinclair ZX Spectrum
**Language:** Sinclair BASIC
**Units:** 64 (4 phases)
**Prerequisite:** Snake Spectrum complete
**Concept:** Space ship dodges falling asteroids. Exploring BASIC's performance limits.

---

## Overview

Asteroid Dodge puts the player's ship at the bottom of the screen as asteroids scroll downward. The player must weave through the falling rocks to survive as long as possible. This game manages multiple objects and reveals Sinclair BASIC's performance characteristics.

---

## Learning Goals

By completing Asteroid Dodge, learners will:

- Manage multiple simultaneous objects
- Implement simulated vertical scrolling
- Create complex UDG designs (ship, asteroids)
- Use DRAW for visual effects
- Build difficulty ramping systems
- Track and display high scores
- Observe attribute clash first-hand
- Understand BASIC performance limits

---

## Phase 1: Ship and Asteroids (Units 1-16)
*Creating the game elements.*

### Units 1-4: Ship Design
- **Unit 1:** Ship UDG design - distinctive look
- **Unit 2:** Multi-character ship (2×2)
- **Unit 3:** Ship positioning at bottom
- **Unit 4:** Ship colour - standing out

### Units 5-8: Asteroid Design
- **Unit 5:** Asteroid UDG design
- **Unit 6:** Multiple asteroid variants
- **Unit 7:** Asteroid colour scheme
- **Unit 8:** Visual variety

### Units 9-12: Ship Movement
- **Unit 9:** Left/right INKEY$ controls
- **Unit 10:** Movement speed
- **Unit 11:** Boundary limits
- **Unit 12:** Responsive feel

### Units 13-16: Asteroid Movement
- **Unit 13:** Falling asteroids - Y decreasing
- **Unit 14:** Multiple asteroid tracking
- **Unit 15:** Asteroid respawn at top
- **Unit 16:** Phase 1 complete - elements moving

**Phase Goal:** Ship and asteroids moving independently.

---

## Phase 2: Collision and Gameplay (Units 17-32)
*Making it a game.*

### Units 17-20: Collision Detection
- **Unit 17:** Ship hitbox definition
- **Unit 18:** Asteroid position checking
- **Unit 19:** Overlap detection
- **Unit 20:** Collision response

### Units 21-24: Game Loop
- **Unit 21:** Main loop structure
- **Unit 22:** Input processing
- **Unit 23:** Object updates
- **Unit 24:** Draw and timing

### Units 25-28: Lives System
- **Unit 25:** Lives variable
- **Unit 26:** Collision costs a life
- **Unit 27:** Invulnerability period
- **Unit 28:** Game over at zero lives

### Units 29-32: Scoring
- **Unit 29:** Score based on time
- **Unit 30:** Bonus for near misses
- **Unit 31:** Score display
- **Unit 32:** Phase 2 complete - playable game

**Phase Goal:** Complete gameplay with collision and lives.

---

## Phase 3: Multiple Objects (Units 33-48)
*Managing the asteroid field.*

### Units 33-36: Asteroid Arrays
- **Unit 33:** X position array
- **Unit 34:** Y position array
- **Unit 35:** Speed array - per asteroid
- **Unit 36:** Active state array

### Units 37-40: Increasing Density
- **Unit 37:** Start with few asteroids
- **Unit 38:** Add more over time
- **Unit 39:** Maximum asteroid count
- **Unit 40:** Balanced difficulty curve

### Units 41-44: Performance Observation
- **Unit 41:** Frame rate with few asteroids
- **Unit 42:** Frame rate with many asteroids
- **Unit 43:** Slowdown observation
- **Unit 44:** The BASIC bottleneck

### Units 45-48: Attribute Clash
- **Unit 45:** Colour cells revealed
- **Unit 46:** Ship meets asteroid colours
- **Unit 47:** Clash as gameplay reality
- **Unit 48:** Phase 3 complete - multi-object management

**Phase Goal:** Multiple asteroids with performance awareness.

---

## Phase 4: Effects and Polish (Units 49-64)
*Visual and audio enhancement.*

### Units 49-52: Visual Effects
- **Unit 49:** DRAW for explosion effects
- **Unit 50:** Star field background
- **Unit 51:** Trail effects
- **Unit 52:** Visual feedback

### Units 53-56: Sound Effects
- **Unit 53:** BEEP for collision
- **Unit 54:** BEEP for near miss
- **Unit 55:** BEEP for milestone
- **Unit 56:** Audio feedback

### Units 57-60: High Scores
- **Unit 57:** High score tracking
- **Unit 58:** Name entry for high score
- **Unit 59:** High score display
- **Unit 60:** Persistence during session

### Units 61-64: Final Game
- **Unit 61:** Title screen
- **Unit 62:** Difficulty options
- **Unit 63:** "Why assembly matters" discussion
- **Unit 64:** **RELEASE: Asteroid Dodge complete**

**Phase Goal:** Polished game with performance understanding.

---

## Summary

**Asteroid Dodge** reveals BASIC's limitations:

### Technical Specifications

- **Display:** Character mode with UDGs
- **Ship:** 2×2 character ship
- **Asteroids:** 5-15 depending on speed
- **Input:** Real-time INKEY$
- **Features:** Scoring, lives, difficulty progression

### Skills Learned

- Multiple object management
- Simulated scrolling concept
- Complex UDG designs
- DRAW for effects
- Difficulty ramping
- Performance observation
- Attribute clash awareness

### Performance Observations

| Asteroids | Frame Rate | Experience |
|-----------|-----------|------------|
| 5 | Good | Smooth |
| 10 | Fair | Acceptable |
| 15 | Poor | Sluggish |
| 20+ | Bad | Unplayable |

### Attribute Clash Reality

When ship and asteroids share an 8×8 cell:
- Colours conflict
- One colour wins per cell
- Visual messiness
- Spectrum signature limitation

### Progression

This game prepares learners for **Pattern Match** where turn-based gameplay avoids real-time performance issues and full UDG capabilities are explored.
