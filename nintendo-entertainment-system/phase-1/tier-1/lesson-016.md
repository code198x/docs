# Lesson 016: Boundaries

**Arc:** Controller Input
**Position:** Lesson 4 of 4 in arc
**Type:** Synthesis (Complete Player Control)
**Estimated Completion:** 70 lines of assembly

## Learning Objectives

- Implement robust boundary checking
- Prevent paddle from leaving screen
- Handle edge cases cleanly
- Create polished movement system

## Key Concepts Introduced

### Edge Case Handling
Check boundaries AFTER movement but BEFORE rendering. Clamp to valid range. Prevents visual glitches.

### Boundary Constants
Define min/max values clearly. Top/bottom account for sprite size (16 pixels). Consistent boundaries improve gameplay feel.

### Order of Operations
1. Read input
2. Update position
3. Apply boundaries (clamp)
4. Update sprite
Clean separation of concerns.

### Movement Polish
Smooth acceleration vs instant speed. For Pong, instant is fine (simple controls). More complex games might use acceleration.

## Code Pattern

```asm
.segment "ZEROPAGE"
buttons:    .res 1
paddle_y:   .res 1

; Boundary constants
PADDLE_TOP = 8
PADDLE_BOTTOM = 216  ; 240 - 16 - 8 (screen - sprite - border)
PADDLE_SPEED = 3

.segment "CODE"
Reset:
    ; [Init code from previous lessons]
    LDA #120
    STA paddle_y

MainLoop:
:   LDA nmi_ready
    BEQ :-
    LDA #$00
    STA nmi_ready

    JSR ReadController
    JSR UpdatePaddle
    JSR UpdateOAM
    JMP MainLoop

UpdatePaddle:
    ; Save original position
    LDA paddle_y
    PHA

    ; Handle Up button
    LDA buttons
    AND #%00001000
    BEQ :+
    LDA paddle_y
    SEC
    SBC #PADDLE_SPEED
    STA paddle_y

    ; Handle Down button
:   LDA buttons
    AND #%00000100
    BEQ :+
    LDA paddle_y
    CLC
    ADC #PADDLE_SPEED
    STA paddle_y

    ; Check if both pressed (conflict)
:   LDA buttons
    AND #%00001100   ; Both Up and Down
    CMP #%00001100
    BNE :+
    ; Restore original position if both pressed
    PLA
    STA paddle_y
    JMP :++

    ; Apply boundaries
:   PLA              ; Discard saved position

    ; Top boundary
    LDA paddle_y
    CMP #PADDLE_TOP
    BCS :+
    LDA #PADDLE_TOP
    STA paddle_y

    ; Bottom boundary
:   LDA paddle_y
    CMP #PADDLE_BOTTOM
    BCC :+
    LDA #PADDLE_BOTTOM
    STA paddle_y

:   RTS

UpdateOAM:
    ; Sprite 0: Paddle (8×16 sprite)
    LDA paddle_y
    STA $0200        ; Y position

    LDA #$00
    STA $0201        ; Tile index

    LDA #%00000001   ; Palette 1
    STA $0202        ; Attributes

    LDA #16
    STA $0203        ; X position (left side)

    RTS

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

; [NMI handler with DMA from lesson 011]
```

## Boundary Testing Checklist

- [ ] Paddle stops at top (can't go higher)
- [ ] Paddle stops at bottom (can't go lower)
- [ ] Paddle doesn't flicker at edges
- [ ] Up+Down simultaneously = no movement
- [ ] Smooth movement at all positions
- [ ] No wrap-around (0 to 255)

## Quick Reference

### Why Save/Restore Position?
Handles Up+Down conflict cleanly. If both pressed, restore original position (no movement). Alternative: prioritize one direction.

### Alternative Conflict Handling
```asm
; Ignore Down if Up pressed
LDA buttons
AND #%00001000   ; Check Up first
BNE handle_up
; Only check Down if Up not pressed
LDA buttons
AND #%00000100
BEQ no_movement
```

---

**Version:** 1.0
**Created:** 2025-10-24
