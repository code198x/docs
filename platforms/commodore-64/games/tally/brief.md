# Tally — Brief

**Title (working):** Tally
**System / Track:** Commodore 64 / BASIC
**Position:** Volume 1, Game 4 of 8
**Headline concept:** Emergence — pattern out of many trials
**Embedded concept:** Visualisation — show data as a picture
**Topics:** ~6 topics
**Constraint position:** period-faithful
**Status:** draft

Format: [`specifications/brief-basic-v1.md`](../../../../specifications/brief-basic-v1.md)

---

## 1. Pedagogical Role

Teach numeric arrays as counters and the screen as a chart — `DIM T(6)`, accumulation inside a `FOR` loop, and a bar built cell by cell by POKEing screen RAM and colour RAM — so the learner arrives at Bleeper able to hold many values in one named structure and turn them into a picture, the first time the program produces more than it was told.

---

## 2. Classic Ancestors

- **The dice-statistics type-in** — a staple of the home-computer books and magazines: roll the dice a thousand times, count each face, and graph the result. *Compute!'s Gazette* and the Usborne listings used it to show that randomness has shape.
- **Monte Carlo simulation** — never named for the learner, but felt: enough random trials reveal the underlying distribution. Roll often enough and the sixes settle to one in six, and the six bars settle into a bell.

---

## 3. Core Experience

Choose how many rolls. The C64 rolls, and the bars climb cell by cell as each face tallies up — the bell curve appears out of pure randomness. The result is the picture, and the picture is the same shape every time even though every roll is different.

---

## 4. Visual Direction

- A live bar chart drawn straight into memory: each bar is a column of solid blocks POKEd into screen RAM from 1024, with a matching colour POKEd into colour RAM from 55296 — the same screen-as-canvas the learner met in Skyline, now carrying data instead of a skyline.
- One colour per bar (the six face values each get their own hue) so the chart reads at a glance — colour as a label, not decoration.
- Labels and the run count printed with `PRINT` and `TAB`: the face numbers 1–6 sit under their columns, the totals above or beside them, lined up with `TAB` so the dashboard stays tidy as the numbers grow.
- The bars grow upward a cell at a time as the tallies climb, so the shape *emerges* on screen instead of appearing all at once.
- Magazine-screenshot test: a Commodore-magazine screenshot of six solid coloured columns rising into the classic bell — tall in the middle, short at the edges — with the face numbers ranked beneath. The kind of picture that made a type-in worth the evening.

---

## 5. Audio Direction

- C64 SID, single voice, minimal — POKEd at 54272. At most a soft tick as each bar grows a cell, so you can *hear* the run filling up. Quiet, not musical.
- Equally valid silent: the focus is on watching the curve form, and a long run with no sound is perfectly in keeping. Sound here is a small flourish, never the point.
- No multi-voice music, no roll-by-roll fanfare. The SID stays out of the way.

---

## 6. Anti-goals

- No real-time animation of each individual roll — the C64 rolls fast and the bars accumulate; this is not a race to watch one die tumble.
- No two-player play, no betting, no win/lose. Tally is a simulation, a toy for watching randomness resolve into order.
- No sprites, no custom characters — solid blocks POKEd into screen RAM only. Sprites belong to later volumes.
- No three-voice SID music; the audio is a single soft tick at most.
- Keep it small — a few dozen lines of BASIC V2, Usborne-listing standard.

---

## 7. Topic Progression

1. **One die.** `D = INT(RND(1)*6)+1`, then `PRINT "YOU ROLLED:";D`. Run it several times — a different face each time. The learner already met `RND` in Oracle; here it produces a die roll. **New:** the die-roll range formula (familiar ground, made concrete). **Program:** ~3 lines. **Polish beat:** is it fair? Roll it twenty times and tally by hand — does each face turn up about as often?

