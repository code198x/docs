# Dungeon Crawl: 128-Unit Outline

**Game:** 11 of 16
**Platform:** Commodore 64
**Units:** 128
**Concept:** Top-down adventure game. Explore interconnected dungeon rooms, collect keys, unlock doors, solve puzzles, defeat enemies, complete quests. A Zelda-inspired adventure with inventory, NPCs, and save system.

---

## Why 128 Units?

Dungeon Crawl introduces multiple complex interconnected systems:
1. **Multi-room world structure** - 64+ rooms with transitions and connections
2. **Full inventory system** - Items, equipment, consumables, quest items
3. **Combat system** - Melee attacks, enemy AI, damage, defeat
4. **NPC dialogue system** - Conversations, hints, quest-giving
5. **Quest framework** - Main quest, side quests, objectives, rewards
6. **Save/password system** - State serialisation and restoration
7. **Puzzle mechanics** - Switches, push blocks, hidden passages
8. **Dungeon content** - Multiple themed zones with appropriate enemies/items

At 64 units, each of these systems received only 2-4 units - insufficient for proper learning depth. 128 units allows each system to be properly developed and integrated.

---

## Skills Applied from Previous Games

| Skill | Learned In | Application in Dungeon Crawl |
|-------|-----------|---------------------------|
| SID fundamentals | SID Symphony | Area music, sound effects, ambiance |
| Hardware sprites | Starfield | Player, enemies, items, NPCs |
| Joystick input | Starfield | 8-direction movement |
| Sprite collision | Starfield | Combat, item collection |
| Custom characters | Maze Raider | Dungeon tiles, walls, floors |
| Tile-based maps | Maze Raider | Room layouts |
| Tile collision | Maze Raider | Wall collision |
| Animation frames | Platform Panic | Character walking, attack animations |
| Power-up collection | Brick Basher | Item pickup mechanics |
| Object management | Sprite Storm | Enemy and item management |
| Resource tracking | Night Raid | Health, keys, inventory |
| Boss encounters | Night Raid | Mini-bosses and final boss |
| Multiplexing | Sprite Storm | Multiple enemies on screen |
| Raster effects | Raster Rider | UI borders, transitions |

## New Skills Introduced

| Skill | Phase | Description |
|-------|-------|-------------|
| Multi-room architecture | 1-2 | Connected room structure and transitions |
| Room streaming | 2 | Loading room data on demand |
| Inventory management | 3 | Item storage, use, equipment |
| Lock/key mechanics | 3 | Keys unlock corresponding doors |
| Combat framework | 4 | Attack, damage, enemy defeat |
| Enemy AI patterns | 4 | Movement, pursuit, patrol behaviours |
| NPC dialogue system | 5 | Branching conversations |
| Quest tracking | 6 | Objectives, completion, rewards |
| Environmental puzzles | 5 | Switches, blocks, triggers |
| Password save system | 7 | State encoding and restoration |
| Disk I/O | 7 | Reading and writing files to disk |
| Disk save system | 7 | Full game state save/load |
| Map system | 7 | Explored area tracking and display |
| D64 disk images | 8 | Creating distribution disk images |
| Zone-based design | 8 | Themed areas with appropriate content |

---

## Phase 1: Room Foundation (Units 1-16)
*Core room rendering and tile systems.*

### Units 1-4: Project Setup and Design
- **Unit 1:** Top-down adventure concept - analysing Zelda, planning our game
- **Unit 2:** Room data architecture - tile grid format, tile types
- **Unit 3:** Memory layout - room storage, character sets, sprites
- **Unit 4:** Development framework - main loop, state management

### Units 5-8: Dungeon Character Set
- **Unit 5:** Floor tile designs - stone, wood, water, pit
- **Unit 6:** Wall tile designs - solid, corner, decorative
- **Unit 7:** Door tile designs - closed, open, locked
- **Unit 8:** Special tile designs - switches, chests, stairs

### Units 9-12: Room Rendering
- **Unit 9:** Tile-to-character mapping - render single tile
- **Unit 10:** Room drawing routine - render complete room
- **Unit 11:** Colour application - per-tile colouring
- **Unit 12:** Multiple room display - test different layouts

