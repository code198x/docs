# Game 05: Word Scramble

**Track:** Spectrum BASIC
**Genre:** Word puzzle
**Units:** 8
**Language:** Sinclair BASIC
**Max lines:** ~30

---

## Premise

A scrambled word appears on screen. The letters are all there, just in the wrong order. Type the correct word and score a point. Get it wrong and the answer is revealed. Ten rounds, then your final score.

The words come from `DATA` statements — a built-in word list that the learner writes themselves. The scrambling algorithm picks characters from random positions in the original word and assembles them into an anagram. Each round, the word gets longer (and harder to unscramble).

This is the game where strings stop being simple labels and become things you can take apart, rearrange, and stick back together. Spectrum BASIC's string slicing syntax (`a$(2 TO 4)`) is unlike any other language, and this game makes it intuitive.

---

## Core Mechanics

Each round:
1. `READ` the next word from `DATA` into `w$`
2. Scramble `w$` into `s$` by repeatedly extracting a random character and appending it to a new string
3. Display the scrambled word with `PRINT AT`
4. `INPUT` the player's guess into `g$`
5. Compare: `IF g$ = w$` scores a point; otherwise, show the correct answer
6. After ten rounds, display the final score

### Scrambling Algorithm

Start with the original word in a temporary variable `t$`. Repeat `LEN t$` times: pick a random position `p` within `t$`, append `t$(p TO p)` to the scrambled string `s$`, then remove that character from `t$` by joining the parts before and after it.

Removing a character: `LET t$ = t$(1 TO p-1) + t$(p+1 TO LEN t$)`. This shrinks `t$` by one character each iteration. When `t$` is empty, the scramble is complete.

### Word List

Ten words stored in `DATA`, ordered by length:

```basic
200 DATA "cat","bird","lemon","planet","trumpet","elephant","dinosaur","crocodile","adventure","strawberry"
```

Short words (3-4 letters) have fewer possible arrangements and are easier to unscramble. Longer words (9-10 letters) are genuinely challenging. The learner is encouraged to replace these with their own words.

---

## Unit Breakdown

| Unit | Title | What the learner builds | New concepts |
|------|-------|------------------------|-------------|
| 1 | Words in Variables | Store a word in `w$`. Print it. Store another in `g$`. Print both. Compare them with `IF g$ = w$`. The learner sees that string variables work like numeric ones but hold text. | String variables (`w$`, `g$`), string comparison |
| 2 | How Long Is a Word? | Use `LEN w$` to find the number of characters. Print the word and its length. Try different words. Use `LEN` in a condition: `IF LEN g$ <> LEN w$ THEN PRINT "Wrong length!"` — a quick check before comparing. | `LEN`, using `LEN` in conditions |
| 3 | Taking Words Apart | Extract single characters: `w$(1 TO 1)` is the first letter, `w$(3 TO 3)` is the third. Extract substrings: `w$(2 TO 4)` pulls three letters from the middle. Print each character of a word on a separate line using a `FOR` loop. | String slicing (`a$(start TO end)`), 1-indexed positions |
| 4 | Building Words | Join two strings: `LET r$ = a$ + b$`. Build a word character by character in a loop — start with `r$ = ""`, then `LET r$ = r$ + w$(i TO i)` for each position. Reverse a word by looping backwards. | String concatenation (`+`), building strings in a loop |
| 5 | The Scrambler | Scramble a word. Copy `w$` into `t$`. Pick a random position `p` in `t$`. Append `t$(p TO p)` to `s$`. Remove that character from `t$`. Repeat until `t$` is empty. Display the scrambled result. | Removing a character from a string, the full scramble algorithm |
| 6 | Word List | Store ten words in `DATA` statements. `READ w$` pulls the next word. A `FOR` loop runs ten rounds: read, scramble, display, input guess, check answer, track score. | `DATA`, `READ`, score tracking across rounds |
| 7 | Right and Wrong | When the guess is correct: `BEEP .1, 12` and `INK 4` (green) for "Correct!". When wrong: `BEEP .3, -5` and `INK 2` (red) for "Wrong!" followed by the answer. Show the running score after each round. | Feedback with colour and sound, running score display |
| 8 | The Finished Game | Title screen with instructions. `PRINT AT` for layout — scrambled word centred on screen, guess below, score at the bottom. After ten rounds, a final screen with the score and a rating (0-3: "Keep trying", 4-6: "Not bad", 7-9: "Excellent", 10: "Perfect!"). Option to play again with `RESTORE` and `GO TO`. | `PRINT AT` for layout, end-of-game summary, `RESTORE` (preview — fully taught in Game 6) |

**Milestone:** The learner can manipulate strings — slicing, concatenating, measuring — and store data in the program with `DATA`/`READ`.

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
| `sc` | Score (correct answers) |
| `n` | Current round (1-10) |

### String Slicing on the Spectrum

Sinclair BASIC uses `a$(start TO end)` for substrings, not `MID$`/`LEFT$`/`RIGHT$`. Positions are 1-indexed. `a$(3 TO 3)` extracts one character at position 3. `a$(1 TO p-1)` extracts everything before position `p`.

Edge case: if `p` is 1, then `a$(1 TO 0)` returns an empty string — this is valid on the Spectrum and doesn't cause an error. Similarly, `a$(p+1 TO LEN a$)` when `p` equals `LEN a$` also returns an empty string safely.

### Line Numbering

- 10-20: Initialisation, title screen
- 30-40: Start of round (READ, scramble setup)
- 50-70: Scrambling loop
- 80-100: Display scrambled word, INPUT guess, check answer
- 110-130: Score display, next round
- 140-160: End of game, final score, play again
- 200-210: DATA statements (word list)

### No ELSE on the 48K

Checking the guess uses two separate `IF` statements rather than `IF/ELSE`:

```basic
90 IF g$ = w$ THEN LET sc = sc + 1: INK 4: PRINT "Correct!": GO TO 110
100 INK 2: PRINT "Wrong! It was "; w$
110 REM next round
```

The `GO TO 110` after a correct answer skips the "wrong" line. This is the same pattern used in Game 4 for the distance-to-colour chain.

### Why Not RANDOMIZE?

The scrambler uses `RND` without `RANDOMIZE`. On the Spectrum, `RND` produces a different sequence each time the machine is powered on (unlike some computers where it always starts the same). No seed is needed for this game.

---

## Changelog

- **v1.0 (2026-03-13):** Initial game outline for v5.0 curriculum.
