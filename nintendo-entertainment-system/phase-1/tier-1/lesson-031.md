# Lesson 031: Visual Polish

**Arc:** 2-Player Polish
**Position:** Lesson 3 of 4 in arc
**Type:** Standard
**Estimated Completion:** 100 lines of assembly

## Learning Objectives
- Add center court line to nametable
- Implement sprite flicker effect on hit
- Create visual feedback for game events
- Polish overall presentation

## Key Concepts
**Center Line** - Vertical dashed line at X=128
**Flash Effect** - Temporarily change sprite palette on collision
**Visual Feedback** - Player sees/feels every action
**Presentation** - Professional polish makes game feel complete

## Code Pattern
```asm6502
.segment "ZEROPAGE"
flash_timer: .res 1     ; Countdown for flash effect

.segment "CODE"
; Draw center court line in nametable
DrawCenterLine:
    ; Vertical line at column 16 (middle of 32)
    LDX #$00            ; Start at row 3
:   ; Set PPU address: $2000 + (X * 32) + 16
    LDA #$20
    STA $2006
    TXA
    ASL
    ASL
    ASL
    ASL
    ASL                 ; X * 32
    CLC
    ADC #16             ; + 16 (column)
    STA $2006

    ; Write line tile (every other row for dashed effect)
    TXA
    AND #$01
    BEQ @dash
    LDA #$00            ; Blank tile
    JMP @write
@dash:
    LDA #$03            ; Line tile
@write:
    STA $2007

    INX
    CPX #19             ; Rows 3-21
    BNE :-
    RTS

; Flash paddle sprite on collision
FlashPaddleOnHit:
    ; Set flash timer
    LDA #10             ; Flash for 10 frames
    STA flash_timer

    ; Change paddle to highlight palette
    ; (Will revert after timer expires)
    RTS

; Update flash effect each frame
UpdateFlashEffect:
    LDA flash_timer
    BEQ :+              ; Skip if no flash active

    DEC flash_timer     ; Count down

    ; Modify paddle sprite attributes during flash
    ; (Temporarily use different palette)

:   RTS
```

---

**Version:** 1.0
**Created:** 2025-10-27
