# Lesson 025: Melody Sequencer

**Arc:** Sound & Music Mastery
**Position:** Lesson 2 of 5 in arc
**Type:** Standard
**Estimated Completion:** 40 lines of code

## Learning Objectives

- Create data-driven music sequencer
- Store melodies in DATA statements
- Implement note timing and rhythm
- Build reusable music playback engine

## Prerequisites

**From Previous Lessons:**
- Three voice control (L24)
- DATA statements (L6)
- Timer concepts (L15)

**BASIC Knowledge:**
- DATA/READ for sequences
- Arrays for note storage
- Timing loops

## Key Concepts Introduced

### Music Data Format
Store notes as frequency values in DATA. Include duration data for rhythm. Simple format: DATA note,duration,note,duration...

### Sequencer Loop
Read notes from data, play each note for specified duration, advance to next. Loop or stop at end.

### Rest/Silence
Duration with frequency=0 creates rests (silence between notes). Essential for rhythm.

### Tempo Control
Duration values control speed. Multiply all durations by tempo factor for faster/slower playback.

## Code Pattern

```basic
10 DIM N(32),D(32):REM Notes and durations
20 REM Load melody
30 FOR I=1 TO 16
40 READ N(I),D(I)
50 NEXT I
60 POKE 54296,15
70 REM Play sequence
80 FOR I=1 TO 16
90 IF N(I)=0 THEN 150:REM Rest
100 REM Play note on voice 1
110 POKE 54272,N(I) AND 255:REM Low byte
120 POKE 54273,N(I)/256:REM High byte
130 POKE 54277,0:POKE 54278,240
140 POKE 54276,17
150 REM Hold for duration
160 FOR T=1 TO D(I)*50:NEXT T
170 POKE 54276,16:REM Stop
180 NEXT I
1000 REM Mary Had Little Lamb
1010 DATA 10548,4,9398,4,8372,4,9398,4
1020 DATA 10548,4,10548,4,10548,8,0,2
1030 DATA 9398,4,9398,4,9398,8,0,2
1040 DATA 10548,4,12544,4,12544,8,0,2
```

## Hardware Interaction

**Chips Involved:**
- **SID** - Voice 1 for melody (or all 3 voices)

**Memory Addresses:**
- Voice 1 registers: 54272-54278

## Common Pitfalls

1. **16-bit frequency handling:** Need low byte AND high byte POKEs
2. **No rests:** Continuous notes sound wrong, need silence
3. **Wrong duration units:** Too fast = blur, too slow = dragging
4. **Array size:** Must DIM enough space for full song
5. **Not stopping note:** Must gate off between notes or they blend

## Extension Ideas

- Add multiple melodies (different DATA sections)
- Play on different voices (harmony)
- Add waveform variation per note
- Add vibrato (slight frequency wobble)
- Add note repeats (loop sections)
- Create music editor (record keypresses to DATA)

## Builds Toward

**In This Tier:**
- L26: Non-blocking playback (music during gameplay)
- L28: Full 3-voice music composition

## Quick Reference

**Note Data Format:**
```basic
1000 DATA frequency,duration,frequency,duration
1010 DATA 8372,4,9398,4,0,2  :REM C,D,rest
```

**16-Bit Frequency POKE:**
```basic
10 F=8372  :REM Frequency value
20 POKE 54272,F AND 255  :REM Low byte
30 POKE 54273,INT(F/256)  :REM High byte
```

**Duration Units:**
- 1-2: Very short (staccato)
- 4: Quarter note
- 8: Half note
- 16: Whole note
- Multiply by tempo factor (×50 in loops)

**Sequencer Pattern:**
```basic
10 FOR I=1 TO NOTES
20 [set frequency]
30 [gate on]
40 [wait duration]
50 [gate off]
60 NEXT I
```

**Rest Handling:**
```basic
10 IF NOTE=0 THEN SKIP_POKE:GOTO WAIT
20 [normal note playback]
```

**Common Melodies to Try:**
- Mary Had a Little Lamb
- Twinkle Twinkle Little Star
- Happy Birthday
- Jingle Bells
