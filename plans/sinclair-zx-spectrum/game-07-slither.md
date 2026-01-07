# Slither: 64-Unit Outline

**Game:** 7 of 16
**Platform:** ZX Spectrum
**Units:** 64 (4 phases)
**Concept:** Snake game. Eat food, grow longer, don't hit yourself or walls.

---

## Why This Game Seventh?

Slither introduces growing entity management - a snake that lengthens as it eats:

1. **Linked list concepts** - Head, body segments, tail
2. **Self-collision** - Can't hit your own body
3. **Grid-based movement** - Discrete steps
4. **Increasing difficulty** - Longer snake = harder game
5. **Tight game loop** - Optimised for responsiveness

A seemingly simple game with elegant data structure lessons.

---

## Skills Applied from Previous Games

| Skill | From | Application in Slither |
|-------|------|----------------------|
| Tile-based display | Cavern | Grid-based snake |
| Collision detection | All | Wall and self collision |
| Game state | All | Score, length tracking |
| Frame timing | Shatter | Movement speed |
| Input handling | All | Direction control |

## New Skills Introduced

| Skill | Phase | Description |
|-------|-------|-------------|
| Queue/ring buffer | 1 | Snake segment storage |
| Head/tail pointers | 1 | Efficient segment management |
| Self-collision | 2 | Body segment checking |
| Growth mechanics | 2 | Adding segments |
| Grid movement | 1 | Discrete step movement |
| Speed progression | 3 | Faster as game progresses |
| Obstacle mazes | 4 | Advanced level layouts |

---

## Phase 1: Snake Foundation (Units 1-16)
*Snake display and basic movement.*

### Units 1-4: Grid System
- **Unit 1:** Grid layout - play area divided into cells
- **Unit 2:** Cell rendering - drawing grid cells
- **Unit 3:** Border walls - play area boundaries
- **Unit 4:** Grid coordinates - position tracking

### Units 5-8: Snake Data Structure
- **Unit 5:** Segment concept - snake as series of positions
- **Unit 6:** Ring buffer - circular array for segments
- **Unit 7:** Head and tail pointers - track snake ends
- **Unit 8:** Snake display - draw all segments

### Units 9-12: Snake Movement
- **Unit 9:** Direction state - current movement direction
- **Unit 10:** Direction input - change direction on keypress
- **Unit 11:** Head movement - advance head in direction
- **Unit 12:** Tail removal - erase tail (constant length)

### Units 13-16: Basic Play
- **Unit 13:** Movement timing - step at regular intervals
- **Unit 14:** Wall collision - hit wall = game over
- **Unit 15:** Continuous movement - snake always moves
- **Unit 16:** Playable foundation - snake moves around grid

**Phase Goal:** Snake moves around grid with wall collision.

---

## Phase 2: Food and Growth (Units 17-32)
*Eating food and growing longer.*

### Units 17-20: Food System
- **Unit 17:** Food placement - random valid position
- **Unit 18:** Food display - distinct food graphics
- **Unit 19:** Food collision - head reaches food
- **Unit 20:** Food respawn - new food after eating

### Units 21-24: Snake Growth
- **Unit 21:** Growth flag - mark snake for growth
- **Unit 22:** Tail retention - don't remove tail when growing
- **Unit 23:** Length tracking - count segments
- **Unit 24:** Score from length - points for eating

### Units 25-28: Self-Collision
- **Unit 25:** Body collision check - head hits body?
- **Unit 26:** Efficient checking - only check body segments
- **Unit 27:** Death on self-collision - game over
- **Unit 28:** Complete collision system - walls and self

### Units 29-32: Game Flow
- **Unit 29:** Lives system - multiple attempts
- **Unit 30:** Game over detection - no lives left
- **Unit 31:** Score display - current score shown
- **Unit 32:** High score tracking - best score

**Phase Goal:** Snake eats, grows, and can collide with itself.

---

## Phase 3: Polish and Features (Units 33-48)
*Speed, sound, and enhancements.*

### Units 33-36: Speed Progression
- **Unit 33:** Base speed setting - initial movement rate
- **Unit 34:** Speed increase - faster as snake grows
- **Unit 35:** Speed tiers - discrete speed levels
- **Unit 36:** Speed cap - maximum difficulty

### Units 37-40: Sound
- **Unit 37:** Eat sound - food collected
- **Unit 38:** Turn sound - direction change
- **Unit 39:** Death sound - collision
- **Unit 40:** Speed up sound - difficulty increase

### Units 41-44: Visual Enhancements
- **Unit 41:** Snake head graphics - distinct head
- **Unit 42:** Body segment variety - patterned body
- **Unit 43:** Food animation - pulsing food
- **Unit 44:** Death animation - snake collapse

### Units 45-48: Game Modes
- **Unit 45:** Classic mode - empty arena
- **Unit 46:** Obstacle mode - walls in arena
- **Unit 47:** Bonus food - special items worth more
- **Unit 48:** Mode selection - choose game type

**Phase Goal:** Polished game with multiple modes.

---

## Phase 4: Levels and Release (Units 49-64)
*Level variety and final polish.*

### Units 49-52: Level Variety
- **Unit 49:** Level 1 - open arena
- **Unit 50:** Level 2 - central obstacles
- **Unit 51:** Level 3 - maze-like walls
- **Unit 52:** Level progression - advance on score

### Units 53-56: Advanced Features
- **Unit 53:** Wraparound mode - exit one side, enter other
- **Unit 54:** Two-player mode - competitive snakes
- **Unit 55:** Power-ups - temporary abilities
- **Unit 56:** Length target - reach length to win level

### Units 57-60: Presentation
- **Unit 57:** Title screen - game logo
- **Unit 58:** Level preview - show layout before play
- **Unit 59:** Pause functionality - pause game
- **Unit 60:** Options menu - speed, mode selection

### Units 61-64: Release
- **Unit 61:** Instructions display
- **Unit 62:** Balance testing - speed curve
- **Unit 63:** Bug fixing - edge cases
- **Unit 64:** Release build - final TAP file

**Phase Goal:** Complete snake game with variety.

---

## Summary

**Slither** teaches data structure management with a growing entity:

**Phase 1 (Foundation):** Grid, snake structure, movement.

**Phase 2 (Mechanics):** Food, growth, self-collision.

**Phase 3 (Polish):** Speed, sound, game modes.

**Phase 4 (Variety):** Levels, features, release.

### Skills Transferred Forward

1. **Ring buffer/queue** → Efficient data management
2. **Growing entities** → Trails, chains, similar mechanics
3. **Self-collision** → Complex collision scenarios
4. **Grid-based movement** → Puzzle games, discrete movement
5. **Difficulty through growth** → Organic difficulty curves

### Game Specifications

- **Grid:** 30×20 cells
- **Snake:** Starts at length 3
- **Food:** 1 on screen at a time
- **Modes:** Classic, obstacles, wraparound
- **Lives:** 3
- **Speed:** Increases with length
- **Levels:** 8 with different obstacles
- **Controls:** 4-way direction
- **Audio:** Beeper effects
- **Distribution:** TAP file