2. **Six counters in one array.** `DIM T(6)`, then a `FOR` loop that rolls and does `T(D) = T(D)+1`. The face value *is* the index — no chain of six `IF`s. After the loop, `PRINT` the six totals. **New:** numeric arrays (`DIM`), an array element as a counter, the roll value used as a subscript. **Program:** ~8 lines. **Polish beat:** ten rolls give a ragged six; the array holds all of them without six separate variables.

3. **Accumulate a long run.** Wrap the roll-and-tally in a `FOR I = 1 TO 1000` loop and print the totals at the end. Roll 1000 and the six counts come out roughly equal; roll 10 and they do not. **Emergence:** enough random events reveal the underlying pattern. **New:** accumulation inside a counted `FOR` loop (the array filling across many trials). **Program:** ~10 lines. **Polish beat:** how many rolls make the pattern convincing — 50, 100, 1000? Try each and watch the totals settle.

4. **One bar by POKE.** Take a single tally and draw it as a column of solid blocks POKEd into screen RAM from 1024, with a colour POKEd into colour RAM from 55296 — height proportional to the count. The learner reaches the screen by hand, exactly as in Skyline, but now the height *means* something. **New:** a POKEd bar — screen RAM + colour RAM driven by a data value. **Program:** ~12 lines. **Polish beat:** the block column is denser and more "data" than printed characters — it looks like a real chart.

5. **All six bars.** Loop over the array and draw all six columns side by side, each face value in its own colour, with `PRINT`/`TAB` labels underneath. The bell curve appears — tall in the middle, short at the edges. **New:** a `FOR` loop drawing the whole chart from the array; `TAB` to line up the labels. **Program:** ~18 lines. **Polish beat:** scale the bars so the tallest fits the screen — pick the height that makes the curve unmistakable.

6. **Player sets the run count.** `INPUT "HOW MANY ROLLS";N` and run `FOR I = 1 TO N`, then draw the chart. Now the learner can experiment — roll 10 and the bars are ragged, roll 1000 and the curve is clean. Add the soft SID tick as the bars grow if you like. **New:** `INPUT` controlling the loop count (player-set runs). **Program:** ~20–25 lines. **Polish beat:** roll 10, then 100, then 1000 — watch randomness become a picture. That is the design lesson.

---

## 8. Ship Test

- [ ] Every topic's code runs on a PAL C64 (emulator + real hardware)
- [ ] Every topic produces a working, runnable result
- [ ] One new BASIC concept per topic — no topic introduces two major ideas
- [ ] Gradual progression — a reader can follow from topic 1 to the finished chart without gaps
- [ ] A 1000-roll run gives a roughly even, bell-shaped distribution (no off-by-one in the `RND` formula or the array index)
- [ ] The POKEd bars draw correctly into screen RAM (1024) and colour RAM (55296), and read cleanly as a chart
- [ ] `TAB` labels stay lined up as the totals grow
- [ ] British English throughout (exception: "program")
- [ ] Screenshots show the actual running program, not mockups
- [ ] Code samples in `/code-samples/`, not inline
- [ ] Magazine voice — warm, technical, never condescending

---

## 9. Pattern Library Extractions

- **basic** — numeric array as a set of counters: `DIM T(6)` with the data value used as the subscript (`T(D) = T(D)+1`). Replaces a chain of `IF`s with one indexed increment — the pattern behind every histogram, score table, and frequency count.
- **basic** — accumulation in a counted loop: a `FOR` loop filling an array across many trials, the foundation of every simulation and statistics routine.
- **basic** — POKEd bar chart: a column of solid blocks written into screen RAM with a matching colour RAM cell, height driven by a data value. The C64-native "turn numbers into a picture", building on Skyline's screen-as-canvas. C64-specific addresses; cross-platform concept.

---

## 10. Vault Tie-ins

- **Dice-statistics type-ins** — the "roll 1000 times and graph it" tradition in the Commodore magazines and Usborne listings.
- **Probability and randomness** — the design principle that enough random trials reveal the underlying distribution.
- **Memory-mapped screen** — screen RAM at 1024 and colour RAM at 55296, the C64 surface the volume keeps returning to and the assembly track revisits at machine speed.
