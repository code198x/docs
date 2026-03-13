# Game 02: Countdown

**Track:** Spectrum BASIC
**Genre:** Reaction timer
**Units:** 8
**Language:** Sinclair BASIC
**Max lines:** ~25

---

## Premise

A word appears on screen after a random delay. Press any key the instant you see it. The program measures how fast you reacted and shows your time. Play five rounds and try to beat your best.

This game teaches the difference between two ways of reading the keyboard: INPUT (which stops and waits) and INKEY$ (which checks right now and keeps going). That distinction is the foundation of every action game on the Spectrum. The reaction timer makes it physical — you feel the difference between waiting and polling.

The learner already knows PRINT, LET, IF/THEN, and GO TO from Game 1. This game builds on those skills while introducing sound, screen clearing, and real-time keyboard checking.

---

## Core Mechanics

The program clears the screen, waits a random number of seconds, then displays a word (like "NOW!"). A timing loop counts upward while INKEY$ checks for a keypress. When the player presses a key, the loop stops and the elapsed count becomes the reaction score. Lower is better. After five rounds, the program shows the best time.

---

## Unit Breakdown

| Unit | Title | What the learner builds | New concepts |
|------|-------|------------------------|--------------|
| 1 | Clean slate | Use CLS to clear the screen, then print a message. Clear and print again. See how CLS gives you a fresh display each time. | CLS |
| 2 | Wait for it | Use PAUSE to make the program wait before showing a message. Change the PAUSE value to control the delay. The screen sits empty, then the word appears. | PAUSE |
| 3 | Make some noise | Add BEEP to play a sound when the word appears. Experiment with pitch and duration — high notes, low notes, short blips, long tones. | BEEP (duration, pitch) |
| 4 | Press any key | Use INKEY$ in a loop to wait for a keypress. The loop checks INKEY$ on every pass — if it equals the empty string `""`, no key is pressed, so loop again. When a key is pressed, the loop ends. | INKEY$, empty string `""`, polling loop with GO TO |
| 5 | How fast? | Add a counter variable inside the INKEY$ loop. Each pass adds 1. When the player presses a key, print the counter as their reaction score. | Counting in a loop, timing |
| 6 | A proper word | Store the prompt in a string variable (`a$`). Print `a$` instead of a fixed string. Change the word between rounds — "NOW!", "GO!", "PRESS!" — so the player can't predict the text. | String variables (`a$`), assigning strings with LET |
| 7 | Random delay | Replace the fixed PAUSE with a random value (`PAUSE 50 + INT(RND * 100)`) so the player cannot anticipate when the word appears. Add a cheat check: if the player presses a key during the pause, print "Too early!" | Random PAUSE, cheat detection |
| 8 | Five rounds | Wrap the game in a five-round loop using GO TO and a round counter. Track the best (lowest) score across all rounds. Print a summary at the end with the best time and a rating. | Round counter, tracking a best score, end-of-game summary |

**Milestone:** The learner understands two models of keyboard input — blocking (INPUT) and non-blocking (INKEY$) — and can make sounds and clear the screen. These are the tools every real-time game needs.

---

## Technical Notes

### Key Variables

```
a$  - the prompt word displayed on screen
t   - reaction time counter
b   - best (lowest) time across rounds
r   - current round number
```

### Line Numbering

The final program uses roughly lines 10-250. A single main loop controlled by GO TO handles the five rounds.

### Memory

Negligible. Under 600 bytes.

### Spectrum-Specific Notes

- INKEY$ returns a single character if a key is held, or the empty string `""` if no key is pressed. It does not wait — execution continues immediately.
- PAUSE N waits for N frames (1 frame = 1/50th of a second at 50Hz). PAUSE 50 is one second. PAUSE also ends early if a key is pressed, which matters for the cheat detection in unit 7.
- BEEP takes two arguments: duration in seconds and pitch in semitones relative to middle C. `BEEP 0.1, 10` is a short high blip. `BEEP 0.5, -5` is a longer low tone.
- No ELSE keyword on the 48K. The "too early" check and the "key pressed" check each need separate IF/THEN lines.

---

## Changelog

- **v1.0 (2026-03-13):** Initial game outline for v5.0 curriculum.
