# Unit 3: Hit or Miss — Design

**Game:** SID Symphony (C64)
**Date:** 2025-11-25
**Status:** Ready for implementation

## Goal

Detect when the player hits or misses notes. Provide feedback for both. No scoring yet — that's Unit 4.

## Technical Decisions

### Hit Detection

- A "hit" = X pressed while any note is in columns 0-3 (the hit zone)
- Check on key-down *transition* only (not every frame X is held)
- Find first note in hit zone, remove it immediately
- With current spawn rate (60 frames), rarely multiple notes in zone

### Hit Feedback

- Note disappears immediately (mark slot as `$FF`)
- SID plays the note (already wired from Unit 1's `play_note`)
- Optional: brief green flash on hit zone

### Miss Detection

- A "miss" = note despawns (reaches column 0 / wraps to `$FF`) without being hit
- Detected in `move_notes` when a note exits the left edge

### Miss Feedback

- Hit zone flashes red briefly
- No audio (future enhancement: play a "bum note" — wrong frequency)

### Empty Keypresses

- X still plays SID even with no note in hit zone
- Maintains "musical toy" feel from Unit 1
- No penalty for now (Unit 4 may add consequences)

## New Constants

```asm
COL_RED         = $02           ; For miss feedback
COL_GREEN       = $05           ; For hit feedback (already defined)
FLASH_DURATION  = 4             ; Frames to show flash colour
```

## New Variables

```asm
hit_flash:      !byte $00       ; Frames remaining for hit flash
miss_flash:     !byte $00       ; Frames remaining for miss flash
key_was_pressed: !byte $00      ; To detect key-down transition
```

## New Routines

### check_hit
Called when X transitions from not-pressed to pressed:
```asm
check_hit:
            ldx #$00
check_hit_loop:
            lda note_x,x
            cmp #NOTE_INACTIVE
            beq check_hit_next
            cmp #HIT_ZONE_X         ; In hit zone? (< 4)
            bcs check_hit_next      ; No, check next
            ; Found a note in hit zone - HIT!
            jsr erase_note          ; Remove from screen
            lda #NOTE_INACTIVE
            sta note_x,x            ; Mark inactive
            lda #FLASH_DURATION
            sta hit_flash           ; Trigger green flash
            rts                     ; Done (first match only)
check_hit_next:
            inx
            cpx #MAX_NOTES
            bne check_hit_loop
            rts                     ; No note in zone
```

### detect_miss
Called in move_notes when a note despawns:
```asm
; In move_notes, when note wraps to $FF:
            lda #FLASH_DURATION
            sta miss_flash          ; Trigger red flash
```

### update_flash
Called each frame to manage flash colours:
```asm
update_flash:
            ; Handle hit flash (green)
            lda hit_flash
            beq no_hit_flash
            dec hit_flash
            ; Set hit zone to green
            jsr flash_zone_green
            rts
no_hit_flash:
            ; Handle miss flash (red)
            lda miss_flash
            beq no_miss_flash
            dec miss_flash
            ; Set hit zone to red
            jsr flash_zone_red
            rts
no_miss_flash:
            ; Restore normal hit zone colour (cyan)
            jsr restore_zone_colour
            rts
```

## Main Loop Changes

```asm
main_loop:
            jsr wait_frame

            ; Check for key-down transition
            jsr check_x_key         ; A = 1 if pressed
            ldx key_was_pressed
            sta key_was_pressed     ; Update for next frame
            cpx #$00
            bne not_key_down        ; Was already pressed
            cmp #$01
            bne not_key_down        ; Not pressed now either
            ; Key just went down - check for hit
            jsr check_hit
            jsr play_note           ; Always play on keypress
            jmp after_key_check

not_key_down:
            ; Handle key release (same as before)
            ; ...

after_key_check:
            ; Spawn/move notes (same as Unit 2)
            ; ...

            ; Update flash effects
            jsr update_flash

            jmp main_loop
```

## Progression Within Unit

1. Detect key-down transition (not just "is held")
2. Check if any note is in hit zone on key-down
3. Remove hit notes, add hit flash
4. Detect missed notes in move_notes
5. Add miss flash
6. Polish timing and feel

## What We're NOT Doing

- Scoring (Unit 4)
- Multiple tracks (Unit 4+)
- Different pitches per note (Unit 5-6)
- Graded hits (Perfect/Good/Late) — future enhancement
- Audio feedback for misses — future enhancement ("bum note")

## The "Aha" Moment

You can succeed and fail. There are stakes. It's a game now — not just a toy.
