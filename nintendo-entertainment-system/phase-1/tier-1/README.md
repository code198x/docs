# Tier 1: Pong (Lessons 1-32)

**Philosophy:** Assembly-first fundamentals through immediate game results
**Arc Length:** Focused (4-8 lessons per feature)
**Game Built:** 2-player Pong (60fps)
**Code Range:** Starting with ~50 bytes (minimal program) to ~2KB (complete game)
**Hardware Introduced:** PPU basics, OAM sprites, controller input, VBlank timing

## Goals

- Write first 6502 assembly program that runs on NES
- Understand NES hardware architecture (PPU, CPU, APU basics)
- Master VBlank synchronization for 60fps gameplay
- Implement sprite-based paddle movement with controller input
- Build complete two-player Pong with collision and scoring
- Experience assembly game development from day one

## Arcs Overview

### Arc 1: Hello, NES (L1-4)
**Milestone:** Display single color on screen
**Concepts:** iNES header, reset vector, PPU initialization, infinite loop

- **L1:** Minimal NES Program - Boot and display solid color
- **L2:** Understanding PPU - How the graphics chip works
- **L3:** CPU and Memory Map - 6502 basics and NES memory layout
- **L4:** VBlank Timing - Synchronizing with the screen refresh

### Arc 2: Background Graphics (L5-8)
**Milestone:** Display playfield (solid color with borders)
**Concepts:** Nametables, CHR-ROM, pattern tables, palettes

- **L5:** Pattern Tables - Creating 8×8 pixel tiles in CHR-ROM
- **L6:** Palettes - Choosing background colors
- **L7:** Nametables - Background tile layout (32×30 grid)
- **L8:** Playfield - Pong court with center line and borders

### Arc 3: Sprite Fundamentals (L9-12)
**Milestone:** Display and move a paddle sprite
**Concepts:** OAM (Object Attribute Memory), sprite DMA, sprite positioning

- **L9:** Sprite Basics - Creating paddle graphic in CHR-ROM
- **L10:** OAM Structure - 4-byte sprite format (Y, tile, attributes, X)
- **L11:** Sprite DMA - Fast OAM updates during VBlank ($4014)
- **L12:** Moving Paddle - Update sprite position each frame

### Arc 4: Controller Input (L13-16)
**Milestone:** Control paddle with D-pad
**Concepts:** Controller polling, input registers ($4016/$4017), button state

- **L13:** Controller Basics - Reading $4016 register
- **L14:** Button Detection - Isolating D-pad Up/Down
- **L15:** Paddle Control - Link input to sprite Y position
- **L16:** Boundaries - Prevent paddle from leaving screen

### Arc 5: Two-Player System (L17-20)
**Milestone:** Two paddles (left and right)
**Concepts:** Controller 2 input, multiple sprites, player state

- **L17:** Second Paddle - Adding player 2 sprite
- **L18:** Controller 2 - Reading second controller ($4017)
- **L19:** Independent Control - Each player moves their paddle
- **L20:** Collision Bounds - Both paddles respect screen edges

### Arc 6: Ball Physics (L21-24)
**Milestone:** Bouncing ball sprite
**Concepts:** Velocity, direction, sprite-to-sprite collision

- **L21:** Ball Sprite - Adding third sprite for ball
- **L22:** Velocity - Ball moves with X and Y speed
- **L23:** Wall Bounce - Ball reflects off top/bottom
- **L24:** Paddle Bounce - Ball reflects off paddles (basic collision)

### Arc 7: Scoring System (L25-28)
**Milestone:** Track and display score
**Concepts:** Binary-to-decimal conversion, score display with background tiles

- **L25:** Score Variables - RAM storage for player scores
- **L26:** Point Detection - Increment score when ball exits sides
- **L27:** Number Tiles - Creating 0-9 digits in CHR-ROM
- **L28:** Score Display - Update nametable with current scores

