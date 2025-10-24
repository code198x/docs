# Lesson 012: Moving Paddle

**Arc:** Sprite Fundamentals
**Position:** Lesson 4 of 4 in arc
**Type:** Synthesis (Animated Sprite)
**Estimated Completion:** 50 lines of assembly

## Learning Objectives

- Animate sprite position each frame
- Implement automatic movement
- Create bouncing behaviour
- Master velocity and position updates

## Key Concepts Introduced

### Velocity Variables
Separate variable for speed and direction. Add velocity to position each frame. Positive = down/right, negative = up/left.

### Signed Arithmetic
6502 uses two's complement. $FF = -1, $FE = -2, etc. ADC works for both positive and negative values with carry flag.

### Boundary Detection
Check if position reaches edge. Reverse velocity on collision. Creates bouncing effect.

### Frame-Rate Independence
Update on every VBlank = consistent 60fps motion. Velocity controls speed (pixels per frame).

## Code Pattern

```asm
.segment "ZEROPAGE"
paddle_y:    .res 1
paddle_vy:   .res 1   ; Velocity (signed)

.segment "CODE"
Reset:
    ; [Init from previous lessons]

    ; Initialize position and velocity
    LDA #100
    STA paddle_y
    LDA #2           ; Move down at 2 pixels/frame
    STA paddle_vy

MainLoop:
:   LDA nmi_ready
    BEQ :-
    LDA #$00
    STA nmi_ready

    ; Update paddle position
    LDA paddle_y
    CLC
    ADC paddle_vy    ; Add velocity (signed)
    STA paddle_y

    ; Check top boundary (Y < 8)
    CMP #8
    BCS :+           ; Branch if Y >= 8
    LDA #8
    STA paddle_y
    LDA paddle_vy
    EOR #$FF         ; Negate velocity
    CLC
    ADC #$01
    STA paddle_vy

    ; Check bottom boundary (Y > 200)
:   LDA paddle_y
    CMP #200
    BCC :+           ; Branch if Y < 200
    LDA #200
    STA paddle_y
    LDA paddle_vy
    EOR #$FF         ; Negate velocity
    CLC
    ADC #$01
    STA paddle_vy

    ; Update OAM
:   JSR UpdateOAM

    JMP MainLoop

UpdateOAM:
    LDA paddle_y
    STA $0200
    LDA #$00
    STA $0201
    LDA #%00000000
    STA $0202
    LDA #16
    STA $0203
    RTS

; [NMI handler from lesson 011]
```

## Quick Reference

### Two's Complement Negation
```asm
; Negate value in A
EOR #$FF         ; Flip all bits
CLC
ADC #$01         ; Add 1
```

### Signed Values
- $00-$7F: Positive (0 to 127)
- $80-$FF: Negative (-128 to -1)
- $FF = -1, $FE = -2, $80 = -128

### Boundary Check Pattern
```asm
CMP #limit
BCC within       ; Branch if less than
; Handle exceeded
within:
```

---

**Version:** 1.0
**Created:** 2025-10-24
