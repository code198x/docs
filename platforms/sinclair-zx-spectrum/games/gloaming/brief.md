# Gloaming — Brief

**System / Track:** ZX Spectrum / Assembly
**Position:** Volume 1 — **two modules, one game** (per the 2026-07-02 amendment to
[spectrum-assembly-gentle-ramp.md](../../../../decisions/spectrum-assembly-gentle-ramp.md)):
**Module 1 "Gloaming"** (the tiny first game, after the Primer) and **Module 2 "The Long
Night"** (the revisit that deepens it), ahead of Shadowkeep.
**Status:** Realigned to the 14-section spec 2026-07-02, superseding the 2026-06-01 draft
and its amendment blocks. Both module endpoints are **built, gated, and human-playtested**
(`code-samples/.../gloaming/prototype/` — `gloaming-m1.asm` and `gloaming.asm`, suites in
`capture/`); this brief is the design contract those builds satisfy. Design history lives
in [`prototype-log.md`](prototype-log.md); the unit decomposition in
[`per-unit-plan.md`](per-unit-plan.md).

> *Dusk in a small square. You are the lamplighter; the dark is coming. Light every lamp
> before the night takes you — and then learn what it costs to hold the square until dawn.*

## 1. Pedagogical Role

**Module 1** is the first game a learner builds *and finishes* in assembly — the
load-bearing skill is the **structured, frame-locked game loop carrying a cell-based
character** (save/restore movement, attribute-byte collision). **Module 2**'s load-bearing
skill is **iteration**: data-driven behaviour and escalation applied to a finished game
the learner already owns, with every change motivated by a real playtest finding.

Module 1 carries exactly the two majors the gentle-ramp assigns and nothing heavier; it
teaches the "before" half of the track's deprecation pairs (cell-step movement, one-thing-
per-cell save/restore) honestly, not as a strawman. Module 2 adds data structures — a
table, a queue, a ring buffer — never new rendering technique. The cliff guard holds
across both: no pre-shift, no masking, no Y-sort, no multi-room. Assumes the Primer;
never blocks a newcomer.

## 2. Classic Ancestors

- ***Jetpac***, ***Pssst***, ***Cookie*** (Ultimate, 1983) — the single-screen line:
  small, complete, polished, classic. Module 1's shape and its lesson — a tiny finished
  game beats a sprawling unfinished one — are this tradition's.
- ***Pac-Man*** (Namco, 1980) — the antagonist's grammar, credited openly per
  [inspired-by-not-clones-naming.md](../../../../decisions/inspired-by-not-clones-naming.md):
  simple deterministic rules read as *intent* and *personality*; scatter rhythm keeps
  relentless pursuit fair. Gloaming's wisp is a one-ghost application of those lessons.

Module 2's creeping-dark character also owes a literary debt — **Mashadar in Shadar
Logoth** (*The Wheel of Time*) — credited in unit prose where the tendril is taught.

## 3. Remix Unit

**Same tropes, new core mechanic.** The 1983 single-screen arcade tropes are preserved —
one screen, one life-or-death antagonist, a completable objective, an ending that loops to
the title. The mechanical foundation is novel twice over: **the screen is the map and the
attribute byte is the rule** (collision, lamp state, glow, and solid night are all one-byte
cell states), and — module 2 — **light as territory**: lamps cast pools the dark must
route around while its tendril takes the ground between them. The fight over individual
cells *is* the game.

## 4. Core Experience

**Module 1 (moment to moment):** step, dodge, light. A tidy loop — see the cold lamp,
route around the buildings, reach it before the wisp reaches you — ending in a square you
brought back to light. Completion, warm and small.

**Module 2 (across a run):** a siege. The night hunts what you love oldest, takes ground
as it walks, and comes back faster each watch; every lamp is progress, decoy, and
territory at once. Five watches survived end in dawn — the run's texture is *pressure,
rhythm, and one earned morning*.

## 5. Constraint Position

**Period-faithful, 1983,** both modules. Nothing here a 1983 bedroom coder didn't ship.

- **In active use:** bitmap memory ($4000–$57FF: glyphs, ground stipple, brickwork, mist
  texture), attribute memory ($5800–$5AFF) as the visual *and* rules vocabulary, port
  `$FE` (half-row keyboard scan; beeper bit 4), IM 1 `HALT`-locked 50 Hz loop, ROM font.
