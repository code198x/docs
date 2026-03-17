# Game 06: Quiz Master

**Track:** Spectrum BASIC
**Genre:** Multiple-choice quiz with categories
**Units:** 8
**Language:** Sinclair BASIC
**Final size:** ~90 lines

---

## Premise

A quiz game with multiple-choice questions. Each question appears on a formatted card: the category in bright colour at the top, the question below, and four options labelled A-D. The player presses a single key — no Enter needed. Right answers flash green with an ascending jingle. Wrong answers flash red and reveal the correct option in green.

Eight questions from four categories (Science, History, Geography, Entertainment). After all questions, a results screen shows the total score, a breakdown by category with colour-coded labels, and a rating.

This is the last Foundations game. After this, the learner has every basic tool: variables, strings, arrays, loops, decisions, input, colour, sound, screen positioning, data storage, and reusable subroutines. The Skills phase begins with Game 7, where these tools combine into real-time games.

---

## Core Mechanics

Each round:
1. `READ` the category index, question, four options, and correct answer letter from `DATA`
2. `GO SUB` to draw the question card — header bar, category label, question, options
3. Wait for the player to press A, B, C, or D (using `INKEY$` with `AND`)
4. Compare the keypress to the correct answer
5. Show feedback — green `>` marker and border flash for correct, red `>` for wrong with green `>` on the correct option
6. Update the overall score and the category score array

After all questions, display a results screen: animated score count-up, category breakdown with colour-coded labels, and a rating tier.

### Question Data Format

Each question uses one `DATA` line with seven values:

```basic
500 DATA 1,"Closest planet to the Sun?","Mercury","Venus","Earth","Mars","a"
```

Category index (1-4), question text, options A-D, correct answer letter (lowercase).

### Categories and Scoring

Four categories tracked with `DIM s(4)`:
- `s(1)` = Science (yellow)
- `s(2)` = History (magenta)
- `s(3)` = Geography (green)
- `s(4)` = Entertainment (cyan)

When the player answers correctly, the matching element increments: `LET s(p) = s(p) + 1`.

### Input

The game uses `INKEY$` in a loop rather than `INPUT`, so the player presses a single key without needing to hit Enter:

```basic
52 LET k$ = INKEY$
54 IF k$ <> "a" AND k$ <> "b" AND k$ <> "c" AND k$ <> "d" THEN GO TO 52
```

This introduces `AND` for combining conditions.

---

## Unit Breakdown

| Unit | Title | What the learner builds | New concepts |
|------|-------|------------------------|-------------|
| 1 | One Question | The game screen with header bar, a hardcoded question and four options displayed with `PRINT AT`. `INPUT` takes a letter. `IF` checks the answer. Green or red feedback. One question, no DATA — just the core mechanic on a screen that looks like a quiz show. | Reviewing `INPUT`, `IF/THEN`, and screen layout in a quiz context |
| 2 | Questions from DATA | Move the question, options, and answer into a `DATA` statement. `READ` them into variables. Four questions in a `FOR` loop. Score counter. Each round clears and redraws. | `DATA` with multiple values per line, `READ` into multiple variables |
| 3 | Press a Key | Replace `INPUT` with an `INKEY$` loop. The player presses A, B, C, or D — no Enter needed. Ignore any other key. Introduce `AND` to combine the four checks. The response feels instant. | `AND` (combining conditions), `INKEY$` for single-key input |
| 4 | Right and Wrong | Correct: green `>` marker next to the chosen option, border flash green, ascending three-note jingle. Wrong: red `>` marker next to the chosen option, green `>` next to the correct one, border flash red, low buzz. The two paths look and sound completely different. | Visual feedback with `>` markers, border as feedback, two-path feedback |
| 5 | Reusable Drawing | The question display code runs every round: clear screen, draw header bar, print question, draw options. Extract it into a `GO SUB` at line 300. The main loop calls `GO SUB 300` each round. Also extract the key-to-row mapping into `GO SUB 250`. | `GO SUB` / `RETURN`, subroutines as reusable routines |
| 6 | Categories | Add a category index to each `DATA` line. Map the index to a name and colour. Display the category above the question in BRIGHT. Each category has its own colour: Science yellow, History magenta, Geography green, Entertainment cyan. | Category mapping, colour per category |
| 7 | Category Scores | `DIM s(4)` creates an array with four slots — one per category. Correct answers increment the matching slot. The header bar shows the running total. After all questions, print each category with its score. | `DIM` (simple arrays), array indexing (`s(p)`) |
| 8 | The Finished Quiz | Title screen with category colours and instructions. Results screen with animated score count-up, colour-coded category breakdown, and rating tiers. `RESTORE` enables replay. The learner writes their own questions. | Title/results screens, `RESTORE`, rating tiers, program structure |

**Milestone:** The learner has the full BASIC toolkit: variables, strings, arrays, loops, decisions, input, colour, sound, screen positioning, data storage, and reusable subroutines. Foundations complete.

---

## Technical Notes

### Key Variables

| Variable | Purpose |
|----------|---------|
| `q$` | Current question text |
| `a$`, `b$`, `c$`, `d$` | The four options |
| `k$` | The player's keypress |
| `r$` | The correct answer letter |
| `m$` | Temporary string for category name and messages |
| `sc` | Total score |
| `s()` | Category scores (DIM s(4)) |
| `p` | Category index (1-4) |
| `n` | Current question number |
| `y` | Row for option highlighting |
| `ci` | Category ink colour |

### Variable Name Clash

Do NOT use `c$` for the category name — it clashes with option C from `READ`. Use `m$` or another variable for the category display.

### AND for Input Validation

```basic
54 IF k$ <> "a" AND k$ <> "b" AND k$ <> "c" AND k$ <> "d" THEN GO TO 52
```

All four conditions must be true (the key is not A AND not B AND not C AND not D) for the loop to continue waiting. If any condition is false — meaning the key IS one of A/B/C/D — execution falls through.

### DIM and Arrays

`DIM s(4)` creates an array with four elements, indexed 1-4 (Spectrum arrays are 1-indexed). All elements start at zero.

### Line Numbering

- 1-5: Initialisation
- 10-38: Title screen
- 40-56: Game loop, READ, GO SUB, input
- 58-96: Wrong answer path
- 100-124: Correct answer path
- 140: NEXT n
- 150-208: Results screen
- 250-260: Key-to-row mapping subroutine
- 300-344: Question card drawing subroutine
- 500-570: DATA statements (questions)

### Question Length

Questions display at column 4 on a 32-column screen, giving 28 characters before wrapping. Keep questions under 28 characters. Drop "What is the" prefixes — "Closest planet to the Sun?" reads better than "What is the closest planet to the Sun?" anyway.

---

## Changelog

- **v2.0 (2026-03-17):** Complete rework for visual progression. GO SUB for question card and key mapping. Category colours. Animated results. Fixed c$ variable clash. Prototype tested in Emu198x.
- **v1.1 (2026-03-16):** Added GO SUB/RETURN per visual progression plan.
- **v1.0 (2026-03-13):** Initial game outline for v5.0 curriculum.
