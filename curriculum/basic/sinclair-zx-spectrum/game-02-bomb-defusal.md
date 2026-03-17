# Game 02: Bomb Defusal

**Track:** Spectrum BASIC
**Genre:** Timed decision game
**Units:** 8
**Language:** Sinclair BASIC
**Final size:** ~120 lines (including digit renderer subroutines)

---

## Premise

A bomb is ticking. A big block digit counts down in the centre of the screen — white when safe, yellow in danger, red when time is almost up. A fuse burns across the middle of the screen, shrinking each second with a red spark at the burning end. Four coloured wires run across the bottom: blue, red, green, yellow. Press 1, 2, 3, or 4 to cut a wire. Cut the right one and the bomb is defused — green border, ascending jingle. Cut the wrong one and it explodes — border strobe, descending buzz, and the correct wire is revealed. Five bombs, each one faster.

The game reuses the block-pixel digit renderer from Lucky Number — the learner recognises the big digits from Game 1, now counting down instead of displaying a guess. Some subroutines are magic (the digit renderer, the digit DATA). Others the learner writes themselves (the fuse, the wires, the countdown, the input loop). The game teaches CLS, PAUSE, BEEP, INKEY$, and PRINT AT through a program that's genuinely tense to play.

---

## Core Mechanics

Each bomb:
1. Pick a random correct wire (1-4)
2. Set the timer based on the bomb number (bomb 1 = 9 seconds, bomb 5 = 3 seconds)
3. Draw the game screen: header bar, wires, fuse
4. Countdown loop: draw big digit, shorten fuse, advance spark, play tick BEEP, check INKEY$
5. If a valid key is pressed: check against correct wire. Defused or BOOM.
6. If the timer reaches 0: BOOM (time ran out)
7. After 5 bombs: results screen with animated count-up and rating

### The Countdown

The big digit uses the renderer from Game 1 — a subroutine that reads pixel patterns from DATA and draws them as coloured blocks. The digit changes colour as time runs out: white (safe) → yellow (danger) → red (critical). The border matches.

### The Fuse

A thick yellow bar (2 rows of PAPER 6) that shrinks each tick. A cycling red spark character (`x`, `+`, `x`, `-`) sits at the burning end, advancing leftward as the fuse shortens. When the fuse is gone, the bomb explodes.

### The Wires

Four coloured bars, each 2 rows tall, numbered 1-4. The player presses a number key (checked with INKEY$). On defusal, a green marker appears next to the correct wire. On explosion, a red X marks the wrong choice and the correct wire flashes green.

---

## Unit Breakdown

| Unit | Title | What the learner builds | New concepts |
|------|-------|------------------------|-------------|
| 1 | The Game Screen | Black background, red header bar with PRINT AT, "Bomb 1 of 5" and "Score: 0". The screen looks like a game from the first line. The digit renderer subroutine and DATA are provided as a type-in block. | CLS, BORDER, PAPER, INK, PRINT AT for layout |
| 2 | Four Wires | Draw four coloured bars across the bottom of the screen using PRINT AT with PAPER. Each wire is 2 rows tall and labelled 1-4. The learner chooses the colours. | PRINT AT with PAPER for coloured blocks, screen as a canvas |
| 3 | The Countdown | A FOR loop counts down from 9 to 0. Each tick draws the big digit using GO SUB to the renderer, with a brief PAUSE. The digit appears and changes each second. The countdown is visible but there's no input yet. | PAUSE for timing, GO SUB to the digit renderer (partial understanding) |
| 4 | Tick Tick Tick | Add BEEP to each tick — short, rising in pitch as time runs out. Add border colour changes: black when safe, yellow in danger, red when critical. The countdown now has rhythm and tension. | BEEP (duration, pitch), border as atmosphere |
| 5 | Cut a Wire | Add INKEY$ inside the countdown loop. When the player presses 1, 2, 3, or 4, the countdown stops and the game checks the answer. If correct: green border, "DEFUSED!" If wrong: red border, "BOOM!" The game is playable. | INKEY$ for instant input, OR for combining checks, VAL to convert string to number |
| 6 | The Fuse | Draw a thick yellow bar (PAPER 6) between the digit and the wires. Each tick, the bar shrinks by one column. A red spark character cycles at the burning end. When the timer hits 0, the fuse is gone and the bomb explodes. | Shrinking visual elements, character cycling for animation |
| 7 | Five Bombs | Wrap everything in a FOR loop. Each bomb picks a random correct wire with RND. The timer gets shorter each round (bomb 1 = 9 seconds, bomb 5 = 3 seconds). Score tracks defusals. The header updates each round. | FOR/NEXT for rounds, RND for the correct wire, difficulty scaling |
| 8 | The Finished Game | Title screen with instructions and "5 bombs. Each one faster." in red. Results screen with animated score count-up and rating tiers. Border strobe on explosion. Cleanup. | Title/results screens, rating tiers, explosion effects, program structure |

