# Star Catcher: 64-Unit Outline

**Game:** 1 of 8 (AMOS BASIC)
**Platform:** Commodore Amiga
**Language:** AMOS BASIC
**Units:** 64 (4 phases)
**Concept:** Catch falling stars while avoiding hazards. Simple action game showcasing AMOS sprite handling.

---

## Why This Game First?

Star Catcher introduces AMOS fundamentals:

1. **AMOS environment** - Editor, testing, debugging
2. **Sprites** - AMOS sprite commands
3. **Collision** - SPRITE HIT detection
4. **Input** - Joystick and keyboard
5. **Sound** - Built-in effects and samples

A perfect introduction to AMOS capabilities.

---

## Phase 1: AMOS Basics (Units 1-16)
*Environment and first sprites.*

### Units 1-4: AMOS Environment
- **Unit 1:** AMOS editor - interface, modes
- **Unit 2:** Running programs - direct mode, run
- **Unit 3:** Saving and loading - .AMOS files
- **Unit 4:** Debugging basics - PRINT, STOP

### Units 5-8: Screen Setup
- **Unit 5:** SCREEN OPEN - display modes
- **Unit 6:** SCREEN DISPLAY - positioning
- **Unit 7:** INK and PALETTE - colours
- **Unit 8:** CLS and drawing basics

### Units 9-12: First Sprites
- **Unit 9:** Sprite editor - creating images
- **Unit 10:** GET SPRITE - capturing from screen
- **Unit 11:** SPRITE command - display sprite
- **Unit 12:** Sprite positioning - X, Y coordinates

### Units 13-16: Sprite Movement
- **Unit 13:** Moving sprites - updating position
- **Unit 14:** Sprite animation - multiple images
- **Unit 15:** Smooth movement - small increments
- **Unit 16:** First demo - moving sprite

**Phase Goal:** Moving sprite on screen.

---

## Phase 2: Player Control (Units 17-32)
*Input handling and player mechanics.*

### Units 17-20: Joystick Input
- **Unit 17:** JOY() function - reading joystick
- **Unit 18:** JLEFT, JRIGHT - directional checks
- **Unit 19:** JUP, JDOWN - vertical checks
- **Unit 20:** Fire button - FIRE()

### Units 21-24: Keyboard Input
- **Unit 21:** INKEY$ - key reading
- **Unit 22:** KEY STATE - specific keys
- **Unit 23:** Input options - joystick or keyboard
- **Unit 24:** Input responsiveness

### Units 25-28: Player Character
- **Unit 25:** Catcher sprite - basket/net design
- **Unit 26:** Horizontal movement - left/right
- **Unit 27:** Screen boundaries - keep on screen
- **Unit 28:** Player animation - movement states

### Units 29-32: Sound Effects
- **Unit 29:** BOOM, SHOOT, BELL - built-in sounds
- **Unit 30:** SAM PLAY - sample playback
- **Unit 31:** Sound for actions - movement, catch
- **Unit 32:** Sound volume and priority

**Phase Goal:** Controllable player with sound.

---

## Phase 3: Falling Objects (Units 33-48)
*Stars and hazards.*

### Units 33-36: Stars
- **Unit 33:** Star sprites - design
- **Unit 34:** Star spawning - random positions
- **Unit 35:** Star falling - downward movement
- **Unit 36:** Multiple stars - arrays

### Units 37-40: Collision Detection
- **Unit 37:** SPRITE HIT - collision check
- **Unit 38:** SPRITE COL - collision detection
- **Unit 39:** Star catching - player/star collision
- **Unit 40:** Caught stars - removal, scoring

### Units 41-44: Hazards
- **Unit 41:** Hazard sprites - bombs, rocks
- **Unit 42:** Hazard falling - same as stars
- **Unit 43:** Hazard collision - damage player
- **Unit 44:** Lives system - three lives

### Units 45-48: Game Flow
- **Unit 45:** Spawn timing - rate control
- **Unit 46:** Difficulty increase - faster, more
- **Unit 47:** Wave progression - difficulty curves
- **Unit 48:** Level transitions

**Phase Goal:** Complete catch/avoid gameplay.

---

## Phase 4: Polish and Completion (Units 49-64)
*Menus, scoring, and finish.*

### Units 49-52: Scoring
- **Unit 49:** Score variable - tracking points
- **Unit 50:** Score display - on-screen text
- **Unit 51:** Score multipliers - streak bonus
- **Unit 52:** High score - best score tracking

### Units 53-56: Game States
- **Unit 53:** Title screen - game name, start
- **Unit 54:** Playing state - main game
- **Unit 55:** Game over screen - final score
- **Unit 56:** State transitions - between screens

### Units 57-60: Presentation
- **Unit 57:** Background graphics - starfield
- **Unit 58:** Title graphics - logo design
- **Unit 59:** Background music - simple tune
- **Unit 60:** Visual polish - effects

### Units 61-64: Completion
- **Unit 61:** Difficulty settings - easy/normal/hard
- **Unit 62:** Instructions screen - how to play
- **Unit 63:** Full testing - all features
- **Unit 64:** Release build - final version

**Phase Goal:** Complete, polished game.

---

## Summary

**Star Catcher** teaches AMOS fundamentals.

### Game Specifications

- **Player:** Catcher sprite, horizontal movement
- **Objects:** Falling stars (catch) and hazards (avoid)
- **Scoring:** Points per star, streak bonuses
- **Lives:** 3, lost on hazard collision
- **Difficulty:** Increasing speed and density
- **Display:** AMOS screen mode, sprites
- **Sound:** Built-in effects, sample playback
- **Input:** Joystick or keyboard
- **Distribution:** AMOS source + compiled executable
