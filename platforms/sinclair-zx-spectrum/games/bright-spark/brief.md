# Bright Spark — Brief

**Title (working):** Bright Spark
**System / Track:** Sinclair ZX Spectrum / BASIC
**Position:** Volume 1, Game 6 of 8
**Headline concept:** Pattern — recognise, reproduce, extend
**Embedded concept:** Signposting — using colour and sound to make the rules obvious without words
**Topics:** 6 topics, ~7–9 hours
**Constraint position:** period-faithful
**Status:** draft

Format: [`specifications/brief-basic-v1.md`](../../../../specifications/brief-basic-v1.md)

---

## 1. Pedagogical Role

Teach that strings can store and grow a sequence, that FOR/NEXT loops can replay it, and that GO SUB/RETURN makes reusable code blocks — so the learner arrives at Hi-Lo with string manipulation, loop-driven playback, and subroutines as working tools.

---

## 2. Classic Ancestors

- **Simon** (Milton Bradley / Ralph Baer, 1978) — the electronic memory game. Four coloured pads, each with a distinct tone. The device plays a growing sequence; the player repeats it. The mechanic: short-term memory tested against an ever-lengthening chain.
- **Simon type-ins** — published in nearly every home-computer magazine. A universal first "real game" for BASIC — colour, sound, input, and a natural difficulty curve built into the mechanic.

---

## 3. Core Experience

Watch the panels flash. Listen to the tones. Repeat the sequence. Get one more right — the sequence grows. Get one wrong — game over. Each round is a tiny victory; each failure is "one more than I could hold in my head." Short sessions, instant restart, and the compulsion to beat your own record.

---

## 4. Visual Direction

- Four coloured panels (red, blue, green, yellow) are already the strongest visual in V1. Minimal changes.
- INVERSE score display at the top. BRIGHT 1 on the title.
- BRIGHT flash on panels unchanged (core mechanic).
- BEEP with distinct pitches per panel unchanged.

---

## 5. Audio Direction

- **Distinct tone per panel.** Four different pitches — one per colour. The player can close their eyes and replay the sequence by ear alone. Sound and colour reinforce each other — that's **signposting**.
- **Wrong-answer buzz.** A low, harsh tone on failure. Unmistakable, brief, not punishing.
- **No music.** Silence between sequences — the tones are the game's entire audio vocabulary.

---

## 6. Anti-goals

- No difficulty settings — the sequence length *is* the difficulty. It grows by one each round, calibrated to human short-term memory (~7 items). No configuration needed.
- No high-score persistence — the score is the sequence length, shown at game over. No arrays, no SAVE/LOAD.
- No graphical sprites or pixel art — panels are character-cell colour blocks via PRINT and PAPER.
- Maximum ~50 lines of BASIC (plus subroutines). Bright Spark is the largest V1 game — the Simon mechanic requires reusable panel-drawing and flash code via GO SUB.

---

## 7. Topic Progression

1. **Four panels.** Draw four coloured rectangles using PRINT with PAPER changes: `PAPER 2` (red), fill a block with spaces using `PRINT AT` across several rows, then `PAPER 1` (blue) for the next block. Four panels, four colours, filling the screen. **New:** PAPER for background colour, PRINT AT for block filling, the concept of colour as identity. **Program:** ~10 lines. **Polish beat:** which four colours? They need to be distinct at a glance and look good together.

2. **Flashing a panel.** Make one panel flash: redraw it with `BRIGHT 1` (the lighter variant), PAUSE briefly, redraw with `BRIGHT 0` (back to normal). Add a BEEP — a distinct pitch for this panel. The flash + tone together say "this one." **New:** BRIGHT (the 15th colour dimension), PAUSE for flash timing. **Program:** ~14 lines. **Polish beat:** how long should the flash last? Too short to see is unfair; too long is boring.

