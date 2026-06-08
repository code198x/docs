# Tally — Brief

**Title (working):** Tally
**System / Track:** Commodore 64 / BASIC
**Position:** Volume 1, Game 4 of 8
**Headline concept:** Emergence — pattern out of many trials
**Embedded concept:** Visualisation — show data as a picture
**Topics:** 6 topics
**Constraint position:** period-faithful
**Status:** draft

Format: [`specifications/brief-basic-v1.md`](../../../../specifications/brief-basic-v1.md)

> **Design note (2026-06-08).** An earlier draft of this brief was statistically
> self-contradictory: it specified one die counted across six faces (`DIM T(6)`),
> which gives a *flat* distribution, yet promised a bell curve "tall in the
> middle". One die can only produce a flat distribution — a peak comes from
> *summing* dice. Tally now rolls **two dice and tallies their total (2–12)**, a
> genuine bell with its peak at 7. This is the iconic emergence (there are six
> ways to make 7 and only one to make 2), the real Monte Carlo / Galton-board
> lesson, and what the brief's "tall in the middle" language always wanted.

---

## 1. Pedagogical Role

Teach numeric arrays as counters and the screen as a chart — `DIM T(12)`, accumulation inside a `FOR` loop, and a bar built cell by cell by POKEing screen RAM and colour RAM — so the learner arrives at Bleeper able to hold many values in one named structure and turn them into a picture. The total of two dice is the index into the array; rolled enough times, the array *becomes* a bell — the first time the program produces a shape it was never told to draw.

---

## 2. Classic Ancestors

- **The two-dice statistics type-in** — a staple of the home-computer books and magazines: roll two dice a thousand times, count each total, and graph the result. *Compute!'s Gazette* and the Usborne listings used it to show that randomness has shape — that the sum of two fair dice is anything but even.
- **Monte Carlo simulation** — never named for the learner, but felt: enough random trials reveal the underlying distribution. Roll often enough and the totals settle into a bell, tall at 7 and short at the edges, because there are more ways to roll a 7 than a 2.

---

## 3. Core Experience

Choose how many rolls. The C64 rolls two dice over and over, and the bars climb cell by cell as each total tallies up — the bell curve appears out of pure randomness, peaked at 7. The result is the picture, and the picture is the same shape every time even though every roll is different. Roll ten and the bars are ragged; roll a thousand and the bell is unmistakable.

---

## 4. Visual Direction

- A bar chart drawn straight into memory: each bar is a column of solid blocks POKEd into screen RAM from 1024, with a matching colour POKEd into colour RAM from 55296 — the same screen-as-canvas the learner met in Skyline, now carrying data instead of a skyline.
- Eleven bars, one per total (2 to 12), two cells wide, on a **black background** (`POKE 53281,0`) so the colour reads cleanly. A single bright colour across all eleven bars (cyan) so the eye reads the whole *shape* as one form — the bell, not eleven separate columns. Colour here serves the silhouette, not per-bar labelling.
- The totals 2–12 POKEd as digit labels along the bottom row, lined up under their columns, so the chart reads as a real dashboard.
- The bars grow upward from the array, scaled so the tallest (7) fills the screen and the rest fall in proportion — the bell *emerges* on screen.
- Magazine-screenshot test: a Commodore-magazine screenshot of eleven solid cyan columns rising into the classic bell — tall at 7, short at 2 and 12 — with the totals ranked beneath. The kind of picture that made a type-in worth the evening.

---

## 5. Audio Direction

- C64 SID, single voice, minimal — POKEd at 54272. At most a soft tick as each bar grows a cell, so you can *hear* the run filling up. Quiet, not musical.
- Equally valid silent: the focus is on watching the curve form, and a long run with no sound is perfectly in keeping. Sound here is a small flourish, never the point.
- No multi-voice music, no roll-by-roll fanfare. The SID stays out of the way.

---

## 6. Anti-goals

- No real-time animation of each individual roll — the C64 rolls fast and the bars accumulate; this is not a race to watch two dice tumble.
- No two-player play, no betting, no win/lose. Tally is a simulation, a toy for watching randomness resolve into order.
- No sprites, no custom characters — solid blocks POKEd into screen RAM only. Sprites belong to later volumes.
- No three-voice SID music; the audio is a single soft tick at most.
- Keep it small — a few dozen lines of BASIC V2, Usborne-listing standard.

---

## 7. Topic Progression

1. **A die roll.** `D = INT(RND(1)*6)+1`, then `PRINT "YOU ROLLED:";D`, run ten times in a `FOR` loop so the spread is visible at a glance. The learner already met `RND` in Oracle; here it produces a die roll. **New:** the die-roll range formula (familiar ground, made concrete). **Program:** ~5 lines. **Polish beat:** is it fair? Watch ten rolls — does each face turn up about as often?

