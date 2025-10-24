# Lesson 009: Sprite Basics

**Arc:** Sprite Fundamentals
**Position:** Lesson 1 of 4 in arc
**Type:** Standard
**Estimated Completion:** CHR-ROM design + 20 lines

## Learning Objectives

- Understand sprite system (64 hardware sprites)
- Create paddle graphic in CHR-ROM
- Design 8×16 sprite shapes
- Master sprite pattern tables

## Key Concepts Introduced

### NES Sprite System
64 hardware sprites, 8×8 or 8×16 pixels each. Independent from background. Hardware-accelerated rendering with transparency and priority.

### Sprite Pattern Table
Sprites use pattern table 0 or 1 (selected by PPUCTRL bit 3). Same 2-bit pixel format as background tiles. Colour 0 is transparent.

### 8×16 Sprite Mode
Two consecutive tiles form tall sprite. Useful for characters and paddles. Top tile = even number, bottom = odd number. Automatic vertical arrangement.

### Paddle Design
Vertical rectangle, 8×16 pixels. Simple solid shape or detailed design. Colour 3 for main colour (brightest in palette).

## Code Pattern

```asm
; CHR-ROM: Sprite pattern table
.segment "CHARS"

; Background tiles (256 tiles)
; [Border, line tiles from previous lessons]
.res 256*16, $00

; Sprite tiles start at $1000 (pattern table 1)
; Tile $00-$01: Paddle (8×16 sprite)
; Top half ($00)
.byte $3C,$3C,$3C,$3C,$3C,$3C,$3C,$3C  ; Plane 0
.byte $3C,$3C,$3C,$3C,$3C,$3C,$3C,$3C  ; Plane 1

; Bottom half ($01)
.byte $3C,$3C,$3C,$3C,$3C,$3C,$3C,$3C  ; Plane 0
.byte $3C,$3C,$3C,$3C,$3C,$3C,$3C,$3C  ; Plane 1

; Tile $02: Ball (8×8 sprite)
.byte $00,$18,$3C,$7E,$7E,$3C,$18,$00  ; Plane 0
.byte $00,$18,$3C,$7E,$7E,$3C,$18,$00  ; Plane 1

; Remaining sprite tiles
.res 253*16, $00
```

## Paddle Design Examples

Simple solid paddle:
```
  3 3 . . . . 3 3    Hex: $C3,$C3,$C3,$C3
  3 3 . . . . 3 3          $C3,$C3,$C3,$C3
  3 3 . . . . 3 3    (repeated for 8 rows)
  ...
```

Detailed paddle with edge:
```
  3 3 3 3 3 3 3 3    Hex: $FF,$C3,$C3,$C3
  3 3 . . . . 3 3          $C3,$C3,$C3,$FF
  3 3 . . . . 3 3    (top/bottom differ)
  ...
```

## Quick Reference

### Sprite Sizes
- 8×8 mode: Each sprite = 1 tile
- 8×16 mode: Each sprite = 2 tiles (vertical)
- Set in PPUCTRL bit 5

### Pattern Table Selection
- PPUCTRL bit 3 = 0: Use pattern table 0 ($0000)
- PPUCTRL bit 3 = 1: Use pattern table 1 ($1000)

### Colour 0 = Transparent
Any pixel with value 0 shows background through sprite. Use colours 1-3 for visible pixels.

---

**Version:** 1.0
**Created:** 2025-10-24
