# Unit 4: Keeping Score — Design

**Game:** SID Symphony (C64)
**Date:** 2025-11-25
**Status:** Ready for implementation

## Goal

Track the player's performance. Hits earn points. Streaks are tracked. The numbers on screen actually mean something now.

## Technical Decisions

### Scoring System

- **10 points per hit** — Simple, predictable
- **No multipliers yet** — Keep it straightforward for now
- **Streak counter** — How many hits in a row without a miss
- **Best streak** — Track the longest streak achieved (for end screen)

### Why No Multipliers?

Multipliers add complexity:
- When do they kick in?
- How do they scale?
- Do misses reset the multiplier or just the streak?

For Unit 4, we focus on the fundamentals. Multipliers can be a future enhancement.

### Score Storage

16-bit score (0-65535):

```asm
score_lo:       !byte $00
score_hi:       !byte $00
streak:         !byte $00       ; Current streak (0-255)
best_streak:    !byte $00       ; Best streak this game
```

### Adding Points

```asm
POINTS_PER_HIT  = 10

add_score:
            ; Add POINTS_PER_HIT to score
            clc
            lda score_lo
            adc #POINTS_PER_HIT
            sta score_lo
            bcc add_done
            inc score_hi
add_done:
            rts
```

### Streak Management

On hit:
```asm
            inc streak
            lda streak
            cmp best_streak
            bcc not_best
            sta best_streak     ; New best!
not_best:
```

On miss:
```asm
            lda #$00
            sta streak          ; Reset streak
```

### Displaying Score

The score needs to be converted to decimal digits for display. BCD (Binary Coded Decimal) or division-based conversion.

Simple approach using repeated subtraction:

```asm
; Convert 16-bit score to 6 decimal digits
; Score in score_hi/score_lo
; Output to score_digits (6 bytes, MSD first)

score_digits:   !byte 0, 0, 0, 0, 0, 0

convert_score:
            ; ... division/subtraction routine
            ; Divide by 10000, 1000, 100, 10, 1
            ; Store remainders as digits
```

For initial implementation, we can use a simpler 8-bit display if score_hi is zero.

### Displaying Streak

Streak is 0-255, needs 3 digits max. Simpler conversion:

```asm
convert_streak:
            lda streak
            ; Divide by 100
            ; Divide remainder by 10
            ; Remainder is ones digit
```

### Screen Updates

Update score/streak display each frame (or only when changed):

```asm
update_display:
            jsr convert_score
            jsr draw_score
            jsr convert_streak
            jsr draw_streak
            rts
```

## Screen Layout Changes

The Unit 1 layout already has:
```
SCORE: 000000        STREAK: 00
```

We just need to write actual values instead of zeros.

## Integration Points

### In check_hit (on successful hit):

```asm
            ; After marking note inactive...
            jsr add_score
            inc streak
            lda streak
            cmp best_streak
            bcc skip_best
            sta best_streak
skip_best:
            ; Continue with flash, etc.
```

### In move_notes (on miss):

```asm
            ; When note despawns without being hit...
            lda #$00
            sta streak
            ; Continue with miss flash
```

## Progression Within Unit

1. Add score variables
2. Implement add_score routine
3. Implement score-to-digits conversion
4. Draw score on screen
5. Add streak variables
6. Increment streak on hit
7. Reset streak on miss
8. Track best streak
9. Draw streak on screen
10. Test and tune

## What We're NOT Doing

- Score multipliers (future enhancement)
- Combo bonuses (future enhancement)
- Negative points for misses (too punishing)
- Grade system (S/A/B/C) — future enhancement
- Per-note score display (too cluttered)

## The "Aha" Moment

Your actions have consequences you can see. Every hit adds to your score. Every miss breaks your streak. The game is measuring your performance — and you care about those numbers.
