# Lesson 011: Sound FX Generator

**Arc:** Sound Lab
**Position:** Lesson 2 of 2 in arc
**Type:** Synthesis
**Estimated Completion:** 30 lines of code

## Learning Objectives

- Create practical game sound effects
- Use different waveforms for different effect types
- Implement frequency sweeps and noise for variety
- Build reusable sound effect library

## Prerequisites

**From Previous Lessons:**
- SID basics and musical notes (L10)
- POKE for hardware control (L7-10)
- Subroutines for reusable code (learned naturally)

**BASIC Knowledge:**
- SID registers and waveforms
- GOSUB/RETURN for subroutines
- Loops for sound duration

## Key Concepts Introduced

### Sound Effect Design
Different waveforms suit different effects: sawtooth for lasers, noise for explosions, pulse for beeps, triangle for soft sounds.

### Frequency Sweeps
Changing frequency rapidly creates sweeping effects (falling, rising, warble). Perfect for lasers, explosions, and jumps.

### Subroutines for Organization
Each sound effect becomes a GOSUB target: `GOSUB 1000` plays laser, `GOSUB 2000` plays explosion. Organized, reusable code.

## Code Pattern

```basic
10 PRINT "1=LASER 2=EXPLOSION 3=JUMP"
20 GET K$:IF K$="" THEN 20
30 IF K$="1" THEN GOSUB 1000
40 IF K$="2" THEN GOSUB 2000
50 IF K$="3" THEN GOSUB 3000
60 GOTO 20
1000 REM Laser sound
1010 POKE 54296,15
1020 FOR F=255 TO 50 STEP -5
1030 POKE 54272,F:POKE 54273,20
1040 POKE 54276,33:REM Sawtooth
1050 FOR D=1 TO 10:NEXT D
1060 NEXT F
1070 POKE 54276,32:RETURN
2000 REM Explosion sound
2010 POKE 54296,15
2020 POKE 54276,129:REM Noise
2030 FOR D=1 TO 200:NEXT D
2040 POKE 54276,128:RETURN
```

## Hardware Interaction

**Chips Involved:**
- **SID** - All 3 voices available for complex effects

**Memory Addresses:**
- Voice 1: `54272-54278` ($D400-$D406)
- Voice 2: `54279-54285` ($D407-$D40D)
- Voice 3: `54286-54292` ($D40E-$D414)
- Volume: `54296` ($D418)

**Waveforms for Effects:**
- **Sawtooth (33):** Lasers, zaps, bright sounds
- **Noise (129):** Explosions, crashes, white noise
- **Pulse (65):** Beeps, warnings, hollow sounds
- **Triangle (17):** Soft jumps, pickups, mellow tones

## Common Pitfalls

1. **Effect too fast:** Need delays in sweep loops or effect is inaudible
2. **Not turning off:** Forgetting gate off (waveform-1) leaves sound droning
3. **Wrong waveform:** Triangle for explosion sounds weak, noise for melody is wrong
4. **Volume issues:** Check volume set to 15 for all effects
5. **Voice conflicts:** Multiple effects using same voice = interference

## Extension Ideas

- Add more effects (coin, power-up, damage, menu select)
- Layer effects (use multiple voices simultaneously)
- Add pitch variation (randomize frequency slightly)
- Create effect categories (UI sounds, combat sounds, movement sounds)
- Make effects interruptible (stop previous before starting new)

## Builds Toward

**In This Tier:**
- L14: Star Catcher integrates sound effects

**In Next Tier:**
- Games use this library throughout (L18-23)
- Multi-voice effects (L24-28)
- Non-blocking effects with music (L26-27)

## Quick Reference

**Common Game Sound Effects:**

**Laser/Shoot:**
```basic
1000 POKE 54296,15
1010 FOR F=255 TO 50 STEP -5
1020 POKE 54272,F:POKE 54273,20
1030 POKE 54276,33
1040 FOR D=1 TO 10:NEXT D:NEXT F
1050 POKE 54276,32:RETURN
```

**Explosion:**
```basic
2000 POKE 54296,15:POKE 54276,129
2010 FOR D=1 TO 200:NEXT D
2020 POKE 54276,128:RETURN
```

**Jump/Pickup:**
```basic
3000 POKE 54296,15
3010 FOR F=100 TO 200 STEP 5
3020 POKE 54272,F:POKE 54273,10
3030 POKE 54276,17
3040 FOR D=1 TO 5:NEXT D:NEXT F
3050 POKE 54276,16:RETURN
```

**Damage/Hit:**
```basic
4000 POKE 54296,15:POKE 54276,129
4010 FOR D=1 TO 50:NEXT D
4020 POKE 54276,128:RETURN
```

**Coin/Collect:**
```basic
5000 POKE 54296,15
5010 POKE 54272,100:POKE 54273,30
5020 POKE 54276,65
5030 FOR D=1 TO 100:NEXT D
5040 POKE 54276,64:RETURN
```

**Effect Design Tips:**
- **Rising pitch = positive** (jump, collect, power-up)
- **Falling pitch = negative** (fall, death, lose)
- **Fast sweep = quick action** (laser, hit)
- **Slow sweep = long action** (warp, transform)
- **Noise = chaotic** (explosion, static)
- **Pure tone = clean** (beep, select)
