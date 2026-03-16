# Game 02: Countdown

**Track:** Spectrum BASIC
**Genre:** Reaction timer
**Units:** 8
**Language:** Sinclair BASIC
**Max lines:** ~65 (full program with title animation), ~40 game logic

---

## Premise

A word appears on screen after a random delay. Press any key the instant you see it. The program measures how fast you reacted and shows your time. Play five rounds and try to beat your best.

This is the first game the learner builds from scratch. In Game 1, they typed in a complete program and learnt by modifying it. In Game 2, they write every line themselves — but the program is runnable from the very first unit. Each unit adds a visible feature. By Unit 8, the learner has built a complete five-round reaction timer with sound, random delays, cheat detection, best-time tracking, and a results screen.

The title animation counts down 3, 2, 1 with low tones — like the red lights at the start of a Formula 1 race — then a high-pitched burst on GO! as the screen flashes green. The game teaches the difference between INPUT (which stops and waits) and INKEY$ (which checks right now and keeps going). That distinction is the foundation of every action game on the Spectrum.

---

## Core Mechanics

The program clears the screen, waits a random number of seconds, then displays "NOW!" with a border flash and a sound. A timing loop counts upward while INKEY$ checks for a keypress. When the player presses a key, the loop stops and the elapsed count becomes the reaction score. Lower is better. After five rounds, the program shows the best time and a rating.

---

## The Starter Program

Unlike Game 1, there is no type-in. The learner builds this game incrementally. But the finished program includes visual elements they haven't formally learnt yet: a title animation with a red colour fill and block-pixel countdown digits (3, 2, 1, GO!), and a red header bar on the game screen. These use FOR/NEXT (Game 3), PAPER colours (Game 3), and DATA/GO SUB (Games 5-6). They arrive as "magic" sections added in Unit 1, just like the visual subroutines in Lucky Number.

The game logic — the part the learner writes and understands — is roughly 40 lines. The title animation and header bar add another 25 lines of visual scaffolding.

---

## Unit Breakdown

### Unit 1: The Stage

**Concept:** CLS, PAPER/INK/BORDER basics, building the game screen

The learner creates the game screen from scratch: black background, red header bar with "COUNTDOWN" in bright white, "Round 1 of 5" counter, and "Get ready..." in the centre. The title animation (red fill, countdown digits) is provided as a type-in block — magic for now.

**What the learner builds:**
- Line 5: `BORDER 0: PAPER 0: INK 7: CLS` — black screen
- Lines 120-160: header bar and title text
- Line 170: round counter
- Line 190: "Get ready..." prompt

**Visual moments:** A black screen with a red header bar and coloured text. The game screen exists. It doesn't do anything yet, but it looks like it belongs to a game.

---

### Unit 2: The Wait

**Concept:** PAUSE, timing in frames (50fps)

The "Get ready..." message sits on screen, then after a fixed delay the word "NOW!" appears. PAUSE N waits for N frames — PAUSE 50 is one second. The learner experiments with different PAUSE values to feel the difference between half a second and three seconds.

**What the learner adds:**
- Line 200: `LET w=100` — a fixed wait of 2 seconds
- Lines 230-240: the PAUSE loop
- Lines 260-280: clear "Get ready..." and print "NOW!" in bright yellow with FLASH

**Visual moments:** The screen sits still, then "NOW!" appears. The delay is palpable — the learner feels the wait.

---

### Unit 3: Sound

**Concept:** BEEP (duration, pitch), sound as feedback

Add a sound when "NOW!" appears — a short high blip that says "react now." Add a different sound for the result — lower, longer. The learner experiments with pitch and duration.

**What the learner adds:**
- Line 290: `BEEP 0.05,20` — short high blip on "NOW!"
- Line 370: `BEEP 0.1,15` — medium tone on reaction
- Border colour changes: yellow border on "NOW!", green on reaction, back to black

**Visual moments:** The border flashes yellow, the BEEP fires, "NOW!" appears. Press a key and the border turns green with a different tone. Sound and colour reinforce the moment.

---

### Unit 4: Press Any Key

**Concept:** INKEY$, polling loops, the difference from INPUT

Replace the placeholder with a real INKEY$ loop. The program checks INKEY$ on every pass — if it's empty, loop again. When a key is pressed, the loop ends. This is fundamentally different from INPUT: the program doesn't stop and wait, it keeps checking.

**What the learner adds:**
- Lines 300-340: the INKEY$ timing loop
- The `""` empty string comparison

**The key insight:** INPUT blocks — the program stops. INKEY$ polls — the program keeps running. Every action game uses INKEY$, not INPUT. The learner has now used both (INPUT in Game 1, INKEY$ here) and can feel the difference.

**Visual moments:** Press a key and the game responds instantly. The "NOW!" disappears and the result appears. No cursor, no prompt — just immediate response.

---

### Unit 5: How Fast?

**Concept:** Counting in a loop, using a counter as a timer

