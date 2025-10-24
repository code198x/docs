# Lesson 005: Pattern Tables

**Arc:** Background Graphics
**Position:** Lesson 1 of 4 in arc
**Type:** Standard
**Estimated Completion:** CHR-ROM design + 15 lines

## Learning Objectives

- Understand pattern tables (CHR-ROM)
- Create 8×8 pixel tiles
- Design border and line graphics
- Master 2-bit pixel encoding

## Key Concepts Introduced

### Pattern Tables
Two 4KB banks at $0000 and $1000 in PPU memory. Each tile is 16 bytes (8×8 pixels, 2 bits per pixel). Background uses one bank, sprites use either.

### 2-Bit Pixels
Each pixel uses 2 bits for 4 colours (0-3). Bits split across two 8-byte planes. Plane 0 (low bit) + Plane 1 (high bit) = pixel value.

### CHR-ROM
Graphics stored in ROM chip on cartridge. Loaded by .segment "CHARS". 8KB = 512 tiles. Can't change at runtime (without mapper).

### Tile Design Pattern
Draw on graph paper or pixel editor. Convert to hex bytes. Plane 0 first (8 bytes), then plane 1 (8 bytes).

## Code Pattern

```asm
; In CHR-ROM: Create solid tile and border tiles
.segment "CHARS"

; Tile $00: Blank (transparent)
.byte $00,$00,$00,$00,$00,$00,$00,$00
.byte $00,$00,$00,$00,$00,$00,$00,$00

; Tile $01: Solid block
.byte $FF,$FF,$FF,$FF,$FF,$FF,$FF,$FF
.byte $FF,$FF,$FF,$FF,$FF,$FF,$FF,$FF

; Tile $02: Top border
.byte $FF,$FF,$00,$00,$00,$00,$00,$00
.byte $FF,$FF,$00,$00,$00,$00,$00,$00

; Tile $03: Vertical line (center court)
.byte $18,$18,$18,$18,$18,$18,$18,$18
.byte $18,$18,$18,$18,$18,$18,$18,$18

; Remaining tiles (507 more)
.res 507*16, $00
```

## Tile Encoding Example

Drawing "X" pattern:
```
  Pixel pattern:     Plane 0:    Plane 1:
  . 3 . . . . 3 .    01000001    01000001
  . . 3 . . 3 . .    00100010    00100010
  . . . 3 3 . . .    00011000    00011000
  . . . 3 3 . . .    00011000    00011000
  . . 3 . . 3 . .    00100010    00100010
  . 3 . . . . 3 .    01000001    01000001
  
  Hex: $41,$22,$18,$18,$22,$41
       $41,$22,$18,$18,$22,$41
```

## Quick Reference

### Pattern Table Layout
- $0000-$0FFF: Pattern table 0 (256 tiles)
- $1000-$1FFF: Pattern table 1 (256 tiles)
- Each tile: 16 bytes (8 rows × 2 planes)

### Pixel Value Calculation
```
Bit 0 (plane 0): $00-$07
Bit 1 (plane 1): $08-$0F
Value = (plane1_bit << 1) | plane0_bit
```

---

**Version:** 1.0
**Created:** 2025-10-24
