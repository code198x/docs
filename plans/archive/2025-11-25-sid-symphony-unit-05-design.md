# Unit 5: The Crowd — Design

**Game:** SID Symphony (C64)
**Date:** 2025-11-25
**Status:** Ready for implementation

## Goal

Add stakes. The crowd meter rises with hits and falls with misses. If it empties, the game ends. Now there's something to lose.

## Technical Decisions

### Crowd Meter Mechanics

- **Meter range:** 0-20 (fits nicely in the UI)
- **Starting value:** 10 (half full — gives room to grow or shrink)
- **On hit:** +1 (capped at 20)
- **On miss:** -2 (misses hurt more than hits help)
- **Game over:** When meter reaches 0

### Why Asymmetric (+1/-2)?

- Creates tension — you can't coast on early success
- Encourages consistent play over lucky streaks
- Makes recovery feel meaningful
- Standard rhythm game design pattern

### Variables

```asm
CROWD_MAX       = 20
CROWD_START     = 10

crowd_meter:    !byte CROWD_START
```

### Updating the Meter

On hit:
```asm
update_crowd_hit:
            lda crowd_meter
            cmp #CROWD_MAX
            bcs crowd_max           ; Already at max
            inc crowd_meter
crowd_max:
            rts
```

On miss:
```asm
update_crowd_miss:
            lda crowd_meter
            sec
            sbc #$02                ; Subtract 2
            bcs store_crowd
            lda #$00                ; Floor at 0
store_crowd:
            sta crowd_meter
            bne crowd_ok
            ; Crowd empty - game over!
            jmp trigger_game_over
crowd_ok:
            rts
```

### Visual Display

The UI already has:
```
CROWD [          ]
```

Fill the brackets based on meter level:

```asm
; Draw crowd meter (20 characters wide)
draw_crowd:
            ldx #$00
            ldy crowd_meter
draw_crowd_loop:
            cpx #CROWD_MAX
            bcs draw_crowd_done
            ; Draw filled or empty based on Y
            cpy #$00
            beq draw_empty
            lda #$a0                ; Filled block
            dey
            jmp draw_char
draw_empty:
            lda #$20                ; Space
draw_char:
            sta SCREEN + ROW_CROWD * 40 + COL_CROWD,x
            inx
            jmp draw_crowd_loop
draw_crowd_done:
            rts
```

### Colour Feedback

The meter colour could reflect danger level:

```asm
            lda crowd_meter
            cmp #$05                ; Below 5?
            bcc crowd_danger
            cmp #$0f                ; Below 15?
            bcc crowd_normal
            ; Above 15 - crowd is happy
            lda #COL_GREEN
            jmp set_crowd_colour
crowd_normal:
            lda #COL_CYAN
            jmp set_crowd_colour
crowd_danger:
            lda #COL_RED
set_crowd_colour:
            ; Set colour RAM for crowd meter area
```

### Game Over Trigger

```asm
trigger_game_over:
            ; Stop the game
            ; In Unit 8, this transitions to GAMEOVER state
            ; For now, just freeze
            lda #$00
            sta game_running        ; Flag to stop main loop
            jsr draw_game_over      ; Show message
            rts
```

For Unit 5, game over can be simple — stop updating, show "GAME OVER" text. Unit 8 adds proper state machine.

## Screen Layout

The crowd meter sits at the bottom:

```
Row 22: CROWD [##########          ]
```

20 character slots for the meter (columns 7-26).

## Integration Points

### In check_hit (after scoring):

```asm
            jsr add_score
            jsr update_crowd_hit
            ; ... rest of hit handling
```

### In move_notes (on miss):

```asm
            jsr update_crowd_miss
            ; Check if game over was triggered
            lda game_running
            beq game_over_exit
            ; ... rest of miss handling
```

## Progression Within Unit

1. Add crowd_meter variable
2. Draw initial meter on screen
3. Implement draw_crowd routine
4. Increment meter on hit
5. Decrement meter on miss
6. Add game over detection
7. Add simple game over display
8. Add colour feedback for danger level
9. Test and balance

## What We're NOT Doing

- Animated crowd (sprites waving) — too complex
- Sound effects for crowd state — focus on visuals
- Crowd "reactions" text — keep it minimal
- Gradual regeneration over time — too forgiving
- Multiple lives — crowd meter IS the lives

## Balancing Notes

The +1/-2 ratio may need tuning:
- If too hard: try +1/-1 or +2/-2
- If too easy: try +1/-3

Starting at 10/20 gives ~5 misses before game over. With ~40 notes per minute and good play, this should feel fair but tense.

## The "Aha" Moment

You can fail. The game can end. That bar at the bottom isn't decoration — it's your lifeline. Suddenly every note matters. This is where the toy becomes a game.
