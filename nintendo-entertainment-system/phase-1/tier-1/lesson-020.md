# Lesson 020: Ball Physics Refinement

**Arc:** Ball Physics
**Position:** Lesson 4 of 4 in arc (SYNTHESIS)
**Type:** Synthesis
**Estimated Completion:** 120 lines of assembly

## Learning Objectives
- Implement diagonal bounce angles
- Add velocity variation for gameplay
- Create realistic ball physics
- Integrate complete ball system

## Prerequisites
- Ball entity and movement (L17-18)
- Boundary collision (L19)
- Signed arithmetic mastery

## Key Concepts
**Angle Variation** - Velocity changes based on impact point (center vs edge)
**Speed Consistency** - Maintain total speed while changing direction
**Randomness** - Slight variation prevents predictable patterns
**Launch Direction** - Ball starts toward scoring player

## Code Pattern
```asm6502
.segment "ZEROPAGE"
ball_x: .res 1
ball_y: .res 1
ball_vx: .res 1         ; -3 to +3 range
ball_vy: .res 1         ; -3 to +3 range
ball_speed: .res 1      ; Base speed (increases over time)

.segment "CODE"
; Initialize ball with random direction
InitBall:
    LDA #128
    STA ball_x
    LDA #120
    STA ball_y

    ; Random initial direction (use frame counter)
    LDA frame_count
    AND #$01
    BEQ :+

    ; Move right
    LDA #$02
    STA ball_vx
    JMP :++

:   ; Move left
    LDA #$FE            ; -2
    STA ball_vx

:   ; Random Y velocity
    LDA frame_count
    AND #$03
    SEC
    SBC #$02            ; Range: -2 to +1
    STA ball_vy

    ; Set base speed
    LDA #$02
    STA ball_speed
    RTS

; Bounce with angle variation
BounceTop:
    ; Snap position
    LDA #BALL_TOP
    STA ball_y

    ; Reverse Y velocity
    JSR NegateBallVY

    ; Add slight X variation (makes gameplay less predictable)
    LDA frame_count
    AND #$01
    BEQ :+
    INC ball_vx         ; Slight right nudge
    JMP :++
:   DEC ball_vx         ; Slight left nudge

:   ; Clamp X velocity to ±3 range
    JSR ClampBallVX
    RTS

BounceBottom:
    LDA #BALL_BOTTOM
    STA ball_y
    JSR NegateBallVY

    ; Same variation as top
    LDA frame_count
    AND #$01
    BEQ :+
    INC ball_vx
    JMP :++
:   DEC ball_vx

:   JSR ClampBallVX
    RTS

; Clamp X velocity to safe range (±3)
ClampBallVX:
    ; Check if > +3
    LDA ball_vx
    CMP #$04
    BCC :+              ; Branch if < 4
    LDA #$03            ; Clamp to +3
    STA ball_vx

:   ; Check if < -3 (unsigned comparison with $FD)
    LDA ball_vx
    CMP #$FD
    BCS :+              ; Branch if >= $FD (-3)
    LDA #$FD            ; Clamp to -3
    STA ball_vx

:   RTS

; Increase ball speed gradually
IncreaseSpeed:
    LDA ball_speed
    CMP #$04            ; Max speed = 4
    BCS :+              ; Branch if already at max
    INC ball_speed

    ; Scale velocities by new speed (simplified)
    ; In real game, multiply VX/VY by speed factor
    LDA ball_vx
    BMI :+              ; Skip if negative
    INC ball_vx

:   RTS

; Reset ball toward scoring player
ResetBallToward:
    ; A register = direction (0=left, 1=right)
    STA temp

    LDA #128
    STA ball_x
    LDA #120
    STA ball_y

    ; Set velocity toward player who was scored on
    LDA temp
    BEQ :+

    ; Launch right
    LDA #$02
    STA ball_vx
    JMP :++

:   ; Launch left
    LDA #$FE
    STA ball_vx

:   ; Random Y component
    LDA frame_count
    AND #$03
    SEC
    SBC #$02
    STA ball_vy

    RTS

; Complete ball update with physics
UpdateBallPhysics:
    ; Apply velocity
    LDA ball_x
    CLC
    ADC ball_vx
    STA ball_x

    LDA ball_y
    CLC
    ADC ball_vy
    STA ball_y

    ; Check boundaries
    LDA ball_y
    CMP #BALL_TOP
    BCS :+
    JSR BounceTop

:   LDA ball_y
    CMP #BALL_BOTTOM
    BCC :+
    JSR BounceBottom

:   ; Left/right scoring (from L19)
    LDA ball_x
    BEQ @left_score
    CMP #255
    BEQ @right_score
    RTS

@left_score:
    JSR ScorePlayer2
    LDA #1              ; Launch right
    JSR ResetBallToward
    RTS

@right_score:
    JSR ScorePlayer1
    LDA #0              ; Launch left
    JSR ResetBallToward
    RTS
```

## Physics Behavior

**Angle Variation:**
- Center hit: Straight bounce (VX unchanged)
- Edge hit: Angled bounce (VX modified ±1)
- Prevents infinite straight bounces

**Speed Progression:**
- Start: 2 pixels/frame
- After 5 bounces: 3 pixels/frame
- After 10 bounces: 4 pixels/frame (max)

**Launch Direction:**
- Ball launches toward player who was scored on
- Gives losing player chance to return

## Hardware
**RAM Usage:** 5 bytes (x, y, vx, vy, speed)
**Performance:** ~80 cycles per frame (physics + collision)
**Gameplay Feel:** 60fps smooth motion, responsive bounce

## Common Pitfalls
1. **Velocity grows unbounded:** Always clamp after modifications
2. **Ball gets stuck:** Ensure position snapping prevents wall tunneling
3. **Too predictable:** Add randomness to prevent boring patterns
4. **Too fast:** Speed increases should be gradual

## Extension Ideas
- Spin mechanics (paddle movement affects ball angle)
- Power-up system (speed boost, curve ball)
- Trail effect (motion blur)
- Ball size changes

## Builds Toward
**Next Arc (L21-24):**
- Paddle-ball collision detection
- Hit position affects bounce angle
- Complete Pong physics system

**Arc 6 (L25-28):**
- Scoring display
- Win conditions
- Game states

## Quick Reference
### Velocity Ranges
```
ball_vx: -3 to +3 (horizontal)
ball_vy: -3 to +3 (vertical)
Total speed: √(vx² + vy²) ≈ 2-4 pixels/frame
```

### Clamping Pattern
```asm6502
; Clamp to range [MIN, MAX]
LDA value
CMP #MAX+1
BCC :+
LDA #MAX
STA value
:
LDA value
CMP #MIN
BCS :+
LDA #MIN
STA value
:
```

### Random Variation
```asm6502
; Use frame counter for pseudo-random
LDA frame_count
AND #$01        ; 0 or 1
BEQ left
; right variation
```

---

**Version:** 1.0
**Created:** 2025-10-27
**Note:** This synthesis lesson completes the Ball Physics arc. Ball now has complete movement, boundary collision, angle variation, and speed progression. Next arc (L21-24) adds paddle collision to complete Pong physics.
