# Decision: Curriculum Structure

> **AMENDED 2026-06-10 (technique budget reframed).** The original "1–2 major new core techniques
> per game" budget is **retired as a per-game cap.** Evidence overruled it: the good shipped games
> (Dash on NES — ~9 techniques across 16 units, one per unit) are good *because* they layer many
> techniques gently, not because they headline one. The budget was only ever a proxy for capping
> authoring cost — and cost is bounded by **unit count, not technique count** (a 16-unit game costs
> the same to author whether it teaches 2 techniques or 10). So the real constraints are: **one new
> thing per unit** (the cognitive ramp), **a bounded unit count per game** (the authoring cost),
> **each game must be a good, commercial-quality game in its own right**, and **the spiral** defers
> anything not yet earned to a later game. Techniques-per-game is **uncapped**. A game's ladder
> identity is the *game itself* plus the techniques it *first introduces* — the ramp orders
> first-introductions (sprites before the Blitter, etc.), not whole games. The anti-bloat wall is
> unchanged in spirit (see Drift triggers); it's now enforced by unit-count + must-be-a-good-game,
> not a technique cap. This is what un-stuck the Amiga reorder — see
> [amiga-assembly-lineup.md](amiga-assembly-lineup.md).

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
  by the **per-unit one-concept rule** ([incremental-code-samples.md](incremental-code-samples.md),
  [spiral-and-incremental.md](spiral-and-incremental.md), [deprecation-pairs.md](deprecation-pairs.md))
  and a **bounded unit count per game** — not a per-game technique cap (retired; see the
  2026-06-10 amendment above and [spectrum-assembly-gentle-ramp.md](spectrum-assembly-gentle-ramp.md)).

**Not fixed — falls out of the locked parts:**

- **Game count per platform.** A platform carries as many games as it takes to cover the
  intended **genre breadth** while honouring the gentle ramp. Breadth across genres
  is a primary goal — a new genre wants a new game ([modules-not-games.md](modules-not-games.md)).
  The old "4 games per platform" lock is retired: the Spectrum assembly lineup alone now
  sketches ~11 Volume-1 entries.
- **Unit count per game or module.** No fixed *targets* — counts are **illustrative markers,
  not contracts** that firm up and move during build, set by the content and the quality bar.
  But the unit count *is* the authoring-cost meter (one unit ≈ one unit of work), so a game stays
  **bounded** — as long as it takes to be a good game at a gentle ramp, and no longer. That
  bound, plus the per-unit one-concept rule, is what governs cost and load.
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
instinct (rein in the code-led counts) but the wrong mechanism. The first correction (a
"1–2 techniques per game" budget) had the *next* wrong mechanism: it legislated *technique
breadth* when the real cost driver is *unit count*. A 16-unit game costs ~16 units to author
whether it introduces two techniques or ten — and the good shipped games (Dash) introduce
many, one per unit, and are better for it. So the honest version caps the thing that
actually costs: **bounded unit count per game**, with the **per-unit one-concept rule** governing
learner load and **the spiral** deferring un-earned depth to later games. Techniques-per-game
is uncapped; the constraint is "stay a good game at a gentle ramp, no longer." This is why
the structure is now ramp-and-bar driven with counts illustrative, rather than a fixed grid
*or* a technique quota.

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
(`src/content/modules/{platform}/{track}.yaml`), sized by genre breadth and the gentle ramp
rather than a fixed count:

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
  target — counts are illustrative markers; the bound is on *unit count per game*,
  held by the per-unit one-concept rule and must-be-a-good-game.
- Re-introducing **powers-of-2 phase sizing** as a rule.
- **Capping a platform at a fixed game count** by fiat rather than by genre breadth +
  the gentle ramp.
- A **unit** that introduces **more than one new thing** (the one-concept rule is the real
  ramp constraint — techniques-per-*game* is uncapped, per the 2026-06-10 amendment).
- A game's **unit count ballooning** toward "teaches everything" (the original-Exodus trap:
  128 units, 8 phases, never actually a game). Bounded unit count + must-be-a-good-game is the
  anti-bloat wall now that the technique cap is gone.
- A game **contorted to headline a single technique** ("the Blitter game", "the sprites game")
  at the cost of being a good game — the Exodus mistake. Design the *game*; let it introduce
  whatever techniques it needs, gently, with the spiral deepening later.
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
