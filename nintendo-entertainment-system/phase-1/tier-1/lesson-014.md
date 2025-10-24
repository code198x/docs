# Lesson 014: Button Detection

**Arc:** Controller Input
**Position:** Lesson 2 of 4 in arc
**Type:** Standard
**Estimated Completion:** 40 lines of assembly

## Learning Objectives

- Isolate D-pad directions (Up/Down)
- Implement multiple button tests
- Use bit masking efficiently
- Handle simultaneous button presses

## Key Concepts Introduced

### Bit Masking
Use AND to isolate specific bits. AND #%00001000 tests only bit 3 (Up). Result is zero (not pressed) or non-zero (pressed).

### Multiple Button Detection
Test each button independently. Can detect multiple buttons pressed simultaneously. Important for games with button combinations.

### D-Pad Priority
Handle conflicting inputs (Up+Down, Left+Right). Choose priority or ignore conflicting directions. Pong only needs Up/Down.

### Button State Logic
Z flag set after AND = button not pressed. Z flag clear = button pressed. BEQ branches if Z set, BNE branches if Z clear.

## Code Pattern

```asm
.segment "ZEROPAGE"
buttons:   .res 1
paddle_y:  .res 1

.segment "CODE"
MainLoop:
:   LDA nmi_ready
    BEQ :-
    LDA #$00
    STA nmi_ready

    JSR ReadController

    ; Test Up button (bit 3)
    LDA buttons
    AND #%00001000
    BEQ :+           ; Not pressed, skip
    ; Up pressed - move paddle up
    LDA paddle_y
    SEC
    SBC #2           ; Subtract 2 (move up)
    STA paddle_y

    ; Test Down button (bit 2)
:   LDA buttons
    AND #%00000100
    BEQ :+           ; Not pressed, skip
    ; Down pressed - move paddle down
    LDA paddle_y
    CLC
    ADC #2           ; Add 2 (move down)
    STA paddle_y

:   JSR UpdateOAM
    JMP MainLoop

ReadController:
    LDA #$01
    STA $4016
    LDA #$00
    STA $4016

    LDX #$08
:   LDA $4016
    LSR
    ROL buttons
    DEX
    BNE :-
    RTS
```

## Bit Mask Reference

Test individual buttons:
```asm
; A button (bit 7)
AND #%10000000

; B button (bit 6)
AND #%01000000

; Select (bit 5)
AND #%00100000

; Start (bit 4)
AND #%00010000

; Up (bit 3)
AND #%00001000

; Down (bit 2)
AND #%00000100

; Left (bit 1)
AND #%00000010

; Right (bit 0)
AND #%00000001
```

## Quick Reference

### Testing Multiple Buttons
```asm
; Test A OR B pressed
LDA buttons
AND #%11000000   ; Mask both A and B
BEQ not_pressed  ; Neither pressed
; At least one pressed
```

### Handling Conflicts
```asm
; Check if Up and Down both pressed
LDA buttons
AND #%00001100   ; Mask Up and Down
CMP #%00001100   ; Both set?
BEQ ignore       ; Ignore conflicting input
```

---

**Version:** 1.0
**Created:** 2025-10-24
