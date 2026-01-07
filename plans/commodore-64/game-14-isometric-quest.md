# Isometric Quest: 128-Unit Outline

**Game:** 14 of 16
**Platform:** Commodore 64
**Units:** 128 (First advanced-length game)
**Concept:** Isometric adventure game. Explore a 3D-perspective world, solve puzzles, complete quests, and defeat enemies in an Ultimate-style isometric adventure.

---

## Why 128 Units?

Isometric games are significantly more complex than orthogonal games:
1. **Isometric mathematics** - completely new coordinate system
2. **Depth sorting** - painter's algorithm for correct draw order
3. **Isometric collision** - fundamentally different from tile collision
4. **Large world** - many interconnected screens
5. **Adventure systems** - inventory, quests, NPCs, dialogue
6. **Content volume** - extensive world to explore

This is the curriculum's first game requiring extended time due to technical and content complexity.

---

## Skills Applied from Previous Games

All 13 previous games contribute skills to Isometric Quest:

| Category | Skills Applied | Sources |
|----------|---------------|---------|
| Audio | SID music, sound effects | SID Symphony |
| Graphics | Sprites, characters, animation | Starfield, Platform Panic |
| Input | Joystick control | All games |
| Collision | Sprite and tile collision | Maze Raider, various |
| Systems | Inventory, quests, dialogue | Dungeon Crawl |
| Combat | Attack, damage, health | Arena Fighter, Dungeon Crawl |
| Memory | Level streaming, compression | Night Raid, Parallax Patrol |
| Performance | Multiplexing, optimization | Sprite Storm, various |
| Raster | Visual effects | Raster Rider |

## New Skills Introduced

| Skill | Units | Description |
|-------|-------|-------------|
| Isometric projection | 9-16 | 2:1 isometric mathematics |
| Screen-to-world conversion | 17-24 | Click/move position translation |
| Depth sorting | 25-32 | Painter's algorithm implementation |
| Isometric collision | 33-40 | Diamond-shaped collision |
| Isometric pathfinding | 41-48 | A* in isometric space |
| Multi-screen world | 49-56 | World map navigation |
| Z-height handling | 57-64 | Elevated terrain, jumping |
| Isometric shadows | 89-96 | Proper shadow projection |

---

## Phase 1: Isometric Foundation (Units 1-16)
*Understanding and implementing isometric projection.*

### Units 1-4: Isometric Theory
- **Unit 1:** Isometric projection concept - what is 2:1 isometric
- **Unit 2:** Coordinate systems - world vs screen coordinates
- **Unit 3:** Mathematics of isometric - conversion formulas
- **Unit 4:** Planning the implementation - tile sizes, screen layout

### Units 5-8: Basic Isometric Rendering
- **Unit 5:** Isometric tile graphics - diamond shape design
- **Unit 6:** Single tile rendering - drawing at correct position
- **Unit 7:** Tile grid rendering - multiple tiles in grid
- **Unit 8:** Screen filling - complete isometric floor display

### Units 9-12: World-to-Screen Conversion
- **Unit 9:** World coordinates to screen position formula
- **Unit 10:** Implementation of conversion routine
- **Unit 11:** Screen position to world coordinates (reverse)
- **Unit 12:** Testing and verification of conversions

### Units 13-16: Basic Isometric Display
- **Unit 13:** Drawing order basics - back to front
- **Unit 14:** Simple room rendering - floor only
- **Unit 15:** Adding walls - vertical elements
- **Unit 16:** Complete basic isometric room

---

## Phase 2: Depth and Objects (Units 17-32)
*Solving the depth sorting problem.*

### Units 17-20: Depth Sorting Theory
- **Unit 17:** Why depth matters - overlapping objects
- **Unit 18:** Painter's algorithm concept
- **Unit 19:** Sort key calculation - Y + X combination
- **Unit 20:** Sorting algorithm selection

### Units 21-24: Depth Sorting Implementation
- **Unit 21:** Object list structure for sorting
- **Unit 22:** Sort implementation
- **Unit 23:** Rendering in sorted order
- **Unit 24:** Testing with multiple objects

### Units 25-28: Player Character
- **Unit 25:** Player sprite in isometric view
- **Unit 26:** 8-direction player graphics
- **Unit 27:** Player positioning in world
- **Unit 28:** Player in sorted draw order

### Units 29-32: Basic Movement
- **Unit 29:** Input to isometric direction mapping
- **Unit 30:** World-space movement implementation
- **Unit 31:** Screen-space display of movement
- **Unit 32:** Smooth animated walking

---

## Phase 3: Collision and Navigation (Units 33-48)
*Isometric collision detection and pathfinding.*

### Units 33-36: Isometric Collision Theory
- **Unit 33:** Diamond-shaped collision areas
- **Unit 34:** Tile occupancy checking
- **Unit 35:** Sub-tile precision collision
- **Unit 36:** Wall collision concepts

### Units 37-40: Collision Implementation
- **Unit 37:** Player collision detection
- **Unit 38:** Wall collision response
- **Unit 39:** Object collision (furniture, etc.)
- **Unit 40:** Complete collision system

### Units 41-44: Pathfinding Theory
- **Unit 41:** A* algorithm introduction
- **Unit 42:** Heuristic calculation for isometric
- **Unit 43:** Neighbor finding in isometric grid
- **Unit 44:** Path storage and following

### Units 45-48: Pathfinding Implementation
- **Unit 45:** A* implementation for NPCs/enemies
- **Unit 46:** Path following behavior
- **Unit 47:** Dynamic path recalculation
- **Unit 48:** Multiple pathfinding agents

