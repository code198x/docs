# Lesson 029: 2-Player Controller Support

**Arc:** 2-Player Polish
**Position:** Lesson 1 of 4 in arc
**Type:** Standard
**Estimated Completion:** 80 lines of assembly

## Learning Objectives
- Read controller 2 ($4017)
- Assign paddle 2 to controller 2
- Create independent player controls
- Test 2-player gameplay

## Key Concepts
**Controller 2** - $4017 register, same protocol as $4016
**Simultaneous Input** - Both players act same frame
**Button Mapping** - Each player controls their paddle

## Code Pattern
```asm6502
.segment "ZEROPAGE"
buttons1: .res 1        ; Controller 1
buttons2: .res 1        ; Controller 2

.segment "CODE"
ReadControllers:
    ; Strobe both controllers
    LDA #$01
    STA $4016
    LDA #$00
    STA $4016

    ; Read controller 1
    LDX #$08
:   LDA $4016
    LSR
    ROL buttons1
    DEX
    BNE :-

    ; Read controller 2
    LDX #$08
:   LDA $4017
    LSR
    ROL buttons2
    DEX
    BNE :-

    RTS

UpdatePaddle1:
    ; Use buttons1 for paddle 1
    LDA buttons1
    AND #BUTTON_UP
    BEQ :+
    ; Move paddle 1 up
:   ; ... movement code ...
    RTS

UpdatePaddle2:
    ; Use buttons2 for paddle 2
    LDA buttons2
    AND #BUTTON_UP
    BEQ :+
    ; Move paddle 2 up
:   ; ... movement code ...
    RTS
```

---

**Version:** 1.0
**Created:** 2025-10-27
