# Game 04: Hot and Cold

**Track:** Spectrum BASIC
**Genre:** Grid search game
**Units:** 8
**Language:** Sinclair BASIC
**Max lines:** ~30

---

## Premise

A treasure is hidden somewhere on screen. You don't know where. All you have is a cursor and the border colour, which shifts from blue (freezing cold) through red (warm) to white (scorching hot) as you get closer.

The player moves a marker around the screen with keys, watching the border change. When the cursor lands on the hidden square, the treasure is revealed and the round ends. Play five rounds, each with a new hiding spot, and the program counts how many moves it took you altogether.

This is the game where `PRINT AT` arrives. Everything before this used sequential output — text scrolling down the screen. From here on, the learner places things exactly where they want them.

---

## Core Mechanics

The screen is a 22×32 grid (rows 0-21, columns 0-31 — row 22 is reserved for the status line, row 23 for input). A treasure position is chosen at random. The player's cursor starts at the centre.

Each frame of the game loop:
1. **Read input** — check `INKEY$` for Q/A/O/P (up/down/left/right)
2. **Update state** — adjust the cursor's row or column
3. **Draw** — erase the old cursor position, print the cursor at the new position, set the border colour based on distance

Distance is calculated as `ABS(r - tr) + ABS(c - tc)` where `r`,`c` is the cursor and `tr`,`tc` is the treasure. This Manhattan distance maps to border colours:

| Distance | Border colour | Meaning |
|----------|--------------|---------|
| 0 | White (7) | Found it |
| 1-3 | Yellow (6) | Burning hot |
| 4-7 | Red (2) | Warm |
| 8-14 | Magenta (3) | Getting warmer |
| 15-24 | Blue (1) | Cold |
| 25+ | Black (0) | Freezing |

When the cursor reaches the treasure square, the treasure character appears, a celebratory `BEEP` plays, and the next round begins.

---

## Unit Breakdown

| Unit | Title | What the learner builds | New concepts |
|------|-------|------------------------|-------------|
| 1 | Placing Text | Title screen with `PRINT AT`. Place the game name at the top centre and instructions in the middle. Experiment with positioning text at specific rows and columns. | `PRINT AT row, col`, the coordinate grid (row 0-23, col 0-31) |
| 2 | The Cursor | A character (`"+"`) printed at a position stored in variables `r` and `c`. Change the variables and re-run to see it move. Then: a loop that waits for a keypress and moves the cursor down one row each time. | Variables for position (`r`, `c`), `LET r = r + 1` to update position |
| 3 | Four Directions | Q moves up (`LET r = r - 1`), A moves down, O moves left (`LET c = c - 1`), P moves right. The cursor moves freely around the screen. The old position is erased by printing a space there first. | Four-direction movement, erasing by overwriting with `" "` |
| 4 | Staying on Screen | The cursor must not leave the playing area. If `r < 0` then `LET r = 0`. Same for all four edges. Introduce `<=` and `>=` as comparisons — the cursor stops at the boundary rather than wrapping or crashing. | `<=`, `>=`, `<>`, boundary checking |
| 5 | The Hidden Treasure | A random position is chosen at the start: `LET tr = INT(RND * 22)` and `LET tc = INT(RND * 32)`. Nothing visible yet — the treasure is hidden. Print a message when `r = tr` and `c = tc`: "You found it!" | Random target position, combining two conditions |
| 6 | Hot and Cold | Calculate distance: `LET d = ABS(r - tr) + ABS(c - tc)`. Use `IF d < 4 THEN BORDER 6` and similar lines for each colour band. The border shifts as the player moves — blue when far, red when close, white when found. | `ABS`, distance calculation, the game loop pattern (read input, update state, draw) |
| 7 | Rounds and Score | Five rounds. A `FOR` loop wraps the game. A `moves` counter increments each time the player presses a key. After five rounds, display total moves. Fewer moves means a better score. | `FOR`/`NEXT` wrapping a game, move counter, end-of-game summary |
| 8 | Polish | Clear the screen between rounds. Show the round number (`"Round 3 of 5"`) and moves so far at the bottom of the screen. A short `BEEP` sequence when the treasure is found. `BRIGHT 1` on the cursor so it stands out. The finished game. | `CLS` between rounds, status display with `PRINT AT 22, 0`, `BEEP` for feedback |

**Milestone:** The learner can place text anywhere on screen, move a character with keyboard input, and build a complete game loop. `PRINT AT` is now second nature.

---

## Technical Notes

### Key Variables

| Variable | Purpose |
|----------|---------|
| `r` | Cursor row (0-21) |
| `c` | Cursor column (0-31) |
| `tr` | Treasure row |
| `tc` | Treasure column |
| `d` | Distance (Manhattan) |
| `m` | Move counter |
| `n` | Current round |

### Line Numbering

- 10-20: Initialisation (set starting position, random treasure)
- 30-40: Title and round display
- 50-90: Main game loop (read input, update, draw, check distance)
- 100-120: Found treasure — beep, next round
- 130-150: End of game — total score

### No ELSE on the 48K

The Spectrum 48K has no `ELSE`. Distance-to-colour mapping uses a chain of `IF/THEN` statements. Each one sets `BORDER` and then uses `GO TO` to skip the rest:

```basic
60 IF d < 4 THEN BORDER 6: GO TO 80
65 IF d < 8 THEN BORDER 2: GO TO 80
70 IF d < 15 THEN BORDER 3: GO TO 80
75 BORDER 1
80 REM continue
```

This pattern — testing the smallest range first and jumping past the remaining checks — is the standard replacement for `IF/ELSE IF/ELSE` on the 48K.

### Screen Limits

The playing area uses rows 0-21 and columns 0-31. Row 22 is the status line. Row 23 is left empty — printing to the bottom-right cell (row 23, column 31) causes the screen to scroll, which must be avoided.

---

## Changelog

- **v1.0 (2026-03-13):** Initial game outline for v5.0 curriculum.
