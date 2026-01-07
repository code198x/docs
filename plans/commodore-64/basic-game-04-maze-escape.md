# Maze Escape: 64-Unit Outline

**Game:** 4 - Maze Escape
**Platform:** Commodore 64
**Language:** BASIC V2
**Units:** 64 (4 phases)
**Prerequisite:** Catcher complete
**Concept:** Navigate through a maze to reach the exit. Introduces DATA statements for level design.

---

## Overview

Maze Escape challenges players to navigate through mazes, collecting items and avoiding dead ends to reach the exit. This game introduces DATA statements for storing level layouts and four-directional movement with wall collision detection.

---

## Learning Goals

By completing Maze Escape, learners will:

- Use DATA and READ statements for level storage
- Implement two-dimensional level layouts
- Create four-directional player movement
- Build wall collision detection
- Design multiple levels
- Implement level progression
- Create a timer-based scoring system
- Use RESTORE for level reloading

---

## Phase 1: DATA and Level Loading (Units 1-16)
*Storing and displaying mazes.*

### Units 1-4: DATA Statements
- **Unit 1:** DATA statement basics - storing values
- **Unit 2:** READ statement - retrieving values
- **Unit 3:** Multiple DATA lines - sequences
- **Unit 4:** DATA types - numbers and strings

### Units 5-8: Level Format
- **Unit 5:** Maze structure - walls and paths
- **Unit 6:** Character encoding - W for wall, space for path
- **Unit 7:** Row-by-row storage in DATA
- **Unit 8:** Level dimensions - 20×20 playable area

### Units 9-12: Level Rendering
- **Unit 9:** Reading level data
- **Unit 10:** Drawing walls - POKE to screen
- **Unit 11:** Drawing paths - empty spaces
- **Unit 12:** Level display complete

### Units 13-16: Level Elements
- **Unit 13:** Player start position - marked in data
- **Unit 14:** Exit position - goal marker
- **Unit 15:** Rendering player and exit
- **Unit 16:** Phase 1 complete - maze displays correctly

**Phase Goal:** Load and display maze from DATA.

---

## Phase 2: Movement and Collision (Units 17-32)
*Navigating the maze.*

### Units 17-20: Four-Direction Input
- **Unit 17:** Up key - W or cursor up
- **Unit 18:** Down key - S or cursor down
- **Unit 19:** Left key - A or cursor left
- **Unit 20:** Right key - D or cursor right

### Units 21-24: Wall Collision
- **Unit 21:** Check before move - PEEK target cell
- **Unit 22:** Wall detection - don't allow move
- **Unit 23:** Path detection - allow move
- **Unit 24:** Collision response - player stays put

### Units 25-28: Player Movement
- **Unit 25:** Clear old position
- **Unit 26:** Update position variables
- **Unit 27:** Draw at new position
- **Unit 28:** Smooth movement feel

### Units 29-32: Exit Detection
- **Unit 29:** Check for exit position
- **Unit 30:** Level complete trigger
- **Unit 31:** Victory message
- **Unit 32:** Phase 2 complete - playable single maze

**Phase Goal:** Navigate maze with wall collision.

---

## Phase 3: Multiple Levels and Scoring (Units 33-48)
*Expanding the challenge.*

### Units 33-36: Multiple Levels
- **Unit 33:** Level 2 DATA - new maze
- **Unit 34:** Level 3 DATA - harder maze
- **Unit 35:** RESTORE statement - reset DATA pointer
- **Unit 36:** Level selection - skip to correct DATA

### Units 37-40: Level Progression
- **Unit 37:** Level variable tracking
- **Unit 38:** Load next level on completion
- **Unit 39:** Increasing difficulty
- **Unit 40:** All levels complete - game won

### Units 41-44: Timer System
- **Unit 41:** TI variable - system timer
- **Unit 42:** Start time recording
- **Unit 43:** Elapsed time calculation
- **Unit 44:** Time display - formatted output

### Units 45-48: Scoring
- **Unit 45:** Time-based score - faster is better
- **Unit 46:** Bonus points - per level
- **Unit 47:** Total score accumulation
- **Unit 48:** Phase 3 complete - multi-level game

**Phase Goal:** Multiple levels with time-based scoring.

---

## Phase 4: Collectibles and Polish (Units 49-64)
*Adding depth to gameplay.*

### Units 49-52: Collectibles
- **Unit 49:** Treasure items in maze
- **Unit 50:** Collectible DATA encoding
- **Unit 51:** Collection detection
- **Unit 52:** Points for collection

### Units 53-56: Hazards
- **Unit 53:** Hazard tiles - lose time/points
- **Unit 54:** Hazard DATA encoding
- **Unit 55:** Hazard detection
- **Unit 56:** Hazard feedback

### Units 57-60: Visual Polish
- **Unit 57:** Wall graphics - box drawing characters
- **Unit 58:** Colour coding - walls, paths, items
- **Unit 59:** Player appearance - distinct character
- **Unit 60:** HUD design - level, time, score

### Units 61-64: Final Game
- **Unit 61:** Five complete levels
- **Unit 62:** Balance and testing
- **Unit 63:** Title and game over screens
- **Unit 64:** **RELEASE: Maze Escape complete**

**Phase Goal:** Feature-complete maze game with collectibles.

---

## Summary

**Maze Escape** introduces data-driven level design:

### Technical Specifications

- **Display:** Character mode (40×25)
- **Play area:** 20×20 tiles
- **Input:** Four-direction keyboard
- **Levels:** 5 unique mazes
- **Timer:** TI-based system clock
- **Features:** Collectibles, hazards, scoring

### Skills Learned

- DATA/READ statement usage
- Level data encoding
- Two-dimensional collision detection
- Four-directional movement
- Multiple level management
- RESTORE for data navigation
- Timer-based gameplay
- Level design principles

### DATA Structure Example

```basic
1000 DATA "WWWWWWWWWWWWWWWWWWWW"
1010 DATA "W       W          W"
1020 DATA "W WWWWW W WWWWWWWW W"
...
1190 DATA "WWWWWWWWWWWWWWWWWWWE"
```

### Progression

This game prepares learners for **Snake Trail** where they'll use arrays to track a growing snake body and implement self-collision detection.
