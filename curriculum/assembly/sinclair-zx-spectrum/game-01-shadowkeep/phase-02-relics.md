# Phase 2: Relics

**Game:** Shadowkeep (ZX Spectrum Game 1)
**Units:** 17–32
**Theme:** Keys, doors, inventory — the core puzzle mechanic
**Z80 Focus:** Indirect addressing (HL), IX register, 16-bit arithmetic, lookup tables
**Hardware:** Expanded attribute usage, multiple room data management
**Status:** Planned

---

## Overview

Phase 1 proved that attributes make a game world. Phase 2 makes that world interactive. Coloured keys unlock matching doors. A potion restores health. An inventory tracks what the player carries. Multiple rooms connected by doorways create a space worth exploring.

The Z80 focus shifts to indirect addressing and structured data. The HL register pair becomes the primary pointer — `LD A,(HL)` reads from the address HL points to, enabling room data access, inventory lookup, and attribute manipulation through a single register pair. The IX register appears for structured data access with displacement: `LD A,(IX+3)` reads the fourth field of a record, giving the Z80 something resembling struct access.

By Unit 32, the player navigates 4+ rooms, collects coloured keys, opens matching doors, manages health, and tracks progress. The keep has depth.

---

## Prerequisites from Phase 1

- Attribute-based collision — extended to check for door and key colours
- Room data format — expanded with metadata (connections, item lists)
- Character-cell movement — unchanged, new interactions layered on top
- CALL/RET — subroutines for room loading, inventory, status display
- BIT/SET/RES — item flags for tracking collected keys

---

## Unit Progression

| Unit | Title | New Z80 Concept | Game Addition |
|------|-------|----------------|---------------|
| 17 | Key Item | Different INK colour marks keys (e.g., red INK = red key) | Keys visible in rooms |
| 18 | Collect Key | Inventory variable set on collection | Player picks up keys |
| 19 | Door Tiles | Specific attribute combination = locked door | Locked passages visible |
| 20 | Key Opens Door | Check inventory before allowing passage | **Puzzle mechanic works** |
| 21 | Multiple Key Colours | Bit flags for inventory (bit 0 = red, bit 1 = blue, etc.) | Colour-coded puzzles |
| 22 | Locked Door Sound | Beeper: denied (low buzz) | Feedback on blocked |
| 23 | Door Open Sound | Beeper: success (rising tone) | Feedback on unlock |
| 24 | Health System | Health points (1–4) instead of instant death | Forgiveness |
| 25 | Potion Item | New item type restores health on collect | Strategic resource |
| 26 | Status Bar | Health, score, keys shown in bottom two rows | **Clear HUD** |
| 27 | Second Room | Room data table with index, load by number | Two rooms |
| 28 | Room Transition | Clear screen, load new room, reposition player | Moving between rooms |
| 29 | Room Connections | Data table: which exit leads where | Directed navigation |
| 30 | Room Variety | 4+ rooms with different layouts and item placement | Exploration |
| 31 | Map Connectivity | Each room knows its neighbours (N/S/E/W) | Coherent world |
| 32 | Integration + Balance | Puzzle design, item placement, room flow | Satisfying exploration |

---

## Key Teaching Moments

### Indirect Addressing with HL (Unit 27)

The HL register pair holds a 16-bit address. `LD A,(HL)` reads the byte at that address. `INC HL` advances to the next byte. This is how the Z80 walks through data: point HL at the start of a room's data, read each byte in sequence. Unlike the 6502's indirect indexed mode (which needs a zero-page pointer), HL is always available as a pointer — no setup needed beyond loading it.

### Bit Flags for Inventory (Unit 21)

Four coloured keys fit in one byte: bit 0 = red key, bit 1 = blue key, bit 2 = green key, bit 3 = yellow key. `BIT 0,A` checks for the red key. `SET 1,A` grants the blue key. The Z80's single-bit instructions make this cleaner than byte-level flags. One byte, four keys, no wasted memory.

### Room Data Structure (Unit 29)

Each room needs: layout data (32×24 attributes), connections (which rooms are north/south/east/west), starting items, and player entry position. This is structured data — a record with fields. The IX register with displacement (`LD A,(IX+0)` = north room, `LD A,(IX+1)` = south room) gives field access without offset calculations. This is the Z80 equivalent of struct access.

### Colour as Game Language (Units 17–20)

The attribute system becomes a consistent visual language:
- INK 1 (blue) = wall
- INK 2 (red) = red door / red key
- INK 4 (green) = green door / green key
- BRIGHT = collectible item
- FLASH = hazard

The player learns the game by learning the colours. No HUD icons needed to understand what things are. This is the Spectrum's constraint turned into elegant design.

---

## Z80 Concepts Introduced

1. `LD A,(HL)` / `LD (HL),A` — indirect load/store via HL (Unit 27)
2. `LD HL,nn` — load 16-bit immediate into register pair (Unit 27)
3. `INC HL` / `DEC HL` — 16-bit pointer arithmetic (Unit 27)
4. `LD A,(IX+d)` — indexed with displacement (Unit 29)
5. `PUSH` / `POP` — register pair save/restore on stack (Unit 28)
6. Multiple bit flags in one byte — `BIT`/`SET`/`RES` for inventory (Unit 21)
7. Lookup tables with HL pointer — data-driven room connections (Unit 29)
8. 16-bit addition — `ADD HL,DE` for address calculation (Unit 27)

---

## Hardware

### New in Phase 2

No new hardware — Phase 2 uses attribute memory and screen memory in more structured ways. The advance is in data organisation, not hardware access.

### Attribute Colour Map

| INK Colour | Meaning | Introduced |
|------------|---------|-----------|
| 0 (black) | Floor (invisible on black PAPER) | Phase 1 |
| 1 (blue) | Wall | Phase 1 |
| 2 (red) | Red key / Red door | Unit 17 |
| 3 (magenta) | Hazard | Phase 1 (FLASH) |
| 4 (green) | Green key / Green door | Unit 21 |
| 5 (cyan) | Potion / Health item | Unit 25 |
| 6 (yellow) | Treasure | Phase 1 (BRIGHT) |
| 7 (white) | Player character | Phase 1 |

---

## Game State at Phase End

After Unit 32:

- **4+ rooms** — connected by doorways, each with unique layout
- **Coloured keys** — red, blue, green, yellow — unlock matching doors
- **Inventory** — bit flags track held keys, displayed in status bar
- **Health system** — 4 HP, potions restore, enemies/hazards reduce
- **Potions** — health restoration items scattered through rooms
- **Status bar** — health, score, keys, room number
- **Room transitions** — screen clear, new room loads, player repositioned
- **Sound** — collect, denied, unlock, damage, room complete

The keep has structure. Rooms connect logically. Keys create routing puzzles. The player plans a path.

---

## What Carries to Phase 3

- **Room data structure** — enemy placement data added per room
- **Health system** — enemies deal damage instead of instant death
- **Attribute collision** — extended to detect enemy characters
- **Status bar** — adds weapon/combat information
- **Inventory system** — expanded for weapons and special items

---

**Version:** 1.0
**Last Updated:** 2026-02-06
