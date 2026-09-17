# Locksmith — prototype record

The user selected Locksmith after the [remaining-course review](../../basic/course-review.md), then accepted the native trial: “Locksmith is great”. The [bounded brief](brief.md) owns the game scope. The source and self-starting tape live in `code-samples/sinclair-zx-spectrum/basic/locksmith/prototype/`.

## Accepted experience

One four-digit code, digits 1–6 with repetitions, ten guesses, a visible history and numeric EXACT/OTHER clues. The player edits a guess before submitting, then reasons from aggregate feedback. Each code occurrence can count only once. The code remains fixed within a round. R generates a new round; Q exits. No time pressure, audio, hints or machine-code helper.

The old source's frequency-count approach is retained, with input validation, an editable four-digit field and a complete one-screen history. The earlier brief's exclusion of repeated digits is superseded by the accepted trial. Neither colour nor screen contents participate in scoring.

## Execution evidence

Emu198x Spectrum 0.25.0, stock 48K PAL. The source was entered through ROM keyboard tokens, saved with `SAVE "locksmith" LINE 10`, and loaded through the ROM in a fresh process. Verification reads the generated secret to choose and evaluate trials; it never writes secrets, guesses, score variables or screen state.

`verification/evidence/results.json` records 18 passed check groups and 42 scored guesses, including four complete ten-attempt losing rounds and two immediate wins. The independent host model first removes exact pairs and then consumes unmatched occurrences. Actual BASIC uses per-digit frequency counts and subtracts exact matches. The traces retain inputs and both expected clue counts, and every submitted history row is checked.

Checks cover ignored characters, incomplete submission, D and ROM DELETE, deleting an empty guess, held keys, excess digits, success, exhaustion, result stability, replay and quit from title/play/result. Source and tape hashes, stored line identities, branch targets, both TAP block checksums and line-10 autostart are audited in `verification/evidence/manifest.json`.

Original title, board, mid-round, win and loss captures were visually inspected. The review found stale “enter four digits” advice behind the revealed code; line 5200 now clears that row. Line 5000 uses “Attempts used” to avoid a plural label on a one-guess win. Both changes were entered through the ROM and saved, followed by the complete fresh-load regression run. The user played the version with source SHA-256 `b094a9a92c854ba3e6c1f09e57e39ab7aed3735c1b726ae48bd5df67a56d7d85`; the maintained version differs only in these result-display lines. Native acceptance applies to the same rules and difficulty; the subsequent display cleanup has automated and visual verification.

## Teaching handoff

The [nine-lesson progression](lesson-brief.md) has seven [executed teaching checkpoints](lessons.md), with the final source identical to this baseline. Next author the overview and replacement lessons from those maintained programs. Published earlier Locksmith lessons remain unchanged. Assembly and performance investigations remain deferred.
