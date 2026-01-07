# Gobble: 64-Unit Outline

**Game:** 6 of 16 (68000 Assembly)
**Platform:** Commodore Amiga
**Language:** 68000 Assembly
**Units:** 64 (4 phases)
**Concept:** Pac-Man style maze game with ghost AI personalities.

---

## Why This Game Sixth?

Gobble deepens AI and tile-based design:

1. **Ghost AI personalities** - Different behaviours
2. **Constrained movement** - Corridor navigation
3. **State machines** - Enemy modes
4. **Copper screen wrap** - Tunnel effect
5. **Speed progression** - Difficulty scaling

Builds on Crypt's tile system with sophisticated AI.

---

## Skills Applied from Previous Games

| Skill | From | Application |
|-------|------|-------------|
| Tile rendering | Crypt | Maze display |
| Chase AI | Crypt | Ghost following |
| Collision | All | Wall detection |
| State management | Crypt | Game modes |
| Blitter operations | All | Graphics |

## New Skills Introduced

| Skill | Phase | Description |
|-------|-------|-------------|
| AI personalities | 2 | Different ghosts |
| State machines | 3 | Scatter/chase/frightened |
| Copper wrap | 2 | Screen tunnels |
| Constrained movement | 1 | Grid corridors |
| Audio cues | 4 | Gameplay feedback |

---

## Phase 1: Maze Foundation (Units 1-16)
*Maze rendering and player movement.*

### Units 1-4: Maze Structure
- **Unit 1:** Maze data - wall/path grid
- **Unit 2:** Tile types - wall, path, dot, power
- **Unit 3:** Maze rendering - Blitter tiles
- **Unit 4:** Maze display - full screen

### Units 5-8: Maze Design
- **Unit 5:** Classic layout - Pac-Man inspired
- **Unit 6:** Ghost house - spawn area
- **Unit 7:** Tunnels - side exits
- **Unit 8:** Dot placement - fill paths

### Units 9-12: Constrained Movement
- **Unit 9:** Grid position - tile coordinates
- **Unit 10:** Direction input - queued
- **Unit 11:** Turn validation - wall check
- **Unit 12:** Smooth movement - pixel interpolation

### Units 13-16: Player Character
- **Unit 13:** Pac-man sprite - design
- **Unit 14:** Mouth animation - open/close
- **Unit 15:** Direction facing - rotation
- **Unit 16:** Movement demo - navigating maze

**Phase Goal:** Player moving in maze.

---

## Phase 2: Ghosts and Screen Wrap (Units 17-32)
*Ghost display and tunnel effect.*

### Units 17-20: Ghost Basics
- **Unit 17:** Ghost sprites - 4 colours
- **Unit 18:** Ghost array - tracking
- **Unit 19:** Ghost rendering - BOBs
- **Unit 20:** Ghost animation - wobble

### Units 21-24: Copper Screen Wrap
- **Unit 21:** Tunnel concept - exit/enter sides
- **Unit 22:** Copper trick - scroll register
- **Unit 23:** Wrap detection - screen edge
- **Unit 24:** Wrap rendering - seamless

### Units 25-28: Ghost Movement
- **Unit 25:** Ghost house exit - one at a time
- **Unit 26:** Exit timing - staggered
- **Unit 27:** Ghost paths - in corridors
- **Unit 28:** Ghost at intersections

### Units 29-32: AI Foundations
- **Unit 29:** Target tile - where ghost goes
- **Unit 30:** Path to target - direction choice
- **Unit 31:** No reverse - can't turn 180
- **Unit 32:** Ghost demo - moving in maze

**Phase Goal:** Ghosts moving in maze.

---

## Phase 3: AI Personalities (Units 33-48)
*Different ghost behaviours.*

### Units 33-36: Ghost Modes
- **Unit 33:** Mode concept - scatter, chase
- **Unit 34:** Mode timers - switching
- **Unit 35:** Frightened mode - power pellet
- **Unit 36:** Mode transitions - immediate

### Units 37-40: Individual AI
- **Unit 37:** Blinky (red) - direct chase
- **Unit 38:** Pinky (pink) - ambush ahead
- **Unit 39:** Inky (cyan) - complex targeting
- **Unit 40:** Clyde (orange) - shy/random

### Units 41-44: Scatter Behaviour
- **Unit 41:** Scatter targets - corners
- **Unit 42:** Blinky corner - top right
- **Unit 43:** Other corners - assigned
- **Unit 44:** Scatter timing - periodic

### Units 45-48: Frightened State
- **Unit 45:** Power pellet - trigger
- **Unit 46:** Ghost reversal - turn around
- **Unit 47:** Ghost colour change - blue
- **Unit 48:** Ghost eating - points

**Phase Goal:** Four distinct ghost AIs.

---

## Phase 4: Game Features (Units 49-64)
*Dot collection and completion.*

### Units 49-52: Dot Collection
- **Unit 49:** Dot collision - eat on contact
- **Unit 50:** Dot removal - update maze
- **Unit 51:** Dot counting - level complete
- **Unit 52:** Score per dot - 10 points

### Units 53-56: Audio
- **Unit 53:** Wakka sound - continuous
- **Unit 54:** Ghost eat sound
- **Unit 55:** Death sound
- **Unit 56:** Siren - background

### Units 57-60: Level Progression
- **Unit 57:** Level complete - all dots
- **Unit 58:** Speed increase - per level
- **Unit 59:** Bonus fruit - spawn
- **Unit 60:** Intermissions - cutscenes

### Units 61-64: Release
- **Unit 61:** Lives display
- **Unit 62:** High score system
- **Unit 63:** Full testing
- **Unit 64:** Release build - ADF

**Phase Goal:** Complete maze game.

---

## Summary

**Gobble** teaches AI personalities and state machines.

### Technical Specifications

- **Display:** 320×256, 5 bitplanes
- **Player:** Animated BOB, 4-directional
- **Maze:** Tile-based, Blitter-rendered
- **Ghosts:** 4 with unique AI
- **Dots:** 240+ per level
- **Modes:** Scatter, chase, frightened
- **Screen wrap:** Copper effect
- **Distribution:** Bootable ADF

### Skills for Next Game

- AI personality systems
- State machine design
- Constrained grid movement
- Copper screen effects
- Audio cues for gameplay
