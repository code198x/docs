# Lesson 013: Controller Basics

**Arc:** Controller Input
**Position:** Lesson 1 of 4 in arc
**Type:** Standard
**Estimated Completion:** 45 lines of assembly

## Learning Objectives

- Read controller registers ($4016/$4017)
- Understand controller strobe sequence
- Poll 8 button states
- Implement basic input routine

## Key Concepts Introduced

### Controller Registers
$4016 = Controller 1, $4017 = Controller 2. Each read returns one button state in bit 0. Must strobe first, then read 8 times.

### Strobe Sequence
Write $01 then $00 to $4016. Latches current button states. Subsequent reads return buttons in order: A, B, Select, Start, Up, Down, Left, Right.

### Button State Format
Bit 0 of read value = button pressed (1) or not pressed (0). Other bits are open bus (undefined). Use AND #$01 to isolate.

### Serial Reading Pattern
Controller is shift register. Each read shifts next button into bit 0. Must read all 8 buttons in correct order.

## Code Pattern

```asm
.segment "ZEROPAGE"
buttons: .res 1      ; Current button states

.segment "CODE"
ReadController:
    ; Strobe controller
    LDA #$01
    STA $4016
    LDA #$00
    STA $4016

    ; Read 8 buttons into buttons variable
    ; Bit 7: A, Bit 6: B, Bit 5: Select, Bit 4: Start
    ; Bit 3: Up, Bit 2: Down, Bit 1: Left, Bit 0: Right

    LDX #$08         ; 8 buttons to read
:   LDA $4016        ; Read one button
    LSR              ; Shift bit 0 into carry
    ROL buttons      ; Rotate carry into buttons
    DEX
    BNE :-

    RTS

MainLoop:
:   LDA nmi_ready
    BEQ :-
    LDA #$00
    STA nmi_ready

    JSR ReadController

    ; Test if A button pressed
    LDA buttons
    AND #%10000000   ; Bit 7 = A button
    BEQ :+           ; Branch if not pressed
    
    ; A button is pressed
    ; (Do something here)

:   JSR UpdateOAM
    JMP MainLoop
```

## Button Bit Positions

After ReadController:
```
Bit 7: A button
Bit 6: B button
Bit 5: Select
Bit 4: Start
Bit 3: Up
Bit 2: Down
Bit 1: Left
Bit 0: Right
```

## Quick Reference

### Read Sequence
1. Write $01 to $4016 (strobe on)
2. Write $00 to $4016 (strobe off, latch buttons)
3. Read $4016 eight times (A, B, Select, Start, Up, Down, Left, Right)
4. Bit 0 of each read = button state

### Testing Buttons
```asm
LDA buttons
AND #%10000000   ; Test bit 7 (A button)
BEQ not_pressed  ; Branch if zero (not pressed)
; Button is pressed
```

### Why LSR then ROL?
LSR shifts bit 0 into carry flag. ROL shifts carry into buttons. Builds byte with all 8 button states.

---

**Version:** 1.0
**Created:** 2025-10-24
