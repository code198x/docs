# Crypt Crawler: 64-Unit Outline

**Game:** 6 of 16
**Platform:** Nintendo Entertainment System
**Units:** 64 (4 phases)
**Concept:** Flip-screen top-down exploration. Navigate dungeon rooms, collect items, avoid enemies. A proto-Zelda dungeon crawl.

---

## Why This Game Sixth?

Crypt Crawler introduces multi-room exploration and persistent state:

1. **Room-based structure** - Multiple connected screens
2. **Flip-screen transitions** - Move between rooms
3. **Persistent state** - Items stay collected
4. **Simple inventory** - Keys and items
5. **Chase AI** - Enemies follow player

This bridges single-screen games to larger explorable worlds.

---

## Skills Applied from Previous Games

| Skill | From | Application in Crypt Crawler |
|-------|------|----------------------------|
| Tile collision | Crate Escape | Wall collision |
| AI chase | Pellet Panic | Enemy behaviour |
| Object management | Stellar Barrage | Enemies, items |
| Background setup | All | Room rendering |

## New Skills Introduced

| Skill | Phase | Description |
|-------|-------|-------------|
| Room data structure | 1 | Storing multiple screens |
| Room connections | 1 | Exit definitions |
| Screen transitions | 2 | Flip-screen room change |
| Persistent state | 2 | Remembering collected items |
| Simple inventory | 3 | Keys and items carried |
| Key/door mechanics | 3 | Unlock with matching key |

---

## Phase 1: Room System (Units 1-16)
*Multiple rooms and display.*

### Units 1-4: Room Data
- **Unit 1:** Room structure - tiles, enemies, items, exits
- **Unit 2:** Room storage - efficient data format
- **Unit 3:** Multiple rooms - array of room data
- **Unit 4:** Room connections - exit definitions (N, S, E, W)

### Units 5-8: Room Display
- **Unit 5:** Room rendering - display current room
- **Unit 6:** Room colouring - attributes for variety
- **Unit 7:** Item display - show collectibles
- **Unit 8:** Exit indicators - doorways visible

### Units 9-12: Player Character
- **Unit 9:** Top-down player sprite - 4 directions
- **Unit 10:** 4-way movement - up, down, left, right
- **Unit 11:** Wall collision - stop at solid tiles
- **Unit 12:** Player in room - correct positioning

### Units 13-16: Basic World
- **Unit 13:** First room design - starting location
- **Unit 14:** Connected rooms - 4 rooms with exits
- **Unit 15:** Room variety - different layouts
- **Unit 16:** Player navigates - move within room

**Phase Goal:** Display connected rooms with player.

---

## Phase 2: Room Transitions (Units 17-32)
*Moving between rooms and persistence.*

### Units 17-20: Exit Detection
- **Unit 17:** Screen edge detection - player at boundary
- **Unit 18:** Exit collision - walking into exit
- **Unit 19:** Valid exit check - room exists that way?
- **Unit 20:** Direction tracking - which way player exits

### Units 21-24: Screen Transitions
- **Unit 21:** Clear current room - blank display briefly
- **Unit 22:** Load new room - switch room pointer
- **Unit 23:** Draw new room - render destination
- **Unit 24:** Player repositioning - appear at opposite edge

### Units 25-28: Persistent State
- **Unit 25:** Global item state - collected flags array
- **Unit 26:** Item collection - mark as collected
- **Unit 27:** Item visibility - only show uncollected
- **Unit 28:** State persists - items stay collected

### Units 29-32: World Building
- **Unit 29:** Larger world - 16 connected rooms
- **Unit 30:** Room themes - different colours/styles
- **Unit 31:** Dead ends and loops - interesting topology
- **Unit 32:** Complete exploration - navigate entire world

**Phase Goal:** Seamless room-to-room navigation.

---

## Phase 3: Game Elements (Units 33-48)
*Inventory, enemies, and objectives.*

### Units 33-36: Inventory System
- **Unit 33:** Inventory data - items player carries
- **Unit 34:** Item pickup - add to inventory
- **Unit 35:** Inventory display - show carried items
- **Unit 36:** Inventory limit - maximum items

### Units 37-40: Keys and Doors
- **Unit 37:** Door tiles - locked passages
- **Unit 38:** Key items - coloured keys
- **Unit 39:** Key matching - right key for right door
- **Unit 40:** Door unlocking - key consumed, door opens

### Units 41-44: Enemies
- **Unit 41:** Enemy placement - per room
- **Unit 42:** Patrol movement - back and forth
- **Unit 43:** Chase behaviour - follow player
- **Unit 44:** Player damage - health or instant death

### Units 45-48: Win Condition
- **Unit 45:** Goal item - treasure to find
- **Unit 46:** Exit location - where to bring treasure
- **Unit 47:** Win detection - treasure at exit
- **Unit 48:** Victory sequence - game complete

**Phase Goal:** Complete adventure gameplay.

---

## Phase 4: Polish and Release (Units 49-64)
*Presentation and release.*

### Units 49-52: Expanded World
- **Unit 49:** 32 rooms - full dungeon
- **Unit 50:** Hidden rooms - secret areas
- **Unit 51:** Multiple treasures - collection goals
- **Unit 52:** Balanced layout - fair placement

### Units 53-56: Audio
- **Unit 53:** Room transition sound - door effect
- **Unit 54:** Item collection sound - pickup
- **Unit 55:** Enemy contact sound - damage
- **Unit 56:** Victory fanfare - winning audio

### Units 57-60: Presentation
- **Unit 57:** Title screen - game logo
- **Unit 58:** Status bar - health, keys, items
- **Unit 59:** Room name display - location indicator
- **Unit 60:** Game over and victory screens

### Units 61-64: Release
- **Unit 61:** Instructions screen
- **Unit 62:** Map design finalisation
- **Unit 63:** Balance testing - difficulty
- **Unit 64:** Release build - final iNES ROM

**Phase Goal:** Complete flip-screen adventure.

---

## Summary

**Crypt Crawler** teaches multi-room exploration:

**Phase 1 (Rooms):** Room data, display, connections.

**Phase 2 (Transitions):** Screen changes, persistence.

**Phase 3 (Elements):** Inventory, keys, enemies.

**Phase 4 (Polish):** Expanded world, presentation.

### Skills Transferred Forward

1. **Room data structures** → All multi-screen games
2. **Screen transitions** → Metroidvania, larger games
3. **Persistent state** → Save systems, item tracking
4. **Simple inventory** → Adventure games
5. **Key/door mechanics** → Dungeon design

### Game Specifications

- **World:** 32 interconnected rooms
- **View:** Top-down, flip-screen
- **Player:** 16×16 sprite, 4 directions
- **Enemies:** 1-3 per room
- **Items:** Keys, treasures, health
- **Lives:** 3 (or health bar)
- **Mapper:** NROM
- **ROM Size:** 16KB PRG + 8KB CHR
- **Controls:** D-pad + A (action)
- **Audio:** APU effects
- **Distribution:** iNES ROM file
