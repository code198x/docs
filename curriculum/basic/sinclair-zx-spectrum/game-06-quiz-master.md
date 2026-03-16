# Game 06: Quiz Master

**Track:** Spectrum BASIC
**Genre:** Multiple-choice quiz with categories
**Units:** 8
**Language:** Sinclair BASIC
**Max lines:** ~35

---

## Premise

A quiz game with multiple-choice questions. Each question has four options labelled A-D. The player picks a letter. Right answers score a point; wrong answers show the correct option. After all the questions, the final score appears with a rating.

The questions come from `DATA` statements — the learner writes them. Each question has a category (science, history, geography, entertainment), and the game tracks the score per category so the player can see their strengths and weaknesses at the end.

This is the last Foundations game. After this, the learner has every basic tool: variables, strings, arrays, loops, decisions, input, colour, sound, screen positioning, and data storage. The Skills phase begins with Game 7, where these tools combine into real-time games.

---

## Core Mechanics

Each round:
1. `READ` the category, question, four options, and correct answer letter from `DATA`
2. Display the question and options with `PRINT AT`
3. Wait for the player to press A, B, C, or D (using `INKEY$`)
4. Compare the keypress to the correct answer
5. Show feedback — green for correct, red for wrong
6. Update the overall score and the category score

After all questions, display a summary: total score, score per category, and a final rating.

### Question Data Format

Each question uses one `DATA` line with seven values:

```basic
500 DATA "Science","What colour is the sky?","Blue","Green","Red","Yellow","a"
```

Category, question text, options A-D, correct answer letter (lowercase).

### Categories and Scoring

Four categories, tracked with a simple array `DIM s(4)`:
- `s(1)` = Science score
- `s(2)` = History score
- `s(3)` = Geography score
- `s(4)` = Entertainment score

The category name from `DATA` maps to an index (1-4). When the player answers correctly, the matching element increments: `LET s(p) = s(p) + 1`.

### Input

The game uses `INKEY$` in a loop rather than `INPUT`, so the player presses a single key without needing to hit Enter. The loop waits until the keypress is A, B, C, or D — anything else is ignored.

```basic
80 LET k$ = INKEY$
85 IF k$ <> "a" AND k$ <> "b" AND k$ <> "c" AND k$ <> "d" THEN GO TO 80
```

This introduces `AND` for combining conditions — the first time the learner has seen it.

---

## Unit Breakdown

| Unit | Title | What the learner builds | New concepts |
|------|-------|------------------------|-------------|
| 1 | One Question | Hardcode a question and four options. Display them with `PRINT`. Wait for `INPUT` of a letter. Check if it matches the correct answer. Print "Right" or "Wrong". One question, no DATA, no loop — just the core mechanic. | Reviewing `INPUT` and `IF/THEN` in a quiz context |
| 2 | Questions from DATA | Move the question, options, and answer into a `DATA` statement. `READ` them into variables. Add three more questions. A `FOR` loop runs through all four. Score counter increments on correct answers. | `DATA` with multiple values per line, `READ` into multiple variables |
| 3 | Better Display | Use `PRINT AT` to lay out the question neatly: question at the top, options spaced vertically, each labelled A-D. `CLS` between questions. The quiz looks like a quiz now, not scrolling text. | `PRINT AT` for structured layout, `CLS` between screens |
| 4 | Press a Key | Replace `INPUT` with an `INKEY$` loop. The player presses A, B, C, or D — no Enter needed. Ignore any other key. The response feels instant. Introduce `AND` to combine the four checks into one condition. | `AND` (combining conditions), `INKEY$` for single-key input |
| 5 | Right and Wrong | Correct answer: flash the chosen option in green (`INK 4`), play a rising `BEEP`. Wrong answer: flash the chosen option in red (`INK 2`), highlight the correct option in green, play a falling `BEEP`. A one-second `PAUSE` before moving on. | Visual feedback with colour, highlighting the correct answer |
| 6 | Reusable Drawing | The question display code is the same every round: clear the area, print the category header in BRIGHT, draw the question, draw the four options. Extract it into a `GO SUB` at line 400. The main loop calls `GO SUB 400` each round instead of repeating the same PRINT AT lines. | `GO SUB` / `RETURN`, subroutines as reusable drawing routines |
| 7 | Categories and Scores | Add a category field to each `DATA` line. Read it into `c$`. Display the category above the question in BRIGHT. Introduce `DIM s(4)` — an array with four slots, one per category. Map the category name to an index and increment the right slot. | `DIM` (simple arrays), array access (`s(p)`), mapping names to indices |
| 8 | The Finished Quiz | After all questions, display a scoreboard using a second `GO SUB`. Total score at the top. Each category with its score. Use `RESTORE` to allow replaying. Multiple statements on one line with colons. The learner writes their own questions. | `RESTORE`, `OR` (combining conditions), multiple colons, line numbering conventions |

