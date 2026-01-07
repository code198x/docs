# Fortress: 128-Unit Outline

**Game:** 14 of 16 (68000 Assembly)
**Platform:** Commodore Amiga
**Language:** 68000 Assembly
**Units:** 128 (8 phases)
**Concept:** Isometric action-adventure. 3D projection with exploration and puzzles.

---

## Why This Game Fourteenth?

Fortress introduces isometric projection:

1. **Isometric maths** - 2:1 diamond projection
2. **Depth sorting** - Complex 3D ordering
3. **Isometric collision** - 3D space detection
4. **Block puzzles** - Pushing mechanics
5. **Multi-zone exploration** - Large world

The technical peak of the Advanced tier.

---

## Skills Applied from Previous Games

| Skill | From | Application |
|-------|------|-------------|
| Y-depth sorting | Brawler | Draw order |
| Tile rendering | Multiple | Isometric tiles |
| Exploration | Crypt/Wanderer | World design |
| Enemy AI | Multiple | Combat |
| Inventory | Crypt | Equipment |

## New Skills Introduced

| Skill | Phase | Description |
|-------|-------|-------------|
| Isometric projection | 1 | 2D to isometric |
| 3D coordinate system | 1 | X, Y, Z mapping |
| Isometric collision | 3 | 3D detection |
| Block puzzles | 4 | Push mechanics |
| Zone transitions | 5 | Area loading |

---

## Phase 1: Isometric Foundation (Units 1-16)
*Projection and display.*

### Units 1-4: Isometric Concept
- **Unit 1:** Isometric overview - 2:1 ratio
- **Unit 2:** 3D coordinates - X, Y, Z
- **Unit 3:** Screen mapping - 3D to 2D
- **Unit 4:** Projection formula

### Units 5-8: Tile Display
- **Unit 5:** Isometric tiles - diamond shapes
- **Unit 6:** Tile dimensions - 64×32 typical
- **Unit 7:** Floor tiles - ground
- **Unit 8:** Tile rendering - order

### Units 9-12: Depth Sorting
- **Unit 9:** Sorting concept - back to front
- **Unit 10:** Sort key - X + Y + Z
- **Unit 11:** Painter's algorithm - isometric
- **Unit 12:** Sorted display demo

### Units 13-16: Room Display
- **Unit 13:** Room structure - 3D grid
- **Unit 14:** Wall tiles - vertical
- **Unit 15:** Complete room - floor + walls
- **Unit 16:** Isometric room demo

**Phase Goal:** Isometric room display.

---

## Phase 2: Player and Movement (Units 17-32)
*Character in isometric space.*

### Units 17-20: Player Sprite
- **Unit 17:** Isometric player - 8 directions
- **Unit 18:** Player positioning - 3D coords
- **Unit 19:** Player rendering - in sort order
- **Unit 20:** Player animation - walk cycle

### Units 21-24: Movement
- **Unit 21:** 8-directional input - mapping
- **Unit 22:** Isometric movement - angled
- **Unit 23:** Movement speed - consistent
- **Unit 24:** Smooth movement - pixel steps

### Units 25-28: Height and Jumping
- **Unit 25:** Z coordinate - height
- **Unit 26:** Jump mechanic - Z change
- **Unit 27:** Gravity - falling
- **Unit 28:** Landing - on surfaces

### Units 29-32: Camera
- **Unit 29:** Room-based view - single screen
- **Unit 30:** Room boundaries - walls
- **Unit 31:** Exit detection - doorways
- **Unit 32:** Player movement demo

**Phase Goal:** Player moving in isometric space.

---

## Phase 3: Collision System (Units 33-48)
*3D collision detection.*

### Units 33-36: Floor Collision
- **Unit 33:** Floor height - Z levels
- **Unit 34:** Standing detection - on floor
- **Unit 35:** Falling detection - no floor
- **Unit 36:** Multi-level floors - steps

### Units 37-40: Wall Collision
- **Unit 37:** Wall representation - 3D blocks
- **Unit 38:** Wall detection - movement blocking
- **Unit 39:** Wall sliding - along walls
- **Unit 40:** Corner handling

### Units 41-44: Object Collision
- **Unit 41:** Object boxes - 3D bounds
- **Unit 42:** Object overlap - detection
- **Unit 43:** Pushable blocks - special case
- **Unit 44:** Collision response

### Units 45-48: Height Collision
- **Unit 45:** Jump landing - on objects
- **Unit 46:** Head collision - ceiling
- **Unit 47:** Falling onto - platforms
- **Unit 48:** 3D collision complete

**Phase Goal:** Full 3D collision system.

---

## Phase 4: Puzzles and Objects (Units 49-64)
*Block pushing and switches.*

### Units 49-52: Block Puzzles
- **Unit 49:** Pushable blocks - concept
- **Unit 50:** Push mechanics - one tile
- **Unit 51:** Push collision - blocked
- **Unit 52:** Push animation

### Units 53-56: Pressure Plates
- **Unit 53:** Plate concept - triggers
- **Unit 54:** Plate detection - weight on
- **Unit 55:** Plate actions - doors open
- **Unit 56:** Block on plate - puzzles