### Units 13-16: Tile System
- **Unit 13:** Tile type system - walkable, solid, interactive
- **Unit 14:** Tile attribute data - flags per tile type
- **Unit 15:** Tile query functions - check tile at position
- **Unit 16:** Complete room display with all tile types

**Phase Goal:** Dungeon rooms render correctly with varied tiles and colours.

---

## Phase 2: Player and Navigation (Units 17-32)
*Player character and room-to-room movement.*

### Units 17-20: Player Character
- **Unit 17:** Hero sprite design - 4-direction frames
- **Unit 18:** Player positioning - tile-aligned placement
- **Unit 19:** Player state structure - health, position, direction
- **Unit 20:** Initial room with player sprite visible

### Units 21-24: Movement System
- **Unit 21:** 8-direction joystick reading
- **Unit 22:** Smooth pixel movement - sub-tile positioning
- **Unit 23:** Movement speed tuning - responsive feel
- **Unit 24:** Direction-facing update - player faces movement direction

### Units 25-28: Collision and Animation
- **Unit 25:** Wall collision detection - check destination tile
- **Unit 26:** Collision response - slide along walls
- **Unit 27:** Walk animation frames - 2-frame walk cycle
- **Unit 28:** Animation integration - animate while moving, idle when stopped

### Units 29-32: Room Transitions
- **Unit 29:** Map structure - room coordinates, connections
- **Unit 30:** Exit detection - room edge and door exits
- **Unit 31:** Room loading - unload current, load new room
- **Unit 32:** Player repositioning - appear at opposite edge

**Phase Goal:** Player navigates between connected rooms with smooth movement and animation.

---

## Phase 3: Items and Inventory (Units 33-48)
*Item collection and inventory management.*

### Units 33-36: Basic Items
- **Unit 33:** Item data structure - type, position, room
- **Unit 34:** Item sprites - treasure, key, potion, equipment
- **Unit 35:** Item rendering - draw items in room
- **Unit 36:** Item collection - collision detection, removal

### Units 37-40: Item Types
- **Unit 37:** Treasure items - score increment, collection feedback
- **Unit 38:** Key items - key counter, door unlocking
- **Unit 39:** Health items - heart pickups, health restoration
- **Unit 40:** Equipment items - sword, shield, tools

### Units 41-44: Inventory System
- **Unit 41:** Inventory data structure - slots, quantities
- **Unit 42:** Adding items to inventory
- **Unit 43:** Inventory screen layout - item display
- **Unit 44:** Inventory cursor and selection

### Units 45-48: Item Usage
- **Unit 45:** Item use mechanics - select and use
- **Unit 46:** Consumable items - potions restore health
- **Unit 47:** Equipment handling - equip sword/shield
- **Unit 48:** Door unlocking - keys open locked doors

**Phase Goal:** Full inventory system with collectible and usable items.

---

## Phase 4: Combat System (Units 49-64)
*Attack mechanics and enemy encounters.*

### Units 49-52: Player Attack
- **Unit 49:** Attack button detection
- **Unit 50:** Sword swing animation - 3-frame attack sequence
- **Unit 51:** Attack hitbox - damage area in front of player
- **Unit 52:** Attack timing - cooldown between attacks

### Units 53-56: Enemy Framework
- **Unit 53:** Enemy data structure - type, health, position, state
- **Unit 54:** Enemy sprites - multiple enemy designs
- **Unit 55:** Enemy rendering - draw all enemies in room
- **Unit 56:** Enemy per-room data - which enemies in which room

### Units 57-60: Enemy Behaviour
- **Unit 57:** Wander AI - random movement within room
- **Unit 58:** Pursuit AI - move toward player
- **Unit 59:** Patrol AI - follow set path
- **Unit 60:** Behaviour switching - idle, alert, aggressive states

### Units 61-64: Combat Resolution
- **Unit 61:** Attack collision - sword hits enemy
- **Unit 62:** Enemy damage and defeat - health, death animation, removal
- **Unit 63:** Enemy drops - treasure, hearts on defeat
- **Unit 64:** Player damage - enemy contact, invulnerability frames

