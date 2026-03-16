# Game 04: Hot and Cold

**Track:** Spectrum BASIC
**Genre:** Grid search game
**Units:** 8
**Language:** Sinclair BASIC
**Max lines:** ~75 (five rounds with results screen)

---

## Premise

A treasure is hidden somewhere on screen. You can't see it. All you have is a cursor and the border colour — which shifts from black (freezing) through blue, magenta, red, yellow, to white (found it) as you get closer.

Move the cursor with Q/A/O/P. Watch the border. Find the treasure. Five rounds, total moves tracked. Fewer moves = better score.

This is where PRINT AT arrives. Everything before this used sequential output — text appearing wherever the cursor happened to be. From here on, the learner places things at exact coordinates. The cursor moves on a grid, the border responds to position, and the game loop pattern (read input, update state, draw) becomes second nature.

---

## Core Mechanics

The screen is a grid (rows 1-20, columns 0-31). A treasure position is chosen at random. The cursor starts at the centre. Each frame: check INKEY$ for Q/A/O/P, move the cursor, calculate Manhattan distance, set the border colour. When cursor reaches the treasure, flash a star, BEEP, next round.

Distance-to-colour mapping:

| Distance | Border | Meaning |
|----------|--------|---------|
| 0 | White (7) | Found it |
| 1-3 | Yellow (6) | Burning |
| 4-7 | Red (2) | Warm |
| 8-14 | Magenta (3) | Warmer |
| 15-24 | Blue (1) | Cold |
| 25+ | Black (0) | Freezing |

---

## Unit Breakdown

### Unit 1: Placing Text

**Concept:** PRINT AT row,column — exact positioning on the grid

Place the title, instructions, and status line at specific positions. The screen is a 24×32 grid. PRINT AT puts text exactly where you want it.

---

### Unit 2: The Cursor

**Concept:** Position variables, drawing a character at coordinates

A "+" character at position `r`,`c`. Change the variables and the cursor moves. Erase the old position by printing a space, draw at the new position.

---

### Unit 3: Four Directions

**Concept:** INKEY$ for movement, Q/A/O/P, boundary checking

Q moves up (r-1), A down (r+1), O left (c-1), P right (c+1). The cursor moves freely. Boundary checks prevent it leaving the playing area.

---

### Unit 4: The Hidden Treasure

**Concept:** Random target position, ABS, Manhattan distance

A random position `tr`,`tc` is chosen. Calculate distance: `ABS(r-tr)+ABS(c-tc)`. Nothing visible yet — just print the distance on screen so the learner can see it change as they move.

---

### Unit 5: Hot and Cold

**Concept:** Distance-to-colour mapping, the game comes alive

Map the distance to border colours with IF/THEN chains. The border shifts as the player moves — the game becomes playable. Remove the distance display — the border IS the feedback now.

---

### Unit 6: Found It!

**Concept:** Win detection, celebration, the game loop

When distance = 0, flash a green star at the treasure position, play ascending BEEPs, show a "Found!" message. The complete single-round game.

---

### Unit 7: Five Rounds

**Concept:** FOR/NEXT wrapping a game, round counter, total moves

Five rounds, each with a new random treasure. Track moves per round and total. Display round number and running total on the status line.

---

### Unit 8: Results and Polish

**Concept:** Results screen, rating tiers, the complete game

After five rounds, show total moves and a rating. Fewer moves = better tier. The finished game with header, status line, five rounds, and results.

---

**Milestone:** The learner can place text anywhere on screen with PRINT AT, move a character with INKEY$, calculate distance, and build a complete game loop. Position-based thinking — coordinates, boundaries, distance — is now natural.

---

## Changelog

- **v2.0 (2026-03-16):** Rewritten with richer unit descriptions. Added five rounds and results screen to prototype.
- **v1.0 (2026-03-13):** Initial game outline for v5.0 curriculum.
