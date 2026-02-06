# Phase 1: Landfall

**Game:** Exodus (Amiga Game 1)
**Units:** 1-16
**Theme:** Creatures walking across bitmap terrain -- display setup, Copper list, basic AI
**68000 Focus:** MOVE.B/W/L, D0-D7/A0-A7 registers, addressing modes, BEQ/BNE, BSR/RTS, Copper list format
**Hardware:** Copper ($DFF080), bitplanes ($DFF0E0+), hardware sprites, Paula ($DFF0A0+), DMACON ($DFF096)
**Status:** Planned

---

## Overview

Phase 1 gets creatures on screen, walking across terrain. The Amiga requires setup that no other platform demands: a Copper list to define the display, bitplane pointers for the graphics, DMA enables for every subsystem. But once that framework is built, the hardware does extraordinary things.

The Copper list is introduced in Unit 1 -- a program that runs on the display coprocessor, executing WAIT and MOVE instructions synchronised to the electron beam. It sets bitplane pointers, changes colours, and controls the entire display. Every Amiga program needs a Copper list; every Amiga effect depends on one.

Creatures are hardware sprites -- 16 pixels wide, 3 colours plus transparent, DMA-driven. They walk right, turn at edges, fall when there's no terrain below. The terrain is a bitmap stored in bitplane memory. By Unit 16, multiple creatures walk, fall, and arrive at an exit zone. The foundation is complete.

---

## Prerequisites

None -- this is the first phase of the first Amiga game.

---

## Unit Progression

| Unit | Title | New 68000 Concept | Game Addition |
|------|-------|-------------------|---------------|
| 1 | Bootable ADF + Copper List | `MOVE.L`, custom register writes, Copper WAIT/MOVE | Coloured display |
| 2 | Bitplane Display | Bitplane pointers in Copper, `BPLCON0` setup | Bitmap visible |
| 3 | Draw Terrain | Direct memory writes to bitplane data | Land on screen |
| 4 | Creature Sprite | Hardware sprite data, sprite pointers in Copper | **Creature visible** |
| 5 | Creature Walks Right | `ADD.W` position increment per frame | Movement |
| 6 | Creature Turns at Edge | `CMP.W` boundary, direction toggle | Back and forth |
| 7 | Terrain Collision (Floor) | Read pixel below feet from bitplane | **Respects terrain** |
| 8 | Creature Falls | Gravity when no pixel below, `SUB.W`/`ADD.W` | Falls into gaps |
| 9 | Footstep Sound | Paula: sample pointer, length, period, volume | Audio feedback |
| 10 | Multiple Creatures | Data table, `BSR`/`RTS` subroutines, loop | Several walking |
| 11 | Exit Zone | Target area, detect creature arrival | **Goal defined** |
| 12 | Creature Count Display | Copper screen split, text in lower panel | Saved / Total |
| 13 | Score: Creatures Saved | Increment on arrival, display update | Progress |
| 14 | Level Complete | All creatures arrived or lost, result screen | End condition |
| 15 | Title Screen | Copper gradient background, text rendering | Feels real |
| 16 | Integration + Polish | Creature spacing, fall speed, terrain shape | Solid foundation |

---

## Key Teaching Moments

### The Copper List (Unit 1)

The Copper is a coprocessor that executes a program synchronised to the display beam. It has two instructions: WAIT (pause until the beam reaches a specific position) and MOVE (write a value to a custom register). A Copper list is a sequence of these instructions in Chip RAM:

```asm
copper_list:
    dc.w $0100,$1200    ; BPLCON0: 1 bitplane, colour on
    dc.w $00E0,$0000    ; BPL1PTH: bitplane 1 pointer high
    dc.w $00E2,$0000    ; BPL1PTL: bitplane 1 pointer low
    dc.w $0180,$0000    ; COLOR00: black background
    dc.w $0182,$0FFF    ; COLOR01: white foreground

    dc.w $FFFF,$FFFE    ; End: wait for impossible position
```

Point the Copper to this list (`COP1LC` = $DFF080), trigger a restart (`COPJMP1` = $DFF088), and the display appears. Every frame, the Copper re-executes from the start. Changing the list changes the display -- no CPU drawing needed.

### Bitplane Pixel Addressing (Unit 3)

Amiga graphics use planar format. Each bitplane is a separate bitmap where each bit represents one pixel. For a 320x256 display, one bitplane is 320/8 x 256 = 10,240 bytes. To set a pixel at (x, y): calculate byte offset = y x 40 + x/8, then set bit 7-(x AND 7) in that byte. With `MULU` available on the 68000, the offset calculation is straightforward:

