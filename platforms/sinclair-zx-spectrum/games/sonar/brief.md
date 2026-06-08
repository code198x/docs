# Sonar — Brief

**Title (working):** Sonar
**System / Track:** Sinclair ZX Spectrum / BASIC
**Position:** Volume 2, Game 4 of 8 (slot 12)
**Headline concept:** Search — coordinates as a way of knowing
**Embedded concept:** Systematic search — pattern-based exploration beats random guessing
**Topics:** 10 topics, ~10–14 hours
**Constraint position:** period-faithful

Format: [`specifications/brief-basic.md`](../../../../specifications/brief-basic.md)

---

## 1. Pedagogical Role

Teach 2D arrays as a grid data structure — so the learner arrives at Three in a Row able to represent and reason about a board with rows and columns.

---

## 2. Classic Ancestors

- **Battleship** (Milton Bradley, 1967) — the grid-based guessing game. Place ships on a hidden grid; the opponent calls coordinates; you report hit or miss. The mechanic: spatial reasoning through coordinate-based search.
- **Hunt the Wumpus** proximity variant — the "you sense something nearby" mechanic, where distance-based clues guide the search.

---

## 3. Core Experience

A 10×10 grid hides three targets. You call coordinates — row and column. A miss shows how far the nearest target is. A hit marks the cell. Find all three targets in as few guesses as possible. The distance clue turns blind guessing into informed search — each probe narrows the possibilities.

---

## 4. Visual Direction

- **DRAW pixel grid** — horizontal and vertical pixel lines creating 8×8 board. Each cell 3 chars wide × 2 rows tall. Grid drawn via FOR loops with PLOT/DRAW. Reinforces DRAW in structured context. Grid looks like a proper board game.
- Heat-map distance colours unchanged (red close, yellow medium, cyan far). Colours pop against the drawn grid.
- **Probe ping animation:** BORDER flashes the distance colour for 5 frames, then resets. Visual "ping" feedback on each probe.
- Title screen: DRAW radar sweep — three radial lines from a centre point with CIRCLE concentric rings (~3 CIRCLE + DRAW). Suggests sonar/radar scanning.

---

## 5. Audio Direction

- **Hit.** Ascending fanfare — a target found.
- **Near miss (distance 1–2).** A tense high tone — close.
- **Far miss (distance 5+).** A low flat tone — nothing here.
- **All found.** Celebration.

---

## 6. Level Design Direction

- **Content source:** Three targets placed randomly on the grid at game start. Stored in a 2D array or as coordinate pairs.
- **Difficulty curve.** The grid size (10×10) and target count (3) are the difficulty parameters. Fewer targets on a bigger grid is harder. The learner can adjust both.
- **Scale:** One grid per round. A round lasts 15–30 guesses for a methodical player.
- **Pacing.** Early guesses are uninformed — the player is mapping the space. Mid-game, distance clues create convergence zones. Late-game, the last target is the hardest — the grid is full of old clues.
- **Onboarding.** The first guess teaches the distance mechanic — whatever number appears, the player learns "that number means distance."

---

## 7. Anti-goals

- No ships or elongated targets — targets are single cells. Ship placement and hit/sink tracking are beyond V2 scope.
- No two-player mode — the computer hides targets, the player searches.
- No fog of war clearing — every cell shows its result permanently. The grid is a record of the search.
- Maximum ~50 lines of BASIC.

---

## 8. Topic Progression

1. **The grid.** `DIM g(10,10)`. Draw a 10×10 grid of dots with nested FOR loops and PRINT AT. Add row and column labels. **New:** DIM with two dimensions, nested FOR for grid drawing. **Program:** ~10 lines.

2. **Hidden targets.** Place three targets at random positions: `LET g(r,c) = 1` for each. The grid still shows dots — the targets are invisible. **New:** using a 2D array to store hidden state. **Program:** ~16 lines.

3. **Probing a cell.** INPUT row and column. Check `g(r,c)` — if 1, it is a hit; mark it. If 0, it is a miss. Display the result on the grid. **New:** 2D array lookup by player-supplied coordinates. **Program:** ~20 lines.

4. **Distance clues.** On a miss, calculate the distance to the nearest target. Display that number in the cell instead of a blank miss marker. The distance is the game's core information channel. **New:** distance calculation across a 2D grid (loop through targets, compute `ABS(r1-r2) + ABS(c1-c2)`, keep the minimum). **Program:** ~26 lines.

5. **Colour by distance.** Near misses (1–2) in red, medium (3–4) in yellow, far (5+) in blue. The grid becomes a heat map — the player sees warm and cool zones before reasoning about specific numbers. **New:** colour-coding driven by computed values (reinforces Lucky Number's border pattern, now in 2D). **Program:** ~30 lines.

6. **Counting and winning.** Track hits. When all 3 targets are found, the player wins. Display the guess count. If guesses exceed 30, game over — reveal the remaining targets. **New:** win condition across multiple scattered targets, revealing hidden state at game end. **Program:** ~34 lines.

7. **Guess history.** The grid itself *is* the history — every probed cell shows its result permanently. Add a guess counter visible at all times. Add sound (hit/near/far). The grid is now a visual record of a systematic search. **New:** sound-by-distance (reinforces Reflex rating pattern). **Program:** ~40 lines.

8. **Duplicate checking.** Reject guesses for cells already probed: `IF g(r,c) <> 0 THEN PRINT "Already probed!"`. Saves the player from wasting guesses. **New:** state-based input validation. **Program:** ~42 lines.

9. **Replay and difficulty.** "Play again?" + new random targets. Optional: INPUT grid size (5×5 easy, 10×10 standard, 15×15 hard) and target count. `DIM g(n,n)` resizes. **New:** parameterised grid dimensions. **Program:** ~46 lines.

10. **Make it yours.** Title screen. Add a rating based on guess efficiency — par for 3 targets on a 10×10 grid is about 15 guesses. Under par is "Sonar expert!", over 25 is "Keep searching." Teach the design lesson: the same grid engine works for any search game — treasure hunts, minesweepers, exploration. **New:** none (polish + design reflection). **Program:** ~50 lines.

---

## 9. Ship Test

- [ ] Every topic's code runs on a 48K Spectrum
- [ ] 2D array correctly sized and indexed
- [ ] Three targets placed at distinct random positions (no overlap)
- [ ] Distance calculation is correct (Manhattan distance to nearest target)
- [ ] Colour coding maps correctly to distance ranges
- [ ] Already-probed cells are rejected
- [ ] Win condition fires when all 3 targets found
- [ ] British English throughout
- [ ] Code samples in `/code-samples/`
- [ ] Magazine voice

---

## 10. Pattern Library Extractions

- **basic** — DIM 2D arrays: grid storage for spatial game state. The foundation of every board game, map, and level layout.
- **basic** — nearest-target distance: loop through targets, compute Manhattan distance, keep minimum. The simplest spatial-proximity algorithm.
- **rendering** — colour-by-value on a grid: mapping computed values to INK colours at specific PRINT AT positions. A 2D heat map in character cells.

---

## 11. Vault Tie-ins

- **Battleship** (Milton Bradley, 1967) — grid-based search as cultural ancestor.
- **Coordinate geometry in games** — the design principle that spatial reasoning through coordinates creates a different quality of engagement than pixel-level interaction.
- **Systematic search** — the strategy principle that patterned exploration (every third cell, diagonal sweeps) outperforms random probing.
