# Dungeon Explorer: 64-Unit Outline

**Game:** 4 - Dungeon Explorer
**Platform:** Sinclair ZX Spectrum
**Language:** Sinclair BASIC
**Units:** 64 (4 phases)
**Prerequisite:** Paddle Battle complete
**Concept:** Navigate through dungeon rooms using DATA statements and PRINT AT.

---

## Overview

Dungeon Explorer challenges players to navigate through connected dungeon rooms, collecting keys and treasures while avoiding traps. This game introduces DATA statements for room storage and PRINT AT for character-based map display.

---

## Learning Goals

By completing Dungeon Explorer, learners will:

- Use DATA and READ for room storage
- Implement PRINT AT for positioned text
- Create character-based maps
- Build four-directional movement
- Implement wall collision via attributes
- Design room transitions
- Create simple inventory system
- Manage multiple connected rooms

---

## Phase 1: Room Display (Units 1-16)
*Drawing dungeon rooms.*

### Units 1-4: PRINT AT Basics
- **Unit 1:** PRINT AT row, column - positioning
- **Unit 2:** Coordinate system - 0-21 rows, 0-31 columns
- **Unit 3:** Drawing characters at positions
- **Unit 4:** Building a room outline

### Units 5-8: DATA Statements
- **Unit 5:** DATA statement - storing values
- **Unit 6:** READ statement - retrieving values
- **Unit 7:** Room data format - row strings
- **Unit 8:** Complete room in DATA

### Units 9-12: Room Rendering
- **Unit 9:** Reading room data
- **Unit 10:** Displaying row by row
- **Unit 11:** Character meanings - # wall, . floor
- **Unit 12:** Coloured walls and floors

### Units 13-16: Room Design
- **Unit 13:** Wall characters - blocks
- **Unit 14:** Door characters - exits
- **Unit 15:** Player starting position
- **Unit 16:** Phase 1 complete - room displays

**Phase Goal:** Render room from DATA statements.

---

## Phase 2: Movement and Collision (Units 17-32)
*Exploring the dungeon.*

### Units 17-20: Four-Direction Input
- **Unit 17:** INKEY$ for direction keys
- **Unit 18:** Q=up, A=down, O=left, P=right
- **Unit 19:** Direction detection
- **Unit 20:** Movement intent handling

### Units 21-24: Collision Detection
- **Unit 21:** ATTR function - reading attributes
- **Unit 22:** SCREEN$ function - reading character
- **Unit 23:** Wall detection - don't move
- **Unit 24:** Floor detection - allow move

### Units 25-28: Player Movement
- **Unit 25:** Clear old player position
- **Unit 26:** Update position variables
- **Unit 27:** Draw at new position
- **Unit 28:** Smooth movement feel

### Units 29-32: Exit Detection
- **Unit 29:** Door characters in room
- **Unit 30:** Reaching a door
- **Unit 31:** Door direction detection
- **Unit 32:** Phase 2 complete - movement working

**Phase Goal:** Navigate room with wall collision.

---

## Phase 3: Multiple Rooms (Units 33-48)
*Expanding the dungeon.*

### Units 33-36: Room Data Structure
- **Unit 33:** Multiple rooms in DATA
- **Unit 34:** Room separator markers
- **Unit 35:** Room connection data
- **Unit 36:** RESTORE for room loading

### Units 37-40: Room Transitions
- **Unit 37:** Exit triggers room change
- **Unit 38:** Loading new room data
- **Unit 39:** Player entry position
- **Unit 40:** Smooth room transition

### Units 41-44: Items and Keys
- **Unit 41:** Key items in rooms
- **Unit 42:** Collecting keys
- **Unit 43:** Inventory tracking
- **Unit 44:** Locked doors - need key

### Units 45-48: Treasure
- **Unit 45:** Treasure items
- **Unit 46:** Score for collecting
- **Unit 47:** Treasure display on HUD
- **Unit 48:** Phase 3 complete - multi-room dungeon

**Phase Goal:** Connected rooms with items.

---

## Phase 4: Hazards and Polish (Units 49-64)
*Adding danger and refinement.*

### Units 49-52: Hazards
- **Unit 49:** Trap characters
- **Unit 50:** Stepping on trap - damage
- **Unit 51:** Health system
- **Unit 52:** Game over on zero health

### Units 53-56: Enemy Placement
- **Unit 53:** Static enemy in room
- **Unit 54:** Touching enemy - damage
- **Unit 55:** Enemies block path
- **Unit 56:** Combat avoidance gameplay

### Units 57-60: HUD and Status
- **Unit 57:** Health bar display
- **Unit 58:** Inventory display
- **Unit 59:** Room name/number
- **Unit 60:** Clean HUD layout

### Units 61-64: Final Game
- **Unit 61:** Five complete rooms
- **Unit 62:** Goal room - treasure vault
- **Unit 63:** Victory condition
- **Unit 64:** **RELEASE: Dungeon Explorer complete**

**Phase Goal:** Complete dungeon exploration game.

---

## Summary

**Dungeon Explorer** introduces data-driven design:

### Technical Specifications

- **Display:** Character mode (32×22 usable)
- **Rooms:** 5 connected dungeon rooms
- **Input:** Four-direction INKEY$
- **Features:** Keys, locks, treasure, traps
- **Collision:** SCREEN$ and ATTR checks

### Skills Learned

- DATA/READ for level storage
- PRINT AT for positioned text
- Character-based map design
- Four-directional movement
- Collision via screen reading
- Room transition logic
- Inventory management
- HUD design

### Room Data Format

```basic
1000 DATA "################################"
1010 DATA "#......#.........#............#"
1020 DATA "#......#....K....#............#"
1030 DATA "#......#.........D............#"
...
```

### SCREEN$ and ATTR

| Function | Purpose |
|----------|---------|
| SCREEN$(r,c) | Get character at position |
| ATTR(r,c) | Get attribute at position |
| Use case | Collision detection |

### Progression

This game prepares learners for **Snake Spectrum** where they'll use arrays to track a growing snake body and implement User-Defined Graphics for custom characters.
