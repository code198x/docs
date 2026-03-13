# Game 03: Colour Flood

**Track:** Spectrum BASIC
**Genre:** Visual toy / screen-filling patterns
**Units:** 8
**Language:** Sinclair BASIC
**Max lines:** ~25

---

## Premise

Fill the Spectrum's screen with colour. Stripes, blocks, checkerboards, random splashes — each pattern is just a few lines of code, and the results are immediate and vivid. The learner types a short program and watches colour flood across the display.

This is the first game where the result is primarily visual. Previous games produced text; this one produces colour. The learner sees the direct connection between a loop and a row of coloured blocks, between a nested loop and a filled grid. FOR/NEXT stops being an abstract idea about repetition and becomes a tool for painting the screen.

The Spectrum has eight colours (0 to 7), a BRIGHT mode that doubles them to sixteen shades, and three colour controls: BORDER (the edge), PAPER (the background), and INK (the foreground). The learner explores all of these, building a small collection of visual patterns they can combine and modify.

---

## Core Mechanics

Each unit adds a new pattern or technique. By the end, the learner has a program that cycles through several patterns — stripes, checkerboards, colour washes — with keypresses to advance between them. The program is a visual toy rather than a scored game: the satisfaction comes from making beautiful things appear on screen.

---

## Unit Breakdown

| Unit | Title | What the learner builds | New concepts |
|------|-------|------------------------|--------------|
| 1 | Counting | Use FOR/NEXT to print the numbers 1 to 10. Change the range. Print a word ten times. See how the loop variable changes each time through. | FOR/NEXT, loop variable |
| 2 | The border | Use BORDER to change the screen border colour. Loop through all eight colours (0 to 7) with FOR/NEXT and a short PAUSE between each. The border cycles through the rainbow. | BORDER, the 8 colours (0-7): black, blue, red, magenta, green, cyan, yellow, white |
| 3 | Paper and ink | Use PAPER and INK to change the background and text colours. Print coloured text. Use CLS after setting PAPER to flood the whole screen with a background colour. | PAPER, INK, how CLS fills the screen with the current PAPER colour |
| 4 | Horizontal stripes | Use a FOR/NEXT loop to print 32 spaces with a different PAPER colour on each row. The screen fills with horizontal stripes — one colour per row, cycling through all eight. | Using PAPER inside a loop, printing spaces to fill a row, the screen as 24 rows of 32 columns |
| 5 | Vertical stripes | Use a FOR/NEXT loop across the columns. Print one coloured space at a time, changing INK or PAPER every few columns. The screen fills with vertical stripes. | Column-by-column printing, controlling colour per character cell |
| 6 | Nested loops | Put one FOR/NEXT inside another: the outer loop counts rows, the inner loop counts columns. Fill the entire screen cell by cell. Change the colour based on the row, the column, or both. | Nested FOR/NEXT loops, the screen as a 24x32 grid |
| 7 | Checkerboard | Use the row and column numbers together to decide the colour of each cell. If row + column is even, use one colour; if odd, use another. The screen fills with a checkerboard. Add BRIGHT for a third variation. | Odd/even logic, BRIGHT, combining row and column values |
| 8 | Pattern picker | Combine all the patterns into one program. The player presses a key to cycle between stripes, checkerboard, random splash (using RND to pick colours), and a custom pattern of the learner's own design. | Organising code into sections, building a menu, creative application of everything learnt |

**Milestone:** The learner understands FOR/NEXT loops, nested loops, and the Spectrum's colour model. They can fill the screen with any pattern they can describe in terms of rows, columns, and colours.

---

## Technical Notes

### Key Variables

```
r   - row counter (outer loop, 0 to 23)
c   - column counter (inner loop, 0 to 31)
k   - colour number (0 to 7)
```

### Line Numbering

The final program uses roughly lines 10-250. Each pattern occupies a block of 20-30 lines. A menu section at the top lets the player pick a pattern.

### Memory

Negligible. Under 700 bytes.

### The Spectrum Colour Model

- Eight colours numbered 0-7: black (0), blue (1), red (2), magenta (3), green (4), cyan (5), yellow (6), white (7).
- INK sets the foreground (text) colour. PAPER sets the background colour. BORDER sets the screen edge colour.
- BRIGHT 1 makes colours brighter (effectively 16 shades). BRIGHT 0 returns to normal.
- Colour is set per character cell (8x8 pixels), not per pixel. Each cell has one INK colour and one PAPER colour. This "attribute clash" is a defining feature of the Spectrum's display.
- Setting PAPER before CLS fills the entire screen with that background colour.

### Spectrum-Specific Notes

- PRINT with no text but a colour control (e.g. `PRINT PAPER 2;" "`) prints a single coloured space. A row of 32 spaces fills one screen row.
- No ELSE keyword. The checkerboard pattern uses two separate IF/THEN lines (one for even, one for odd) or a calculated expression for the colour number.
- FOR/NEXT loops on the Spectrum always execute at least once, even if the start value exceeds the end value. This rarely matters here but is worth knowing.

---

## Changelog

- **v1.0 (2026-03-13):** Initial game outline for v5.0 curriculum.
