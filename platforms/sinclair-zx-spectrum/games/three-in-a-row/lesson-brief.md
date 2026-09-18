# Three in a Row — teaching progression

**Status:** Native game accepted; lesson development authorised. Ten lessons use eight independently runnable checkpoints. The user-approved overview and ten replacement lessons are published, with production and live checks passed.

**Endpoint:** Preserve `code-samples/sinclair-zx-spectrum/basic/three-in-a-row/prototype/three.bas` from samples commit `46ca3c6` byte-for-byte. The human plays X, the computer O. Win → block → centre → first free corner → last free edge remains the deliberately fallible policy. Visible reasons, silence, retained results, session tally, alternating completed-round starters and R/Q controls remain unchanged.

## Central idea

**The priority of rules is part of a decision.** A board is stored separately from its drawing. One table supplies winning triples; another lists corner preferences. The same immediate-opportunity routine can answer either “can O win?” or “must O block X?”. A truthful branch caption does not imply a safe or deeply planned move. The worked fork demonstrates that limit.

## Sequence

| Lesson | Checkpoint | Result and explanation |
|---|---|---|
| 1. Draw nine squares | `board` | New program, numbered grid, nine-element array, character versus pixel coordinates, loops and subroutine return. STOP retains the board. |
| 2. Place a cross | `place` | Direct 1–9 keys, empty-cell validation, release gate and substantial X drawing. All nine cells may contain X; no turn or result rule yet. |
| 3. Take turns | `turns` | Local two-player X/O turns, octagonal O, move count and a separate full-board waiting loop. Completing a line does not yet end play. |
| 4. Read a winning line | `results` | Eight DATA triples, RESTORE, shared winner scan, winning-line highlight and win-before-draw result. Two-player rules now complete. |
| 5. Choose an empty square | `reply` | Replace O input with a first-empty policy. Explain choice versus placement and the nonterminal-board contract. Human win 1/5/9 stops before another O reply. |
| 6. Win before blocking | `tactics` | Shared opportunity routine receives mark, returns mv; win priority precedes block, with first-empty fallback. Legal 1/3/7/6 trace ends in O winning at 8 instead of blocking at 9. |
| 7. Prefer useful squares | `policy` | Centre, first free corner in 1/3/7/9 order, last free edge. Explain both tie rules and limited lookahead. |
| 8. Make two threats | Reuse `policy` | Work through X 1/8/7/4 against O 5/3/9. At X7 two winning gaps exist; reversing the scan only changes which is left open. No new source. |
| 9. Finish the session | `finished` | Accepted title, tally, retained ending, alternating starters and restart semantics. Round state begins at 200; session state begins at 10/20. |
| 10. Keep the game | Reuse `finished` | SAVE with LINE 10, exported tape, fresh ROM LOAD, play/replay/reset/quit. Program storage versus unfinished match state. |

## Transitions and local explanations

The first source is a complete new program. Later sources have exact add/replace/delete instructions and maintained ordinary `changes.bas` listings, with full sources available separately. `checkpoints.json` records those transitions. Deletion means entering a BASIC line number alone. No diff notation is required.

Presentation grows with the rules: grid and numbering first, X with input, O with turns, winning highlight with detection, captions with computer decisions. The title and session do not replace the game with unexplained supplied code. Temporary two-player turn state, practice endings and RUN-based round restart are removed explicitly when their replacement exists.

Questions explain coordinate mapping, numeric ownership, incomplete rules, empty-line rejection, first versus last candidate, routine input/output, fork limits, state lifetime and tape entry points. Worked paths and branch reasons must match each particular checkpoint, not merely the final game.

## Verification

Each checkpoint is entered in a fresh 48K PAL ROM using keyword keys, saved to a self-starting TAP and loaded in a separate process. Audit exact edit reconstruction, unchanged-line token identity, branch targets, tape checksums, autostart and final-source identity. Use the final prototype suite again against the independently entered finished checkpoint.

Check ignored/occupied/held input, reset, both marks, stable endings, drawn and won rounds, reasons and the legal worked traces. Separate ROM-command fixtures cover all sixteen mark/line combinations and simultaneous win/block opportunities; they use no direct memory writes and are not public play captures. Inspect original images and desktop/mobile lesson rendering. Native acceptance does not establish independent learner outcomes.

Language sources: Steven Vickers, edited by Robin Bradbeer, *ZX Spectrum BASIC Programming*, second edition (1983), chapters 4–7, 9, 12–13, 15–18 and 20. Public lessons cite relevant public manual chapters and canonical Meet BASIC setup/save instructions. Performance/assembly comparisons remain deferred.