---

## Phase 4: World Structure (Units 49-64)
*Large world with multiple screens.*

### Units 49-52: Room/Screen System
- **Unit 49:** Room data structure
- **Unit 50:** Room loading and rendering
- **Unit 51:** Room transition detection
- **Unit 52:** Room connections (exits)

### Units 53-56: World Map
- **Unit 53:** World map structure
- **Unit 54:** Screen coordinates to world position
- **Unit 55:** World map display (pause menu)
- **Unit 56:** Fast travel concept

### Units 57-60: Z-Height
- **Unit 57:** Elevated terrain concept
- **Unit 58:** Stairs and ramps
- **Unit 59:** Height in sorting
- **Unit 60:** Jumping between heights

### Units 61-64: Complete Navigation
- **Unit 61:** Full room-to-room movement
- **Unit 62:** Multi-level buildings
- **Unit 63:** Outdoor-to-indoor transitions
- **Unit 64:** Complete navigable world

---

## Phase 5: Adventure Systems (Units 65-80)
*Inventory, items, quests.*

### Units 65-68: Inventory System
- **Unit 65:** Inventory data structure
- **Unit 66:** Item pickup in isometric
- **Unit 67:** Inventory display
- **Unit 68:** Item use mechanics

### Units 69-72: Item Types
- **Unit 69:** Consumables (health potions)
- **Unit 70:** Equipment (weapons, armor)
- **Unit 71:** Key items (quest items)
- **Unit 72:** Complete item system

### Units 73-76: NPC Dialogue
- **Unit 73:** NPC placement and interaction
- **Unit 74:** Dialogue system framework
- **Unit 75:** Branching dialogue
- **Unit 76:** Quest-giving NPCs

### Units 77-80: Quest System
- **Unit 77:** Quest data structure
- **Unit 78:** Quest tracking and display
- **Unit 79:** Quest completion detection
- **Unit 80:** Reward handling

---

## Phase 6: Combat and Enemies (Units 81-96)
*Combat system and enemy AI.*

### Units 81-84: Combat Framework
- **Unit 81:** Attack mechanics
- **Unit 82:** Damage and health
- **Unit 83:** Combat collision detection
- **Unit 84:** Death and respawn

### Units 85-88: Enemy Types
- **Unit 85:** Basic melee enemy
- **Unit 86:** Ranged enemy
- **Unit 87:** Patrol behavior
- **Unit 88:** Aggressive behavior

### Units 89-92: Visual Effects
- **Unit 89:** Isometric shadows
- **Unit 90:** Hit effects
- **Unit 91:** Death animations
- **Unit 92:** Magic/spell effects

### Units 93-96: Boss Encounters
- **Unit 93:** Boss design principles
- **Unit 94:** Boss room setup
- **Unit 95:** Boss attack patterns
- **Unit 96:** Boss defeat and rewards

---

## Phase 7: Content and Polish (Units 97-112)
*Full game content and presentation.*

### Units 97-100: World Content
- **Unit 97:** Village area design (safe hub)
- **Unit 98:** Forest area design (exploration)
- **Unit 99:** Dungeon area design (challenge)
- **Unit 100:** Castle/final area design

### Units 101-104: Sound Design
- **Unit 101:** Ambient sounds per area
- **Unit 102:** Combat sounds
- **Unit 103:** Interface sounds
- **Unit 104:** Music per area

### Units 105-108: Save System
- **Unit 105:** Save state design
- **Unit 106:** Password generation
- **Unit 107:** Password entry
- **Unit 108:** Save system testing

### Units 109-112: User Interface
- **Unit 109:** Title screen
- **Unit 110:** Pause menu with map
- **Unit 111:** Game over and continue
- **Unit 112:** Complete UI polish

---

## Phase 8: Mastery (Units 113-128)
*Optimization, extras, release.*

### Units 113-116: Performance
- **Unit 113:** Profiling and bottlenecks
- **Unit 114:** Sorting optimization
- **Unit 115:** Rendering optimization
- **Unit 116:** Memory optimization

### Units 117-120: Extra Content
- **Unit 117:** Optional side quests
- **Unit 118:** Hidden areas
- **Unit 119:** Bonus items
- **Unit 120:** True ending requirements

### Units 121-124: Difficulty and Accessibility
- **Unit 121:** Difficulty options
- **Unit 122:** Tutorial integration
- **Unit 123:** Accessibility features
- **Unit 124:** Balance testing

### Units 125-128: Release
- **Unit 125:** Bug hunting and fixes
- **Unit 126:** Final testing
- **Unit 127:** Documentation
- **Unit 128:** Release build

---

## Summary

**Isometric Quest** is the curriculum's first 128-unit game, justified by:
1. Completely new coordinate system (isometric projection)
2. Complex depth sorting requirements
3. Different collision detection
4. Large world with adventure systems
5. Integration of combat, quests, inventory

### Skills Transferred Forward
1. **Isometric projection** - Future isometric games
2. **Depth sorting (painter's algorithm)** - Any layered graphics
3. **A* pathfinding** - Complex AI in future games
4. **Large world management** - Mega Blaster, Symphony's End

### Game Specifications
- **World:** 64+ screens across 4 themed areas
- **Perspective:** 2:1 isometric projection
- **Items:** 30+ item types
- **Enemies:** 8+ enemy types, 3 bosses
- **Quests:** Main quest + 10 side quests
- **NPCs:** 20+ dialogue NPCs
- **Features:** Save system, map, inventory, quest log