3. **A sequence.** Store the sequence as a string: `LET s$ = ""`. Each round, add a random panel: `LET s$ = s$ + STR$(INT(RND*4)+1)`. Replay the sequence with a FOR loop that reads each character: `FOR i = 1 TO LEN(s$)`, flash the panel named by `s$(i)`. The panel-drawing and flash code from Unit 2 move into GO SUB subroutines — the learner already understands the flash code, GO SUB just means "put it somewhere reusable and call it." **New:** GO SUB/RETURN (reusable code), strings as sequences (concatenation, LEN, indexing, STR$/VAL). **Program:** ~30 lines + subroutines. **Polish beat:** watch the sequence get longer. At what length do you start to struggle?

4. **The player repeats.** After the sequence plays, wait for the player to repeat it. A FOR loop from 1 to LEN(s$): inside, an INKEY$ wait loop that checks which key was pressed and compares to `s$(i)`. Correct press — flash the panel, continue. Wrong press — game over. **New:** INKEY$ inside FOR (combining real-time input with counted repetition), string comparison for validation. **Program:** ~25 lines. **Polish beat:** flash the panel when the player presses — their input is mirrored visually. It feels like playing an instrument.

5. **Game over and score.** When the player fails, display the sequence length: `PRINT "The sequence was "; LEN(s$) - 1; " long"`. Add the wrong-answer buzz. Clear the panels and show the result centre-screen. Add a "Press any key to play again" prompt with GO TO back to the start. **New:** LEN as score, game-over flow, replay loop. **Program:** ~28 lines. **Polish beat:** is the game-over moment respectful? "The sequence was 7 long" acknowledges achievement. "You failed" doesn't.

6. **Make it yours.** Add a title screen: "*** BRIGHT SPARK ***" with the four panel colours shown as a legend. Number each panel (1–4) so the player knows which key to press. Add colour to the score display — green for a good run (6+), yellow for decent (4–5), red for short (1–3). The learner now owns a complete Simon game — and has built something people will ask to play. **New:** decorative title, numbered panels as instructions, colour-coded results. **Program:** ~30 lines. **Polish beat:** the four tones should form a pleasing interval — a chord, not noise. Tune them.

---

## 8. Ship Test

- [ ] Every topic's code runs on a 48K Spectrum (emulator + real hardware)
- [ ] Every topic produces a working, runnable result
- [ ] Four panels are visually distinct — identifiable from across the room
- [ ] Flash effect is clearly visible — BRIGHT 1 vs BRIGHT 0 difference is obvious
- [ ] Each panel has a distinct, memorable tone
- [ ] Sequence replay is timed correctly — fast enough to be exciting, slow enough to follow
- [ ] Player input validation works — correct presses continue, wrong presses end the game
- [ ] Game difficulty scales naturally — ~7 items is the human short-term memory limit
- [ ] British English throughout
- [ ] Screenshots show actual running programs
- [ ] Code samples in `/code-samples/`
- [ ] Magazine voice

---

## 9. Pattern Library Extractions

- **basic** — string-as-sequence: `s$ = s$ + STR$(n)` to grow a sequence, `s$(i)` to read it back. The pattern of using a string as a simple ordered data structure. Used in every game that records a history or replays a pattern.
- **framework** — GO SUB/RETURN subroutines: reusable code blocks for operations called from multiple places (panel drawing, flash effect). The Spectrum's tool for avoiding code duplication. Cross-platform concept.
- **rendering** — BRIGHT flash effect: toggle BRIGHT 1/0 with PAUSE for a visual "pulse." The simplest animation — change a property briefly, then revert. Cross-platform concept.
- **audio** — distinct-tone-per-object: each panel gets its own pitch, creating an audio vocabulary the player memorises. The pattern behind every game where sound identifies objects or actions.

---

## 10. Vault Tie-ins

- **Simon** (Milton Bradley / Ralph Baer, 1978) — the electronic memory game as direct ancestor.
- **Ralph Baer** — inventor of Simon (and the Brown Box / Magnavox Odyssey). Person entry.
- **Short-term memory in game design** — the design principle that ~7 items is the human limit, and games calibrated to that limit feel challenging but fair.
