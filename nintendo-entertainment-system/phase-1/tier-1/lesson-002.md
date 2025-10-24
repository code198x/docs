# Lesson 002: Understanding PPU

**Arc:** Hello, NES
**Position:** Lesson 2 of 4 in arc
**Type:** Standard
**Estimated Completion:** 20 lines of assembly (experimentation)

## Learning Objectives

- Understand PPU architecture
- Master PPU register usage
- Explore palette system
- Change background colours

## Key Concepts Introduced

### PPU Architecture
Independent graphics processor. Handles all display work while CPU runs game logic. 256×240 resolution, 60Hz refresh, tile-based rendering.

### PPU Registers
Memory-mapped at $2000-$2007. CPU writes to these to control PPU. $2006 (address) then $2007 (data) pattern for VRAM access.

### Palette Memory
$3F00-$3F1F in PPU memory. Background palettes ($3F00-$3F0F), sprite palettes ($3F10-$3F1F). Each palette has 4 colours.

### NES Colour System
64 total colours (master palette). Colours numbered $00-$3F. Each palette entry indexes into master palette.

## Code Pattern

```asm
; Change background colour to different values
Reset:
    SEI
    CLD

    ; Wait for PPU warmup
    BIT $2002
:   BIT $2002
    BPL :-
:   BIT $2002
    BPL :-

    ; Try different colours
    LDA #$3F
    STA $2006
    LDA #$00
    STA $2006

    ; Colour $0F (black), $30 (white), $29 (green), $12 (blue)
    LDA #$12        ; Try changing this value!
    STA $2007

    ; Enable rendering
    LDA #%00001000
    STA $2001

Forever:
    JMP Forever
```

## Palette Reference

Common NES Colours:
- $0F: Black
- $00: Dark grey
- $10: Light grey
- $20: White
- $30: White (same as $20)
- $29: Green
- $12: Blue
- $16: Red
- $27: Orange
- $1A: Light green
- $21: Sky blue

## Quick Reference

### PPU Control Flow
1. Set PPUADDR high byte ($2006)
2. Set PPUADDR low byte ($2006)
3. Read/write PPUDATA ($2007)
4. PPUADDR auto-increments after each access

### PPU Memory Map
- $0000-$1FFF: Pattern tables (CHR-ROM)
- $2000-$2FFF: Nametables (background layout)
- $3F00-$3F1F: Palettes (colours)

### Why Two $2006 Writes?
PPUADDR is 16-bit but CPU is 8-bit. Write high byte first, then low byte. PPU combines them internally.

---

**Version:** 1.0
**Created:** 2025-10-24
