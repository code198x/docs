# Lesson 021: Paddle-Ball Collision Detection

**Arc:** Paddle-Ball Collision
**Position:** Lesson 1 of 4 in arc
**Type:** Standard
**Estimated Completion:** 100 lines of assembly

## Learning Objectives
- Detect collision between ball and paddle sprites
- Implement bounding box collision (AABB)
- Test overlap on both X and Y axes
- Handle collision response (bounce)

## Prerequisites
- Ball physics (L17-20)
- Paddle movement (L13-16)
- Sprite positioning

## Key Concepts
**AABB Collision** - Axis-Aligned Bounding Box: rectangle overlap test
**Two-Stage Test** - Check X overlap AND Y overlap
**Sprite Sizes** - Ball 8×8, Paddle 8×16 (different hitboxes)
**Bounce Timing** - Collision detected before position update prevents tunneling

## Code Pattern
```asm6502
.segment "ZEROPAGE"
; Ball entity
ball_x: .res 1
ball_y: .res 1
ball_vx: .res 1
ball_vy: .res 1

; Paddle entities (from L11-12)
paddle1_x: .res 1
paddle1_y: .res 1
paddle2_x: .res 1
paddle2_y: .res 1

; Collision sizes
BALL_WIDTH = 8
BALL_HEIGHT = 8
PADDLE_WIDTH = 8
PADDLE_HEIGHT = 16

.segment "CODE"
; Check if ball collides with paddle 1
CheckBallPaddle1:
    ; X axis overlap test
    ; Ball left edge < Paddle right edge AND
    ; Ball right edge > Paddle left edge

    LDA ball_x
    CLC
    ADC #BALL_WIDTH         ; Ball right edge
    CMP paddle1_x           ; Compare to paddle left
    BCC @no_collision       ; Branch if ball_right < paddle_left

    LDA paddle1_x
    CLC
    ADC #PADDLE_WIDTH       ; Paddle right edge
    CMP ball_x              ; Compare to ball left
    BCC @no_collision       ; Branch if paddle_right < ball_left

    ; X axes overlap - now check Y
    LDA ball_y
    CLC
    ADC #BALL_HEIGHT        ; Ball bottom edge
    CMP paddle1_y           ; Compare to paddle top
    BCC @no_collision       ; Branch if ball_bottom < paddle_top

    LDA paddle1_y
    CLC
    ADC #PADDLE_HEIGHT      ; Paddle bottom edge
    CMP ball_y              ; Compare to ball top
    BCC @no_collision       ; Branch if paddle_bottom < ball_top

    ; Both axes overlap = COLLISION!
    JSR HandlePaddle1Hit
    LDA #$01                ; Return collision flag
    RTS

@no_collision:
    LDA #$00                ; No collision
    RTS

; Check if ball collides with paddle 2
CheckBallPaddle2:
    ; Same logic as paddle 1, but use paddle2_x/y
    LDA ball_x
    CLC
    ADC #BALL_WIDTH
    CMP paddle2_x
    BCC @no_collision

    LDA paddle2_x
    CLC
    ADC #PADDLE_WIDTH
    CMP ball_x
    BCC @no_collision

    LDA ball_y
    CLC
    ADC #BALL_HEIGHT
    CMP paddle2_y
    BCC @no_collision

    LDA paddle2_y
    CLC
    ADC #PADDLE_HEIGHT
    CMP ball_y
    BCC @no_collision

    JSR HandlePaddle2Hit
    LDA #$01
    RTS

@no_collision:
    LDA #$00
    RTS

; Handle paddle 1 collision
HandlePaddle1Hit:
    ; Reverse ball X velocity (bounce away from paddle)
    JSR NegateBallVX

    ; Snap ball outside paddle (prevent sticking)
    LDA paddle1_x
    CLC
    ADC #PADDLE_WIDTH       ; Paddle right edge
    STA ball_x              ; Place ball just right of paddle

    RTS

; Handle paddle 2 collision
HandlePaddle2Hit:
    ; Reverse ball X velocity
    JSR NegateBallVX

    ; Snap ball outside paddle (left side)
    LDA paddle2_x
    SEC
    SBC #BALL_WIDTH         ; Place ball just left of paddle
    STA ball_x

    RTS

; Main game loop integration
MainLoop:
    ; ... wait for VBlank ...

    JSR ReadControllers
    JSR UpdatePaddles

    ; Check collisions BEFORE updating ball position
    JSR CheckBallPaddle1
    JSR CheckBallPaddle2

    JSR UpdateBall
    JSR CheckBallCollision  ; Screen boundaries

    JSR UpdatePaddleSprites
    JSR UpdateBallSprite

    JMP MainLoop
```

## AABB Collision Visualization

```
Paddle 1 (8×16):          Ball (8×8):
  X─┬───────┬─X+8           X─┬─────┬─X+8
   │       │                 │     │
  Y┼───────┼                Y┼─────┼
   │       │                 └─────┘─Y+8
   │       │
   │       │
   └───────┘─Y+16

Collision if:
  ball_x + 8 > paddle_x  AND
  paddle_x + 8 > ball_x  AND
  ball_y + 8 > paddle_y  AND
  paddle_y + 16 > ball_y
```

## Hardware
**Collision Tests:** ~60 cycles per paddle (120 total per frame)
**Accuracy:** Pixel-perfect (no gaps or false positives)
**Performance Impact:** Negligible (<1% of frame budget)

## Common Pitfalls
1. **Testing collision after movement:** Ball can tunnel through paddle
2. **Wrong comparison operators:** Use BCC (unsigned less-than) correctly
3. **Not snapping ball position:** Ball gets stuck overlapping paddle
4. **Forgetting ADC for edges:** Must calculate right/bottom edges

## Extension Ideas
- Hit sound effect (BEEP or APU pulse)
- Paddle hit animation (flash sprite)
- Different bounce behavior per paddle zone
- Particle effect on collision

## Builds Toward
**In This Arc:**
- L22: Angle control (hit position affects bounce)
- L23: Paddle movement influence on ball
- L24: Polish and edge cases

## Quick Reference
### AABB Test Pattern
```asm6502
; X overlap:
LDA obj1_x
CLC
ADC obj1_width      ; Right edge
CMP obj2_x          ; Compare to obj2 left
BCC no_overlap

LDA obj2_x
CLC
ADC obj2_width      ; Right edge
CMP obj1_x          ; Compare to obj1 left
BCC no_overlap

; Y overlap (same pattern):
; ...

; If reach here = collision!
```

### Collision Response Order
1. Detect collision (this lesson)
2. Reverse velocity (bounce direction)
3. Snap position (prevent overlap)
4. Optional: Modify velocity (next lessons)

---

**Version:** 1.0
**Created:** 2025-10-27
