# Phase 1: First Steps

**Game:** Dash (NES Game 1)
**Units:** 1-16
**Theme:** A character that runs and jumps across platforms
**6502 Focus:** Registers (A/X/Y), zero page, LDA/STA, ca65 segments, iNES header, NMI handler, PPU register protocol
**Hardware:** PPU ($2000-$2007), OAM DMA ($4014), controller ($4016), APU pulse/triangle ($4000-$4008)
**Status:** Planned

---

## Overview

Phase 1 gets a character on screen, under the player's control, running and jumping across tile-based platforms. The NES requires more setup than other platforms -- the iNES header, PPU warmup, NMI handler, and OAM DMA must all be in place before a single pixel appears. This framework is earned, not given, and every NES game reuses it.

The key insight: the NES is a two-chip system. The CPU can't draw to the screen directly -- it talks to the PPU through registers, and only during VBlank. This discipline shapes everything. By Phase 1's end, learners have internalised the pattern: set up data, wait for NMI, update PPU, repeat.

Jump is introduced in Unit 3 -- the core platformer verb, as early as possible. Tile-based collision follows in Units 7-8. By Unit 16, there's a complete game loop: run, jump, collect items, lose lives, see a score, restart from the title screen.

---

## Prerequisites

None -- this is the first phase of the first NES game.

---

## Unit Progression

| Unit | Title | New 6502 Concept | Game Addition |
|------|-------|------------------|---------------|
| 1 | One Sprite on Screen | ca65 `.segment`, iNES header, `LDA`/`STA`, PPU warmup | See your character |
| 2 | Controller Input | Read `$4016` (strobe + serial), `AND`, `BEQ`/`BNE` | **Control something** |
| 3 | Jump | Velocity variable, gravity (add each frame), impulse | **The core verb** |
| 4 | Landing | Y-position floor check, velocity reset | Solid ground |
| 5 | Jump Sound | APU pulse channel (`$4000`-`$4003`), duty + timer | Satisfying leap |
| 6 | Background Tiles | `$2006`/`$2007` nametable writes during VBlank | Visible level |
| 7 | Platform Collision (Floor) | Read metatile below feet, stop falling if solid | **Platforms work** |
| 8 | Wall Collision | Read metatile at sides, prevent horizontal overlap | Can't walk through walls |
| 9 | Collectible Items | Multiple OAM entries, `JSR`/`RTS` subroutines | Things to pick up |
| 10 | Collect = Score | `CMP` proximity, score in zero page, nametable update | **Reward** |
| 11 | Collect Sound | APU triangle channel (`$4008`-`$400B`) | Audio feedback |
| 12 | Hazard Tiles | Tile type flag, damage on contact | Stakes |
| 13 | Three Lives | Game state, HUD tile update | Forgiveness |
| 14 | Game Over Screen | Nametable writes, state machine | End state |
| 15 | Title Screen + Restart | Full nametable write, button edge detection, state reset | **Complete loop** |
| 16 | Integration + Polish | Sprite hiding (Y=$EF), boundaries, animation frame | Solid foundation |

---

## Key Teaching Moments

### The PPU Boundary (Unit 1)

The NES CPU cannot see the PPU's memory. There's no shared screen RAM like the C64 or Spectrum. Instead, the CPU writes to PPU registers ($2006/$2007 for VRAM address/data, $2003/$2014 for OAM) -- and only during VBlank, the brief period when the PPU isn't drawing. Miss the window, corrupt the screen. This constraint is THE NES skill.

```asm
; Write tile to nametable (MUST be during VBlank)
lda #$20
sta $2006           ; VRAM address high byte
lda #$00
sta $2006           ; VRAM address low byte ($2000 = top-left of nametable)
lda #$01            ; Tile index
sta $2007           ; Write tile to VRAM
```

### The NMI Handler (Unit 1)

The PPU fires an NMI (Non-Maskable Interrupt) at the start of every VBlank. The handler runs OAM DMA, updates PPU registers, and sets a "frame ready" flag. The main loop does game logic and waits for the flag. This NMI-driven structure is the skeleton of every NES game:

```asm
nmi:
    pha
    txa
    pha
    tya
    pha

    ; OAM DMA -- copy sprite buffer to PPU
    lda #$00
    sta $2003           ; OAM address = 0
    lda #>oam_buf       ; High byte of OAM buffer
    sta $4014           ; Trigger DMA (256 bytes copied)

    ; Set frame-ready flag
    lda #$01
    sta nmi_done

    pla
    tay
    pla
    tax
    pla
    rti
```

