# Three in a Row — proposed BASIC prototype

**Status:** The user selected an opponent-design review. This bounded prototype is recommended by the [source review](review.md); its specific scope and play experience are not yet accepted. Existing published lessons remain available during development.

**Target:** Stock 48K PAL ZX Spectrum, Sinclair BASIC. No machine-code helper or expansion. Maintain prototype sources in `code-samples/sinclair-zx-spectrum/basic/three-in-a-row/prototype/` when implementation begins. Enter and save through the ROM, then fresh-load a self-starting tape for execution checks and native play.

## Experience

Play noughts and crosses against an opponent whose decisions you can inspect. A single 3×3 board uses keys 1–9 in reading order. The human places X; the computer places O. Three matching marks in a row, column or diagonal wins. A full board without a winner draws. Keep the final board and deciding move visible so the player can explain what happened.

The first trial should use the retained priority: take an immediate win, block an immediate loss, then prefer centre, corners and edges. It is deliberately fallible. Give each computer move a short truthful reason, such as “O chose 5: centre” or “O chose 9: block”. The caption reports the branch taken; it must not pretend that the program considered a deeper plan.

Start the first round with the human, then alternate the starter after each completed round so both roles are available without another menu. Keep a small session win/loss/draw tally. R restarts or begins another round, and Q quits. Restarting an unfinished round preserves its starter and does not change the tally. Explain whose turn it is and who starts the new round.

## Presentation and controls

Use a large centred board, substantial X and O marks and small numbers only in empty cells. Shapes and labels carry the meaning; colour helps distinguish turns. Draw the accepted move before evaluating and presenting its result. Highlight a winning line without hiding the rest of the board. Reserve a stable area for the opponent's reason and the result/replay controls.

Read a single 1–9 key press to choose a square. Ignore unrelated keys; reject occupied cells without spending a turn. Wait for release so a held key cannot become another move after the computer replies. The prototype should be silent, keeping attention on the board and explanations; sound can be reconsidered only if play benefits from it. Artwork should be original and represented directly in BASIC or a small locally explained character table.

## Representation and learning

Keep a nine-element board and the eight winning triples from the existing implementation. Geometry draws the state; it never determines ownership or wins. Reuse a line scan to find both opportunities and threats, with the side being tested supplied explicitly. Resolve ties deterministically and document the order. Match the displayed explanation to the chosen branch.

The central idea is **a decision depends on both the rules and their priority**. Taking a win before blocking is observable. So is the limitation of considering only the next move: a fork offers two threats that cannot both be blocked. The retained counterexample provides an experiment before any stronger strategy is introduced.

Suggested runnable teaching stages, subject to the accepted prototype:

| Stage | Result | Idea to explain | Check |
|---|---|---|---|
| Draw and place | Numbered board accepts a legal human mark | Flat array, display mapping and validated keys | Empty/occupied squares and held input |
| Read a result | Completed lines and draws are detected | DATA triples and shared evaluation | All eight lines for both marks; win before draw |
| Choose a reply | Computer chooses an empty square | Candidate moves and a definite tie order | No overwrite or move after the round ends |
| Win and block | Immediate opportunities outrank threats | Reusable evaluation and ordered rules | Position with both a winning move and a blocking move |
| Explain the fallback | Centre/corner/edge choices have visible reasons | Heuristics and their limits | Retained fork trace and a drawn game |
| Finish the session | Both starters, retained result, replay, tally and tape | Round versus session state | Complete fresh-load, play, replay and quit cycle |

These are teaching possibilities, not an agreed unit count. Introduce presentation and input quality during development, not as an unexplained final rewrite.

## Boundaries and verification

One board, one readable opponent and one short repeatable round are enough for this trial. No tournament, campaign, network play, larger board, difficulty menu, mandatory unbeatable policy or arbitrary line budget. Performance/assembly comparisons remain deferred.

Use an exhaustive host traversal to check the exact implemented policy under both starters. Record reachability, legal moves, terminal results and counterexamples; never present path frequencies as player win rates. A host model supplements fresh-ROM execution and cannot establish BASIC timing or display correctness.

Native checks must cover every winning line, a full-board draw, a last-cell win, illegal/occupied keys, held keys across a computer turn, both starters, result stability, reset without counting an abandoned round, tally updates exactly once and quit from title/play/result. Check the move-reason caption against the actual decision. Preserve and inspect original captures, then let the user judge pace, clarity and whether beating the rule-based opponent is satisfying.

If the opponent feels exhausted after one discovered exploit, that is evidence for revisiting its policy. If its reason text explains away all the fun or makes the screen busy, try a quieter presentation before expanding features. Native acceptance establishes the baseline for full lesson authoring.
