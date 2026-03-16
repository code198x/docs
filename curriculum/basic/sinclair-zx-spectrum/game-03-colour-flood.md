# Game 03: Colour Flood

**Track:** Spectrum BASIC
**Genre:** Visual toy / screen-filling patterns
**Units:** 8
**Language:** Sinclair BASIC
**Max lines:** ~60 (pattern picker with six patterns)

---

## Premise

Fill the Spectrum's screen with colour. Stripes, checkerboards, diagonals, random splashes — each pattern is just a few lines of code, and the results are immediate and vivid. The learner types a short program and watches colour flood across the display.

This is the first game where the result is primarily visual. Previous games produced text with colour accents; this one IS colour. The learner sees the direct connection between a loop and a row of coloured blocks, between a nested loop and a filled grid. FOR/NEXT stops being an abstract concept about repetition and becomes a tool for painting the screen.

By the end, the learner has a pattern picker — a program that cycles through six visual patterns at the press of a key. The satisfaction comes from making beautiful things appear on screen.

---

## Core Mechanics

Each unit builds a new pattern. The final program is a menu-driven pattern picker: press 1-6 to fill the screen with a different visual. The patterns progress from simple (one loop, one colour) to complex (nested loops, calculated colours, BRIGHT mode).

---

## Unit Breakdown

### Unit 1: Counting

**Concept:** FOR/NEXT, loop variable, STEP

The learner's first FOR/NEXT loop: print the numbers 1 to 10. Then 1 to 100. Then 10 to 1 using STEP -1. See how the loop variable changes each time through.

This is the formal introduction to FOR/NEXT — they used it briefly in Game 2 (five rounds) and saw it in Lucky Number's header bar, but here they learn how it works from the ground up.

---

### Unit 2: The Border Rainbow

**Concept:** BORDER, the 8 colours (0-7), loops with colour

Use FOR/NEXT to cycle the border through all eight colours with a PAUSE between each. The border sweeps through the rainbow — the learner's first colour animation.

Introduce the colour numbers: 0=black, 1=blue, 2=red, 3=magenta, 4=green, 5=cyan, 6=yellow, 7=white.

---

### Unit 3: Paper and Ink

**Concept:** PAPER, INK, how CLS fills with PAPER, BRIGHT

Set PAPER before CLS to flood the entire screen with a colour. Print coloured text with INK. Use BRIGHT 1 for brighter shades. Build a colour chart: eight PAPER colours × normal and bright.

---

### Unit 4: Horizontal Stripes

**Concept:** FOR/NEXT with PRINT AT, filling rows with colour

Use a FOR/NEXT loop to fill each row with a different PAPER colour. The screen fills with horizontal stripes — the rainbow repeating every eight rows. The formula `PAPER (r - INT(r/8)*8)` wraps the colour number back to 0 after reaching 7.

**Visual moment:** Rainbow stripes flooding the screen row by row.

---

### Unit 5: Vertical Stripes

**Concept:** Column-by-column printing, swapping the formula

Change the colour formula from row-based to column-based: `PAPER (c - INT(c/8)*8)`. The stripes turn 90 degrees. Same loop, different formula, completely different visual.

**Visual moment:** Vertical rainbow stripes — the horizontal pattern rotated.

---

### Unit 6: Nested Loops

**Concept:** Nested FOR/NEXT, the screen as a grid, diagonal formula

Put one FOR/NEXT inside another: outer loop counts rows, inner loop counts columns. The screen fills cell by cell. Use `r+c` in the colour formula to create diagonal stripes — each diagonal line is a different colour.

**Visual moment:** Diagonal rainbow stripes cascading across the screen.

---

### Unit 7: Checkerboard

**Concept:** Even/odd logic, two-colour patterns, BRIGHT variations

If `r+c` is even, use one colour. If odd, use another. The screen fills with a checkerboard. Change the colours. Add BRIGHT to one colour for a three-tone pattern. The formula `INT((r+c)/2)*2=(r+c)` tests for even/odd.

**Visual moment:** Red and yellow checkerboard filling the screen.

---

### Unit 8: Pattern Picker

**Concept:** Menu system, code organisation, RND for random patterns, creative application

Combine all patterns into one program with a menu. Press 1-6 to choose: horizontal stripes, vertical stripes, checkerboard, random splash, diagonal, BRIGHT stripes. The random splash uses `PAPER INT(RND*8)` per cell — every cell a random colour.

**Visual moment:** The random splash — a mosaic of every colour, different every time.

---

**Milestone:** The learner understands FOR/NEXT loops, nested loops, STEP, and the Spectrum's colour model (8 colours, PAPER/INK/BORDER, BRIGHT). They can fill the screen with any pattern they can describe in terms of rows, columns, and colour formulae.

---

## Changelog

- **v2.0 (2026-03-16):** Rewritten for visual-first approach. Added pattern picker as capstone. Expanded to ~60 lines.
- **v1.0 (2026-03-13):** Initial game outline for v5.0 curriculum.
