# Tail Chase prototype record

The user accepted the native prototype after play: “Works, just fine”. The accepted scope is the [24×16, eight-food round](brief.md), with a four-cell body growing to twelve cells. Ten published lessons and twelve verified teaching checkpoints now accompany it; see the [teaching implementation](lessons.md).

## Implementation and evidence

The maintained source and verification tools are in `code-samples/sinclair-zx-spectrum/basic/tail-chase/prototype/`. Its README provides tape loading and rebuild commands. The `verification/` directory retains the recorded tape, ROM-stored program lines, results, control results and a capture manifest.

Execution used Emu198x Spectrum 0.25.0, stock 48K PAL, ROM keyboard entry and a fresh ROM tape load. Source, tape, emulator and ROM hashes identify the run in `results.json`. No game-state fixtures were injected. An independent body model checked movement, growth and every occupancy cell during a complete eight-food round.

Eleven main checks passed: fresh loading and initial state; invalid/reverse input; continuous movement into a wall; restart; reversal after a turn; entry into a departing tail cell; self-collision; all eight foods; frozen completion; and exit from play and title. Three separate control checks passed for preserving the first queued turn, ignoring simultaneous directions and exit from the result screen. Title, wall collision, self-collision and completion captures were visually inspected. Intermediate arena and retry captures were omitted because the HUD was still being drawn.

The body uses a twelve-slot circular coordinate array and a separate occupancy grid. Each move updates the departing tail and new head without shifting the entire body. A non-growing move may enter the departing tail cell; rejected moves preserve the body. Food selection rejects occupied cells. Screen colour is presentation only.

The ROM FRAMES low byte provides an 18-frame minimum interval. Recorded movement observations include drawing and food-selection boundaries; they do not establish a fixed 18-frame period or native host latency. Human approval establishes that the prototype worked acceptably in this native trial. Original-hardware performance and independent learner outcomes remain untested.

## Teaching implementation

The [lesson brief](lesson-brief.md) develops an ordered body through shifting, circular storage, growth and occupancy. The [implementation record](lessons.md) owns the twelve executed checkpoints and ten published lessons. The final teaching source is byte-identical to this accepted prototype. The overview and lessons were approved after local review and are published.
