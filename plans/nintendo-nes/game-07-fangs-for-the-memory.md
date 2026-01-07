# Fangs for the Memory: 64-Unit Outline

**Game:** 7 of 16
**Platform:** Nintendo Entertainment System
**Units:** 64 (4 phases)
**Concept:** Snake game with a twist. Control a growing creature, eat food, don't bite yourself. The name's a pun - you'll remember it.

---

## Why This Game Seventh?

Fangs for the Memory introduces growing entity management:

1. **Ring buffer** - Efficient segment storage
2. **Head/tail pointers** - Track snake ends
3. **Self-collision** - Body segment checking
4. **Growth mechanics** - Adding segments
5. **Grid movement** - Discrete steps

A simple-looking game with elegant data structure lessons.

---

## Skills Applied from Previous Games

| Skill | From | Application in Fangs |
|-------|------|---------------------|
| Tile display | All | Grid-based playfield |
| Controller input | All | Direction control |
| Collision detection | All | Wall and self collision |
| Game state | All | Score, length tracking |

## New Skills Introduced

| Skill | Phase | Description |
|-------|-------|-------------|
| Ring buffer | 1 | Circular array for segments |
| Head/tail pointers | 1 | Efficient segment management |
| Grid movement | 1 | Discrete step movement |
| Self-collision | 2 | Body segment checking |
| Growth mechanics | 2 | Extending the snake |
| Speed progression | 3 | Faster as game progresses |

---

## Phase 1: Snake Foundation (Units 1-16)
*Snake display and basic movement.*

### Units 1-4: Grid System
- **Unit 1:** Grid layout - play area cells
- **Unit 2:** Cell rendering - drawing grid
- **Unit 3:** Border walls - boundaries
- **Unit 4:** Grid coordinates - position tracking

### Units 5-8: Snake Data Structure
- **Unit 5:** Segment concept - positions array
- **Unit 6:** Ring buffer - circular array
- **Unit 7:** Head and tail pointers - track ends
- **Unit 8:** Snake display - draw all segments

### Units 9-12: Snake Movement
- **Unit 9:** Direction state - current direction
- **Unit 10:** Direction input - change on keypress
- **Unit 11:** Head movement - advance head
- **Unit 12:** Tail removal - erase tail (constant length)

### Units 13-16: Basic Play
- **Unit 13:** Movement timing - step at intervals
- **Unit 14:** Wall collision - game over
- **Unit 15:** Continuous movement - always moving
- **Unit 16:** Playable foundation - snake moves around

**Phase Goal:** Snake moves around grid.

---

## Phase 2: Food and Growth (Units 17-32)
*Eating food and growing longer.*

### Units 17-20: Food System
- **Unit 17:** Food placement - random valid position
- **Unit 18:** Food display - distinct graphics
- **Unit 19:** Food collision - head reaches food
- **Unit 20:** Food respawn - new food after eating

### Units 21-24: Snake Growth
- **Unit 21:** Growth flag - mark for growth
- **Unit 22:** Tail retention - don't remove when growing
- **Unit 23:** Length tracking - count segments
- **Unit 24:** Score from length - points for eating

### Units 25-28: Self-Collision
- **Unit 25:** Body collision check - head hits body?
- **Unit 26:** Efficient checking - scan body segments
- **Unit 27:** Death on self-collision - game over
- **Unit 28:** Complete collision - walls and self

### Units 29-32: Game Flow
- **Unit 29:** Lives system - multiple attempts
- **Unit 30:** Game over - no lives left
- **Unit 31:** Score display - current score
- **Unit 32:** High score - best score

**Phase Goal:** Snake eats, grows, self-collision.

---

## Phase 3: Features and Modes (Units 33-48)
*Speed, sound, and game modes.*

### Units 33-36: Speed Progression
- **Unit 33:** Base speed - initial rate
- **Unit 34:** Speed increase - faster with growth
- **Unit 35:** Speed tiers - discrete levels
- **Unit 36:** Speed cap - maximum difficulty

### Units 37-40: Sound
- **Unit 37:** Eat sound - food collected
- **Unit 38:** Turn sound - direction change
- **Unit 39:** Death sound - collision
- **Unit 40:** Speed up sound - difficulty increase

### Units 41-44: Visual Enhancements
- **Unit 41:** Snake head graphics - distinct head
- **Unit 42:** Body segment variety - pattern
- **Unit 43:** Food animation - pulsing
- **Unit 44:** Death animation - collapse

### Units 45-48: Game Modes
- **Unit 45:** Classic mode - empty arena
- **Unit 46:** Obstacle mode - walls in arena
- **Unit 47:** Bonus food - special items
- **Unit 48:** Mode selection - choose type

**Phase Goal:** Polished game with modes.

---

## Phase 4: Levels and Release (Units 49-64)
*Level variety and polish.*

### Units 49-52: Level Layouts
- **Unit 49:** Level 1 - open arena
- **Unit 50:** Level 2 - central obstacles
- **Unit 51:** Level 3 - maze walls
- **Unit 52:** Level progression - advance on score

### Units 53-56: Advanced Features
- **Unit 53:** Wraparound mode - screen edges connect
- **Unit 54:** Two-player mode - competitive
- **Unit 55:** Power-ups - temporary abilities
- **Unit 56:** Length targets - reach length to win

### Units 57-60: Presentation
- **Unit 57:** Title screen - game logo
- **Unit 58:** Level preview - show layout
- **Unit 59:** Pause - pause game
- **Unit 60:** Options - settings

### Units 61-64: Release
- **Unit 61:** Instructions display
- **Unit 62:** Balance testing - speed curve
- **Unit 63:** Bug fixing - edge cases
- **Unit 64:** Release build - final iNES ROM

**Phase Goal:** Complete snake game.

---

## Summary

**Fangs for the Memory** teaches data structure management:

**Phase 1 (Foundation):** Grid, ring buffer, movement.

**Phase 2 (Mechanics):** Food, growth, self-collision.

**Phase 3 (Features):** Speed, sound, modes.

**Phase 4 (Levels):** Variety, release.

### Skills Transferred Forward

1. **Ring buffer** → Efficient data management
2. **Growing entities** → Trails, chains
3. **Self-collision** → Complex collision
4. **Grid movement** → Puzzle games
5. **Speed progression** → Difficulty curves

### Game Specifications

- **Grid:** 30×26 cells
- **Snake:** Starts at length 3
- **Food:** 1 on screen
- **Modes:** Classic, obstacles, wraparound
- **Lives:** 3
- **Speed:** Increases with length
- **Mapper:** NROM
- **ROM Size:** 16KB PRG + 8KB CHR
- **Controls:** D-pad
- **Audio:** APU effects
- **Distribution:** iNES ROM file
