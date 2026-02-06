# Phase 1: Threshold

**Game:** Shadowkeep (ZX Spectrum Game 1)
**Units:** 1–16
**Theme:** First room — movement, walls, and the attribute system as game design
**Z80 Focus:** LD, INC/DEC, JP/JR, CP, CALL/RET, IN/OUT, DJNZ, AND/OR
**Hardware:** Screen memory ($4000+), attribute memory ($5800+), keyboard port ($FE), beeper
**Status:** Planned

---

## Overview

Phase 1 teaches the ZX Spectrum through its most distinctive feature: the attribute system. Every 8×8 character cell on screen has an attribute byte controlling INK colour, PAPER colour, BRIGHT, and FLASH. In Shadowkeep, this isn't just a display feature — it's the game design tool. Walls are INK, floors are PAPER, items are BRIGHT, hazards are FLASH. Collision detection is a single attribute read.

The learner draws a room by setting attributes, moves a character on the 8-pixel grid, and checks what colour they're about to walk into. By Unit 7, wall collision works without any distance calculations — just read the attribute, check the INK colour. This is fundamentally different from the C64 approach (hardware sprite collision) and teaches the Spectrum way of thinking.

By Unit 16, the learner has a single room with walls, collectible treasures, a hazard zone, an exit door, lives, score, and sound. A complete game loop in one room.

---

## Unit Progression

| Unit | Title | New Z80 Concept | Game Addition |
|------|-------|----------------|---------------|
| 1 | Block on Screen | `LD A,n` / `LD (addr),A`, memory addresses | Coloured block at $5800 |
| 2 | Attribute Anatomy | Bit fields: `AND`/`OR` for INK, PAPER, BRIGHT, FLASH | Understand the attribute byte |
| 3 | Drawing a Room | `DJNZ` loop, attribute memory as a grid | Walls and floor from data |
| 4 | Keyboard Input | `IN A,($FE)`, row selection, key detection | Read key presses |
| 5 | Player Character | Print character to screen RAM ($4000+), position tracking | Character on screen |
| 6 | Character-Cell Movement | `INC`/`DEC` for position, `CP`/`JR` for boundary check | Move on 8-pixel grid |
| 7 | Wall Collision | Read attribute at target cell, check INK colour | **Walls block movement** |
| 8 | Room from Data | Room layout as byte table, draw from data with loop | Data-driven room |
| 9 | Treasure Item | BRIGHT bit marks collectibles, `BIT`/`RES` instructions | Shining items on floor |
| 10 | Collect Treasure | Read attribute, check BRIGHT, clear it, update score | **Items work** |
| 11 | Score Display | `CALL` ROM print routine ($0D6B), number conversion | Score on status line |
| 12 | Beeper Sound | `OUT ($FE),A`, bit 4 toggle, timing loop | Collect sound |
| 13 | Exit Door | Specific attribute combination marks the exit | Goal visible |
| 14 | Room Complete | All treasures collected → door opens, exit detection | **Win condition** |
| 15 | Hazards and Lives | FLASH attribute = danger, 3 lives, death on touch | Stakes |
| 16 | Integration | Edge cases, status bar, restart logic | Complete single room |

---

## Key Teaching Moments

### The Attribute System (Unit 2)

The attribute byte is the Spectrum's defining feature — and its most famous limitation. One byte per 8×8 cell:

```
Bit 7: FLASH (INK/PAPER swap at 1.56Hz)
Bit 6: BRIGHT (intensity boost)
Bits 5-3: PAPER (background colour, 0-7)
Bits 2-0: INK (foreground colour, 0-7)
```

In Shadowkeep, this byte IS the game world. INK colour 1 (blue) means wall. INK colour 0 (black on black) means floor. BRIGHT means item. FLASH means hazard. One byte encodes collision type, item presence, and danger — no separate collision map needed.

### Collision via Attribute Reading (Unit 7)

Before moving the player, read the attribute at the destination cell. Calculate the attribute address: `$5800 + (row × 32) + column`. Load the byte, mask with `AND $07` to isolate INK bits. If INK equals the wall colour, movement is blocked. This is faster, simpler, and more elegant than distance-based collision. It's the reason most Spectrum games use character-cell movement.