```asm
; Set pixel at D0=x, D1=y in bitplane at A0
    mulu #40,d1         ; y * bytes_per_row
    move.w d0,d2
    lsr.w #3,d2         ; x / 8 = byte offset
    add.w d2,d1         ; total byte offset
    move.w d0,d2
    not.w d2
    and.w #7,d2         ; bit number = 7 - (x AND 7)
    bset d2,0(a0,d1.w)  ; Set the bit
```

### Terrain Collision (Unit 7)

A creature checks the pixel below its feet in the bitplane. If the pixel is set (1), there's ground -- walk normally. If clear (0), there's a gap -- fall. One bit test per frame per creature. The bitmap IS the collision map. No separate collision data, no tile lookup. This is why a terrain puzzle works so naturally on the Amiga -- the graphics and the game data are the same thing.

---

## 68000 Concepts Introduced

1. `MOVE.B`/`MOVE.W`/`MOVE.L` -- data transfer with size control (Unit 1)
2. Custom register addresses ($DFF000+) -- hardware control via memory-mapped I/O (Unit 1)
3. Copper list format -- WAIT/MOVE instruction pairs (Unit 1)
4. `BPLCON0` -- bitplane count and display mode (Unit 2)
5. Bitplane pointer registers -- `BPL1PTH`/`BPL1PTL` in Copper (Unit 2)
6. Pixel addressing -- `MULU` for row offset, `BSET`/`BTST` for bit (Unit 3)
7. Hardware sprite format -- control words + pixel data (Unit 4)
8. `ADD.W`/`SUB.W` -- movement increment/decrement (Unit 5)
9. `CMP.W` / `BEQ`/`BNE`/`BGT`/`BLT` -- comparison and conditional branches (Unit 6)
10. `BTST` -- test individual bits for pixel collision (Unit 7)
11. `BSR`/`RTS` -- subroutine call and return (Unit 10)
12. Paula sample playback -- `AUDxLC`, `AUDxLEN`, `AUDxPER`, `AUDxVOL` (Unit 9)
13. `DMACON` -- enable/disable DMA channels for Copper, bitplanes, sprites, audio (Unit 1)

---

## Hardware

### Custom Registers Used in Phase 1

| Register | Address | Purpose | Introduced |
|----------|---------|---------|------------|
| DMACON | $DFF096 | DMA enable: Copper, bitplanes, sprites, audio | Unit 1 |
| COP1LC | $DFF080 | Copper list 1 pointer (long) | Unit 1 |
| COPJMP1 | $DFF088 | Restart Copper from COP1LC | Unit 1 |
| BPLCON0 | $DFF100 | Bitplane count, display mode | Unit 2 |
| BPL1PTH/L | $DFF0E0/$E2 | Bitplane 1 pointer (high/low word) | Unit 2 |
| COLOR00-01 | $DFF180-$182 | Palette colours 0-1 | Unit 1 |
| SPR0PTH/L | $DFF120/$122 | Sprite 0 pointer | Unit 4 |
| AUD0LC | $DFF0A0 | Audio channel 0 sample pointer | Unit 9 |
| AUD0LEN | $DFF0A4 | Audio channel 0 sample length | Unit 9 |
| AUD0PER | $DFF0A6 | Audio channel 0 period (pitch) | Unit 9 |
| AUD0VOL | $DFF0A8 | Audio channel 0 volume | Unit 9 |

---

## Game State at Phase End

After Unit 16:

- **Copper list** -- defines display: bitplane pointers, colours, screen split
- **Bitplane display** -- 1-bitplane terrain bitmap (2 colours)
- **Terrain** -- drawn directly in bitplane memory
- **Creatures** -- hardware sprites walking across terrain
- **Gravity** -- creatures fall when no pixel below their feet
- **Direction** -- creatures turn at edges and walls
- **Multiple creatures** -- data table, subroutine loop
- **Exit zone** -- creatures arrive and are counted
- **Score display** -- Copper screen split for lower panel
- **Sound** -- Paula footstep sample
- **Title screen** -- Copper gradient background
- **Complete loop** -- title -> play -> result -> title

Creatures walk, fall, and arrive. The display framework is solid. Bootable from disk.

---

## What Carries to Phase 2

- **Copper list** -- extended with more colours, screen splits, gradient effects
- **Bitplane system** -- Phase 2 adds the Blitter for hardware-accelerated modification
- **Terrain collision** -- the pixel test pattern is reused by ability checks
- **Creature data table** -- extended with ability state, animation, and type fields
- **Paula playback** -- extended with more samples and eventually MOD music

---

**Version:** 1.0
**Last Updated:** 2026-02-06
