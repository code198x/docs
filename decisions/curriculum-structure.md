# Decision: Curriculum Structure

## The decision

The curriculum is a **sequence of modules** built to a **multi-disciplinary commercial
quality bar**, with **no fixed game or unit counts**. A few things are locked; everything
else falls out of them.

**Locked:**

- **4 platforms** carry the assembly track: ZX Spectrum, C64, NES, Amiga. (Gateway
  BASIC/HLL tracks exist where applicable — e.g. Spectrum BASIC — and are governed by
  their own specs, not this one.)
- **The quality bar.** Each game reaches **mid-tier full-price** — the £7.95 1987
  Hewson / Gremlin / Mikro-Gen / Durell tier. Real commercial product, ambitious, not
  pretending to be Ultimate's absolute top. From [real-retro-games.md](real-retro-games.md)
  and [commercial-bar-revamp.md](commercial-bar-revamp.md).
- **The pacing discipline.** Complexity rises gently and close to monotonically, governed
  by the per-game **technique budget** ([spectrum-assembly-gentle-ramp.md](spectrum-assembly-gentle-ramp.md))
  and the per-unit one-concept rule ([incremental-code-samples.md](incremental-code-samples.md),
  [spiral-and-incremental.md](spiral-and-incremental.md), [deprecation-pairs.md](deprecation-pairs.md)).

**Not fixed — falls out of the locked parts:**

- **Game count per platform.** A platform carries as many games as it takes to cover the
  intended **genre breadth** while honouring the technique budget. Breadth across genres
  is a primary goal — a new genre wants a new game ([modules-not-games.md](modules-not-games.md)).
  The old "4 games per platform" lock is retired: the Spectrum assembly lineup alone now
  sketches ~11 Volume-1 entries.
- **Unit count per game or module.** No targets. Counts are **illustrative markers, not
  contracts** — every "~N units" / "32" in the outlines is a marker that firms up and moves
  during build. Content and the quality bar decide how many units; the technique budget,
  not a unit total, is what caps authoring cost.
- **Phase shape.** Phases divide where a game's spiral progression naturally divides. There
  is no powers-of-2 phase-size rule (an earlier aesthetic preference, now dropped).

### Module, not game, is the unit of sequencing

The curriculum sequences **modules** ([modules-not-games.md](modules-not-games.md)). A
module has a `kind`:

- `game` — builds a buildable game (the common case);
- `teaching` — a non-game on-ramp (e.g. the Primer, *Meet the Machine*);
- `interval` — a short between-game step into conceptual/academic material
  ([between-game-intervals.md](between-game-intervals.md), exploratory).

One game can span several modules — a **revisit** returns to a game already built and
upgrades a technique (the deprecation pair at game scale). So "how many games" and "how
many modules" are different questions; the module sequence is the spine, and ordering is
the module catalogue's array position, not anything encoded in a slug.

## Why

Earlier curriculum versions oscillated between 16-game tracks (v3.0) and 4-game tracks
(v4.0), with code-led per-game unit counts (128/256/512/512). Under
[real-retro-games.md](real-retro-games.md), multi-disciplinary units cost 2–3× their
code-led predecessors, and at those costs the v4.0 counts compound to multi-decade
authoring time even at sustained pace.

The previous answer — lock every game to 256 units, phases to powers of 2 — had the right
instinct (rein in the code-led counts) but the wrong mechanism. A fixed unit total
legislates the *output* when the real constraint is the *input*: how much new hard
technique a game introduces. The honest version caps that directly. The **technique
budget** (1–2 major new core techniques per game; split or insert when a game would exceed
it) is what actually governs authoring cost and learner load; unit and game counts are
then free to be whatever the content and the quality bar require. This is why the structure
is now budget-and-bar driven with counts illustrative, rather than a fixed grid.

## The acceleration assumption (load-bearing)

A large module sequence across four platforms is only viable if authoring accelerates as
the project matures. Specifically:

- **Pattern reuse** compounds across games on the same platform.
- **Brief format and authoring workflow** mature, reducing per-unit overhead.
- **Visual/audio infrastructure** built for one game generalises to the next.
- **LLM-assisted authoring** improves over the project's lifespan.
- **Eventually, contributors and a community** generate patterns and reduce the
  solo-authoring load.

Realistic acceleration likely brings later games to 60–70% of the first game's authoring
time per platform — not the 10× speedup that would make the total a short project. The bet
is that *combined* acceleration sources bend the curve enough to make the whole curriculum
viable across years rather than decades.

**This assumption is load-bearing.** If acceleration doesn't materialise, scope must be
cut — fewer games per platform, fewer platforms, or a longer timeline. The decision tree is
per-platform: if a platform's first game takes longer than projected, defer its later games
until acceleration materialises elsewhere first.

## What this means per platform

Per-platform lineups live in `docs/platforms/{system}/` and in the module catalogues
(`src/content/modules/{platform}/{track}.yaml`), sized by genre breadth and the technique
budget rather than a fixed count:

- **Spectrum (assembly).** The fully worked lineup. A `teaching` Primer (*Meet the
  Machine*), then **Gloaming** (the tiny first game), then **Shadowkeep** (the first
  substantial game, October flagship), then the rendering-technique sequence and the rest
  of Volume 1 (~11 entries), with Volumes 2–6 sketched. See
  [spectrum-assembly-gentle-ramp.md](spectrum-assembly-gentle-ramp.md).
- **C64 / NES / Amiga (assembly).** First substantial games are designed (Cadence,
  Nightshade, Exodus); subsequent games are sized by genre breadth and budget when each
  brief is touched. The same gentle-ramp discipline applies — these tracks will likely
  grow their own opening (a teaching module + a tiny first game) when authored.

## Drift triggers

If curriculum-level planning shows any of these, stop and re-read this decision:

- Re-introducing a **fixed unit count** ("256 per game", "phase must be 16 units") as a
  target — counts are illustrative markers; the budget is on *techniques*.
- Re-introducing **powers-of-2 phase sizing** as a rule.
- **Capping a platform at a fixed game count** by fiat rather than by genre breadth +
  technique budget.
- A new game proposed at **3–4 new major techniques** without a split or insert (the
  gentle-ramp budget violation).
- **Collapsing distinct genres into revisits** to shrink the game count — breadth across
  genres is primary; a revisit is for returning to a *specific game we built*.
- Treating **acceleration as guaranteed** rather than a load-bearing assumption.
- Per-game scope creeping toward **Ultimate top-tier** (Knight Lore / Head Over Heels
  scale with multi-frame everywhere).

## Status

Active. Captured 2026-05-13; **rewritten 2026-06-01** around the module model, the technique
budget, and no-fixed-unit-counts. The original 4-games-per-platform / 256-units-per-game /
powers-of-2-phases model is retired (see § Why) — the multi-disciplinary bar and the
acceleration assumption are carried forward intact. Descends from
[real-retro-games.md](real-retro-games.md); operationalised per-track by
[spectrum-assembly-gentle-ramp.md](spectrum-assembly-gentle-ramp.md); structure model in
[modules-not-games.md](modules-not-games.md). Per-platform curriculum docs live under
`docs/platforms/{system}/`.
