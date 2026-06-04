# Decision: units teach by showing the build — incremental, runnable milestones

**Status:** Decided 2026-06-04. Raises the bar for **every unit across the corpus**
(Spectrum + C64, BASIC + assembly). **Supersedes the one-program-per-unit format**
and amends [`specifications/unit.md`](../specifications/unit.md). **Nothing is
"done" until converted** — existing `complete` marks (including the C64
*Meet the Machine* primer) revert to `in-progress` pending conversion. **Gates
expansion:** no third system and no content-range expansion until the corpus
meets this bar. Amends the October bar in
[`october-2026-launch-spec.md`](october-2026-launch-spec.md).

**Drift trigger:** if a unit dumps one finished program under "The Complete Code"
with a single end-result screenshot, or shows inline snippets that aren't
independently runnable — **stop, that's the old bar.** Each milestone runs and
shows its own result.

## The problem it fixes

Our units *claim* incremental, one-concept, "runnable at every step" pedagogy —
but they don't deliver it. Inline "snippets" are **excerpts of the final program**
(e.g. Starfield u4's `snippets/01-sid-setup.asm` is 13 lines, no stub, no entry —
it can't be assembled or run). The only runnable artefact is the full program at
the end. So the reader can run the project **only at the end**, and the
progression is *explained*, never *shown*. That violates the principle we hold —
"the reader should be able to run the project after each section."

## The decision

A unit teaches by showing its construction. Each **meaningful milestone** is a
real, runnable state with a real result:

- **Milestones, not lines.** The 2–5 meaningful observable states, not every edit.
- **Each milestone runs.** Code-samples become cumulative `step-NN.asm`
  (step N = step N−1 + the increment); the **last step is the complete program**.
- **Each milestone shows its result, in the medium that fits what it produces.**
  A **still** (PNG) for a static state — and *especially* for detail- or
  dither-heavy graphics, which a video codec washes out (the capture-pipeline
  CRF/dither gotcha); a **video** (MP4) for *motion* — movement, scrolling,
  animation, parallax — things a still cannot show; a **real audio clip**
  for sound. A milestone can carry more than one (the ship *moves* and the laser
  *fires*). A step with no observable result folds into the next one that has one.
  All three are headless script steps the c64 supports (`--screenshot`,
  `Start`/`StopVideoRecording`, `Start`/`SaveAudio…`).
- **Explain with whatever makes the subject clear — not prose alone.** Diagrams,
  flowcharts (the game loop, a state machine), tables (register maps, bit layouts,
  memory maps), register/bit-layout visuals — authored explanations sit alongside
  the captured results. Units already have components for several of these (the u2
  game-loop diagram, the joystick bit-table, register views); use them freely and
  build more where a picture beats a paragraph.
- **Code shown as the diff/addition.** What this step *adds*, highlighted, with the
  full cumulative state available expandable — not a re-dump of the whole program
  each time.
- **Before/after recap.** Where the unit started; where it ended — in the medium
  that shows it. A still `ImageComparison` only when both states are static and
  visually distinct; for motion/audio units the milestone media is the bookend and
  a one-line prose recap suffices (a two-still comparison of a sprite at A vs B
  doesn't sell it).

## The bar is also depth, reach, and care

Structure is necessary, not sufficient. The raised bar equally commits to:

1. **Built to run in the page, not just on disk (design-forward).** Every milestone
   is independently runnable — exactly the substrate an in-browser Emu198x (WASM,
   on the roadmap) needs to make each step a *run-it / tweak-a-value* widget. Design
   the per-unit manifest **WASM-aware now** (the same runnable `step-NN` feeds both
   captured media and a future in-page runner) so we don't re-do it later. Reading
   becomes doing.
2. **Debugging is a taught spine, not an afterthought.** The Primer planted "debug by
   observing" (u15) then dropped it. Every unit shows **"when it's wrong, here's how
   to *see* why"** by reading the machine's real state — the values that matter and
   what each symptom implies. Keep it **tool-neutral**: the learner checks values in
   their own code, and *if* their emulator has a monitor, live. Do **not** presuppose
   a specific emulator, and do **not** lean on Emu198x's own debug surfaces in
   learner-facing prose — Emu198x is *our* capture/verification tool, not necessarily
   the learner's runtime (and its debug-view story isn't one to promote yet).
3. **Historical / craft grounding — every attribution VALIDATED, never hand-waved.**
   Connect technique to the era's real software ("the starfield *Uridium* shipped",
   "why the pros flashed a frame on hit") — craft-with-heritage, on the 198x ethos.
   **But any attribution to a specific game or demo is a claim that must be sourced**
   (disassembly, original source, a credible technical write-up, the reference
   library) — exactly like every other provenance claim. The audience *includes the
   people who wrote and reverse-engineered these games*; a false "this is how X did
   it" is caught instantly and is unrecoverable. If we cannot verify it, we don't
   say it — at most "a common technique of the era," and only if *that* is true.