2. **Two dice, one total.** Roll two dice and add them: `D1 = INT(RND(1)*6)+1`, `D2 = INT(RND(1)*6)+1`, `T = D1+D2`, then `PRINT D1;"+";D2;"=";T`. Run ten and look at the totals — they cluster around 7, never spread evenly. The range is now 2 to 12, and the middle is already crowded. **New:** combining two random values; the 2–12 range of a two-dice total. **Program:** ~7 lines. **Polish beat:** notice how rarely a 2 or a 12 shows up — there's only one way to roll each.

3. **Counting the totals.** `DIM T(12)`, then a short `FOR` loop (20 rolls) that does `T(D) = T(D)+1` — the total *is* the index, no chain of `IF`s. Print the eleven counts (2 to 12). With only 20 rolls the shape is ragged. **New:** numeric arrays (`DIM`), an array element as a counter, the total used as a subscript. **Program:** ~9 lines. **Polish beat:** twenty rolls give a lumpy eleven; the array holds them all without eleven separate variables.

4. **A long run.** Wrap the roll-and-tally in `FOR I = 1 TO 1000` and print the totals at the end. Now 7 is plainly the biggest and the edges are small — the bell is there in the numbers. **Emergence:** enough random events reveal the underlying pattern. **New:** accumulation inside a counted `FOR` loop (the array filling across many trials). **Program:** ~9 lines. **Polish beat:** how many rolls make the pattern convincing — 50, 100, 1000? Try each and watch the totals settle around 7.

5. **The bell in bars.** Loop over the array and draw all eleven totals as columns of solid blocks POKEd into screen RAM from 1024, with colour POKEd into colour RAM from 55296, scaled so the tallest fills the screen, on a black background. POKE the totals 2–12 as labels along the bottom. The bell appears as a picture — tall at 7, short at the edges. **New:** a POKEd bar chart driven from an array; scaling heights to fit; labels POKEd into screen RAM. **Program:** ~22 lines. **Polish beat:** scale by the largest tally so the curve always fills the screen, whatever the run length.

6. **You set the rolls.** `INPUT "HOW MANY ROLLS";N` and run `FOR I = 1 TO N`, then draw the chart. Now the learner can experiment — roll 10 and the bars are ragged, roll 1000 and the curve is clean. Add the soft SID tick as the bars grow if you like. **New:** `INPUT` controlling the loop count (player-set runs). **Program:** ~24 lines. **Polish beat:** roll 10, then 100, then 1000 — watch randomness become a picture. That is the design lesson.

---

## 8. Ship Test

- [ ] Every topic's code runs on a PAL C64 (emulator + real hardware)
- [ ] Every topic produces a working, runnable result
- [ ] One new BASIC concept per topic — no topic introduces two major ideas
- [ ] Gradual progression — a reader can follow from topic 1 to the finished chart without gaps
- [ ] A 1000-roll run gives a bell-shaped distribution peaked at 7, tapering to the edges (no off-by-one in the two-dice formula or the array index; totals sum to the run count)
- [ ] The POKEd bars draw correctly into screen RAM (1024) and colour RAM (55296), and read cleanly as a chart on the black background
- [ ] Labels 2–12 stay lined up under their columns
- [ ] British English throughout (exception: "program")
- [ ] Screenshots show the actual running program, not mockups
- [ ] Code samples in `/code-samples/`, not inline
- [ ] Magazine voice — warm, technical, never condescending

---

## 9. Pattern Library Extractions

- **basic** — numeric array as a set of counters: `DIM T(12)` with the data value (a two-dice total) used as the subscript (`T(D) = T(D)+1`). Replaces a chain of `IF`s with one indexed increment — the pattern behind every histogram, score table, and frequency count.
- **basic** — accumulation in a counted loop: a `FOR` loop filling an array across many trials, the foundation of every simulation and statistics routine.
- **rendering** — POKEd bar chart: columns of solid blocks written into screen RAM with matching colour RAM cells, heights driven by array values and scaled to fit. The C64-native "turn numbers into a picture", building on Skyline's screen-as-canvas. C64-specific addresses; cross-platform concept.

---

## 10. Vault Tie-ins

- **Two-dice statistics type-ins** — the "roll 1000 times and graph it" tradition in the Commodore magazines and Usborne listings, and the demonstration that the sum of two dice is a bell, not a flat line.
- **Probability and randomness** — the design principle that enough random trials reveal the underlying distribution; the bell at 7 because there are more ways to make 7 than any other total.
- **Memory-mapped screen** — screen RAM at 1024 and colour RAM at 55296, the C64 surface the volume keeps returning to and the assembly track revisits at machine speed.