**Phase Goal:** Working combat system with varied enemy behaviours.

---

## Phase 5: Adventure Elements (Units 65-80)
*NPCs, dialogue, and environmental puzzles.*

### Units 65-68: NPC System
- **Unit 65:** NPC data structure - position, sprite, dialogue ID
- **Unit 66:** NPC sprites - villager, merchant, sage designs
- **Unit 67:** NPC rendering - static characters in rooms
- **Unit 68:** NPC interaction trigger - button press near NPC

### Units 69-72: Dialogue System
- **Unit 69:** Dialogue box rendering - border, background
- **Unit 70:** Text display - printing dialogue text
- **Unit 71:** Multi-line dialogue - page breaks, continuation
- **Unit 72:** Dialogue dismissal - button to close

### Units 73-76: Advanced Dialogue
- **Unit 73:** Dialogue branching - multiple responses
- **Unit 74:** State-aware dialogue - text changes based on progress
- **Unit 75:** NPC hints - clues about puzzles and progress
- **Unit 76:** Shop NPCs - buy/sell items (if applicable)

### Units 77-80: Environmental Puzzles
- **Unit 77:** Pushable blocks - detection and movement
- **Unit 78:** Floor switches - activation on step/block
- **Unit 79:** Switch-door linkage - switch opens specific door
- **Unit 80:** Hidden passages - bombable/pushable walls

**Phase Goal:** NPCs with dialogue and environmental puzzle mechanics.

---

## Phase 6: Quest System (Units 81-96)
*Objectives, tracking, and progression.*

### Units 81-84: Quest Framework
- **Unit 81:** Quest data structure - ID, objectives, status
- **Unit 82:** Objective types - collect, defeat, reach, talk
- **Unit 83:** Quest state tracking - active, complete, rewarded
- **Unit 84:** Quest list management - multiple quests

### Units 85-88: Main Quest
- **Unit 85:** Main quest design - story premise, stages
- **Unit 86:** Quest items - sacred crystals, keys, artifacts
- **Unit 87:** Stage progression - quest advances on collection
- **Unit 88:** Victory condition - all objectives complete

### Units 89-92: Side Quests
- **Unit 89:** Side quest design - optional objectives
- **Unit 90:** NPC quest-giving - receive quests from NPCs
- **Unit 91:** Quest completion dialogue - return to NPC
- **Unit 92:** Quest rewards - items, gold, equipment

### Units 93-96: Quest Interface
- **Unit 93:** Quest log display - list active quests
- **Unit 94:** Objective display - current quest goals
- **Unit 95:** Completion notifications - quest complete popup
- **Unit 96:** Quest integration - dialogue, items, world state

**Phase Goal:** Complete quest system with main story and side quests.

---

## Phase 7: Persistence and UI (Units 97-112)
*Save system, map, and user interface.*

### Units 97-100: HUD System
- **Unit 97:** HUD layout design - health, keys, equipped item
- **Unit 98:** Health display - heart icons
- **Unit 99:** Key counter display
- **Unit 100:** Equipped item display - current weapon/tool

### Units 101-104: Map System
- **Unit 101:** Exploration tracking - mark visited rooms
- **Unit 102:** Map data structure - room states
- **Unit 103:** Map rendering - dungeon overview
- **Unit 104:** Player position on map - current location marker

### Units 105-108: Save Systems
- **Unit 105:** Game state encoding - what to save (position, inventory, quests, map)
- **Unit 106:** Password system - encode state to characters, entry screen
- **Unit 107:** Disk I/O fundamentals - Kernal routines, OPEN, PRINT#, INPUT#, CLOSE
- **Unit 108:** Disk save/load - write game state to file, read and restore

### Units 109-112: Menu System
- **Unit 109:** Title screen design - logo, options
- **Unit 110:** Main menu - new game, continue, options
- **Unit 111:** Pause menu - inventory, map, save, quit
- **Unit 112:** Game over screen - retry, password