4. **Game feel is content, not garnish.** Why the timing, the flash, the feedback
   make a shot *feel good* — the gap between "it works" and "a good game." A game-dev
   curriculum that ignores juice teaches syntax, not craft. The voice/style guide
   carries this.
5. **Accessibility is a hard rule the media decision created.** Adding video + audio
   means meaning can no longer live *only* in the media — a screen-reader user, a
   sound-off learner, and a learner whose video washed the dithering all need it
   carried in prose / diagram / alt / transcript. **No milestone's point may live
   only in a clip.** Alt on every still and diagram; a described "what you'll hear"
   for audio; captions / described-action for video. Non-negotiable; lands in the
   `unit.md` amendment.

## The make-or-break: capture must be automated

Converting ~150+ units × N milestones × (still | video | audio) is only sustainable
if capture is **manifest-driven and one-command-regenerable**. A per-unit manifest
lists each milestone's runnable `step-NN` and its capture recipe (medium, frames,
injected input — joystick/fire — audio/video window); one command rebuilds every
still, clip, and recording for the unit. (Authored explanations — diagrams,
flowcharts, tables — live in the MDX, not the manifest.)

**Every capture saves the exact script that produced it,** committed *alongside the
artifact* — the Emu198x `--script` JSON (or VICE moncommands) plus the command,
ROMs, and `.prg`. The media is then never a mystery: any still, clip, or recording
can be re-run, diffed when the code changes, and **audited for honesty** — you can
read the script and see whether the fire button was genuinely injected or the state
was staged (the u8 question, made answerable). The script is the source; the
media is a build output of it.

**Captures reproduce from a cold boot — no staging, ever.** A capture boots the
machine from ROM and reaches its state the way the unit tells the *learner* to:
autostart / `LOAD` + `RUN`, then capture exactly what is on screen. **No monitor
pokes, no screen-clears, no `g <entry>` BASIC-bypass, no injected or hand-set
state.** If the boot banner, `LOAD` chatter, or `READY.` / `RUN` text is still on
screen, *that is the screenshot*, and the prose describes what is actually there —
not a cleaned-up ideal. If a unit wants a clean screen, the **program** clears it
(real, taught, reproducible), never the harness. This is why real input injection
(Emu198x boot → type `RUN` → inject the actual joystick/fire) is the pipeline, not
monitor-poked or rendered state — the saved script then has nothing to hide.
(Retires this session's `f 0400 07e7 20` clear, `g $080d` bypass, and the rendered
u8 border — all to be re-captured honestly on conversion.) Without this it rots exactly like the **16 empty placeholder PNGs**
in Starfield today. The pipeline proven this session — headless Emu198x (with the
joystick port-2 fix), cross-checked against VICE — is what makes this viable now
and didn't before. Building this tooling is part of the exemplar, not an afterthought.

## Scope — nothing is done until converted

This is a corpus-wide bar, not a going-forward-only convention. Everything built
the old way is **not done** until converted:

- The **C64 *Meet the Machine* primer** — marked `complete` 2026-06-04 (commit
  `04236f57`); reverts to `in-progress`.
