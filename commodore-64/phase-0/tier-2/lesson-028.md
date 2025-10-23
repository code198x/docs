# Lesson 028: Multi-Voice Game Music

**Arc:** Sound & Music Mastery
**Position:** Lesson 5 of 5 in arc
**Type:** Synthesis
**Estimated Completion:** 70 lines of code

## Learning Objectives

- Compose complete 3-voice game music
- Balance melody, bass, and rhythm tracks
- Integrate music with gameplay without slowdown
- Synthesize all Sound & Music Mastery concepts

## Prerequisites

**From Previous Lessons:**
- Three voice control (L24)
- Melody sequencer (L25)
- Non-blocking music (L26)
- Sound effects library (L27)

**BASIC Knowledge:**
- Complete SID mastery
- Music theory basics
- Data-driven sequencing

## Key Concepts Introduced

### Three-Track Composition
Voice 1: Melody (sawtooth, lead), Voice 2: Bass (triangle, low notes), Voice 3: Rhythm/drums (pulse/noise, percussive).

### Track Synchronization
All three voices advance together, reading from parallel DATA arrays. Same timing index for all tracks.

### Waveform Roles
Different waveforms suit different musical roles: triangle=bass, sawtooth=melody, pulse=harmony, noise=percussion.

### Music-Gameplay Balance
Full 3-voice music + complex gameplay = potential slowdown. Learn to balance or simplify one system.

## Code Pattern

```basic
10 DIM M1(32),M2(32),M3(32),D(32):REM 3 voices + duration
20 REM Load music data
30 FOR I=1 TO 16
40 READ M1(I),M2(I),M3(I),D(I)
50 NEXT I
60 MI=1:MT=0:ML=16
70 POKE 54296,15
80 REM Game loop
90 REM [Gameplay here]
100 GOSUB 1000:REM Update music
110 GOTO 90
1000 REM Update all three voices
1010 MT=MT+1
1020 IF MT<D(MI)*5 THEN RETURN
1030 REM Stop all voices
1040 POKE 54276,16:POKE 54283,16:POKE 54290,16
1050 MI=MI+1:IF MI>ML THEN MI=1
1060 REM Voice 1 - Melody (sawtooth)
1070 IF M1(MI)>0 THEN POKE 54272,M1(MI) AND 255:POKE 54273,INT(M1(MI)/256):POKE 54277,0:POKE 54278,240:POKE 54276,33
1080 REM Voice 2 - Bass (triangle)
1090 IF M2(MI)>0 THEN POKE 54279,M2(MI) AND 255:POKE 54280,INT(M2(MI)/256):POKE 54284,0:POKE 54285,240:POKE 54283,17
1100 REM Voice 3 - Rhythm (pulse/noise)
1110 IF M3(MI)>0 THEN POKE 54286,M3(MI) AND 255:POKE 54287,INT(M3(MI)/256):POKE 54291,0:POKE 54292,240:POKE 54290,65
1120 MT=0:RETURN
2000 REM Music data - melody,bass,rhythm,duration
2010 DATA 8372,4186,0,4,9398,4699,0,4,10548,5274,0,4,9398,4699,0,4
2020 DATA 8372,4186,8372,4,8372,4186,0,4,8372,4186,8372,8,0,0,0,2
2030 REM [More music data...]
```

## Hardware Interaction

**Chips Involved:**
- **SID** - All three voices simultaneously

**Memory Addresses:**
- Voice 1: 54272-54278
- Voice 2: 54279-54285
- Voice 3: 54286-54292
- Volume: 54296

## Common Pitfalls

1. **Track desynchronization:** All voices must advance together
2. **Bass too high:** Bass should be octave below melody (divide frequency by 2)
3. **Rhythm too busy:** Drums on every note = cluttered
4. **Performance impact:** 3-voice music + complex game = noticeable slowdown
5. **Clashing frequencies:** Some note combinations sound bad (check harmonics)

## Extension Ideas

- Add music variation per game state (intense during danger)
- Create multiple songs for different levels/moods
- Add dynamic mixing (reduce bass during action)
- Implement music crossfade between songs
- Add conductor system (change music based on events)
- Save music as separate data file

## Builds Toward

**In Next Tier:**
- All games can use this music system
- More complex integration challenges

**Performance Note:**
"3-voice music playback takes ~2-3ms per frame. Combined with sprite-heavy gameplay, this contributes to Tier 2's natural 12-15 fps performance awareness."

## Quick Reference

**Waveform Assignment:**
```
Voice 1 (Melody): 33 (sawtooth) - bright, cutting
Voice 2 (Bass): 17 (triangle) - smooth, low
Voice 3 (Rhythm): 65 (pulse) or 129 (noise)
```

**Frequency Relationships:**
```
Melody: Standard pitch (8000-16000)
Bass: Octave down (melody ÷ 2)
Rhythm: Short bursts or noise
```

**Music Data Format:**
```basic
2000 DATA melody_freq,bass_freq,rhythm_freq,duration
2010 DATA 8372,4186,0,4  :REM C note, C bass, no drum, quarter
2020 DATA 0,4186,8372,4  :REM Rest melody, bass continues, drum hit
```

**Composition Tips:**
- Start with melody alone, get it right
- Add bass on strong beats (1st, 3rd)
- Add rhythm sparingly (accents)
- Use rests for breathing room
- Match music tempo to game pace

**Performance Budget:**
```
Music update: 2-3ms/frame
Sprite system: 5-8ms/frame
Game logic: 3-5ms/frame
Total: 10-16ms (target 16.7ms for 60fps)
```

**Arc 2 Complete - Sound & Music Mastered!**
