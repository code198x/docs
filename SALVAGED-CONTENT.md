# Salvaged Content from Archived Lessons

**Date:** 2025-01-17
**Purpose:** Document reusable code examples, explanations, and media from archived lessons 5-7 for use in future curriculum-aligned lessons.

---

## From Lesson 5: Random Encounters → Future Lesson 13 (Random Events)

**Archived Location:** `_archive/lesson-005-random-encounters/`

### Code Examples to Reuse

**RND Seeding:**
```basic
X=RND(-TI)  : REM seed with current time
```

**Dice Rolling:**
```basic
10 X=RND(-TI)
20 PRINT "ROLLING A D20..."
30 R=INT(RND(1)*20)+1
40 PRINT "YOU ROLLED ";R
```

**Treasure Hunt Structure:**
```basic
10 X=RND(-TI) : SC=0
20 FOR I=1 TO 10
30   PRINT "CHEST ";I;": ";
40   GOLD=INT(RND(1)*20)+1
50   SC=SC+GOLD
60   PRINT "+";GOLD;" GOLD"
70   IF RND(1)<0.3 THEN PRINT "A TRAP! LOSE 5 GOLD!": SC=SC-5
80 NEXT I
90 PRINT "TOTAL SCORE: ";SC
```

### Explanatory Text to Reuse

- "RND(-TI) copies the current system clock into the random generator"
- "Use RND(1) for random numbers between 0 and 1"
- "INT(RND(1)*N)+1 gives you random numbers from 1 to N"
- "Random tables turn static scripts into games"

---

## From Lesson 6: Simple Animation → Future Lesson 15 (Timing)

**Archived Location:** `_archive/lesson-006-simple-animation/`

### Code Examples to Reuse

**Bouncing Star with FOR Loop Delay:**
```basic
10 X=0 : D=1
20 PRINT CHR$(147)
30 PRINT CHR$(19); : PRINT SPC(X); "*"
40 FOR T=1 TO 120: NEXT T
50 X = X + D
60 IF X=0 OR X=38 THEN D = -D
70 GOTO 20
```

**Frame-Accurate TI Timing:**
```basic
10 X=0 : D=1
20 PRINT CHR$(147)
30 PRINT CHR$(19); : PRINT SPC(X); "*"
40 T0=TI : T1=T0+2
50 IF TI<T1 THEN 50
60 X = X + D
70 IF X=0 OR X=38 THEN D = -D
80 GOTO 20
```

### Explanatory Text to Reuse

- "TI counts in jiffies (1/60th of a second on NTSC, 1/50th on PAL)"
- "FOR...NEXT loops act as crude delays but are CPU-dependent"
- "TI gives you frame-perfect delays synchronized to the video output"
- "TI$ returns time as formatted string (HHMMSS)"
- "Use TI for delays and frame timing; use TI$ for readable clocks"

### Videos to Reuse

**Location:** `_archive/lesson-006-simple-animation/`

- `example-1.mp4` (46KB) - Bouncing star with FOR loop delay
- `example-2.mp4` (43KB) - Bouncing star with TI timing

**Reuse in Lesson 15 (Timing)** - These videos perfectly demonstrate timing differences.

---

## From Lesson 7: Sound Off → Future Lessons 10-11 (First Sound / Sound Effects)

**Archived Location:** `_archive/lesson-007-sound-off/`

### Code Examples to Reuse

**Working SID Triangle Wave:**
```basic
10 POKE 54296,15      : REM maximum volume
20 POKE 54277,9       : REM attack/decay
30 POKE 54273,37      : REM low byte of frequency
40 POKE 54272,17      : REM high byte
50 POKE 54276,17      : REM triangle waveform + gate on
60 FOR T=1 TO 250: NEXT T
70 POKE 54276,16      : REM gate off
```

**SID Register Quick Reference:**
```
54296 - Master volume (0-15)
54272 - Frequency high byte
54273 - Frequency low byte
54276 - Control register (waveform + gate)
54277 - Attack/Decay
```

**Waveform Values:**
- Triangle: 16 (+ 1 for gate = 17)
- Sawtooth: 32 (+ 1 for gate = 33)
- Pulse: 64 (+ 1 for gate = 65)
- Noise: 128 (+ 1 for gate = 129)

### Explanatory Text to Reuse

- "The SID chip is legendary for a reason"
- "SID voice 1 lives at addresses $D400–$D40E (54272–54286)"
- "Frequency = two bytes; envelope = attack/decay"
- "Gate bit turns the sound on/off"
- "Attack/Decay packs two 4-bit values into one byte"
- "Frequencies use little-endian byte order"
- "Always gate off before changing waveforms to avoid clicks"

### Video to Reuse

**Location:** `_archive/lesson-007-sound-off/`

- `example-1.mp4` (114KB) - Working SID sound with audible triangle wave

**Reuse in Lesson 10 (First Sound)** - Perfect demonstration of basic SID programming.

---

## Quick Reference Table

### Experimental Section Ideas

**From Lesson 6 (Animation):**
- "Slow it down: increase delay loop to 200"
- "Speed it up: change delay to 60"
- "Move diagonally: add Y variable"
- "Change the character: swap * for @ or string"
- "Leave a trail by removing clear step"

**From Lesson 7 (Sound):**
- "Change the waveform: POKE 54276,65 (pulse) or 33 (sawtooth)"
- "Adjust attack/decay: POKE 54277,33 for slower attack"
- "Try different frequencies"
- "Build a siren: loop frequency from low to high"
- "Combine with animation—play tone when star hits wall"

### Game Integration Ideas

**From Lesson 6 (Animation):**
- Title screens: animate flashing "PRESS FIRE"
- HUD effects: bounce arrows around menu selection
- Simple enemies: ASCII ghosts patrol the screen
- Transitions: wipe screen by sliding symbols

**From Lesson 7 (Sound):**
- UI cues: tone when menus open
- Collision sound: different frequencies for hits vs. misses
- Victory jingle: loop through notes
- Alarm: random pitches for warning effects

---

## Lesson Structure Elements to Preserve

All three archived lessons had excellent pedagogical structure to maintain in new lessons:

1. **Opening paragraph** - Sets context, connects to prior knowledge
2. **The One-Minute Tour** - Bullet-point overview
3. **Example Program** - Simple, runnable code
4. **Experiment Section** - Variations to try
5. **Concept Expansion** - Where this leads
6. **Game Integration** - Practical uses
7. **From the Vault** - Links to deeper topics
8. **Quick Reference** - Table or code block summary
9. **What You've Learnt** - Capabilities unlocked

---

## Media Assets Summary

**Salvaged Videos (3 files, 203KB total):**
- lesson-006/example-1.mp4 (46KB) - FOR loop animation
- lesson-006/example-2.mp4 (43KB) - TI timer animation
- lesson-007/example-1.mp4 (114KB) - SID sound demonstration

**Future Use:**
- Lesson 10 (First Sound) - lesson-007/example-1.mp4
- Lesson 15 (Timing) - lesson-006/example-1.mp4, example-2.mp4

---

**End of Salvage Document**