### DJNZ — The Loop Instruction (Unit 3)

The Z80's `DJNZ` (Decrement B and Jump if Not Zero) is a single instruction that does what the 6502 needs three for (`DEX` / `CPX #0` / `BNE`). Load B with the count, put the loop body between the label and `DJNZ`, done. It's the Z80's first taste of "this processor has instructions specifically for common patterns."

### BIT/SET/RES — Single-Bit Operations (Unit 9)

The Z80 can test, set, or clear individual bits without masking. `BIT 6,(HL)` tests the BRIGHT bit. `RES 6,(HL)` clears it (item collected). `SET 7,(HL)` would set FLASH. These are cleaner than the 6502's `AND`/`ORA`/`EOR` approach — each operation is a single, readable instruction.

### Beeper Audio (Unit 12)

The Spectrum's "sound chip" is a single bit on I/O port $FE (bit 4). Toggle it fast → high pitch. Toggle it slow → low pitch. Sound generation is entirely in software: a tight loop that toggles the bit at the right frequency. This means sound blocks the CPU — no background music during gameplay on a 48K Spectrum. The simplicity is both a constraint and a teaching opportunity.

---

## Z80 Concepts Introduced

1. `LD A,n` / `LD (addr),A` — load and store (Unit 1)
2. `AND` / `OR` — bit masking for attribute fields (Unit 2)
3. `LD B,n` / `DJNZ` — counted loop (Unit 3)
4. `IN A,($FE)` — port input for keyboard (Unit 4)
5. `LD (HL),A` — indirect store via HL register pair (Unit 5)
6. `INC` / `DEC` — increment/decrement (Unit 6)
7. `CP` / `JR Z` / `JR NZ` / `JR C` — compare and conditional relative jump (Unit 6)
8. `JP` — unconditional absolute jump (Unit 6, game loop)
9. `BIT` / `SET` / `RES` — single-bit test/set/clear (Unit 9)
10. `CALL` / `RET` — subroutine call and return (Unit 11)
11. `OUT ($FE),A` — port output for beeper and border (Unit 12)

---

## Hardware

### Memory Regions

| Address | Purpose | Introduced |
|---------|---------|-----------|
| `$4000`–`$57FF` | Screen bitmap (6144 bytes, non-linear) | Unit 5 |
| `$5800`–`$5AFF` | Attribute memory (768 bytes, 32×24 grid) | Unit 1 |

### I/O Ports

| Port | Direction | Purpose | Introduced |
|------|-----------|---------|-----------|
| `$FE` | Read | Keyboard (row selected by high byte) | Unit 4 |
| `$FE` | Write | Border colour (bits 0–2) + beeper (bit 4) | Unit 12 |

### System Variables

| Address | Name | Purpose | Introduced |
|---------|------|---------|-----------|
| `$5C08` | LAST_K | Last key pressed | Unit 4 |
| `$5C6A` | FRAMES | Frame counter (50Hz) | Unit 15 |

### ROM Routines

| Address | Name | Purpose | Introduced |
|---------|------|---------|-----------|
| `$0D6B` | PRINT_A | Print character in A register | Unit 5 |

---

## Game State at Phase End

After Unit 16:

- **Single room** — walls, floor, hazard zone, exit door, drawn from data
- **Player** — character-cell movement (8-pixel grid), keyboard controlled
- **Collision** — attribute-based: walls block, items collect, hazards kill
- **Treasures** — BRIGHT items scattered in room, collect all to open exit
- **Score** — displayed on status line, increments per treasure
- **Lives** — three, lost on hazard contact, displayed on screen
- **Sound** — beeper effects for collect, death, room complete
- **Exit** — door opens when all treasures collected, step on it to win

The game is simple but demonstrates the Spectrum's attribute system as a complete game design tool.

---

## What Carries to Phase 2

- **Attribute-as-game-world pattern** — extended with key colours, door types, new item types
- **Room data format** — expanded to support multiple rooms with metadata
- **Character-cell movement** — same grid system, new things to interact with
- **CALL/RET** — subroutines expand into room loading, inventory management
- **Score/lives system** — carried forward unchanged

---

**Version:** 1.0
**Last Updated:** 2026-02-06