### Units 57-60: Other Objects
- **Unit 57:** Switches - toggle
- **Unit 58:** Moving platforms - paths
- **Unit 59:** Spikes - hazards
- **Unit 60:** Collectibles - keys, items

### Units 61-64: Puzzle Design
- **Unit 61:** Puzzle room 1 - simple
- **Unit 62:** Puzzle room 2 - medium
- **Unit 63:** Puzzle room 3 - complex
- **Unit 64:** Puzzle variety

**Phase Goal:** Working puzzle mechanics.

---

## Phase 5: Zones and Exploration (Units 65-80)
*Multi-zone world.*

### Units 65-68: Zone Structure
- **Unit 65:** Zone concept - themed areas
- **Unit 66:** Zone data - rooms per zone
- **Unit 67:** Zone graphics - tile sets
- **Unit 68:** Zone transitions

### Units 69-72: Zone 1 - Ruins
- **Unit 69:** Ruins theme - crumbling stone
- **Unit 70:** Ruins rooms - 8+ rooms
- **Unit 71:** Ruins enemies
- **Unit 72:** Ruins boss room

### Units 73-76: Zone 2 - Catacombs
- **Unit 73:** Catacombs theme - underground
- **Unit 74:** Catacombs rooms - darker
- **Unit 75:** Catacombs enemies
- **Unit 76:** Catacombs boss

### Units 77-80: Zone 3 - Tower
- **Unit 77:** Tower theme - vertical
- **Unit 78:** Tower rooms - heights
- **Unit 79:** Tower enemies - flying
- **Unit 80:** Tower boss - final

**Phase Goal:** Three explorable zones.

---

## Phase 6: Combat and Enemies (Units 81-96)
*Fighting system.*

### Units 81-84: Combat Mechanics
- **Unit 81:** Attack action - sword swing
- **Unit 82:** Attack hitbox - 3D
- **Unit 83:** Attack animation
- **Unit 84:** Attack damage

### Units 85-88: Enemy Types
- **Unit 85:** Walker enemy - patrol
- **Unit 86:** Shooter enemy - ranged
- **Unit 87:** Flyer enemy - aerial
- **Unit 88:** Heavy enemy - tough

### Units 89-92: Boss Fights
- **Unit 89:** Boss 1 - ruins guardian
- **Unit 90:** Boss 2 - catacomb horror
- **Unit 91:** Boss 3 - tower master
- **Unit 92:** Boss patterns - isometric

### Units 93-96: Equipment
- **Unit 93:** Weapons - sword, better sword
- **Unit 94:** Armour - damage reduction
- **Unit 95:** Items - health, keys
- **Unit 96:** Equipment display

**Phase Goal:** Combat and bosses.

---

## Phase 7: Polish and Features (Units 97-112)
*Presentation and saves.*

### Units 97-100: Save System
- **Unit 97:** Save data - progress
- **Unit 98:** Save format - room, items
- **Unit 99:** Save/load - disk I/O
- **Unit 100:** Continue option

### Units 101-104: Audio
- **Unit 101:** Zone music - per area
- **Unit 102:** Boss music
- **Unit 103:** Sound effects - full set
- **Unit 104:** Audio integration

### Units 105-108: Presentation
- **Unit 105:** Title screen
- **Unit 106:** Zone intro - name
- **Unit 107:** Game over
- **Unit 108:** Victory sequence

### Units 109-112: Extra Features
- **Unit 109:** Map display - explored
- **Unit 110:** Item inventory screen
- **Unit 111:** Hints/tips - NPCs
- **Unit 112:** Secrets - hidden rooms

**Phase Goal:** Polished adventure.

---

## Phase 8: Release (Units 113-128)
*Testing and release.*

### Units 113-116: Balance
- **Unit 113:** Puzzle difficulty
- **Unit 114:** Combat balance
- **Unit 115:** Boss balance
- **Unit 116:** Overall progression

### Units 117-120: Testing
- **Unit 117:** Full playthrough
- **Unit 118:** All puzzles
- **Unit 119:** All zones
- **Unit 120:** Save/load testing

### Units 121-124: Optimisation
- **Unit 121:** Sort optimisation
- **Unit 122:** Render optimisation
- **Unit 123:** Collision optimisation
- **Unit 124:** Overall tuning

### Units 125-128: Release
- **Unit 125:** Credits
- **Unit 126:** Documentation
- **Unit 127:** Final testing
- **Unit 128:** Release build - ADF

**Phase Goal:** Complete isometric adventure.

---

## Summary

**Fortress** teaches isometric projection and 3D gameplay.

### Technical Specifications

- **Display:** Isometric 2:1, 320×256
- **Projection:** 3D coordinate system
- **Sorting:** Painter's algorithm for 3D
- **Zones:** 3 themed areas, 24+ rooms
- **Puzzles:** Block pushing, switches
- **Combat:** Melee with bosses
- **Save:** Disk-based progress
- **Audio:** Zone music, effects
- **Distribution:** Bootable ADF

### Skills for Next Game

- Isometric projection maths
- 3D depth sorting
- 3D collision detection
- Block puzzle mechanics
- Multi-zone world design
