# Game 07: Speed Circuit

**Track:** C64 BASIC
**Genre:** Top-Down Racing
**Units:** 8
**BASIC Version:** Stock BASIC V2

---

## Overview

Top-down racing using character graphics for the track. Teaches timing and surface detection.

### What You Build

- Car (character)
- Track (custom characters)
- Lap counting
- Timer using TI
- Surface effects (grass slowdown)

---

## Unit Breakdown

### Unit 1: Track Design
**Concepts:** Custom characters for track pieces

### Unit 2: Drawing the Track
**Concepts:** Level data, PRINT track

### Unit 3: The Car
**Concepts:** Car character, position

### Unit 4: Movement
**Concepts:** Joystick, 4/8 direction

### Unit 5: Surface Detection
**Concepts:** PEEK surface, speed effects

### Unit 6: Checkpoints
**Concepts:** Checkpoint detection, lap counting

### Unit 7: Timer
**Concepts:** TI and TI$ variables

### Unit 8: Complete Race
**Concepts:** Countdown, best times

---

## Custom Characters for Track

```basic
100 REM COPY CHARSET TO RAM
110 POKE 56334,0: POKE 1,51
120 FOR I=0 TO 2047: POKE 12288+I,PEEK(53248+I): NEXT
130 POKE 1,55: POKE 56334,1
140 POKE 53272,(PEEK(53272)AND240)+12

150 REM DEFINE TRACK PIECES
160 FOR I=0 TO 7: READ D: POKE 12288+128*8+I,D: NEXT
170 DATA 255,255,255,255,255,255,255,255: REM ROAD
```

## Surface Detection

```basic
200 REM CHECK SURFACE UNDER CAR
210 SURFACE=PEEK(1024+CY*40+CX)
220 IF SURFACE=32 THEN SP=1: REM GRASS - SLOW
230 IF SURFACE=160 THEN SP=3: REM ROAD - NORMAL
240 IF SURFACE=102 THEN SP=4: REM BOOST PAD
250 IF SURFACE=86 THEN 900: REM BARRIER - CRASH
```

### Timer Usage

```basic
300 REM START RACE TIMER
310 TI$="000000"

400 REM DISPLAY TIME
410 T=TI/60: REM CONVERT TO SECONDS
420 PRINT TAB(30)INT(T)
```

---

## Skills Learned

- TI/TI$ for timing
- Surface-based gameplay
- Checkpoint systems
- Custom track characters
- Lap counting logic
