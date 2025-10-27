# Lesson 017: Ball Entity

**Arc:** Ball Physics
**Position:** Lesson 1 of 4 in arc
**Type:** Standard
**Estimated Completion:** 60 lines of assembly

## Learning Objectives
- Create ball sprite entity
- Initialize ball position and tile
- Store ball state in RAM
- Display ball alongside paddles

## Prerequisites
- Sprite basics (L09)
- OAM structure (L10)
- Paddle sprites (L11-12)

## Key Concepts
**Entity Structure** - Position (X/Y), velocity (VX/VY), sprite data stored in RAM
**Ball Sprite** - 8×8 round sprite using tile $02 from CHR-ROM
**Sprite Slot** - Ball uses OAM slots 2-3 (paddles use 0-1, 4-5)
**Center Start Position** - Ball begins at screen center (128, 120)

## Code Pattern
```asm6502
.segment "ZEROPAGE"
ball_x: .res 1          ; Ball X position (0-255)
ball_y: .res 1          ; Ball Y position (0-239)
ball_vx: .res 1         ; Ball X velocity (-127 to +127, signed)
ball_vy: .res 1         ; Ball Y velocity (-127 to +127, signed)

.segment "CODE"
; Initialize ball at screen center
InitBall:
    LDA #128            ; Center X
    STA ball_x
    LDA #120            ; Center Y
    STA ball_y
    LDA #$01            ; Initial X velocity (moving right)
    STA ball_vx
    LDA #$FF            ; Initial Y velocity (moving up, -1 signed)
    STA ball_vy
    RTS

; Update ball sprite in OAM
UpdateBallSprite:
    ; Ball uses OAM index 8 (sprite slot 2)
    LDX #8

    ; Y position (subtract 1 for PPU quirk)
    LDA ball_y
    SEC
    SBC #1
    STA oam_buffer,X
    INX

    ; Tile ID ($02 = ball tile)
    LDA #$02
    STA oam_buffer,X
    INX

    ; Attributes (palette 1, no flip)
    LDA #%00000001
    STA oam_buffer,X
    INX

    ; X position
    LDA ball_x
    STA oam_buffer,X

    RTS

; Reset handler
Reset:
    ; ... PPU initialization ...

    JSR InitOAM
    JSR InitPaddles
    JSR InitBall        ; Add ball initialization

    ; ... enable NMI ...
```

## Ball Tile Design

In CHR-ROM (from L09):
```
; Tile $02: Ball (8×8)
.byte $00,$18,$3C,$7E,$7E,$3C,$18,$00  ; Plane 0
.byte $00,$18,$3C,$7E,$7E,$3C,$18,$00  ; Plane 1

Visual:
  . . . 3 3 . . .
  . . 3 3 3 3 . .
  . 3 3 3 3 3 3 .
  . 3 3 3 3 3 3 .
  . . 3 3 3 3 . .
  . . . 3 3 . . .
```

## Hardware
**RAM Usage:** 4 bytes (ball_x, ball_y, ball_vx, ball_vy)
**OAM Slots:** 1 sprite (8×8 mode)
**Sprite Priority:** Ball draws after paddles (higher OAM index)

## Common Pitfalls
1. **Forgetting Y-1 adjustment:** PPU displays sprites 1 scanline lower than OAM Y value
2. **Unsigned velocity:** Need signed bytes for negative movement
3. **Wrong OAM index:** Each sprite = 4 bytes, so sprite 2 starts at index 8
4. **Ball appears behind background:** Check attribute bit 5 (priority)

## Extension Ideas
- Animated ball (cycle through tiles)
- Ball trail effect (fade previous positions)
- Different ball sizes (8×16 sprite mode)
- Ball spin visualization (rotation animation)

## Builds Toward
**In This Arc:**
- L18: Ball velocity and movement
- L19: Screen boundary collision
- L20: Ball physics refinement

**Later This Tier:**
- L21-24: Paddle-ball collision
- L25-28: Scoring and game states
- L29-32: 2-player polish

## Quick Reference
### Entity RAM Layout
```
ball_x:  X position (0-255)
ball_y:  Y position (0-239)
ball_vx: X velocity (signed, -127 to +127)
ball_vy: Y velocity (signed, -127 to +127)
```

### OAM Sprite Slots (Current)
```
Slots 0-1: Paddle 1 (8×16)
Slots 2:   Ball (8×8)
Slots 3-4: Paddle 2 (8×16, when added)
Slots 5-63: Unused
```

### Signed Byte Values
```
$00 =   0
$01 =  +1
$7F = +127
$80 = -128
$FF =  -1
```

---

**Version:** 1.0
**Created:** 2025-10-27
