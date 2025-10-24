# Lesson 010: OAM Structure

**Arc:** Sprite Fundamentals
**Position:** Lesson 2 of 4 in arc
**Type:** Standard
**Estimated Completion:** 30 lines of assembly

## Learning Objectives

- Understand OAM (Object Attribute Memory)
- Master 4-byte sprite format
- Create OAM buffer in RAM
- Write sprite data manually

## Key Concepts Introduced

### OAM (Object Attribute Memory)
256 bytes of sprite data inside PPU. 64 sprites × 4 bytes each. Describes position, tile, palette, and flip flags.

### 4-Byte Sprite Format
- Byte 0: Y position (0-239, but sprites at 0-1 are hidden)
- Byte 1: Tile index (which tile from pattern table)
- Byte 2: Attributes (palette, flip, priority)
- Byte 3: X position (0-255)

### OAM Buffer ($0200-$02FF)
CPU can't write OAM directly (too slow). Build sprite data at $0200-$02FF, then use DMA ($4014) to copy during VBlank.

### Sprite Attributes (Byte 2)
- Bits 0-1: Palette (0-3)
- Bit 5: Priority (0=front, 1=behind background)
- Bit 6: Flip horizontal
- Bit 7: Flip vertical

## Code Pattern

```asm
.segment "ZEROPAGE"
paddle_y: .res 1

.segment "CODE"
Reset:
    ; [PPU warmup, palette, playfield from previous lessons]

    ; Initialize paddle position
    LDA #100
    STA paddle_y

    ; Set up sprite in OAM buffer
    ; Sprite 0: Paddle at left side
    LDA paddle_y
    STA $0200        ; Y position

    LDA #$00
    STA $0201        ; Tile index $00 (paddle top)

    LDA #%00000000   ; Palette 0, no flip
    STA $0202        ; Attributes

    LDA #16
    STA $0203        ; X position

    ; Hide remaining sprites (Y = $FF)
    LDX #$04
    LDA #$FF
:   STA $0200,X
    INX
    INX
    INX
    INX
    BNE :-

    ; Enable rendering (8×16 sprites)
    LDA #%10100000   ; NMI, 8×16 sprites, pattern table 1
    STA $2000

    LDA #%00011110   ; Show background and sprites
    STA $2001

MainLoop:
    JMP MainLoop
```

## Attribute Byte Reference

```
Bit 7-6: Flip
  00 = No flip
  01 = Flip horizontal
  10 = Flip vertical
  11 = Flip both

Bit 5: Priority
  0 = In front of background
  1 = Behind background (except colour 0)

Bit 2-4: Unused

Bit 1-0: Palette
  00 = Sprite palette 0
  01 = Sprite palette 1
  10 = Sprite palette 2
  11 = Sprite palette 3
```

## Quick Reference

### OAM Memory Layout
```
$0200: Sprite 0 (Y, tile, attr, X)
$0204: Sprite 1
$0208: Sprite 2
...
$02FC: Sprite 63
```

### Hiding Sprites
Set Y position to $FF (off-screen). Sprite won't render but still processes (uses DMA time).

---

**Version:** 1.0
**Created:** 2025-10-24
