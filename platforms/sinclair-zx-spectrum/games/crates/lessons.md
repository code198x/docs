# Crates — teaching checkpoints

**Status:** Thirteen runnable checkpoints implement the eleven-lesson plan. The accepted three-room prototype remains unchanged. The user approved the replacement overview and eleven lessons after reviewing the website preview. They are published at [Crates](https://code198x.com/systems/sinclair-zx-spectrum/basic/crates/), backed by thirteen executed checkpoints.

## Maintained work

- Samples: `code-samples/sinclair-zx-spectrum/basic/crates/teaching/`, with complete BASIC listings, exact edit snippets, a source-hashed roster, original tile sketches and verification tools.
- Website: `website/src/content/curriculum/sinclair-zx-spectrum/basic/crates/`, with the approved overview and eleven lessons. Review evidence and the navigation roster remain under `website/src/drafts/crates/`.
- Direction: [agreed game scope](brief.md), [lesson brief](lesson-brief.md) and [accepted prototype](prototype.md).
- Evidence: the teaching tree's `verification/results.json`, `boundaries.json`, `graphics.json`, `fresh-tape.json`, `timing.json` and `captures/manifest.json` own configuration-specific execution, experiments, packaging, timing and inspected images.

The sequence builds one four-character crate, then a tile bank before introducing the world array. Lesson 2 has separate tile-bank, warehouse and player-overlay checkpoints. Walking precedes floor-only pushing; target preservation precedes the goal counter and complete one-room visit. A known valid text map precedes its validator. Room selection then brings in the second and third puzzles. Lesson 11 saves the lesson 10 source unchanged.

Every edit roster reconstructs its maintained complete listing from the declared predecessor. New-program instructions need only present the first listing. Later instructions must distinguish added/replaced lines from deletions; generated snippets contain only the lines to enter. The accepted artwork's sketches and byte rows are documented in `tiles.md`, including the change in character allocation between the first crate experiment and the full tile bank.

## Endpoint and map format

All three decoded grids and player starts equal the accepted prototype's independent model. The complete tile bank is unchanged. The endpoint deliberately replaces room-specific assignments with a loader and validation; final program bytes therefore differ from the prototype.

Maps contain eight strings of eight visible symbols: `-` floor, `#` wall, `.` target, `C` crate, `*` crate-on-target, `P` player and `+` player-on-target. Spaces are not silently discarded. Graphics and room data have explicit RESTORE positions. The loader validates row length before indexing, known symbols, exactly one player, at least one crate and equal crate/target totals, counting combined states correctly. Invalid rooms stop before play; missing DATA remains a visible BASIC authoring error. A structurally valid pre-solved room can begin completed. Structural validation is not a solvability test.

The teaching HUD adds `GOALS filled/total` as a text alternative to the green delivered-crate colour. Its executed captures were included in the approved lesson preview; this approval is separate from the earlier native prototype playtest. The accepted scope, rooms, single-step controls, restart/replay, progression, exit and silence are retained.

## Verification

Checks use released Emu198x Spectrum 0.25.0 with the configured stock 48K PAL ROM. Program edits and tape operations go through the ROM; memory and screen reads observe results. Checkpoint caches retain source, tape and stored-program identities. Declared fixtures are restored before proceeding, and program bytes are compared after restoration.

Each checkpoint was executed independently at its intended stage of development. Checks compare all world cells, player coordinates, step and goal counts, and tile pixels with independently computed expectations. Early stages deliberately differ from the endpoint: walking cannot push, floor-only pushes cannot cover targets, and the target/counter stages do not yet end play on delivery.

The checks cover blocked moves, held and simultaneous keys, array bounds, target preservation, full reconstruction, current-room restart, completion, all three solutions and new-game reset. Additional checks execute a one-bit tile edit, change wall colour without changing collision, reject adjacent-crate pushes and reject a push beyond an open array edge. Map fixtures cover short/long rows, unknown symbols, missing/extra players, zero crates, unequal counts, missing DATA, combined symbols and valid pre-solved rooms.

Tape packaging selects the named final program from ROM-recorded TAP blocks without changing its header or payload. A fresh default LOAD must therefore find the finished game first, rebuild the graphics, and support all three rooms, a new game and exit. Packaging evidence is separate from the earlier checkpoint passes. Timing evidence names the measured source and tape; it is not a native host-latency measurement.

No original-hardware or beginner-comprehension claim follows from these checks. Native playtesting of the teaching endpoint is not inferred from approval of the website preview. Website review evidence is recorded separately below; it does not establish learner comprehension or approve the drafts.

## Draft website review

The reviewed overview and eleven drafts used maintained CodeFromFile listings, exact add/replace/delete instructions, local explanations, original tile sketches, inspected captures, Sources and keyboard-operable Question disclosures. Puzzle solutions remain optional reveals. The first program has a complete listing without redundant add-line instructions; lesson 11 reuses the final source unchanged.

`website/src/drafts/crates/review-results.json` records draft hashes, the teaching-roster hash and review results. `scripts/check-crates-review.mjs` checks all twelve pages at 390 and 1440 pixels in light and dark themes: 48 combinations passed for HTTP responses, rendered source equality, answer disclosure by keyboard, overflow, images, internal links/anchors and serious/critical WCAG A/AA Axe findings. A separate check confirmed all eleven previous/overview/next navigation sets. Four representative browser captures were visually inspected, alongside the existing inspected execution captures.

Before integration, the standard `npm run build` passed: 69 unit tests passed, 9 skipped, and 2,344 pages built and indexed. That pre-integration build contained the existing overview and six legacy lessons, with no review route or draft captures. The review routes and images were development-only. Those checks established the rendered draft and build state; the user subsequently approved the course. They do not establish learner comprehension.

## Publication

The approved course is game 5 after Sonar. The catalogue lists eleven lessons, the BASIC landing page includes Crates in the current course, and Sonar links onwards. Five inspected execution captures accompany the course. The six old lessons redirect by topic: warehouse to world memory (2), player and walls to movement (3), pushing to pushing (4), targets to preservation (5), and the final game to keeping the warehouse (11). The former system-root URLs and all reviewed page bookmarks also redirect, for 25 redirects total.

The production build passes with 69 tests passed and nine existing skips. All 25 built redirects resolve to built destinations and carry noindex metadata. All twelve production pages passed 48 browser combinations; `website/src/drafts/crates/publication-results.json` records those checks, source hashes and the 2,349-page build. Deployment evidence is separate from the earlier draft review. Samples merged before the website so every source listing was available to the deployment build.

- [Samples PR 13](https://github.com/code198x/code-samples/pull/13) merged as `31a5bb0727c9e1eb2732eb56c82b403c099572d9`.
- [Website PR 426](https://github.com/code198x/website/pull/426) merged as `d3eeab888bc5e91df0b6d4874b5e94adb33dd309` after all CI and CodeQL checks passed.
- [Pages deployment 35125413766](https://github.com/code198x/website/actions/runs/35125413766) succeeded. Live checks passed the overview, all eleven lessons, all 25 redirects and the BASIC/Sonar onward links. [publication.json](publication.json) retains the 39 checks and revision identities.

The user approved the three-room game after native prototype play, then approved the overview and eleven lessons after reviewing the website preview. No additional original-hardware, beginner-comprehension or native teaching-version playtest claim follows from publication.
