# Sonar — replacement brief

**Status:** Game scope agreed after play: one target on an 8×8 grid with near/medium/far clues. The banded prototype is the accepted endpoint. See the [prototype review](prototype.md) and [lesson brief](lesson-brief.md). Eleven teaching checkpoints are executed and the nine replacement lessons are approved; see the [implementation record](lessons.md) for publication status.
**Route:** Meet BASIC → Bright Spark → Volley → Touchdown → Sonar.
**Target:** Stock 48K ZX Spectrum, PAL, Sinclair BASIC, keyboard and tape save/load.
**Next work:** Maintain the approved course and its execution evidence. Keep a larger board as an optional extension.

Apply the [project charter](../../../../PROJECT.md), [game brief specification](../../../../specifications/brief.md) and [curriculum design](../../../../specifications/curriculum.md). Earlier design assumptions remain in Git history.

## The agreed game

A hidden object lies in one cell of a sea grid. Choose a row and column, send a probe, and read a distance clue. Each probe leaves its result on the board. Use the accumulated clues to choose the next position; finding the object ends the round. The board should let the player explain a choice, not just guess until something happens.

Start with one target on an 8×8 board. Count distinct valid probes; repeated cells and invalid input do not consume a probe. Allow as long as the player needs, and do not impose a guess limit, invented par or judgemental rating. Show the result, offer another round, and allow a clean exit. A completed small game includes instructions, play, discovery, retry, exit and a saved tape that reloads.

Calculate orthogonal distance: row difference plus column difference, with no diagonal shortcut. Reveal only a band: `N` for 1–2 steps, `M` for 3–4, or `F` for 5 or more. A distance of zero is a hit, shown as `*`. Explain this as the game's chosen clue rule, not a simulation of sound travelling through water. With target row 3, column 6, a probe at row 1, column 2 gives `2+4=6`, so the player sees `F`. The clue gives no direction.

## Scope and teaching comparison

One target, banded clues and an 8×8 board are agreed. The user accepted the banded version as good as it is after play. Retain a larger board as an optional extension, not a requirement for the finished game. More cells can yield more broad far readings and also require a new display and input layout. Multiple targets are outside this scope.

Retain the exact-distance prototype as a teaching comparison. On an 8×8 board, exact distances from opposite ends of the top row determine both target coordinates: `d1=(r-1)+(c-1)` and `d2=(r-1)+(8-c)`, hence `r=(d1+d2-5)/2` and `c=(d1-d2+9)/2`. This is useful evidence of how clue precision changes play. Explain the calculation before grouping distances into bands; do not require learners to discover the algebraic shortcut to continue.

## What it adds after Touchdown

Touchdown stores one height per column. Sonar stores information at a row and column, and the player's earlier actions change that information. A turn-based program gives time to inspect the board and trace its rules without a flight loop running in the background.

Introduce two-dimensional arrays, the distinction between hidden state and the player's recorded knowledge, input validation before indexing, and distance calculated from two coordinates. Reinforce PRINT AT, PAPER, variables, conditions, nested loops, small routines and reset. Recall each idea locally; neither earlier games nor Foundations are attendance requirements.

Keep the target in two scalar variables initially. Introduce an array because the board needs to remember probes, not merely because the module is supposed to teach DIM. Prototype stage 4 introduces `g(row,column)=-1` for unprobed and a non-negative distance for a probe; zero means found. Explain that sentinel explicitly and initialise it with nested loops. The target remains separate from the array of revealed clues. In the accepted banded endpoint, the stored non-negative value is instead a clue code: 0 for a hit, 1 for near, 2 for medium and 3 for far. The lesson sequence introduces bands before remembered clues, so its array stores these codes from the outset.

The board is a view of stored information. Redrawing must not generate new clues or change the hidden target. This prepares a possible later Crates project, where actions change a world grid; Crates is not yet an agreed successor.

## Appearance, controls and sound

Use bold PAPER-coloured cells from the first board, a contrasting frame, clear row/column labels and a visible probe count. Use the verified layout of three character columns by two character rows per cell: an 8×8 board occupies 24×16 character cells, leaving space for labels, prompts and results. The exact-distance comparison can reach 14, so cells accommodate two digits as well as the final letter clues.

Unknown cells, previous clues, the latest probe and a discovered target must remain distinguishable without colour. Use a symbol for a hit and a marker or highlight for the latest probe; colour reinforces the printed result. No continuous animation is needed. Explain every asset locally; custom graphics are optional only if they improve a tested display problem.

Use row/column entry first, with short string input so Q can leave and invalid text can be rejected before numeric conversion. Start with the displayed range 1–8. A keyboard-steered cursor would add repeat handling and movement state; defer it until coordinate entry proves inadequate in play.

