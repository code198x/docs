# Chomp: 64-Unit Outline

**Game:** 6 of 16
**Platform:** ZX Spectrum
**Units:** 64 (4 phases)
**Concept:** Pac-Man style maze game. Collect dots, avoid ghosts, eat power pills to turn the tables.

---

## Why This Game Sixth?

Chomp introduces constrained movement and enemy AI with personality - ghosts that behave differently:

1. **Maze constraints** - Movement limited to corridors
2. **Enemy personalities** - Different AI for each ghost
3. **State changes** - Power pills reverse hunter/hunted
4. **Wrap-around** - Screen edge looping
5. **Level progression** - Increasing speed/difficulty

This teaches more sophisticated AI than simple chase behaviour.

---

## Skills Applied from Previous Games

| Skill | From | Application in Chomp |
|-------|------|---------------------|
| Tile-based levels | Cavern | Maze structure |
| Collision detection | All | Wall and ghost collision |
| Object arrays | Skyfire | Ghost management |
| Chase AI | Chambers | Ghost behaviour base |
| Frame timing | Shatter | Speed control |
| Persistent state | Chambers | Score, level tracking |

## New Skills Introduced

| Skill | Phase | Description |
|-------|-------|-------------|
| Constrained movement | 1 | Movement only in valid directions |
| Maze pathfinding | 2 | Finding valid routes |
| AI personalities | 2 | Different behaviour per enemy |
| Scatter/chase modes | 3 | AI state machines |
| Screen wrapping | 2 | Edge-to-edge movement |
| Frightened mode | 3 | Reversed behaviour |
| Speed progression | 4 | Difficulty scaling |

---

## Phase 1: Maze Foundation (Units 1-16)
*Maze display and player movement.*

### Units 1-4: Maze Structure
- **Unit 1:** Maze data format - walls, corridors, dots, power pills
- **Unit 2:** Maze tile graphics - wall pieces, corners, dots
- **Unit 3:** Maze display routine - render complete maze
- **Unit 4:** Attribute colouring - distinctive maze look

### Units 5-8: Player Character
- **Unit 5:** Pac-Man sprite - mouth animation frames
- **Unit 6:** Direction-based animation - face movement direction
- **Unit 7:** Player positioning - centred in corridor
- **Unit 8:** Smooth movement - pixel-level scrolling within maze

### Units 9-12: Constrained Movement
- **Unit 9:** Valid direction checking - can move this way?
- **Unit 10:** Direction input - keyboard controls
- **Unit 11:** Queued direction - buffer next turn
- **Unit 12:** Cornering - smooth turns at junctions

### Units 13-16: Dot Collection
- **Unit 13:** Dot collision detection - player on dot
- **Unit 14:** Dot removal - erase collected dot
- **Unit 15:** Dot counter - track remaining dots
- **Unit 16:** Score increment - points per dot

**Phase Goal:** Navigate maze and collect dots.

---

## Phase 2: Ghosts and AI (Units 17-32)
*Ghost movement and behaviour.*

### Units 17-20: Ghost Basics
- **Unit 17:** Ghost sprites - 4 distinct ghost designs
- **Unit 18:** Ghost data structure - position, direction, mode
- **Unit 19:** Ghost movement - smooth corridor navigation
- **Unit 20:** Ghost collision - player death on contact

### Units 21-24: AI Foundations
- **Unit 21:** Target tile concept - ghost aims for a tile
- **Unit 22:** Direction decision - choose direction toward target
- **Unit 23:** No reverse rule - ghosts can't turn back
- **Unit 24:** Four ghosts active - all ghosts moving

### Units 25-28: Ghost Personalities
- **Unit 25:** Blinky (red) - directly chases player
- **Unit 26:** Pinky (pink) - targets ahead of player
- **Unit 27:** Inky (cyan) - complex targeting using Blinky
- **Unit 28:** Clyde (orange) - chase or scatter based on distance

