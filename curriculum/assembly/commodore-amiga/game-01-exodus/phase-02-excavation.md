# Phase 2: Excavation

**Game:** Exodus (Amiga Game 1)
**Units:** 17-32
**Theme:** Blitter terrain modification -- the core game mechanic
**68000 Focus:** Blitter registers, minterms, bitwise operations (AND/OR/EOR), MULU for offset calculation
**Hardware:** Blitter ($DFF040-$DFF074), DMABUSY ($DFF002 bit 14)
**Status:** Planned

---

## Overview

Phase 2 introduces the Blitter -- the hardware rectangle copier that defines Amiga graphics programming. But in Exodus, the Blitter isn't just a graphics tool; it's the game design tool. Digging a tunnel is a Blitter clear. Building a bridge is a Blitter fill. Drawing a redirect wall is a Blitter line. Every game action is a Blitter operation.

The key concept is the minterm: a 4-input logic function that determines how source and destination pixels combine. Clear = write zeros. Fill = write ones. Copy = transfer source to destination. Cookie-cut = paste with masking. Understanding minterms is understanding the Blitter.

By the end of Phase 2, creatures respond to terrain that the player modifies in real time. The Blitter IS the gameplay.

---

## Prerequisites from Phase 1

- Copper list with bitplane display
- Terrain bitmap in bitplane memory
- Creature walking and falling with pixel collision
- Multiple creatures with data table
- Paula sample playback

---

## Unit Progression

| Unit | Title | New 68000 Concept | Game Addition |
|------|-------|-------------------|---------------|
| 17 | Blitter Basics: Rectangle Clear | `BLTCON0`, `BLTDPT`, `BLTSIZE`, DMA trigger | Erase a rectangle |
| 18 | Dig Ability | Assign digger, creature clears terrain below | **Terrain modification** |
| 19 | Blitter Copy: Rectangle Fill | Source + destination channels, copy minterm | Fill a rectangle |
| 20 | Build Ability | Creature places terrain ahead | Bridge over gap |
| 21 | Blitter Line Draw | Line mode for angled surfaces | Ramps |
| 22 | Redirect Ability | Place wall that reverses creature direction | Traffic control |
| 23 | Dig Sound | Paula channel 2, digging sample | Satisfying feedback |
| 24 | Build Sound | Paula channel 3, building sample | Construction feel |
| 25 | Blitter Wait (DMABUSY) | Poll `$DFF002` bit 14 before next op | No corruption |
| 26 | Cookie-Cut Masking | A/B/C/D channels, minterm for masked copy | Clean rendering |
| 27 | Creature as BOB | Blitter cookie-cut onto terrain bitplane | Smooth on terrain |
| 28 | BOB Restore | Save background, restore before redraw | No trails |
| 29 | Multiple Abilities Active | Different creatures doing different tasks | Complex behaviour |
| 30 | Ability Limit per Level | Counter per type, display remaining | Strategy |
| 31 | Undo: Stop Ability | Cancel task, creature resumes walking | Correction |
| 32 | Integration + Blitter Tuning | Operation timing, visual polish, balance | Core mechanic solid |

---

## Key Teaching Moments

### The Blitter (Unit 17)

The Blitter copies rectangular blocks of memory using DMA -- no CPU cycles. It has four channels (A, B, C, D) and a logic function (minterm) that combines them. For terrain clearing:

```asm
; Clear a rectangle: write zeros to destination
; Wait for Blitter idle
.wait:
    btst #14,$DFF002
    bne.s .wait

    clr.w $DFF066       ; BLTDMOD = 0 modulo (for full-width blit)
    move.w #$0100,$DFF040 ; BLTCON0: use D channel only, minterm $00 (zero)
    clr.w $DFF042       ; BLTCON1: no special modes
    move.l a0,$DFF054   ; BLTDPTH: destination address
    move.w d0,$DFF058   ; BLTSIZE: (height << 6) | width_words — triggers blit
```

Set the destination, set the minterm to "output zero", set the size. The Blitter clears the rectangle while the CPU continues with game logic.

### Minterms (Unit 19)

The Blitter combines up to 3 source channels (A, B, C) into destination D using a minterm -- an 8-bit value that encodes a Boolean function. Each bit corresponds to one combination of A, B, C inputs:

| Bit | A | B | C | Meaning |
|-----|---|---|---|---------|
| 7 | 1 | 1 | 1 | All sources set |
| 6 | 1 | 1 | 0 | A and B set, C clear |
| ... | | | | |
| 0 | 0 | 0 | 0 | All sources clear |

Common minterms:
- `$F0` = copy A to D (ignore B and C)
- `$00` = clear D (all zeros)
- `$FF` = fill D (all ones)
- `$CA` = cookie-cut: `(A AND B) OR (NOT A AND C)` -- paste B through mask A over background C

### Cookie-Cut Masking (Unit 26)

Cookie-cut pastes a sprite image onto a background cleanly. The four channels:
- **A** = mask (the silhouette shape)
- **B** = source image (the creature graphic)
- **C** = background (existing screen pixels)
- **D** = destination (the screen)

Minterm `$CA` means: where the mask is 1, use the source image; where the mask is 0, keep the background. One Blitter operation, perfect compositing. This is how every Amiga game renders BOBs (Blitter Objects).

---

## 68000 Concepts Introduced

1. Blitter register setup -- `BLTCON0`, `BLTCON1`, channel pointers, modulos (Unit 17)
2. Minterm concept -- 8-bit Boolean function for channel combination (Unit 17)
3. DMA busy polling -- `BTST #14,$DFF002` before new operation (Unit 25)
4. `MULU` for address calculation -- row offset = y * bytes_per_row (Unit 17)
5. Blitter line mode -- `BLTCON1` octant bits for line direction (Unit 21)
6. Multi-channel Blitter -- A/B/C/D with cookie-cut minterm (Unit 26)
7. Background save/restore -- copy before draw, restore before next frame (Unit 28)
8. `AND.W`/`OR.W`/`EOR.W` -- bitwise operations for minterm understanding (Unit 19)

---

## Hardware

### Blitter Registers

| Register | Address | Purpose | Introduced |
|----------|---------|---------|------------|
| BLTCON0 | $DFF040 | Control: ASH shift, channel enables, minterm | Unit 17 |
| BLTCON1 | $DFF042 | Control: BSH shift, line mode, fill mode | Unit 21 |
| BLTAMOD | $DFF064 | Channel A modulo | Unit 26 |
| BLTBMOD | $DFF062 | Channel B modulo | Unit 26 |
| BLTCMOD | $DFF060 | Channel C modulo | Unit 26 |
| BLTDMOD | $DFF066 | Channel D modulo | Unit 17 |
| BLTAPTH | $DFF050 | Channel A pointer (mask) | Unit 26 |
| BLTBPTH | $DFF04C | Channel B pointer (source) | Unit 26 |
| BLTCPTH | $DFF048 | Channel C pointer (background) | Unit 26 |
| BLTDPTH | $DFF054 | Channel D pointer (destination) | Unit 17 |
| BLTSIZE | $DFF058 | Size: triggers blit (height << 6 | width) | Unit 17 |
| DMACONR | $DFF002 | DMA status: bit 14 = Blitter busy | Unit 25 |

---

## Game State at Phase End

After Unit 32:

- **Dig ability** -- creature clears terrain below, creating tunnel
- **Build ability** -- creature places terrain ahead, creating bridge
- **Redirect ability** -- creature places wall that reverses direction
- **Cookie-cut BOBs** -- creatures rendered cleanly on terrain
- **Background save/restore** -- no visual trails
- **Ability limits** -- finite uses per level for strategic planning
- **Undo** -- cancel an ability in progress
- **Multiple abilities** -- different creatures doing different things simultaneously
- **Sound effects** -- dig, build, redirect samples via Paula

The core puzzle mechanic works. The Blitter modifies terrain in real time and creatures respond.

---

## What Carries to Phase 3

- **Blitter operations** -- used for UI panel rendering, explosion effects, more abilities
- **Cookie-cut pattern** -- all game entities use this rendering approach
- **Minterm understanding** -- extended for more complex compositing
- **DMA busy discipline** -- always wait before starting new operations

---

**Version:** 1.0
**Last Updated:** 2026-02-06
