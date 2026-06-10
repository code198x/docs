# Lineup replan — NES · Assembly (PROPOSAL — not applied)

> **APPLIED 2026-06-10.** This proposal was applied to the catalogue and the per-track decision record under `decisions/`; the "not applied" status below is historical. Kept as the signed-off provenance record. Some game names predate the 2026-06-10 naming pass.

> **Status: proposal for review.** Not applied. On sign-off → written into
> `website/src/content/modules/nintendo-entertainment-system/assembly.yaml`
> (+ per-game `units/*.yaml` re-scopes) and a decision record. Counts flexible;
> genres may recur across tracks; progressive + spiral — one new PPU/hardware
> rung per game, revisit the rest deeper.
>
> Follows the **Spectrum · Assembly** template
> ([`spectrum-assembly.md`](spectrum-assembly.md)): a decomposed hardware
> **ladder**, a **spiral spine**, a sequenced **lineup** anchored to real
> classics, locked anchors, a catalogue diff, settled/open. The Spectrum's hard
> part was *drawing moving things cleanly over a coloured background*; the NES's
> is **driving the PPU** — getting tiles, sprites, scroll, palettes, sound and
> (eventually) bigger ROMs out of a chip that gives you nothing for free and
> only lets you touch most of it during vblank.

## The PPU / 6502 hardware ladder (the decomposed hard part)

