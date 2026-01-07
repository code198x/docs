# Chambers: 64-Unit Outline

**Game:** 5 of 16
**Platform:** ZX Spectrum
**Units:** 64 (4 phases)
**Concept:** Flip-screen top-down exploration. Navigate rooms, collect items, avoid enemies. Atic Atac territory.

---

## Why This Game Fifth?

Chambers introduces multi-room navigation and persistent state - the foundation for adventure and exploration games:

1. **Room-based structure** - Multiple screens connected
2. **Flip-screen transitions** - Move between rooms
3. **Persistent state** - Items stay collected, doors stay open
4. **Simple inventory** - Keys unlock doors
5. **Enemy AI** - Chase behaviour

This bridges single-screen games to larger explorable worlds.

---

## Skills Applied from Previous Games

| Skill | From | Application in Chambers |
|-------|------|------------------------|
| Screen memory | Ink War | Room graphics |
| Attributes | Ink War | Room colouring |
| Tile-based levels | Cavern | Room layouts |
| Software sprites | Shatter | Player, enemies, items |
| Object arrays | Skyfire | Enemy and item management |
| Collision detection | All | Walls, items, enemies |
| Frame timing | Shatter | Smooth movement |

## New Skills Introduced

| Skill | Phase | Description |
|-------|-------|-------------|
| Room data structure | 1 | Storing multiple screens |
| Room connections | 1 | Which exit leads where |
| Screen transitions | 2 | Flip-screen room change |
| Persistent state | 2 | Remembering collected items |
| Simple inventory | 3 | Keys, items carried |
| Chase AI | 3 | Enemy follows player |
| Locked doors | 3 | Key-colour matching |

---

## Phase 1: Room System (Units 1-16)
*Multiple rooms and display.*

### Units 1-4: Room Data
- **Unit 1:** Room structure - tiles, enemies, items, exits
- **Unit 2:** Room storage - efficient data format
- **Unit 3:** Multiple rooms - array of room data
- **Unit 4:** Room connections - exit definitions (N, S, E, W)

### Units 5-8: Room Display
- **Unit 5:** Room rendering - display current room tiles
- **Unit 6:** Room colouring - attributes for variety
- **Unit 7:** Item display - show collectible objects
- **Unit 8:** Exit indicators - door graphics at edges

### Units 9-12: Player Character
- **Unit 9:** Top-down player sprite - 4-direction views
- **Unit 10:** 4-way movement - up, down, left, right
- **Unit 11:** Wall collision - stop at solid tiles
- **Unit 12:** Player in room - correct initial position

### Units 13-16: Basic World
- **Unit 13:** First room design - starting location
- **Unit 14:** Connected rooms - 4 rooms with exits
- **Unit 15:** Room variety - different tile layouts
- **Unit 16:** Complete display - player in explorable area

**Phase Goal:** Display connected rooms with player navigation.

---

## Phase 2: Room Transitions (Units 17-32)
*Moving between rooms and persistence.*

### Units 17-20: Exit Detection
- **Unit 17:** Screen edge detection - player at boundary
- **Unit 18:** Exit collision - walking into exit
- **Unit 19:** Valid exit check - is there a room that way?
- **Unit 20:** Direction tracking - which way did player exit

### Units 21-24: Screen Transitions
- **Unit 21:** Clear current room - erase display
- **Unit 22:** Load new room - switch room pointer
- **Unit 23:** Draw new room - render destination
- **Unit 24:** Player repositioning - appear at opposite edge

### Units 25-28: Persistent State
- **Unit 25:** Global item state - array of collected flags
- **Unit 26:** Item collection - mark item as collected
- **Unit 27:** Item visibility - only show uncollected items
- **Unit 28:** State across transitions - items stay collected

### Units 29-32: World Exploration
- **Unit 29:** Larger world - 16 connected rooms
- **Unit 30:** Room variety - different themes/colours
- **Unit 31:** Dead ends and loops - interesting topology
- **Unit 32:** Complete exploration - navigate entire world

