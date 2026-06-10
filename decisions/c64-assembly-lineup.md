# Decision: C64 Assembly — VIC-II / 6502 hardware ladder lineup

> **STATUS: Active.** Accepted 2026-06-10 as part of the 2026 lineup replan. Records the
> re-sequenced assembly lineup. The two shipped anchors (`meet-the-machine`, `starfield`) are
> **locked**. Counts flexible; names are working titles pending the naming pass. The catalogue is
> authoritative (`website/src/content/modules/commodore-64/assembly.yaml`).

## The decision

Where the Spectrum's hard part is *software* (drawing moving things cleanly), the C64's is *the
hardware* — the VIC-II hands you sprites, a raster beam you can interrupt and a smooth-scroll
register, but each is a doorway to a deeper technique. So the C64 track is a **VIC-II / 6502
hardware ladder**: one rung per game, every later game inheriting the rungs below.

| Rung | Technique | Game |
|---|---|---|
| 0 | char/screen + colour memory | Meet the Machine + Starfield (shipped) |
| 1 | hardware sprites (physics, collision) | Platform Panic |
| 2 | custom charsets + tile maps | Maze Raider |
| (consolidation) | ball physics on a char field | Brick Basher |
| 3 | raster interrupt / split screen | Night Raid |
| 4 | smooth hardware scrolling | Scroll Runner |
| 5 | sprite multiplexing | Sprite Storm |
| 6 | interrupt-driven SID music | SID Symphony |
| — | large scrolling world + items | Catacombs |
| — | per-line raster road | Raster Rider |
| 7 | raster-time budgeting (integration) | **Overdrive** (new) |
| — | disk I/O + save | Dungeon Crawl |
| — | isometric depth-sort (the hard render, last) | Isometric Quest |

Optional later **breadth** games (sequence when their rung is owned, not launch-gating): Mega
Blaster (scroll-action platformer), Arena Fighter (beat-'em-up), Parallax Patrol (layered parallax).

Sprites, SID and raster interrupts are *introduced* at primer level inside Starfield, so the games
below **deepen** them rather than introducing them cold — the C64 equivalent of "Shadowkeep
introduces masking; Lamplight deepens it."

## Key choices

- **`symphonys-end` dropped; `overdrive` added.** The old "capstone with demo-scene techniques"
  (`symphonys-end`) was a *duplicate* all-techniques capstone — the demo-scene / full-showcase role
  is the **Cadence** flagship's job. Its content (stable IRQ chains, raster bars, everything at once)
  is exactly the rung-7 raster-budgeting material, which the new **Overdrive** integration game now
  teaches. The `symphonys-end` slug is **parked** (not reused); the name could later return as a
  Cadence-track finale.
- **Cadence stays the deferred post-launch flagship** — the music-driven showcase capstone, off the
  launch critical path (consistent with [commercial-bar-revamp.md](commercial-bar-revamp.md) and
  the launch spec). Overdrive is the in-ladder integration game, not a Cadence substitute.
- **`night-raid` re-sequenced earlier** (to the raster-split slot) so the raster interrupt is taught
  before the scroller leans on it.
- **Isometric depth-sort is last** — by the time you reach it you own multiplexing-with-sorting,
  tiles, save and music, so it adds *one* concept, not six.

## Teardown on apply

Every coming-soon module carried a 64–256-unit auto-generated stub scaffold (`symphonys-end` had
256). These were torn down on apply, mirroring the Starfield re-scope precedent
([october-2026-launch-spec.md](october-2026-launch-spec.md), 2026-06-03) — coming-soon games are
catalogue-only with no fake unit counts. `catacombs` and `sid-symphony` previously had catalogue
rows but no module page; pages were added so the ladder's links resolve.

## Still open

- **Naming** — `Overdrive` is a working title; could be where a re-scoped `symphonys-end` name
  returns. Mega Blaster / Arena Fighter / Parallax Patrol breadth placement firms up when briefed.
- **Brick Basher** is a consolidation game (no new rung); fine as a breather, or fold its mechanics
  elsewhere if the ladder wants tightening.

## Provenance

Applied from `docs/tracker/lineup-replan/c64-assembly.md` (the reviewed proposal).
