# Lesson 023: Paddle Movement Influence

**Arc:** Paddle-Ball Collision
**Position:** Lesson 3 of 4 in arc
**Type:** Standard
**Estimated Completion:** 90 lines of assembly

## Learning Objectives
- Detect paddle movement direction during hit
- Transfer paddle momentum to ball
- Implement "smash" hits (moving paddle = faster ball)
- Create responsive gameplay feel

## Prerequisites
- Angle control (L22)
- Paddle velocity tracking
- Ball velocity modification

## Key Concepts
**Paddle Velocity** - Track paddle movement each frame (stationary/up/down)
**Momentum Transfer** - Moving paddle adds to ball velocity
**Speed Boost** - Smash hit increases ball speed temporarily
**Defensive vs Offensive** - Stationary = defensive return, moving = attacking shot

## Code Pattern
```asm6502
.segment "ZEROPAGE"
; Paddle state (from L11-16)
paddle1_x: .res 1
paddle1_y: .res 1
paddle1_vy: .res 1      ; Paddle velocity (0, +speed, -speed)

paddle2_x: .res 1
paddle2_y: .res 1
paddle2_vy: .res 1

; Constants
PADDLE_SPEED = 3        ; Pixels per frame when moving

.segment "CODE"
; Update paddle 1 with velocity tracking
UpdatePaddle1:
    ; Read controller
    LDA buttons1
    AND #BUTTON_UP
    BEQ :+

    ; Moving up
    LDA paddle1_y
    CMP #PADDLE_TOP
    BEQ @stationary         ; At boundary, can't move
    SEC
    SBC #PADDLE_SPEED
    STA paddle1_y
    LDA #$FD                ; -3 velocity (moving up)
    STA paddle1_vy
    RTS

:   LDA buttons1
    AND #BUTTON_DOWN
    BEQ @stationary

    ; Moving down
    LDA paddle1_y
    CMP #PADDLE_BOTTOM
    BEQ @stationary         ; At boundary, can't move
    CLC
    ADC #PADDLE_SPEED
    STA paddle1_y
    LDA #$03                ; +3 velocity (moving down)
    STA paddle1_vy
    RTS

@stationary:
    ; Not moving
    LDA #$00
    STA paddle1_vy
    RTS

; Handle paddle hit with movement influence
HandlePaddle1HitWithMomentum:
    ; Calculate angle from hit position (from L22)
    JSR CalculateHitAngle   ; Returns angle in A
    STA temp                ; temp = base angle

    ; Add paddle momentum to ball Y velocity
    LDA temp                ; Base angle
    CLC
    ADC paddle1_vy          ; Add paddle velocity
    STA ball_vy

    ; Clamp to safe range (-4 to +4)
    LDA ball_vy
    CMP #$05                ; Check if > +4
    BCC :+
    CMP #$FC                ; Check if < -4 (signed)
    BCS :+
    LDA #$04                ; Clamp to +4
    STA ball_vy

:   ; Reverse X velocity (bounce)
    JSR NegateBallVX

    ; Speed boost for moving paddle (smash hit)
    LDA paddle1_vy
    BEQ @no_boost           ; Branch if paddle stationary

    ; Paddle is moving - increase ball X speed
    LDA ball_vx
    BMI @negative_boost     ; Branch if ball moving left

@positive_boost:
    ; Ball moving right
    CMP #$04                ; Already at max?
    BCS @no_boost
    INC ball_vx             ; Increase speed
    JMP @no_boost

@negative_boost:
    ; Ball moving left
    CMP #$FC                ; Already at min?
    BCC @no_boost
    DEC ball_vx             ; Increase speed (more negative)

@no_boost:
    ; Snap ball position
    LDA paddle1_x
    CLC
    ADC #PADDLE_WIDTH
    STA ball_x
    RTS

; Calculate angle from hit position (from L22)
CalculateHitAngle:
    ; Paddle center
    LDA paddle1_y
    CLC
    ADC #8
    STA temp

    ; Ball center
    LDA ball_y
    CLC
    ADC #4
    STA temp+1

    ; Offset
    LDA temp+1
    SEC
    SBC temp

    ; Convert offset to angle (-3 to +3 range)
    CMP #$FD                ; < -3?
    BCS :+
    LDA #$FD                ; Clamp to -3
:   CMP #$04                ; > +3?
    BCC :+
    LDA #$03                ; Clamp to +3

:   RTS                     ; Return angle in A
```

## Momentum Transfer Examples

**Stationary paddle:**
```
Paddle VY: 0
Hit offset: -2 (slightly top)
Result VY: -2 (normal angle)
```

**Moving up paddle:**
```
Paddle VY: -3 (moving up)
Hit offset: -2 (slightly top)
Result VY: -2 + (-3) = -5 → clamped to -4 (steep angle)
Ball VX: increased by 1 (speed boost)
```

**Moving down paddle:**
```
Paddle VY: +3 (moving down)
Hit offset: +2 (slightly bottom)
Result VY: +2 + (+3) = +5 → clamped to +4 (steep angle)
Ball VX: increased by 1 (speed boost)
```

## Gameplay Feel

**Defensive Return (stationary):**
- Normal angle
- Normal speed
- Safe, controlled

**Offensive Smash (moving):**
- Steeper angle (harder to return)
- Increased speed (faster ball)
- Risky (timing required)

## Hardware
**Additional Cost:** ~20 cycles per collision (velocity checks)
**RAM Usage:** +2 bytes (paddle1_vy, paddle2_vy)
**Player Perception:** Noticeable skill ceiling increase

## Common Pitfalls
1. **Not clamping final velocity:** Can produce unrealistic angles/speeds
2. **Applying boost when stationary:** Check paddle_vy != 0 first
3. **Infinite speed increase:** Clamp after every modification
4. **Asymmetric feel:** Ensure both paddles behave identically

## Extension Ideas
- Visual paddle charge-up (moving paddle glows)
- Audio feedback (different sound for smash vs normal hit)
- Particle burst on smash hit
- Combo system (consecutive smashes increase effect)

## Builds Toward
**In This Arc:**
- L24: Polish and edge cases (final arc synthesis)

**Next Arc:**
- L25-28: Scoring system and game states

## Quick Reference
### Velocity Addition
```asm6502
; Base angle + paddle momentum
LDA base_angle
CLC
ADC paddle_vy
STA ball_vy

; Clamp to [-4, +4]
; (check both upper and lower bounds)
```

### Speed Boost Pattern
```asm6502
; If paddle moving, increase ball X speed
LDA paddle_vy
BEQ no_boost        ; Skip if stationary

; Increase ball_vx magnitude
LDA ball_vx
BMI negative_side
INC ball_vx         ; Positive direction
JMP done
negative_side:
DEC ball_vx         ; Negative direction (more negative)
done:
```

### Paddle Velocity Tracking
```asm6502
; Each frame:
; If moving up:   paddle_vy = -PADDLE_SPEED
; If moving down: paddle_vy = +PADDLE_SPEED
; If stationary:  paddle_vy = 0
```

---

**Version:** 1.0
**Created:** 2025-10-27
