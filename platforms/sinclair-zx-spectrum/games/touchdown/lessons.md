# Touchdown — lesson implementation

**Status:** The eleven-lesson brief is agreed. The overview and eleven replacement lessons are published.

## Maintained work

- Samples branch `curriculum/touchdown-lessons`: `sinclair-zx-spectrum/basic/touchdown/teaching/`, with sixteen runnable game checkpoints, exact edit rosters/snippets and a separate input diagnostic.
- Website branch `curriculum/touchdown-lessons`: `src/content/curriculum/sinclair-zx-spectrum/basic/touchdown/`, served at `/systems/sinclair-zx-spectrum/basic/touchdown/`. The old numbered and review URLs redirect to the published course.
- Scope: [game brief](brief.md), [agreed lesson sequence](lesson-brief.md), [prototype evidence](prototype.md).

The simpler stages keep the final gravity/thrust model. Vertical landing gains retry before fuel; the first lateral game starts at column 18 beside an eight-cell pad, with a verified one-key-at-a-time approach. Combined input precedes the height array. Terrain has four separate checkpoints; custom graphics have two. The final four-cell-pad program is byte-for-byte the reviewed prototype. AND first appears in lesson 4's menu filter and is reinforced by lesson 5's fuel condition.

## Verification

On Emu198x Spectrum 0.22.1, configured 48K PAL ROM, all sixteen sources were entered through ROM keyboard events and run to contact/exit. Every thrust-capable checkpoint completed a scripted safe approach. All eight diagnostic input combinations passed. Additional checks cover both practice-pad edges and adjacent misses, empty fuel with held thrust, a safe empty-tank coast, the raised-array experiment, ascending side contact and held-Q release. A fresh emulator loaded and played the final teaching tape.

Source hashes and results are retained under the teaching samples' `verification/`. The new final tape's 3,071-byte stored program is identical to the reviewed prototype tape; the existing full boundary/retry evidence therefore covers that same final program. `equivalence.json` records both tape hashes. Different saved runtime data gives the tape files different whole-file hashes.

All 48 overview/lesson, narrow/wide and light/dark browser combinations passed. Checks compare full code blocks and inline examples to authored sources, open questions with the keyboard, verify local links and images, detect horizontal overflow and run serious/critical accessibility checks. The website build passed 69 tests with nine existing skips; no development review pages were emitted. Retained `browser-results.json` and `scripts/check-touchdown-review.mjs` support reproduction.

The user played the native prototype and reported that it works well and is quite hard. Scripted practice landings establish that the controls allow success; they do not establish beginner ease. The user subsequently approved the teaching stages and prose. No new subjective audio or original-hardware result is claimed.

## Publication

The catalogue contains eleven units, the overview uses the House presentation, and the BASIC landing page and Volley link onward to Touchdown. The old eight numbered lesson URLs map by topic to the replacement lessons; old system-root URLs and review links also redirect. All 29 explicit redirects and their built destinations pass checks. Readable keyword spaces and the shared questions are preserved; there are no Keyboard notes sections.

The production build passes. Publication browser checks cover the twelve generated pages at narrow and wide widths in both themes. A What’s New entry is prepared outside the public collections for separate editorial/distribution review.

Release changes: [website PR 421](https://github.com/code198x/website/pull/421), [samples PR 11](https://github.com/code198x/code-samples/pull/11), and [documentation PR 21](https://github.com/code198x/docs/pull/21).

[Pages deployment 34365662926](https://github.com/code198x/website/actions/runs/34365662926) succeeded for website commit `7ff4ceb8f9c692403ba44e36dadc496f417f5aa5`. Live checks passed the overview, all eleven lesson pages and all eight old numbered redirects. The full 48-combination production browser sweep and all 29 built redirects passed before merge.
