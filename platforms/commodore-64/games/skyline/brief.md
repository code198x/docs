# Skyline — Brief

**Title (working):** Skyline
**System / Track:** Commodore 64 / BASIC
**Position:** Volume 1, Game 1 of 8
**Headline concept:** Composition — placing parts to make a whole
**Embedded concept:** Coordinates — addressing the screen by row and column
**Topics:** 6 topics, ~6–8 hours
**Constraint position:** period-faithful
**Status:** draft

Format: [`specifications/brief-basic-v1.md`](../../../../specifications/brief-basic-v1.md)

---

## 1. Pedagogical Role

Make the screen a canvas the learner addresses by hand: screen RAM at 1024, colour RAM at 55296, and `1024 + R*40 + C` as the one formula that reaches any cell — so that every later game in the volume already knows how to put a coloured thing at a chosen place. This is the foundation. Reflex flashes the border, Tally POKEs a bar chart, Rover walks a rover across the grid — all of it is Skyline's canvas with something moving on top.

---

## 2. Classic Ancestors

- **"Draw a picture" type-ins** — the listings that opened a hundred magazines and Usborne books: a page of `POKE` statements that, run blind, resolve into a house, a rocket, a face. The reward was watching something you couldn't read as code appear as a picture.
- **The skyline / cityscape demo** — the cityscape was a stock subject because it is forgiving (rectangles of solid blocks) and it scales (one tower teaches the loop, a row of them teaches the nested loop). It is the "hello, screen" of memory-mapped graphics.

---

## 3. Core Experience

A city rises out of black. Towers of solid blocks climb the screen one block at a time, windows light up in colour, and a sunset settles behind them — a picture you wrote, appearing. No input, no game loop: the joy is watching it build and knowing every block went where you sent it.

---

## 4. Visual Direction

- The screen is the 40×25 character grid. Each cell is two bytes the program writes by hand: a **screen code** at `1024 + R*40 + C` (the shape) and a colour at the matching cell in **colour RAM** at `55296 + R*40 + C` (the hue). Skyline is built entirely from solid and part-solid block screen codes — no text, no PETSCII letters, just blocks stacked into towers.
- **Colour carries meaning, not decoration.** A tower body is one dark colour; a lit window is a bright one in the *same cell position* the eye reads as "a light is on". The contrast between an unlit tower cell and a lit window cell is the whole image — the learner sees that the colour byte is a second, parallel screen they address with the identical coordinate formula.
- The backdrop is set with two registers, not POKEd cell by cell: `POKE 53281` (background) holds the sky, `POKE 53280` (border) frames it. The sunset is a single deliberate pair of values — the learner changes two numbers and the mood of the whole picture turns.
- **Magazine-screenshot test:** a *Compute!'s Gazette* listing page, the program name above a photographed C64 screen — a row of dark towers of uneven height against a deep-blue sky, scattered cyan and yellow windows, a violet border. The kind of result a reader would type three pages of `DATA`-free `POKE`s to get, and feel they earned.

---

## 5. Audio Direction

- Skyline is **near-silent by design** — it is a picture, not an event. The SID at 54272 stays out of the way so the learner's attention is on the screen filling in.
- The one optional touch: a **soft, short tone as each tower tops out** — a single SID voice, a brief note, so the city "lands" block by block with a quiet sense of completion. It is a grace note, introduced as a take-it-or-leave-it polish beat, never a mechanic.
- Everything else is deliberately quiet. No music, no looping sound — the SID comes up to a real voice with rhythm later, in Bleeper. Here it does, at most, one thing once.

---

## 6. Anti-goals

- **No movement, no input, no game loop.** This is the canvas, not the game. Real-time input and a live loop arrive in Rover; Skyline ends when the picture is complete and stops.
- **No sprites, no custom characters, no raster tricks.** The whole image is stock screen codes in stock screen RAM. VIC-II sprites belong to a later volume.
- **No `DATA`-table picture.** The city is *computed* with loops and `RND`, not read from a fixed list of coordinates — the lesson is the formula and the loop, not transcribing someone else's pixels.
- **No multi-voice sound.** At most one soft tone. The SID's depth is Bleeper's job.
- Keep it small: the finished program is well under 40 lines of BASIC.

---

## 7. Topic Progression

1. **One block on the screen.** Clear the screen, then place a single solid block: pick a row and a column, work out `1024 + R*40 + C`, `POKE` the block's screen code there, and `POKE` a colour into the matching cell at `55296 + R*40 + C`. One block, exactly where you sent it. **New:** screen RAM at 1024 and colour RAM at 55296; the screen code for a solid block; the `1024 + R*40 + C` coordinate formula. **Program:** ~6 lines. **Polish beat:** move the block by changing R and C and re-running — feel the grid. The colour byte is a *separate* POKE; comment out the colour-RAM line and watch the block take whatever colour was already there.

