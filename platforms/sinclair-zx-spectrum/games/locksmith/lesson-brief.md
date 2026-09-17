# Locksmith — teaching progression

**Status:** The user accepted the native game and authorised development of its teaching progression. This nine-lesson decomposition uses seven independently runnable programs. Verification evidence belongs in the [implementation record](lessons.md); the overview and nine replacement lessons are now authored for local review. Publication awaits lesson approval.

**Endpoint:** Preserve `code-samples/sinclair-zx-spectrum/basic/locksmith/prototype/locksmith.bas` at samples commit `e8272b9`. The final checkpoint must be byte-identical. Four digits from 1–6, repeated digits, ten attempts, numeric EXACT/OTHER clues, visible history, editable input, R for a new round, Q to quit and deliberate silence remain unchanged.

## Central idea

**A clue counts evidence without using it twice.** Exact matches compare positions; total matches compare how many occurrences each side can supply. Subtracting exact matches leaves the right digits in other places. The history then makes separate clues useful together.

Teach the program as separate stored code, editable guess, scoring and presentation. The printed history is retained output in this accepted endpoint, not a second array of old guesses. The game never reads the display to score or choose the code. Do not imply that a colour or column marker identifies which individual digit matched.

## Progression

| Lesson | Checkpoint | Runnable result and local explanation | Question or experiment |
|---|---|---|---|
| 1. Make room for a guess | `board` | Start a new program. Draw the title, separator and four empty cells; STOP leaves it inspectable. Explain row/column coordinates, PRINT AT, colour, variables, GO SUB and RETURN where used. | Why does `5 + 2 * i` place digits in columns 7, 9, 11 and 13? |
| 2. Edit four digits | `editor` | Poll INKEY$, append valid digits, cap the string at four and erase its last character. Enter confirms a complete editable guess without scoring it. Explain strings, LEN, comparisons, slicing, CHR$ and press/release handling. | What remains after entering 123456, then deleting twice? Why does holding a key produce only one entry? |
| 3. Check the places | `exact` | Display the known practice code 1122, parse the typed digits into a numeric array and count equal positions. One result row is replaced on each submission; the same guess remains editable. Explain DIM, indexed values, VAL and loops. | Against 1122, how many exact matches do 1111, 1212 and 1122 have? |
| 4. Count each digit once | `clues` | Add frequency counts for 1–6. Sum the smaller count for each digit and subtract exact matches to produce OTHER. Explain the nested loops and why the algorithm needs both kinds of count. | Why is 1111 against 1122 scored 2 EXACT, 0 OTHER, even though a naive pairwise search can find four equal pairs? Why is 2211 scored 0 EXACT, 4 OTHER? |
| 5. Keep earlier clues | `history` | Append each result to its own row and clear the next editable guess. Stop after ten practice guesses; R clears the board with the same known code. An early correct guess does not end this inspection program. | Which state changes after submission, and which evidence must remain visible? What happens at the tenth row? |
| 6. Put the clues together | Reuse `history` | Trace the recorded 1111, 2222 and 2211 guesses against the visible practice code. Reason about possible codes from aggregate clues; no new BASIC is needed. The program is an inspection aid, not a hidden-code challenge yet. | Two ones and two twos leave six arrangements. Which arrangement survives 0 EXACT, 4 OTHER for 2211? |
| 7. Hide a new code | `round` | Replace the fixed practice code with four independent random draws, remove its display, end immediately on four exact matches and lose after ten misses. Reveal the answer and support complete replay. Explain RND, INT, RANDOMIZE and round state. | Why can the generator produce 1111? Why must the code remain unchanged between guesses? |
| 8. Invite the player in | `finished` | Add the accepted title and instructions, with S to start and Q to quit. Preserve the trial's layout, rules and result behaviour. Explain the different title, game and result loops. | Why does R start at line 200 while RUN begins at line 10? |
| 9. Keep the game | Reuse `finished` | SAVE a self-starting tape, fresh-load it through the ROM, then play, replay and quit. Distinguish program storage from saving progress in an unfinished round. | What does LINE 10 arrange when the tape loads? |

The first listing is a complete new program; do not instruct the learner to “add” every line. Later lessons use exact add/replace/delete transitions and include complete checkpoint listings. No fixed lesson length or arbitrary line budget is imposed.

## Temporary scaffolding and transitions

The practice code is deliberately visible and set with ordinary LET statements in the source. Verification enters it through the ROM; no game-state setup writes are used. The editor's “Four digits ready” response is replaced by scoring. Exact-only output gains the OTHER column when its algorithm exists. The single result row becomes a ten-row history. Practice rounds always record ten guesses, even if one equals 1122; hidden rounds then introduce immediate success. The practice-specific captions and fixed code must be removed when random rounds arrive.

The final program keeps only the active code and guess in arrays. Earlier guesses persist on screen until CLS starts a new round. Explain this modest representation accurately; do not teach a history-array subsystem that is absent from the accepted game.

## Worked examples and source leads

Use 1122 as the visible code. Compare 1111, 2222, 2211, 1212, 1234, 1112, 3456, 2111 and 1222. Every example needs both the positional check and the occurrence accounting. In particular, `total - bulls` is valid because total includes exact matches; do not describe OTHER as a second unconstrained search.

For lesson six, the executed history trace supports 1111 → 2/0, 2222 → 2/0, and 2211 → 0/4. A host enumeration can establish candidate counts as verification evidence; the learner reasons through the final six arrangements. Do not add a solver or hint feature to the game.

During prose authoring, check Steven Vickers, edited by Robin Bradbeer, *ZX Spectrum BASIC Programming*, second edition (1983): chapters 4–5 (loops and subroutines), 7–9 (expressions, strings and functions), 11–14 (random numbers, arrays, conditions and characters), 15–16 (PRINT and colour), 18 (keyboard input) and 20 (tape files). The authored lessons cite the relevant public manual chapters and link the canonical Meet BASIC setup/save routes. Essential explanations remain local.

## Verification and boundaries

Enter each checkpoint in a fresh stock 48K PAL ROM session, SAVE it and load it in a separate process. Check stored line identity, tape checksums, literal branch targets, editing reconstruction, unchanged line tokens and final source identity. An endpoint's verification does not establish an intermediate program works.

Exercise each editor independently: empty and short submission, ignored keys, four-digit capacity, deletion including empty and single-character strings, and a held key. For fixed-code stages compare known guesses with an independent occurrence-matching model. Verify single-row replacement, retention of every history row, the practice-stage correct-guess behaviour, ten-row bounds and reset semantics. Check the hidden round's two endings, replay and all available quit routes. Retain original captures and inspect the rendered output.

Native acceptance applies to the final game. Checkpoint execution and source review do not establish independent learner outcomes. No teaching stage changes the accepted game's ten-guess budget or repeated-digit rules. Performance and assembly comparisons remain deferred.
