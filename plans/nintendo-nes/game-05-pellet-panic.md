# Pellet Panic: 64-Unit Outline

**Game:** 5 of 16
**Platform:** Nintendo Entertainment System
**Units:** 64 (4 phases)
**Concept:** Pac-Man style maze game. Collect pellets, avoid ghosts, power pills turn the tables. Frantic energy.

---

## Why This Game Fifth?

Pellet Panic introduces constrained movement and AI personalities:

1. **Maze navigation** - Movement limited to corridors
2. **AI personalities** - Each ghost behaves differently
3. **State changes** - Power pills reverse hunter/hunted
4. **Screen wrap** - Edge-to-edge movement
5. **Chase and scatter** - AI mode switching

This teaches sophisticated AI beyond simple chase behaviour.

---

## Skills Applied from Previous Games

| Skill | From | Application in Pellet Panic |
|-------|------|-----------------------------|
| Tile collision | Crate Escape | Maze walls |
| Object arrays | Stellar Barrage | Ghost management |
| Background modification | Fracture Point | Pellet removal |
| Animation | All | Player and ghost sprites |

## New Skills Introduced

| Skill | Phase | Description |
|-------|-------|-------------|
| Constrained movement | 1 | Corridor-only movement |
| Direction queuing | 1 | Buffer next turn |
| AI personalities | 2 | Different targeting per ghost |
| Scatter/chase modes | 3 | AI state machines |
| Frightened mode | 3 | Reversed behaviour |
| Screen wrapping | 2 | Exit one side, enter other |

---

## Phase 1: Maze Navigation (Units 1-16)
*Maze display and player movement.*

### Units 1-4: Maze Structure
- **Unit 1:** Maze data format - walls, corridors, pellets
- **Unit 2:** Tile types - wall, corridor, pellet, power pill
- **Unit 3:** Maze rendering - nametable setup
- **Unit 4:** Attribute colouring - maze appearance

### Units 5-8: Player Character
- **Unit 5:** Pac-Man sprite - mouth animation
- **Unit 6:** Direction-based display - face movement direction
- **Unit 7:** Animation frames - 2-frame mouth cycle
- **Unit 8:** Player on maze - positioned in corridor

### Units 9-12: Constrained Movement
- **Unit 9:** Valid direction check - can move this way?
- **Unit 10:** Tile-based movement - snap to grid
- **Unit 11:** Direction input - read D-pad
- **Unit 12:** Queued direction - buffer next turn

### Units 13-16: Smooth Movement
- **Unit 13:** Sub-tile positioning - smooth between tiles
- **Unit 14:** Turn at intersections - change direction
- **Unit 15:** Cornering - smooth turn execution
- **Unit 16:** Controllable player - navigate maze smoothly

**Phase Goal:** Smooth maze navigation.

---

## Phase 2: Ghosts and Collection (Units 17-32)
*Ghosts and pellet collection.*

### Units 17-20: Pellet Collection
- **Unit 17:** Pellet detection - player on pellet tile
- **Unit 18:** Pellet removal - update nametable
- **Unit 19:** Pellet counter - track remaining
- **Unit 20:** Score increment - points per pellet

### Units 21-24: Ghost Basics
- **Unit 21:** Ghost sprites - 4 distinct designs
- **Unit 22:** Ghost data - position, direction, mode
- **Unit 23:** Ghost movement - corridor navigation
- **Unit 24:** Ghost display - render all ghosts

### Units 25-28: Ghost AI Foundation
- **Unit 25:** Target tile concept - where ghost wants to go
- **Unit 26:** Direction decision - choose toward target
- **Unit 27:** No reverse rule - ghosts can't turn back
- **Unit 28:** Basic chase - target player position

### Units 29-32: Screen Wrapping
- **Unit 29:** Tunnel positions - side exits
- **Unit 30:** Player wrap - exit and enter opposite
- **Unit 31:** Ghost wrap - also wraps (slower)
- **Unit 32:** Complete navigation - full maze access

**Phase Goal:** Ghosts chase player through maze.

---

## Phase 3: AI Personalities and Modes (Units 33-48)
*Ghost personalities and power pills.*

### Units 33-36: Ghost Personalities
- **Unit 33:** Blinky (red) - direct chase
- **Unit 34:** Pinky (pink) - targets ahead of player
- **Unit 35:** Inky (cyan) - uses Blinky's position
- **Unit 36:** Clyde (orange) - chase or scatter by distance

### Units 37-40: Power Pills
- **Unit 37:** Power pill tiles - large dots
- **Unit 38:** Power pill collection - trigger mode change
- **Unit 39:** Frightened mode - ghosts turn blue
- **Unit 40:** Ghost vulnerability - can be eaten

### Units 41-44: Scatter Mode
- **Unit 41:** Mode timer - alternating modes
- **Unit 42:** Scatter targets - corner positions
- **Unit 43:** Mode transitions - behaviour switches
- **Unit 44:** Complete AI cycle - scatter/chase/frightened

### Units 45-48: Lives and Death
- **Unit 45:** Ghost collision - player death
- **Unit 46:** Death animation - player shrinks
- **Unit 47:** Lives system - multiple attempts
- **Unit 48:** Respawn - reset positions

**Phase Goal:** Full Pac-Man-style AI.

---

## Phase 4: Polish and Release (Units 49-64)
*Audio, presentation, and release.*

### Units 49-52: Audio
- **Unit 49:** Waka-waka sound - pellet eating
- **Unit 50:** Power pill sound - mode change
- **Unit 51:** Ghost eaten sound - score feedback
- **Unit 52:** Death sound - player caught

### Units 53-56: Game Flow
- **Unit 53:** Level complete - all pellets eaten
- **Unit 54:** Level transition - reset maze
- **Unit 55:** Difficulty increase - faster ghosts
- **Unit 56:** Fruit bonus - bonus items appear

### Units 57-60: Presentation
- **Unit 57:** Title screen - game logo
- **Unit 58:** Ready message - before level starts
- **Unit 59:** High score display - best scores
- **Unit 60:** Game over screen - final score

### Units 61-64: Release
- **Unit 61:** Instructions screen
- **Unit 62:** AI tuning - ghost behaviour balance
- **Unit 63:** Speed balancing - difficulty curve
- **Unit 64:** Release build - final iNES ROM

**Phase Goal:** Complete maze chase game.

---

## Summary

**Pellet Panic** teaches AI personalities and state-based behaviour:

**Phase 1 (Maze):** Constrained movement, direction queuing.

**Phase 2 (Basics):** Pellets, ghosts, screen wrap.

**Phase 3 (AI):** Personalities, modes, power pills.

**Phase 4 (Polish):** Audio, presentation, release.

### Skills Transferred Forward

1. **Constrained movement** → Maze-based games
2. **AI personalities** → Enemy variety
3. **State machine AI** → Complex behaviours
4. **Screen wrapping** → Various mechanics
5. **Mode transitions** → Game state changes

### Game Specifications

- **Maze:** 28×31 tile layout
- **Pellets:** 240 per level
- **Power Pills:** 4 per level
- **Ghosts:** 4 with unique AI
- **Lives:** 3
- **Mapper:** NROM
- **ROM Size:** 16KB PRG + 8KB CHR
- **Controls:** D-pad only
- **Audio:** APU effects
- **Distribution:** iNES ROM file
