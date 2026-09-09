# Touchdown — lesson implementation

**Status:** The eleven-lesson brief is agreed. The overview and eleven replacement lesson drafts are implemented for review; publication is pending lesson approval.

## Maintained work

- Samples branch `curriculum/touchdown-lessons`: `sinclair-zx-spectrum/basic/touchdown/teaching/`, with sixteen runnable game checkpoints, exact edit rosters/snippets and a separate input diagnostic.
- Website branch `curriculum/touchdown-lessons`: `src/drafts/touchdown/`, served by the development-only Touchdown review route. Start the website with `CODE_SAMPLES_PATH` pointing to the teaching samples checkout; open `/systems/sinclair-zx-spectrum/basic/touchdown/review/overview/`.
- Scope: [game brief](brief.md), [agreed lesson sequence](lesson-brief.md), [prototype evidence](prototype.md).

The simpler stages keep the final gravity/thrust model. Vertical landing gains retry before fuel; the first lateral game starts at column 18 beside an eight-cell pad, with a verified one-key-at-a-time approach. Combined input precedes the height array. Terrain has four separate checkpoints; custom graphics have two. The final four-cell-pad program is byte-for-byte the reviewed prototype. AND first appears in lesson 4's menu filter and is reinforced by lesson 5's fuel condition.

## Verification

On Emu198x Spectrum 0.22.1, configured 48K PAL ROM, all sixteen sources were entered through ROM keyboard events and run to contact/exit. Every thrust-capable checkpoint completed a scripted safe approach. All eight diagnostic input combinations passed. Additional checks cover both practice-pad edges and adjacent misses, empty fuel with held thrust, a safe empty-tank coast, the raised-array experiment, ascending side contact and held-Q release. A fresh emulator loaded and played the final teaching tape.

Source hashes and results are retained under the teaching samples' `verification/`. The new final tape's 3,071-byte stored program is identical to the reviewed prototype tape; the existing full boundary/retry evidence therefore covers that same final program. `equivalence.json` records both tape hashes. Different saved runtime data gives the tape files different whole-file hashes.

All 48 overview/lesson, narrow/wide and light/dark browser combinations passed. Checks compare full code blocks and inline examples to authored sources, open questions with the keyboard, verify local links and images, detect horizontal overflow and run serious/critical accessibility checks. The website build passed 69 tests with nine existing skips; no development review pages were emitted. Retained `browser-results.json` and `scripts/check-touchdown-review.mjs` support reproduction.

The user played the native prototype and reported that it works well and is quite hard. Scripted practice landings establish that the controls allow success; they do not establish beginner ease. The new teaching stages and prose still need review. No new subjective audio or original-hardware result is claimed.

## Review and publication

Review the full overview and eleven lessons, paying particular attention to lesson 4's program reorganisation and lesson 7's input explanation. Listings and inline examples retain readable keyword spaces; ROM entry alone suppresses redundant token spaces. There are no Keyboard notes sections.

After lesson approval, replace the published Touchdown content, reconcile its eleven-unit catalogue and module number, preserve or redirect existing lesson URLs, and update the BASIC landing page and Volley's onward route in one release. Then build and deploy. Current production content remains unchanged.
