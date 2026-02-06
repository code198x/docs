# Phase 5: Copper Sky

**Game:** Exodus (Amiga Game 1)
**Units:** 65-80
**Theme:** Visual polish -- Copper gradients, bitplane art, animation, themes
**68000 Focus:** Copper instruction timing, bitplane pointer arithmetic, DMA scheduling
**Hardware:** Copper colour changes, multiple bitplane pointers, sprite animation
**Status:** Planned

---

## Overview

Phase 5 transforms the game's look. The signature effect is the Copper gradient sky: a smooth colour transition from light blue at the top to dark blue at the horizon, rendered by writing a new colour value on every raster line. Zero CPU cost -- the Copper does it all. This is the effect that makes people say "it looks like an Amiga."

Parallax scrolling adds depth: a cloud layer scrolls at a different rate from the terrain. Creature animations bring the sprites to life. Themed palettes give each level visual identity: grass, snow, cave, desert. Tile detail, water animation, and polished transitions complete the transformation. By Phase 5's end, screenshots sell the game.

---

## Prerequisites from Phase 4

- Multi-bitplane terrain with type encoding
- Level loading from disk
- Copper screen split for UI panel
- Cookie-cut BOB rendering for creatures

---

## Unit Progression

| Unit | Title | New 68000 Concept | Game Addition |
|------|-------|-------------------|---------------|
| 65 | Copper Gradient Sky | WAIT/MOVE per line, colour gradient in list | **Atmospheric sky** |
| 66 | Dynamic Gradient | Modify Copper list colours per frame | Time of day |
| 67 | Parallax Cloud Layer | Separate bitplane, different scroll rate | Depth |
| 68 | Terrain Texture Detail | Dithering, surface patterns in bitplane | Rich terrain |
| 69 | Creature Animation Frames | Multiple sprite images, cycle per step | Walking animation |
| 70 | Ability Animation | Dig sparks, build placement, explosion effect | Visual feedback |
| 71 | Water Animation | Copper colour cycling for flowing water | Living hazard |
| 72 | Entrance Animation | Trap door opens, creatures emerge | Polished spawn |
| 73 | Exit Celebration | Creatures dance on arrival | Satisfying arrival |
| 74 | Palette Design per Theme | Different colour sets: grass, snow, cave, desert | Visual variety |
| 75 | Background Detail | Mountains, trees, decorative elements | Rich environment |
| 76 | Screen Transitions | Copper fade to black between levels | Smooth flow |
| 77 | Death Animation | Creature "pops" -- expanding circle clear | Clear feedback |
| 78 | Title Screen Art | Multi-bitplane illustration, colour cycling | Presentation |
| 79 | Level Preview | Brief terrain display before timer starts | Orientation |
| 80 | Integration + Visual Audit | Copper timing, palette harmony, consistency | Looks professional |

---

## Key Teaching Moments

### Copper Gradient (Unit 65)

A gradient writes a new `COLOR00` value on every raster line. The Copper WAITs for line N, MOVEs a colour, WAITs for N+1, MOVEs the next:

```asm
; Sky gradient: 64 lines from light to dark blue
sky_gradient:
    dc.w $2C01,$FFFE    ; WAIT line $2C
    dc.w $0180,$08AF    ; COLOR00 = light blue
    dc.w $2D01,$FFFE    ; WAIT line $2D
    dc.w $0180,$079F    ; slightly darker
    dc.w $2E01,$FFFE    ; WAIT line $2E
    dc.w $0180,$068F    ; darker
    ; ... continue for each line
    dc.w $6B01,$FFFE    ; WAIT line $6B
    dc.w $0180,$0014    ; dark blue at horizon
```

64 lines = 128 Copper instructions. The Copper executes in parallel with the display -- no CPU involvement. This is how Amiga games create those distinctive gradient skies that 8-bit machines can't match.

### Parallax (Unit 67)

Parallax uses the Copper to point to different bitplane data for the sky zone. The sky bitplane scrolls at half the camera speed (or a fixed rate for clouds). At the terrain zone, the Copper switches to the terrain bitplane pointers. Two independent scroll rates from one display:

```asm
; Copper: sky zone with slow scroll
    dc.w $00E0,$0000    ; BPL1PTH = sky bitplane (high)
    dc.w $00E2,$0000    ; BPL1PTL = sky bitplane (low)
    ; ... sky colours ...

    dc.w $7001,$FFFE    ; WAIT for terrain zone
    dc.w $00E0,$0000    ; BPL1PTH = terrain bitplane (high)
    dc.w $00E2,$0000    ; BPL1PTL = terrain bitplane (low)
    ; ... terrain colours ...
```

Each frame, update the sky bitplane pointer to shift the clouds. The terrain pointer stays fixed (or follows the camera). The Copper does the split automatically.

### Dynamic Copper Modification (Unit 66)

The Copper list lives in Chip RAM -- regular memory. Modifying the colour values in the list each frame changes the gradient. A time-of-day effect: each frame, shift all gradient colours slightly warmer (sunset) or cooler (dawn). The CPU writes new colour values to the Copper list; next frame, the Copper executes the updated list. Live modification of a live display program.

---

## 68000 Concepts Introduced

1. Copper list generation -- programmatic creation of WAIT/MOVE pairs (Unit 65)
2. Dynamic Copper modification -- writing to Copper list in RAM each frame (Unit 66)
3. Bitplane pointer switching -- different BPLxPT values per screen zone (Unit 67)
4. Colour cycling -- rotating palette entries via Copper or direct register writes (Unit 71)
5. Sprite animation tables -- frame index cycling per creature state (Unit 69)
6. Copper fade -- gradual colour reduction to black across all entries (Unit 76)
7. DMA timing awareness -- Copper, Blitter, and sprite DMA sharing bandwidth (Unit 80)

---

## Hardware

### New in Phase 5

| Resource | Purpose | Introduced |
|----------|---------|------------|
| Per-line Copper colour writes | Gradient effects across screen height | Unit 65 |
| Zone-specific bitplane pointers | Different graphics per screen section | Unit 67 |

---

## Game State at Phase End

After Unit 80:

- **Gradient sky** -- smooth Copper colour transition per raster line
- **Dynamic time of day** -- gradient shifts frame by frame
- **Parallax clouds** -- background scrolls at different rate
- **Terrain texture** -- dithered, detailed bitplane patterns
- **Creature animation** -- walking cycle, ability animations
- **Water animation** -- Copper colour cycling for flow
- **Themed palettes** -- grass, snow, cave, desert
- **Background detail** -- decorative elements add atmosphere
- **Screen transitions** -- Copper fade between levels
- **Title screen art** -- multi-bitplane illustration
- **Level preview** -- brief terrain display before play

The game looks like a commercial Amiga release. Every pixel has atmosphere.

---

## What Carries to Phase 6

- **Copper list structure** -- extended with music visualisation hooks
- **Palette system** -- music data may reference theme-specific palettes
- **Animation framework** -- creature and ability animations continue
- **DMA timing awareness** -- audio DMA adds to the bandwidth budget

---

**Version:** 1.0
**Last Updated:** 2026-02-06
