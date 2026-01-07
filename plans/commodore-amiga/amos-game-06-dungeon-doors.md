# Dungeon Doors: 64-Unit Outline

**Game:** 6 of 8 (AMOS BASIC)
**Platform:** Commodore Amiga
**Language:** AMOS BASIC
**Units:** 64 (4 phases)
**Concept:** Flip-screen exploration. Navigate rooms, collect keys, find the exit.

---

## Why This Game Sixth?

Dungeon Doors introduces multi-screen exploration:

1. **Room transitions** - Screen changes
2. **Persistent state** - Items stay collected
3. **Key/door mechanics** - Inventory puzzles
4. **Map system** - Track exploration
5. **Save/load** - Game state persistence

Builds on tile rendering and state management.

---

## Skills Applied from Previous Games

| Skill | From | Application in Dungeon Doors |
|-------|------|----------------------------|
| Tile rendering | Maze Runner | Room graphics |
| Enemy AI | Maze Runner | Chase behaviour |
| State machines | All | Game state |
| File I/O | Space Swarm | Save/load |
| Level data | Crate Stack | Room definitions |

## New Skills Introduced

| Skill | Phase | Description |
|-------|-------|-------------|
| Room transitions | 1 | Screen changes |
| Persistent state | 2 | Items collected |
| Inventory system | 2 | Key tracking |
| Map display | 3 | Exploration tracking |
| Save/load game | 4 | Full state save |

---

## Phase 1: Room System (Units 1-16)
*Multi-room structure.*

### Units 1-4: Room Data
- **Unit 1:** Room concept - single screen
- **Unit 2:** Room array - tiles per room
- **Unit 3:** Room connections - exits
- **Unit 4:** World layout - room grid

### Units 5-8: Room Rendering
- **Unit 5:** Tile graphics - walls, floors
- **Unit 6:** Room drawing - full screen
- **Unit 7:** Room variety - different themes
- **Unit 8:** Room transitions - exit detection

### Units 9-12: Room Navigation
- **Unit 9:** Edge exit - leave screen
- **Unit 10:** Load next room - transition
- **Unit 11:** Entry position - where player appears
- **Unit 12:** Smooth transition - fade effect

### Units 13-16: Room Content
- **Unit 13:** Room elements - doors, items
- **Unit 14:** Element placement - per room
- **Unit 15:** Element tracking - what's where
- **Unit 16:** Basic navigation demo

**Phase Goal:** Navigate between rooms.

---

## Phase 2: Inventory and Items (Units 17-32)
*Collection and persistence.*

### Units 17-20: Key System
- **Unit 17:** Key sprites - coloured keys
- **Unit 18:** Key collection - pick up
- **Unit 19:** Key inventory - tracking owned
- **Unit 20:** Door sprites - locked doors

### Units 21-24: Door Mechanics
- **Unit 21:** Door colours - match keys
- **Unit 22:** Door unlocking - key + door
- **Unit 23:** Door opening - remove barrier
- **Unit 24:** Key consumption - optional

### Units 25-28: Persistent State
- **Unit 25:** Collected items array - tracking
- **Unit 26:** Room state - per-room changes
- **Unit 27:** State persistence - between rooms
- **Unit 28:** Reset conditions - death, restart

### Units 29-32: Inventory Display
- **Unit 29:** Inventory HUD - show keys
- **Unit 30:** Item count - how many
- **Unit 31:** Current room - identifier
- **Unit 32:** HUD layout - screen usage

**Phase Goal:** Key/door puzzle mechanics.

---

## Phase 3: Exploration Features (Units 33-48)
*Enemies, map, hazards.*

### Units 33-36: Dungeon Enemies
- **Unit 33:** Enemy sprites - skeletons, bats
- **Unit 34:** Enemy placement - per room
- **Unit 35:** Chase behaviour - follow player
- **Unit 36:** Patrol behaviour - set path

### Units 37-40: Combat/Avoidance
- **Unit 37:** Enemy collision - damage
- **Unit 38:** Health system - hit points
- **Unit 39:** Health pickups - restoration
- **Unit 40:** Death handling - respawn

### Units 41-44: Map System
- **Unit 41:** Map data - explored rooms
- **Unit 42:** Map display - pause screen
- **Unit 43:** Room reveal - on visit
- **Unit 44:** Goal indicator - exit location

### Units 45-48: Dungeon Hazards
- **Unit 45:** Trap tiles - spikes
- **Unit 46:** Moving hazards - fireballs
- **Unit 47:** Puzzle elements - switches
- **Unit 48:** Secret areas - hidden rooms

**Phase Goal:** Full dungeon exploration.

---

## Phase 4: Game Completion (Units 49-64)
*Save system and polish.*

### Units 49-52: Save System
- **Unit 49:** Save data - what to save
- **Unit 50:** Save format - structured data
- **Unit 51:** Save to disk - write file
- **Unit 52:** Load from disk - read file

### Units 53-56: Game Structure
- **Unit 53:** Dungeon layout - 16+ rooms
- **Unit 54:** Key distribution - puzzle design
- **Unit 55:** Exit location - goal room
- **Unit 56:** Victory condition - reach exit

### Units 57-60: Presentation
- **Unit 57:** Title screen - game logo
- **Unit 58:** Room enter effect - flash/fade
- **Unit 59:** Sound effects - doors, keys, enemies
- **Unit 60:** Background music - dungeon theme

### Units 61-64: Completion
- **Unit 61:** Full dungeon design
- **Unit 62:** Victory screen
- **Unit 63:** Full testing
- **Unit 64:** Release build

**Phase Goal:** Complete exploration game.

---

## Summary

**Dungeon Doors** teaches multi-screen exploration.

### Game Specifications

- **Player:** Explorer sprite, 4-directional
- **World:** 16+ rooms in grid layout
- **Keys:** 4 colours, match to doors
- **Doors:** Locked, require matching key
- **Enemies:** Chasers and patrollers
- **Health:** Hit points, pickups restore
- **Map:** Pause menu exploration display
- **Save:** Full game state to disk
- **Display:** Flip-screen rooms
- **Sound:** Effects and dungeon music
- **Distribution:** AMOS source + compiled
