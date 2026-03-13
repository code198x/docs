# Game 09: Word Worm

**Track:** Spectrum BASIC
**Genre:** Typing challenge
**Units:** 16
**Language:** Sinclair BASIC
**Max lines:** ~80

---

## Premise

Words fall from the top of the screen. Type them before they reach the bottom. Get it right and the word vanishes. Get it wrong and it keeps falling. Miss three words and the game is over.

It starts gently — short words, slow descent. But the speed creeps up. By level three, five-letter words are dropping at pace. By level five, you're juggling three words on screen at once, fingers hammering the keyboard, eyes flicking between the falling text and your half-typed attempt.

Word Worm teaches the learner to think about strings as sequences of characters, not opaque blocks. Every keypress is checked against the next expected letter. Mistakes are visible — the partial word on screen shows exactly where you went wrong. The game's pressure makes string manipulation visceral: you feel the difference between CHR$ 65 and CHR$ 66 when one saves you and the other doesn't.

---

## Core Mechanics

### Falling Words

Words appear at the top of the screen (row 2) at a random column. Each word descends one row per tick. A tick is N iterations of the game loop — the value of N decreases as the game progresses, making words fall faster.

Multiple words can be on screen simultaneously (up to 3 in later levels). Each word falls independently.

### The Word List

50 words stored in a string array, graded by length:

| Grade | Length | Examples | Levels |
|-------|--------|----------|--------|
| Short | 3-4 letters | cat, jump, fire, gold | 1-2 |
| Medium | 4-5 letters | storm, brick, flame | 3-4 |
| Long | 5-7 letters | thunder, crystal, phantom | 5+ |

Words are common English words — no obscure vocabulary. The learner enters them as DATA statements.

### Typing

The player types the currently active word. Each keypress is captured with INKEY$ and compared to the next expected character. The active word is always the lowest one on screen (closest to the bottom — most urgent).

A typing prompt at the bottom of the screen shows:
- The target word
- Characters typed so far (in green for correct)
- The cursor position

If the player types a wrong character, the character appears in red. Backspace (DELETE key, CHR$ 12) removes the last typed character.

### Completing a Word

When the player types the final correct character, the word vanishes from the screen (erased), a score is added, and the next word becomes the active target. A short rising BEEP confirms the kill.

### Missing a Word

If a word reaches row 20 (the bottom), it's missed:
- The word flashes red briefly
- The miss counter increments
- The word vanishes
- Three misses and the game ends

### Difficulty Progression

| Level | Word grade | Fall speed (ticks per row) | Words on screen | New word delay |
|-------|-----------|---------------------------|-----------------|----------------|
| 1 | Short | 30 | 1 | After current word completed |
| 2 | Short | 25 | 1 | After current word completed |
| 3 | Medium | 20 | 2 | Every 40 ticks |
| 4 | Medium | 15 | 2 | Every 30 ticks |
| 5 | Long | 12 | 3 | Every 25 ticks |

The player advances a level every 10 words completed.

### Scoring

| Event | Points |
|-------|--------|
| Word completed | 10 × word length |
| Streak bonus (5 in a row, no misses) | 50 |
| Level completion | 100 |

---

## Unit Breakdown

| Unit | Title | What the learner builds | New concepts |
|------|-------|------------------------|-------------|
| 1 | The Word List | Create a string array: DIM w$(50,7). Fill it from DATA statements using READ. Print all 50 words to verify they loaded correctly. | String arrays (DIM w$(size, max_length)), DATA/READ for strings, array of strings vs array of numbers |
| 2 | A Falling Word | Pick a random word from the array. Display it at row 2 with PRINT AT. In a loop, erase it (print spaces) and redraw it one row lower each tick. It falls from top to bottom and vanishes. | Timed movement (counter variable), erase-and-redraw for text, PRINT AT with string variables |
| 3 | Fall Speed | Control how fast the word falls. A counter variable increments each loop iteration. When it reaches a threshold, the word moves down one row and the counter resets. Lower threshold = faster fall. | Tick-based timing, speed as a variable, decoupling display from loop speed |
| 4 | Reading Keypresses | Add INKEY$ to the loop. Display each keypress at the bottom of the screen. The loop keeps running — the word keeps falling — whether or not the player types. Input and animation happen in the same loop. | INKEY$ alongside animation, concurrent input and display, game loop with two jobs |
| 5 | Character Matching | Compare the keypress to the next expected character in the target word. Use string slicing: IF k$ = w$(n)(p TO p) where p is the current position. Correct: advance p. Wrong: show the character in red. | String slicing for single characters, character-by-character comparison, position tracking |
| 6 | CHR$ and CODE | Display the character code of each keypress with CODE(k$). Show that "A" is 65, "a" is 97. Convert codes back to characters with CHR$. The learner sees strings as sequences of numbers. | CHR$, CODE, ASCII-like character codes, the relationship between characters and numbers |
| 7 | Building the Input String | As the player types correct characters, build a display string character by character: LET t$ = t$ + k$. Show the growing string at the bottom of the screen in green INK. A visible, growing progress indicator. | String building by concatenation, character-by-character construction, visual feedback |
| 8 | Completing a Word | When the player types the last character (position equals word length), the word is complete. Erase it from the screen, add to the score, BEEP, and pick the next word. The cycle begins again. | Completion detection (position = LEN), cycling through content, reset for next word |
| 9 | Missing a Word | If the word reaches row 20: flash it red, increment the miss counter, remove it. Display misses in the HUD. Three misses and the game loop exits to a game over screen. | Miss detection, fail counter, game over condition |
| 10 | The HUD | Top row: score, level, misses (shown as three hearts or symbols — lose one per miss). Bottom two rows: the target word and the player's typed progress. Clean, readable layout. | HUD with multiple data points, symbol-based life display |
| 11 | Increasing Difficulty | Every 10 completed words, increase the level. Lower the fall speed threshold. Select longer words from the array (levels 1-2 use indices 1-20, levels 3-4 use 15-35, level 5 uses 30-50, with overlap for variety). | Level progression, difficulty as variable, array index ranges |
| 12 | Multiple Words | From level 3, a second word appears while the first is still falling. Track two (then three) words simultaneously: arrays for each word's row, column, and text. The active target is always the lowest word. | Multiple active objects, parallel tracking arrays, selecting the most urgent target |
| 13 | GO SUB Dispatch | The game loop now juggles: move words, check input, check misses, update HUD. Organise with GO SUBs: GO SUB 500 moves all falling words, GO SUB 600 handles input, GO SUB 700 checks for misses, GO SUB 800 updates the HUD. | GO SUB as dispatch, multiple subroutines called per tick, code organisation for complexity |
| 14 | Streak Bonus | Track consecutive completions without a miss. Five in a row: flash "STREAK!" on screen, award 50 bonus points, BEEP fanfare. The streak resets on any miss. Rewards clean play. | Streak counter, conditional bonus, reset on failure |
| 15 | Sound and Polish | Word complete: rising BEEP (pitch based on word length — longer words, higher note). Miss: low BEEP. Streak: three ascending notes. Game over: descending phrase. Border colour reflects current level. | Sound variety, pitch as data, visual polish |
| 16 | The Finished Game | Play through all five levels. Verify word selection, fall speed, multiple words, streak tracking, scoring. Test edge cases: what if two words reach the bottom on the same tick? What if the player completes a word just as it reaches the bottom row? Clean the listing. ~80 lines of working, tested code. | Edge case testing, full integration, the finished product |

