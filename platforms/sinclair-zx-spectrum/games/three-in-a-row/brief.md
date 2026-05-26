# Three in a Row — Brief

**Title (working):** Three in a Row
**System / Track:** Sinclair ZX Spectrum / BASIC
**Position:** Volume 2, Game 5 of 8 (slot 13)
**Headline concept:** Adversary — the program plays against you
**Embedded concept:** AI personality — the computer's "style" emerges from simple rules
**Topics:** 10 topics, ~10–14 hours
**Constraint position:** period-faithful
**Status:** draft

Format: [`specifications/brief-basic.md`](../../../../specifications/brief-basic.md)

---

## 1. Pedagogical Role

Teach that a program can evaluate board positions and make choices — the simplest form of game AI — so the learner arrives at The Caverns understanding that "the computer thinks" is really "the computer follows rules the programmer wrote."

---

## 2. Classic Ancestors

- **Tic-Tac-Toe / Noughts and Crosses** — the universal pen-and-paper game. Two players, a 3×3 grid, three in a line wins. Solved (perfect play always draws), but the process of *learning* to play perfectly is the lesson.
- **OXO** (Alexander Douglas, 1952) — one of the earliest computer games, a tic-tac-toe implementation on the EDSAC. The tradition of "teach the computer to play noughts and crosses" is as old as computer games themselves.

---

## 3. Core Experience

You and the computer take turns placing marks on a 3×3 grid. The computer plays to win — it blocks your threats, takes winning moves, and picks sensible positions. You try to outthink it. Most games end in a draw; the satisfaction is in *understanding why*.

---

## 4. Visual Direction

- **The board.** A 3×3 grid drawn with PRINT characters (lines and intersections). Large cells — each one fills several character positions for readability.
- **X and O.** Player's mark in one colour (cyan), computer's in another (red). Distinct at a glance.
- **Position numbers.** Empty cells show their number (1–9) so the player knows which number to type.
- **Magazine-screenshot test:** a mid-game board — X in the corner, O in the centre, two moves each — the reader analysing who has the advantage.

---

## 5. Audio Direction

- **Player move.** Short neutral tone — acknowledgement.
- **Computer move.** Different short tone — "my turn."
- **Win.** Ascending fanfare for the winner (player or computer).
- **Draw.** A flat tone — stalemate.

---

## 6. Level Design Direction

- **Content source:** No DATA needed — the board is a 3×3 array, the AI is algorithmic.
- **Difficulty curve.** The AI has three tiers: (1) random moves, (2) blocks player wins, (3) blocks + takes wins + prefers centre/corners. The learner builds each tier as a separate topic, seeing the AI get smarter.
- **Scale:** One 3×3 board. A game lasts 5–9 moves.
- **Onboarding:** Against the random AI (tier 1), the player always wins. This teaches the interface. Against the smart AI (tier 3), draws become common — this teaches the game's depth.

---

## 7. Anti-goals

- No variable board size — always 3×3. Larger boards (Connect Four, Gomoku) are different games.
- No unbeatable AI — the tier-3 AI plays well but not perfectly. Minimax is beyond V2 scope.
- No network play — one player vs computer only.
- Maximum ~60 lines of BASIC.

---

## 8. Topic Progression

1. **The board.** DIM a 3×3 array: `DIM b(3,3)`. Draw an empty board with PRINT AT. Number each cell 1–9. **New:** 2D array as a board (reinforces Sonar). **Program:** ~10 lines.

2. **Player moves.** INPUT a position (1–9). Convert to row/column. Place the player's mark in the array and on screen. Reject occupied cells. **New:** mapping a single number to 2D coordinates (`row = INT((n-1)/3)+1`, `col = ((n-1) MOD 3)+1`). **Program:** ~16 lines.

3. **Win detection.** Check all 8 winning lines (3 rows, 3 columns, 2 diagonals). If any line has three matching marks, that player wins. **New:** checking multiple conditions across a 2D array, the concept of "winning lines." **Program:** ~24 lines.

4. **Computer moves — random.** The computer picks a random empty cell. Simple, beatable, but the game now has two players. **New:** finding a random empty cell (loop until `b(r,c) = 0`). **Program:** ~28 lines.

5. **Computer moves — blocking.** Before picking randomly, the computer checks: can the player win on their next move? If so, block that cell. **New:** threat detection (scanning winning lines for "two player marks + one empty"). **Program:** ~34 lines.

6. **Computer moves — winning.** Before blocking, the computer checks: can *it* win on this move? If so, take that cell. Win → block → random: a three-tier priority. **New:** opportunity detection (same scan, for computer's marks). **Program:** ~38 lines.

7. **Computer moves — strategy.** After win/block checks, prefer centre (cell 5) if empty, then corners (1,3,7,9), then edges (2,4,6,8). The AI now plays well — draws are common against an attentive player. **New:** positional preference as strategy. **Program:** ~44 lines.

8. **Draw detection.** If all 9 cells are filled and nobody won, it is a draw. Display "Draw!" — and congratulate the player, because drawing against a decent AI is respectable. **New:** full-board detection. **Program:** ~46 lines.

9. **Who goes first?** Ask the player: "Do you want to go first? (Y/N)." If the computer goes first, it picks centre. The game feels different depending on who opens. **New:** turn-order choice, the concept that first-move advantage matters. **Program:** ~50 lines.

10. **Make it yours.** Title screen. Win/loss/draw record across rounds. The design lesson: the AI's "personality" — cautious, aggressive, strategic — emerged entirely from the priority order of simple rules. No intelligence, just authored behaviour. That is the headline concept: **Adversary** means "a program that appears to think." **New:** none (polish + design reflection). **Program:** ~55 lines.

---

## 9. Ship Test

- [ ] Every topic's code runs on a 48K Spectrum
- [ ] Win detection catches all 8 winning lines
- [ ] AI correctly blocks immediate player wins
- [ ] AI correctly takes immediate wins for itself
- [ ] AI prefers centre → corners → edges when no immediate threat/opportunity
- [ ] Draw detection works when board is full
- [ ] Player cannot place in an occupied cell
- [ ] British English throughout ("noughts and crosses" not "tic-tac-toe" in prose)
- [ ] Code samples in `/code-samples/`
- [ ] Magazine voice

---

## 10. Pattern Library Extractions

- **ai** — three-tier priority AI: win → block → prefer. The simplest decision-making pattern that produces convincing play. Cross-platform.
- **ai** — threat/opportunity scanning: checking winning lines for "two of mine + one empty." The pattern behind every board-game AI that evaluates positions.
- **basic** — number-to-grid mapping: converting a single input (1–9) to row/column coordinates. The pattern for any grid interface that uses numbered cells.

---

## 11. Vault Tie-ins

- **Noughts and Crosses / Tic-Tac-Toe** — the universal game as cultural ancestor.
- **OXO** (Alexander Douglas, 1952) — one of the earliest computer games.
- **Game AI** — the design principle that authored rules create the *appearance* of intelligence.
