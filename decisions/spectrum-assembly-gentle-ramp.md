# Decision: Spectrum Assembly — Gentle Complexity Ramp

> **STATUS: Active.** Accepted 2026-05-29. The governing decision for the assembly **opening**
> (Primer + tiny first game), the per-game **technique budget**, the **hybrid** difficulty
> ordering, and the **re-scope of Shadowkeep** (advanced rendering Trunk relocated to Greypeak).
> Amends — via AMENDED banners applied to each — `spectrum-assembly-track.md`,
> `shadowkeep-32-unit-commitment.md`, `shadowkeep-four-arc-framing.md`,
> `spectrum-assembly-per-game-scope.md`, and `october-2026-launch-spec.md`. The four open
> questions are resolved in § *Open questions*. The full unit-by-unit re-pace of Shadowkeep's
> plan, and the authoring of the Primer / tiny-game units, are downstream content work.

## The problem

The Spectrum Assembly track makes its **first game** carry two of the hardest loads
in the whole curriculum at once:

1. **Assembly from zero** — the toolchain, registers, the memory model, the
   no-safety-net mindset. The single biggest leap anywhere in the curriculum
   (BASIC → assembly).
2. **The commercial-engine Trunk** — `spectrum-assembly-track.md` makes Shadowkeep
   *"introduce Trunk Layers 1–4; every game inherits"*: pre-shifted sprites, masked
   drawing, Y-sort rendering, tile-map collision. Genuinely intermediate-to-advanced Z80.

The shipped 8-unit slice shows the cliff in raw form (lines of assembly per unit):

| Unit | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 |
|------|----|----|----|----|-----|-----|----|-----|
| Lines | 54 | 54 | 49 | **230** | **396** | **515** | 43 | 156 |

Unit 4 introduces ~12 concepts in one unit (keyboard matrix, `IN A,(C)`, `BIT`,
inverted key logic, RAM state, address arithmetic, 9-byte cell preservation, a move
helper, bounds, frame-rate limiting, `XOR A`). The 32-unit re-pacing helps the
*slope*, but it cannot lower the *ceiling*: by track design, game 1 must still summit
the engine course, because every later game inherits the Trunk.

Two further observations sharpen it:

- **The advanced Trunk is filed under the wrong game.** Shadowkeep's headline is
  *Atmosphere (Sense of Place)* — achievable with art, attribute lighting, room design
  and audio, all cell-based. Game 2 **Greypeak**'s headline is *Depth (Spatial
  Illusion)* — isometric, Ritman/Knight Lore — which is *literally what masking +
  Y-sort + pre-shifted sprites exist to do*. The hard rendering Trunk belongs in
  Greypeak, not Shadowkeep.
- **"Commercial bar" never required the advanced engine.** Manic Miner and Atic Atac
  (Shadowkeep's own ancestor) are cell-based and are classics. The old slice "read as
  a prototype" for want of art, polish and completeness — not for want of sub-cell
  sprite movement. The 32-unit commitment welded "commercial bar" to "advanced engine";
  they are separable.

## The governing principle

One rule generates the entire re-plan:

> **Technique budget.** Each game introduces at most **one or two major new core
> techniques** (the load-bearing hard ones — a rendering technique, a new data
> structure, a new control paradigm). Lighter supporting work (a palette, an extra
> room, an SFX) doesn't count against the budget but is still paced unit-by-unit.
> Where the current lineup forces a game over budget, **split the game or insert one
> ahead of it.** Complexity rises gently and close to monotonically.

This rule *produces* every decision below as a consequence — it isn't a target we
inflate toward. The game count is whatever falls out of honouring the budget.

**Precedent:** `shadowkeep-four-arc-framing.md` already practises the sibling move for
*genre* — combat, spells, classes, parser and quest-state were moved out of Shadowkeep
into the games where they're canonically primary (Embergate, Lantern Path, Edge of
Iron). Relocating the rendering Trunk to Greypeak is the same move applied to
*technique*. We are extending an established pattern.

