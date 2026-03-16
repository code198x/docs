# Game 01: Lucky Number

**Track:** Spectrum BASIC
**Genre:** Number guessing game
**Units:** 8
**Language:** Sinclair BASIC
**Max lines:** ~100 (starter program), ~20 understood by end

---

## Premise

The computer picks a number between 1 and 100. You guess. The computer tells you higher or lower. Keep guessing until you find it.

This is the very first program the learner encounters. They have never programmed before. But their first experience of the Spectrum isn't `10 PRINT "Hello"` on a blank screen — it's typing in a complete, visually impressive game and watching it come alive. A rainbow title screen. Big block-pixel letters. A temperature bar that shifts from blue to white. Sound effects. A victory celebration.

The learner types in the full program before they understand any of it. This mirrors how millions of children first encountered programming in the 1980s: type-in listings from magazines. You typed the lines, you ran the program, you marvelled at the result, and then — slowly — you started to understand how it worked.

Over the eight units that follow, the learner takes the program apart. Each unit focuses on one concept: what PRINT does, what a variable holds, how IF/THEN makes decisions. The visual subroutines (the rainbow cascade, the block-pixel fonts, the temperature bar) remain black boxes for now. They're magic. The learner will understand them in later games as each technique is formally introduced. What matters here is the game logic: the guess, the comparison, the loop.

By the end of Game 1, the learner understands variables, input, decisions, and loops. They can modify the game — change the range, tweak the messages, adjust the scoring. And they've had the experience of typing something in and seeing something extraordinary happen. That's the hook.

---

## Core Mechanics

The player types a number. The program compares it to a secret number and prints "Too high", "Too low", or "You got it!" The game loops until the player guesses correctly. The secret number is random each time. A temperature bar shows how close the guess is. The current guess is displayed as large block-pixel digits. Border colour shifts with distance. Sound effects punctuate every guess and celebrate a win.

---

## The Starter Program

The learner types in a ~100-line program in Unit 1. This program includes:

- **Title screen:** Rainbow cascade (rows 0-7 in ascending PAPER colours), block-pixel "LUCKY NUMBER" rendered from DATA strings, "Press any key" prompt with FLASH.
- **Game screen:** Header bar in PAPER 1, guess counter, temperature bar (blue→yellow→red→white), large block-pixel digit display of the current guess, border colour feedback, directional hints.
- **Win screen:** Border strobe celebration, ascending BEEP tones, green colour flood across the temperature bar, guess count and scoring tier message, play again prompt.
- **Subroutines:** Digit renderer at line 8000 (draws a 4×5 block-pixel digit from DATA), number renderer at 8200 (centres 1-3 digit numbers on screen). These are black boxes — the learner types them in but doesn't need to understand them yet.
- **DATA statements:** Block-pixel font patterns for "LUCKY" and "NUMBER" (lines 5000-5015), digit patterns 0-9 (lines 5100-5195).

The program uses concepts from across the first six games: FOR/NEXT, PRINT AT, INK/PAPER/BORDER/BRIGHT, BEEP, DATA/READ/RESTORE, GO SUB/RETURN. None of these are formally taught in Game 1. They arrive via the starter program and are understood later, each in the game that introduces them properly.

The game logic — the part the learner will understand by Unit 8 — is roughly 20 lines buried within the larger program. Everything else is visual scaffolding.

---

## Unit Breakdown

| Unit | Title | What the learner builds | New concepts |
|------|-------|------------------------|--------------|
| 1 | The Magic Program | Type in the full Lucky Number program. This is a type-in experience — follow the listing, line by line. RUN it. Play it. See the rainbow cascade, hear the sounds, watch the big digits appear. The first experience of the Spectrum is something worth showing to a friend. | What a program is, line numbers, the Spectrum keyboard (K-mode and L-mode), RUN |
| 2 | What Just Happened? | Strip everything away. New program: `10 PRINT "Hello"`. One instruction, one result. Add a second PRINT line. Change the message. Understand that programs are instructions executed in order. Back to Lucky Number: find the PRINT lines. They're everywhere — that's how the game talks to you. | PRINT, strings, how line numbers control order |
| 3 | Remembering Things | `LET n = 42` then `PRINT n`. The computer remembered a number. `LET n$ = "Alex"` then `PRINT n$`. It remembered text. Back to Lucky Number: find `LET n = INT(RND*100)+1`. That's where the secret number lives. Change it to `LET n = 50`. RUN. Now you know the answer — the game still works, but you can predict it. | LET, numeric variables, string variables |
| 4 | Asking the Player | `INPUT "What is your name? "; n$`. The program stops and waits. Whatever the player types goes into the variable. Back to Lucky Number: find the INPUT line. That's how the game asks for your guess. Without INPUT, the game can't interact. | INPUT, prompts |
| 5 | Making Decisions | `IF g = n THEN PRINT "You got it!"` — if the guess matches the number, something happens. `IF g < n` — too low. `IF g > n` — too high. These three lines are the heart of Lucky Number. Find them in the listing. This is how the game knows what to tell you. | IF/THEN, `=`, `<`, `>` comparisons |
| 6 | Going Round Again | `GO TO 400` — jump back and ask again. Without this, the game asks once and stops. With it, the game keeps asking until you get it right. Find the GO TO in Lucky Number. This is the loop that makes it a game. Add REM comments to mark the sections you now understand. | GO TO, loops, REM |
| 7 | A Different Number Every Time | `LET n = INT(RND * 100) + 1`. RND gives a random decimal. Multiply by 100, take INT, add 1: a random whole number from 1 to 100. Remove the `LET n = 50` from Unit 3. Now the game surprises you again. | RND, INT |
| 8 | Making It Yours | The learner now understands the game logic: INPUT asks, IF/THEN decides, GO TO loops, RND randomises. Modify the game: change the range to 1-50 or 1-200. Change the feedback messages. Adjust the guess counter thresholds ("Incredible!" for under 5). Experiment with the visual parts — change a PAPER colour, alter a BEEP pitch. You don't need to understand the subroutines to tinker with them. | Counting with variables, combining strings and numbers in PRINT, experimentation |

