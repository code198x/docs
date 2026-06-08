# Hi-Lo — Brief

**Title (working):** Hi-Lo
**System / Track:** Sinclair ZX Spectrum / BASIC
**Position:** Volume 1, Game 7 of 8
**Headline concept:** Narrowing — feedback brings you closer
**Embedded concept:** Feedback loops — each response refines the next action
**Topics:** 5 topics, ~5–7 hours
**Constraint position:** period-faithful

Format: [`specifications/brief-basic-v1.md`](../../../../specifications/brief-basic-v1.md)

---

## 1. Pedagogical Role

Teach the loop-until-condition pattern — a loop that doesn't count iterations but runs until something specific happens — so the learner understands that not all loops are FOR/NEXT, and arrives at Touchdown with the structural vocabulary for game loops that run "until the game ends."

---

## 2. Classic Ancestors

- **Hi-Lo card games** — the casino/pub tradition. A card is dealt; the player guesses whether the next card will be higher or lower. Simple binary prediction against a sequence of reveals.
- **Play Your Cards Right** (ITV, 1980–) — the Bruce Forsyth game show. "Higher! Lower!" as audience participation. The mechanic entered British popular culture through television before it appeared in type-in listings.

---

## 3. Core Experience

A number appears. Will the next one be higher or lower? Guess right — your streak grows. Guess wrong — game over. Each correct guess narrows your sense of what's likely, but the next number can always surprise you. Fast rounds, instant stakes, and the tension of a winning streak you don't want to break.

---

## 4. Visual Direction

- **Playing card display.** Each number shown as a card — PAPER 7 (white) rectangle drawn with PRINT AT (7 rows x 9 columns). Value (A, 2-9, 10, J, Q, K) at top-left and bottom-right corners.
- **Suit UDGs.** Four 8x8 pixel characters (spade, heart, diamond, club) defined with DATA/READ/POKE at game start (CHR$ 144-147). Hearts and diamonds in INK 2 (red); spades and clubs in INK 0 (black) against the white card.
- **Two-card layout.** Current card revealed (value + suit visible), next card face-down. Player guesses H or L, next card flips.
- **New unit: "The Cards"** (inserted after unit 5). Defines suit UDGs, writes card-drawing subroutine, replaces number display with card visuals. Design concept: **Representation** — the same data shown differently changes the experience. "You just taught the Spectrum what a heart looks like."
- INVERSE header bar with streak and best score. BRIGHT on title.
- **Unit count: 11** (was 10).

---

## 5. Audio Direction

- **Correct BEEP.** Short ascending tone — relief, continuation.
- **Wrong buzz.** Low, harsh — the streak is over.
- **No other sound.** The game's rhythm is decision → reveal → reaction. Sound marks the reveal only.

---

## 6. Anti-goals

- No cards — pure numbers, not a card-game simulation. No suits, no deck, no card graphics. The mechanic is abstracted to its essence: higher or lower.
- No betting — no score beyond the streak. No currency, no risk/reward calculation.
- No difficulty settings — the range (1–100 or 1–13) is fixed. The difficulty is inherent in the probability.
- No arrays or stored history — each round is one comparison: current number vs next number.
- Maximum ~25 lines of BASIC.

---

## 7. Topic Progression

1. **Two numbers.** Generate two random numbers: `LET a = INT(RND*13)+1` and `LET b = INT(RND*13)+1`. Print both. Which is higher? The learner can see the answer. This is the raw material — two numbers and a comparison. **New:** reinforcement of RND/INT (familiar ground). **Program:** 4 lines. **Polish beat:** use a range of 1–13 (like cards) or 1–100? The range changes how the game feels.

2. **The player guesses.** Show only the first number. Ask: `INPUT "Higher or lower (H/L)? "; g$`. Then reveal the second number. Compare: `IF g$ = "H" AND b > a THEN PRINT "Correct!"`. `IF g$ = "L" AND b < a THEN PRINT "Correct!"`. Otherwise: `PRINT "Wrong!"`. One guess, one result. **New:** string comparison (`g$ = "H"`), AND for compound conditions. **Program:** ~10 lines. **Polish beat:** what happens when the numbers are equal? That's a design decision — draw counts as wrong, or as a freebie?

3. **Keep going.** Wrap the game in a loop: after a correct guess, the second number becomes the new first number (`LET a = b`), generate a new `b`, and go round again. The loop runs until the player gets one wrong. This is the **loop-until-condition** pattern — not FOR/NEXT (which counts), but GO TO with an exit branch. **New:** loop-until-condition (the structural pattern, not a new keyword), variable reassignment as state transition (`a = b`). **Program:** ~14 lines. **Polish beat:** the moment the streak breaks — does it feel fair? If `b` equals `a`, the player had no information. Handle it.

4. **The streak.** Add a counter: `LET streak = 0`, increment on each correct guess. Display at a fixed position with PRINT AT. When the game ends, the streak is the score. Add colour: green BORDER on correct, red on wrong. Add a rating: streak of 5+ is "Impressive!", 10+ is "Unstoppable!". **New:** PRINT AT for persistent score display, streak as score. **Program:** ~20 lines. **Polish beat:** the streak number is the only thing the player cares about. Make it visible. Make it big.

5. **Make it yours.** Add a title screen. Add a "Play again?" prompt at game over (`INPUT "Again? (Y/N) "; r$`, `IF r$ = "Y" THEN GO TO 10`). Add a best-streak tracker: `IF streak > best THEN LET best = streak`. Display the best streak alongside the current one — now the player is competing against themselves across rounds. **New:** best-score tracking with a comparison variable, replay loop. **Program:** ~25 lines. **Polish beat:** the best-streak display turns a throwaway game into something you play for ten minutes. One variable changes the entire relationship.

---

## 8. Ship Test

- [ ] Every topic's code runs on a 48K Spectrum (emulator + real hardware)
- [ ] Every topic produces a working, runnable result
- [ ] Loop-until-condition pattern is clearly distinct from FOR/NEXT — the learner understands "loop until something happens" vs "loop N times"
- [ ] Equal-number case is handled explicitly (not silently wrong)
- [ ] Streak counter updates correctly and is visible during play
- [ ] Best-streak tracking persists across rounds within a single run
- [ ] AND compound condition is explained — not just shown
- [ ] British English throughout
- [ ] Screenshots show actual running programs
- [ ] Code samples in `/code-samples/`
- [ ] Magazine voice

---

## 9. Pattern Library Extractions

- **basic** — loop-until-condition: `GO TO` with an `IF` exit branch. The pattern for "keep going until X happens" — structurally different from FOR/NEXT. The foundation of every game loop, menu loop, and retry loop. Cross-platform.
- **basic** — state transition via reassignment: `LET a = b` — the outgoing value becomes the incoming value. The pattern behind every "next round" transition in turn-based games.
- **basic** — best-score tracking: `IF score > best THEN LET best = score`. The simplest persistent metric — one comparison, one variable, infinite replayability.

---

## 10. Vault Tie-ins

- **Hi-Lo card games** — the casino/pub tradition as cultural ancestor.
- **Play Your Cards Right** (ITV, 1980–) — Bruce Forsyth's game show; how the mechanic entered British popular culture.
- **Feedback loops in game design** — the design principle that each player action should produce information that shapes the next action.
