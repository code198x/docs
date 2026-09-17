# Three in a Row — opponent review

**Status:** The user selected this review after Locksmith's publication. The next prototype scope in [brief.md](brief.md) is a recommendation, not an accepted game. Existing public lessons and samples remain unchanged.

## What the source implements

The retained endpoint is `code-samples/sinclair-zx-spectrum/basic/three-in-a-row/unit-06/three-in-a-row.bas`. Six existing lessons lead to it. The board is a one-dimensional nine-element array, with zero for empty, one for X and two for O. A DATA table supplies eight winning triples. The computer takes an immediate win, otherwise blocks an immediate player win, otherwise chooses centre, the first free corner in 1/3/7/9 order, or the last empty cell in numeric order. That last rule emerges because lines 830–840 keep overwriting mv.

The source always lets the human start as X. It draws marks with PLOT/DRAW and CIRCLE, reads moves through numeric INPUT, clears the display for endings, retains win/loss/draw totals and offers replay. It has no normal quit command and no explanation of an opponent move. The inherited brief's two-dimensional array, UDG artwork and starter choice are absent. Its “No DATA needed” claim disagrees with the winning-line table, and its MOD expression is not the subtraction-based mapping used by the samples.

## A counterexample to the lesson

The strategy lesson claims the opponent plays soundly and cannot be beaten by a careful player. Its policy has no fork handling. The following legal sequence defeats the source's deterministic choices, using the board's top-left-to-bottom-right numbering:

| Turn | Mark and cell | Why the computer chooses its reply |
|---|---|---|
| 1 | X at 1 | Human opening |
| 2 | O at 5 | Centre preference |
| 3 | X at 8 | Human move |
| 4 | O at 3 | First remaining corner |
| 5 | X at 7 | Creates threats at both 4 and 9 |
| 6 | O at 9 | The 7/8/9 triple appears before 1/4/7 in the block scan |
| 7 | X at 4 | Completes 1/4/7 |

The fork is two distinct winning next moves. Blocking one leaves the other. This is a concrete boundary of the policy, not evidence that immediate win/block checks are useless.

[verification/review.py](verification/review.py) pins the final source by SHA-256, reads its DATA triples and traverses every legal human reply against a direct translation of its choice routine. On each computer turn, separate trial-placement checks verify legality, immediate-win priority and immediate blocking when there is no winning move. [review.json](verification/review.json) records 247 distinct computer-turn positions and 489 terminal move sequences: 12 human wins, 127 draws and 350 computer wins.

Those counts are paths through a model, not probabilities for human play. This review does not run BASIC or establish input response, drawing, sound or native playability. Replay the counterexample on the Spectrum during the prototype work, then compare the revised BASIC's decisions with its model. Only the inherited player-first mode is covered here.

The earlier course review also called the lesson's line 330 reference absent. It exists in the actual unit-05 source included by that lesson; the final unit-06 source moves that draw check to 320. The invincibility claim is the substantive defect.

## Presentation and input findings

The final source checks a result before returning to the board redraw, and its ending routines immediately CLS. The deciding mark and final position are therefore not preserved for inspection. That removes exactly the evidence an opponent-design game should let the player study.

Range checking at 260 does not explicitly require an integer. Numeric INPUT also exposes BASIC expression entry rather than a one-key square selection. Native behaviour for unusual input was not tested here. A direct 1–9 key editor can make the accepted command set explicit, reject occupied cells without changing turns and provide release handling.

The retained presentation uses a 96-pixel square board, full-screen redraws and different sound cues, including a multi-note player win. No visual or audio judgement is inferred from reading that code. The proposed prototype should use more of the screen, preserve the final board and make whose turn it is clear in words as well as mark shapes.

## Recommended decision

Build one deliberately fallible rule-based opponent first. Keep win → block → centre → corners → edges, and report the rule that actually selected the move. This makes the program's choice inspectable, gives the player an exploitable weakness and supports a later fork experiment. Describe it as rule-based, without claiming it can force a draw.

An unbeaten opponent is a different endpoint. If the trial becomes uninteresting as soon as its weakness is found, investigate a fork-aware upgrade or bounded lookahead and prove the resulting claim over all legal replies. Do not add difficulty menus or minimax before that play evidence. A stronger opponent that draws every careful game may be useful for comparison, but it is not automatically a more enjoyable first game.

Three in a Row is a candidate for Boards and deduction: Locksmith combines clues about hidden state; this game evaluates shared visible state to choose an action. Keep the essential array, table and priority explanations local. There is no fixed lesson count or inherited Volume 2 prerequisite.
