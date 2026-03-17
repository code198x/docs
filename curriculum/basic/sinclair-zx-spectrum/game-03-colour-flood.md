# Game 03: Colour Flood

**Track:** Spectrum BASIC
**Genre:** Colour memory (Simon Says)
**Units:** 8
**Language:** Sinclair BASIC
**Final size:** ~90 lines

---

## Premise

Four big coloured panels fill the screen: blue, red, green, yellow. The Spectrum plays a sequence — one panel lights up bright with a distinct tone, then fades back. Watch, memorise, repeat. Get it right and the sequence grows by one. Get it wrong and it's game over. How long can you remember?

This is Simon Says for the Spectrum. The panels are impossible to miss — each one flashes bright across 8 rows of the screen. Each colour has its own pitch, so you hear the sequence as well as see it. The difficulty scales naturally: a 3-colour sequence is easy; a 10-colour sequence is genuinely hard.

The game teaches FOR/NEXT (playing and checking sequences), the Spectrum's colour model (PAPER colours, BRIGHT), and string manipulation in its simplest form (building and reading a sequence stored as a string).

---

## Core Mechanics

A string `s$` stores the sequence as digit characters ("1", "13", "132"...). Each round appends a random colour (1-4). A FOR/NEXT loop plays the sequence: for each character, the matching panel flashes bright with PAPER and BRIGHT, the border changes to that colour, a BEEP sounds at a colour-specific pitch, then the panel dims back. The player repeats the sequence by pressing number keys 1-4. Each keypress is checked against the string. Wrong = game over with explosion strobe. Correct full sequence = score +1, sequence grows.

### The Panels

Four panels arranged in a row, each 7 columns wide × 8 rows tall. Drawn by a subroutine at line 400. Colours: PAPER 1 (blue), PAPER 2 (red), PAPER 4 (green), PAPER 6 (yellow). Each panel has a centred number label (1-4).

### The Flash

A subroutine at line 500 draws a single panel in BRIGHT 1, changes the border to that colour, and plays a BEEP. Each colour has its own pitch: blue=5, red=10, green=15, yellow=20. After a brief PAUSE, the dim subroutine redraws all panels at normal brightness.

### Sound Design

Each colour has a distinct pitch, spaced 5 semitones apart. The sequence becomes a melody — experienced players recognise patterns by sound as well as colour. The "correct" jingle plays two high notes. The "wrong" strobe plays alternating low tones.

---

## Unit Breakdown

| Unit | Title | What the learner builds | New concepts |
|------|-------|------------------------|-------------|
| 1 | Counting | FOR/NEXT counts to 10, backwards, in twos. The loop variable changes each pass. The learner experiments with different start, end, and STEP values. | FOR/NEXT, loop variable, STEP |
| 2 | The Colour Palette | A FOR loop cycles PAPER through all colours, printing coloured blocks across the screen. The learner sees all 8 colours (0-7) and discovers BRIGHT doubles the palette. One loop fills the screen with colour. | PAPER in loops, the 8 colours, BRIGHT |
| 3 | Four Panels | Draw four big coloured panels across the screen using nested loops and PRINT AT with PAPER. Each panel is 7 columns × 8 rows. Number labels centred on each panel. The game screen exists. | PAPER with PRINT AT for large blocks, screen layout with colour |
| 4 | Flash and Fade | A subroutine flashes one panel bright (PAPER + BRIGHT 1), plays a BEEP at a colour-specific pitch, then a second subroutine redraws all panels at normal brightness. The learner calls GO SUB to flash panel 2, panel 4, any panel. | GO SUB for reusable drawing, BRIGHT 1 for emphasis, BEEP per colour |
| 5 | Play a Sequence | Store a sequence in a string: `LET s$ = "132"`. A FOR loop reads each character with `VAL s$(i TO i)` and flashes the matching panel. The panels light up in order — a visible, audible pattern. | Strings as data, LEN, VAL, STR$, FOR/NEXT to iterate a string |
| 6 | Your Turn | After the sequence plays, the player repeats it. INKEY$ waits for key 1-4. Each keypress flashes the matching panel and checks against the expected colour. Wrong = game over. Right = next in sequence. | INKEY$ for input, comparing player input against stored sequence |
| 7 | Growing Sequences | Replace the fixed sequence with a growing one. Each round appends a random colour: `LET s$ = s$ + STR$ (INT (RND*4)+1)`. Score tracks completed rounds. "Correct!" between rounds. GO TO loops back. | String concatenation with RND, growing data, score tracking |
| 8 | The Finished Game | Title screen with colour panels and instructions. Results screen with animated score count-up and ratings. Explosion strobe on game over. Border resets between phases. The complete game. | Title/results screens, rating tiers, program structure |

**Milestone:** The learner understands FOR/NEXT loops, BRIGHT, the colour model, and has built a genuinely fun memory game using strings to store growing data. The four chunky panels and per-colour tones make this a sensory experience, not a logic exercise.

---

## Technical Notes

### Key Variables

| Variable | Purpose |
|----------|---------|
| `s$` | The sequence string (e.g. "1324") |
| `sc` | Score (completed rounds) |
| `c` | Current colour number being played/checked |
| `e` | Expected colour from sequence |
| `k$` | Player's keypress |
| `i` | Loop counter for playback and checking |
| `px` | Panel x-position (column) |

### Four Colours Not Seven

The v2 prototype used 7 colours (matching the Spectrum's palette). The v3 uses 4 — blue (1), red (2), green (4), yellow (6). Four is plenty for Simon Says: the original game only had four. Fewer colours means the panels can be bigger, the key mapping is simpler (1-4 not 1-7), and the game is accessible to younger learners.

The skipped colours (3=magenta, 5=cyan, 7=white) could return as BRIGHT variants in a "Try This" extension — expanding the palette adds difficulty.

### Panel Drawing

Each panel occupies 7 columns × 8 rows. The four panels sit at columns 1, 9, 17, 25 — filling 28 of the 32 available columns with 1-column gaps between them. Rows 3-10, leaving room for the header (row 0) and status messages (row 19).

### String as Sequence Storage

`s$` grows by one character each round. Character `i` holds the colour for step `i` of the sequence. `VAL s$(i TO i)` converts it back to a number for the panel flash. This is the learner's first use of strings as structured data — the same idea that will drive DATA/READ in Game 5.

### Line Numbering

- 1-5: Initialisation
- 10-46: Title screen
- 48-68: Game screen setup
- 80-152: Game loop (new round, play sequence, player input, correct)
- 200-258: Game over and results
- 400-424: Draw panels subroutine (dim)
- 500-522: Flash panel subroutine (bright)

---

## Changelog

- **v4.0 (2026-03-17):** Four chunky colour panels (7×8 blocks), distinct BEEP per colour, GO SUB for flash/dim, proper title and results screens. Prototype tested in Emu198x.
- **v3.0 (2026-03-16):** Simon Says redesign with border flashes.
- **v2.0 (2026-03-16):** Screen-filling patterns (replaced — too much tech demo).
- **v1.0 (2026-03-13):** Initial game outline.