2. **A tower.** Stack blocks up a column with a `FOR` loop: hold the column fixed, count rows from the ground upward, `POKE` a block (and its colour) at each. One loop turns one block into a tower of any height — change the loop's range, change the height. **New:** `FOR…NEXT` driving a `POKE` down a fixed column. **Program:** ~9 lines. **Polish beat:** which way does the tower grow — up from the bottom or down from the top? Decide where "the ground" is (row 24) and build upward, the way a city looks right.

3. **A row of towers.** Wrap the tower in a second loop: an outer `FOR` steps the column across the screen, the inner `FOR` raises a tower at each. Nested loops — the inner runs in full for every step of the outer — turn one tower into a skyline. **New:** nested `FOR…NEXT` (rows × columns); the outer loop choosing *where*, the inner loop drawing *what*. **Program:** ~13 lines. **Polish beat:** leave a gap between towers (step the column by 2 or 3) so the city has streets, not a wall. Spacing is composition.

4. **Lights in the windows.** Use the colour cell properly: as each tower goes up, give some cells a bright "window" colour against the tower's dark body — same coordinate, different byte. The colour RAM stops being a flat wash and starts carrying the image. **New:** colour RAM as a parallel screen addressed by the identical formula; bright-on-dark colour to read as "a light is on". **Program:** ~17 lines. **Polish beat:** every other cell lit looks mechanical; a window here and there looks alive. Composition again — restraint reads as a real building.

5. **No two cities alike.** Bring in `RND`: randomise each tower's height, and light each window on a coin-flip, not a fixed pattern. Run it twice and get two different skylines — the program now produces more than you typed. **New:** `RND` for tower heights and for which windows light. **Program:** ~22 lines. **Polish beat:** unbounded `RND` gives ugly extremes — clamp heights to a sensible range so towers stay city-shaped. Constrained randomness is the craft.

6. **Sunset.** Set the mood with two registers: `POKE 53281` for the sky behind the towers and `POKE 53280` for the border around it. One deliberate pair of values turns a black screen into dusk — and, optionally, a soft SID tone (54272) sounds as each tower tops out. The learner now has a complete, self-composing cityscape. **New:** `POKE 53280` (border) and `53281` (background) as single-register colour; an optional one-voice SID tone. **Program:** ~26 lines. **Polish beat:** try three sky/border pairs — midnight blue, dusk violet, dawn orange — and watch the same towers tell three different times of day. The backdrop is two numbers; the feeling is the whole picture.

---

## 8. Ship Test

- [ ] Every topic's code runs on a PAL Commodore 64 (emulator + real hardware)
- [ ] Every topic produces a working, runnable result — a picture on the screen at every step
- [ ] One new BASIC concept per topic — no topic introduces two major ideas
- [ ] The `1024 + R*40 + C` formula and its `55296 + …` colour twin are used consistently, never magic-numbered cell by cell
- [ ] Gradual progression — a reader can follow from one block to the finished city without gaps
- [ ] Randomised skyline stays city-shaped — no zero-height or screen-tall towers from unclamped `RND`
- [ ] Border/background sunset reads as intended against the tower colours on a real display
- [ ] British English throughout (exception: "program")
- [ ] Screenshots show the actual running program on real hardware, not mockups
- [ ] Code samples in `/code-samples/`, not inline
- [ ] Magazine voice — warm, technical, never condescending

---

## 9. Pattern Library Extractions

- **rendering** — the screen-RAM POKE: `POKE 1024 + R*40 + C, code` with its colour twin `POKE 55296 + R*40 + C, colour`. The single most-reused technique in the volume — every game that puts a character anywhere starts here.
- **basic** — nested `FOR…NEXT` over a 2D grid: outer loop chooses the cell, inner loop fills it. The shape behind the bar chart in Tally and the grid scan in Rover.
- **rendering** — register-as-backdrop: `POKE 53280`/`53281` for border and background. One write changes the whole frame; reused for the border flash in Reflex.
- **basic** — constrained `RND`: clamp a random value to a usable range so variety stays sensible. The first appearance of randomness-as-ingredient, deepened in Oracle and Tally.

---

## 10. Vault Tie-ins

- **"Draw a picture" type-ins** — the magazine and Usborne tradition of `POKE`-listing pictures; the cultural root of memory-mapped graphics as a beginner's first wonder.
- **C64 screen memory** — the 40×25 character grid at 1024 and its colour RAM at 55296; the memory-mapped display the whole volume is built on.
- **VIC-II colour** — the 16-colour palette, the border (53280) and background (53281) registers, and why colour is a byte you write, not a keyword.
- **MOS 6510 / memory-mapped I/O** — the bridge note: the addresses Skyline POKEs are the same ones the C64 assembly track revisits at machine speed. Every POKE is a register.
