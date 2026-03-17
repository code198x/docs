# Game 05: Word Scramble

**Track:** Spectrum BASIC
**Genre:** Word puzzle
**Units:** 8
**Language:** Sinclair BASIC
**Final size:** ~80 lines

---

## Premise

A scrambled word appears on screen, each letter on its own blue tile. The letters are all there, just in the wrong order. Type the correct word and the tiles turn green. Get it wrong and the answer is revealed in red, letter by letter. Ten rounds, words getting longer. Final score with a rating.

The words come from `DATA` statements — a built-in word list that the learner writes themselves. The scrambling algorithm picks characters from random positions in the original word and assembles them into an anagram. Each round, the word gets longer (and harder to unscramble).

This is the game where strings stop being simple labels and become things you can take apart, rearrange, and stick back together. Spectrum BASIC's string slicing syntax (`a$(2 TO 4)`) is unlike any other language, and this game makes it intuitive.

---

## Core Mechanics

Each round:
1. `READ` the next word from `DATA` into `w$`
2. Scramble `w$` into `s$` by repeatedly extracting a random character and appending it to a new string
3. Display the scrambled word on blue tiles with animated letter reveal
4. `INPUT` the player's guess into `g$`
5. Compare: `IF g$ = w$` turns tiles green with a victory jingle; otherwise, tiles show the correct answer in red, letter by letter
6. After ten rounds, display the final score with an animated count-up and a rating

### Scrambling Algorithm

Start with the original word in a temporary variable `t$`. Pick a random position `p` within `t$`, append `t$(p TO p)` to the scrambled string `s$`, then remove that character from `t$` by joining the parts before and after it. Repeat until `t$` is empty. If the scramble matches the original, scramble again.

Removing a character: `LET t$ = t$(1 TO p-1) + t$(p+1 TO LEN t$)`. This shrinks `t$` by one character each iteration. When `t$` is empty, the scramble is complete.

### Word List

Ten words stored in `DATA`, ordered by length:

```basic
900 DATA "cat","sun","bird","fish","lemon"
910 DATA "planet","castle","trumpet","dinosaur","adventure"
```

Short words (3 letters) have fewer possible arrangements and are easier to unscramble. Longer words (9 letters) are genuinely challenging. The learner is encouraged to replace these with their own words.

---

## Unit Breakdown

| Unit | Title | What the learner builds | New concepts |
|------|-------|------------------------|-------------|
| 1 | Words in Variables | The game screen with a red header bar, then a hardcoded word stored in `w$` and printed at a specific position. A second variable `g$` holds another word. Compare them with `IF`. The screen looks like a game from the first line — black background, coloured header, positioned text. | String variables (`w$`, `g$`), string comparison |
| 2 | How Long Is a Word? | Blue tiles appear on screen — one tile per letter. `LEN w$` controls how many tiles to draw and where to centre them. Change the word and the tiles change. The learner sees `LEN` as a visual tool, not an abstract function. | `LEN`, using `LEN` to control loops and layout |
| 3 | Letters on Tiles | Extract individual characters with `w$(1 TO 1)`, `w$(2 TO 2)`. A `FOR` loop places each character on its tile, one at a time, with an ascending `BEEP`. The animated letter reveal — the game's signature visual moment. | String slicing (`a$(n TO n)`), character-by-character display |
| 4 | Building New Words | Join strings with `+`. Build a word character by character in a loop. Reverse a word by looping backwards — the reversed word appears on the tiles letter by letter. Concatenation is the other half of slicing: taking apart and putting back together. | String concatenation (`+`), building strings in loops |
| 5 | The Scrambler | The full scramble algorithm. Copy `w$` into `t$`. Pick a random position, append that character to `s$`, remove it from `t$`, repeat. Display the scrambled result on the tiles. Add a safety check: if the scramble matches the original, scramble again. | Removing a character from a string, the full scramble algorithm, `RND` with `LEN` |
| 6 | Guess and Check | `INPUT` takes the player's guess. If correct: tiles turn green (`PAPER 4`), border flashes green, ascending jingle. If wrong: "Wrong!" in red, then the correct answer is revealed on the tiles letter by letter in red with ascending `BEEP`. The two paths look and sound completely different. | `INPUT` for strings, colour feedback, border as feedback, in-place tile colour changes |
| 7 | Word List | `DATA` stores ten words. `READ w$` pulls the next one. A `FOR` loop runs ten rounds: read, scramble, display, guess, check, track score. The header bar shows the round number and running score. Each round is a complete play of what the learner built in units 1-6. | `DATA`, `READ`, `FOR` loop as game structure, score tracking |
| 8 | The Finished Game | Title screen with instructions and colour-coded difficulty hint. Results screen with animated score count-up and rating tiers (colour-coded: green for perfect, yellow for good, cyan for decent, magenta for "keep practising"). Cleanup to reset colours. The complete arc: title, play, results. | Title and results screens, rating tiers, animated score display, program structure |

