# Sonar — teaching checkpoints and drafts

**Status:** The user approved the overview and nine replacement lessons. They are published at [Sonar](https://code198x.com/systems/sinclair-zx-spectrum/basic/sonar/), with eleven executed teaching checkpoints.

## Maintained work

- Samples: `sinclair-zx-spectrum/basic/sonar/teaching/`, including complete listings, exact edit snippets, `roster.json`, derivation and verification scripts, results and captures.
- Website: `src/content/curriculum/sinclair-zx-spectrum/basic/sonar/`, with an overview and nine approved units. The route is `/systems/sinclair-zx-spectrum/basic/sonar/`. Review and publication evidence remain under `src/drafts/sonar/`.
- Direction: [game brief](brief.md), [lesson brief](lesson-brief.md) and [prototype review](prototype.md).

The teaching sequence begins with one row, grows a complete board, validates one coordinate before two, introduces exact distance then bands, and only then records the clues. The array experiment is a separate small program: learners save the preceding game, inspect DIM and sentinel values, then reload the game before applying the memory edits. Distinct counting and repeat handling follow memory. Fixed rounds precede random targets. The final lesson saves and reloads the lesson 8 program unchanged.

Every edit roster reconstructs its maintained complete source from the declared starting state. This explicitly accounts for the separate array experiment. The final teaching source is byte-for-byte equal to the accepted banded prototype; its stored BASIC program was also compared with the accepted tape after loading both through the ROM.

## Verification

All eleven checkpoints were entered with ROM keyboard events and executed on Emu198x Spectrum 0.25.0, stock 48K PAL configuration. Results retain executable, ROM and source hashes. Checks cover the board, row-only input, both coordinate prompts, invalid and long input, exact-distance examples, band boundaries using a declared and restored corner target, the array experiment, all 64 remembered clues, repeated probes, display reconstruction, fixed and random retries, and the final fresh-load/play/retry/exit cycle. Screen and numeric state were observed without program or game-state injection. Captures were visually inspected.

The final saved teaching tape's program bytes equal those loaded from the accepted banded tape. This comparison concerns the stored program; whole tape files can differ because SAVE also includes current variables and metadata. No new original-hardware or beginner-comprehension claim follows from these checks.

The overview and nine lessons passed 40 publication browser combinations: 390 and 1440 pixel widths, light and dark themes. Checks cover rendered listings against sample files, keyboard operation of questions, links, image loading, page overflow and serious/critical WCAG A/AA findings. The executed final-game image was inspected. `scripts/check-sonar-review.mjs` and `src/drafts/sonar/publication-results.json` retain reproduction and source identities. Earlier draft-review evidence is retained separately.

The production build passed, including 69 tests with nine existing skips. All 23 redirects and their built destinations passed: six old numbered lessons, their six former system-root URLs, nine reviewed unit bookmarks and two review overview URLs. Old lessons map by topic; winning leads to the complete-round lesson and the old final game leads to saving and finishing.

## Publication

The catalogue contains nine units. Sonar is game 4 in the current BASIC course, following Touchdown. The overview uses the House presentation and an executed capture; the BASIC landing page and Touchdown link onward to it. The approved wording corrections are included. The larger grid remains optional; the game is silent, with one target and no probe limit.

- [Samples PR 12](https://github.com/code198x/code-samples/pull/12) merged as `e7d6bcb54653c8c3ec94a8eaad9a16ebe85c9c11` before the website change, so production builds can load every teaching source.
- [Website PR 425](https://github.com/code198x/website/pull/425) merged as `6480885788e0ab8091ee5f96ec7f57025d22d30c`.
- [Pages deployment 35101307863](https://github.com/code198x/website/actions/runs/35101307863) published that website revision. Live checks passed the overview, all nine lessons, all 23 redirects and the BASIC/Touchdown onward links. `publication.json` retains those checks.

No new learner-comprehension, original-hardware or audio claim is made. The user approved the game after native play and then the nine-lesson course after reviewing the preview.
