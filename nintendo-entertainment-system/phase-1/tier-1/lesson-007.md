# Lesson 007: Nametables

**Arc:** Background Graphics
**Position:** Lesson 3 of 4 in arc
**Type:** Standard
**Estimated Completion:** 50 lines of assembly

## Learning Objectives

- Understand nametable structure
- Write tiles to screen
- Master 32×30 tile grid
- Create static backgrounds

## Key Concepts Introduced

### Nametable Layout
32×30 grid of tile indices at $2000-$23BF. Each byte is tile number from pattern table. 960 tiles cover 256×240 screen.

### Tile Coordinates
Row 0-29, column 0-31. Address = $2000 + (row × 32) + column. Top-left is $2000, bottom-right is $23BF.

### Writing to Nametable
Set PPUADDR to nametable address, write tile indices to PPUDATA. PPUADDR auto-increments. Write row-by-row or use PPUCTRL bit 2 for column-by-column.

### Attribute Table
Follows nametable at $23C0-$23FF. Sets palette per 16×16 pixel area. 2 bits per area, 4 areas per byte.

## Code Pattern

```asm
Reset:
    ; [PPU warmup code from previous lessons]

    ; Load palettes
    ; [Palette code from lesson 006]

    ; Fill nametable with blank tiles
    LDA $2002        ; Reset latch
    LDA #$20
    STA $2006
    LDA #$00
    STA $2006

    LDA #$00         ; Tile 0 (blank)
    LDX #$04         ; 4 × 256 = 1024 bytes
:   LDY #$00
:   STA $2007
    DEY
    BNE :-
    DEX
    BNE :--

    ; Draw top border (row 0)
    LDA $2002
    LDA #$20
    STA $2006
    LDA #$00
    STA $2006

    LDA #$01         ; Tile $01 (solid)
    LDX #32
:   STA $2007
    DEX
    BNE :-

    ; Draw bottom border (row 29)
    LDA $2002
    LDA #$23
    STA $2006
    LDA #$A0
    STA $2006

    LDA #$01
    LDX #32
:   STA $2007
    DEX
    BNE :-

    ; Enable rendering
    LDA #%00001010
    STA $2001

    JMP MainLoop
```

## Quick Reference

### Nametable Memory
- $2000-$23BF: Nametable (960 tiles)
- $23C0-$23FF: Attribute table (64 bytes)
- $2400-$27FF: Nametable 1 (mirroring)
- $2800-$2BFF: Nametable 2 (mirroring)
- $2C00-$2FFF: Nametable 3 (mirroring)

### Address Calculation
```
address = $2000 + (row * 32) + column
```

### PPUCTRL Increment
- Bit 2 = 0: Add 1 (horizontal, across)
- Bit 2 = 1: Add 32 (vertical, down)

---

**Version:** 1.0
**Created:** 2025-10-24
