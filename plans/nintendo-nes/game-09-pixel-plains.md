# Pixel Plains: 64-Unit Outline

**Game:** 9 of 16
**Platform:** Nintendo Entertainment System
**Units:** 64 (4 phases)
**Concept:** Side-scrolling platformer. Run and jump through the plains, avoid enemies, collect coins. The NES's signature genre.

---

## Why This Game Ninth?

Pixel Plains introduces NES hardware scrolling - the platform's signature feature:

1. **Hardware scrolling** - NES scroll registers
2. **Nametable management** - Two-screen arrangement
3. **Camera following** - Scroll tracks player
4. **Large levels** - Bigger than one screen
5. **Scrolling collision** - Collision in scrolling world

This is Super Mario Bros. territory - the quintessential NES game type.

---

## Skills Applied from Previous Games

| Skill | From | Application in Pixel Plains |
|-------|------|---------------------------|
| Platformer physics | Crate Escape | Jumping, gravity |
| Tile collision | Crate Escape | Platform collision |
| Object management | Stellar Barrage | Enemies, items |
| Player animation | Crate Escape | Walk, jump, idle |

## New Skills Introduced

| Skill | Phase | Description |
|-------|-------|-------------|
| Scroll registers | 1 | PPU scroll control |
| Nametable switching | 1 | Two-screen management |
| Camera following | 2 | Scroll tracks player |
| Off-screen entities | 2 | Enemies beyond view |
| Level streaming | 3 | Loading level columns |
| Metatile columns | 3 | Efficient level data |

---

## Phase 1: Scrolling Foundation (Units 1-16)
*NES hardware scrolling basics.*

### Units 1-4: Scroll Registers
- **Unit 1:** PPU scroll concept - $2005 register
- **Unit 2:** Scroll X - horizontal offset
- **Unit 3:** Fine vs coarse scroll - pixel and tile
- **Unit 4:** Scroll during rendering - split scroll

### Units 5-8: Nametable Arrangement
- **Unit 5:** Nametable layout - 4 logical screens
- **Unit 6:** Mirroring modes - horizontal, vertical
- **Unit 7:** Two-screen scrolling - nametable switching
- **Unit 8:** Seamless scroll - no visible seams

### Units 9-12: Level Data
- **Unit 9:** Level format - column-based data
- **Unit 10:** Metatiles - 2×2 blocks
- **Unit 11:** Level width - wider than screen
- **Unit 12:** Initial level display - first screen

### Units 13-16: Basic Scrolling
- **Unit 13:** Manual scroll - test scroll movement
- **Unit 14:** Scroll limits - level start and end
- **Unit 15:** Scroll speed - consistent rate
- **Unit 16:** Scrolling foundation - background moves

**Phase Goal:** Hardware scrolling working.

---

## Phase 2: Camera and Player (Units 17-32)
*Player movement with camera.*

### Units 17-20: Camera System
- **Unit 17:** Camera position - scroll offset tracking
- **Unit 18:** Player-centred - scroll follows player
- **Unit 19:** Dead zone - tolerance for small moves
- **Unit 20:** Camera boundaries - level edge limits

### Units 21-24: World Coordinates
- **Unit 21:** World vs screen - position types
- **Unit 22:** World position - player in level
- **Unit 23:** Screen conversion - world to screen
- **Unit 24:** Tile lookup - tile at world position

### Units 25-28: Scrolling Collision
- **Unit 25:** Ground detection - in scrolling world
- **Unit 26:** Wall collision - scrolling walls
- **Unit 27:** Platform standing - while scrolling
- **Unit 28:** Complete physics - smooth scrolling platforming

### Units 29-32: Column Updates
- **Unit 29:** New column detection - scroll reveals new area
- **Unit 30:** Column rendering - draw new column
- **Unit 31:** Attribute updates - colours for new area
- **Unit 32:** Seamless updates - no visible pop-in

**Phase Goal:** Player moves through scrolling level.

---

## Phase 3: Game Elements (Units 33-48)
*Enemies, items, and hazards.*

### Units 33-36: Scrolling Enemies
- **Unit 33:** Enemy world position - in level coordinates
- **Unit 34:** Enemy activation - spawn when near
- **Unit 35:** Enemy screen rendering - convert to screen
- **Unit 36:** Enemy deactivation - remove when far

### Units 37-40: Enemy Behaviours
- **Unit 37:** Walking enemy - patrol pattern
- **Unit 38:** Jumping enemy - hops around
- **Unit 39:** Flying enemy - aerial movement
- **Unit 40:** Enemy collision - damage player

### Units 41-44: Collectibles
- **Unit 41:** Coin placement - in level data
- **Unit 42:** Coin display - render in world
- **Unit 43:** Coin collection - player touches
- **Unit 44:** Score tracking - points from coins

### Units 45-48: Level Goals
- **Unit 45:** Level end marker - goal position
- **Unit 46:** Level complete - reaching goal
- **Unit 47:** Level transition - load next level
- **Unit 48:** Multiple levels - progression

**Phase Goal:** Complete scrolling platformer gameplay.

---

## Phase 4: Polish and Release (Units 49-64)
*Audio, presentation, and release.*

### Units 49-52: Audio
- **Unit 49:** Jump sound - player jumping
- **Unit 50:** Coin sound - collection feedback
- **Unit 51:** Enemy stomp sound - defeating enemy
- **Unit 52:** Background music - level theme

### Units 53-56: Game Flow
- **Unit 53:** Lives system - multiple attempts
- **Unit 54:** Checkpoints - mid-level restart
- **Unit 55:** Game over - no lives
- **Unit 56:** Continue system - retry level

### Units 57-60: Presentation
- **Unit 57:** Title screen - game logo
- **Unit 58:** Level intro - world and level number
- **Unit 59:** HUD - score, lives, time
- **Unit 60:** Victory screen - level complete

### Units 61-64: Release
- **Unit 61:** Instructions screen
- **Unit 62:** Level design polish
- **Unit 63:** Scroll optimisation - smooth performance
- **Unit 64:** Release build - final iNES ROM

**Phase Goal:** Complete side-scrolling platformer.

---

## Summary

**Pixel Plains** teaches NES hardware scrolling:

**Phase 1 (Scrolling):** Scroll registers, nametables.

**Phase 2 (Camera):** Player following, world coordinates.

**Phase 3 (Elements):** Enemies, items, levels.

**Phase 4 (Polish):** Audio, presentation, release.

### Skills Transferred Forward

1. **Hardware scrolling** → All scrolling NES games
2. **Camera following** → Standard for platformers
3. **World coordinates** → Large level design
4. **Column updates** → Efficient scrolling
5. **Entity activation** → Performance management

### NES-Specific Learning

| Concept | What Students Learn |
|---------|-------------------|
| $2005 register | PPU scroll control |
| Nametable mirroring | Two-screen arrangement |
| Column rendering | VBlank-safe updates |
| Split scrolling | Status bar techniques |

### Game Specifications

- **Levels:** 4+ stages, each 4-8 screens wide
- **Player:** 16×16 sprite with animations
- **Physics:** Gravity, variable jump
- **Enemies:** 4+ types
- **Collectibles:** Coins, power-ups
- **Lives:** 3
- **Mapper:** NROM
- **ROM Size:** 32KB PRG + 8KB CHR
- **Controls:** D-pad + A (jump)
- **Audio:** APU effects + music
- **Distribution:** iNES ROM file