**Phase Goal:** Complete UI with dual save systems (password and disk), map, and menus.

---

## Phase 8: Content and Polish (Units 113-128)
*Full dungeon content and release quality.*

### Units 113-116: Zone Design
- **Unit 113:** Zone 1: Starting village and surroundings (safe area)
- **Unit 114:** Zone 2: Forest dungeon (tutorial challenge)
- **Unit 115:** Zone 3: Cave dungeon (intermediate challenge)
- **Unit 116:** Zone 4: Castle dungeon (final challenge)

### Units 117-120: Boss Encounters
- **Unit 117:** Mini-boss 1 design - Forest guardian
- **Unit 118:** Mini-boss 2 design - Cave beast
- **Unit 119:** Final boss design - Castle lord
- **Unit 120:** Boss room integration - locked until conditions met

### Units 121-124: Audio Design
- **Unit 121:** Area music - theme per zone
- **Unit 122:** Combat music - boss battle theme
- **Unit 123:** Sound effects - comprehensive effect palette
- **Unit 124:** Audio integration - triggers, transitions

### Units 125-128: Polish and Distribution
- **Unit 125:** Balance tuning - difficulty curve across zones
- **Unit 126:** Bug fixing and edge cases
- **Unit 127:** D64 disk image creation - c1541, file layout, directory
- **Unit 128:** Release build - final testing, complete D64 distribution

**Phase Goal:** Complete, polished adventure game with D64 disk distribution.

---

## Summary

**Dungeon Crawl** at 128 units provides proper depth for a full adventure game:

**Phase 1 (Foundation):** Room system, tiles, rendering - the dungeon world exists.

**Phase 2 (Navigation):** Player, movement, transitions - explore the dungeon.

**Phase 3 (Items):** Collection, inventory, usage - gather resources and equipment.

**Phase 4 (Combat):** Attack, enemies, damage - face the dungeon's threats.

**Phase 5 (Adventure):** NPCs, dialogue, puzzles - adventure game depth.

**Phase 6 (Quests):** Objectives, tracking, rewards - meaningful progression.

**Phase 7 (Persistence):** Save, map, UI - professional game features.

**Phase 8 (Content):** Zones, bosses, polish - complete playable adventure.

### Skills Transferred Forward

The following skills debut in Dungeon Crawl and will be applied in future games:

1. **Multi-room architecture** → Isometric Quest (large world), Mega Blaster (scrolling world)
2. **Inventory system** → Arena Fighter (loadouts), Isometric Quest (full inventory)
3. **NPC dialogue** → Isometric Quest (extensive dialogue), Symphony's End
4. **Quest framework** → Isometric Quest, Symphony's End (story progression)
5. **Disk I/O and save** → All subsequent games with persistence
6. **D64 disk distribution** → All subsequent games (professional packaging)
7. **Environmental puzzles** → Isometric Quest (block puzzles), Symphony's End

### Comparison: 64 vs 128 Units

| System | 64-Unit Depth | 128-Unit Depth |
|--------|---------------|----------------|
| Room system | 4 units | 8 units |
| Movement/navigation | 8 units | 16 units |
| Items/inventory | 4 units | 16 units |
| Combat | 4 units | 16 units |
| NPCs/dialogue | 4 units | 16 units |
| Quest system | 4 units | 16 units |
| Save/UI | 4 units | 16 units |
| Content/polish | 8 units | 16 units |

### Game Specifications

- **Rooms:** 64+ connected rooms across 4 zones
- **Zones:** Village, Forest, Caves, Castle (themed areas)
- **Items:** Keys, potions, equipment, quest items, treasure
- **Enemies:** 8+ types with varied AI behaviours
- **Bosses:** 2 mini-bosses, 1 final boss
- **NPCs:** 15+ with dialogue and quest-giving
- **Puzzles:** Switches, push blocks, hidden passages, keys
- **Quests:** Main quest (3 stages) + 5 side quests
- **Save:** Dual system - password backup + disk save
- **Distribution:** D64 disk image
- **Features:** Map display, inventory screen, quest log
