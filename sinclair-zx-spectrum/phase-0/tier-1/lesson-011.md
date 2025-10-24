# Lesson 011: Music Box

**Arc:** Sound & Timing
**Position:** Lesson 2 of 2 in arc
**Type:** Synthesis (Complete Demo)
**Estimated Completion:** 40 lines of code

## Learning Objectives

- Create musical sequences with BEEP
- Use DATA for note sequences
- Understand musical timing
- Combine PAUSE with BEEP for rhythm

## Key Concepts Introduced

### Musical Notes
Store note pitches and durations in DATA statements. Create melodies by reading and playing them in sequence.

### PAUSE Command
PAUSE n stops program for n/50 seconds (PAL timing). PAUSE 50 = 1 second. PAUSE 0 waits for keypress.

### Rhythm and Timing
Combine BEEP duration with PAUSE for precise musical timing.

## Code Pattern

```basic
10 RESTORE
20 READ pitch,dur
30 IF pitch=999 THEN STOP
40 BEEP dur,pitch
50 PAUSE dur*50
60 GO TO 20
100 DATA 0,0.5,2,0.5,4,0.5
110 DATA 5,1,999,0
```

## Quick Reference

- `PAUSE n` - Wait n/50 seconds
- `PAUSE 0` - Wait for keypress
- Musical timing: Combine BEEP and PAUSE
- DATA for note sequences

**Note Values:**
- C=0, D=2, E=4, F=5, G=7, A=9, B=11

---

**Version:** 1.0
**Created:** 2025-10-24