### Controller Reading (Unit 2)

The NES controller is a shift register. Write 1 then 0 to $4016 to latch the button states. Then read $4016 eight times -- each read returns one button (A, B, Select, Start, Up, Down, Left, Right) in bit 0. The pattern is always the same: strobe, then 8 reads.

### Gravity and Jump (Units 3-4)

Velocity-based physics: `velocity_y` starts at 0. Each frame, add gravity (e.g., +1). To jump, set `velocity_y` to a negative value (e.g., -5). Each frame, add velocity to position. When position reaches the floor, stop and reset velocity. This produces a natural parabolic arc from two additions per frame.

---

## 6502 Concepts Introduced

1. `LDA`/`STA` -- load and store between registers and memory (Unit 1)
2. ca65 segments (`.segment "CODE"`, `"HEADER"`, `"VECTORS"`) -- cartridge layout (Unit 1)
3. PPU register protocol -- address/data writes to $2006/$2007 (Unit 1)
4. NMI handler -- interrupt at VBlank, OAM DMA, frame sync (Unit 1)
5. Controller strobe -- $4016 write/read protocol for input (Unit 2)
6. `AND` for bit masking -- isolate button bits from controller byte (Unit 2)
7. `BEQ`/`BNE` -- conditional branches on zero flag (Unit 2)
8. Zero-page variables -- position, velocity, game state (Unit 3)
9. `INC`/`DEC` -- increment and decrement (Unit 3)
10. `ADC`/`SBC` -- addition and subtraction with carry (Unit 3)
11. `JSR`/`RTS` -- subroutine call and return (Unit 9)
12. `CMP` -- comparison setting flags for distance checks (Unit 10)
13. APU register writes -- pulse and triangle channel setup (Units 5, 11)

---

## Hardware

### PPU Registers Used in Phase 1

| Register | Address | Purpose | Introduced |
|----------|---------|---------|------------|
| PPUCTRL | $2000 | NMI enable, pattern table select, nametable select | Unit 1 |
| PPUMASK | $2001 | Enable sprites, enable background, clipping | Unit 1 |
| PPUSTATUS | $2002 | VBlank flag, reset address latch | Unit 1 |
| OAMADDR | $2003 | OAM address for DMA | Unit 1 |
| PPUADDR | $2006 | VRAM address (double-write) | Unit 6 |
| PPUDATA | $2007 | VRAM data read/write | Unit 6 |

### Other Hardware

| Register | Address | Purpose | Introduced |
|----------|---------|---------|------------|
| OAMDMA | $4014 | Trigger OAM DMA transfer (256 bytes) | Unit 1 |
| Controller 1 | $4016 | Strobe write + serial read for buttons | Unit 2 |
| Pulse 1 | $4000-$4003 | First pulse channel (duty, envelope, timer) | Unit 5 |
| Triangle | $4008-$400B | Triangle channel (linear counter, timer) | Unit 11 |
| APU Status | $4015 | Channel enable bits | Unit 5 |

---

## Game State at Phase End

After Unit 16:

- **Player character** -- sprite on screen, controlled by D-pad
- **Run and jump** -- left/right movement with velocity-based jump
- **Tile-based level** -- background tiles drawn from nametable data
- **Platform collision** -- stand on solid tiles, blocked by walls
- **Collectible items** -- sprite items, proximity detection, score
- **Hazard tiles** -- spike tiles damage the player
- **Three lives** -- displayed in HUD, lost on hazard contact
- **Score display** -- nametable tiles updated during VBlank
- **Sound effects** -- pulse jump sound, triangle collect sound
- **Game over screen** -- state transition on zero lives
- **Title screen** -- press Start to begin
- **Complete loop** -- title -> play -> game over -> title

A character that runs and jumps across platforms. Single screen, but the NES framework is solid.

---

## What Carries to Phase 2

- **NMI framework** -- the handler structure is permanent, extended with scroll updates and music
- **PPU write discipline** -- VBlank-only updates become second nature
- **OAM buffer pattern** -- sprite management evolves into metasprites
- **Tile collision** -- extended to metatiles with different types (one-way, ladder)
- **Controller reading** -- extended with edge detection for menu navigation
- **Game state machine** -- expanded with level transitions and new states

---

**Version:** 1.0
**Last Updated:** 2026-02-06
