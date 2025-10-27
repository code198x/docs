# Lesson 027: Score Display in Nametable

**Arc:** Scoring System
**Position:** Lesson 3 of 4 in arc
**Type:** Standard
**Estimated Completion:** 90 lines of assembly

## Learning Objectives
- Write score digits to nametable during VBlank
- Calculate nametable addresses for score display
- Update specific tiles without redrawing entire screen
- Create status bar layout

## Key Concepts
**Nametable Addressing** - $2000 + (Y × 32) + X for tile position
**VBlank Updates** - Only write to VRAM during VBlank window
**Status Bar** - Top 2 rows reserved for scores (row 0-1)
**PPU Address Sequence** - Write high byte, then low byte to $2006

## Code Pattern
```asm6502
.segment "ZEROPAGE"
nametable_update: .res 1  ; Flag: update needed

.segment "CODE"
; NMI handler (runs during VBlank)
NMI:
    PHA
    TXA
    PHA
    TYA
    PHA

    ; OAM DMA (always first)
    LDA #$00
    STA $2003
    LDA #>oam_buffer
    STA $4014

    ; Update nametable if flagged
    LDA nametable_update
    BEQ @no_update
    JSR UpdateScoreDisplay
    LDA #$00
    STA nametable_update

@no_update:
    ; Restore registers
    PLA
    TAY
    PLA
    TAX
    PLA

    ; Set ready flag
    LDA #$01
    STA nmi_ready

    RTI

; Update score display in nametable
UpdateScoreDisplay:
    ; Player 1 score at position (4, 1)
    LDA score_p1
    JSR ScoreToDigits       ; digit_tens, digit_ones set

    ; Write P1 tens digit
    LDA #$20                ; Nametable $2000
    STA $2006
    LDA #(1*32 + 4)         ; Row 1, Column 4
    STA $2006

    LDA digit_tens
    JSR DigitToTile
    STA $2007               ; Write tile

    ; Write P1 ones digit
    LDA #$20
    STA $2006
    LDA #(1*32 + 5)         ; Row 1, Column 5
    STA $2006

    LDA digit_ones
    JSR DigitToTile
    STA $2007

    ; Player 2 score at position (26, 1)
    LDA score_p2
    JSR ScoreToDigits

    ; Write P2 tens digit
    LDA #$20
    STA $2006
    LDA #(1*32 + 26)
    STA $2006

    LDA digit_tens
    JSR DigitToTile
    STA $2007

    ; Write P2 ones digit
    LDA #$20
    STA $2006
    LDA #(1*32 + 27)
    STA $2006

    LDA digit_ones
    JSR DigitToTile
    STA $2007

    RTS

; Main loop - flag score update
ScorePlayer1:
    INC score_p1
    LDA #$01
    STA nametable_update    ; Request nametable update
    ; ... win check ...
    RTS
```

## Status Bar Layout

```
Row 0: +--------------------------------+
       |         P O N G                |
Row 1: |   00                      00   |
       |   ^^                      ^^   |
       |   P1 score               P2    |
Row 2: +================================+
       |                                |
       |   (Play area begins row 3)     |
```

## Quick Reference
### Nametable Address Calculation
```
Address = $2000 + (row × 32) + column
Example: Row 1, Col 4 = $2000 + 32 + 4 = $2024
```

### VBlank Update Pattern
```asm6502
; In game logic:
LDA #$01
STA nametable_update

; In NMI:
LDA nametable_update
BEQ skip
JSR UpdateScoreDisplay
LDA #$00
STA nametable_update
```

---

**Version:** 1.0
**Created:** 2025-10-27
