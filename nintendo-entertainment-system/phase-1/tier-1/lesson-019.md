# Lesson 019: Screen Boundary Collision

**Arc:** Ball Physics
**Position:** Lesson 3 of 4 in arc
**Type:** Standard
**Estimated Completion:** 90 lines of assembly

## Learning Objectives
- Detect ball collision with screen edges
- Implement bounce physics (velocity reversal)
- Handle top/bottom boundaries
- Handle left/right boundaries (scoring zones)

## Prerequisites
- Ball movement (L18)
- Boundary detection (L16)
- Signed arithmetic

## Key Concepts
**Bounce Physics** - Reverse velocity component when hitting wall
**Boundary Constants** - Top=8, Bottom=232, Left=0, Right=255
**Scoring Zones** - Left/right edges trigger scoring, not bounce
**Velocity Negation** - Flip sign bit: EOR #$FF, CLC, ADC #$01

## Code Pattern
```asm6502
.segment "ZEROPAGE"
ball_x: .res 1
ball_y: .res 1
ball_vx: .res 1
ball_vy: .res 1

; Boundary constants
BALL_TOP = 8            ; Top boundary (below status area)
BALL_BOTTOM = 232       ; Bottom boundary
BALL_LEFT = 0           ; Left edge (scoring zone)
BALL_RIGHT = 255        ; Right edge (scoring zone)

.segment "CODE"
; Check and handle ball collisions
CheckBallCollision:
    ; Check top boundary
    LDA ball_y
    CMP #BALL_TOP
    BCS :+                  ; Branch if Y >= TOP

    ; Hit top wall - bounce down
    LDA #BALL_TOP
    STA ball_y              ; Snap to boundary
    JSR NegateBallVY        ; Reverse Y velocity

:   ; Check bottom boundary
    LDA ball_y
    CMP #BALL_BOTTOM
    BCC :+                  ; Branch if Y < BOTTOM

    ; Hit bottom wall - bounce up
    LDA #BALL_BOTTOM
    STA ball_y              ; Snap to boundary
    JSR NegateBallVY        ; Reverse Y velocity

:   ; Check left boundary (Player 2 scores)
    LDA ball_x
    CMP #BALL_LEFT
    BNE :+                  ; Branch if not at left edge

    ; Ball went off left edge
    JSR ScorePlayer2        ; Award point to player 2
    JSR ResetBall           ; Return ball to center
    RTS

:   ; Check right boundary (Player 1 scores)
    LDA ball_x
    CMP #BALL_RIGHT
    BNE :+                  ; Branch if not at right edge

    ; Ball went off right edge
    JSR ScorePlayer1        ; Award point to player 1
    JSR ResetBall           ; Return ball to center

:   RTS

; Negate ball Y velocity (bounce)
NegateBallVY:
    LDA ball_vy
    EOR #$FF                ; Flip all bits
    CLC
    ADC #$01                ; Add 1 (two's complement negation)
    STA ball_vy
    RTS

; Negate ball X velocity (bounce)
NegateBallVX:
    LDA ball_vx
    EOR #$FF
    CLC
    ADC #$01
    STA ball_vx
    RTS

; Reset ball to center (after scoring)
ResetBall:
    LDA #128
    STA ball_x
    LDA #120
    STA ball_y
    ; Velocity stays same direction
    RTS

; Placeholder scoring routines (implemented in L25-28)
ScorePlayer1:
    ; TODO: Increment P1 score
    RTS

ScorePlayer2:
    ; TODO: Increment P2 score
    RTS

; Main game loop integration
MainLoop:
    ; ... wait for VBlank ...

    JSR ReadControllers
    JSR UpdatePaddles
    JSR UpdateBall
    JSR CheckBallCollision  ; Add collision detection

    JSR UpdatePaddleSprites
    JSR UpdateBallSprite

    JMP MainLoop
```

## Two's Complement Negation

How to reverse velocity:
```
Original:  $02 (+2)
EOR #$FF:  $FD (flip bits)
ADC #$01:  $FE (-2)

Original:  $FE (-2)
EOR #$FF:  $01 (flip bits)
ADC #$01:  $02 (+2)
```

## Boundary Visualization

```
     0                         255 (X)
  8  +---------------------------+
     |                           |
     |         PLAY AREA         |
     |                           |
     |      Ball bounces top     |
     |      and bottom only      |
     |                           |
     |    Left/Right = SCORE     |
232  +---------------------------+
```

## Hardware
**Collision Checks:** ~50 cycles per frame (4 boundary tests)
**Bounce Effect:** Instantaneous (happens same frame)
**Position Clamping:** Prevents ball from getting stuck in wall

## Common Pitfalls
1. **Not clamping position:** Ball can tunnel through wall if moving too fast
2. **Bouncing on left/right edges:** These should trigger scoring, not bounce
3. **Wrong comparison operators:** Use BCS/BCC correctly for unsigned compare
4. **Forgetting to negate velocity:** Position resets but ball keeps moving same direction

## Extension Ideas
- Spin effect (angle changes based on paddle contact point)
- Speed increase after each bounce
- Sound effects for wall bounce
- Visual flash on collision

## Builds Toward
**In This Arc:**
- L20: Ball physics refinement

**Next Arc:**
- L21-24: Paddle-ball collision (final piece of Pong physics)

## Quick Reference
### Boundary Test Pattern
```asm6502
; Top boundary (inclusive)
LDA position
CMP #BOUNDARY
BCS not_past_boundary    ; Branch if >= boundary

; Bottom boundary (exclusive)
LDA position
CMP #BOUNDARY
BCC not_past_boundary    ; Branch if < boundary
```

### Velocity Negation
```asm6502
LDA velocity
EOR #$FF        ; Flip bits
CLC
ADC #$01        ; Add 1
STA velocity    ; Store negated value
```

### Boundary Constants
```
Top:    8   (below 8-pixel status bar)
Bottom: 232 (8 pixels from screen bottom)
Left:   0   (edge, triggers scoring)
Right:  255 (edge, triggers scoring)
```

---

**Version:** 1.0
**Created:** 2025-10-27
