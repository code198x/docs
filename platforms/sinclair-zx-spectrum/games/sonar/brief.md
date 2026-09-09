# Sonar — proposed replacement brief

**Status:** Sonar is selected as the next Spectrum BASIC project. This is the proposed scope and development plan; the replacement has not been prototyped or approved for lesson writing.
**Route:** Meet BASIC → Bright Spark → Volley → Touchdown → Sonar.
**Target:** Stock 48K ZX Spectrum, PAL, Sinclair BASIC, keyboard and tape save/load.
**Next session:** Begin with the bounded prototype task at the end of this brief. No work is scheduled automatically.

Apply the [project charter](../../../../PROJECT.md), [game brief specification](../../../../specifications/brief.md) and [curriculum design](../../../../specifications/curriculum.md). Earlier design assumptions remain in Git history.

## The game to investigate

A hidden object lies in one cell of a sea grid. Choose a row and column, send a probe, and read a distance clue. Each probe leaves its result on the board. Use the accumulated clues to choose the next position; finding the object ends the round. The board should let the player explain a choice, not just guess until something happens.

Start with one target on an 8×8 board. Count distinct valid probes; repeated cells and invalid input do not consume a probe. Allow as long as the player needs, and do not impose a guess limit, invented par or judgemental rating. Show the result, offer another round, and allow a clean exit. A completed small game includes instructions, play, discovery, retry, exit and a saved tape that reloads.

The proposed first version uses orthogonal distance: row difference plus column difference, with no diagonal shortcut. Explain this as the game's chosen clue rule, not a simulation of sound travelling through water. With target row 3, column 6, a probe at row 1, column 2 gives `2+4=6`; a probe at the target gives zero. The clue reports distance without direction.

## The decision to make before writing lessons

A single target with exact distances is mathematically easy to locate. On an 8×8 board, distances from opposite ends of the top row determine both target coordinates: `d1=(r-1)+(c-1)` and `d2=(r-1)+(8-c)`, hence `r=(d1+d2-5)/2` and `c=(d1-d2+9)/2`. A third probe can find it. This is a useful discovery to teach, but it may not sustain repeated rounds.

Play the exact-distance version before deciding whether it is a compact deduction game worth keeping as-is. Ask whether the player can understand a clue, make a reasoned next choice and enjoy discovering the shortcut. Do not promise a long search or obscure the shortcut merely to stretch play.

If it is too slight, compare one change at a time:

- First try distance bands with explicit meanings, such as 1–2, 3–4 and 5 or more, while retaining a distinct hit. This changes the information supplied without introducing several hidden objects or a nearest-target search.
- Consider two targets only if the one-target alternatives still lack worthwhile play. Define which target a clue refers to and whether found targets continue to affect later clues. Removing a target can make earlier nearest-target clues misleading; do not silently reinterpret old numbers or build a lesson around that ambiguity.

The target count and clue precision for the finished course are unresolved until this comparison. Multiple targets are not a promised final feature. A change to the central clue rule must be reflected in the brief before lesson drafting.

## What it adds after Touchdown

Touchdown stores one height per column. Sonar stores information at a row and column, and the player's earlier actions change that information. A turn-based program gives time to inspect the board and trace its rules without a flight loop running in the background.

Introduce two-dimensional arrays, the distinction between hidden state and the player's recorded knowledge, input validation before indexing, and distance calculated from two coordinates. Reinforce PRINT AT, PAPER, variables, conditions, nested loops, small routines and reset. Recall each idea locally; neither earlier games nor Foundations are attendance requirements.

Keep the target in two scalar variables initially. Introduce an array because the board needs to remember probes, not merely because the module is supposed to teach DIM. A proposed record is `g(row,column)=-1` for unprobed and a non-negative distance for a probe; zero means found. Explain that sentinel explicitly and initialise it with nested loops. This is a representation to test, not a claim that it is already implemented.

The board is a view of stored information. Redrawing must not generate new clues or change the hidden target. This prepares a possible later Crates project, where actions change a world grid; Crates is not yet an agreed successor.

## Appearance, controls and sound

Use bold PAPER-coloured cells from the first board, a contrasting frame, clear row/column labels and a visible probe count. Trial three character columns by two character rows per cell: an 8×8 board occupies 24×16 character cells, leaving space to investigate labels, prompts and results. Distances can reach 14, so every cell must accommodate two digits. Confirm the complete layout against the ROM's input area before fixing it.

Unknown cells, previous clues, the latest probe and a discovered target must remain distinguishable without colour. Use a symbol for a hit and a marker or highlight for the latest probe; colour reinforces the printed result. No continuous animation is needed. Explain every asset locally; custom graphics are optional only if they improve a tested display problem.

Use row/column entry first, with short string input so Q can leave and invalid text can be rejected before numeric conversion. Start with the displayed range 1–8. A keyboard-steered cursor would add repeat handling and movement state; defer it until coordinate entry proves inadequate in play.

Add short probe/discovery sounds only after the information display works. Test them by listening and ensure they do not hide essential feedback. Do not repeat sounds while waiting for input. Flight-style simultaneous controls and detailed Emu198x typing instruction are unnecessary here.