### Arc 8: Game Loop Polish (L29-32)
**Milestone:** Complete Pong game with win condition
**Concepts:** Game states, reset/serve, win detection, title screen basics

- **L29:** Serve System - Ball starts from center after point
- **L30:** Win Condition - First to 11 points
- **L31:** Game Reset - Start new game after win
- **L32:** **SYNTHESIS** - Complete Pong (60fps, 2-player, scoring)

## Learning Outcomes

By completing Tier 1, you will have:

- Written your first 6502 assembly programs for NES
- Understood iNES ROM format (header, PRG-ROM, CHR-ROM)
- Mastered VBlank synchronization for 60fps timing
- Programmed the PPU for background and sprite rendering
- Implemented controller input polling for both players
- Created sprite-based collision detection
- Built complete game state management
- Compiled and tested NES .nes ROM files
- Debugged assembly code with emulator tools

## Prerequisites

None. This is the starting point for the entire NES curriculum. Tier 1 assumes:
- No prior programming experience
- No prior assembly knowledge
- No prior NES development experience

**Tools needed:**
- ca65/ld65 assembler (cc65 toolchain)
- Mesen emulator with debugger
- Text editor

## Builds Toward

**Tier 2:** Breakout (brick collision, complex playfield, score HUD)
**Next Concepts:** More sprites, complex collision, nametable manipulation, attribute tables

## Key Discovery Moments

Throughout Tier 1, you'll experience several "wow" realizations:

1. **L1:** "I made the NES display something - assembly isn't scary!"
2. **L4:** "VBlank timing makes 60fps automatic - the hardware helps me!"
3. **L8:** "The playfield is just tiles - simple but effective!"
4. **L11:** "Sprite DMA updates all 64 sprites instantly!"
5. **L16:** "I'm controlling a paddle with assembly - this is real!"
6. **L24:** "Ball physics work - I'm building a real game!"
7. **L32:** "I built a complete NES game from scratch in assembly!"

## Teaching Notes

**Assembly-first philosophy:**
- Don't apologize for assembly - make it exciting
- Immediate results (display color in lesson 1)
- Gradual complexity (add features incrementally)
- Reference classic NES games for motivation

**6502 instruction introduction order:**
1. **L1-4:** LDA, STA (load/store), JMP (infinite loop)
2. **L5-8:** TAX, TAY (transfer), INX, DEX (increment/decrement)
3. **L9-12:** CMP, BNE, BEQ (compare and branch)
4. **L13-16:** AND, ORA (bit manipulation for input)
5. **L17-20:** JSR, RTS (subroutines for organization)
6. **L21-24:** ADC, SBC (arithmetic for physics)
7. **L25-28:** Loops and tables (score display)
8. **L29-32:** Complete game state machine

**PPU fundamentals taught:**
- $2000: PPU control register
- $2001: PPU mask register (enable rendering)
- $2002: PPU status (VBlank flag)
- $2003/$2004: OAM address/data
- $2005: Scroll position (set to 0,0)
- $2006/$2007: VRAM address/data
- $4014: OAM DMA (sprite batch update)

**VBlank timing emphasis:**
- Every program must synchronize with VBlank
- NMI (Non-Maskable Interrupt) is the standard approach
- ~2273 cycles available during VBlank (NTSC)
- OAM DMA happens during VBlank
- Nametable/palette updates during VBlank

**Pong as teaching vehicle:**
- Simple rules (everyone understands Pong)
- Covers all core NES features (sprites, background, input, collision)
- 60fps achievable in assembly on lesson 32
- Foundation for all future games

## Comparison with Other Platforms

| Aspect | NES (Assembly) | C64 (Phase 0 BASIC) | ZX Spectrum (Phase 0 BASIC) |
|--------|----------------|---------------------|------------------------------|
| **First program** | Display color (assembly) | PRINT counter (BASIC) | PRINT counter (BASIC) |
| **Graphics** | PPU tiles/sprites | POKE screen memory | PRINT AT, PLOT |
| **Input** | Read $4016/$4017 | PEEK keyboard | INKEY$ |
| **Game loop** | VBlank NMI | GOTO loop | GO TO loop |
| **Difficulty** | High (assembly) | Low (BASIC) | Low (BASIC) |
| **Results** | Professional quality | Educational | Educational |