**Milestone:** The learner can work with string arrays, build strings character by character, use CHR$ and CODE, and manage multiple moving objects on screen. These skills — especially character-level string handling and string arrays — are essential for the text adventure parser in later games.

---

## Technical Notes

### Data Structures

```
DIM w$(50,7)    - word list: 50 words, max 7 characters each
DIM fr(3)       - falling word row position (up to 3 active words)
DIM fc(3)       - falling word column position
DIM fw$(3,7)    - falling word text
DIM fa(3)       - falling word active flag (0=inactive, 1=active)
```

The word list is loaded once at startup. The falling word arrays are updated every tick.

### String Array Sizing

DIM w$(50,7) allocates 50 strings of up to 7 characters each. On the 48K Spectrum, Sinclair BASIC string arrays use the second dimension as the fixed string length. Shorter words are padded with spaces. When displaying, use w$(n)( TO LEN w$(n)) or trim trailing spaces — but since words don't have trailing spaces in the DATA, the padding is invisible when printed.

In practice, the learner reads words with READ and assigns them directly: LET w$(i) = "cat". Sinclair BASIC pads to length 7 automatically.

### Character Comparison

Sinclair BASIC's INKEY$ returns lowercase for letter keys (unless CAPS LOCK is on). The word list should use lowercase. Comparison is case-sensitive — "A" does not equal "a". To keep things simple, all words and input are lowercase.

If the learner wants case-insensitivity, they can convert with CODE and CHR$: LET k$ = CHR$(CODE k$ - 32) to convert lowercase to uppercase. But lowercase throughout is simpler for 80 lines.

### Backspace Handling

The DELETE key on the Spectrum generates CHR$ 12. When detected:
- If the typed string t$ is not empty, remove the last character: LET t$ = t$(1 TO LEN t$ - 1)
- Update the display

This is straightforward string slicing. If t$ is already empty, do nothing.

### Multiple Word Management

With up to 3 words on screen, the game loop iterates through the falling word arrays:

```
500 REM MOVE FALLING WORDS
510 FOR i = 1 TO 3
520   IF fa(i) = 0 THEN GO TO 560
530   PRINT AT fr(i), fc(i); "       "
540   LET fr(i) = fr(i) + 1
550   PRINT AT fr(i), fc(i); INK 6; fw$(i)
560 NEXT i
570 RETURN
```

The active target is whichever word has the highest row value (closest to the bottom). If two words are on the same row, the leftmost is targeted first.

### No ELSE on the 48K

Character matching uses sequential IF/THEN:
```
IF k$ = "" THEN GO TO 250
IF k$ = CHR$ 12 THEN GO SUB 650: GO TO 250
IF k$ = w$(n)(p TO p) THEN LET t$ = t$ + k$: LET p = p + 1
IF k$ <> w$(n)(p TO p) THEN PRINT AT 21, p; INK 2; k$
```

Each line is independent. No ELSE needed.

### Line Numbering

- 1-49: Initialisation, DIM arrays, load word list from DATA
- 50-99: Level setup, pick first word, draw initial screen
- 100-199: Main game loop
- 200-299: Level complete / game over screens
- 500-599: Move falling words subroutine
- 600-699: Handle input subroutine
- 700-799: Check misses subroutine
- 800-899: Update HUD subroutine
- 900-999: DATA (50 words)

### Memory and Performance

The word list (50 × 7 = 350 bytes) and falling word arrays (~50 bytes) are negligible. The program is ~80 lines (~4-5 KB). Performance is adequate — the loop runs fast enough for smooth falling at the speeds needed, and INKEY$ polling adds no overhead.

The only risk is BEEP: Sinclair BASIC's BEEP blocks the entire program for its duration. Keep all BEEPs very short (0.05 seconds or less) to avoid pausing the falling animation.

---

## Changelog

- **v1.0 (2026-03-13):** Initial game outline for v5.0 curriculum.
