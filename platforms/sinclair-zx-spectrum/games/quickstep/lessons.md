# Quickstep — teaching implementation

Eight independently ROM-entered checkpoints now support the [ten-lesson progression](lesson-brief.md). They live under `code-samples/sinclair-zx-spectrum/basic/quickstep/teaching/`. The final source is byte-identical to the accepted six-lane prototype. The overview and ten lessons are authored and locally verified. User review and website publication remain outstanding.

## Maintained programs

| Lessons | Checkpoint | Executed result |
|---|---|---|
| 1 | `board` | Original player and strip artwork on a 15×3 practice board; stops after drawing. |
| 2 | `walk` | One step per press/release, four bounds, preserved exit background, retry and quit. |
| 3 | `lane` | Manual SPACE advancement, all wrap positions, drawn vehicles checked against numeric phase, player overlay and background restoration. |
| 4 | `clock` | Timed updates and a two-update lane countdown; continuous traffic without contact rules. |
| 5 | `crossing` | Complete one-lane crossing, both contact phases, rejected player/vehicle swap, frozen result and reset. |
| 6–7 | `six-lanes` | Accepted board, phases and periods, independent lane state, complete crossing and verified planning traces; polling-only input. |
| 8 | `buffered` | Recognised taps during update work survive to the next step; held controls still repeat. |
| 9–10 | `finished` | Exact accepted endpoint, including the title/start screen and full game. Saving reuses this source. |

The first two programs initialise the four player UDGs and the strip texture. The vehicle stage adds the eight vehicle UDGs. The practice board and temporary SPACE control are explicitly replaced during the progression. Moving away from the exit must restore its marked background in the inspection programs, where reaching it does not end play; moving away from a lane must restore any vehicle artwork that the player covered. These intermediate requirements do not alter the accepted final source.

`checkpoints.json` records source identities. `edits.md`, each checkpoint's `edits.json`, and its `changes.bas` list the exact additions, replacements and deletions. The opening uses its complete listing. Reconstructing each next source from the preceding one passes, literal branch and RESTORE targets exist, and unchanged lines have identical ROM-stored bytes across independently entered programs.

## Execution evidence

`verification/evidence/manifest.json` records **96 passed execution check groups** across eight checkpoints. Each source was entered through a fresh stock 48K ROM keyboard session, saved to a self-starting TAP and loaded in fresh Emu198x Spectrum 0.25.0 sessions. The audit verifies source and tape hashes, both TAP block checksums, stored line identities, retained capture hashes and final-source identity.

Keyboard-driven model trials compare the one-lane and six-lane programs with separate occupied-cell models. They cover safe waits, phase/countdown reset, both wrap directions where present, board bounds, centre-only victory, entry into occupied cells, traffic reaching a waiting player, attempted swapping, frozen results and exit control flow. Inspection trials cover single-step input and restoration of backgrounds. The manual traffic test compares actual lane bitmap bytes with the expected UDG positions through a full wrap. No trial injects player positions, traffic phases or screen contents.

Separate ordinary-frame trials check the actual control loops, complete crossings, retry and quit. A four-frame tap during lane-update work is missed in `clock`, `crossing` and `six-lanes`, then retained in `buffered` and `finished`. This is the verified before/after experiment for lesson eight. Held movement clamps at the boundary in every clocked stage; manual stages retain one move per press/release. Buffered crossing trials use short presses because holding a key through a long update can leave a further recognised key in the ROM latch. That queued-step behaviour is part of the accepted endpoint and must be explained.

Original frame captures were checked against live bitmap and attribute RAM, with a complete player required before accepting a board capture. RAM/image agreement alone can accept an unfinished redraw, so it is insufficient as a presentation check. The retained ordinary-frame board and success captures have been inspected. CPU statement-boundary checks establish state transitions, not animation or timing.

## Timing and planning examples

Each clocked checkpoint has a 700-frame ordinary resting trial that observes at least two wraps of the low frame-counter byte. Consecutive update counts are checked so missed observations cannot silently inflate the measured intervals.

| Checkpoint | Observed commit intervals | Median PAL frames | Range |
|---|---|---|---|
| `clock` | 17 | 43 | 30–47 |
| `crossing` | 17 | 44 | 29–45 |
| `six-lanes` | 12 | 46 | 24–101 |
| `buffered` | 12 | 47 | 25–102 |
| `finished` | 12 | 47 | 25–103 |

These small, configuration-specific samples describe update commits, not input latency or an original-hardware benchmark. The unchanged endpoint's earlier 1,200-frame trial remains in the [prototype record](prototype.md); different observation windows need not give identical medians. The 32-frame threshold is an update-start target, and busier updates can exceed it.

`verification/evidence/planning.json` extracts two consecutive-update examples from actual `six-lanes` keyboard trials. At (9,4), waiting on the central strip lets lanes advance, then moving to (9,3) succeeds. In the second example, a sideways move from (7,7) to (8,7) succeeds, but waiting there lets the bottom lane advance from phase 9 to 8 and catch the player. Each example retains all starting phases and countdowns, so the lesson can ask for a prediction with enough information to answer it. Neither example relies on injected setup state.

## Website authoring and local review

The overview and ten lessons are authored on website branch `curriculum/quickstep-lessons`. Seventeen CodeFromFile blocks include maintained listings and exact editing transitions. The first listing begins a new program. Planning and saving reuse existing programs. Worked examples explain cell coordinates, character bytes, string rotation, frame-counter wrap, both collision checks, independent countdowns and the one-key input latch. Optional answer reveals give the reasoning.

Primary citations identify the relevant chapters of the original Sinclair BASIC Programming manual, including its system-variable table. Shared setup, saving and Foundations links were checked. Three unmodified emulator captures illustrate the practice board, six-lane crossing and successful finish.

The production build passed: 69 tests passed and 9 skipped, followed by content checks, Astro generation and search indexing. Vale reports no errors or warnings and two suggestions. All prose add/replace/delete lists agree with the maintained transitions.

`scripts/check-quickstep-review.mjs` passed 44 browser page checks: eleven pages on desktop and Pixel 7, in light and dark themes. All seventeen rendered code blocks match their maintained sources. Checks cover keyboard answer reveals, expanded listings, links and anchors, loaded images, one main heading, horizontal overflow and serious/critical Axe findings. Representative desktop and mobile captures were visually inspected. `verification/website-review.json` retains the browser results; `verification/website-manifest.json` identifies pages, included sources and original figures.

The preview catalogue places Quickstep after Drift as game 9, with all ten lessons available. Existing later catalogue identifiers move up to make room; their URLs stay stable. The update article remains a draft and is absent from the built update pages and RSS feed. No merge or publication has occurred.

## Review handoff

Review the overview and ten lessons in the local website preview before publication. The accepted six-lane game's rules, controls, artwork, silence and difficulty are preserved. Native acceptance applies to that unchanged endpoint; intermediate programs have automated execution evidence, not independent learner review. Assembly and performance comparisons remain deferred until the initial BASIC versions are complete.
