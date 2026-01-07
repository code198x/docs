# Unit 2: Notes in Motion — Design

**Game:** SID Symphony (C64)
**Date:** 2025-11-25
**Status:** Ready for implementation

## Goal

Notes spawn on the right, scroll left across Track 2, and despawn at the left edge. No hit detection yet — that's Unit 3.

## Technical Decisions

### Frame Timing

Wait for raster line 0 using `$D012` (busy wait). This ensures exactly one update per frame (50 Hz PAL / 60 Hz NTSC).

**Why this matters (must explain in lesson):**
- The C64 draws the screen 50/60 times per second
- `$D012` tells you which raster line is currently being drawn
- Without sync, movement looks jerky and inconsistent
- Waiting for line 0 guarantees exactly one update per frame
- This is the foundation of all smooth C64 animation

### Note Storage

Start simple, then expand:

1. **First:** Single note (one X position variable)
2. **Then:** Fixed array of 4 slots

Inactive notes marked with `$FF`. This teaches object lifecycle and array-based game objects.

### Visual Representation

- Character: Solid block `$A0` (same as hit zone)
- Colour: White (`$01`) to stand out against cyan track
- Restores dash character when note leaves each position

### Movement

- Speed: 1 column every 2 frames (`NOTE_SPEED = 2`)
- Frame counter decrements each frame
- When counter hits zero: move note, reset counter
- ~1.3 seconds to cross the screen

### Spawning

- Interval: Every 60 frames (`SPAWN_INTERVAL = 60`)
- Position: Column 39 (right edge of track)
- Only spawn if free slot exists (array version)

### Despawning

- Trigger: Note reaches column 0
- Action: Mark slot as inactive (`$FF`)
- Track repair: Restore dash character at vacated position

## Progression Within Unit

1. Single note, manual spawn at startup (prove movement works)
2. Auto-spawn single note on timer
3. Expand to 4-slot array
4. Multiple notes scrolling simultaneously

## What We're NOT Doing

- Hit detection (Unit 3)
- Multiple tracks (Unit 4)
- Different pitches/voices (Unit 4-5)
- Song data (Unit 6)

## The "Aha" Moment

The screen comes alive. Something is happening. It looks like the game it's going to become.

## Constants

```asm
NOTE_SPEED      = 2         ; Frames between movements
SPAWN_INTERVAL  = 60        ; Frames between spawns
MAX_NOTES       = 4         ; Maximum simultaneous notes
NOTE_CHAR       = $a0       ; Solid block
NOTE_COLOUR     = $01       ; White
TRACK_CHAR      = $2d       ; Dash (restore after note passes)
NOTE_INACTIVE   = $ff       ; Marker for empty slot
NOTE_START_X    = 39        ; Spawn position (right edge)
```

## Data Structures

```asm
; Single note version
note_x:         !byte $ff   ; X position ($ff = inactive)

; Array version (added mid-unit)
note_x_array:   !byte $ff, $ff, $ff, $ff   ; 4 note X positions
```

## New Routines Needed

- `wait_frame` — Busy wait for raster line 0
- `update_notes` — Move all active notes left, despawn at edge
- `spawn_note` — Place new note at column 39 if slot available
- `draw_note` — Write note character to screen at position
- `erase_note` — Restore track character at position
