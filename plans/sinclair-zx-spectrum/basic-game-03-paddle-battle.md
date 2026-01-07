# Paddle Battle: 64-Unit Outline

**Game:** 3 - Paddle Battle
**Platform:** Sinclair ZX Spectrum
**Language:** Sinclair BASIC
**Units:** 64 (4 phases)
**Prerequisite:** Pixel Rain complete
**Concept:** Pong-style paddle game with INKEY$ keyboard control.

---

## Overview

Paddle Battle is a Pong-style game where players control paddles to bounce a ball back and forth. This introduces real-time keyboard input with INKEY$, collision detection, and the combination of PLOT and DRAW for game graphics.

---

## Learning Goals

By completing Paddle Battle, learners will:

- Implement real-time keyboard polling with INKEY$
- Use DRAW command for paddle graphics
- Create ball physics with velocity
- Implement collision detection
- Build a two-player game mode
- Create score display and tracking
- Manage game speed and difficulty
- Structure a complete action game

---

## Phase 1: Paddles and Input (Units 1-16)
*Getting paddles moving.*

### Units 1-4: INKEY$ Introduction
- **Unit 1:** INKEY$ vs INPUT - non-blocking
- **Unit 2:** Key detection - checking keypresses
- **Unit 3:** Continuous polling in a loop
- **Unit 4:** Multiple key handling

### Units 5-8: Paddle Drawing
- **Unit 5:** DRAW command - vertical line
- **Unit 6:** Paddle as thick line - multiple DRAWs
- **Unit 7:** Paddle position variable
- **Unit 8:** Erasing paddle - OVER 1 technique

### Units 9-12: Paddle Movement
- **Unit 9:** Left paddle controls - Q/A keys
- **Unit 10:** Right paddle controls - P/L keys
- **Unit 11:** Movement boundaries
- **Unit 12:** Smooth movement feel

### Units 13-16: Two Paddles
- **Unit 13:** Both paddles displayed
- **Unit 14:** Independent movement
- **Unit 15:** Boundary checking both
- **Unit 16:** Phase 1 complete - controllable paddles

**Phase Goal:** Two independently moving paddles.

---

## Phase 2: Ball Physics (Units 17-32)
*Adding the bouncing ball.*

### Units 17-20: Ball Basics
- **Unit 17:** Ball as PLOT pixel (or small shape)
- **Unit 18:** Ball position variables - X, Y
- **Unit 19:** Ball velocity - DX, DY
- **Unit 20:** Ball movement each frame

### Units 21-24: Wall Bouncing
- **Unit 21:** Top boundary detection
- **Unit 22:** Bottom boundary detection
- **Unit 23:** Y velocity reversal - bounce
- **Unit 24:** Continuous bouncing

### Units 25-28: Paddle Collision
- **Unit 25:** Left paddle position check
- **Unit 26:** Right paddle position check
- **Unit 27:** Ball hits paddle - X reversal
- **Unit 28:** Paddle miss detection

### Units 29-32: Game Loop
- **Unit 29:** Combined movement loop
- **Unit 30:** Input, ball update, collision
- **Unit 31:** Frame timing
- **Unit 32:** Phase 2 complete - bouncing ball game

**Phase Goal:** Playable ball-and-paddle mechanics.

---

## Phase 3: Scoring and Game Rules (Units 33-48)
*Making it competitive.*

### Units 33-36: Scoring
- **Unit 33:** Score variables - player 1 and 2
- **Unit 34:** Point when ball passes paddle
- **Unit 35:** Score display - PRINT AT
- **Unit 36:** Score update on point

### Units 37-40: Game Flow
- **Unit 37:** Point scored - pause
- **Unit 38:** Ball reset - centre court
- **Unit 39:** Serve direction alternates
- **Unit 40:** Game to 11 points

### Units 41-44: Win Conditions
- **Unit 41:** Winning score reached
- **Unit 42:** Winner announcement
- **Unit 43:** Game over screen
- **Unit 44:** Play again option

### Units 45-48: Single Player Mode
- **Unit 45:** Computer paddle - AI
- **Unit 46:** Ball tracking AI
- **Unit 47:** AI difficulty - reaction speed
- **Unit 48:** Phase 3 complete - full game modes

**Phase Goal:** Complete game with scoring and AI.

---

## Phase 4: Polish and Effects (Units 49-64)
*Refining the experience.*

### Units 49-52: Visual Enhancement
- **Unit 49:** Court lines - centre line with DRAW
- **Unit 50:** Score display - large characters
- **Unit 51:** Colour scheme - consistent
- **Unit 52:** Ball trail effect

### Units 53-56: Sound Effects
- **Unit 53:** BEEP for paddle hit
- **Unit 54:** BEEP for wall bounce
- **Unit 55:** BEEP for point scored
- **Unit 56:** Different tones per event

### Units 57-60: Difficulty Options
- **Unit 57:** Ball speed settings
- **Unit 58:** Paddle size options
- **Unit 59:** Menu system
- **Unit 60:** Difficulty selection

### Units 61-64: Final Game
- **Unit 61:** Title screen
- **Unit 62:** All modes tested
- **Unit 63:** Code cleanup
- **Unit 64:** **RELEASE: Paddle Battle complete**

**Phase Goal:** Polished two-player Pong game.

---

## Summary

**Paddle Battle** establishes real-time game programming:

### Technical Specifications

- **Display:** High-resolution with DRAW
- **Input:** INKEY$ real-time polling
- **Players:** 1-2 players
- **AI:** Basic ball-tracking
- **Audio:** BEEP sound effects

### Skills Learned

- Real-time keyboard input
- Line drawing with DRAW
- Ball velocity and physics
- Collision detection
- Two-player implementation
- Simple AI opponent
- Game state management
- Sound effect usage

### INKEY$ vs INPUT

| Feature | INPUT | INKEY$ |
|---------|-------|--------|
| Blocking | Yes - waits | No - continues |
| Use case | Menu selection | Real-time games |
| Key storage | Variable | Must check immediately |

### Progression

This game prepares learners for **Dungeon Explorer** where they'll use DATA statements to define room layouts and implement character-based maps with PRINT AT.