Add a counter variable `t` inside the INKEY$ loop. Each pass adds 1. When the player presses a key, `t` holds the reaction time. Print it on screen.

**What the learner adds:**
- Line 300: `LET t=0`
- Line 320: `LET t=t+1` inside the loop
- Line 390: display the time

**Visual moments:** "Time: 12" appears after pressing a key. Try again — "Time: 8". The number is the score. Lower is better. The learner can see their own reaction speed as a number.

---

### Unit 6: Random Delay

**Concept:** RND applied to PAUSE, cheat detection

Replace the fixed wait with a random one: `LET w=50+INT(RND*100)`. Now the player can't anticipate when "NOW!" appears. Add cheat detection: if INKEY$ is pressed during the wait, print "Too early!" and restart the round.

**What the learner adds:**
- Line 200: `LET w=50+INT(RND*100)`
- Lines 220-230: cheat check inside the wait loop
- "Too early!" message with a low warning BEEP

**Visual moments:** The delay is different every time. Press too soon and "Too early!" appears in bright red with an ominous low tone. The game fights back.

---

### Unit 7: Five Rounds

**Concept:** FOR/NEXT loop for rounds, tracking a best score

Wrap the game in a five-round FOR/NEXT loop. Track the best (lowest) time across all rounds. Show "New best!" when the player beats their record. Display the best time in the header area.

**What the learner adds:**
- Lines 110, 450: `FOR n=1 TO 5` / `NEXT n`
- Line 180: best time display
- Lines 400-410: best time tracking and "New best!"
- Lines 430-440: "Press any key..." between rounds (with debounce)

**The key insight:** FOR/NEXT is a loop with a built-in counter. Unlike GO TO (which loops forever until something breaks out), FOR/NEXT runs a specific number of times. The round counter `n` increments automatically.

**Visual moments:** "Round 2 of 5" updates automatically. "Best: 8" appears in the header. "New best!" flashes in green when you beat your record.

---

### Unit 8: The Results Screen

**Concept:** End-of-game summary, rating tiers, the complete program

After five rounds, clear the screen and show the results: best time and a rating tier. The learner writes the IF/THEN rating logic (familiar from Game 1) and designs their own tier messages.

**What the learner adds:**
- Lines 470-590: results screen with header, best time, rating tiers
- "Too slow!" timeout handling (if the player doesn't press within 500 counts)

**Visual moments:** The results screen with "RESULTS" in bright white, the best time in cyan, and a rating like "Lightning fast!" or "Keep practising!" in colour.

---

**Milestone:** The learner has built a complete game from scratch — not modified an existing one, but written every line. They understand CLS, PAUSE, BEEP, INKEY$, FOR/NEXT, counting in loops, and random delays. They know the difference between INPUT and INKEY$, and they've built a game with five rounds, cheat detection, and a results screen.

---

## Technical Notes

### Key Variables

```
n   - current round number (1-5)
w   - wait duration in frames (random)
t   - reaction time counter
b   - best (lowest) time across rounds
```

### Line Numbering

- 1-72: Title animation (red fill, countdown digits, GO!)
- 74-92: Game title screen (press any key)
- 100-450: Game logic (rounds, timing, scoring)
- 460-610: Results screen
- 5100-5135: Digit DATA (reused from Lucky Number, digits 1-3 only)
- 8000-8080: Digit renderer subroutine

### Memory

Under 2 KB. Comfortable on a 48K Spectrum.

### Spectrum-Specific Notes

- INKEY$ returns a single character if a key is held, or `""` if no key is pressed. It does not wait.
- PAUSE N waits for N frames (1/50th second each). PAUSE also ends early if a key is pressed — this matters for cheat detection (the wait loop uses `PAUSE 1` per iteration, not a single long PAUSE, so INKEY$ can check between frames).
- BEEP duration is in seconds, pitch is in semitones from middle C. Range: -60 to 69.
- The debounce pattern (lines 430-440) waits for the key to be released before waiting for a new press. Without this, the reaction keypress would immediately skip the "Press any key..." prompt.

### Pedagogical Notes

Game 2 is the first game built from scratch. The learner writes every line — but the program is runnable from Unit 1 onwards. Each unit adds a visible feature. This is different from Game 1's "type first, understand later" approach: here the learner understands everything they write, with the exception of the title animation block (which uses FOR/NEXT and DATA/GO SUB from later games).

FOR/NEXT appears in Unit 7 for the round loop. This is ahead of Game 3 (where FOR/NEXT is formally introduced), but in a controlled context: `FOR n=1 TO 5` is simple enough to explain as "do this five times" without a deep dive into the concept. The formal exploration comes in Game 3.

---

## Changelog

- **v2.0 (2026-03-16):** Rewritten for visual-first, build-incrementally approach. Added title animation with countdown digits. Expanded from ~25 to ~65 lines. Added FOR/NEXT in Unit 7 (ahead of formal introduction in Game 3).
- **v1.0 (2026-03-13):** Initial game outline for v5.0 curriculum. ~25 lines, build from scratch.