- **Deliberately avoided:** pre-shifted/masked sprites and Y-sort (the Smooth Motion /
  Overlap revisits and later rungs), multi-room and flick (Shadowkeep), rendered digits
  (Shadowkeep's major — all scores here read as pips), 128K banking and AY (later games),
  randomness (fixed layouts are the era's mastery loop; determinism keeps the gate
  scripts honest).

## 6. Visual Direction

**The attribute palette is the art, the rules, and the signposting at once**, organised by
colour temperature: *warm = light, safe, progress; cold = dark, threat, to-do.* One
element per 8×8 cell; clash never bites.

- **The canvas first:** bare cobbles are a sparse blue stipple on black; walls and the two
  interior buildings are brickwork (white mortar courses on dusk-blue). The stipple is
  load-bearing, not decorative — every ground-state change (glow, solid night) is an ink
  recolour or occlusion of those pixels.
- **Cell vocabulary:** cobble (blue stipple), wall/building (blue brick), unlit lamp
  (steady cyan), lit lamp (BRIGHT yellow), glow pool (gold-ink stipple), solid night
  (dense BRIGHT-blue mist — a *presence*, never a void), lamplighter (BRIGHT white),
  wisp (cyan FLASH — flash is the dark's signature alone).
- **Forbidden combinations:** no walkable white-ink-on-black (hides the player); unlit
  lamps never FLASH (never read as the wisp); lit lamp and player differ in hue though
  both BRIGHT.
- **Progress as atmosphere:** the wall ramp warms with each lamp (mortar white → yellow,
  BRIGHT late; the full golden square is reserved for the win); module 2's dawn sweeps
  down the screen row by row, burning the mist off.
- **Magazine-screenshot test (module 2, mid-watch-three):** a stippled blue-black square
  bounded in brick; three golden pools pushing back the dark; a bright-blue mist tendril
  snaking from a building's face toward the oldest pool; the white lamplighter mid-stride
  for a cold cyan lamp; pip bar and lives in the HUD. Instantly Spectrum, instantly *this
  game*.

## 7. Audio Direction

Single-voice beeper throughout; phrases are blocking and used as **punctuation** — the
game pauses to say something, then resumes. One motif family carries the whole score
(authored as `.bpr` beside the source; routines emitted by `build198x beeper`):

- **The dusk bells** — cold A4 tolls with the E5→C5 motif "a lamp lit far off", D5 left
  hanging. Module 1 plays the opening tolls as a one-shot title chime; module 2 loops the
  full tune, polling SPACE between cells (a tune must yield the keyboard).
- **The blips** — lighting is a rising third quoting the dawn motif at blip speed;
  snuffing (module 2) falls the same third an octave down.
- **The fanfare** (win/held) — a rising C-E-G-C run; **the sting** (nightfall) — two
  steps down onto a long A4.
- **The dawn phrase** (module 2) — dusk's bell reversed: C5-E5-G5, the G5 leaning on the
  dominant so the fanfare's C answers it across the dawn sweep. Chosen by audition from
  three candidates (`dawn-candidates.bpr` preserved as the worked example).
- **In-game music: deliberately absent** — the square is quiet; the beeper speaks only
  when the world changes. Period-honest and it keeps the phrases meaningful.

## 8. Level Design Direction

- **Scale:** one square, 32×24 cells — rows 1–23 playable inside a brick border; two 4×3
  interior buildings; eight hand-placed lamps. Module 1 = one dusk on it; module 2 = five
  watches on it. The *same* square deepening is the point.
- **Pacing:** module 1 is gentle throughout (pace-16 hunt, playtest-approved). Module 2's
  curve is **escalation as data on two axes** — wisp pace 16/13/11/9/9 and tendril reach
  3/6/9/13/18 per watch. Both tables were tuned by play: pace 8 is the human wall (the
  final watch is the climax, not the ceiling), and reach front-loading broke watch one.
- **Signposting:** colour temperature does it all — cold is task and threat, warm is done
  and safe. No tutorial text anywhere.
- **Onboarding:** the gathering (the wisp holds ~2.4 s at dusk-start — read the square,
  pick a route); in module 2, the first lamp *redirects the hunt off your back*, teaching
  the targeting rule by consequence.
- **Fairness by construction:** the catch recoils the wisp to its corner (a life buys a
  fresh chase); the withdraw-and-rest rhythm guarantees a window after every snuff; the
  tendril's ring release means the square can never be permanently walled.

## 9. Polish Direction

- **Title:** GLOAMING in ROM font on black, the chime/bells, PRESS SPACE — sparse and
  suggestive. **Attract mode: absent** (period-honest at this scale). **Options: none**
  (QAOP+Space fixed, one difficulty — the watches are the difficulty).
- **Endings:** both land. Win/held: the golden square with the fanfare; module 2's dawn
  adds the chime→sweep→fanfare ceremony. Loss: NIGHT FALLS over absolute black with the
  sting. Input locks (`LOCK 25`) make every ending dwell; playtest confirmed the lock is
  invisible, which is the pass condition for an input lock.
- **The Finish, answered:** *Win* — all eight lamps (module 1) / five watches → DAWN
  BREAKS (module 2). *Curve* — the two dusk tables, read live. *Music and stings* — the
  bells, the fanfare, the sting, the dawn phrase (all shipped). *Endings that land* —
  locks plus the dawn sweep. *Feel* — the repeat-gated key (first press instant, then one
  step per 6 frames, release re-arms), the gathering, the recoil. *Go-again* — module 1:
  best-lives pips ("the lives you kept on your finest win"); module 2: the longest-night
  row, dawn filling it. All pips, no digits.
- **Shippable:** both builds already pass their winnability gates and human playtests;
  the Itch.io-adjacent bar is the authored polish (this section) holding through the
  units.

## 10. Anti-goals

- **No pre-shift, no masking, no Y-sort, no multi-room, no flick** — the cliff; later
  rungs own these.
- **No rendered digits** — Shadowkeep's major; every count here is pips.
- **No randomness** — layouts, spawns, and behaviour are deterministic; variety comes
  from data (watch corners, tables), and the gate scripts stay repeatable.
- **No second wisp, no pathfinding** — one antagonist, one compare-and-step rule; its
  intelligence is rhythm and targeting, never search.
- **No snuffing, tendril, pools, or watches in module 1** — the module boundary is a
  scope wall; the tiny game stays tiny.
- **No 128K, no AY** — later games.

## 11. Phase Trajectory

Unit-level detail lives in [`per-unit-plan.md`](per-unit-plan.md); counts are
illustrative, never targets. Deliverables are real: both module endpoints exist and are
gated today — authoring decomposes proven builds.

**Module 1 — Gloaming (~20 units, five phases):**

| Phase | New | Revisits | Phase-end deliverable |
|---|---|---|---|
| A. A square at dusk (4) | attrs-as-map, the textured canvas, a glyph, the HALT loop | — | the lit, bricked, textured square with a lamplighter standing in it |
| B. Movement (6) | key scan, cell step, the repeat gate, save/restore, wall bit-test + buildings, bounds | the loop carries update phases | the lamplighter walks the square honestly |
| C. A game (5) | lamp state, lighting, pips, the warm ramp, the win | save/restore becomes *rules* (the under-byte) | the completable toy — the 15→16 seam teaches "a game needs a way to lose" |
| D. Jeopardy (2) | the hunting wisp (timer idiom revisited), lives, recoil, loss | movement code drives a second mover | **the tiny game** — winnable, losable |
| E. Finish (3) | blips, chime, title, the again-loop, best-lives pips | the state machine closes | the shipping module-1 build (= `gloaming-m1.asm`) |

**Module 2 — The Long Night (~10 units, one arc):** each unit is one behaviour or system
from the reshape, taught with its playtest confession — nearest-light seek and snuffing;
withdraw-and-rest; pools; the tendril (ring buffer); oldest-lit (the grudge queue); the
two-axis deepening and watches; the dawn; the bells; the longest night; the dawn phrase
and the `.bpr` workflow. Phase-end deliverable: the five-watch night (= `gloaming.asm`),
the game the author beat unassisted on 2026-07-02.

## 12. Ship Test

Per module, all five axes:

- **Code:** assembles (pasmonext), runs (Emu198x), per-unit DoD green.
- **Visuals:** §6 vocabulary holds; the magazine-screenshot test passes (module 1: the
  warm-ramped square mid-play; module 2: the watch-three shot described above).
- **Audio:** module 1 — chime, blip, fanfare, sting; module 2 — the full bell loop and
  dawn phrase; all phrases land as punctuation, none as lag.
- **Level design:** winnable by scripted run *and* by hands — **both already pass**:
  suites in `prototype/capture/` (`m1-won/m1-sting/m1-probe`; `won/dawn/sting/probe` +
  audio), human playtests logged 2026-07-02. The menace probes are part of the bar: an
  idle player must lose.
- **Polish:** endings dwell, the go-again pips survive the loop, no soft-locks (the
  tendril's ring release is the structural guarantee).

## 13. Pattern Library Extractions

- **ai** — *seek-step*: one compare-and-step rule reading as intent (cross-platform).
  *Oldest-grievance targeting*: a lit-order queue that spreads pressure and prevents
  camping (cross-platform). *Scatter rhythm*: hunt → take → withdraw → rest as a fairness
  device (cross-platform).
- **framework** — *escalation-as-data on two axes* (extends the existing pattern).
  *Ring-buffer territory trail*: fixed-length claimed ground with release-on-overflow —
  no-permanent-walls by construction (cross-platform, the module's crown jewel).
  *Interstitial state machine*: win-as-continuation (watch → watch) vs win-as-ending.
- **input** — *repeat-gated held key*: instant first step, timed repeats, release re-arms
  (cross-platform; the same timer idiom drives the antagonist's pace).
- **rendering** — *attribute-byte-as-rule* (extends Shadowkeep's entry: here it carries
  five cell states). *Texture blit under attrs*: ground state made visible by ink-only
  changes over a stippled canvas (Spectrum-specific; the visibility-substrate principle
  generalises).
- **audio** — *beep-and-rest phrase style* with blocking phrases as punctuation; the
  `.bpr` → `build198x beeper` authoring workflow.

## 14. Vault Tie-ins

- *Jetpac* (Ultimate, 1983) — direct ancestor (the single-screen line).
- *Pssst* (Ultimate, 1983), *Cookie* (Ultimate, 1983) — sibling ancestors.
- Ultimate Play the Game — studio entry.
- *Pac-Man* (Namco, 1980) — the ghost-AI and scatter lessons, taught by name in the
  wisp and grudge units.
- ZX Spectrum attribute system (hardware page) — every rules unit references it.
- ZX Spectrum beeper / port `$FE` (hardware page) — the audio units.
- Kempston/QAOP input conventions (hardware/culture page) — the keys unit.

(The Mashadar debt is credited in unit prose, not the vault — literary influence, not a
catalogued game.)
