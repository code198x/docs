# Lesson 006: Palettes

**Arc:** Background Graphics
**Position:** Lesson 2 of 4 in arc
**Type:** Standard
**Estimated Completion:** 25 lines of assembly

## Learning Objectives

- Load background palettes
- Understand 4-colour palette structure
- Master palette memory layout
- Choose effective game colours

## Key Concepts Introduced

### Palette Structure
Background: 4 palettes × 4 colours each at $3F00-$3F0F. Sprites: 4 palettes at $3F10-$3F1F. First colour ($3F00) is universal background.

### Universal Background Colour
$3F00 is backdrop colour. Shows where no tiles are drawn. Also shows through transparent pixels (colour 0) in tiles.

### Palette Selection
Tiles reference palette 0-3 via attribute table. Each 16×16 pixel area uses one palette. Limitation: only 4 colours per 16×16 region.

### Writing Palettes
Set PPUADDR to $3F00, write 16 bytes for background palettes. Usually done during init or VBlank.

## Code Pattern

```asm
Reset:
    SEI
    CLD

    ; PPU warmup
    BIT $2002
:   BIT $2002
    BPL :-
:   BIT $2002
    BPL :-

    ; Load background palettes
    LDA $2002        ; Reset latch
    LDA #$3F
    STA $2006
    LDA #$00
    STA $2006

    ; Palette 0 (Pong court - black/white)
    LDA #$0F         ; Universal background (black)
    STA $2007
    LDA #$30         ; Colour 1 (white)
    STA $2007
    LDA #$30         ; Colour 2 (white)
    STA $2007
    LDA #$30         ; Colour 3 (white)
    STA $2007

    ; Palette 1-3 (unused for now)
    LDX #12
:   LDA #$0F
    STA $2007
    DEX
    BNE :-

    ; Enable rendering
    LDA #%00001010   ; Show background
    STA $2001

MainLoop:
    JMP MainLoop
```

## Pong Colour Schemes

Classic arcade look:
```
Palette 0 (court):
  $0F (black background)
  $30 (white lines)
  $30 (white borders)
  $30 (white text)
```

Modern variant:
```
Palette 0:
  $0F (black background)
  $21 (cyan court)
  $30 (white score)
  $16 (red accents)
```

## Quick Reference

### Palette Memory Map
- $3F00: Universal background
- $3F01-$3F03: Background palette 0
- $3F04: Mirror of $3F00
- $3F05-$3F07: Background palette 1
- $3F08: Mirror of $3F00
- $3F09-$3F0B: Background palette 2
- $3F0C: Mirror of $3F00
- $3F0D-$3F0F: Background palette 3

### Common Colours for Pong
- $0F: Black (background)
- $00: Dark grey (shadow)
- $30: White (lines, borders)
- $21: Light blue (variant)
- $16: Red (accents)

---

**Version:** 1.0
**Created:** 2025-10-24
