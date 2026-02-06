# Phase 4: The Labyrinth

**Game:** Shadowkeep (ZX Spectrum Game 1)
**Units:** 49–64
**Theme:** The maze expands — many rooms, compressed data, a map
**Z80 Focus:** Block operations (LDIR/LDDR), 16-bit arithmetic, data compression, memory management
**Hardware:** Contended memory timing, efficient screen writes
**Status:** Planned

---

## Overview

Four rooms is a puzzle. Sixteen rooms is a labyrinth. Phase 4 expands the keep to a real maze — enough rooms that the player needs a map, enough variety that each area feels distinct, and enough data that compression becomes necessary.

The Z80 focus is block operations and memory management. `LDIR` (Load, Increment, Repeat) copies a block of memory in a single instruction — essential for fast room drawing. `LDDR` copies in reverse. These are the Z80's hardware-accelerated alternatives to byte-by-byte loops, and they transform room transitions from sluggish redraws to near-instant loads.

Data compression appears for the first time: room layouts use run-length encoding to fit more rooms in memory. The 48K Spectrum has ~42KB of user RAM, and each uncompressed room takes 768 bytes (one attribute per cell). Sixteen rooms at 768 bytes = 12KB just for room data — compression is a practical necessity, not an academic exercise.

---

## Prerequisites from Phase 3

- Room data structure — expanded with enemy data, item placement, connections
- HL pointer manipulation — used extensively for data decompression
- CALL/RET — subroutines for room loading, drawing, transitions
- Enemy table processing — enemies now defined per room in data

---

## Unit Progression

| Unit | Title | New Z80 Concept | Game Addition |
|------|-------|----------------|---------------|
| 49 | LDIR — Block Copy | `LDIR` for fast memory copy (BC=count, DE=dest, HL=src) | Instant room draw |
| 50 | Room Buffer | Copy room data to working buffer, modify in place | Rooms reset on re-entry |
| 51 | Run-Length Encoding | Compression: repeat-byte + count pairs | Compact room storage |
| 52 | RLE Decompression | Expand RLE data to attribute buffer | Rooms load from compressed data |
| 53 | 8+ Rooms | Expanded room table, room index lookup | Larger world |
| 54 | Room Themes | Different colour palettes per area (change PAPER/INK mapping) | Visual variety |
| 55 | 16-Bit Room Pointers | `LD HL,(table_addr)` for room data addresses | Address tables for many rooms |
| 56 | Map Display | Show visited rooms as grid on pause screen | **Player orientation** |
| 57 | Map Data | Bit flags per room (visited, has key, has boss) | Tracked exploration |
| 58 | One-Way Passages | Attribute marks one-way door — enter but can't return easily | Routing challenge |
| 59 | Teleport Tiles | Step on tile, warp to distant room | Surprising navigation |
| 60 | Save Points | Checkpoint tile, respawn here on death | Fairness in large maze |
| 61 | Contended Memory | Understanding $4000–$7FFF timing penalty | Why screen writes slow down |
| 62 | Fast Attribute Fill | Optimised attribute write loop, avoid contended timing | Faster room transitions |
| 63 | Room Count Display | "Room X of Y" in status bar | Progress indication |
| 64 | Integration + Balance | Room flow, key placement across rooms, route design | Satisfying exploration |

---

## Key Teaching Moments

### LDIR — The Block Copy (Unit 49)

`LDIR` copies BC bytes from HL to DE, incrementing both pointers. One instruction replaces an entire loop:

```z80
    ld hl,room_data     ; Source
    ld de,$5800         ; Destination (attributes)
    ld bc,768           ; Byte count (32×24)
    ldir                ; Copy entire room
```

On the 6502, this would be a loop with indexed addressing. On the Z80, it's four setup instructions and one operation. `LDIR` is one of the Z80's genuine luxuries — and it transforms room transitions from multi-frame redraws to near-instant loads.

### Run-Length Encoding (Unit 51)

An uncompressed room is 768 bytes. But most rooms are mostly floor with some walls — highly compressible. RLE stores repeated values as (value, count) pairs. A row of 20 floor cells becomes two bytes instead of twenty. Typical compression ratio: 3:1 to 5:1, meaning 16 rooms fit in 2–4KB instead of 12KB.

The decompressor is simple: read a byte, read a count, write that byte count times, repeat until the buffer is full. This is the learner's first encounter with data compression — a practical solution to a real memory constraint.

### Contended Memory (Unit 61)

The Spectrum's screen memory ($4000–$7FFF) shares the bus with the ULA (the chip that generates the display). When the ULA is reading screen data to draw the picture, the CPU must wait. This slows down any code that accesses this 16KB region. Understanding contended memory explains why screen writes are slower than expected, and motivates techniques like writing attributes during the border period or using an off-screen buffer.

### The Map as Game Feature (Unit 56)

A pause-screen map showing visited rooms serves two purposes: it helps the player navigate, and it teaches the learner about game state visualisation. Each room's visited flag is one bit — 16 rooms fit in 2 bytes. Drawing the map is a nested loop that checks each flag and draws a filled or empty square. Simple concept, satisfying result.

---

## Z80 Concepts Introduced

1. `LDIR` — block copy (load, increment, repeat) (Unit 49)
2. `LDDR` — block copy in reverse (Unit 50, buffer manipulation)
3. Working buffer pattern — copy data to RAM, modify in place (Unit 50)
4. Run-length encoding — compression concept and implementation (Unit 51)
5. RLE decompression loop — expand compressed data (Unit 52)
6. 16-bit indirect load — `LD HL,(addr)` for pointer tables (Unit 55)
7. Contended memory — ULA bus contention on $4000–$7FFF (Unit 61)
8. Optimised screen writes — timing-aware attribute updates (Unit 62)

---

## Hardware

### New in Phase 4

| Resource | Purpose | Introduced |
|----------|---------|-----------|
| Contended memory ($4000–$7FFF) | Bus contention with ULA during display | Unit 61 |

### Memory Budget

| Data | Size (uncompressed) | Size (RLE) | Notes |
|------|---------------------|------------|-------|
| Room attributes | 768 bytes each | ~150–250 bytes | 32×24 cells |
| Room metadata | ~8 bytes each | 8 bytes | Connections, flags |
| Enemy spawn data | ~20 bytes each | 20 bytes | Up to 4 enemies |
| 16 rooms total | ~12.7KB | ~4–5KB | Fits comfortably in RAM |

---

## Game State at Phase End

After Unit 64:

- **16+ rooms** — RLE-compressed, loaded to attribute buffer
- **Room themes** — different colour palettes per area (dungeon, crypt, tower)
- **Map screen** — pause to see visited rooms, current position
- **One-way passages** — routing puzzles, can't always backtrack
- **Teleport tiles** — surprise connections between distant rooms
- **Save points** — checkpoints in the labyrinth, respawn on death
- **Fast transitions** — LDIR-powered room loading
- **Room counter** — "Room X of Y" in status bar

The keep feels large and worth exploring. Route planning matters. The map provides orientation without removing mystery.

---

## What Carries to Phase 5

- **Room buffer** — Phase 5 draws UDG characters into the bitmap based on buffer contents
- **LDIR** — used for character set copying, sprite blitting, screen effects
- **Contended memory awareness** — essential for flicker-free pixel graphics
- **Data compression** — pattern reused for sprite data and level packs

---

**Version:** 1.0
**Last Updated:** 2026-02-06
