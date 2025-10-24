# Lesson 010: Sound FX

**Arc:** Sound & Timing
**Position:** Lesson 1 of 2 in arc
**Type:** Standard
**Estimated Completion:** 15 lines of code

## Learning Objectives

- Use BEEP command for sound
- Understand pitch (frequency) and duration
- Create simple sound effects
- Experience 1-bit audio limitations

## Key Concepts Introduced

### BEEP Command
BEEP duration,pitch creates sound. Duration in seconds, pitch in semitones from middle C (0).

### Frequency vs Pitch
Pitch measured in musical semitones. -12 is an octave lower, +12 is octave higher. Range: approximately -60 to +60.

### Sound Effects
Short beeps create game sound effects: explosions, pickups, jumps.

## Code Pattern

```basic
10 REM Laser sound
20 FOR n=20 TO -20 STEP -2
30 BEEP 0.01,n
40 NEXT n
50 REM Explosion
60 FOR n=1 TO 10
70 BEEP 0.05,-40+RND*20
80 NEXT n
```

## Quick Reference

- `BEEP duration,pitch` - Play sound
- Duration: seconds (0.01 = short beep)
- Pitch: semitones (0=middle C, +12=octave up)
- Only one sound at a time (single channel)

---

**Version:** 1.0
**Created:** 2025-10-24
