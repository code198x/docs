# Unit 6: Three Voices — Design

**Game:** SID Symphony (C64)
**Date:** 2025-11-25
**Status:** Ready for implementation

## Goal

Expand to all three tracks with all three SID voices. Three keys, three lanes, three sounds. The full rhythm game experience.

## Technical Decisions

### Three Tracks, Three Keys

| Track | Row | Key | SID Voice |
|-------|-----|-----|-----------|
| 1 (top) | 8 | X | Voice 1 |
| 2 (middle) | 12 | C | Voice 2 |
| 3 (bottom) | 16 | V | Voice 3 |

### Why X, C, V?

- Adjacent keys on the bottom row
- Left hand position natural for three fingers
- Same row avoids awkward hand positions
- Common pattern in rhythm games

### Key Detection

Extend existing keyboard reading to check three keys:

```asm
KEY_X           = (some matrix position)
KEY_C           = (some matrix position)
KEY_V           = (some matrix position)

key_x_was:      !byte $00
key_c_was:      !byte $00
key_v_was:      !byte $00
```

Each key needs its own transition detection (was-pressed tracking).

### Note Data Extension

Notes now need a track assignment:

```asm
note_x:         !byte $ff, $ff, $ff, $ff, $ff, $ff  ; 6 slots now
note_track:     !byte $00, $00, $00, $00, $00, $00  ; Track 0, 1, or 2
```

Why 6 slots? With three tracks spawning, we could have 2 per track visible at once.

### Track-Specific Hit Detection

When X is pressed, only check notes on track 0.
When C is pressed, only check notes on track 1.
When V is pressed, only check notes on track 2.

```asm
; A = track to check (0, 1, or 2)
check_hit_on_track:
            sta check_track
            ldx #$00
check_hit_loop:
            lda note_x,x
            cmp #NOTE_INACTIVE
            beq check_next
            lda note_track,x
            cmp check_track
            bne check_next          ; Wrong track
            lda note_x,x
            cmp #HIT_ZONE_X
            bcs check_next          ; Not in hit zone
            ; HIT on correct track!
            jsr erase_note
            lda #NOTE_INACTIVE
            sta note_x,x
            ; ... scoring, flash, etc.
            rts
check_next:
            inx
            cpx #MAX_NOTES
            bne check_hit_loop
            rts                     ; No hit

check_track: !byte $00
```

### Three SID Voices

Each track triggers a different SID voice with a different pitch:

```asm
; Voice base addresses
SID_V1          = $d400
SID_V2          = $d407
SID_V3          = $d40e

; Pitches (different notes for each track)
PITCH_TRACK1_LO = $17         ; ~262 Hz (middle C)
PITCH_TRACK1_HI = $11
PITCH_TRACK2_LO = $8f         ; ~330 Hz (E)
PITCH_TRACK2_HI = $15
PITCH_TRACK3_LO = $a1         ; ~392 Hz (G)
PITCH_TRACK3_HI = $19
```

Forms a C major chord when all three play together.

### Playing the Right Voice

```asm
; A = track (0, 1, 2)
play_track_voice:
            cmp #$00
            beq play_voice1
            cmp #$01
            beq play_voice2
            jmp play_voice3

play_voice1:
            lda #PITCH_TRACK1_LO
            sta SID_V1
            lda #PITCH_TRACK1_HI
            sta SID_V1 + 1
            lda #$11                ; Gate on
            sta SID_V1 + 4
            rts

; ... similar for voice 2 and 3
```

### Track Row Mapping

```asm
ROW_TRACK1      = 8
ROW_TRACK2      = 12
ROW_TRACK3      = 16

track_rows:
            !byte ROW_TRACK1, ROW_TRACK2, ROW_TRACK3
```

Drawing uses `note_track,x` to look up the row.

### Spawning on Specific Tracks

For now, round-robin or random:

```asm
spawn_track:    !byte $00       ; Next track to spawn on

spawn_note:
            ; Find free slot
            ; ...
            ; Assign position and track
            lda #NOTE_START_X
            sta note_x,x
            lda spawn_track
            sta note_track,x
            ; Rotate to next track
            inc spawn_track
            lda spawn_track
            cmp #$03
            bcc spawn_done
            lda #$00
            sta spawn_track
spawn_done:
            jsr draw_note
            rts
```

In Unit 7, song data will specify tracks explicitly.

### Staggered Spawns

With three tracks, spawn interval could be shorter:

```asm
SPAWN_INTERVAL  = 40            ; Every 40 frames (was 60)
```

Or keep at 60 but let song data control timing in Unit 7.

## Main Loop Changes

Check all three keys each frame:

```asm
            ; Check X key (track 1)
            jsr check_x_key
            ; ... transition detection ...
            beq no_x_hit
            lda #$00
            jsr check_hit_on_track
            beq no_x_hit            ; No hit, but still play
            ; Hit!
no_x_hit:
            jsr maybe_play_voice1   ; Play if key down

            ; Check C key (track 2)
            jsr check_c_key
            ; ... similar ...

            ; Check V key (track 3)
            jsr check_v_key
            ; ... similar ...
```

## Progression Within Unit

1. Add track data to note arrays
2. Update draw_note/erase_note for variable rows
3. Implement track-specific hit detection
4. Add C and V key reading
5. Add transition detection for all three keys
6. Configure three SID voices
7. Play correct voice for each track
8. Update spawning for three tracks
9. Adjust spawn timing
10. Test and balance

## What We're NOT Doing

- Different note graphics per track (keep it simple)
- Track-specific colours (maybe future)
- Difficulty ramping within a song (Unit 7+)
- Track-specific scoring (all tracks equal)

## Visual Design

Each track could have a subtle colour difference:

| Track | Note Colour | Hit Zone |
|-------|-------------|----------|
| 1 | Light blue | Cyan |
| 2 | White | Cyan |
| 3 | Light blue | Cyan |

Or keep all white for simplicity. Colour can be polish.

## The "Aha" Moment

It's a real rhythm game now. Three tracks, three keys, three sounds. Your fingers are moving, the SID is singing harmonies, and when you hit all three notes at once — that chord rings out. This is what we were building toward.
