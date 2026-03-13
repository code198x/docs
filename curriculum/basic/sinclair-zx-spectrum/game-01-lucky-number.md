# Game 01: Lucky Number

**Track:** Spectrum BASIC
**Genre:** Number guessing game
**Units:** 8
**Language:** Sinclair BASIC
**Max lines:** ~20

---

## Premise

The computer picks a number between 1 and 100. You guess. The computer tells you higher or lower. Keep guessing until you find it.

This is the very first program the learner writes. They have never programmed before. Every concept is new: what a line number is, what PRINT does, what a variable holds. The game exists to make these ideas tangible. You type something, the computer responds, and you can see exactly why.

The number starts fixed (not random) so the learner can predict what the program will do while testing. Randomness arrives late, once everything else works. By the end, the game plays properly and the learner has written a complete interactive program from scratch.

---

## Core Mechanics

The player types a number. The program compares it to a secret number and prints "Too high", "Too low", or "You got it!" The game loops until the player guesses correctly. In the final version, the secret number is random each time.

---

## Unit Breakdown

| Unit | Title | What the learner builds | New concepts |
|------|-------|------------------------|--------------|
| 1 | Hello, Spectrum | Type `10 PRINT "Hello"` and run it. Change the message. Add a second PRINT line. See how line numbers control order. | PRINT, strings, RUN, line numbers |
| 2 | Giving things names | Use LET to store a number in a variable. Print the variable. Change the value and run again to see the output change. | LET, numeric variables |
| 3 | Asking a question | Use INPUT to ask the player for their name and greet them. Then ask for a number and print it back. | INPUT, string input, prompts |
| 4 | Making decisions | Set a secret number with LET. Ask the player to guess. Use IF/THEN to print "Correct!" when the guess matches. | IF/THEN, `=` comparison |
| 5 | Higher or lower | Add two more IF/THEN lines: one for too high (`>`), one for too low (`<`). The program now gives feedback on every guess. | `<` and `>` comparisons |
| 6 | Play again | Use GO TO to jump back to the INPUT line after a wrong guess. The game now loops until the player wins. | GO TO, loops |
| 7 | Pick a number, any number | Replace the fixed number with `LET n = INT(RND * 100) + 1`. The game is different every time. Add REM lines to explain what each section does. | RND, INT, REM |
| 8 | Finishing touches | Add a title message, a guess counter, and a "Well done — you got it in N guesses" message at the end. Test with friends. | Counting with variables, combining strings and numbers in PRINT |

**Milestone:** The learner has written, edited, and run a complete interactive program. They understand variables, input, decisions, and loops — the building blocks of every program that follows.

---

## Technical Notes

### Key Variables

```
n   - the secret number (fixed in units 4-6, random from unit 7)
g   - the player's guess
c   - guess counter (unit 8)
```

### Line Numbering

The final program uses roughly lines 10-200. No subroutines or DATA statements — everything runs top to bottom with a single GO TO loop.

### Memory

Negligible. The entire program fits in under 500 bytes.

### Spectrum-Specific Notes

- The Spectrum 48K has no ELSE keyword. Each comparison needs its own IF/THEN line.
- The K-mode cursor (keyword mode) appears when the Spectrum expects a command. The learner needs to understand this before they can type their first line. Unit 1 should address this directly.
- `GO TO` is two words on the Spectrum, not `GOTO`.

---

## Changelog

- **v1.0 (2026-03-13):** Initial game outline for v5.0 curriculum.
