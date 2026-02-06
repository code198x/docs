# Phase 5: Pattern Table

**Game:** Dash (NES Game 1)
**Units:** 65-80
**Theme:** Visual polish -- CHR art, tile themes, metasprites, colour
**6502 Focus:** CHR data format (2-bitplane tiles), attribute table mastery, lookup tables, Sprite 0 techniques
**Hardware:** Pattern tables ($0000/$1000 in CHR ROM), attribute table ($23C0), Sprite 0 hit
**Status:** Planned

---

## Overview

Until now, the game uses placeholder tiles -- functional but generic. Phase 5 transforms the look with custom CHR art. The player becomes a recognisable character (16x16 metasprite). Platforms become stone, grass, wood. Backgrounds show sky, mountains, caves. Each level theme has its own palette.

The NES's 2-bitplane tile format means 4 colours per tile, selected from a 4-colour palette. There are 4 background palettes and 4 sprite palettes, each chosen from the NES's 64-colour master palette. The constraint forces clarity -- every pixel earns its place.

Parallax scrolling via Sprite 0 hit adds depth. The sky scrolls at half speed behind the level. Tile animation (water, lava) brings the world to life. By Phase 5's end, screenshots sell the game.

---

## Prerequisites from Phase 4

- Hardware scrolling with nametable seam loading
- Sprite 0 hit for status bar split
- VBlank budget management
- Metatile system with level data

---

## Unit Progression

| Unit | Title | New 6502 Concept | Game Addition |
|------|-------|------------------|---------------|
| 65 | CHR Tile Design | 2-bitplane format: 8+8 bytes per tile, 4 colours | Custom tiles |
| 66 | Outdoor Theme | Trees, grass, hills, sky, clouds | First theme |
| 67 | Underground Theme | Rock, dirt, crystals, lava glow | Second theme |
| 68 | Player Metasprite (16x16) | 4 OAM entries composited, table-driven | **Recognisable character** |
| 69 | Metasprite Routine | Reusable table-driven multi-sprite renderer | System for all entities |
| 70 | Background Detail Tiles | Decorative: windows, cracks, vines, signs | Rich environments |
| 71 | Attribute Table Mastery | 4 palette zones per 32x32 area, precise packing | Correct colouring |
| 72 | Palette Design per Theme | 4 background + 4 sprite palettes per level | Cohesive colour |
| 73 | Tile Animation (Water, Lava) | Alternate tile indices in nametable per frame | Living world |
| 74 | Parallax Sky | Sprite 0 split: different scroll rate for sky rows | Depth |
| 75 | Player Trail Effect | Brief afterimage sprites during fast movement | Speed visual |
| 76 | Death Animation | Multi-frame sprite sequence | Dramatic |
| 77 | Item Collect Animation | Sprite expansion then vanish | Satisfying |
| 78 | Screen Shake | Temporary scroll offset on damage | Impact feedback |
| 79 | Title Screen Art | Full nametable character art: "DASH" | Presentation |
| 80 | Integration + Visual Audit | Tile consistency, attribute alignment, palette harmony | Looks professional |

---

## Key Teaching Moments

### CHR Tile Format (Unit 65)

NES tiles use 2 bitplanes stored sequentially. Each 8x8 tile is 16 bytes: 8 bytes for bitplane 0 (low bits), then 8 bytes for bitplane 1 (high bits). For each pixel, the two planes combine to give a 2-bit value (0-3) that indexes into a 4-colour palette:

```
Bitplane 0, row 0: %01000010    ; Low bits
Bitplane 1, row 0: %01100110    ; High bits
Combined:          0 3 1 0 0 1 3 0  ; 2-bit colour per pixel
```

Colour 0 is transparent for sprites, background for tiles. Three visible colours per tile. The constraint forces strong silhouettes and clear readability.

### Metasprites (Unit 68)

A 16x16 character needs 4 hardware sprites (8x8 each). A metasprite table defines the offsets:

```asm
; Metasprite: 4 sprites composited into 16x16
; Each entry: Y-offset, tile, attributes, X-offset
player_meta:
    .byte $00, $10, $00, $00    ; top-left
    .byte $00, $11, $00, $08    ; top-right
    .byte $08, $12, $00, $00    ; bottom-left
    .byte $08, $13, $00, $08    ; bottom-right
```

The metasprite routine adds the base position to each offset and writes to the OAM buffer. Flipping the entire metasprite (facing left) means flipping each sprite AND swapping left/right positions. One routine, any entity size.

### Parallax via Sprite 0 (Unit 74)

Extend the Sprite 0 technique from Phase 4. After the status bar, write a slow scroll value for the sky rows. When the beam reaches the terrain area (detect via a scanline counter or second Sprite 0), write the full camera scroll. Sky moves at half speed, terrain at full speed. Two scroll writes per frame, genuine parallax.

---

## 6502 Concepts Introduced

1. CHR data interpretation -- 2-bitplane pixel layout (Unit 65)
2. Metasprite table format -- offset/tile/attribute per sub-sprite (Unit 68)
3. Table-driven rendering -- generic metasprite routine (Unit 69)
4. Attribute byte packing -- shift/OR for 4 quadrants per byte (Unit 71)
5. Palette design -- NES master palette constraints, harmony principles (Unit 72)
6. Nametable tile swapping -- periodic updates for animation (Unit 73)
7. Multi-split scrolling -- Sprite 0 for parallax zones (Unit 74)

---

## Hardware

### New in Phase 5

| Resource | Purpose | Introduced |
|----------|---------|------------|
| CHR pattern data format | 2-bitplane, 16 bytes per 8x8 tile | Unit 65 |
| Multiple Sprite 0 splits | Parallax scrolling zones | Unit 74 |

---

## Game State at Phase End

After Unit 80:

- **Custom CHR art** -- themed tilesets for outdoor and underground
- **Player metasprite** -- 16x16 character, 4 hardware sprites composited
- **Metasprite system** -- reusable for enemies and items
- **Background detail** -- decorative tiles for rich environments
- **Themed palettes** -- different colour schemes per level
- **Tile animation** -- water and lava cycle between frames
- **Parallax sky** -- background scrolls at half speed
- **Death animation** -- multi-frame sequence
- **Title screen art** -- character-based "DASH" logo
- **Screen shake** -- impact feedback on damage

The game looks commercially polished. Every pixel has purpose.

---

## What Carries to Phase 6

- **Metasprite system** -- enemies use the same rendering routine
- **Themed palettes** -- different moods for different levels
- **VBlank budget** -- must accommodate music engine updates alongside visual work
- **Title screen** -- ready for music

---

**Version:** 1.0
**Last Updated:** 2026-02-06
