# Sonar prototype review

The replacement's first six stages live in `code-samples/sinclair-zx-spectrum/basic/sonar/prototype/`. They progress from a visible-target board diagnostic through validated probes and exact distances to remembered clues, a complete fixed-site round and random placement. The original published six-lesson Sonar course is unchanged. The banded variant is the accepted game endpoint; the replacement teaching sequence is described in the [lesson brief](lesson-brief.md).

## What this prototype establishes

The 8×8 board fits labels, a frame and three-character clue cells above the ROM input area. A cell is three character columns wide and two rows high. `>` marks the latest probe, a dot means unknown and `*` means found; colour is supplementary. Stages 1–5 use a fixed target at row 3, column 6; stage 6 chooses a random target for each round. The first checkpoint's `>14` is explicitly a layout diagnostic.

Row and column are read separately as strings with `INPUT LINE`. Only a single digit from 1 to 8 reaches `VAL`. Q exits from either prompt. Long input can expand the ROM input area and scroll the board, so answers longer than sixteen characters trigger reconstruction of the board, diagnostic target where applicable, and latest marker before rejection. Status prints do not advance beyond the last output row.

The target remains two scalar variables. From stage 4, `g(row,column)` stores the player’s knowledge: `-1` for unprobed, otherwise the revealed distance, with zero for a hit. New valid probes increment the counter once, including the winning probe; repeats and invalid input do not. Revisiting a cell moves the latest marker without discarding earlier clues. The cell renderer serves both ordinary updates and complete redraws.

Stage 5 adds instructions and a discovery/retry/exit cycle. Retry recreates the array and clears the count, latest marker, status and input state. Stage 6 changes target selection to two `INT (RND * 8) + 1` expressions. It seeds once after the player starts, then continues the random sequence across retries. Separate rounds may legitimately place a target in the same cell. All stages retain Q exit and RUN restart. No probe limit, rating or sound has been introduced.

The retained samples evidence passes on released Emu198x Spectrum 0.25.0 with the configured 48K ROM. It includes all 64 fixed-target distances, maximum-distance corner checks with labelled target edits, invalid-input and long-input recovery, both quit prompts, and ROM tape saving and automatic loading in fresh processes. The executed captures were visually inspected. Native host-keyboard behaviour, human enjoyment and original hardware remain separate, unverified claims.

The stages 4–6 checks additionally cover all 64 stored clues, unchanged counts on repeated probes, complete reconstruction after clearing the display, repeated fixed-site resets, all exit phases and twelve random rounds. Each later tape was loaded in a fresh emulator process and played; the complete-round versions also retried after loading. Target range and observed variation passed. These observations do not establish generator uniformity or whether people want another round.

## Exact clues and the next design decision

The mathematical investigation in `prototype/verification/deduction.py` enumerates all 64 target positions. In every case, exact clues from `(1,1)` and `(1,8)` identify one target. The ordinary fixed target gives 7 and 4; the third probe can be `(3,6)`. This confirms the brief's shortcut, rather than showing that a player discovered or enjoyed it.

The user reported that the playable versions worked well, found a second target in four moves, and described a binary-style search. They then requested more interesting deduction and surprises. This motivates comparing clue precision; it does not establish a preferred final rule.

The user played the separate `prototype/experiments/distance-bands.bas` variant and accepted the game as good as it is. The agreed endpoint keeps one target and an 8×8 board, reporting near (1–2 steps), medium (3–4), or far (5+), with a distinct hit. A larger board is an optional extension. Exact-distance stages 1–6 remain useful comparison evidence. No detailed banded probe trace was supplied, so this is qualitative acceptance by one player, not measured beginner difficulty.

The banded execution record checks distance boundaries, a hit, repeated probes, long-input recovery, retry, eight random rounds solved from revealed clues, and ROM saving and fresh loading. Captures were visually inspected. The final game remains silent. Its experimental source path is retained to preserve existing evidence references; it now identifies the selected endpoint.

## Next work

The [teaching implementation](lessons.md) contains eleven executed checkpoints and nine approved lessons. That record owns publication status. The selected rule and board size remain stable.

The samples README owns running instructions. Its verification scripts and results own configuration-specific execution evidence; this document records the teaching and game-design implications.
