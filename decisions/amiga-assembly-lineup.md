# Decision: Amiga Assembly — custom-chip hardware ladder lineup

> **STATUS: Active.** Accepted 2026-06-10 as part of the 2026 lineup replan. Records the
> re-sequenced lineup and the **Exodus re-scope**. The shipped primer (`meet-the-machine`) is
> **locked**. Assembly is the *metal* path — a deeper road than AMOS/Blitz, **peer in worth, not
> above them** (it ranks *techniques* by hardware difficulty, never the *tracks*). Counts flexible;
> the catalogue is authoritative (`website/src/content/modules/commodore-amiga/assembly.yaml`).

## The decision

The Amiga's hard part is driving the custom chips — Agnus/Denise/Paula — by hand to draw moving
things cleanly. The track is a **hardware ladder**: one rung per game, every later game inheriting
the rungs below.

| # | Module | Rung / headline |
|---|---|---|
| 1 | **Exodus** | Blitter copy + masked (cookie-cut) blit — the Blitter is the gameplay (re-scoped) |
| 2 | Shatter Point | Copper splits + first Paula samples |
| — | **How the Copper Works** | *interval* — a built demo of Copper DMA (see below) |
| 3 | Signal | hardware sprites (re-sequenced after Shatter Point) |
| 4 | Ascent | jump physics + Blitter cookie-cut enemies |
| 5 | Crypt | rooms + Copper transitions + state |
| 6 | Gobble | Blitter tiles + ghost AI |
| 7 | Wanderer | smooth hardware scrolling (Shadow of the Beast) |
| 8 | Onslaught | full MOD replay on Paula + bullet patterns |
| 9 | Highway | Copper road rendering + sprite scaling (Lotus) |
| 10 | Parallax | dual playfield — multi-layer parallax + boss |
| 11 | Brawler | Y-depth sorting + large Blitter objects |
| 12 | Fortress | isometric projection + depth sort |
| 13 | Echoes of the Ancients | connected metroidvania world + ability-gating + multi-disk |
| 14 | Ascension: The Guru Meditation | capstone — custom loaders, deep combat, full save |

## Key choices

- **Exodus re-scoped (the load-bearing change).** Exodus was a 128-unit / 8-phase
  "teaches-everything" flagship at 16/128 — the all-in-one model the ladder replaces. The **16 built
  units stay** (Copper Landscape → Integration and Polish — a finishable terrain game); the 112-unit
  future scaffold is dropped, and the Copper/Paula/sprite/scroll material it would have grown into
  moves out to the dedicated rung-games. Exodus becomes **the Blitter game** (rungs 1–2). This
  contradicted Exodus's old 128-unit frontmatter, which is why it needed an explicit decision; it
  preserves shipped work while shrinking scope to one rung pair.
- **Signal re-sequenced after Shatter Point** so hardware sprites land as its *one* new rung (it had
  implied Copper + sprites + Blitter + Paula all at once — a 4-new game).
- **`venom` (Snake) and `tetrad` (Tetris) dropped.** Off the hardware ladder — the same call the
  Spectrum track made dropping its own snake/Tetris. Not re-anchored to a rung; removed.
- **A "How the Copper Works" interval** sits after Shatter Point (which introduces Copper) — the
  first concrete [between-game-intervals.md](between-game-intervals.md) module, authored as a
  **buildable demo** ([modules-not-games.md](modules-not-games.md) § Non-game artefacts) rather than
  prose theory. It pays off the Copper splits with the DMA list underneath.
- **Fortress (iso) before Echoes (metroidvania)** — both are large late-game worlds; iso composition
  precedes the connected-world capstone run.
- **No new games added** beyond the interval — assembly already had the breadth (16 modules). The
  work was pacing discipline (one new rung per game; the four-skills-per-game arrays demoted to
  explicit revisits) and anchoring each game to a real Amiga classic.

## Teardown on apply

Every coming-soon module carried a 128-unit stub scaffold; torn down (catalogue-only, no fake
counts), except **Exodus** which keeps its 16 built units. Mirrors the Starfield/Dash re-scope
precedent.

## Still open

- Whether to insert further interval modules (per between-game-intervals.md, still exploratory) —
  the Copper one is the first; cadence stays editorial.
- Working titles where not shipped (Ascension/Echoes/etc.).

## Provenance

Applied from `docs/tracker/lineup-replan/amiga-assembly.md` (the reviewed proposal), with the agreed
venom/tetrad drop and the Copper DMA interval added.