The accepted game is silent. Printed clues and the result message provide its feedback; sound is not outstanding completion work. Flight-style simultaneous controls and detailed Emu198x typing instruction are unnecessary here.

## Runnable development sequence

These are the prototype investigation checkpoints, not the public lesson count. The [lesson brief](lesson-brief.md) orders the teaching stages around the accepted banded game. Keep changes small enough to explain and test independently.

| Stage | Result | New idea and changes | Check |
|---|---|---|---|
| 1. See the board | A labelled, coloured 8×8 board and a visible fixed target | Translate board coordinates to PRINT AT positions; recall nested loops | Corners, labels and two-digit values fit; prompts do not overwrite the board |
| 2. Send a probe | Enter a coordinate and get a hit or miss against the fixed target | Validate both coordinates before using them; separate input from the rule | Empty, fractional, out-of-range and non-numeric entries are rejected; Q exits |
| 3. Read a distance | Each valid probe reports exact orthogonal distance | Explain ABS and add the two differences; hide the target during play | Same cell, same row/column, corners and reversed differences; work the example by hand |
| 4. Remember the search | Previous clues survive and repeated cells are recognised | Introduce the 2D probe array, sentinel, lookup and full redraw from state | Repeated probes preserve the count; redraw reproduces every clue |
| 5. Finish a round | Instructions, count, discovery, retry and exit form a complete small game | Add result handling and an explicit reset contract | Find the fixed target, replay several times, quit at prompts; no state leaks between rounds |
| 6. Search a new site | A fresh random target makes each round new | Recall RND and range conversion; change target placement only | Targets always lie within the board; repeated positions on separate rounds remain valid |
| 7. Test the information | Accepted near/medium/far clues support the small deduction game | Band the exact distance and retain the exact version for comparison | Boundary checks and human play passed; 8×8 banded scope is agreed |
| 8. Finish and keep it | Clear instructions, credits and a reloadable silent game | Refine only observed presentation problems; explain save/load briefly | Inspect clues and hits, save, fresh-load, play, retry and exit |

Stages 1–3 are the first investigation. Stage 5 fulfils the small fixed-site play cycle; stages 6–8 establish the intended replayable package. If array state, input or presentation makes a step too dense, split it. Do not inherit the older six lessons or invent a line limit.

## Verification and evidence

Use deterministic target positions first. Check every cell's clue against a separately calculated expectation, including the maximum distance 14 and the zero-distance hit. Check that changing only a row or column changes the expected term, and that display coordinates and array indices cannot be confused.

Exercise input cancellation at both coordinate prompts, invalid inputs, repeated misses, the winning probe, repeated retries and quitting from each permitted phase. Reset the target, board, counter, latest-probe marker, messages and temporary input state. Count the winning probe once. Do not count rejected input. Test the renderer by rebuilding the display from the stored board.

Use ROM keyboard entry and actual execution for maintained checkpoints, preserving readable keyword spaces in source. Record source hashes, emulator version, ROM/target configuration, captures and test-only starting edits separately from ordinary play. Existing Touchdown verification helpers are donors to inspect, not evidence that Sonar works. Emu198x Spectrum 0.22.1 was used for the preceding course; recheck the available release and configuration when resuming.

For play review, record the actual probes, what the player thought each clue meant, and why they chose the next position. Separate this from scripted correctness. Inspect the board and listen to any sounds; capture output only from execution. Test tape saving and loading in a fresh session before calling the package finished. The samples verification records own execution results. General positive feedback on the opening checkpoints does not establish replay value, specific native-input acceptance, audio quality or original-hardware behaviour.

Source Sinclair BASIC details from Steven Vickers, edited by Robin Bradbeer, *ZX Spectrum BASIC Programming*, second edition (Sinclair Research, 1983): chapters 4–5 (loops and routines), 7–9 (expressions, strings and functions), 11 (random numbers), 12 (arrays), 15–16 (printing and colour), 18–20 (input, sound and tape). Confirm precise passages during implementation. Original program and graphics use the samples repository's licence; prose follows the documentation licence.

## Resume here

1. Read this brief, the [prototype review](prototype.md), `docs/work.md` and the samples prototype README. Preserve unrelated local work in each repository.
2. Use `sonar/teaching/` for maintained lesson checkpoints. Its final program equals `prototype/experiments/distance-bands.bas`; the earlier prototypes remain comparison evidence.
3. Follow the [lesson brief](lesson-brief.md) and [implementation record](lessons.md). Verify any changed checkpoint rather than assuming the accepted endpoint covers it.
4. Maintain CodeFromFile listings, readable keyword spacing and the shared Question presentation. Preserve existing public URLs and the topic-based redirects when changing content. The larger board is optional and outside the approved default.