**Phase Goal:** Seamless room-to-room navigation with persistence.

---

## Phase 3: Game Elements (Units 33-48)
*Inventory, enemies, and objectives.*

### Units 33-36: Inventory System
- **Unit 33:** Inventory data - what player carries
- **Unit 34:** Item pickup - add to inventory
- **Unit 35:** Inventory display - show carried items
- **Unit 36:** Inventory limit - maximum items carried

### Units 37-40: Keys and Doors
- **Unit 37:** Door tiles - locked doors in rooms
- **Unit 38:** Key items - coloured keys
- **Unit 39:** Door-key matching - right key for right door
- **Unit 40:** Door unlocking - key consumed, door opens

### Units 41-44: Enemies
- **Unit 41:** Enemy placement - enemies per room
- **Unit 42:** Enemy movement - simple patrol
- **Unit 43:** Chase behaviour - enemy follows player
- **Unit 44:** Player damage - health or instant death

### Units 45-48: Win Condition
- **Unit 45:** Goal item - treasure to find
- **Unit 46:** Exit location - where to bring treasure
- **Unit 47:** Win detection - treasure at exit
- **Unit 48:** Victory sequence - game completion

**Phase Goal:** Complete adventure with items, enemies, and goals.

---

## Phase 4: Polish and Release (Units 49-64)
*Presentation and final polish.*

### Units 49-52: Expanded World
- **Unit 49:** 32-room world - full exploration space
- **Unit 50:** Hidden rooms - secret areas
- **Unit 51:** Multiple treasures - collect several items
- **Unit 52:** Balanced layout - fair item placement

### Units 53-56: Audio and Feedback
- **Unit 53:** Room transition sound - door/exit effect
- **Unit 54:** Item collection sound - pickup feedback
- **Unit 55:** Enemy contact sound - damage/death
- **Unit 56:** Victory fanfare - winning audio

### Units 57-60: Presentation
- **Unit 57:** Title screen - game logo
- **Unit 58:** Lives/health display - status bar
- **Unit 59:** Room name display - location indicator
- **Unit 60:** Game over and victory screens

### Units 61-64: Release
- **Unit 61:** Instructions - controls and objectives
- **Unit 62:** Map design finalisation - world layout
- **Unit 63:** Balance testing - item and enemy placement
- **Unit 64:** Release build - final TAP file

**Phase Goal:** Complete flip-screen adventure game.

---

## Summary

**Chambers** teaches multi-room exploration fundamentals:

**Phase 1 (Rooms):** Room data, display, connections - world exists.

**Phase 2 (Transitions):** Screen changes, persistence - exploration works.

**Phase 3 (Elements):** Inventory, keys, enemies - adventure gameplay.

**Phase 4 (Polish):** Full world, audio, presentation - complete game.

### Skills Transferred Forward

The following skills debut in Chambers:

1. **Room data structures** → All multi-screen games
2. **Screen transitions** → Dungeon Crawl, Bastion, large games
3. **Persistent state** → Save systems, item tracking
4. **Simple inventory** → Adventure games, RPG elements
5. **Key/door mechanics** → Dungeon Crawl, Bastion
6. **Chase AI** → Enemy behaviour throughout curriculum

### Classic Spectrum Heritage

Chambers pays homage to:
- **Atic Atac** (1983) - Ultimate's flip-screen adventure
- **Sabre Wulf** (1984) - Jungle exploration
- **Underwurlde** (1984) - Expanded exploration

These games pioneered exploration on the Spectrum.

### Game Specifications

- **World:** 32 interconnected rooms
- **View:** Top-down, flip-screen transitions
- **Player:** 16×16 sprite, 4 directions
- **Enemies:** 1-3 per room, chase behaviour
- **Items:** Keys (4 colours), treasures, health
- **Doors:** Colour-coded, require matching key
- **Objective:** Collect treasures, find exit
- **Lives:** 3 (or health bar)
- **Controls:** 4-way movement, action button
- **Audio:** Beeper effects
- **Distribution:** TAP file
