# Game 01: Reflex

**Track:** Blitz Basic
**Genre:** Reaction Timer
**Units:** 4
**BASIC Version:** Blitz Basic 2

---

## Overview

Simple reaction test. Introduction to Blitz environment, compilation, and VBlank timing.

### What You Build

- Wait for signal
- Measure reaction time
- Multiple rounds
- Best time tracking
- Average calculation

---

## Unit Breakdown

### Unit 1: Blitz Environment
**Concepts:** Editor, compilation, running

### Unit 2: Display and Timing
**Concepts:** BitMap, VWait, timing

### Unit 3: Input Detection
**Concepts:** Joyb(), fire button

### Unit 4: Complete Game
**Concepts:** Scoring, statistics

---

## Blitz vs AMOS

```blitz
; BLITZ IS COMPILED - MUCH FASTER
; More strict syntax, more powerful

DEFTYPE .w  ; Default to word (16-bit)

; Constants
#SCREENW = 320
#SCREENH = 256

; Initialisation
BitMap 0,#SCREENW,#SCREENH,4
VWait 50

; Timing is frame-accurate
startframe.l = VBlankCount()
```

---

## Complete Code

```blitz
DEFTYPE .w
#SCREENW = 320
#SCREENH = 256

BitMap 0,#SCREENW,#SCREENH,4
best.w = 9999

For round = 1 To 5
  Cls 0
  Locate 10,10
  NPrint "GET READY..."

  ; Random delay
  VWait Rnd(150)+50

  Locate 10,10
  NPrint "GO!          "
  start.l = VBlankCount()

  ; Wait for button
  While Joyb(1)=0 : Wend

  reaction.w = VBlankCount()-start
  If reaction < best Then best = reaction

  Locate 10,12
  NPrint "Time: ",reaction," frames"
  VWait 100
Next round

NPrint "Best: ",best," frames"
MouseWait
End
```

---

## Skills Learned

- Blitz Basic syntax
- DEFTYPE for types
- VWait and VBlankCount
- Compilation benefits
- Joystick input
