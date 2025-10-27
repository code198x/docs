# Lesson 025: Score Variables and Logic

**Arc:** Scoring System
**Position:** Lesson 1 of 4 in arc
**Type:** Standard
**Estimated Completion:** 70 lines of assembly

## Learning Objectives
- Create score variables in RAM
- Implement scoring logic (award points)
- Handle score limits (0-99 range)
- Track win conditions

## Prerequisites
- Ball boundary detection (L19)
- RAM variable management
- Binary arithmetic

## Key Concepts
**Binary-Coded Decimal (BCD)** - Store score as decimal digits for display
**Score Cap** - Pong typically plays to 11 or 21 points
**Point Award** - Increment score when ball passes paddle
**Win Detection** - Check if score reaches target

## Code Pattern
```asm6502
.segment "ZEROPAGE"
score_p1: .res 1        ; Player 1 score (0-99)
score_p2: .res 1        ; Player 2 score (0-99)
win_score: .res 1       ; Score needed to win (11 typical)

; Game state
game_state: .res 1
STATE_TITLE = 0
STATE_PLAYING = 1
STATE_GAMEOVER = 2

.segment "CODE"
; Initialize scores
InitScores:
    LDA #$00
    STA score_p1
    STA score_p2
    LDA #11             ; Play to 11 points (classic Pong)
    STA win_score
    LDA #STATE_TITLE
    STA game_state
    RTS

; Award point to player 1
ScorePlayer1:
    LDA score_p1
    CMP win_score       ; Already at win score?
    BCS :+              ; Skip if >= win_score

    INC score_p1        ; Increment score

    ; Check for win
    LDA score_p1
    CMP win_score
    BCC :+              ; Branch if < win_score

    ; Player 1 wins!
    LDA #STATE_GAMEOVER
    STA game_state
    LDA #1              ; Winner ID
    STA temp            ; Store for game over screen

:   RTS

; Award point to player 2
ScorePlayer2:
    LDA score_p2
    CMP win_score
    BCS :+

    INC score_p2

    ; Check for win
    LDA score_p2
    CMP win_score
    BCC :+

    ; Player 2 wins!
    LDA #STATE_GAMEOVER
    STA game_state
    LDA #2              ; Winner ID
    STA temp

:   RTS

; Check ball left boundary (from L19, now with scoring)
CheckBallLeftBoundary:
    LDA ball_x
    BNE :+              ; Branch if not at left edge

    ; Ball went off left edge - Player 2 scores
    JSR ScorePlayer2
    JSR ResetBall
    ; TODO: Play score sound

:   RTS

; Check ball right boundary
CheckBallRightBoundary:
    LDA ball_x
    CMP #255
    BNE :+              ; Branch if not at right edge

    ; Ball went off right edge - Player 1 scores
    JSR ScorePlayer1
    JSR ResetBall
    ; TODO: Play score sound

:   RTS

; Reset ball to center
ResetBall:
    LDA #128
    STA ball_x
    LDA #120
    STA ball_y

    ; Launch toward player who was scored on
    LDA score_p1
    CMP score_p2
    BCS @launch_left    ; Branch if P1 >= P2 (P2 scored last)

@launch_right:
    ; Player 1 scored last, launch toward P2
    LDA #$02
    STA ball_vx
    JMP @set_vy

@launch_left:
    ; Player 2 scored last, launch toward P1
    LDA #$FE            ; -2
    STA ball_vx

@set_vy:
    ; Random Y component
    LDA frame_count
    AND #$03
    SEC
    SBC #$02            ; Range: -2 to +1
    STA ball_vy

    RTS

; Main game loop with state machine
MainLoop:
    ; Wait for VBlank
:   LDA nmi_ready
    BEQ :-
    LDA #$00
    STA nmi_ready

    ; State machine
    LDA game_state
    CMP #STATE_TITLE
    BEQ TitleScreen
    CMP #STATE_PLAYING
    BEQ PlayingState
    CMP #STATE_GAMEOVER
    BEQ GameOverState

    JMP MainLoop

PlayingState:
    ; Game logic
    JSR ReadControllers
    JSR UpdatePaddle1
    JSR UpdatePaddle2
    JSR CheckAllCollisions
    JSR UpdateBall
    JSR CheckBallLeftBoundary
    JSR CheckBallRightBoundary

    ; Update sprites
    JSR UpdatePaddleSprites
    JSR UpdateBallSprite

    JMP MainLoop

TitleScreen:
    ; TODO: Display title, wait for start button
    ; For now, just start game
    LDA #STATE_PLAYING
    STA game_state
    JSR InitScores
    JMP MainLoop

GameOverState:
    ; TODO: Display winner, wait for restart
    ; For now, return to title
    LDA #STATE_TITLE
    STA game_state
    JMP MainLoop
```

## Score Logic Flow

```
Ball crosses left edge:
  ┌─────────────────────┐
  │ ScorePlayer2()      │
  │ - Increment score   │
  │ - Check win         │
  └──────────┬──────────┘
             │
      Win?   │   No
      ┌──────▼──────┐
      Yes            │
  ┌───▼────┐   ┌────▼─────┐
  │Set     │   │Reset     │
  │GameOver│   │Ball      │
  └────────┘   └──────────┘
```

## Typical Win Scores

```
Classic Pong: 11 points
Quick game: 7 points
Long game: 21 points
Arcade: First to 15
```

## Hardware
**RAM Usage:** 3 bytes (score_p1, score_p2, win_score)
**Performance:** Score check = ~20 cycles (negligible)
**Score Range:** 0-255 (typically limited to 0-99 for display)

## Common Pitfalls
1. **No score cap:** Players score beyond display capability
2. **Not resetting ball:** Game continues after score
3. **Wrong launch direction:** Ball always goes same direction
4. **Missing win check:** Game never ends

## Extension Ideas
- Serve system (winner serves next)
- Score advantage rule (must win by 2)
- Best of 3/5 matches
- Score-based difficulty (ball speeds up at 5 points)

## Builds Toward
**In This Arc:**
- L26: Number-to-tiles conversion
- L27: Score display in nametable
- L28: Game state screens (title, game over)

## Quick Reference
### Score Award Pattern
```asm6502
; Award point:
INC score_player

; Check win:
LDA score_player
CMP win_score
BCC still_playing   ; Branch if < win_score

; Player won
LDA #STATE_GAMEOVER
STA game_state
```

### Ball Launch Direction
```asm6502
; Launch toward player who was scored on:
LDA score_p1
CMP score_p2
BCS launch_left     ; P1 >= P2, P2 scored last

; P1 scored last:
LDA #$02            ; Launch right (toward P2)
JMP set_velocity

launch_left:
LDA #$FE            ; Launch left (toward P1)
```

### Game States
```
STATE_TITLE    = 0  (waiting for start)
STATE_PLAYING  = 1  (active game)
STATE_GAMEOVER = 2  (winner declared)
```

---

**Version:** 1.0
**Created:** 2025-10-27
