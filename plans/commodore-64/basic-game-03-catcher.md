# Catcher: 64-Unit Outline

**Game:** 3 - Catcher
**Platform:** Commodore 64
**Language:** BASIC V2
**Units:** 64 (4 phases)
**Prerequisite:** Star Field complete
**Concept:** Catch falling objects with a paddle. First real-time action game with keyboard control.

---

## Overview

Catcher is a simple action game where objects fall from the top of the screen and the player must catch them with a paddle at the bottom. This introduces real-time keyboard input, game loops, and collision detection.

---

## Learning Goals

By completing Catcher, learners will:

- Implement real-time keyboard polling with GET
- Create responsive player movement
- Manage falling object mechanics
- Implement collision detection using PEEK
- Build a score display system
- Create a lives/health system
- Implement difficulty progression
- Structure a complete action game loop

---

## Phase 1: Player Control (Units 1-16)
*Getting the paddle moving.*

### Units 1-4: GET Statement
- **Unit 1:** GET vs INPUT - non-blocking input
- **Unit 2:** Key detection - checking for keypresses
- **Unit 3:** Key codes - which keys return what
- **Unit 4:** Continuous polling - in a loop

### Units 5-8: Paddle Creation
- **Unit 5:** Paddle design - three characters wide
- **Unit 6:** Paddle position variable
- **Unit 7:** Drawing paddle - POKE to screen
- **Unit 8:** Paddle at bottom of screen

### Units 9-12: Paddle Movement
- **Unit 9:** Left movement - Z or , key
- **Unit 10:** Right movement - X or . key
- **Unit 11:** Clearing old paddle position
- **Unit 12:** Smooth left-right movement

### Units 13-16: Boundary Control
- **Unit 13:** Left edge detection
- **Unit 14:** Right edge detection
- **Unit 15:** Preventing off-screen movement
- **Unit 16:** Phase 1 complete - controllable paddle

**Phase Goal:** Smoothly moving player paddle.

---

## Phase 2: Falling Objects (Units 17-32)
*Things to catch.*

### Units 17-20: Single Falling Object
- **Unit 17:** Object character - what falls
- **Unit 18:** Object position variables - X and Y
- **Unit 19:** Vertical movement - falling down
- **Unit 20:** Object animation loop

### Units 21-24: Object Respawn
- **Unit 21:** Reaching bottom - object missed
- **Unit 22:** Respawn at top - random X position
- **Unit 23:** Reset Y position
- **Unit 24:** Continuous falling cycle

### Units 25-28: Fall Speed
- **Unit 25:** Speed variable - fall rate
- **Unit 26:** Frame counting - move every N loops
- **Unit 27:** Adjustable difficulty
- **Unit 28:** Smooth falling animation

### Units 29-32: Multiple Objects
- **Unit 29:** Object arrays - multiple fallers
- **Unit 30:** Initialising multiple objects
- **Unit 31:** Updating all objects per frame
- **Unit 32:** Phase 2 complete - falling objects system

**Phase Goal:** Multiple falling objects with respawn.

---

## Phase 3: Collision and Scoring (Units 33-48)
*Making it a game.*

### Units 33-36: Collision Detection
- **Unit 33:** PEEK from screen memory
- **Unit 34:** Checking paddle position
- **Unit 35:** Object meets paddle - caught!
- **Unit 36:** Precise collision - paddle width

### Units 37-40: Scoring
- **Unit 37:** Score variable
- **Unit 38:** Points for catch
- **Unit 39:** Score display - on screen
- **Unit 40:** High score tracking

### Units 41-44: Lives System
- **Unit 41:** Lives variable - starts at 3
- **Unit 42:** Losing a life - object reaches bottom
- **Unit 43:** Lives display
- **Unit 44:** Game over condition

### Units 45-48: Game Structure
- **Unit 45:** Title screen
- **Unit 46:** Game over screen
- **Unit 47:** Play again option
- **Unit 48:** Phase 3 complete - playable game with scoring

**Phase Goal:** Complete game with collision, score, and lives.

---

## Phase 4: Polish and Difficulty (Units 49-64)
*Making it challenging.*

### Units 49-52: Difficulty Progression
- **Unit 49:** Level system
- **Unit 50:** Speed increase per level
- **Unit 51:** More objects at higher levels
- **Unit 52:** Level display

### Units 53-56: Visual Polish
- **Unit 53:** Coloured objects - variety
- **Unit 54:** Catch effect - flash or sound
- **Unit 55:** Miss effect - warning colour
- **Unit 56:** Screen borders - play area

### Units 57-60: Special Objects
- **Unit 57:** Bonus objects - extra points
- **Unit 58:** Bad objects - avoid these
- **Unit 59:** Life objects - extra life
- **Unit 60:** Object variety - visual distinction

### Units 61-64: Final Game
- **Unit 61:** All features integrated
- **Unit 62:** Balance testing - fair difficulty
- **Unit 63:** Code cleanup
- **Unit 64:** **RELEASE: Catcher complete**

**Phase Goal:** Polished action game with progressive difficulty.

---

## Summary

**Catcher** establishes real-time game programming:

### Technical Specifications

- **Display:** Character mode (40×25)
- **Input:** Keyboard (GET) - real-time
- **Objects:** Paddle + up to 5 falling objects
- **Collision:** PEEK-based detection
- **Features:** Score, lives, levels

### Skills Learned

- Real-time keyboard polling
- Non-blocking input handling
- Falling object mechanics
- Collision detection with PEEK
- Score display and tracking
- Lives/health system
- Difficulty progression
- Game state management

### Game Loop Structure

```
10 REM INITIALISE
20 REM MAIN LOOP
30 GET K$: REM CHECK INPUT
40 REM MOVE PADDLE
50 REM MOVE OBJECTS
60 REM CHECK COLLISIONS
70 REM UPDATE SCORE
80 REM CHECK GAME OVER
90 GOTO 20
```

### Progression

This game prepares learners for **Maze Escape** where they'll use DATA statements to define level layouts and implement four-directional movement with wall collision.