## The opening (settled in session)

Two entries sit *ahead* of Shadowkeep, doing the assembly-onboarding that Shadowkeep
was silently assuming:

### Primer — "Meet the Machine" (not a game)

A bridge sequence whose job is to move the learner from a high-level mental model into
the machine's. **Floor: programming literacy** — assumes the reader has met variables,
loops, conditionals and subroutines *somewhere* (our BASIC, or any other language).
The spine is language-agnostic and concretely demonstrated in the emulator; references
to BASIC (or Python, or C) are *optional asides*, not load-bearing.

Beats (each light — one idea, a trivial task; "feels easy" is correct here):
- The toolchain: write source → assemble → run.
- `LD` is not `LET`: a register is a physical, finite 8-bit store, not a variable.
- Bytes have no type: `65`, `"A"`, a pixel pattern are one thing seen three ways.
- Memory is yours to manage (they already know `POKE`).
- **The screen is memory** ($4000) — poke a byte, pixels appear; `PLOT` was doing this all along.
- Attributes are memory too ($5800).
- Flags and conditional jumps vs `IF/THEN`; `DJNZ` vs `FOR`; `CALL`/`RET` vs `GOSUB`.

Outcome: fluent in the machine; has not built a game yet.

**Audience signpost (recommend, never gate):** a single line at the top —
*"New to programming entirely? You'll have a smoother time starting with the BASIC
course; this track assumes you've met variables, loops and subroutines before."* A
never-programmed learner may ignore it and dive in — that's their call, not ours to forbid.

### Game 1 — a tiny first game (cell-based, single screen)

Deliberately small by game-design standards. The achievement is *"I finished a real
game, in assembly,"* not ambition. Single screen, move a character (cell-based, with
background save/restore), simple collision, a win and a score.

- **New major techniques:** (1) the structured game loop (input → update → draw →
  repeat); (2) a cell-based moving sprite with preservation + simple collision.
- Introduces the *simple* technique versions that later games will visibly upgrade —
  the "before" half of the track's deprecation-pairs pedagogy.
- Rough scope: ~16–20 units.

## Shadowkeep, re-scoped (Path B)

Shadowkeep becomes the **atmospheric, cell-based flick-adventure** its own headline
already describes — and stays the October flagship and the first *substantial* game.

- **Keeps:** room-as-data + flick-screen transitions; attribute lighting / mood;
  authored level design; beeper SFX + composed theme; the four-arc structure;
  Arcs 3–4 essentially intact (items, multiple keeps, tape save/load, secrets/lore,
  atmospheric cycles, collection endings are all cell-based-friendly).
- **Loses (relocated):** pixel-level pre-shifted movement, masked sprite drawing,
  Y-sort layered rendering, tile-map-decoupled-from-attribute collision. These move to
  the rendering-Trunk games below.
- **New major techniques (now within budget):** room-data + flick transitions; +
  atmosphere (lighting + audio as supporting craft). Cell movement reused from Game 1.
- **Hits commercial bar through** art, lighting, room design, audio, completeness —
  the Manic Miner / Atic Atac route — not through sub-cell sprites.

This *reinforces* `shadowkeep-four-arc-framing.md`'s headline rather than contradicting
it, and lowers October risk by removing the hardest engineering from the launch artefact.

## The rendering Trunk, spread (not dumped on Greypeak)

Moving the Trunk to Greypeak triggers the budget rule *again*: iso projection + masking
+ Y-sort + pre-shift is itself a 4-technique pile-up. So it spreads across a short
rendering sub-sequence, each step motivated by a felt limitation of the previous game:

| Slot | Game | New major technique(s) | Motivated by |
|------|------|------------------------|--------------|
| (insert) | **"Smooth Motion"** (small) | Pre-shifted sprites (sub-cell movement) | "Your cell games stepped jerkily; arcade games glide." |
| (insert) | **"Overlap"** (small) | Masked sprite drawing | "Your sprite erased the wall it walked over." |
| 2 | **Greypeak** (Depth/iso) | Y-sort depth ordering + isometric projection | "Now make it look three-dimensional." |

