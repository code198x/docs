# Lesson 015: Paddle Control

**Arc:** Controller Input
**Position:** Lesson 3 of 4 in arc
**Type:** Standard
**Estimated Completion:** 55 lines of assembly

## Learning Objectives

- Link controller input to paddle movement
- Remove automatic velocity
- Create responsive controls
- Master direct position control

## Key Concepts Introduced

### Direct Position Control
Controller input directly modifies paddle_y. No velocity variable needed. Immediate response to player input.

### Control Smoothness
Movement speed set by how much we add/subtract per frame. 2-3 pixels per frame feels responsive without being too fast.

### Removing Auto-Movement
Previous automatic bouncing removed. Player has full control. Better for gameplay (Pong requires precise positioning).

### Input Polling Rate
Controller read every frame (60 times per second). Fast enough for responsive gameplay. Some games use button state changes (pressed this frame vs last frame).

## Code Pattern

```asm
.segment "ZEROPAGE"
buttons:   .res 1
paddle_y:  .res 1

.segment "CODE"
Reset:
    ; [Init code]
    LDA #100
    STA paddle_y
    ; No velocity initialization needed

MainLoop:
:   LDA nmi_ready
    BEQ :-
    LDA #$00
    STA nmi_ready

    JSR ReadController

    ; Up button - move paddle up
    LDA buttons
    AND #%00001000
    BEQ :+
    LDA paddle_y
    SEC
    SBC #3           ; Speed: 3 pixels per frame
    STA paddle_y

    ; Down button - move paddle down
:   LDA buttons
    AND #%00000100
    BEQ :+
    LDA paddle_y
    CLC
    ADC #3
    STA paddle_y

    ; Apply boundaries before updating sprite
:   JSR ClampPaddle
    JSR UpdateOAM
    JMP MainLoop

ClampPaddle:
    ; Top boundary (Y < 8)
    LDA paddle_y
    CMP #8
    BCS :+
    LDA #8
    STA paddle_y

    ; Bottom boundary (Y > 200)
:   LDA paddle_y
    CMP #200
    BCC :+
    LDA #200
    STA paddle_y

:   RTS

UpdateOAM:
    LDA paddle_y
    STA $0200        ; Y position
    LDA #$00
    STA $0201        ; Tile
    LDA #%00000000
    STA $0202        ; Attributes
    LDA #16
    STA $0203        ; X position
    RTS
```

## Control Feel Reference

Movement speeds:
- 1 pixel/frame: Very slow (240 frames edge-to-edge)
- 2 pixels/frame: Moderate (120 frames)
- 3 pixels/frame: Fast (80 frames) - **Good for Pong**
- 4 pixels/frame: Very fast (60 frames)
- 5+ pixels/frame: Too fast (hard to control)

## Quick Reference

### Boundary Values for Pong
```
Top edge:    Y = 8   (below border)
Bottom edge: Y = 200 (above border, accounting for 16px paddle)
Left edge:   X = 16  (player 1)
Right edge:  X = 224 (player 2)
```

### Clamping Pattern
```asm
; Clamp to minimum
CMP #min
BCS :+           ; Branch if >= min
LDA #min         ; Set to min
STA value

; Clamp to maximum
: CMP #max
BCC :+           ; Branch if < max
LDA #max         ; Set to max
STA value
```

---

**Version:** 1.0
**Created:** 2025-10-24
