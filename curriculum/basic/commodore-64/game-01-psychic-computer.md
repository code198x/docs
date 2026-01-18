# Game 01: Psychic Computer

**Track:** C64 BASIC
**Genre:** Number Guessing
**Units:** 4
**BASIC Version:** Stock BASIC V2

---

## Overview

The classic "guess my number" game - the simplest possible introduction to programming.

### What You Build

- Computer picks a random number (1-100)
- Player enters guesses
- "Too high" / "Too low" feedback
- Win message with attempt count
- Play again option

---

## Unit Breakdown

### Unit 1: First Program
**Concepts:** PRINT, line numbers, RUN, SAVE

### Unit 2: Variables and Random
**Concepts:** Variables, RND(), INT()

### Unit 3: Input and Conditionals
**Concepts:** INPUT, IF/THEN, comparison operators

### Unit 4: Game Loop and Polish
**Concepts:** GOTO loops, counters, complete game

---

## Complete Code

```basic
10 PRINT CHR$(147)
20 PRINT "** PSYCHIC COMPUTER **"
30 PRINT
40 N = INT(RND(1)*100)+1
50 A = 0
60 PRINT "I'M THINKING OF A NUMBER"
70 PRINT "BETWEEN 1 AND 100..."
80 PRINT
90 A = A + 1
100 INPUT "YOUR GUESS"; G
110 IF G > N THEN PRINT "TOO HIGH!": GOTO 90
120 IF G < N THEN PRINT "TOO LOW!": GOTO 90
130 PRINT "*** CORRECT! ***"
140 PRINT "YOU GOT IT IN"; A; "TRIES!"
150 INPUT "PLAY AGAIN (Y/N)"; A$
160 IF A$ = "Y" THEN GOTO 10
170 END
```

---

## Skills Learned

- Variables (numeric and string)
- INPUT statement
- IF/THEN conditionals
- GOTO loops
- RND() function
