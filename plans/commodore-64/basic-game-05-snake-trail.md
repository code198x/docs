# Snake Trail: 64-Unit Outline

**Game:** 5 - Snake Trail
**Platform:** Commodore 64
**Language:** BASIC V2
**Units:** 64 (4 phases)
**Prerequisite:** Maze Escape complete
**Concept:** Classic snake game using character graphics. Introduces arrays for body tracking.

---

## Overview

Snake Trail is a classic snake game where the player controls a growing snake, eating food to increase length while avoiding collisions with walls and their own body. This game introduces array usage for tracking the snake's body segments.

---

## Learning Goals

By completing Snake Trail, learners will:

- Use DIM to declare arrays
- Implement circular buffer for body tracking
- Create timed movement using TI
- Build self-collision detection
- Implement food spawning
- Create growth mechanics
- Handle screen wrapping
- Manage game speed progression

---

## Phase 1: Snake Basics (Units 1-16)
*Getting the snake moving.*

### Units 1-4: Array Fundamentals
- **Unit 1:** DIM statement - declaring arrays
- **Unit 2:** Array indexing - accessing elements
- **Unit 3:** Arrays for coordinates - X and Y
- **Unit 4:** Array bounds - maximum size

### Units 5-8: Snake Head
- **Unit 5:** Head position variables
- **Unit 6:** Drawing the head
- **Unit 7:** Direction variable - up, down, left, right
- **Unit 8:** Direction change with keys

### Units 9-12: Timed Movement
- **Unit 9:** TI variable - system timer
- **Unit 10:** Move timing - not every loop
- **Unit 11:** Consistent speed - frames between moves
- **Unit 12:** Movement feels right

### Units 13-16: Basic Movement
- **Unit 13:** Move in current direction
- **Unit 14:** Update head position
- **Unit 15:** Draw new position
- **Unit 16:** Phase 1 complete - controllable head

**Phase Goal:** Moving snake head with direction control.

---

## Phase 2: Snake Body (Units 17-32)
*Growing the trail.*

### Units 17-20: Body Tracking
- **Unit 17:** Body segment array - X positions
- **Unit 18:** Body segment array - Y positions
- **Unit 19:** Body length variable
- **Unit 20:** Initial body - three segments

### Units 21-24: Body Movement
- **Unit 21:** Circular buffer concept
- **Unit 22:** Head becomes body
- **Unit 23:** Tail removal - last segment
- **Unit 24:** Body follows head

### Units 25-28: Body Display
- **Unit 25:** Drawing body segments
- **Unit 26:** Different character for body
- **Unit 27:** Erasing old tail
- **Unit 28:** Visual snake complete

### Units 29-32: Self-Collision
- **Unit 29:** Check head against body
- **Unit 30:** Loop through body array
- **Unit 31:** Collision detection
- **Unit 32:** Phase 2 complete - moving snake with body

**Phase Goal:** Complete snake with trailing body.

---

## Phase 3: Food and Growth (Units 33-48)
*Eating to survive.*

### Units 33-36: Food Spawning
- **Unit 33:** Food position variables
- **Unit 34:** Random food placement
- **Unit 35:** Avoid spawning on snake
- **Unit 36:** Drawing food character

### Units 37-40: Eating Mechanics
- **Unit 37:** Head meets food detection
- **Unit 38:** Increment length variable
- **Unit 39:** Don't remove tail - growth!
- **Unit 40:** Spawn new food

### Units 41-44: Scoring
- **Unit 41:** Score variable
- **Unit 42:** Points per food
- **Unit 43:** Score display on screen
- **Unit 44:** High score tracking

### Units 45-48: Wall Collision
- **Unit 45:** Screen boundary detection
- **Unit 46:** Wall collision = game over
- **Unit 47:** OR screen wrapping option
- **Unit 48:** Phase 3 complete - eat, grow, score

**Phase Goal:** Complete snake game with food and scoring.

---

## Phase 4: Polish and Features (Units 49-64)
*Refining the experience.*

### Units 49-52: Speed Progression
- **Unit 49:** Speed variable
- **Unit 50:** Faster as snake grows
- **Unit 51:** Maximum speed cap
- **Unit 52:** Speed display

### Units 53-56: Game States
- **Unit 53:** Title screen
- **Unit 54:** Game over screen - final score
- **Unit 55:** Play again prompt
- **Unit 56:** High score persistence

### Units 57-60: Visual Polish
- **Unit 57:** Head character - distinct
- **Unit 58:** Body character - segments
- **Unit 59:** Food variety - different looks
- **Unit 60:** Border display

### Units 61-64: Final Game
- **Unit 61:** Difficulty options - speed/wrap
- **Unit 62:** Full testing
- **Unit 63:** Code cleanup
- **Unit 64:** **RELEASE: Snake Trail complete**

**Phase Goal:** Polished snake game with all features.

---

## Summary

**Snake Trail** demonstrates array-based game programming:

### Technical Specifications

- **Display:** Character mode (40×25)
- **Play area:** Full screen or bordered
- **Input:** Four-direction keyboard
- **Max length:** 100 segments
- **Timer:** TI-based movement
- **Features:** Growth, scoring, speed progression

### Skills Learned

- Array declaration with DIM
- Array manipulation
- Circular buffer technique
- Timed game loops with TI
- Self-collision detection
- Random spawn with exclusion
- Speed/difficulty progression
- Game state management

### Array Structure

```basic
100 DIM SX(100), SY(100): REM BODY POSITIONS
110 SL = 3: REM SNAKE LENGTH
120 HD = 0: REM HEAD INDEX
130 TL = SL - 1: REM TAIL INDEX
```

### Progression

This game prepares learners for **Space Dodge** where they'll implement simulated scrolling and manage many more objects on screen, encountering BASIC's speed limits.