Reached this way, Greypeak carries *two* new majors on a foundation already laid —
not four at once. Names for the two inserts are working-draft.

## Volume 1 — detailed (revised lineup)

The thematic identity of Volume 1 (*Rooms and Worlds*) is preserved; the budget rule
inserts/splits where the old 8-game lineup over-packs. Unit counts are rough floors,
to firm during build.

| # | Entry | Headline / role | New major technique(s) | ~Units |
|---|-------|-----------------|------------------------|--------|
| — | **Primer** | Meet the Machine | (machine literacy, not a game) | ~8–12 |
| 1 | **Tiny first game** | "I finished a game in asm" | game loop; cell sprite + collision | ~16–20 |
| 2 | **Shadowkeep** | Atmosphere | room-data + flick; atmosphere craft | 32 (Oct, Arcs 1–2); 64 full |
| 3 | **Smooth Motion** (insert) | smoothness | pre-shifted sprites | ~20 |
| 4 | **Overlap** (insert) | sprites over scenery | masking | ~20 |
| 5 | **Greypeak** | Depth (iso) | Y-sort + iso projection | ~56 |
| 6 | **Underlight** | Openness (non-linear geography) | large room-graph + map streaming | ~64 |
| 7 | **Whitewinter** | Scale (procedural vastness) | procedural generation + location-graph | ~80 |
| 8 | **Brace and Boon** | Duality (two characters) | dual-entity control + state | ~64 |
| 9 | **Embergate** | Power (action-RPG) | combat state machine; classes/XP/spells | ~80 |
| 10 | **The Lantern Path** | Conversation (parser world) | parser + dialogue + quest state | ~80 |
| 11 | **The Last Banner** | Decision (resource trade-offs) | tactical grid | ~48 |

**Flagged for the budget rule (need attention during detailed V1 build):**
- **Whitewinter, Embergate, Lantern Path** are each ~80-unit, multi-technique games
  (procedural + location-graph; combat + classes + XP + spells; parser + dialogue +
  quest). At 1–2 majors per game they likely each need internal sub-arc discipline or
  one or more inserts/splits. Detailed pacing deferred to their own spec passes, but
  flagged now.
- **Underlight** (non-linear geography) and **Brace and Boon** (two-character) are each
  a clean 1–2 majors and look budget-compatible as single games.

## Open structural tension — thematic vs difficulty ordering

The budget rule wants **monotonic difficulty**; volumes are organised **thematically**.
These conflict: Embergate (action-RPG, very hard) and Lantern Path (parser, very hard)
sit late in *Volume 1* by theme, yet are harder than much of Volumes 2–3. A learner
walking the lineup in order would hit a difficulty spike mid-Volume-1.

Three resolutions (a decision for Steve, not resolved here):
- **(a) Thematic volumes, ramp-within-volume.** Each volume re-ramps gently from its
  own floor; difficulty zig-zags across volume boundaries. Simplest; accepts spikes.
- **(b) A difficulty "spine" ordering** as the recommended learning path, with thematic
  volumes kept as a secondary index. Best for the learner; most restructuring.
- **(c) Hybrid:** engineer the *early* sequence (opening → ~Greypeak) to be strictly
  monotonic — that's where new learners are most fragile — and let later volumes assume
  a competent learner, ramping within-theme. **Recommended:** solves the real problem
  (the early cliff) without re-indexing a multi-decade track.

## Volumes 2–6 — sketch only (per agreed scope)

Not re-authored. Budget rule applied at low resolution to flag candidates:

