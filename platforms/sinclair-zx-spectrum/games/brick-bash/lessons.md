# Brick Bash teaching implementation

The user agreed to retain the native prototype's difficulty and proceed with the ten-lesson progression. Nine executed checkpoints now support the [lesson brief](lesson-brief.md); the saving lesson reuses the ninth. The final source is byte-identical to the prototype the user played. The overview and all ten lessons are published after Tail Chase as game 7. The user approved the overview and lessons after local review: “Looks and reads fine”. Publication is complete.

## Maintained checkpoints

Sources live in `code-samples/sinclair-zx-spectrum/basic/brick-bash/teaching/`. Its README maps every lesson to a complete listing. Each source directory includes exact add/replace/delete line numbers and a changed-lines listing; the first checkpoint is presented as a new program. The derivation script is an authoring convenience, not a runtime dependency.

The progression builds pixel drawing, movement, the paddle and serve, catches, one destructible brick, a wall-coordinate inspector, complete wall destruction, aiming and the finished game. The inspector temporarily replaces the movement and result routines while retaining the graphics and revised wall routines: learners enter the ball's candidate coordinates, see the proposed row/column and hit result, and watch stored brick state change. The next checkpoint restores the movement, paddle drawing and result routines around the new wall lookup. Entering -1 at the X prompt leaves this inspection program.

Before aiming is introduced, a catch preserves horizontal direction. Both full-wall variants were cleared by keyboard play checked against an independent rectangle model. This makes the aiming lesson a visible rule change rather than a requirement hidden in the first working wall.

## Execution and source evidence

Execution used Emu198x Spectrum 0.25.0 with the stock 48K PAL configuration. Each listing was entered through ROM keyword keys, saved to a self-starting tape and loaded into a fresh session. Stored ROM lines were compared with the build record. Input drives play and the inspector; verification reads state and bitmap memory without injecting game-state fixtures.

The samples' `verification/evidence/summary.json` records nine checkpoints and 55 passed execution groups. These cover drawing the four ball pixels, toggling them off and back without damaging the court; safe bottom stopping; held paddle clamps and attached-ball movement; repeated catches before aiming; one-brick clearance; lookup bounds, gaps, one-pixel contact and removed bricks; both full-wall clearances; miss, retry, frozen completion and exit. The final tape additionally carries forward all fourteen prototype checks, including centre returns, one-pixel paddle-edge catches and exit from every phase.

Complete playfield bitmap comparisons check the court, live bricks, paddle and ball. Capture verification checks result labels against ROM font glyphs and the top 176 display rows against the current RAM bitmap, retains the unmodified PNG and records the wait in `captures.json`. Result prompts also finish before capture, and retained images are visually inspected. The inspector's diagnostic row is below the court. Source transitions replay exactly, all literal branch targets exist, and each tape has a checksum-valid header/data pair. Source, tape and executable identities are retained; the final run also records the ROM identity.

A separate host audit exhaustively compares the regular-wall lookup with independent rectangle scanning for 45,056 integer positions. It includes the worked overlap/gap examples in the lesson brief. This is arithmetic verification, not 45,056 emulator interactions. The executable game traces remain the evidence for integrated movement and state changes.

The initial native trial establishes the endpoint's reported playability and difficulty. The final teaching listing preserves that source exactly. Intermediate stages perform less work; their pace is not claimed to match the final game's. Neither original-hardware performance nor independent learner outcomes has been established.

## Website implementation and local review

The overview and ten MDX lessons live under `website/src/content/curriculum/sinclair-zx-spectrum/basic/brick-bash/`. Unit metadata supplies the ten lesson identities and three teaching groups. The module catalogue places Brick Bash after Tail Chase as game 7; the BASIC landing page includes it in the published course. The earlier placeholder had no authored lesson routes to redirect.

Eighteen CodeFromFile blocks use the maintained listings and exact changed-line snippets. Unit one presents a new short program without redundant add-line instructions. Later units give explicit deletions, replacements and additions; unit ten reuses the final source. Five verified game captures accompany the overview and selected lessons. The original difficulty, graphics and endpoint source are unchanged.

The pages explain pixel versus character coordinates, OVER drawing, paddle artwork and serve state, inclusive overlap, discrete axis order, stored brick state, address/gap/state checks, three contact zones, reset and fresh tape loading. Questions include worked reasoning; the coordinate inspector remains explicitly separate from ordinary play. Local setup and saving links provide optional help without replacing the immediate explanation.

The full website build passed: 69 tests passed and nine were skipped by the existing suite; route, source, link and asset build gates completed. The dedicated browser review covers eleven pages on desktop and Pixel 7 profiles in both light and dark themes: 44 page checks, exact rendered source comparisons, keyboard question toggles, local links and anchors, image loading, one main heading, no horizontal page overflow and no serious/critical Axe findings. `verification/website-review.json` retains the browser results and `verification/website-manifest.json` identifies the authored files, source references and captures. Representative rendered pages were visually inspected.

The published overview is [Brick Bash](https://code198x.com/systems/sinclair-zx-spectrum/basic/brick-bash/). The user has now approved these authored pages separately from the earlier prototype feedback. Performance/assembly revisits remain deferred.

## Publication

The approved samples and lessons are merged in [samples PR 15](https://github.com/code198x/code-samples/pull/15) and [website PR 428](https://github.com/code198x/website/pull/428). The [Pages deployment](https://github.com/code198x/website/actions/runs/35215033753) succeeded. `verification/publication.json` records 27 live checks: all eleven page responses and canonical URLs, eighteen rendered source blocks matching maintained files, five unchanged capture hashes, ten unchanged tape hashes and the Tail Chase → Brick Bash course order.

Ten live pages also passed the desktop/light browser checks. Two attempts at the complete live browser run stopped on network navigation timeouts; the complete 44-page desktop/mobile and light/dark review passed locally. The direct live checks above all passed. Performance/assembly revisits remain deferred.
