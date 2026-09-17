# Tail Chase teaching implementation

**Status:** Twelve teaching checkpoints are implemented and verified. The user approved the overview and ten lessons after local website review. The overview and all ten lessons are published after Crates. The native prototype remains the accepted gameplay endpoint.

## Maintained sources

`code-samples/sinclair-zx-spectrum/basic/tail-chase/teaching/` contains complete sources, focused editing snippets, a checkpoint manifest and ROM build/verification tools. `verification/evidence/` retains each checkpoint's source identity, saved ROM listing, tape and execution record. Its `summary.json` records twelve passed checkpoints and 76 named execution check groups. Its README gives reproduction commands.

| Lesson | Executed checkpoints | Result |
|---|---|---|
| 1. Give the snake a face | face; arena | Original UDG bytes, stationary drawing, fresh tape loading |
| 2. Keep moving | moving-head | Continuous rightward travel, boundary rejection, retry and exit |
| 3. Choose the next turn | steering | Four-direction travel, ignored reversal, repeated routes and clock-byte wrap |
| 4. Remember where the head went | shifted-body | Ordered coordinate copying, legal departing-tail entry and stable body |
| 5. Reuse the empty slot | circular-body | Same body behaviour through repeated array-index and clock-byte wraps |
| 6. Leave the tail behind | fixed-food; fixed-food-body-test | One-food growth and frozen completion; separate diagnostic continues to a five-cell self-collision |
| 7. Ask the board | occupancy; occupancy-body-test | Equivalent behaviour with all 384 occupancy cells checked against body order |
| 8. Find another snack | random-food | Actual random food reached through legal keyboard turns, one-food completion and retry |
| 9. Eat all eight | eight-foods | Complete eight-food round, wall/self collisions, departing-tail entry, restart, frozen completion and all quit phases |
| 10. Keep the game | Reuses eight-foods | ROM SAVE with entry line 10 and fresh tape load; no extra numbered source changes |

The final endpoint is byte-identical to the accepted prototype. Its eleven full-round checks are supplemented by the three queued-turn/simultaneous-input/result-exit checks. The total of 76 includes repeated checks across intermediate versions; it is not a count of distinct game rules.

Each source was entered through real ROM keyboard tokens and recorded as a tape in a fresh emulator process. Each saved tape has one header/data pair and valid checksums. Verification then loaded it through the ROM in another process. Inputs use the keyboard; observations read state without injecting fixtures. Explicit diagnostic listings are different programs, not claims about normal one-food gameplay.

Execution configuration: Emu198x Spectrum 0.25.0, stock 48K PAL. Build records identify executable/source/tape hashes; the final run also identifies the ROM. The independent movement model compares ordered body positions, counts and rejection behaviour, and the occupancy stages compare every grid cell. Source auditing replays all edit instructions, verifies snippet contents and checks literal branch targets. Human acceptance of the identical endpoint is separate from scripted teaching-stage checks; no independent learner trial or original-hardware test is claimed.

## Lesson presentation

The website sources are under `src/content/curriculum/sinclair-zx-spectrum/basic/tail-chase/`, with a module overview and ten descriptive unit routes. Unit metadata supplies the lesson navigation. The catalogue places Tail Chase after Crates as game 6 and removes the obsolete first-custom-graphics claim. The BASIC landing page includes the same route.

Lessons keep the first short listing whole, then provide exact additions, replacements and deletions alongside changed-line snippets and complete source disclosures. Circular storage is introduced after coordinate shifting. Growth precedes the occupancy grid, so the scan and direct lookup can be compared on the same rules. Two labelled diagnostic checkpoints make self-collision observable after the first growth; later edits restore the normal ending.

Captured face/arena, one-food completion, both self-collision diagnostics and final completion were inspected. Selected captures appear in the lessons. Result captures allow display scanout to finish after the program reaches its frozen state. The movement checks, rather than screenshots, establish state transitions. FRAMES explanations cite Vickers/Bradbeer, *ZX Spectrum BASIC Programming*, second edition, chapter 18, pp. 129–131; the lessons state the short-interval assumption and distinguish the minimum threshold from total update time.

The website production build passed its 69 tests (nine skipped) and content checks. The [browser review](verification/website-review.json) passed all 44 combinations of eleven pages, two device profiles and two themes, with no serious/critical accessibility findings, missing source displays, broken images or page overflow. All 57 discovered internal links and anchors resolved. Desktop/mobile overview and circular-slot table screenshots were inspected. Independent learner feedback remains follow-up evidence.

## Publication

- [Samples PR 14](https://github.com/code198x/code-samples/pull/14), merged as `a22e6f9e5efbf13c42fd56552f4e54d87bbc6870`.
- [Website PR 427](https://github.com/code198x/website/pull/427), merged as `fa9145e9deb81e0978fa61bcc926f0aa14dcce33` after its production CI and security checks passed.
- [Pages deployment](https://github.com/code198x/website/actions/runs/35203127216) succeeded for that website commit.
- [Live course](https://code198x.com/systems/sinclair-zx-spectrum/basic/tail-chase/): overview, ten lessons, four capture assets, BASIC course order and the retained final tape checked. Every rendered source block matches its maintained sample; canonical lesson URLs agree. The [publication record](verification/publication.json) stores those checks and release identities.

## Remaining scope

Keep the initial BASIC versions as the current priority; performance and assembly revisits remain deferred. The catalogue's fourteen proposals after Tail Chase are inherited candidates, not an agreed remaining-game count or an instruction to implement all fourteen. Later selection should settle a bounded continuation explicitly.