### Units 29-32: Screen Wrapping
- **Unit 29:** Tunnel detection - side exits in maze
- **Unit 30:** Player wrap - exit right, enter left
- **Unit 31:** Ghost wrap - slower in tunnel
- **Unit 32:** Complete navigation - full maze access

**Phase Goal:** Four ghosts with distinct AI personalities.

---

## Phase 3: Game Modes (Units 33-48)
*Power pills, scatter mode, and game flow.*

### Units 33-36: Power Pills
- **Unit 33:** Power pill placement - corner positions
- **Unit 34:** Power pill collection - trigger frightened mode
- **Unit 35:** Frightened state - ghosts reverse, turn blue
- **Unit 36:** Ghost vulnerability - player can eat ghosts

### Units 37-40: Scatter Mode
- **Unit 37:** Mode timer - alternate chase and scatter
- **Unit 38:** Scatter targets - ghosts head to corners
- **Unit 39:** Mode transitions - switching behaviour
- **Unit 40:** Complete AI cycle - scatter/chase/frightened

### Units 41-44: Lives and Respawn
- **Unit 41:** Lives system - 3 lives
- **Unit 42:** Death sequence - player caught animation
- **Unit 43:** Ghost respawn - return to pen after eaten
- **Unit 44:** Level restart - positions reset on death

### Units 45-48: Level Completion
- **Unit 45:** All dots collected - level clear
- **Unit 46:** Level transition - flash maze, reset
- **Unit 47:** Fruit bonus - bonus items appear
- **Unit 48:** Score multiplier - ghost eating combos

**Phase Goal:** Complete Pac-Man mechanics with power pills and modes.

---

## Phase 4: Polish and Release (Units 49-64)
*Difficulty progression and presentation.*

### Units 49-52: Difficulty Progression
- **Unit 49:** Speed increase - faster each level
- **Unit 50:** Frightened duration decrease - shorter power time
- **Unit 51:** Ghost behaviour tightening - smarter targeting
- **Unit 52:** Level variety - different maze layouts (optional)

### Units 53-56: Audio
- **Unit 53:** Waka-waka sound - dot eating
- **Unit 54:** Power pill sound - mode change
- **Unit 55:** Ghost eaten sound - score feedback
- **Unit 56:** Death sound - game over jingle

### Units 57-60: Presentation
- **Unit 57:** Title screen - game logo
- **Unit 58:** Ready message - level start
- **Unit 59:** Intermissions - cutscenes between levels
- **Unit 60:** High score display - top scores

### Units 61-64: Release
- **Unit 61:** Instructions screen
- **Unit 62:** AI tuning - ghost behaviour balance
- **Unit 63:** Speed balancing - fair difficulty curve
- **Unit 64:** Release build - final TAP file

**Phase Goal:** Complete, polished maze chase game.

---

## Summary

**Chomp** teaches sophisticated enemy AI and game state management:

**Phase 1 (Maze):** Constrained movement, dot collection.

**Phase 2 (Ghosts):** Four distinct AI personalities.

**Phase 3 (Modes):** Power pills, scatter/chase cycles.

**Phase 4 (Polish):** Difficulty scaling, presentation.

### Skills Transferred Forward

1. **Constrained pathfinding** → Maze-based games
2. **AI personalities** → Enemy variety throughout
3. **State machine AI** → Complex enemy behaviour
4. **Screen wrapping** → Various game mechanics
5. **Mode transitions** → Game state management
6. **Difficulty curves** → All games with progression

### Game Specifications

- **Maze:** 28×31 tiles (classic proportions)
- **Dots:** 240 per maze
- **Power Pills:** 4 per maze
- **Ghosts:** 4 with distinct AI
- **Lives:** 3
- **Bonus Fruit:** Cherry, strawberry, etc.
- **Levels:** Increasing speed, shorter power time
- **Controls:** 4-way movement
- **Audio:** Beeper effects
- **Distribution:** TAP file
