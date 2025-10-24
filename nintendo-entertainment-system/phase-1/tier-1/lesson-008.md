# Lesson 008: Playfield

**Arc:** Background Graphics
**Position:** Lesson 4 of 4 in arc
**Type:** Synthesis (Complete Background)
**Estimated Completion:** 80 lines of assembly

## Learning Objectives

- Create complete Pong court
- Draw center line with tiles
- Implement efficient nametable filling
- Master background synthesis

## Key Concepts Introduced

### Playfield Design
Top/bottom borders (rows 0, 29), left/right goals (columns 0, 31), center dashed line (column 16). Classic Pong court layout.

### Efficient Tile Writing
Use loops for repeated tiles. Use subroutines for common patterns. Minimize code size and improve maintainability.

### Dashed Line Pattern
Alternate solid/blank tiles vertically. Create visual center line for Pong court. Use tile $03 for line segments.

### Background Synthesis
Combine multiple techniques: palette loading, pattern table design, nametable filling. Complete static background for gameplay.

## Code Pattern

```asm
DrawPlayfield:
    ; Clear screen
    LDA $2002
    LDA #$20
    STA $2006
    LDA #$00
    STA $2006

    LDA #$00
    LDX #$04
:   LDY #$00
:   STA $2007
    DEY
    BNE :-
    DEX
    BNE :--

    ; Top border (row 0)
    JSR DrawTopBorder

    ; Bottom border (row 29)
    JSR DrawBottomBorder

    ; Center dashed line (column 16)
    JSR DrawCenterLine

    RTS

DrawTopBorder:
    LDA $2002
    LDA #$20
    STA $2006
    LDA #$00
    STA $2006

    LDA #$01
    LDX #32
:   STA $2007
    DEX
    BNE :-
    RTS

DrawBottomBorder:
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
    RTS

DrawCenterLine:
    ; Draw dashed line at column 16
    LDY #1           ; Start at row 1
:   ; Calculate address: $2000 + (Y * 32) + 16
    TYA
    ASL              ; × 2
    ASL              ; × 4
    ASL              ; × 8
    ASL              ; × 16
    ASL              ; × 32
    CLC
    ADC #$20
    STA $2006
    LDA #$10         ; Column 16
    STA $2006

    ; Alternate: solid on odd rows, blank on even
    TYA
    AND #$01
    BEQ :+
    LDA #$03         ; Solid segment
    JMP :++
:   LDA #$00         ; Blank
:   STA $2007

    INY
    CPY #29          ; Stop before bottom border
    BNE :---
    RTS
```

## Quick Reference

### Pong Court Layout
```
Row 0:    ████████████████████████████████
Row 1-28: █              ┊              █
Row 29:   ████████████████████████████████

          Col 0         16            31
```

### Subroutine Benefits
- JSR (Jump to Subroutine): Save return address, jump
- RTS (Return from Subroutine): Return to caller
- Clean code organization, reusable functions

---

**Version:** 1.0
**Created:** 2025-10-24