## Runnable development sequence

These are prototype checkpoints, not a fixed public lesson count. Keep changes small enough to explain and test independently.

| Stage | Result | New idea and changes | Check |
|---|---|---|---|
| 1. See the board | A labelled, coloured 8×8 board and a visible fixed target | Translate board coordinates to PRINT AT positions; recall nested loops | Corners, labels and two-digit values fit; prompts do not overwrite the board |
| 2. Send a probe | Enter a coordinate and get a hit or miss against the fixed target | Validate both coordinates before using them; separate input from the rule | Empty, fractional, out-of-range and non-numeric entries are rejected; Q exits |
| 3. Read a distance | Each valid probe reports exact orthogonal distance | Explain ABS and add the two differences; hide the target during play | Same cell, same row/column, corners and reversed differences; work the example by hand |
| 4. Remember the search | Previous clues survive and repeated cells are recognised | Introduce the 2D probe array, sentinel, lookup and full redraw from state | Repeated probes preserve the count; redraw reproduces every clue |
| 5. Finish a round | Instructions, count, discovery, retry and exit form a complete small game | Add result handling and an explicit reset contract | Find the fixed target, replay several times, quit at prompts; no state leaks between rounds |
| 6. Search a new site | A fresh random target makes each round new | Recall RND and range conversion; change target placement only | Targets always lie within the board; repeated positions on separate rounds remain valid |
| 7. Test the information | A selected clue rule supports understandable, worthwhile play | Compare exact distances with bands only if necessary; retain both sources for comparison | Human play notes explain choices and whether repeat play is worthwhile; settle scope here |
| 8. Finish and keep it | Clear display, short sounds if useful, credits and a reloadable game | Refine only observed presentation problems; explain save/load briefly | Listen, inspect both large clues and hits, save, fresh-load, play, retry and exit |

Stages 1–3 are the first investigation. Stage 5 fulfils the small fixed-site play cycle; stages 6–8 establish the intended replayable package. If array state, input or presentation makes a step too dense, split it. Do not inherit the older six lessons or invent a line limit.

## Verification and evidence

Use deterministic target positions first. Check every cell's clue against a separately calculated expectation, including the maximum distance 14 and the zero-distance hit. Check that changing only a row or column changes the expected term, and that display coordinates and array indices cannot be confused.

Exercise input cancellation at both coordinate prompts, invalid inputs, repeated misses, the winning probe, repeated retries and quitting from each permitted phase. Reset the target, board, counter, latest-probe marker, messages and temporary input state. Count the winning probe once. Do not count rejected input. Test the renderer by rebuilding the display from the stored board.

Use ROM keyboard entry and actual execution for maintained checkpoints, preserving readable keyword spaces in source. Record source hashes, emulator version, ROM/target configuration, captures and test-only starting edits separately from ordinary play. Existing Touchdown verification helpers are donors to inspect, not evidence that Sonar works. Emu198x Spectrum 0.22.1 was used for the preceding course; recheck the available release and configuration when resuming.

For play review, record the actual probes, what the player thought each clue meant, and why they chose the next position. Separate this from scripted correctness. Inspect the board and listen to any sounds; capture output only from execution. Test tape saving and loading in a fresh session before calling the package finished. No new execution, native-input, audio or original-hardware result is claimed by this plan.

Source Sinclair BASIC details from Steven Vickers, edited by Robin Bradbeer, *ZX Spectrum BASIC Programming*, second edition (Sinclair Research, 1983): chapters 4–5 (loops and routines), 7–9 (expressions, strings and functions), 11 (random numbers), 12 (arrays), 15–16 (printing and colour), 18–20 (input, sound and tape). Confirm precise passages during implementation. Original program and graphics use the samples repository's licence; prose follows the documentation licence.

## Resume here

1. Open the Code198x docs, code-samples and website repositories and read their current agent instructions/status. Read this brief and `docs/work.md`; preserve unrelated local work.
2. Inspect the older Sonar source at `code-samples/sinclair-zx-spectrum/basic/sonar/unit-01/` through `unit-06/` and its existing website lessons. They are donors and reference, not the starting program to patch into a new course. Their array mixes target and probe state and they start with three targets.
3. Create a new samples branch and `sinclair-zx-spectrum/basic/sonar/prototype/`. Implement only stages 1–3: labelled PAPER board, fixed target, validated probes and exact distance. Show the target in a diagnostic version, then hide it. Retain separate complete checkpoints.
4. Run those checkpoints on the configured 48K ROM, verify the layout and worked distance examples, and make the prototype available for native play. That runnable prototype and its evidence are the first deliverable when work resumes.
5. Continue to remembered probes and a complete round, then review the clue-rule decision with human play evidence. Fix the lesson breakdown only after the prototype supports it. Draft the replacement overview and lessons outside public collections. Use maintained CodeFromFile listings, readable keyword spacing in full and inline code, and the shared Question presentation; do not add Keyboard notes sections. Obtain lesson approval before publication and preserve the existing Sonar URLs.

This planning task ends with the saved brief. It does not start implementation or schedule a reminder. On return, “Pick up Sonar from the plan” is enough to begin at step 1.