**Milestone:** The learner can manipulate strings — slicing, concatenating, measuring — and store data in the program with `DATA`/`READ`. Every new concept had a visual payoff on the same screen.

---

## Technical Notes

### Key Variables

| Variable | Purpose |
|----------|---------|
| `w$` | The current word (correct answer) |
| `s$` | The scrambled version |
| `g$` | The player's guess |
| `t$` | Temporary copy used during scrambling |
| `p` | Random position within `t$` |
| `c` | Starting column for centred tiles |
| `sc` | Score (correct answers) |
| `n` | Current round (1-10) |

### Visual Design

The game uses blue tiles (`PAPER 1`) as letter holders — two rows tall, spaced two columns apart, centred on screen. Letters appear in bright yellow (`INK 6; BRIGHT 1`) on the tiles.

On a correct answer, tiles change to green (`PAPER 4`) with white letters and the border flashes green. On a wrong answer, the correct letters are revealed in bright red (`INK 2; BRIGHT 1`) on the blue tiles, one at a time with ascending pitch.

The header bar (`PAPER 2`, red) spans row 0 with the round number left-aligned and the score right-aligned in yellow.

### Tile Centring Formula

Each letter occupies 2 columns (letter + gap). For a word of length `L`, the starting column is `(32 - L*2) / 2`. The tile at position `i` (1-indexed) is at column `c + i*2 - 2`.

### String Slicing on the Spectrum

Sinclair BASIC uses `a$(start TO end)` for substrings, not `MID$`/`LEFT$`/`RIGHT$`. Positions are 1-indexed. `a$(3 TO 3)` extracts one character at position 3. `a$(1 TO p-1)` extracts everything before position `p`.

Edge case: if `p` is 1, then `a$(1 TO 0)` returns an empty string — this is valid on the Spectrum and doesn't cause an error. Similarly, `a$(p+1 TO LEN a$)` when `p` equals `LEN a$` also returns an empty string safely.

### Line Numbering

- 1-5: Initialisation
- 10-36: Title screen
- 38-58: Scramble algorithm
- 60-96: Round display (header, tiles, animated reveal)
- 100-130: Wrong answer path (feedback, reveal, border flash)
- 140-164: Correct answer path (green tiles, jingle, border flash)
- 170-172: Next round
- 180-228: Results screen (animated count-up, rating, cleanup)
- 900-910: DATA statements (word list)

### No ELSE on the 48K

Checking the guess uses two separate `IF` statements rather than `IF/ELSE`:

```basic
102 IF g$ = w$ THEN GO TO 140
104 REM === Wrong path follows ===
```

The `GO TO 140` after a correct answer skips the "wrong" block. This is the same pattern used in Game 4 for the distance-to-colour chain.

### Lowercase Words

Words are stored in lowercase in `DATA`. The Spectrum's `INPUT` returns whatever case the player types. Since most players type in lowercase (the default mode), this avoids case-mismatch frustration. The learner can discuss case sensitivity as a "Try This" extension.

---

## Changelog

- **v2.0 (2026-03-17):** Complete rework for visual progression. Blue letter tiles, animated reveal, green/red tile colour changes, border flash feedback, centred layout, animated score count-up. Prototype tested in Emu198x.
- **v1.1 (2026-03-16):** Added animated letter reveal per visual progression plan.
- **v1.0 (2026-03-13):** Initial game outline for v5.0 curriculum.