**Milestone:** The learner has typed in, run, and partially understood a complete interactive program. They know variables, input, decisions, and loops — the building blocks of every program that follows. And their very first Spectrum program was something that looked and sounded like a real game.

---

## Technical Notes

### Key Variables

```
n   - the secret number (overridden to 50 in unit 3, restored to random in unit 7)
g   - the player's guess
c   - guess counter
d   - distance from correct answer (ABS(g-n))
h   - heat bar length
pc  - PAPER colour for digit renderer
v   - value to display as big digits
dr  - display row for digit renderer
dc  - display column for digit renderer
f   - digit value (0-9) for single digit renderer
```

### The Subroutine Black Boxes

The starter program contains two subroutines the learner doesn't need to understand in Game 1:

- **Line 8000 (Draw digit):** Takes a digit value `f` and screen position `dr`, `dc`, reads 5 rows of DATA for that digit, prints PAPER-coloured spaces where the pattern has a "1". Each digit is 4 columns × 5 rows.
- **Line 8200 (Draw number):** Takes a number `v`, clears the display area, splits into digits, centres them on screen, calls the digit renderer for each.

These subroutines use FOR/NEXT (Game 3), PRINT AT (Game 4), DATA/READ/RESTORE (Game 5), and GO SUB/RETURN (Game 6). Each concept is formally introduced in the game listed. Until then, the subroutines are magic that works.

### Line Numbering

- 1-9: Setup (BORDER, PAPER, INK, CLS)
- 10-60: Rainbow cascade (title screen)
- 70-220: Block-pixel title rendering from DATA
- 230-240: "Press any key" prompt
- 250-680: Game logic (the part the learner understands by Unit 8)
- 700-930: Win screen and play again
- 5000-5015: Title font DATA ("LUCKY", "NUMBER")
- 5100-5195: Digit font DATA (0-9)
- 8000-8080: Digit renderer subroutine
- 8200-8440: Number renderer subroutine

### Memory

~3 KB including DATA statements and subroutines. Comfortable on a 48K Spectrum.

### Spectrum-Specific Notes

- The Spectrum 48K has no ELSE keyword. Each comparison needs its own IF/THEN line.
- The K-mode cursor (keyword mode) appears when the Spectrum expects a command. The learner needs to understand this before they can type their first line. Unit 1 addresses this directly as part of the type-in experience.
- `GO TO` is two words on the Spectrum, not `GOTO`.
- The type-in experience in Unit 1 should include guidance on common mistakes: missing spaces, wrong mode (K vs L), mistyped line numbers. Typing errors are part of the learning.

### Pedagogical Notes

The "type first, understand later" approach mirrors the magazine type-in culture of the 1980s. Research on worked examples (Sweller, 1988) supports studying complete solutions before constructing new ones — the learner builds a mental model from the whole before tackling the parts.

The risk is that 100 lines feels overwhelming. Mitigation: the type-in is guided step by step, with checkpoints ("type lines 1-60, then RUN — you should see the rainbow"). The learner sees progress before they've finished typing. If something goes wrong, they can RUN what they have so far and compare.

The visual subroutines must NOT be explained in Game 1. Premature explanation would overload the learner and steal the teaching moment from the later game where each concept is properly introduced. The correct response to "how does the rainbow work?" is "we'll get to that — for now, it's magic."

---

## Changelog

- **v2.0 (2026-03-16):** Rewritten for starter-kit approach. The learner types in a complete visual program first, then learns the game logic over 8 units. Visual subroutines are black boxes understood in later games.
- **v1.0 (2026-03-13):** Initial game outline for v5.0 curriculum. 20-line text-only program.
