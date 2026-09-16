# Sonar — lesson brief

**Status:** The 8×8, one-target banded game is agreed after play. This breakdown now has eleven executed teaching checkpoints and nine lesson drafts. See the [implementation and review record](lessons.md). The user approved the nine lessons; publication work is recorded in the implementation record.

**Endpoint:** `code-samples/sinclair-zx-spectrum/basic/sonar/prototype/experiments/distance-bands.bas`, with its retained `verification/bands-results.json`. Apply the [game brief](brief.md), [unit specification](../../../../specifications/unit.md) and [content workflow](../../../../specifications/content-creation-workflow.md).

## Teaching shape

Build the accepted game through nine lessons. The count follows the changes in what the learner must understand; split a lesson if its runnable stages become too dense. It does not inherit the published course's six units or the prototype's investigation order.

Introduce the clue rule before the array, so the learner records near/medium/far results from the first remembered search. Use a fixed target until the reset and round cycle work. Keep exact distances as a short, runnable explanation of the calculation and an optional deduction exercise; the final game reveals bands.

| Lesson | Result the learner can run | Changes and local explanation | Check before continuing |
|---|---|---|---|
| 1. A sea to search | Labelled 8×8 board with a visible fixed target | Recall PRINT AT, PAPER and nested loops. Separate board row/column from character positions. Grow a row into the complete board rather than supplying an unexplained renderer. | Predict and display all four corner cells; labels, frame and target fit above ROM input. |
| 2. Send a probe | Enter a row and column; see a hit or miss | Read strings with INPUT LINE, allow Q, reject invalid text before VAL. Explain LEN, string comparisons, routine calls and the returned numeric value locally. Show one coordinate prompt before reusing it for the other. | Blank, 0, 9, text, expressions and fractional input stay at the same prompt. Q works at either prompt. A long answer restores the board; an invalid column retains the selected row. |
| 3. Measure the distance | Hidden target and an exact distance at the latest probe | Explain ABS as a non-negative difference and add row and column differences. Remove the visible target. Show why distance supplies information without direction. | Work `(1,2)` to `(3,6)` by hand: 6. Test same row, same column, reversed differences, zero and opposite corners. |
| 4. Read the sonar | Latest probe shows N, M, F or a hit | Group distances into 1–2, 3–4 and 5+. Distinguish measured distance, clue code and displayed letter. Explain the branch order, including why a far distance must not be classified again after conversion. Add the visible legend when the symbols appear. | Predict results at distances 0, 1, 2, 3, 4, 5 and 14. Explain why F does not mean exactly five steps. |
| 5. Remember the clues | Every revealed clue remains on the board | Introduce DIM with two indices, then initialise unknown cells to -1 using nested loops. Keep target coordinates separate. First inspect an initialised array, then store and render a probe. Zero is a hit, so it cannot also mean unknown. | Probe two different cells and see both clues. Read an unprobed cell without revealing the target. Explain which values represent knowledge and which represent the hidden world. |
| 6. One probe, one count | Repeats preserve the count; a full redraw restores the search | Read the array before calculating a new clue. Count only previously unknown cells, including the hit. Separate drawing from rule changes. Move the latest marker without losing the earlier result. | Probe A, B, A: count is two and both clues remain. Clear and rebuild the display without changing target, clues or count. Reject long input after several probes and retain the same history. |
| 7. A complete round | Instructions, discovery, retry and quit against the fixed target | Give zero its ending behaviour; explain the round restart separately from a subroutine return. Reset the array, count, marker, messages and temporary input. Keep the fixed target to expose stale state. | Find the target, reject an invalid replay answer, retry several times, and quit from instructions, either coordinate prompt and the result screen. |
| 8. Search somewhere new | Random target on every new round | Recall RND, INT and range conversion. Seed once after starting, continue the sequence on retry, and explain why the same site may legitimately recur. | Confirm both coordinates stay within 1–8. Each retry starts with no clues and count zero. Solve several rounds using the displayed bands. |
| 9. Keep your game | Saved game reloads into instructions and supports a complete round | Explain SAVE with LINE, the program name and matching LOAD, using the canonical setup workflow. Revisit instructions, readability and provenance. No extra mechanic is introduced to make the final lesson look larger. | Save, load in a fresh emulator session, play, retry and quit. Compare the final teaching program with the accepted endpoint and record any deliberate differences. |

The fixed-site round in lesson 7 is already a complete small game. Lessons 8–9 fulfil the agreed random-round, reloadable endpoint. The accepted version is silent; audio is not an unfinished requirement.

## Questions that earn their place

Use the shared Question presentation, with a visible prompt and an explanation that can be revealed. Keep these tied to concrete states rather than adding a vocabulary quiz to every lesson.

- With target `(3,6)`, why do probes `(1,6)` and `(3,4)` both read near? Each is two orthogonal steps away, although the direction differs.
- Why initialise the array to -1 instead of accepting DIM's zeros? Zero already represents a discovery; an untouched board must not look like 64 hits.
- After probing A, B, then A again, which values change? The latest marker moves back to A; the two stored clues and distinct-probe count stay the same.
- Why must a redraw leave the count alone? Drawing presents stored knowledge; otherwise recovering a scrolled display would change the game.
- Does a repeated random target prove that RND is broken? No. Independent rounds can select the same cell; a valid range and one repeated outcome do not establish the generator's distribution.

An optional exact-distance exercise can compare two top-corner clues, with the coordinate derivation available as an explanation. Do not make algebraic fluency a gate to the banded game. An open probe-choice question should accept different justified strategies; use the consistency of all known clues as the criterion.

## Source and evidence work

The prototype establishes the endpoint and useful donor routines. It does not supply every teaching state in this order. Maintain complete listings under a new `sonar/teaching/` tree, with exact add/replace/delete instructions and source-backed snippets for the prose. Keep readable keyword spacing in maintained files; ROM token entry may suppress redundant spaces only at its boundary.

Derive and execute each checkpoint before writing claims about its output. Reuse the existing ROM keyboard-entry and observation helpers. Retain source hashes, target configuration, declared fixed-target edits, input sequences and inspected captures. Verify band boundaries independently from the program's classification branches, and preserve input, redraw and reset checks when those features enter the teaching sequence. Do not transfer the full endpoint's passing result to a simplified program.

Use Vickers, edited by Bradbeer, *ZX Spectrum BASIC Programming*, second edition (1983): chapters 4–5 for loops and routines, 7–9 for names and expressions, 11 for random numbers, 12 for arrays, 15–16 for screen/input behaviour and colour, and 20 for tape. Check passages as each explanation is authored. The distance model and bands are game rules, not claims about physical sonar.

Draft the overview and units outside public website collections. Use CodeFromFile for maintained full states, explicit BASIC line edits for changes, and the shared Question and Sources components. No Keyboard notes sections are needed. The overview should show the finished game and its simple controls without exposing verification machinery to the learner.

## Optional extension and publication

A larger board is a later experiment. Revisit cell dimensions, row/column labels, accepted input, coordinate bounds and clue usefulness together; changing a single 8 is not a complete extension. Keep the default game at 8×8 and do not introduce it as a promised additional lesson.

Before publication, review the actual teaching sources, execution evidence and prose together. Inspect narrow/wide layouts, code rendering, keyboard-accessible questions, media and links using the website's checks. Preserve the existing Sonar URLs through an explicit topic-based redirect map if the unit structure changes. Update the catalogue, overview and Touchdown onward route only when the replacement content is ready; a lesson plan alone does not change public availability.
