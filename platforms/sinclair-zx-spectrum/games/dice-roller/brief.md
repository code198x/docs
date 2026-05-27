# Dice Roller — Brief

**Title (working):** Dice Roller
**System / Track:** Sinclair ZX Spectrum / BASIC
**Position:** Volume 1, Game 5 of 8
**Headline concept:** Accumulation — patterns emerge from randomness
**Embedded concept:** Anticipation — the moment before the result; Mastery through practice — repeated play reveals the system
**Topics:** 5 topics, ~5–7 hours
**Constraint position:** period-faithful
**Status:** draft

Format: [`specifications/brief-basic-v1.md`](../../../../specifications/brief-basic-v1.md)

---

## 1. Pedagogical Role

Teach FOR/NEXT as the tool for counted repetition — so the learner arrives at Bright Spark able to write loops that repeat a known number of times, replacing the open-ended GO TO loops they've used so far.

---

## 2. Classic Ancestors

- **Dice simulators** — a universal type-in from the earliest home-computer books. *Practise Your BASIC* (Usborne, 1983) includes dice-rolling examples as FOR/NEXT demonstrations. The mechanic: roll dice, watch results accumulate, see patterns emerge from randomness.
- **Monte Carlo simulations** — the idea that enough random trials reveal the underlying distribution. Not named as such in the curriculum, but the learner experiences it: roll 100 dice, and sixes appear about 1/6 of the time.

---

## 3. Core Experience

Roll the dice. Watch the numbers appear. Roll again — five at once, then fifty, then five hundred. Patterns appear: sixes aren't lucky or unlucky, they just come 1/6 of the time. The pleasure is in watching randomness resolve into order when you accumulate enough results.

---

## 4. Visual Direction

- Dark theme from start. INVERSE title bar. DRAW die face illustration on title screen (DRAW rectangle + 6 PLOT dots, ~10 commands).
- Bar chart uses CHR$ 143 (solid block character) instead of asterisks — denser, chunkier, more like real data visualisation. Same code structure, one character swap.
- Six colours per face unchanged (red, yellow, green, magenta, cyan, white).
- PRINT AT dashboard with live-updating tallies unchanged.

---

## 5. Audio Direction

- **Roll sound.** A quick descending BEEP sequence (3–4 tones) — the sound of dice tumbling.
- **No other sound.** The focus is on watching the numbers, not listening.

---

## 6. Anti-goals

- No game mechanics — no betting, no gambling, no win/lose. This is a simulation, a toy for watching randomness. The design concept (Accumulation) is about observation, not competition.
- No arrays — tallies use six individual variables (`LET t1 = t1 + 1` through `t6 = t6 + 1`). Arrays arrive in V2.
- No graphical dice — no UDGs, no PLOT-drawn pips. Text only.
- Maximum ~25 lines of BASIC.

---

## 7. Topic Progression

1. **One die.** `LET d = INT(RND*6)+1`. `PRINT "You rolled: "; d`. Run it several times — different numbers each time. The learner already knows the RND/INT formula from Lucky Number; now it produces a die roll. **New:** reinforcement of the range formula (familiar ground). **Program:** 3 lines. **Polish beat:** is it fair? Roll it 20 times by hand and tally. Does each number appear roughly equally?

2. **Five dice at once.** `FOR i = 1 TO 5: LET d = INT(RND*6)+1: PRINT d; " "; : NEXT i`. Five rolls appear on one line. The learner sees FOR/NEXT for the first time — "do this five times." Change 5 to 10, to 50. The loop runs however many times you tell it. **New:** FOR/NEXT (counted repetition), the loop variable `i`, semicolons for same-line output. **Program:** ~5 lines. **Polish beat:** how many dice feel like "a handful" vs "a flood"?

3. **Keeping a tally.** After each roll, increment a counter for that face: `IF d = 1 THEN LET t1 = t1 + 1` through to `IF d = 6 THEN LET t6 = t6 + 1`. After the loop, PRINT all six tallies. Roll 100 dice — the tallies are roughly equal. Roll 10 — they're not. **Accumulation**: enough random events reveal the underlying pattern. **New:** combining FOR/NEXT with chained IF/THEN (two patterns working together). **Program:** ~15 lines. **Polish beat:** what number of rolls makes the pattern convincing? 50? 100? 1000?

4. **A visible tally.** Replace the end-of-run printout with a live dashboard: use PRINT AT to place each tally at a fixed screen position, updated inside the loop. The screen now shows the tallies growing in real time as each die rolls. Add a brief PAUSE inside the loop so the learner can watch each roll land. **New:** PRINT AT for fixed-position output (the learner's first encounter with screen coordinates). **Program:** ~20 lines. **Polish beat:** watching 500 rolls accumulate at speed is hypnotic. Watch the tallies converge.

5. **Make it yours.** Add a title screen. Add a bar chart: after the rolls complete, draw horizontal bars using repeated PRINT characters (`PRINT "*"` in a FOR loop) proportional to each tally. Add colour — each face value gets a different INK. Ask the player how many dice to roll: `INPUT "How many rolls? "; n` and use `FOR i = 1 TO n`. The learner now has a simulation they can experiment with — change the number of rolls, watch the pattern emerge or dissolve. **New:** INPUT controlling loop count, PRINT-character bar charts. **Program:** ~25 lines. **Polish beat:** roll 10, then 100, then 1000. Watch randomness become order. That's the design lesson.

---

## 8. Ship Test

- [ ] Every topic's code runs on a 48K Spectrum (emulator + real hardware)
- [ ] Every topic produces a working, runnable result
- [ ] FOR/NEXT loop is clearly explained — the learner understands "do this N times"
- [ ] 1000-roll tally shows roughly equal distribution (no off-by-one in the RND formula)
- [ ] PRINT AT dashboard updates correctly inside the loop
- [ ] Bar chart is visually readable — bars are proportional to tallies
- [ ] British English throughout
- [ ] Screenshots show actual running programs
- [ ] Code samples in `/code-samples/`
- [ ] Magazine voice

---

## 9. Pattern Library Extractions

- **basic** — FOR/NEXT counted loop: the fundamental "do this N times" structure. The foundation of every repetitive operation from here forward. Cross-platform.
- **basic** — PRINT AT dashboard: fixed-position screen output updated inside a loop. The pattern behind every score display, status bar, and real-time readout. Spectrum-specific syntax; cross-platform concept.
- **basic** — text bar chart: `FOR j = 1 TO count: PRINT "*";: NEXT j` — data visualisation in one line. The simplest form of "turn numbers into pictures."

---

## 10. Vault Tie-ins

- **Dice simulators** — the type-in tradition; Usborne and magazine listings.
- **Probability and randomness** — the design principle that enough random events reveal underlying distributions.
- *Practise Your BASIC* (Usborne, 1983) — FOR/NEXT examples as pedagogical ancestor.
