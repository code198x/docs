# Locksmith — teaching implementation

The user accepted the native baseline and authorised the teaching progression. Seven independently ROM-entered checkpoints now support the [nine-lesson brief](lesson-brief.md). Sources live under `code-samples/sinclair-zx-spectrum/basic/locksmith/teaching/`. The final source is byte-identical to the accepted prototype at samples commit `e8272b9`. Replacement lesson prose and publication remain outstanding.

## Maintained programs

| Lessons | Checkpoint | Executed result |
|---|---|---|
| 1 | `board` | Four empty digit cells and an inspectable static board |
| 2 | `editor` | Validated four-digit editing, deletion, held-key handling and confirmation |
| 3 | `exact` | Exact-position counts against visible practice code 1122 |
| 4 | `clues` | Both aggregate clues, with correct repeated-digit accounting |
| 5–6 | `history` | All ten practice guesses retained; correct guesses do not end the inspection program |
| 7 | `round` | Hidden random codes, immediate success, ten-guess exhaustion and complete replay |
| 8–9 | `finished` | Accepted title, controls, presentation and complete game; saving reuses this source |

The fixed practice code and captions disappear when random rounds arrive. The editor's confirmation is replaced by scoring, the single result row becomes a history, and only hidden rounds introduce immediate success. No accepted game rules, difficulty, controls or sound choices changed.

## Execution and audit

`verification/evidence/manifest.json` records **80 passed execution check groups and 52 scored guesses**. Every program was independently entered through stock 48K PAL ROM keyword keys, saved to a line-10 auto-starting TAP, then loaded into a fresh Emu198x Spectrum 0.25.0 process. Tests send keys and inspect state; they never write the secret, guess, result or display.

Every interactive checkpoint independently checks empty and short submission, ignored characters, four-digit capacity, D and Spectrum DELETE, deleting an empty guess and a held key. Fixed-code trials exercise zero through four exact matches, misplaced matches including four OTHER, repeated values and excess occurrences. The independent model removes exact pairs and consumes remaining matching occurrences; BASIC counts per-digit frequencies. The history trial also checks that an early correct guess keeps the practice program running, that all earlier rows remain visible, and that ten submissions lead to its practice ending.

Both complete-game stages exercise random-code success, a full losing round, result stability, replay and quit. The final program additionally checks title exit. The accepted prototype retains its separate 18-group native-trial verification; this teaching evidence does not substitute for it.

The audit reconstructs each source from the preceding source and its exact editing manifest, checks literal targets, compares unchanged line tokens between independently entered programs, verifies TAP block checksums and stored program bytes, checks source identities and confirms the final byte-for-byte match. Original captures of static, editing, scoring, history and complete-game states were visually inspected. The initial board's capture includes the ROM STOP report; it is an inspection stage.

## Deduction example

The actual history trial records:

| Guess | EXACT | OTHER | Codes consistent with all clues so far |
|---|---|---|---|
| 1111 | 2 | 0 | 150 |
| 2222 | 2 | 0 | 6 |
| 2211 | 0 | 4 | 1: 1122 |

`verification/evidence/history/deduction.json` retains these values. A host enumeration of the 1,296 possible codes verifies the candidate counts. The learner can reason through the final six arrangements without implementing that enumeration. This is a visible-code worked example; no solver or hint system is added to the game.

## Authoring handoff

Author the overview and nine lessons from the maintained listings and exact transitions. Treat the first program as new rather than enumerating every line to add. Explain each temporary practice behaviour and its replacement. Keep input, stored numeric state, scoring and the printed history distinct: the endpoint does not keep a history array or read its picture to apply rules.

Check the brief's primary-manual source leads and shared setup/save routes during prose authoring. Include repeated-digit counterexamples and the recorded deduction trace. Native approval applies to the final game; independent learner outcomes remain untested. Performance/assembly investigations stay deferred, and the earlier published Locksmith lessons remain available until replacements are approved.
