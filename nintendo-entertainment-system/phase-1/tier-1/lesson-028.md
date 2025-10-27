# Lesson 028: Game State Screens

**Arc:** Scoring System
**Position:** Lesson 4 of 4 in arc (SYNTHESIS)
**Type:** Synthesis
**Estimated Completion:** 150 lines of assembly

## Learning Objectives
- Implement title screen with nametable
- Create game over screen showing winner
- Handle state transitions (title → playing → game over)
- Integrate complete game flow

## Key Concepts
**State Machine** - Title/Playing/GameOver states
**Screen Data** - Pre-designed nametable layouts
**Controller Start** - Detect button press to begin
**Winner Display** - Show which player won

## Code Pattern
```asm6502
.segment "CODE"
TitleScreen:
    ; Display "PONG" and "PRESS START"
    JSR LoadTitleNametable
    JSR WaitForStart

    ; Transition to playing
    LDA #STATE_PLAYING
    STA game_state
    JSR InitScores
    JMP MainLoop

GameOverScreen:
    ; Display winner and final scores
    JSR LoadGameOverNametable
    JSR DisplayWinner
    JSR WaitForStart

    ; Transition back to title
    LDA #STATE_TITLE
    STA game_state
    JMP MainLoop

LoadTitleNametable:
    ; Write "PONG" at center
    ; Write "PRESS START" below
    ; ... nametable setup ...
    RTS

LoadGameOverNametable:
    ; Write "PLAYER X WINS!"
    ; Write final scores
    RTS
```

## Builds Toward
- L29-32: 2-player polish and complete game

---

**Version:** 1.0
**Created:** 2025-10-27
