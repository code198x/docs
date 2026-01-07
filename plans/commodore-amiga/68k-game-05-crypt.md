# Crypt: 64-Unit Outline

**Game:** 5 of 16 (68000 Assembly)
**Platform:** Commodore Amiga
**Language:** 68000 Assembly
**Units:** 64 (4 phases)
**Concept:** Flip-screen top-down exploration. Navigate dungeon rooms.

---

## Why This Game Fifth?

Crypt introduces multi-screen design:

1. **Room transitions** - Copper-based screen changes
2. **Tile rendering** - Efficient Blitter tile drawing
3. **Persistent state** - Items remain collected
4. **Key/door mechanics** - Inventory puzzles
5. **Chase AI** - Enemy following behaviour

First exploration-focused game in the sequence.

---

## Skills Applied from Previous Games

| Skill | From | Application |
|-------|------|-------------|
| BOB rendering | Ascent | Player, enemies |
| Collision | Ascent | Walls, items |
| Enemy AI | Ascent | Chase behaviour |
| Blitter operations | All | Tile rendering |
| Object tracking | Blast Zone | Inventory |

## New Skills Introduced

| Skill | Phase | Description |
|-------|-------|-------------|
| Tile-based maps | 1 | Room structure |
| Blitter tiles | 1 | Efficient drawing |
| Screen transitions | 2 | Copper effects |
| Persistent state | 3 | Item tracking |
| Inventory system | 3 | Key collection |

---

## Phase 1: Room System (Units 1-16)
*Tile-based room rendering.*

### Units 1-4: Tile Basics
- **Unit 1:** Tile concept - grid-based rooms
- **Unit 2:** Tile data - 16×16 or 32×32 pixels
- **Unit 3:** Tile set - walls, floors, objects
- **Unit 4:** Room array - tile indices

### Units 5-8: Blitter Tiles
- **Unit 5:** Tile rendering - Blitter copy
- **Unit 6:** Tile sheet - source graphics
- **Unit 7:** Efficient rendering - sequential
- **Unit 8:** Room drawing - full screen

### Units 9-12: Room Data
- **Unit 9:** Room structure - dimensions, tiles
- **Unit 10:** Room connections - exits
- **Unit 11:** Room objects - items, doors
- **Unit 12:** Multiple rooms - world data

### Units 13-16: Player in Room
- **Unit 13:** Player sprite - top-down view
- **Unit 14:** Grid movement - tile-aligned
- **Unit 15:** Wall collision - can't walk through
- **Unit 16:** Room demo - player walking

**Phase Goal:** Tile-rendered rooms.

---

## Phase 2: Transitions and Display (Units 17-32)
*Screen changes and Copper effects.*

### Units 17-20: Copper Transitions
- **Unit 17:** Fade effect - palette manipulation
- **Unit 18:** Fade out - darken colours
- **Unit 19:** Fade in - brighten colours
- **Unit 20:** Transition sequence - out/in

### Units 21-24: Room Transitions
- **Unit 21:** Exit detection - room edge
- **Unit 22:** Next room - load data
- **Unit 23:** Entry position - where player appears
- **Unit 24:** Smooth transition - fade between

### Units 25-28: Room Variety
- **Unit 25:** Wall themes - different graphics
- **Unit 26:** Floor types - stone, grass
- **Unit 27:** Decorations - non-collision tiles
- **Unit 28:** Room atmosphere - colour schemes

### Units 29-32: Display Polish
- **Unit 29:** Status bar - HUD area
- **Unit 30:** Room name - display
- **Unit 31:** Minimap concept
- **Unit 32:** Screen layout - game + HUD

**Phase Goal:** Room transitions working.

---

## Phase 3: Items and Inventory (Units 33-48)
*Collection and keys.*

### Units 33-36: Item System
- **Unit 33:** Item sprites - keys, health, treasure
- **Unit 34:** Item placement - per room
- **Unit 35:** Item collision - pick up
- **Unit 36:** Item removal - from room

### Units 37-40: Key/Door Mechanics
- **Unit 37:** Key colours - red, blue, yellow, green
- **Unit 38:** Key collection - add to inventory
- **Unit 39:** Door sprites - locked doors
- **Unit 40:** Door unlocking - key consumption

### Units 41-44: Persistent State
- **Unit 41:** Item tracking - global array
- **Unit 42:** Room state - what's collected
- **Unit 43:** State on room re-entry
- **Unit 44:** Door state - open stays open

### Units 45-48: Inventory Display
- **Unit 45:** Inventory HUD - key icons
- **Unit 46:** Health display - hearts
- **Unit 47:** Treasure count - score
- **Unit 48:** Inventory demo - working system

**Phase Goal:** Keys and doors working.

---

## Phase 4: Enemies and Completion (Units 49-64)
*AI and game finish.*

### Units 49-52: Chase AI
- **Unit 49:** Enemy sprites - skeletons, bats
- **Unit 50:** Enemy placement - per room
- **Unit 51:** Chase algorithm - toward player
- **Unit 52:** Chase speed - slower than player

### Units 53-56: Combat
- **Unit 53:** Enemy collision - damage player
- **Unit 54:** Health system - hit points
- **Unit 55:** Health pickups - restoration
- **Unit 56:** Enemy respawn - on room re-entry

### Units 57-60: Audio
- **Unit 57:** Footsteps - movement sound
- **Unit 58:** Door sounds - open, locked
- **Unit 59:** Enemy sounds - spotted, attack
- **Unit 60:** Ambient music - dungeon theme

### Units 61-64: Release
- **Unit 61:** Dungeon layout - 16+ rooms
- **Unit 62:** Goal room - escape
- **Unit 63:** Full testing
- **Unit 64:** Release build - ADF

**Phase Goal:** Complete dungeon exploration.

---

## Summary

**Crypt** teaches multi-room exploration.

### Technical Specifications

- **Display:** 320×256, 5 bitplanes
- **Player:** BOB sprite, 4-directional
- **Rooms:** Tile-based, Blitter-rendered
- **Items:** Keys (4 colours), health, treasure
- **Doors:** Locked, require matching key
- **Enemies:** Chase AI
- **Transitions:** Copper fade effects
- **Distribution:** Bootable ADF

### Skills for Next Game

- Tile-based map rendering
- Copper transition effects
- Persistent game state
- Inventory systems
- Chase AI behaviour
