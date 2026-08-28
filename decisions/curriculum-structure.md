# Decision: Curriculum Structure

## The decision

The curriculum is a **sequence of modules** built to a **multi-disciplinary commercial quality bar**, with **no fixed game or unit counts**. A few things are locked; everything else falls out of them.

**Locked:**

- **Four systems carry the assembly track**: ZX Spectrum, C64, NES, Amiga. Gateway BASIC and HLL tracks exist where applicable and are governed by their own specs.
- **The quality bar.** Each game reaches **mid-tier full-price** — the £7.95 1987 Hewson / Gremlin / Mikro-Gen / Durell tier. Real commercial product, ambitious, not pretending to be Ultimate's absolute top. From [real-retro-games.md](real-retro-games.md) and [commercial-bar-revamp.md](commercial-bar-revamp.md).
- **The pacing discipline.** Complexity rises gently and close to monotonically, governed by the **per-unit one-concept rule** ([incremental-code-samples.md](incremental-code-samples.md), [spiral-and-incremental.md](spiral-and-incremental.md), [deprecation-pairs.md](deprecation-pairs.md)) and a **bounded unit count per game**.

**Not fixed — falls out of the locked parts:**

- **Game count per system.** A system carries as many games as it takes to cover the intended **genre breadth** while honouring the gentle ramp. Breadth across genres is a primary goal: a new genre wants a new game ([modules-not-games.md](modules-not-games.md)).
- **Unit count per game or module.** Counts are **illustrative markers, not contracts**; they firm up and move during build, set by the content and the quality bar. The unit count *is* the authoring-cost meter — roughly one unit of work per unit — so a game stays **bounded**: as long as it takes to be a good game at a gentle ramp, and no longer.
- **Phase shape.** Phases divide where a game's spiral progression naturally divides. There is no powers-of-2 phase-size rule.

### What bounds a game

Four constraints, and no cap on technique count:

1. **One new thing per unit** — the cognitive ramp.
2. **A bounded unit count per game** — the authoring cost.
3. **Each game must be a good, commercial-quality game in its own right.**
4. **The spiral** defers anything not yet earned to a later game.

Techniques per game are **uncapped**. A game's ladder identity is the game itself plus the techniques it *first introduces*; the ramp orders first-introductions — sprites before the Blitter — not whole games.

### Module, not game, is the unit of sequencing

The curriculum sequences **modules** ([modules-not-games.md](modules-not-games.md)). A module has a `kind`:

- `game` — builds a buildable game, the common case
- `teaching` — a non-game on-ramp, such as the Primer, *Meet the Machine*
- `interval` — a short between-game step into conceptual material ([between-game-intervals.md](between-game-intervals.md), exploratory)

One game can span several modules: a **revisit** returns to a game already built and upgrades a technique — the deprecation pair at game scale. So "how many games" and "how many modules" are different questions. The module sequence is the spine, and ordering is the catalogue's array position, not anything encoded in a slug.

## Why

Two mechanisms were tried before this one, and both legislated the wrong variable.

**Fixed unit counts per game** — 128, 256, 512 — were sized for code-led work. Under the multi-disciplinary commitment a unit costs two to three times its code-led predecessor, and at those counts the total compounds to multi-decade authoring time even at sustained pace. Counts had to become illustrative.

**A technique cap** — one or two major new techniques per game — then legislated *technique breadth* when the real cost driver is *unit count*. A sixteen-unit game costs about sixteen units to author whether it introduces two techniques or ten, and the good shipped games introduce many. Dash carries roughly nine across sixteen units, one per unit, and is good *because* it layers them gently rather than headlining one.

So the constraint sits on the thing that costs — bounded unit count — with the one-concept rule governing learner load and the spiral deferring un-earned depth.

## The acceleration assumption

A large module sequence across four systems is only viable if authoring accelerates as the project matures:

- **Pattern reuse** compounds across games on the same system.
- **Brief format and authoring workflow** mature, reducing per-unit overhead.
- **Visual and audio infrastructure** built for one game generalises to the next.
- **LLM-assisted authoring** improves over the project's lifespan.
- **Contributors and a community**, eventually, reduce the solo-authoring load.

Realistic acceleration brings later games to perhaps 60–70% of the first game's authoring time per system — not the tenfold speedup that would make the total a short project. The bet is that combined sources bend the curve enough to make the curriculum viable across years rather than decades.

**This assumption is load-bearing.** If acceleration does not materialise, scope must be cut: fewer games per system, fewer systems, or a longer timeline. The decision tree is per-system — if a system's first game takes longer than projected, defer its later games until acceleration materialises elsewhere.

## Per system

Lineups live in `docs/platforms/{system}/` and in the module catalogues (`src/content/modules/{system}/{track}.yaml`), sized by genre breadth and the gentle ramp rather than by a fixed count.

**Spectrum assembly** is the fully worked track: a `teaching` primer, then Gloaming, then Shadowkeep, then the rendering sequence and the rest of Volume 1. See [spectrum-assembly-gentle-ramp.md](spectrum-assembly-gentle-ramp.md).

**C64, NES and Amiga assembly** have their first substantial games designed — Cadence, Nightshade, Exodus. Subsequent games are sized when each brief is touched, and these tracks will likely grow their own opening as they are authored.

## Drift triggers

If curriculum-level planning shows any of these, stop and re-read this decision:

- Re-introducing a **fixed unit count** as a target — "256 per game", "phases must be 16 units". Counts are illustrative; the bound is unit count per game, held by the one-concept rule and must-be-a-good-game.
- Re-introducing **powers-of-2 phase sizing**.
- **Capping a system at a fixed game count** by fiat rather than by genre breadth and the gentle ramp.
- A **unit that introduces more than one new thing**. The one-concept rule is the real ramp constraint; techniques per game are uncapped.
- A game's **unit count ballooning** toward "teaches everything" — the original Exodus trap — a hundred-plus units across eight phases, and never a game.
- A game **contorted to headline a single technique** — "the Blitter game", "the sprites game" — at the cost of being a good game. Design the game; let it introduce whatever it needs, gently.
- **Collapsing distinct genres into revisits** to shrink the game count. Breadth is primary; a revisit returns to a specific game already built.
- Treating **acceleration as guaranteed** rather than as a load-bearing assumption.
- Per-game scope creeping toward **Ultimate top-tier** — Knight Lore or Head Over Heels scale, multi-frame everywhere.

## Status

Active. Captured 2026-05-13. Descends from [real-retro-games.md](real-retro-games.md); operationalised per track by [spectrum-assembly-gentle-ramp.md](spectrum-assembly-gentle-ramp.md); structure model in [modules-not-games.md](modules-not-games.md).