NES students write more complex code but achieve commercial-quality results from tier 1.

## NES-Specific Techniques Introduced

### iNES Header (L1)
16-byte header specifying:
- PRG-ROM size (program code)
- CHR-ROM size (graphics data)
- Mapper number (0 for NROM)
- Mirroring mode (vertical/horizontal)

### Reset Vector (L1-2)
```asm
.segment "VECTORS"
.word NMI_Handler    ; $FFFA: NMI
.word Reset_Handler  ; $FFFC: Reset (start here)
.word IRQ_Handler    ; $FFFE: IRQ
```

### PPU Initialization Sequence (L2-3)
Must wait 2 VBlanks after reset before PPU is stable:
1. Wait for first VBlank (bit 7 of $2002)
2. Initialize memory, variables
3. Wait for second VBlank
4. Enable PPU rendering

### OAM DMA Pattern (L11)
```asm
LDA #$02        ; High byte of $0200 (OAM buffer)
STA $4014       ; Trigger DMA (copies 256 bytes)
                ; Takes 513 CPU cycles
```

### Controller Reading Pattern (L13-14)
```asm
LDA #$01
STA $4016       ; Strobe controller
LDA #$00
STA $4016       ; Stop strobe
LDA $4016       ; Read A button
LDA $4016       ; Read B button
; ... 8 reads total
```

### VBlank NMI Handler Structure (L4)
```asm
NMI_Handler:
    ; Save registers
    PHA             ; Push A
    TXA
    PHA             ; Push X
    TYA
    PHA             ; Push Y

    ; Update graphics (OAM DMA, palettes, etc.)

    ; Restore registers
    PLA
    TAY             ; Pull Y
    PLA
    TAX             ; Pull X
    PLA             ; Pull A
    RTI             ; Return from interrupt
```

## Quick Reference

**Memory Regions:**
- $0000-$00FF: Zero Page (fast access)
- $0100-$01FF: Stack
- $0200-$02FF: OAM buffer (sprite data)
- $0300-$07FF: General RAM
- $8000-$FFFF: PRG-ROM (program code)

**PPU Registers:**
- $2000: PPUCTRL (control)
- $2001: PPUMASK (enable rendering)
- $2002: PPUSTATUS (VBlank flag bit 7)
- $2003: OAMADDR (OAM address)
- $2004: OAMDATA (OAM write)
- $2005: PPUSCROLL (scroll position)
- $2006: PPUADDR (VRAM address)
- $2007: PPUDATA (VRAM read/write)
- $4014: OAMDMA (OAM batch copy)

**Controller Buttons (order when reading $4016):**
1. A
2. B
3. Select
4. Start
5. Up
6. Down
7. Left
8. Right

**Sprite OAM Format (4 bytes):**
- Byte 0: Y position (0-239)
- Byte 1: Tile index (0-255)
- Byte 2: Attributes (palette, flip, priority)
- Byte 3: X position (0-255)

**Useful 6502 Instructions (Tier 1):**
- `LDA`: Load accumulator
- `STA`: Store accumulator
- `LDX/LDY`: Load X/Y register
- `STX/STY`: Store X/Y register
- `TAX/TAY/TXA/TYA`: Transfer between A, X, Y
- `CMP`: Compare (sets flags)
- `BNE/BEQ`: Branch if not equal / equal
- `JMP`: Jump to address
- `JSR`: Jump to subroutine
- `RTS`: Return from subroutine
- `INX/INY`: Increment X/Y
- `DEX/DEY`: Decrement X/Y

---

**Version:** 1.0
**Created:** 2025-10-23
**Status:** Overview complete - individual lesson specs to be created
