# Unit 8: The Performance — Design

**Game:** SID Symphony (C64)
**Date:** 2025-11-25
**Status:** Ready for implementation

## Goal

Complete the game. Title screen, game over, victory condition, state machine. Everything comes together into something you actually want to play.

## Technical Decisions

### Game States

```asm
STATE_TITLE     = 0
STATE_PLAYING   = 1
STATE_GAMEOVER  = 2
STATE_VICTORY   = 3

game_state:     !byte STATE_TITLE
```

### State Transitions

- **TITLE → PLAYING**: Player presses SPACE
- **PLAYING → GAMEOVER**: Crowd meter empties
- **PLAYING → VICTORY**: Song ends with crowd meter > 0

### Main Loop as Dispatcher

```asm
main_loop:
            jsr wait_frame

            lda game_state
            cmp #STATE_TITLE
            beq do_title
            cmp #STATE_PLAYING
            beq do_playing
            cmp #STATE_GAMEOVER
            beq do_gameover
            jmp do_victory

do_title:
            jsr update_title
            jmp main_loop

do_playing:
            jsr update_game
            jmp main_loop

do_gameover:
            jsr update_gameover
            jmp main_loop

do_victory:
            jsr update_victory
            jmp main_loop
```

### Title Screen

```
         SID SYMPHONY

      Press SPACE to play


    X = Track 1 (top)
    C = Track 2 (middle)
    V = Track 3 (bottom)
```

Simple text screen. No animation needed. Just wait for SPACE.

```asm
update_title:
            jsr check_space_key
            beq title_done
            ; Start game
            jsr reset_game
            lda #STATE_PLAYING
            sta game_state
title_done:
            rts
```

### Game Over Screen

```
         GAME OVER

       Score: 001234
       Streak: 12

    Press SPACE to retry
```

Display final score and best streak. Wait for SPACE to restart.

### Victory Screen

```
        SONG COMPLETE!

       Score: 002345
       Streak: 18

    Press SPACE to play again
```

Similar to game over, but celebratory message.

### Reset Game

```asm
reset_game:
            ; Clear all notes
            ldx #MAX_NOTES - 1
reset_notes:
            lda #NOTE_INACTIVE
            sta note_x,x
            dex
            bpl reset_notes

            ; Reset song pointer
            lda #<song_data
            sta song_ptr_lo
            lda #>song_data
            sta song_ptr_hi
            lda #$01
            sta next_note_timer
            sta song_playing

            ; Reset score and crowd
            lda #$00
            sta score_lo
            sta score_hi
            sta streak

            lda #CROWD_START
            sta crowd_meter

            ; Redraw game screen
            jsr setup_screen
            rts
```

### Detecting Victory

In `check_song`, when end-of-song is detected:

```asm
end_of_song:
            lda #$00
            sta song_playing

            ; Check if player survived
            lda crowd_meter
            beq game_over_transition  ; Crowd empty = barely failed
            ; Still have crowd = victory!
            lda #STATE_VICTORY
            sta game_state
            jsr draw_victory_screen
            rts

game_over_transition:
            lda #STATE_GAMEOVER
            sta game_state
            jsr draw_gameover_screen
            rts
```

### Detecting Game Over (During Play)

In `update_crowd` or wherever crowd depletes:

```asm
            lda crowd_meter
            bne crowd_ok
            ; Crowd empty - game over
            lda #STATE_GAMEOVER
            sta game_state
            jsr draw_gameover_screen
crowd_ok:
            ; ... continue
```

## Screen Drawing Routines

### draw_title_screen

Clear screen, print title text, instructions.

### draw_gameover_screen

Clear game area, show "GAME OVER", score, instructions.

### draw_victory_screen

Clear game area, show "SONG COMPLETE!", score, instructions.

## Progression Within Unit

1. Add game state variable and dispatcher
2. Create title screen drawing routine
3. Implement TITLE state (wait for SPACE)
4. Create game over screen
5. Implement GAMEOVER transition from crowd depletion
6. Create victory screen
7. Implement VICTORY transition from song end
8. Add reset_game routine
9. Test full game loop: title → play → win/lose → title
10. Polish and tune

## What We're NOT Doing

- High score persistence (no disk/tape saves)
- Multiple difficulty levels (future enhancement)
- Song selection menu (could add in future)
- Animated title screen (keep it simple)
- Sound effects for menu navigation

## Future Enhancements (Post-Unit 8)

These could become bonus content or a "Unit 9":

- High score table (in-memory only)
- Multiple songs with selection
- Difficulty settings (note speed, spawn rate)
- Better SID sounds (instruments, filters)
- Visual polish (colour cycling, animations)
- Two-player mode?

## The "Aha" Moment

You've built a complete game. Not a demo, not a prototype — a game with a beginning, middle, and end. Title screen, gameplay, win and lose conditions. Everything you learned across 7 units combines into something you actually want to play.

This is what game development feels like: lots of small pieces that suddenly become a whole.
