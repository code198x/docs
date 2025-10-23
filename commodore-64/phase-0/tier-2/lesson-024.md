# Lesson 024: Three Voice Player

**Arc:** Sound & Music Mastery
**Position:** Lesson 1 of 5 in arc
**Type:** Standard
**Estimated Completion:** 35 lines of code

## Learning Objectives

- Control all three SID voices simultaneously
- Create chords and harmonies
- Understand voice independence
- Build foundation for music composition

## Prerequisites

**From Previous Lessons:**
- SID basics (L10-11)
- Musical note frequencies (L10)
- Multiple system management (L20-23)

**BASIC Knowledge:**
- SID register layout
- Waveform control
- ADSR envelopes

## Key Concepts Introduced

### Three Independent Voices
SID has 3 completely independent voices. Each has own frequency, waveform, ADSR. Can play different notes simultaneously.

### Chord Construction
Musical chords = multiple notes together. C major chord = C + E + G played simultaneously on voices 1, 2, 3.

### Voice Register Offsets
Voice 1: 54272+, Voice 2: 54279+, Voice 3: 54286+. Each voice has 7 control registers.

### Harmonic Balance
Different waveforms and volumes per voice create rich sounds. Triangle bass + sawtooth melody + pulse harmony.

## Code Pattern

```basic
10 REM Play C major chord (C,E,G)
20 POKE 54296,15:REM Volume max
30 REM Voice 1 - C note
40 POKE 54272,84:POKE 54273,32
50 POKE 54277,0:POKE 54278,240
60 POKE 54276,17:REM Triangle
70 REM Voice 2 - E note
80 POKE 54279,52:POKE 54280,41
90 POKE 54284,0:POKE 54285,240
100 POKE 54283,17:REM Triangle
110 REM Voice 3 - G note
120 POKE 54286,0:POKE 54287,49
130 POKE 54291,0:POKE 54292,240
140 POKE 54290,17:REM Triangle
150 REM Hold for duration
160 FOR D=1 TO 1000:NEXT D
170 REM Stop all voices
180 POKE 54276,16:POKE 54283,16:POKE 54290,16
```

## Hardware Interaction

**Chips Involved:**
- **SID** - All three voices

**Memory Addresses:**
```
Voice 1: 54272-54278 ($D400-$D406)
Voice 2: 54279-54285 ($D407-$D40D)
Voice 3: 54286-54292 ($D40E-$D414)
Volume:  54296 ($D418)
```

## Common Pitfalls

1. **Register confusion:** Easy to POKE wrong voice (54273 vs 54280)
2. **Volume conflicts:** All voices share master volume (54296)
3. **Timing misalignment:** Starting voices at slightly different times sounds wrong
4. **ADSR mismatch:** Different ADSRs per voice = notes don't align
5. **Frequency errors:** Wrong note frequencies break chords

## Extension Ideas

- Play different chord types (minor, diminished, augmented)
- Create chord progressions (C-F-G-C sequence)
- Add rhythm (strum chords, not all together)
- Use different waveforms per voice (triangle bass, sawtooth lead)
- Create arpeggio (rapid note sequence)
- Add melody over sustained chord

## Builds Toward

**In This Tier:**
- L25: Melody sequencer
- L26: Non-blocking music
- L28: Complete 3-voice game music

## Quick Reference

**SID Voice Register Layout (each voice):**
```
+0,+1: Frequency (16-bit)
+2,+3: Pulse width (pulse wave only)
+4: Control register (waveform + gate)
+5: Attack/Decay
+6: Sustain/Release
```

**Voice Base Addresses:**
```basic
V1=54272  :REM $D400
V2=54279  :REM $D407
V3=54286  :REM $D40E
```

**Play Note on Voice:**
```basic
1000 REM Play note F on voice V
1010 POKE V,FL:POKE V+1,FH:REM Frequency
1020 POKE V+5,0:POKE V+6,240:REM ADSR
1030 POKE V+4,17:REM On
1040 RETURN
```

**Common Chords:**
```
C major: C(8372) E(10548) G(12544)
F major: F(11176) A(14080) C(8372)
G major: G(12544) B(15804) D(9398)
A minor: A(14080) C(8372) E(10548)
```

**Waveform Combinations:**
- Triangle+Triangle+Triangle = Mellow, organ-like
- Sawtooth+Sawtooth+Sawtooth = Bright, brassy
- Triangle+Sawtooth+Pulse = Rich, varied
- Pulse+Pulse+Pulse = Hollow, reedy

See `/docs/SID-QUICK-REFERENCE.md` (if available) for note frequency table
