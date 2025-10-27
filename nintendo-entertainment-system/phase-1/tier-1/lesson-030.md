# Lesson 030: Sound Effects

**Arc:** 2-Player Polish
**Position:** Lesson 2 of 4 in arc
**Type:** Standard
**Estimated Completion:** 100 lines of assembly

## Learning Objectives
- Use APU pulse channels for sound effects
- Create paddle hit sound
- Create wall bounce sound
- Create scoring sound
- Trigger sounds at game events

## Key Concepts
**APU Pulse Channels** - $4000-$4007 (two square wave generators)
**Frequency Control** - Pitch via timer registers
**Envelope** - Volume decay over time
**Sound Triggers** - Play sound when event occurs

## Code Pattern
```asm6502
.segment "CODE"
; Play paddle hit sound (high blip)
PlayPaddleHitSound:
    ; Pulse 1: High pitch, short duration
    LDA #%00111111      ; Duty 00, envelope on, volume 15
    STA $4000
    LDA #$C9            ; Low frequency byte
    STA $4002
    LDA #$00            ; High frequency byte
    STA $4003
    RTS

; Play wall bounce sound (mid pitch)
PlayWallBounceSound:
    LDA #%00111010      ; Volume 10
    STA $4000
    LDA #$54            ; Mid frequency
    STA $4002
    LDA #$00
    STA $4003
    RTS

; Play score sound (descending chirp)
PlayScoreSound:
    ; Use pulse 2 for variety
    LDA #%00111111
    STA $4004
    LDA #$20            ; Low pitch
    STA $4006
    LDA #$01
    STA $4007
    RTS

; Integrate into collision handlers
HandlePaddle1Hit:
    ; ... collision logic ...
    JSR PlayPaddleHitSound
    RTS

CheckBallBoundaries:
    ; ... boundary check ...
    JSR PlayWallBounceSound
    RTS

ScorePlayer1:
    INC score_p1
    JSR PlayScoreSound
    ; ... rest of scoring ...
    RTS
```

---

**Version:** 1.0
**Created:** 2025-10-27
