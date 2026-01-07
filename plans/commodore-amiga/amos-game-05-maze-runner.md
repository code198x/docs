# Maze Runner: 64-Unit Outline

**Game:** 5 of 8 (AMOS BASIC)
**Platform:** Commodore Amiga
**Language:** AMOS BASIC
**Units:** 64 (4 phases)
**Concept:** Pac-Man style maze game. Collect items, avoid enemies, use power-ups.

---

## Why This Game Fifth?

Maze Runner introduces tile-based design:

1. **Tile rendering** - PASTE BOB for mazes
2. **Constrained movement** - Corridor navigation
3. **AI behaviours** - Ghost personalities
4. **State machines** - Enemy modes
5. **Banks** - AMOS data storage

Builds on bob rendering and state management.

---

## Skills Applied from Previous Games

| Skill | From | Application in Maze Runner |
|-------|------|---------------------------|
| Bob rendering | Crate Stack | Maze tiles |
| Collision | All | Wall/ghost detection |
| Animation | Space Swarm | Character animation |
| Power-ups | Bounce Back | Ghost vulnerability |
| State machines | All | Enemy behaviour |

## New Skills Introduced

| Skill | Phase | Description |
|-------|-------|-------------|
| Tile-based maps | 1 | Maze structure |
| PASTE BOB grids | 1 | Efficient rendering |
| Constrained movement | 2 | Corridor navigation |
| AI personalities | 3 | Different behaviours |
| AMOS Banks | 4 | Data organisation |

---

## Phase 1: Maze Foundation (Units 1-16)
*Tile-based maze rendering.*

### Units 1-4: Maze Data
- **Unit 1:** Tile concept - grid-based design
- **Unit 2:** Maze array - 2D data structure
- **Unit 3:** Tile types - wall, path, dot, power
- **Unit 4:** Maze data - DATA statements

### Units 5-8: Tile Rendering
- **Unit 5:** Tile bobs - wall, path graphics
- **Unit 6:** PASTE BOB - drawing tiles
- **Unit 7:** Maze rendering - full maze
- **Unit 8:** Rendering optimisation

### Units 9-12: Maze Design
- **Unit 9:** Classic layout - Pac-Man inspired
- **Unit 10:** Tunnels - screen wrap paths
- **Unit 11:** Ghost house - enemy spawn
- **Unit 12:** Dot placement - collectibles

### Units 13-16: Display
- **Unit 13:** Maze colours - walls, paths
- **Unit 14:** Score area - outside maze
- **Unit 15:** Lives display - remaining
- **Unit 16:** Maze foundation complete

**Phase Goal:** Rendered maze display.

---

## Phase 2: Player Movement (Units 17-32)
*Constrained corridor navigation.*

### Units 17-20: Grid Movement
- **Unit 17:** Tile-based position - grid coordinates
- **Unit 18:** Movement direction - up/down/left/right
- **Unit 19:** Move validation - check for wall
- **Unit 20:** Smooth movement - pixel interpolation

### Units 21-24: Turning
- **Unit 21:** Input buffering - queue next direction
- **Unit 22:** Turn at junction - when possible
- **Unit 23:** Pre-turning - anticipate junction
- **Unit 24:** Movement feel - responsive

### Units 25-28: Player Animation
- **Unit 25:** Character sprite - pac-man style
- **Unit 26:** Mouth animation - open/close
- **Unit 27:** Direction facing - rotate sprite
- **Unit 28:** Death animation - sequence

### Units 29-32: Dot Collection
- **Unit 29:** Dot collision - player on dot
- **Unit 30:** Dot removal - update maze
- **Unit 31:** Score increase - points per dot
- **Unit 32:** Sound effect - chomp

**Phase Goal:** Player navigating maze, eating dots.

---

## Phase 3: Enemy AI (Units 33-48)
*Ghost behaviours and states.*

### Units 33-36: Basic Ghosts
- **Unit 33:** Ghost sprites - 4 colours
- **Unit 34:** Ghost positioning - start in house
- **Unit 35:** Ghost exit - leave ghost house
- **Unit 36:** Ghost array - tracking all

### Units 37-40: Ghost Modes
- **Unit 37:** Chase mode - pursue player
- **Unit 38:** Scatter mode - patrol corner
- **Unit 39:** Frightened mode - flee player
- **Unit 40:** Mode timers - switch between

### Units 41-44: AI Personalities
- **Unit 41:** Blinky - direct chase
- **Unit 42:** Pinky - ambush ahead
- **Unit 43:** Inky - unpredictable
- **Unit 44:** Clyde - random/shy

### Units 45-48: Ghost Interactions
- **Unit 45:** Power pellet - frighten all
- **Unit 46:** Ghost collision - normal = death
- **Unit 47:** Ghost eating - frightened = points
- **Unit 48:** Ghost respawn - return to house

**Phase Goal:** Four ghosts with AI.

---

## Phase 4: Game Features (Units 49-64)
*Levels, audio, polish.*

### Units 49-52: Level Progression
- **Unit 49:** Level complete - all dots gone
- **Unit 50:** Level transition - reset maze
- **Unit 51:** Speed increase - per level
- **Unit 52:** AMOS Banks - level storage

### Units 53-56: Bonus Features
- **Unit 53:** Fruit spawn - bonus item
- **Unit 54:** Fruit types - by level
- **Unit 55:** Bonus points - fruit values
- **Unit 56:** Bonus timing - appear/disappear

### Units 57-60: Presentation
- **Unit 57:** Title screen - game logo
- **Unit 58:** Ready screen - level start
- **Unit 59:** Sound effects - complete set
- **Unit 60:** Background music - maze theme

### Units 61-64: Completion
- **Unit 61:** High score system
- **Unit 62:** Two-player alternating
- **Unit 63:** Full testing
- **Unit 64:** Release build

**Phase Goal:** Complete maze game.

---

## Summary

**Maze Runner** teaches tile-based design and AI.

### Game Specifications

- **Player:** Animated character, 4-directional
- **Maze:** Tile-based, bob-rendered
- **Dots:** Regular (10pts) + power (50pts)
- **Ghosts:** 4 with unique AI personalities
- **Modes:** Chase, scatter, frightened
- **Fruit:** Bonus items per level
- **Levels:** Increasing speed
- **Lives:** 3
- **Display:** AMOS screen, sprites + bobs
- **Sound:** Chomp, ghost sounds, music
- **Distribution:** AMOS source + compiled
