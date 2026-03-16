# Game 03: Colour Flood

**Track:** Spectrum BASIC
**Genre:** Colour memory (Simon Says)
**Units:** 8
**Language:** Sinclair BASIC
**Max lines:** ~65

---

## Premise

The Spectrum's border floods with colour — a sequence of flashes, each with its own tone. Watch, memorise, repeat. Get it right and the sequence grows by one. Get it wrong and the game is over. How long a sequence can you remember?

This is Simon Says for the Spectrum. The border is the display — it fills with a colour that's impossible to miss. Each colour has its own pitch, so you can hear the sequence as well as see it. The colour key on screen maps numbers 1-7 to colours, so the player always knows what to press.

The game teaches FOR/NEXT properly (playing and checking sequences), the Spectrum's colour model (all 7 colours plus their sounds), and string manipulation in its simplest form (building and reading a sequence string).

---

## Core Mechanics

A string `s$` stores the sequence as digit characters ("2", "46", "463"...). Each round appends a random colour (1-7). A FOR/NEXT loop plays the sequence by flashing the border and BEEPing for each character. The player repeats the sequence by pressing number keys. Each keypress is checked against the string. Wrong answer = game over. Correct full sequence = score +1, sequence grows.

---

## Unit Breakdown

### Unit 1: Counting

**Concept:** FOR/NEXT, loop variable, STEP

The formal introduction to FOR/NEXT. Count to 10, count backwards, count in twos. See how the loop variable changes each pass.

---

### Unit 2: The Border Rainbow

**Concept:** BORDER, the 7 colours (1-7), BEEP per colour

Cycle the border through all seven colours with a different BEEP tone for each. The learner sees and hears the colour-to-number mapping. Colour 0 (black) is excluded because it's invisible against the black screen.

---

### Unit 3: The Game Screen

**Concept:** PAPER, INK, BRIGHT, building a visual layout

Build the game screen: blue header bar, colour reference key (seven coloured blocks labelled 1-7), score display, status message. Uses FOR/NEXT to draw the header bar and the colour key.

---

### Unit 4: Play a Sequence

**Concept:** Strings as data, LEN, VAL, STR$, FOR/NEXT to iterate

Store a fixed sequence in a string (`LET s$="246"`). Loop through it with FOR/NEXT, using `VAL s$(i)` to extract each colour number. Flash the border and BEEP for each one. The learner sees a FOR/NEXT loop reading data from a string — each character is a colour instruction.

---

### Unit 5: Your Turn

**Concept:** INKEY$ for input, comparing keys to expected values, debounce

After the sequence plays, the player repeats it. A FOR/NEXT loop checks each keypress against the string. Correct = border flashes the colour with a tone. Wrong = game over with an error BEEP.

---

### Unit 6: Growing Sequences

**Concept:** String concatenation, RND, the game loop

Replace the fixed sequence with a growing one. Each round: `LET s$=s$+STR$(INT(RND*7)+1)` appends a random colour. The sequence starts at length 1 and grows by one each round. GO TO loops back for the next round after a correct answer.

---

### Unit 7: Scoring and Game Over

**Concept:** Score tracking, IF/THEN rating tiers, game flow

Add a score counter that increments each round. On game over, show the score and a rating tier. "Correct!" flashes green between rounds. "Wrong! Game over." flashes red with a low BEEP.

---

### Unit 8: Polish

**Concept:** Speed, difficulty, sound design, the complete game

Speed up the sequence playback as the score increases (shorter PAUSE values). Add BRIGHT to the colour key. Design the sound profile — each colour's BEEP pitch should feel distinct and memorable. The complete game.

---

**Milestone:** The learner understands FOR/NEXT loops, the Spectrum's colour model, string basics (LEN, VAL, STR$, concatenation), and has built a genuinely fun memory game. The border-flooding visual and per-colour sounds make this a sensory experience, not just a logic exercise.

---

## Technical Notes

### Key Variables

```
s$  - the sequence string (e.g. "2463")
sc  - score (number of completed rounds)
c   - current colour number being played/checked
k$  - the key the player pressed
i   - loop counter for sequence playback and checking
```

### Line Numbering

- 1-18: Setup and header bar
- 20-30: Colour key and initial display
- 32-34: Variable initialisation
- 40-66: New round and sequence playback
- 70-110: Player input and checking
- 112-126: Round complete / game over

### Spectrum-Specific Notes

- `STR$ n` converts a number to a string. `VAL s$` converts a string to a number. These are how the sequence string stores and retrieves colour numbers.
- `s$(i)` reads the i-th character of string `s$`. On the Spectrum, string indexing starts at 1, not 0.
- Colours 1-7 are used (not 0) because BORDER 0 is black and invisible against the black screen background.
- Each colour gets a BEEP at `c*3` semitones — this spaces the tones evenly so each colour sounds distinct.

---

## Changelog

- **v3.0 (2026-03-16):** Complete redesign as Simon Says colour memory game. Replaced screen-filling visual toy with a proper game.
- **v2.0 (2026-03-16):** Visual-first screen-filling patterns (replaced — too much tech demo, not enough game).
- **v1.0 (2026-03-13):** Initial game outline for v5.0 curriculum.
