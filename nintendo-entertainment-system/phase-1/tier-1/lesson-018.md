# Lesson 018: Ball Velocity and Movement

**Arc:** Ball Physics
**Position:** Lesson 2 of 4 in arc
**Type:** Standard
**Estimated Completion:** 75 lines of assembly

## Learning Objectives
- Implement ball position updates
- Apply velocity to position each frame
- Handle signed arithmetic for direction
- Create smooth 60fps ball movement

## Prerequisites
- Ball entity (L17)
- Frame-based game loop (L04)
- Signed byte arithmetic

## Key Concepts
**Velocity Application** - Add VX/VY to X/Y each frame for constant motion
**Signed Addition** - Use ADC for positive, SBC for negative velocity
**60fps Movement** - Ball moves every frame (consistent speed)
**Fixed-Point Limitation** - Whole-pixel movement only (no sub-pixel yet)

## Code Pattern
```asm6502
.segment "CODE"
; Update ball position based on velocity
UpdateBall:
    ; Update X position
    LDA ball_x
    CLC
    ADC ball_vx         ; Add signed velocity (works for both + and -)
    STA ball_x

    ; Update Y position
    LDA ball_y
    CLC
    ADC ball_vy         ; Add signed velocity
    STA ball_y

    RTS

; Main game loop
MainLoop:
    ; Wait for VBlank
:   LDA nmi_ready
    BEQ :-
    LDA #$00
    STA nmi_ready

    ; Game logic during rendering
    JSR ReadControllers
    JSR UpdatePaddles
    JSR UpdateBall      ; Add ball movement

    ; Update OAM buffer (for next VBlank)
    JSR UpdatePaddleSprites
    JSR UpdateBallSprite

    JMP MainLoop
```

## Velocity Examples

Different ball speeds:
```asm6502
; Slow horizontal
LDA #$01
STA ball_vx
LDA #$00
STA ball_vy

; Fast diagonal
LDA #$02
STA ball_vx
LDA #$02
STA ball_vy

; Moving left and up
LDA #$FE            ; -2
STA ball_vx
LDA #$FF            ; -1
STA ball_vy
```

## Signed Arithmetic Explanation

Why ADC works for signed bytes:
```
Example 1: Moving right (+2)
  ball_x = 100 ($64)
  ball_vx = +2 ($02)
  Result: $64 + $02 = $66 (102) ✓

Example 2: Moving left (-2)
  ball_x = 100 ($64)
  ball_vx = -2 ($FE)
  Result: $64 + $FE = $162
  (8-bit overflow wraps to $62 = 98) ✓
```

## Hardware
**Performance:** Ball update = ~30 cycles per frame
**Speed Range:** 1-3 pixels per frame typical (60-180 pixels/second)
**Frame Rate:** Ball moves every VBlank (60fps NTSC, 50fps PAL)

## Common Pitfalls
1. **Updating position in NMI handler:** Do physics in main loop, not during VBlank
2. **Forgetting to update OAM:** Position changes won't show without UpdateBallSprite
3. **Using SBC for negative velocity:** ADC handles signed bytes automatically
4. **Ball too fast:** Keep velocity ≤ 3 pixels/frame for playable speed

## Extension Ideas
- Variable ball speed (increase over time)
- Maximum velocity limit
- Acceleration/deceleration
- Speed boost power-ups

## Builds Toward
**In This Arc:**
- L19: Screen boundary collision
- L20: Ball physics refinement (bounce angles)

**Later This Tier:**
- L21-24: Paddle collision detection
- L25: Scoring system

## Quick Reference
### Update Pattern
```asm6502
; Every frame:
LDA position
CLC
ADC velocity    ; Signed add works for + and -
STA position
```

### Typical Velocities
```
Horizontal (X):
  $01 = +1 (right, slow)
  $02 = +2 (right, medium)
  $FE = -2 (left, medium)
  $FF = -1 (left, slow)

Vertical (Y):
  $01 = +1 (down, slow)
  $02 = +2 (down, medium)
  $FE = -2 (up, medium)
  $FF = -1 (up, slow)
```

### Speed Guidelines
```
1 pixel/frame = 60 pixels/second
2 pixels/frame = 120 pixels/second (good default)
3 pixels/frame = 180 pixels/second (fast)
4+ pixels/frame = Too fast, hard to track
```

---

**Version:** 1.0
**Created:** 2025-10-27
