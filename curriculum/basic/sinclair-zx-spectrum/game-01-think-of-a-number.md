# Game 01: Think of a Number

**Track:** Spectrum BASIC
**Genre:** Number Guessing
**Units:** 4
**BASIC Version:** Sinclair BASIC

---

## Overview

Classic number guessing game. Introduction to Sinclair BASIC's unique keyword entry system.

### What You Build

- Computer picks random number (1-100)
- Player guesses with feedback
- Attempt counter
- Play again option

---

## Unit Breakdown

### Unit 1: First Program
**Concepts:** Keyword entry, PRINT, line numbers

### Unit 2: Variables and RND
**Concepts:** LET, RND, INT

### Unit 3: Input and IF
**Concepts:** INPUT, IF/THEN

### Unit 4: Game Loop
**Concepts:** GO TO, complete game

---

## Complete Code

```basic
10 CLS
20 PRINT "** THINK OF A NUMBER **"
30 PRINT
40 LET n = INT(RND*100)+1
50 LET a = 0
60 PRINT "I'm thinking of a number"
70 PRINT "between 1 and 100..."
80 PRINT
90 LET a = a + 1
100 INPUT "Your guess? ";g
110 IF g > n THEN PRINT "Too high!": GO TO 90
120 IF g < n THEN PRINT "Too low!": GO TO 90
130 PRINT "*** CORRECT! ***"
140 PRINT "You got it in ";a;" tries!"
150 INPUT "Play again? (y/n) ";a$
160 IF a$ = "y" THEN GO TO 10
170 STOP
```

---

## Spectrum BASIC Notes

- Keywords entered with single keypress (K for PRINT, etc.)
- LET required for assignment
- GO TO is two words
- No ELSE statement in standard BASIC
