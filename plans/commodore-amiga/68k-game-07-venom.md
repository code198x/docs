# Venom: 64-Unit Outline

**Game:** 7 of 16 (68000 Assembly)
**Platform:** Commodore Amiga
**Language:** 68000 Assembly
**Units:** 64 (4 phases)
**Concept:** Snake game with ring buffer data structure.

---

## Why This Game Seventh?

Venom introduces efficient data structures:

1. **Ring buffer** - Circular array for snake body
2. **Grid-based movement** - Discrete positioning
3. **Self-collision** - Complex detection
4. **Growth mechanics** - Dynamic length
5. **Multiple modes** - Variety of play

A programming-focused game with elegant solutions.

---

## Skills Applied from Previous Games

| Skill | From | Application |
|-------|------|-------------|
| Tile rendering | Crypt/Gobble | Snake segments |
| Grid movement | Gobble | Movement system |
| Collision | All | Walls, self |
| Blitter operations | All | Segment drawing |
| Game states | All | Modes |

## New Skills Introduced

| Skill | Phase | Description |
|-------|-------|-------------|
| Ring buffer | 1 | Efficient snake storage |
| Circular array | 1 | Wrap-around indexing |
| Self-collision | 2 | Body detection |
| Dynamic sizing | 2 | Growth handling |
| Speed scaling | 3 | Difficulty curve |

---

## Phase 1: Snake Movement (Units 1-16)
*Ring buffer and basic movement.*

### Units 1-4: Ring Buffer
- **Unit 1:** Ring buffer concept - circular array
- **Unit 2:** Head/tail pointers - tracking
- **Unit 3:** Adding elements - move head
- **Unit 4:** Removing elements - move tail

### Units 5-8: Snake Data
- **Unit 5:** Segment structure - X, Y position
- **Unit 6:** Snake array - fixed max length
- **Unit 7:** Length tracking - current size
- **Unit 8:** Initial snake - 3 segments

### Units 9-12: Movement
- **Unit 9:** Direction state - up/down/left/right
- **Unit 10:** Grid movement - tile steps
- **Unit 11:** New head position - from direction
- **Unit 12:** Move snake - add head, remove tail

### Units 13-16: Snake Display
- **Unit 13:** Segment sprite - body tile
- **Unit 14:** Head sprite - different appearance
- **Unit 15:** Drawing snake - all segments
- **Unit 16:** Movement demo - moving snake

**Phase Goal:** Moving snake with ring buffer.

---

## Phase 2: Collision and Growth (Units 17-32)
*Self-collision and food.*

### Units 17-20: Wall Collision
- **Unit 17:** Boundary walls - arena edges
- **Unit 18:** Wall detection - head check
- **Unit 19:** Wall collision - death
- **Unit 20:** Wall variation - obstacles

### Units 21-24: Self-Collision
- **Unit 21:** Self-collision concept - hit own body
- **Unit 22:** Body scan - check all segments
- **Unit 23:** Efficient detection - skip recent
- **Unit 24:** Self-collision death

### Units 25-28: Food System
- **Unit 25:** Food sprite - apple/pellet
- **Unit 26:** Food placement - random empty
- **Unit 27:** Food collision - eat
- **Unit 28:** New food spawn

### Units 29-32: Growth Mechanics
- **Unit 29:** Growth concept - don't remove tail
- **Unit 30:** Growth amount - per food
- **Unit 31:** Length increase - ring buffer
- **Unit 32:** Growth demo - eating and growing

**Phase Goal:** Snake eating and growing.

---

## Phase 3: Game Features (Units 33-48)
*Scoring, speed, levels.*

### Units 33-36: Scoring
- **Unit 33:** Points per food - base value
- **Unit 34:** Length bonus - longer = more
- **Unit 35:** Speed bonus - faster = more
- **Unit 36:** Score display - Blitter text

### Units 37-40: Speed System
- **Unit 37:** Base speed - initial
- **Unit 38:** Speed increase - with length
- **Unit 39:** Speed caps - maximum
- **Unit 40:** Speed display - indicator

### Units 41-44: Level Design
- **Unit 41:** Arena shapes - open, walled
- **Unit 42:** Obstacle patterns - internal walls
- **Unit 43:** Level progression - complete at length
- **Unit 44:** Level variety - 10+ arenas

### Units 45-48: Special Food
- **Unit 45:** Bonus food - temporary spawn
- **Unit 46:** Bonus points - high value
- **Unit 47:** Bonus timing - disappears
- **Unit 48:** Food variety - different types

**Phase Goal:** Levels and scoring.

---

## Phase 4: Modes and Polish (Units 49-64)
*Game modes and completion.*

### Units 49-52: Game Modes
- **Unit 49:** Classic mode - standard play
- **Unit 50:** Survival mode - endless, speed up
- **Unit 51:** Puzzle mode - specific targets
- **Unit 52:** Mode selection - menu

### Units 53-56: Two-Player
- **Unit 53:** Second snake - different colour
- **Unit 54:** Separate controls - P1/P2
- **Unit 55:** Snake collision - with each other
- **Unit 56:** Versus scoring

### Units 57-60: Audio
- **Unit 57:** Movement sound - subtle
- **Unit 58:** Eat sound - crunch
- **Unit 59:** Death sound - splat
- **Unit 60:** Background music

### Units 61-64: Release
- **Unit 61:** High score table
- **Unit 62:** Title screen
- **Unit 63:** Full testing
- **Unit 64:** Release build - ADF

**Phase Goal:** Complete snake game.

---

## Summary

**Venom** teaches ring buffers and efficient data structures.

### Technical Specifications

- **Display:** 320×256, 5 bitplanes
- **Snake:** Ring buffer, max 100+ segments
- **Arena:** Tile-based, various layouts
- **Food:** Random placement, bonus types
- **Speed:** Scales with length
- **Modes:** Classic, survival, puzzle, versus
- **Players:** 1-2
- **Distribution:** Bootable ADF

### Skills for Next Game

- Ring buffer implementation
- Self-collision detection
- Dynamic growth mechanics
- Speed scaling systems
- Multiple game modes