- **V2 (Verticality):** Salt Caverns (Manic Miner) and Hollowhalls (JSW) are clean
  1–2 majors. The AY/128K audio introduction (The Witch's Year) is a single major —
  fine. No obvious over-pack.
- **V3 (Motion and Threat):** Hostraider (Cybernoid — dense art + projectile pools +
  Follin music) and Ironstreak (smooth scroll + T-state counting) each look like 2+
  majors; candidate split/insert points. Flag for their spec passes.
- **V4 (Real World / 3D):** Coldstar (Elite, 96u) and Coreworks (Freescape, 80u) are
  canonically huge multi-technique engines — strong split/sub-arc candidates.
- **V5 (demoscene) / V6 (Next):** late-curriculum; assume a competent learner; budget
  applied during their own design.

Detailed application deferred until each volume's spec pass — consistent with treating
mid/late-track reframe work as post-October.

## October 2026 launch — reframed

The launch artefact shifts from *"Shadowkeep Arcs 1–2, 32 units (8 shipped)"* to:

> **The gentle assembly opening:** Primer + a *complete* tiny first game + the start of
> the re-scoped (cell-based) Shadowkeep.

This is argued to be a **better and more achievable** launch: a learner can actually
*finish something* in assembly by October, and the hardest engineering is removed from
the critical path. The shipped 8 units are already cell-snapped, so they largely
survive into the re-scoped Shadowkeep / tiny game rather than being thrown away.
Final call on what anchors October is Steve's (see open questions).

## Records to amend (if accepted)

| Record | Change |
|--------|--------|
| `spectrum-assembly-track.md` | Add Primer + tiny game + the two rendering inserts; Shadowkeep no longer "introduces full Trunk Layers 1–4" (Trunk introduction spreads tiny-game → Smooth Motion → Overlap → Greypeak); record the technique-budget principle; resolve the thematic/difficulty ordering per § tension. Update 44→N entry count via this new track decision (satisfies that doc's own "new track decision" drift trigger). |
| `shadowkeep-32-unit-commitment.md` | Remove/relocate the three engine changes (pre-shift, Y-sort, attribute-decoupled collision); re-pace Arc 1–2 as cell-based atmosphere. Core "commercial bar" intent retained, now met via art/atmosphere. |
| `shadowkeep-four-arc-framing.md` | Mostly survives; reaffirm "Atmosphere" headline; confirm Arcs 3–4 are cell-based (they already are). Re-pace Arc 1–2 per-unit refinements. |
| `spectrum-assembly-per-game-scope.md` | Add budgets for Primer, tiny game, two inserts; reduce Shadowkeep Arc 1–2 engineering scope; adjust Greypeak. |
| `october-2026-launch-spec.md` | Reframe the assembly launch artefact per § October reframed. |
| `per-unit-plan.md` (Shadowkeep) | Re-pace to cell-based atmosphere; remove pre-shift/mask/Y-sort units. |

## Open questions — resolved 2026-05-29

1. **Ordering tension → (c) hybrid.** Early sequence (opening → Greypeak) is engineered
   strictly monotonic; later volumes assume a competent learner and ramp within-theme.
2. **October anchor → reframed.** Launch artefact becomes "opening + complete tiny game +
   start of re-scoped Shadowkeep", replacing "32 units of Shadowkeep". Applied to the launch spec.
3. **Insert names → deferred to build.** "Smooth Motion" / "Overlap" stay working titles; real
   inspired-by names when those games are spec'd.
4. **Tiny first game → working concept for now.** Earns a name / tradition slot when designed.

## Drift triggers (preliminary)

- **Re-loading game 1 with engine technique.** The opening's whole point is that the
  first game a learner builds is small. If a unit in the tiny game or early Shadowkeep
  reaches for pre-shift/mask/Y-sort, stop — that's the cliff returning.
- **Exceeding the technique budget without a split/insert.** A game quietly growing to
  3–4 new majors is the failure mode this decision exists to prevent.
- **Re-welding "commercial bar" to "advanced engine."** Cell-based games can hit
  commercial bar (Manic Miner, Atic Atac). Don't re-justify advanced rendering in
  Shadowkeep on "it has to look commercial."
- **Gating beginners out.** The BASIC-first advice is a recommendation, never a block.
