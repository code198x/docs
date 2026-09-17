# Brick Bash prototype record

Native feedback was: “That works, it's surprisingly tough”. The [bounded prototype](brief.md) is working in native play: one ball, a horizontal paddle, three rows of six bricks, miss, clear, retry and quit. Difficulty is a play observation, not a request to change the rules. The user subsequently agreed to retain this baseline and develop the teaching progression. The [lesson brief](lesson-brief.md) defines ten lessons, now supported by [nine executed checkpoints](lessons.md). The final teaching listing is identical to this prototype.

## Execution evidence

Maintained source, loading instructions and verification tools live in `code-samples/sinclair-zx-spectrum/basic/brick-bash/prototype/`. Its `verification/` directory retains the ROM-saved tape, stored program, build and execution records, and four inspected captures. The manifest identifies their hashes and confirms the tape's header/data pair checksums.

Execution used Emu198x Spectrum 0.25.0 with a stock 48K PAL ROM. Source entered through ROM keyword keys was saved to tape and loaded into fresh sessions. Keyboard events drive all checks; no game-state fixtures were injected. Results identify source, tape, executable and ROM hashes.

Fourteen checks passed across the main and control runs. They cover fresh loading; held movement, clamps and attached ball; miss; retry; all eighteen bricks cleared; frozen completion; all three paddle return zones; exact one-pixel contact at both paddle edges; restart during flight; and quitting from title, ready, flight and result. Every observed move agrees with an independent host model that scans physical brick rectangles instead of reproducing BASIC's index calculation. Both side walls, the top and horizontal and vertical brick responses occur in the clearance trace.

Full playfield bitmap comparisons check remaining bricks, walls, paddle and ball in ready, miss and completion states. Title, ready, miss and completion captures were visually inspected. The model and bitmap checks establish scripted correctness separately from native feedback.

## Representation and limits

A 2×2 pixel ball moves at most four pixels per axis. The paddle moves by character columns. A 3×6 array stores live bricks; screen colour never decides contact. Wall and paddle reflection precede brick checks. Horizontal contact is resolved before vertical contact, a deliberate discrete corner convention rather than continuous billiards physics. Original UDGs round the artwork; collision uses the full brick rectangles.

The four ball pixels are toggled with OVER 1 for drawing and erasure. Ordinary movement observations had a median of 20 PAL frames, ranging from 18 to 25. The loop has no explicit timing delay. Observations mark movement commit/drawing boundaries and do not establish fixed pacing or host latency. Native play worked but was described as surprisingly tough. Original hardware and independent learner outcomes remain untested.

The approved overview and ten lessons are published around the [executed checkpoints](lessons.md), including the temporary wall-coordinate inspector. Keep the current version as a baseline; no difficulty change or performance/assembly revisit is agreed.
