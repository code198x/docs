# Meteor Storm — checkpoint execution record

**Status:** Nineteen complete teaching programs are implemented and executed in
`code-samples/sinclair-zx-spectrum/assembly/meteor-storm/checkpoints/`. The accepted
prototype is preserved. Twenty-four [authored lessons and browser investigations](lessons.md)
await user review; no new game module is published by this work.

The user explicitly permits as many lessons as understanding requires. These
source states do not settle the final lesson count. The [teaching progression](lesson-brief.md)
now includes six small experiments around the thirteen game stages:

- `one-row-shift` and `eight-shifts` make the byte carry and table data visible
  before the full ship uses pre-shifted artwork.
- `pixel-address` and `draw-ship` separate bitmap addressing from the complete drawing routine.
- `interrupt-clock` isolates the private IM2 handler and frame counter.
- `half-rate-clock` isolates the alternate-frame gate before clocked steering.

The game stages then cover pixel motion, clocked steering, one meteor, first
contact, pooled objects, a finite course, drift, stars, elapsed time, boost,
render cost, records and the finished presentation. The final fresh-tape activity
reuses `finished`; it does not introduce another source version.

Every directory has complete assembly and any required data, plus controls,
repeat instructions and a worked prediction. The sample README owns build/run
commands; `contracts.md` owns the inputs, clobbers, bounds and lifetime assumptions
that need explaining when helpers are introduced. Later checkpoints contain only
the systems present at that stage, rather than the whole endpoint hidden behind
feature flags. Object records grow from four to five to seven bytes as the
corresponding state becomes necessary.

## Executed evidence

Target: stock 48K PAL Spectrum, original Z80. Asm198x 0.0.58 builds every source;
upstream Pasmo 0.5.5 emits identical raw machine code for all nineteen programs.
The native emulator executable and each source/data hash are recorded in
`verification/evidence/` in the sample repository.

- `checkpoints.json`: 142 checks across seventeen programs, including actual
  screen-memory shifts, movement bounds, clean XOR erasure, clocks across byte
  wrap, idle losses, keyboard-driven completions, retries, pickups and pool bounds.
- `opening-additions.json`: 20 checks for the new bitmap-address and static ship
  experiments, including all sixteen ship rows and independent Pasmo byte parity.
- `boundaries.json`: four keyboard-driven first-dodge cases. With meteor X=116,
  ship X=100 or 132 misses; X=102 or 130 hits. The strict comparison at separation
  16 is observable on both sides.
- `endpoint.json`: 49 checks covering accepted gameplay measurements, full title
  glyphs and margins, complete score text in bitmap memory, held-key release,
  first-hit loss, vertical stars, gentle drift, normal/boost passage, finish bonus,
  independent records, retry reset and fresh ROM tape loading.

All play outcomes use ordinary frames and keyboard input. Read-only probes let
an independent host model choose steering; no state writes or CPU stepping
manufacture a successful run. The model's conservative route is evidence that
the course is traversable, not a judgement about human difficulty.

The finished teaching program reproduces the reference measurements exactly for
the tested routes: 1046 course steps, 2092 elapsed PAL frames at normal speed
(41.84 seconds) and 1046 while boosting (20.92 seconds). Those routes score 670
and 960 points respectively, including finish bonuses of 590 and 800. Scores
reflect the route's collected stars, not the theoretical maximum.

## The optimisation earns its lesson

In the straightforward `boost` checkpoint, frame_delta records 1, 2 and 4:
startup can sample a single frame, and dense boosted updates occasionally miss
the intended two-frame interval. The tested run takes 1053 elapsed frames.

In `render-budget`, frame_delta records only 1 and 2. Each meteor retains its old
image position while both simulation/contact steps execute, then erases and
redraws once. Removal on the first step still erases immediately. The lesson can
therefore measure a concrete cost and improvement without teaching collision
skipping as an optimisation. These are observations of this executable and
emulator configuration, not a physical-hardware benchmark.

## Accepted endpoint comparison

The prototype source remains SHA-256
`fefac65915baa0a2fa29395a7ff8f19fac9c2261b11073ebd37e7a602d302f4d`.
Its accepted tape hash remains
`99bf888e88ab29e65908aa755b8a0e99be37f6a95f132926c90755aa35414e9a`.
A fresh build reproduces that tape when the code-header name matches the original
build. Asm198x's tape header derives its ten-character name from the output path,
so changing that path can change a tape hash without changing machine code.

The teaching endpoint is deliberately different source:
`113e89bed3bc25073eaa474448e79a485a068891e5982772090715fc597496a9`.
Its verified tape is
`5d7bdcc1a705fabef3530f006241ef065c7f902a44d9e4e8e8f7a5afc0557f47`.
It removes recovery/blinking state left over from an earlier multi-hit prototype,
an unused erasure routine and unused constants/dirty state. The misleading
`draw_all` name becomes `count_objects`, matching its actual job. The accepted
one-life rule, art, course, controls, movement, drift, boost, scoring and records
remain intact. Runtime comparisons establish behavioural agreement, not source
or binary identity.

## Lesson review

The [lesson implementation record](lessons.md) maps twenty-four authored lessons
onto the nineteen programs. Browser source editing, companion artwork, actual RAM,
collision stepping and downloadable tape now support the progression.

Some earlier batched native result captures show incomplete text despite complete
bitmap memory. They remain excluded from lesson illustrations. The finished
browser result has now been visually inspected, and all 640 pixels of its score
line agree with bitmap RAM and the actual ROM font. This establishes correct
browser presentation; the native capture discrepancy itself is not diagnosed.
Impact audio remains captured but not separately listening-reviewed. No physical
hardware testing or user acceptance of the new lessons is claimed.