**Milestone:** The learner can place text anywhere on screen, control timing with PAUSE, create sound with BEEP, and read the keyboard instantly with INKEY$. They've used subroutines from Game 1 in a new context — the same digit renderer, a different game. The Spectrum is alive: it reacts, it has rhythm, and things happen in time.

---

## Technical Notes

### Key Variables

| Variable | Purpose |
|----------|---------|
| `b` | Current bomb number (1-5) |
| `w` | Correct wire number (1-4, random) |
| `t` | Timer start value (seconds) |
| `c` | Current countdown value |
| `k$` | Player's keypress |
| `g` | Wire number chosen (VAL k$) |
| `sc` | Score (bombs defused) |
| `y` | Row for wire markers |
| `fl` | Fuse length (columns remaining) |
| `pc` | Digit colour (7=white, 6=yellow, 2=red) |
| `z$` | Spark character cycle string |
| `si` | Spark character index |

### The Digit Renderer (Subroutine)

Lines 8000-8250 draw a single block-pixel digit at a given row and column. The digit pattern is read from DATA at lines 5100-5195 (10 digits, 5 rows each, 4 columns wide). The variable `pc` controls the PAPER colour.

This is a "half-open" black box. The learner types it in and uses it via GO SUB, but unit 3 explains the principle: "The subroutine reads a pattern from DATA — rows of dots and ones — and prints a coloured space wherever there's a one. Each digit has its own pattern. The line `RESTORE 5100+f*10` jumps to the right pattern for digit `f`."

### Timer Formula

`LET t = 11 - b * 2` gives: bomb 1 = 9, bomb 2 = 7, bomb 3 = 5, bomb 4 = 3, bomb 5 = 1. Minimum clamped to 3 (`IF t < 3 THEN LET t = 3`) so bomb 5 is still playable.

### INKEY$ Inside a Timed Loop

The countdown loop runs `FOR c = t TO 0 STEP -1`. Inside each tick, after drawing the digit and fuse, a secondary loop runs 6 iterations checking INKEY$. This gives the player ~6 chances per tick to press a key. If a valid key is detected, execution jumps out of both loops to the wire-checking code.

### Fuse Length Formula

`LET fl = INT(16 * c / t)` — proportional to time remaining. At the start (`c = t`), the fuse is 16 columns. At `c = 0`, it's 0. Minimum clamped to 1 so the spark always has somewhere to sit.

### Spark Animation

The string `z$` holds four characters that cycle: `x+x-`. The index `si = (c - INT(c/4)*4) + 1` selects one character per tick, creating a flickering effect at the burning end of the fuse. Printed in INK 2 (red) with BRIGHT 1.

### Line Numbering

- 1-5: Initialisation
- 10-34: Title screen
- 36-90: Bomb setup, wires, fuse
- 92-152: Countdown loop (digit, fuse, border, tick, input)
- 154-174: Time ran out (explosion)
- 180-218: Wire cut (wrong/defused)
- 230-252: Next bomb, results loop
- 260-306: Results screen
- 5100-5195: Digit DATA
- 8000-8250: Digit renderer subroutines

---

## Changelog

- **v3.0 (2026-03-17):** Complete rework. Renamed from Countdown to Bomb Defusal. Big block digits, burning fuse, coloured wires, explosion strobe. Reuses Game 1 digit renderer. PRINT AT moved to Game 2. Prototype tested in Emu198x.
- **v2.0 (2026-03-16):** Added title animation, build-incrementally approach.
- **v1.0 (2026-03-13):** Initial reaction timer outline.