**Milestone:** The learner has the full BASIC toolkit for simple programs: variables, strings, arrays, loops, decisions, input, colour, sound, screen positioning, data storage, and reusable subroutines. Foundations complete.

---

## Technical Notes

### Key Variables

| Variable | Purpose |
|----------|---------|
| `q$` | Current question text |
| `a$`, `b$`, `c$`, `d$` | The four options |
| `k$` | The player's keypress |
| `ans$` | The correct answer letter |
| `cat$` | Current category name |
| `sc` | Total score |
| `s()` | Category scores (DIM s(4)) |
| `p` | Category index (1-4) |
| `n` | Current question number |

### Mapping Category to Index

Without `ELSE`, the mapping uses a chain of `IF/THEN` with `GO TO`:

```basic
70 IF cat$ = "Science" THEN LET p = 1: GO TO 90
72 IF cat$ = "History" THEN LET p = 2: GO TO 90
74 IF cat$ = "Geography" THEN LET p = 3: GO TO 90
76 LET p = 4
90 REM continue
```

An alternative is to store the index as part of the `DATA`:

```basic
500 DATA 1,"What colour is the sky?","Blue","Green","Red","Yellow","a"
```

This avoids the string comparison chain entirely. The unit teaches both approaches — the learner chooses which they prefer.

### AND and OR

`AND` and `OR` combine conditions in `IF` statements:

```basic
85 IF k$ <> "a" AND k$ <> "b" AND k$ <> "c" AND k$ <> "d" THEN GO TO 80
```

On the Spectrum, `AND` and `OR` are also numeric operators (they return 1 or 0), but this game uses them purely as logical connectives. The numeric behaviour is noted but not explored — it's a topic for later games.

### DIM and Arrays

`DIM s(4)` creates an array with four elements, indexed 1-4 (not 0-3 — Spectrum arrays are 1-indexed). All elements start at zero. No need to initialise.

Arrays persist across the program's lifetime. If the player replays, the scores must be reset manually:

```basic
15 FOR i = 1 TO 4: LET s(i) = 0: NEXT i
```

This is placed after `RESTORE` in the replay path.

### Line Numbering

- 10-20: Initialisation (`DIM`, variables, title screen)
- 30-50: Start of round (READ question data, display)
- 60-90: Input loop (wait for A/B/C/D)
- 100-130: Check answer, update score, feedback
- 140-160: Next question or end of quiz
- 170-200: Scoreboard display
- 210-230: Play again prompt, `RESTORE`
- 500-600: `DATA` statements (questions)

### Multiple Statements with Colons

Sinclair BASIC allows multiple statements on one line separated by colons:

```basic
15 LET sc = 0: FOR i = 1 TO 4: LET s(i) = 0: NEXT i
```

This keeps the listing compact. The unit teaches when colons help (grouping related setup) and when they hurt (long game logic that becomes hard to read). A line should be readable at a glance — if it needs a second read, split it.

---

## Changelog

- **v1.1 (2026-03-16):** Added GO SUB/RETURN (moved from Game 7). Unit 6 now teaches reusable drawing subroutines. Unit 7 becomes categories/scores. Unit 8 combines scoreboard, RESTORE, and learner-written questions. Per visual progression plan.
- **v1.0 (2026-03-13):** Initial game outline for v5.0 curriculum.
