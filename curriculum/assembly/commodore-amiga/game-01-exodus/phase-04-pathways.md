# Phase 4: Pathways

**Game:** Exodus (Amiga Game 1)
**Units:** 49-64
**Theme:** Level data, terrain types, and smarter creature AI
**68000 Focus:** Address register indirect with displacement, LEA for address calculation, word alignment, data structures
**Hardware:** trackdisk.device for disk I/O, multi-bitplane terrain encoding
**Status:** Planned

---

## Overview

Phase 4 gives the game content. Levels are bitmap data loaded from the ADF disk -- each level a pre-drawn terrain with entrances, exits, and varying terrain types. Different terrain materials respond differently to abilities: dirt can be dug, rock resists, steel is indestructible, and water kills on contact.

Multi-bitplane terrain encodes material type through colour. The same pixels that display the terrain also encode its properties -- no separate collision map. This is the Amiga way: the display IS the data.

Smarter creature AI handles wall turns, overhangs, crowd behaviour, and multiple spawn points. Password progression and a level select screen give the game structure. By Phase 4's end, there are 8+ levels with a difficulty curve.

---

## Prerequisites from Phase 3

- Blitter terrain modification (all abilities)
- Copper screen split with UI panel
- Mouse-driven creature selection and ability assignment
- Timer and creature counting

---

## Unit Progression

| Unit | Title | New 68000 Concept | Game Addition |
|------|-------|-------------------|---------------|
| 49 | Level Data Format | Compressed bitmap in structured data block | Structured levels |
| 50 | Level Loading from Disk | `trackdisk.device` sector reads, decompression | Levels from ADF |
| 51 | Multiple Levels | Level pointer table, load next on completion | Progression |
| 52 | Level Select Screen | Menu with names, mouse cursor selection | Choose level |
| 53 | Terrain Type: Rock | Different colour, cannot be dug | Routing constraint |
| 54 | Terrain Type: Steel | Indestructible, blocks all abilities | Hard boundary |
| 55 | Terrain Type: Water | Kills creatures on contact | Lethal hazard |
| 56 | Multi-Bitplane Terrain | 2+ bitplanes encode type via colour | Type from colour |
| 57 | Smarter Wall Turn | Handle overhangs, step-up detection | Robust walking |
| 58 | Crowd Behaviour | Creatures queue behind pausers, interact | Group dynamics |
| 59 | Trap Door Entrance | Creatures spawn from specific point | Level design tool |
| 60 | Multiple Entrances | Several spawn points, distributed | Complex flow |
| 61 | Multiple Exits | Different targets, all must be reached | Routing puzzle |
| 62 | Save Threshold | "Save 80%" to pass | Difficulty per level |
| 63 | Password System | Level progress as encoded string | Persistence |
| 64 | Integration + Level Design | 8+ levels, varied terrain, difficulty curve | Real content |

---

## Key Teaching Moments

### Multi-Bitplane Terrain (Unit 56)

Two bitplanes give 4 colours, each representing a terrain type:

| Colour | Bitplane 1 | Bitplane 0 | Terrain | Ability Response |
|--------|-----------|-----------|---------|-----------------|
| 0 (black) | 0 | 0 | Empty (air) | N/A |
| 1 (brown) | 0 | 1 | Dirt | Diggable |
| 2 (grey) | 1 | 0 | Rock | Resists digging |
| 3 (blue) | 1 | 1 | Steel/Water | Indestructible/lethal |

The dig ability checks: read both bitplanes at the target position. If colour = 1 (dirt), proceed with Blitter clear. If colour = 2 or 3, refuse. The display doubles as the data structure -- one read, two purposes.

### Disk Loading (Unit 50)

Level data lives on the ADF disk. The Amiga's `trackdisk.device` provides low-level sector access:

```asm
; Read sectors from disk using trackdisk.device
    move.l #io_request,a1
    move.w #CMD_READ,IO_COMMAND(a1)
    move.l #buffer,IO_DATA(a1)
    move.l #level_size,IO_LENGTH(a1)
    move.l level_offset,IO_OFFSET(a1)
    jsr _LVODoIO(a6)
```

Each level is a compressed bitmap. Load, decompress (RLE), and write to bitplane memory. Level design happens in a paint program; the game engine just renders it.

### LEA for Address Calculation (Unit 49)

`LEA` (Load Effective Address) calculates an address without accessing memory. Unlike `MOVE.L`, it doesn't read from the address -- it computes it. This is the 68000's most versatile addressing tool:

```asm
; Calculate address of level N's data
    lea level_table,a0  ; Base of level pointer table
    move.w level_num,d0
    lsl.w #2,d0         ; x4 (each pointer is 4 bytes)
    move.l 0(a0,d0.w),a1 ; Load level data pointer
```

---

## 68000 Concepts Introduced

1. `LEA` -- load effective address without memory access (Unit 49)
2. Address register indirect with displacement -- `0(a0,d0.w)` (Unit 49)
3. `trackdisk.device` -- Amiga low-level disk I/O (Unit 50)
4. RLE decompression -- expand run-length encoded data (Unit 49)
5. Multi-bitplane pixel reading -- test bits in multiple planes for terrain type (Unit 56)
6. Word alignment awareness -- 68000 requires even addresses for word/long operations (Unit 50)
7. Creature state extensions -- step-up, queue, spawn point tracking (Units 57-60)
8. XOR-based encoding -- password generation/validation (Unit 63)

---

## Hardware

### New in Phase 4

| Resource | Purpose | Introduced |
|----------|---------|------------|
| trackdisk.device | Low-level ADF disk sector access | Unit 50 |
| Multiple bitplane pointers | 2+ bitplanes for terrain type encoding | Unit 56 |

---

## Game State at Phase End

After Unit 64:

- **8+ levels** -- loaded from disk, varied terrain layouts
- **Terrain types** -- dirt (diggable), rock (resistant), steel (indestructible), water (lethal)
- **Multi-bitplane display** -- terrain type encoded in colour
- **Level select** -- menu with mouse navigation
- **Password system** -- encoded level progress
- **Multiple entrances** -- creatures spawn from different points
- **Multiple exits** -- all must be reached
- **Save threshold** -- minimum percentage to pass
- **Smarter AI** -- wall turns, overhangs, crowd queueing
- **Difficulty curve** -- levels progress from tutorial to challenging

A real puzzle game with content and structure.

---

## What Carries to Phase 5

- **Multi-bitplane system** -- extended with Copper colour changes per terrain zone
- **Level data format** -- richer metadata for themes, palettes, music
- **Disk loading** -- art assets, music data loaded alongside levels
- **Creature AI** -- extended with animation frames and visual variety

---

**Version:** 1.0
**Last Updated:** 2026-02-06
