# Game 01: Pixel Hunter

**Track:** AMOS
**Genre:** Target Practice
**Units:** 4
**BASIC Version:** AMOS Professional

---

## Overview

Click targets as they appear. Introduction to AMOS environment, mouse input, and sprites.

### What You Build

- Random target spawning
- Mouse click detection
- Score counter
- Timer countdown
- High score tracking

---

## Unit Breakdown

### Unit 1: AMOS Environment
**Concepts:** Screen Open, Flash Off, Curs Off

### Unit 2: Sprites and Mouse
**Concepts:** Load sprites, Sprite command, Mouse Key

### Unit 3: Target Logic
**Concepts:** Rnd, timing, hit detection

### Unit 4: Complete Game
**Concepts:** Timer, scoring, game loop

---

## Complete Code

```basic
' PIXEL HUNTER - AMOS
Screen Open 0,320,256,32,Lowres
Flash Off : Curs Off : Cls 0
Load "targets.abk",1

SCORE=0 : TIME=30 : BEST=0

Do
  TARGETX=Rnd(280)+20
  TARGETY=Rnd(200)+20
  Sprite 1,TARGETX,TARGETY,1
  START=Timer

  Repeat
    If Mouse Key=1
      MX=X Screen(X Mouse)
      MY=Y Screen(Y Mouse)
      If Abs(MX-TARGETX)<16 And Abs(MY-TARGETY)<16
        Inc SCORE
        Boom : Exit
      End If
      Wait 10
    End If
  Until Timer-START>50

  Dec TIME
  Locate 0,0 : Print "SCORE:";SCORE;" TIME:";TIME
Loop Until TIME=0

If SCORE>BEST Then BEST=SCORE
Print "GAME OVER! SCORE:";SCORE;" BEST:";BEST
```

---

## Skills Learned

- AMOS screen setup
- Sprite display
- Mouse input
- Timer usage
- Basic game loop
