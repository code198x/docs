# Phase 2: Solid Ground

**Game:** Dash (NES Game 1)
**Units:** 17-32
**Theme:** Tile-based level design with metatiles, platform types, and animation
**6502 Focus:** Indexed addressing (LDA table,X), 16-bit pointer arithmetic, indirect indexed addressing, data-driven design
**Hardware:** Nametable ($2006/$2007), attribute table, OAM sprite attributes (flip bits)
**Status:** Planned

---

## Overview

Phase 2 transforms the single-screen prototype into a real level design system. The key abstraction is the metatile: a 2x2 group of tiles that forms a single logical block. Levels are designed as grids of metatile indices -- one byte per 16x16 pixel area. This reduces data size, simplifies collision (check one metatile instead of four tiles), and aligns perfectly with the NES attribute table's 16x16 colour zones.

Multiple platform types appear: solid (stand and block), one-way (jump through from below, land from above), and ladders (vertical movement). Player animation -- run cycle, facing direction, idle, jump -- brings the character to life. Multiple levels with transitions and visual themes make this feel like a real game.

---

## Prerequisites from Phase 1

- NMI handler with OAM DMA and VBlank PPU writes
- Controller input reading ($4016 strobe protocol)
- Basic tile collision (solid floor check)
- Sprite rendering and zero-page game state
- JSR/RTS subroutine pattern

---

## Unit Progression

| Unit | Title | New 6502 Concept | Game Addition |
|------|-------|------------------|---------------|
| 17 | Metatile Data Structure | 16-bit pointers, 4-byte tile groups | Building blocks defined |
| 18 | Level Data (Metatile Grid) | Indirect indexed addressing, row/column calculation | Data-driven level |
| 19 | Level Renderer | Nametable fill from level data (rendering off) | **Level from data** |
| 20 | Attribute Table from Metatiles | Bit packing (4 metatiles per byte) | Correct colours |
| 21 | One-Way Platforms | Collision flag per metatile, check only when falling | Jump through from below |
| 22 | Ladder Tiles | Vertical movement when overlapping ladder metatile | Climbing |
| 23 | Player Run Animation | Sprite cycling between 2-4 frames, frame counter | Visual life |
| 24 | Player Facing Direction | OAM attribute bit 6 (horizontal flip) | Left and right |
| 25 | Idle and Jump Sprites | State-based sprite selection | Complete animation set |
| 26 | Level Exit | Door/flag metatile triggers level complete | Goal |
| 27 | Second Level | Level pointer table, load new level | Progression |
| 28 | Level Transition Effect | Palette fade to black via VBlank writes | Polish |
| 29 | Metatile Themes | Different tile indices per level theme | Visual variety |
| 30 | Coin Counter | Separate collectible count, HUD display | Collection goal |
| 31 | All Coins = Bonus | Level-end bonus for 100% collection | Completionist reward |
| 32 | Integration + Level Design | Layout tuning, collision polish, flow testing | Well-designed levels |

---

## Key Teaching Moments

### Metatiles (Unit 17)

A metatile is 4 tiles in a 2x2 square plus a collision type:

```asm
; Metatile definition: 4 tile indices + collision type
; metatile 0 = empty (background)
metatile_tl: .byte $00, $10, $14, $18, $1C  ; top-left tile per metatile
metatile_tr: .byte $00, $11, $15, $19, $1D  ; top-right
metatile_bl: .byte $00, $12, $16, $1A, $1E  ; bottom-left
metatile_br: .byte $00, $13, $17, $1B, $1F  ; bottom-right
metatile_col: .byte $00, $01, $02, $03, $01 ; collision: 0=empty, 1=solid, 2=one-way, 3=ladder
```

One metatile index = one byte in level data = 16x16 pixels on screen. A screen-sized level (16 wide x 15 tall) is just 240 bytes.

### Attribute Table Alignment (Unit 20)

The NES attribute table colours 32x32 pixel areas (4x4 tiles). Each byte covers a 2x2 group of metatiles. The bit packing:

```asm
; attribute = (top-left palette) | (top-right << 2) | (bottom-left << 4) | (bottom-right << 6)
; Each metatile has a palette index (0-3)
metatile_pal: .byte $00, $01, $02, $01, $03  ; palette per metatile type
```

Metatiles are 16x16 -- exactly half the attribute area. Two metatiles per attribute quadrant aligns perfectly. This is why metatiles are 2x2 tiles on the NES.

### One-Way Platforms (Unit 21)

One-way platforms only block from above. The check: is the player falling (velocity_y > 0)? Is the player's bottom edge at the platform's top edge? If both, land. Otherwise, pass through. One flag in the metatile collision table, one extra comparison in the collision routine.

---

## 6502 Concepts Introduced

1. Indexed addressing (`LDA metatile_tl,X`) -- access arrays by index (Unit 17)
2. 16-bit pointer arithmetic -- calculate level data addresses (Unit 18)
3. Indirect indexed addressing (`LDA (ptr),Y`) -- read from calculated addresses (Unit 18)
4. Bit packing for attribute table -- shift and OR operations (Unit 20)
5. Collision type dispatch -- compare and branch chain (Unit 21)
6. Frame counter for animation -- `INC` + `AND` mask for timing (Unit 23)
7. OAM attribute bit manipulation -- horizontal flip via bit 6 (Unit 24)
8. State-based sprite selection -- lookup table indexed by player state (Unit 25)
9. Level pointer table -- indexed access to level addresses (Unit 27)
10. Palette fade -- decrement colour values during VBlank (Unit 28)

---

## Hardware

### New in Phase 2

| Resource | Purpose | Introduced |
|----------|---------|------------|
| Attribute table ($23C0-$23FF) | 2-bit palette selection per 32x32 area | Unit 20 |
| OAM attribute bit 6 | Horizontal sprite flip | Unit 24 |

---

## Game State at Phase End

After Unit 32:

- **Metatile system** -- 2x2 tile groups with collision types and palettes
- **Data-driven levels** -- levels stored as metatile grids, rendered to nametable
- **One-way platforms** -- jump through from below, land from above
- **Ladders** -- climb up and down
- **Player animation** -- run cycle, idle, jump, fall, facing direction
- **Multiple levels** -- at least 2 levels with transitions
- **Level themes** -- different tile sets per level
- **Coin counter** -- separate from score, 100% bonus
- **Palette fade** -- smooth transitions between levels

Looks and plays like a real platformer. Metatiles are the foundation for everything that follows.

---

## What Carries to Phase 3

- **Metatile collision system** -- extended with crumbling platforms, spring tiles, conveyors
- **Animation state machine** -- expanded with damage, death, special move states
- **Level data format** -- extended for longer levels in Phase 4
- **Attribute table handling** -- reused for scroll seam updates

---

**Version:** 1.0
**Last Updated:** 2026-02-06