- The **October launch content** — the Spectrum primer, the 8 BASIC games, the
  assembly opening (Gloaming + Shadowkeep start) — all built the old way.

## October

Per the launch spec, October is "a target, not a hard deadline." Stance: **convert
the launch content in time; do not slip the date if avoidable; if conversion can't
cover everything, shrink launch scope** (fewer games/units, fully converted) rather
than ship at the old bar. The October bar now *includes* "converted to this model."

## Why now — depth before breadth

This raises the bar **before** considering a third system or expanding the content
range. Get what we have to the real bar first; breadth waits.

## First move — the exemplar: Starfield u2 + u4 together

Convert both, because together they exercise the **full toolkit** the model must
handle — nothing hides:

- **u2 Joystick Movement** — input injection + **video** (the ship *moving* is
  motion a still can't show) + authored **diagram/table** (the game-loop flowchart
  and the joystick bit-table, both already present).
- **u4 Laser Sound** — **audio** capture (SID setup → trigger → sound) + fire input
  + register **tables** (SID/ADSR).

Between them: still + video + audio + diagram + table, in one exemplar pair. The
exemplar does three jobs: the **reference implementation**, it forces the
**`unit.md` amendment** (the detailed format contract), and it yields a real
**cost-per-unit** — the number that tells us how big the corpus conversion truly is
before we commit the calendar.

## Cost per unit (measured from the exemplar, 2026-06-04)

The exemplar (Starfield u2 + u4) is **built and verified**. What it cost, and
what it tells us about the corpus conversion:

**One-time costs — now paid, not per-unit:**

- The capture pipeline: `code-samples/_capture/capture.py` (manifest → saved
  Emu198x scripts → cold-boot run → media), reusable across every unit and platform.
- **Two emulator bugs, found and fixed** because the bar's "if we can't capture
  it honestly, it's a bug" rule forced real captures: the SID envelope 15-bit
  rate counter (silent audio) and the VIC sprite-position register readback
  (frozen movement). Both fixed in Emu198x with regression tests.
- Site-wide fixes: GFM tables enabled for MDX (`remark-gfm`); `CodeDiff`
  `context={3}` and the `step-00` / identical-header conventions established.

**Per-unit cost in steady state (tooling now in place):**

1. **Milestone decomposition + cumulative `step-NN.asm`** — low–moderate. The
   complete program already exists; splitting it into runnable steps is largely
   mechanical subtraction (+ a `step-00` baseline).
2. **`capture/manifest.json` + run + honest verification** — low. Capture is one
   command; the real work is *verifying* each artefact (view every still, check
   audio peaks, confirm the saved script injected genuine input). Minutes, not hours.
3. **MDX rewrite to the bar** — the dominant cost. A full authored unit
   (~150 lines): milestones, diff prose, diagrams/tables, debugging spine, game
   feel, accessibility. This is where the time goes.

**The headline finding:** with the pipeline built, per-unit cost is dominated by
**MDX authoring**, not capture — capture is cheap and regenerable. The genuine
variable is **emulator hardening**: 2 of the first 2 units surfaced a core bug.
Early units will keep finding gaps (each paid once, then gone); the rate should
fall sharply as the cores harden. **Budget the conversion as authoring-bound,
with an emulator-hardening tail that front-loads.** Concretely: a unit with no
new emulator gap is a focused authoring session; a unit that hits one can cost
several times that until the core is fixed. Plan the calendar around the
authoring count, and treat the hardening tail as the schedule risk.

## Knock-ons to propagate

- [`specifications/unit.md`](../specifications/unit.md) — **done (v3.0):** format
  contract added (§ *Incremental construction format*), derived from the exemplar.
- [`october-2026-launch-spec.md`](october-2026-launch-spec.md) — October bar now
  includes conversion; scope may shrink.
- [`../platforms/commodore-64/games/starfield/finishing-pass.md`](../platforms/commodore-64/games/starfield/finishing-pass.md)
  — the reorder + Primer-continuity findings still hold, but fold into this model
  (the screenshot approach is now manifest-driven step captures, not one-per-unit).