On the NES the difficulty is the **PPU and its timing**, not pixel-pushing into
a framebuffer (there isn't one you can poke freely). Each rung is **one game's
headline**; every later game inherits the rungs below it.

| Rung | Technique | Why it's its own game |
|---|---|---|
| 0 | **Nametable background tiles** — paint a static screen through the PPU during vblank | The foundation: CHR, nametables, the vblank-only write window. Taught in *Meet the Machine*, owned by the first game |
| 1 | **OAM sprites + controller-driven movement** — DMA a sprite, move it from the joypad inside the NMI loop | The first *game*: one object you control, NMI/vblank heartbeat as the game loop. The single biggest "aha" |
| 2 | **Sprite animation & metasprites** — multi-tile actors, frame cycling, facing | A character made of several tiles that animates; the unit of every later actor |
| 3 | **Attribute tables & palette swaps** — colour regions of the background, swap palettes for state/effects | The NES's odd 16×16 colour grid; needed before scrolling looks right |
| 4 | **PPU scrolling — single screen → two-screen** — the scroll registers, shifting one nametable's worth | First taste of a world bigger than the screen; the mirroring/seam problem appears |
| 5 | **Infinite scrolling — column/row feeding** — stream new tiles into the off-screen nametable as you scroll | "The world never ends"; the hard timing problem — updating the PPU mid-frame budget |
| 6 | **APU sound & music** — square/triangle/noise channels, a frame-driven music + SFX engine | Sound is its own subsystem with its own frame clock; deserves a dedicated home |
| 7 | **Mappers — bank switching (MMC1)** — break the 32KB PRG / 8KB CHR ceiling for bigger games | **First mapper.** The moment "more game than fits in the ROM" becomes the problem |
| 8 | **Advanced mappers — IRQ split + CHR banking (MMC3)** — scanline effects, status bars, big worlds | A second mapper for split-screen HUDs and Metroidvania-scale content |

Rungs 0–6 are the **plain-NROM ladder** — everything a learner needs to build a
complete, varied game with *no mapper*. **Rung 7 is the first hard wall a mapper
solves**, and it is flagged below at exactly the game that first needs it.

## Locked anchors

| # | Module | Status | Role |
|---|---|---|---|
| 0 | **Meet the Machine** | shipped · **locked** | 6502 + PPU window + palettes + CHR + test-and-branch + the NMI heartbeat + joypad (18 units). The on-ramp. Teaches **rung 0** statically. |
| 1 | **Dash** | stub-padded coming-soon · **re-scope to ~16 units** | The NES priority: the first *finishable* game. Owns **rung 1** (OAM sprite + controller + NMI game loop). |

*Meet the Machine* is the launch on-ramp (per
[`october-2026-launch-spec.md`](../../decisions/october-2026-launch-spec.md)) and
is untouched here. Its last units already introduce the NMI heartbeat and the
joypad as *literacy*; **Dash** is where they first become a *game loop* — so the
hand-off is gentle, not a cliff.

## Dash — DECIDED: re-scope (the key next step)

`dash.yaml` today is a **16-of-128** module: 16 real, well-named units
(`See Your Character` → `Integration + Polish`) padded with 112 `Unit NN`
stubs across eight invented "phases". The 16 real units already are a small,
finishable runner — controller-driven sprite, jump, one obstacle, a jump
sound, background tiles, collision, a collectible, score, lives, game-over,
title + restart, polish.

**Re-scope Dash to those ~16 units** — drop the 112 stubs and the eight-phase
scaffold, exactly as C64 *Starfield* was re-scoped from 128 to its real ~16
(per the 2026-06-03 launch amendment). Dash becomes the genuinely small first
game the NES on-ramp needs: **one new rung (OAM sprite + NMI game loop), nothing
else**. Its incidental `Jump Sound` / `Collect Sound` units use a single APU
channel as a *beep*, not the music engine — that stays rung 6.

## Proposed lineup (gentle, one-new-thing-per-game)

Each game adds **one rung or one new family** and revisits the rest. Inspirations
are real NES titles — simpler launch-era games early, the famous engines later.

| # | Game (working) | Genre | NES inspiration | NEW headline | Revisits |
|---|---|---|---|---|---|
| 1 | **Dash** | Single-screen runner | *Track & Field* / simple launch-era action | **Rung 1: OAM sprite + controller + NMI game loop** | nametable tiles, palettes (Meet the Machine) |
| 2 | **Crate Escape** | Single-screen platformer | *Donkey Kong* (1983 NES launch title) | **Rung 2: metasprite + sprite animation** + gravity/jump physics | OAM, controller, collision, tiles |
| 3 | **Fracture Point** | Bat-and-ball / breakout | *Arkanoid* (NES) | **Rung 3: attribute tables & palette swaps** — coloured brick field, ball-vs-tile collision | metasprites, physics, OAM |
| 4 | **Pellet Panic** | Maze chase | *Pac-Man* (NES) | **chase / pathing AI**, tile-grid movement, power-up state | attribute colour, animation, collision |
| 5 | **Fangs for the Memory** | Snake / grid arcade | *Nibbler*-style grid arcade | **data structures on 6502** — ring buffer, grid logic, growth | tile-grid movement, AI, score |
| 6 | **Pixel Plains** | Side-scrolling platformer | *Super Mario Bros.* | **Rung 4 → 5: PPU scrolling, single → infinite** (column feed) | metasprites, physics, attribute colour, AI |
| 7 | **Ion Trail** | Horizontal shooter | *Gradius* (NES) | **scrolling-shooter engine** — enemy patterns, terrain collision, power-ups | infinite scroll, multiplexed OAM, animation |
| 8 | **Crypt Crawler** | Flip-screen dungeon | *The Legend of Zelda* (screen-flip rooms) | **rooms + persistent state**, key/door, screen-flip transitions | scroll-as-flip, AI, attribute colour, collision |
| 9 | **Thunder Run** | Vertical shooter | *Xevious* / *1942* (NES) | **Rung 6: APU music + SFX engine** + vertical infinite scroll, formations | scrolling, patterns, OAM multiplexing |
| 10 | **Gridlock** | Falling-block puzzle | *Tetris* (NES) | **mapper-free big logic** — piece rotation tables, line-clear, lock timing + APU jingles | data structures (Fangs), APU (Thunder Run), attribute colour |
| 11 | **Iron Assault** | Run-and-gun | *Contra* (NES) | **Rung 7: MMC1 — bank switching** for bigger CHR/levels + bosses, two-player | infinite scroll, multiplex, AI, APU — *first mapper* |
| 12 | **Pavement Justice** | Beat-'em-up | *Double Dragon* (NES) | **Y-depth sorting** + melee/combo state machines, many enemies | MMC1 banking, metasprites, AI, APU |
| 13 | **Tarmac Terror** | Pseudo-3D racer | *Rad Racer* (NES) | **IRQ scanline tricks** — road perspective, split horizon, sprite scaling fakes | MMC1, APU, scroll |
| 14 | **Echoes of Eponium** | Metroidvania | *Metroid* (NES) | **Rung 8: MMC3 — IRQ split + CHR banking** — connected world, ability-gating, battery save | scrolling, rooms/state, banking, AI |
| 15 | **Requiem for a Mapper** | Capstone action-adventure | original | **integrate everything** — IRQ HUD, battery backup, professional polish, audio score | *all rungs* |

15 sequenced games post-on-ramp (down from 16 stub modules). **Mappers enter
late and deliberately:** rungs 0–6 carry the first *ten* games (1–10) entirely on
plain NROM, so a learner builds platformers, shooters, mazes, puzzles and a music
engine **before** ever touching a bank-switch. The first mapper (MMC1, rung 7)
appears only at **#11 Iron Assault**, where "more game than fits in 32KB" is the
real, felt problem — not a concept introduced cold.

## Spiral spine — concept families × introduce / revisit-deeper / own

| Family | Introduce | Revisit deeper | Own |
|---|---|---|---|
| **PPU background (nametables)** | MtM static screen → Dash #1 | attribute colour #3, scroll #6 | every game |
| **OAM sprites** | Dash #1 (one sprite) | metasprite #2, multiplex #6–#7, Y-sort #12 | everywhere after |
| **Animation** | metasprite #2 | enemy patterns #7, combo frames #12 | everywhere after |
| **Palettes / attributes** | MtM (palettes) → attribute tables #3 | per-region state #4, scroll-aware #6, CHR-bank palettes #11 | — |
| **Collision** | Dash #1 (bounds) | tile #2, ball-vs-tile #3, grid #4, terrain #7, depth-aware #12 | — |
| **Scrolling** | single-screen #6 | infinite #6, vertical #9, flip-as-scroll #8, IRQ-split #14 | — |
| **AI / game logic** | one obstacle #1 | chase #4, formations #7, bosses #11, combat FSM #12 | — |
| **Data structures** | ring buffer #5 | rotation tables #10, world graph #14 | — |
| **APU sound** | beep SFX #1 | music + SFX engine #6 (Thunder Run #9) | jingles #10, score #15 |
| **Mappers** | **MMC1 #11** (PRG/CHR banking) | **MMC3 #14** (IRQ + CHR banking) | capstone #15 |

Reading the spine top-to-bottom shows the gentle ramp: a family is *introduced*
once, then only *deepened*. By the time the hardest rungs arrive (infinite
scroll #6, MMC3 #14, IRQ racer #13) every supporting family is already owned, so
each adds **one** new idea, not six.

## Diff vs current catalogue

`assembly.yaml` today: Meet the Machine (complete) + 16 coming-soon game modules,
several stub-padded to 128 units. This proposal:

- **Dash** — re-scoped from 16-of-128 to a finishable ~16-unit first game; the
  112 stub units and 8-phase scaffold dropped. The 16 real units survive intact.
- **Sequence re-ordered around the ladder.** Old order front-loaded a Breakout
  (#3) and a Pac-Man (#4) before any scrolling, then scattered mappers. New order
  threads rungs 0→8 so mappers (MMC1/MMC3) land late, where the ROM ceiling bites.
- **Reslotted, not invented:** every game maps to an existing stub —
  `crate-escape`, `fracture-point`, `pellet-panic`, `fangs-for-the-memory`,
  `pixel-plains`, `ion-trail`, `crypt-crawler`, `thunder-run`, `gridlock`,
  `iron-assault`, `pavement-justice`, `tarmac-terror`, `echoes-of-eponium`,
  `requiem-for-a-mapper`. No new slugs; the headline technique per game is
  re-anchored to a ladder rung.
- **Dropped/merged:** `arena-assault` (multi-directional arena) — its multiplex +
  wave-AI material folds into Ion Trail #7 and Iron Assault #11; surfacing it as a
  distinct game duplicated the shooter rung without adding one. (Keep the slug
  parked; reintroduce only if a distinct arena rung emerges.)
- **Inspirations made explicit** per game (the commercial-bar anchor), simpler
  launch-era titles early (*Donkey Kong*, *Arkanoid*) → famous engines later
  (*SMB*, *Metroid*, *Contra*).

## Patterns gap (note, not a blocker)

`patterns/nintendo-nes/` holds only **6** entries (reset-sequence, nmi-game-loop,
controller-reading, palette-loading, multi-sprite-oam, sprite-movement-bounds) —
all rung 0–1, i.e. exactly what *Meet the Machine* + *Dash* need, and half the
Spectrum's 12. **Everything from rung 2 up has no pattern coverage:** metasprites,
attribute tables, scrolling (single/infinite), the APU engine, MMC1/MMC3 banking,
IRQ splits, Y-sort. Pattern authoring should track the lineup — each game's new
rung wants its pattern entry written alongside it. Not a blocker for this
proposal; flagged so it isn't discovered late.

## Settled

- **Dash re-scope** — to ~16 finishable units; the NES launch priority. Mirrors
  the C64 Starfield re-scope precedent.
- **Mappers late** — rungs 0–6 (games 1–10) are NROM-only; MMC1 first at #11,
  MMC3 at #14. A mapper is introduced only where its problem is felt.
- **Format** — matches the Spectrum template (ladder + one-new-thing-per-game +
  spiral spine), so the four core tracks stay structurally consistent.

## Still open (refine any time)

- **Rung 4+5 in one game (#6 Pixel Plains).** The Spectrum folded multiplex+scroll
  into one game (#8 Skyhawk); single→infinite scroll is a big jump — split into two
  games (a single-screen-shift platformer, then an infinite one) if #6 proves too steep?
- **APU placement.** Music engine sits at #9 (Thunder Run) so the early games carry
  only beeps. Pull it earlier (e.g. a dedicated small audio game after #5) if silence
  for eight games feels wrong.
- **Where MMC3 (#14) vs MMC1 (#11) split lands** — Metroidvania genuinely needs CHR
  banking + IRQ; confirm Iron Assault (#11) truly needs only MMC1, or promote it.
- **Names are working titles** (the existing slugs) — swap freely; `arena-assault`
  parked rather than deleted.
