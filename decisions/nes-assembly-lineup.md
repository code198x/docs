# Decision: NES Assembly — PPU / 6502 hardware ladder lineup

> **STATUS: Active.** Accepted 2026-06-10 as part of the 2026 lineup replan. Records the
> re-sequenced lineup and the **Dash re-scope**. The shipped primer (`meet-the-machine`, 18 units)
> is **locked**. Counts flexible; names are working titles. The catalogue is authoritative
> (`website/src/content/modules/nintendo-entertainment-system/assembly.yaml`).

## The decision

The NES's hard part is **driving the PPU** — tiles, sprites, scroll, palettes and sound out of a
chip that gives nothing for free and only lets you touch most of it during vblank. So the track is a
**PPU / 6502 hardware ladder**: one rung per game, every later game inheriting the rungs below.

| # | Game | Rung / headline |
|---|---|---|
| 1 | **Dash** | OAM sprite + controller + the NMI game loop (the first finishable game) |
| 2 | Crate Escape | metasprites + sprite animation |
| 3 | Fracture Point | attribute tables + palette swaps |
| 4 | Pellet Panic | chase AI on a tile grid |
| 5 | Fangs for the Memory | data structures (ring buffer) |
| 6 | **Thunder Run** | **APU music + SFX engine** (pulled early — see below) |
| 7 | Pixel Plains | PPU scrolling, single-screen → two-screen |
| 8 | Ion Trail | infinite scrolling (column feed) |
| 9 | Crypt Crawler | rooms + persistent state (flip-screen) |
| 10 | Gridlock | big game logic, still NROM |
| 11 | **Iron Assault** | **MMC1 — bank switching (the first and only mapper rung)** |
| 12 | Pavement Justice | Y-depth sorting + combat (revisits MMC1) |
| 13 | Tarmac Terror | IRQ scanline tricks (pseudo-3D road) |
| 14 | **Echoes of Eponium** | **MMC3 — IRQ split + CHR banking, in service of the metroidvania** |
| 15 | Requiem for a Mapper | capstone — integrate everything |

## Key choices (the agreed modifications)

- **Dash re-scoped to ~16 finishable units.** `dash.yaml` was a 16-of-128 module: 16 real, named
  units padded with 112 `Unit NN` stubs across an 8-phase scaffold. Re-scoped to the 16 real units in
  a single phase, exactly as **C64 Starfield** was re-scoped (the 2026-06-03 launch amendment). Dash
  is the NES priority — the first *finishable* game; it owns **one** new rung (OAM sprite + NMI loop),
  nothing else.
- **Mappers land late, and there is only one mapper *rung*.** Games 1–10 run on plain **NROM**. The
  **first mapper is MMC1 at Iron Assault (#11)** — "more game than fits in 32KB" as a *felt* problem,
  not a concept introduced cold. **MMC3 is not a second mapper game** — it is the one-new-thing the
  metroidvania (Echoes, #14) introduces, because that genre genuinely needs IRQ split + CHR banking.
  One mapper introduction, one mapper deepening-in-context.
- **The scroll rungs are split across two games.** Single-screen → two-screen scrolling (rung 4) is
  **Pixel Plains**; infinite column-fed scrolling (rung 5) is **Ion Trail**. The original proposal
  folded both into one game; splitting them keeps the steep single→infinite jump to one new idea per
  game.
- **APU pulled earlier.** The music + SFX engine moves up to **Thunder Run (#6)** so the early games
  aren't silent for eight modules; the early games still seed it with single-channel beeps (Dash's
  jump/collect sounds).
- **`arena-assault` parked.** Its multiplex + wave-AI material folds into Ion Trail and Iron Assault;
  surfacing it separately duplicated the shooter rung. Slug parked (not reused).

## Teardown on apply

Every coming-soon module carried a 128–512-unit stub scaffold; these were torn down (coming-soon
games are catalogue-only, no fake counts), except **Dash** which keeps its 16 real units. Mirrors the
Starfield re-scope precedent in [october-2026-launch-spec.md](october-2026-launch-spec.md).

## Still open

- **Pattern coverage lags.** `patterns/nintendo-nes/` holds only rung 0–1 entries; everything from
  metasprites up wants pattern entries written alongside each game. Flagged, not a blocker.
- Working titles throughout; `arena-assault` parked rather than deleted.

## Provenance

Applied from `docs/tracker/lineup-replan/nes-assembly.md` (the reviewed proposal) with the agreed
modifications (rung 4/5 split, APU earlier, MMC3-folded-not-a-second-game).
