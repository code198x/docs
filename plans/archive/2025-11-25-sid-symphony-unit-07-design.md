# Unit 7: Song Data — Design

**Game:** SID Symphony (C64)
**Date:** 2025-11-25
**Status:** Ready for implementation

## Goal

Transform from predictable demo to playable rhythm game with authored content. Notes spawn from song data, not a fixed timer.

## Technical Decisions

### Song Data Format

Delta timing — each note stores frames since the previous note:

```asm
; Song data: pairs of (delta_frames, track_number)
; delta_frames = frames to wait after previous note
; track = 1, 2, or 3 (0 = end of song)

song_data:
    !byte 60, 2     ; After 60 frames, note on track 2
    !byte 30, 2     ; After 30 more frames, note on track 2
    !byte 30, 1     ; After 30 more frames, note on track 1
    !byte 30, 3     ; After 30 more frames, note on track 3
    !byte 60, 2     ; After 60 frames, note on track 2
    ; ... etc
    !byte 0, 0      ; End marker
```

### Why Delta Timing?

- Absolute timestamps overflow a byte quickly (255 frames = ~5 seconds)
- Delta timing allows songs of any length
- Each note just says "wait N frames after the previous note"
- Simpler to author and edit

### New Variables

```asm
song_ptr:        !word song_data  ; Pointer to current position in song
song_ptr_lo      = song_ptr
song_ptr_hi      = song_ptr + 1
next_note_timer: !byte 0          ; Frames until next note spawns
song_playing:    !byte 0          ; 1 = song active, 0 = ended
```

### Reading Song Data

```asm
check_song:
            lda song_playing
            beq song_done           ; Song already ended

            dec next_note_timer
            bne song_done           ; Not time yet

            ; Time for next note - read from song data
            ldy #$00
            lda (song_ptr),y        ; Get delta frames
            beq end_of_song         ; 0 = song ended
            sta next_note_timer     ; Set timer for NEXT note

            iny
            lda (song_ptr),y        ; Get track number
            jsr spawn_note_on_track ; NEW: spawn on specific track

            ; Advance pointer by 2 bytes
            clc
            lda song_ptr_lo
            adc #$02
            sta song_ptr_lo
            bcc song_done
            inc song_ptr_hi

song_done:
            rts

end_of_song:
            lda #$00
            sta song_playing
            rts
```

### Spawn on Specific Track

```asm
spawn_note_on_track:
            ; A = track number (1, 2, or 3)
            tax
            dex                     ; Convert to 0-indexed
            ; Store track in note_track,slot when spawning
            ; ... rest of spawn logic
```

### Track-Specific Data

Extend the note arrays to include track:

```asm
note_x:     !byte $ff, $ff, $ff, $ff
note_track: !byte $00, $00, $00, $00   ; Which track (0, 1, 2)
```

## Changes to Existing Code

### Remove Fixed Spawn Timer

The old `spawn_timer` and `SPAWN_INTERVAL` are removed. Song data drives spawning entirely.

### Update Draw/Erase

`draw_note` and `erase_note` must use `note_track,x` to determine which row to draw on, not a hardcoded row.

### Three Separate Hit Zones

Each track has its own hit zone. When X/C/V is pressed, only check notes on that track.

## Progression Within Unit

1. Create simple test song (8-16 notes)
2. Implement song pointer and delta timer
3. Update spawn to use song data
4. Update spawn to include track assignment
5. Update draw/erase for variable tracks
6. Update hit detection for track-specific keys
7. Detect end-of-song condition
8. Create a longer, playable song

## What We're NOT Doing

- Multiple songs (Unit 8 could add song selection)
- Song editor (future enhancement)
- Loading songs from disk (future enhancement)
- BPM/tempo system (delta frames is simpler)
- Music theory (songs are just patterns)

## Sample Test Song

```asm
; Simple test pattern - alternating tracks
test_song:
    !byte 60, 2     ; Track 2
    !byte 30, 2     ; Track 2
    !byte 30, 1     ; Track 1
    !byte 30, 3     ; Track 3
    !byte 30, 2     ; Track 2
    !byte 30, 1     ; Track 1
    !byte 30, 3     ; Track 3
    !byte 30, 2     ; Track 2
    !byte 60, 1     ; Track 1 (longer gap)
    !byte 30, 2     ; Track 2
    !byte 30, 3     ; Track 3
    !byte 30, 2     ; Track 2
    !byte 0, 0      ; End
```

## The "Aha" Moment

The same game engine can play completely different songs just by changing the data. The code doesn't care what song it's playing. This is data-driven design — a fundamental game development concept.
