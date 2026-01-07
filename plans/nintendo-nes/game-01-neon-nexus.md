# Neon Nexus: 64-Unit Outline

**Game:** 1 of 16
**Platform:** Nintendo Entertainment System
**Units:** 64 (4 phases)
**Concept:** Fixed-screen action game. Navigate a digital grid, collect data cores, avoid security programs. A futuristic introduction to NES development.

---

## Why This Game First?

Neon Nexus teaches PPU fundamentals - the heart of NES development:

1. **Pattern tables** - Understanding tile-based graphics
2. **Nametables** - Building backgrounds from tiles
3. **Sprites and OAM** - Moving objects via Object Attribute Memory
4. **Palettes** - NES colour system (4 palettes × 4 colours)
5. **Controller input** - Reading the NES gamepad

Everything on NES is tiles. This game teaches thinking in tiles from day one.

---

## NES-Specific Concepts

The NES has unique hardware that differs from other platforms:

| Component | Purpose | Key Details |
|-----------|---------|-------------|
| PPU | Graphics chip | Separate from CPU, timing-critical |
| Pattern Tables | Tile definitions | Two 4KB tables (CHR-ROM) |
| Nametables | Screen layout | 32×30 tiles per screen |
| OAM | Sprite data | 64 sprites, 8 per scanline |
| APU | Sound chip | 5 channels (2 pulse, triangle, noise, DMC) |

---

## Phase 1: PPU Foundation (Units 1-16)
*Understanding the Picture Processing Unit.*

### Units 1-4: NES Architecture
- **Unit 1:** NES overview - CPU, PPU, APU, memory map
- **Unit 2:** 6502 assembly basics - registers, instructions
- **Unit 3:** iNES ROM format - header, PRG-ROM, CHR-ROM
- **Unit 4:** Development environment - assembler, emulator

### Units 5-8: Pattern Tables
- **Unit 5:** Tile concept - 8×8 pixel building blocks
- **Unit 6:** CHR-ROM structure - pattern table layout
- **Unit 7:** Tile editor basics - creating tiles
- **Unit 8:** Pattern table organisation - sprites vs background

### Units 9-12: Nametables and Palettes
- **Unit 9:** Nametable structure - 32×30 tile references
- **Unit 10:** Attribute table - palette assignment per 16×16 area
- **Unit 11:** Palette setup - 4 background + 4 sprite palettes
- **Unit 12:** VRAM writes - PPU address and data ports

### Units 13-16: Basic Display
- **Unit 13:** PPU initialisation - proper startup sequence
- **Unit 14:** NMI (VBlank) - when to update PPU
- **Unit 15:** Background display - showing the playfield
- **Unit 16:** First display - static screen visible

**Phase Goal:** Display a static background using PPU.

---

## Phase 2: Sprites and Movement (Units 17-32)
*Moving objects via OAM.*

### Units 17-20: OAM Basics
- **Unit 17:** Sprite structure - Y, tile, attributes, X
- **Unit 18:** OAM memory - 256 bytes for 64 sprites
- **Unit 19:** OAM DMA - fast sprite upload ($4014)
- **Unit 20:** Sprite display - single sprite on screen

### Units 21-24: Player Sprite
- **Unit 21:** Player tile design - character graphics
- **Unit 22:** Player variables - X, Y position in RAM
- **Unit 23:** Sprite positioning - updating OAM data
- **Unit 24:** Player on screen - static player visible

### Units 25-28: Controller Input
- **Unit 25:** Controller registers - $4016, $4017
- **Unit 26:** Reading controller - strobe and shift
- **Unit 27:** Button state - storing current buttons
- **Unit 28:** Movement input - D-pad affects position

### Units 29-32: Player Movement
- **Unit 29:** Movement logic - update position from input
- **Unit 30:** Screen boundaries - keep player on screen
- **Unit 31:** Smooth movement - consistent speed
- **Unit 32:** Controllable player - moves around playfield

**Phase Goal:** Player sprite moves with controller input.

---

## Phase 3: Game Elements (Units 33-48)
*Enemies, items, and collision.*

### Units 33-36: Enemy Sprites
- **Unit 33:** Enemy tile design - security program graphics
- **Unit 34:** Enemy data structure - X, Y, direction, active
- **Unit 35:** Multiple enemies - enemy array
- **Unit 36:** Enemy display - render all enemies

### Units 37-40: Enemy Movement
- **Unit 37:** Simple AI - move in patterns
- **Unit 38:** Patrol behaviour - back and forth
- **Unit 39:** Chase behaviour - move toward player
- **Unit 40:** Enemy variety - different movement types

### Units 41-44: Collectibles
- **Unit 41:** Item tiles - data core graphics
- **Unit 42:** Item placement - positions on playfield
- **Unit 43:** Item display - render uncollected items
- **Unit 44:** Item counter - track collected items

### Units 45-48: Collision Detection
- **Unit 45:** Bounding box concept - collision rectangles
- **Unit 46:** Player-item collision - collecting items
- **Unit 47:** Player-enemy collision - taking damage
- **Unit 48:** Game mechanics - collect all items to win

**Phase Goal:** Complete game mechanics working.

---

## Phase 4: Polish and Release (Units 49-64)
*Sound, presentation, and release.*

### Units 49-52: APU Basics
- **Unit 49:** APU overview - 5 sound channels
- **Unit 50:** Pulse channel - square wave setup
- **Unit 51:** Sound effects - collect, hit, game over
- **Unit 52:** Simple music - title screen tune

### Units 53-56: Game Flow
- **Unit 53:** Lives system - 3 lives
- **Unit 54:** Game over detection - no lives left
- **Unit 55:** Level complete - all items collected
- **Unit 56:** Multiple levels - increasing difficulty

### Units 57-60: Presentation
- **Unit 57:** Title screen - game logo and "PRESS START"
- **Unit 58:** HUD display - score and lives
- **Unit 59:** Game over screen - final message
- **Unit 60:** Victory screen - level complete

### Units 61-64: Release
- **Unit 61:** Instructions - controls display
- **Unit 62:** Bug fixing - edge cases
- **Unit 63:** Balance tuning - enemy speed, item count
- **Unit 64:** Release build - final iNES ROM

**Phase Goal:** Complete, polished NES game.

---

## Summary

**Neon Nexus** teaches NES PPU fundamentals:

**Phase 1 (PPU):** Pattern tables, nametables, palettes.

**Phase 2 (Sprites):** OAM, player movement, controller input.

**Phase 3 (Game):** Enemies, items, collision detection.

**Phase 4 (Polish):** APU basics, game flow, release.

### Skills Transferred Forward

1. **PPU understanding** → All NES games
2. **OAM sprite management** → All games with moving objects
3. **Controller reading** → All NES games
4. **NMI timing** → Frame-based updates throughout
5. **Collision detection** → All action games
6. **APU basics** → Sound in all games

### NES-Specific Learning

| Concept | What Students Learn |
|---------|-------------------|
| CHR-ROM | Tiles stored separately from code |
| Nametables | Building screens from tiles |
| Attribute tables | Colour limitations per area |
| OAM DMA | Fast sprite upload technique |
| VBlank | When it's safe to update PPU |

### Game Specifications

- **Display:** Single fixed screen
- **Player:** 8×8 or 8×16 sprite
- **Enemies:** 4-8 on screen
- **Items:** 10-20 per level
- **Levels:** 4-8 with increasing difficulty
- **Lives:** 3
- **Mapper:** NROM (no banking)
- **ROM Size:** 16KB PRG + 8KB CHR
- **Controls:** D-pad only
- **Audio:** APU effects + simple music
- **Distribution:** iNES ROM file
