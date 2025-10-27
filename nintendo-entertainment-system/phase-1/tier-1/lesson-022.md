# Lesson 022: Angle Control from Hit Position

**Arc:** Paddle-Ball Collision
**Position:** Lesson 2 of 4 in arc
**Type:** Standard
**Estimated Completion:** 110 lines of assembly

## Learning Objectives
- Calculate where ball hits paddle (top/center/bottom)
- Modify bounce angle based on hit position
- Implement steeper/shallower bounce angles
- Create predictable ball control for player

## Prerequisites
- Paddle-ball collision (L21)
- Signed arithmetic
- Ball physics (L20)

## Key Concepts
**Hit Position** - Ball Y relative to paddle center determines angle
**Angle Zones** - Top third (steep up), middle third (medium), bottom third (steep down)
**Velocity Modification** - Change VY based on zone, keep VX magnitude
**Player Skill** - Hitting with paddle edge = more control over ball direction

## Code Pattern
```asm6502
.segment "CODE"
; Calculate hit position and modify bounce angle
HandlePaddle1HitWithAngle:
    ; Calculate paddle center Y
    LDA paddle1_y
    CLC
    ADC #8                  ; Center = Y + half height (16/2=8)
    STA temp                ; temp = paddle center Y

    ; Calculate ball center Y
    LDA ball_y
    CLC
    ADC #4                  ; Ball center = Y + half height (8/2=4)
    STA temp+1              ; temp+1 = ball center Y

    ; Calculate hit offset (ball_center - paddle_center)
    ; Result: negative = hit top, 0 = center, positive = bottom
    LDA temp+1
    SEC
    SBC temp
    STA temp+2              ; temp+2 = hit offset (-8 to +8)

    ; Reverse ball X velocity (bounce)
    JSR NegateBallVX

    ; Snap ball outside paddle
    LDA paddle1_x
    CLC
    ADC #PADDLE_WIDTH
    STA ball_x

    ; Modify Y velocity based on hit position
    LDA temp+2              ; Load hit offset

    ; Top zone (offset < -3)
    CMP #$FD                ; -3 in signed
    BCS @middle             ; Branch if >= -3

    ; Hit top third - steep upward angle
    LDA #$FD                ; -3 (steep up)
    STA ball_vy
    RTS

@middle:
    ; Middle zone (offset -3 to +2)
    LDA temp+2
    CMP #$03
    BCS @bottom             ; Branch if >= 3

    ; Hit middle third - medium angle
    LDA temp+2
    CMP #$80                ; Negative?
    BCS @middle_up

    ; Slightly down
    LDA #$01
    STA ball_vy
    RTS

@middle_up:
    ; Slightly up
    LDA #$FF                ; -1
    STA ball_vy
    RTS

@bottom:
    ; Bottom zone (offset >= 3)
    ; Hit bottom third - steep downward angle
    LDA #$03                ; +3 (steep down)
    STA ball_vy
    RTS

; Same for paddle 2
HandlePaddle2HitWithAngle:
    ; Calculate paddle center
    LDA paddle2_y
    CLC
    ADC #8
    STA temp

    ; Calculate ball center
    LDA ball_y
    CLC
    ADC #4
    STA temp+1

    ; Calculate offset
    LDA temp+1
    SEC
    SBC temp
    STA temp+2

    ; Reverse X velocity
    JSR NegateBallVX

    ; Snap position
    LDA paddle2_x
    SEC
    SBC #BALL_WIDTH
    STA ball_x

    ; Apply same angle logic as paddle 1
    LDA temp+2
    CMP #$FD
    BCS @middle
    LDA #$FD
    STA ball_vy
    RTS

@middle:
    LDA temp+2
    CMP #$03
    BCS @bottom
    LDA temp+2
    CMP #$80
    BCS @middle_up
    LDA #$01
    STA ball_vy
    RTS

@middle_up:
    LDA #$FF
    STA ball_vy
    RTS

@bottom:
    LDA #$03
    STA ball_vy
    RTS
```

## Hit Zones Visualization

```
Paddle (8×16):          Hit Zones:

  ┌───────┐
  │ Top   │ ← Hit here: VY = -3 (steep up)
  │  -3   │
Y ├───────┤
  │Center │ ← Hit here: VY = -1/+1 (medium)
  │ -1/+1 │
  ├───────┤
  │Bottom │ ← Hit here: VY = +3 (steep down)
  │  +3   │
  └───────┘

Offset calculation:
  offset = ball_center_y - paddle_center_y
  Range: -8 to +8 (ball can be slightly off paddle)
```

## Angle Tables (Alternative Implementation)

For more control, use lookup table:
```asm6502
; Angle table indexed by hit offset (0-15, offset+8)
AngleTable:
.byte $FC, $FD, $FD, $FE, $FE  ; Top (steep up)
.byte $FF, $FF, $00, $00       ; Center (medium)
.byte $01, $01, $02, $02       ; Bottom (medium-steep)
.byte $03, $03, $03            ; Bottom (steep down)

; Usage:
LDA temp+2              ; hit offset (-8 to +7)
CLC
ADC #8                  ; Convert to 0-15
TAX
LDA AngleTable,X        ; Look up angle
STA ball_vy
```

## Hardware
**Calculation Cost:** ~40 cycles per paddle hit
**Angle Range:** VY = -3 to +3 (covers full range)
**Player Control:** Skilled players can aim ball precisely

## Common Pitfalls
1. **Integer overflow in offset calculation:** Ball far from paddle causes wrong angle
2. **Not clamping angle values:** VY outside safe range breaks physics
3. **Unsigned comparison on signed offset:** Use correct branch instructions
4. **Same angle for both paddles:** Should feel symmetric

## Extension Ideas
- More granular zones (5-7 zones instead of 3)
- Curved ball (continuous angle calculation)
- Perfect center hit = straight horizontal (VY=0)
- Audio pitch varies with hit position

## Builds Toward
**In This Arc:**
- L23: Paddle movement influence (moving paddle = faster ball)
- L24: Polish and special cases

**Later:**
- L25-28: Scoring and game states
- L29-32: 2-player polish

## Quick Reference
### Hit Position Zones
```
Top third:    offset < -3 → VY = -3 (steep up)
Middle third: -3 ≤ offset < 3 → VY = -1/+1 (medium)
Bottom third: offset ≥ 3 → VY = +3 (steep down)
```

### Center Calculation
```asm6502
; Paddle center Y
LDA paddle_y
CLC
ADC #8          ; Half of paddle height (16/2)

; Ball center Y
LDA ball_y
CLC
ADC #4          ; Half of ball height (8/2)
```

### Offset to Angle Mapping
```
Offset  | Angle (VY)
--------|------------
< -3    | -3 (steep up)
-3 to 0 | -1 (up)
0 to 3  | +1 (down)
> 3     | +3 (steep down)
```

---

**Version:** 1.0
**Created:** 2025-10-27
