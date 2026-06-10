# Lineup replan — Amiga · Blitz (PROPOSAL — not applied)

> **Status: proposal for review.** Not applied. On sign-off → written into
> `website/src/content/modules/commodore-amiga/blitz.yaml` + a decision-record
> amendment under `decisions/amiga-basic-amos-and-blitz.md`. Counts flexible;
> genres may recur across tracks; progressive + spiral. Follows the
> [`spectrum-assembly.md`](spectrum-assembly.md) template.
>
> **Blitz is a peer path to AMOS, not a rung above or below it.** This doc never
> ranks the two. Where Blitz and AMOS share a genre, each track climaxes on its
> *own* strengths — Blitz on compiled speed and reaching the hardware, AMOS on
> immediacy and its built-in toolkit. See
> `decisions/amiga-basic-amos-and-blitz.md` (drift triggers — avoid "rung",
> "middle rung", "graduate", "pulls ahead of AMOS").

## What Blitz *is* — the climax target

Blitz BASIC 2 is compiled to native 68k and reaches into the Amiga's chips. The
lessons it owns:

- **BitMaps, Slices, Shapes, Blit** — build a display, grab a shape, move pixels
  in bulk through the Blitter.
- **Double-buffering** (two BitMaps, `Show`/`Buffer`) — flicker-free redraw.
- **Compiled speed** — *many objects at once* that interpreted BASIC can't.
- **Hardware sprites** (`GetaSprite`/`ShowSprite`) — the chip overlay, not Bobs.
- **Copper** — colour registers and the display list by hand.
- **Smooth hardware scrolling** — scroll the BitMap, not redraw it.

The capability ladder below is a *Blitz-capability* ladder: one new
close-to-the-metal power per game. It is **not** a difficulty ranking against
AMOS or assembly.

## The Blitz capability ladder (the decomposed climb)

The primer (*Meet Blitz*, 15 units, shipped/LOCKED) already taught: Ted +
compile-run loop, Amiga/Blitz modes, Slices, Shapes, the Blitter, the frame
loop, double-buffering, joystick, collision, colour-register cycling, **hardware
sprites**, and smooth scrolling — a remarkably complete toolkit. So the games
**start high** and the ladder is about *applying* each power as a game's spine.

| Rung | Blitz capability foregrounded | Why it earns its own game |
|---|---|---|
| 0 | Shapes + Blit + double-buffer + many objects (primer endpoint) | Already taught — the floor |
| 1 | **Many objects at compiled speed** as the *whole point* | First game: a fast shooter that simply couldn't run interpreted |
| 2 | **Arrays + lists + structured data** | A data-driven game; Blitz as a *structured* language, not just fast |
| 3 | **Smooth hardware scrolling** as a game spine | A scroller that leans on BitMap scroll, not redraw |
| 4 | **Hardware sprites + Copper** combined for effect | Reach past the picture: chip sprites over a Copper-split background |
| 5 | **Blitter as mechanic** — bulk pixel ops drive the game | The Blitter *is* the gameplay (terrain, trails, fills) |
| 6 | **Everything at full speed** — dual-playfield / parallax + sprites | The climax: compiled speed feeding multi-layer hardware |

## Spiral spine — concept families across the lineup

(introduce · revisit-deeper · own)

| Family | Introduce | Revisit deeper | Own |
|---|---|---|---|
| **Many objects at speed** | #1 Flashpoint | #3 Tarmac (objects + scroll), #6 Skyfire (objects + layers) | #6 Skyfire |
| **Shapes / Blitter rendering** | primer → #1 | #5 Groundwork (Blitter mechanic) | #5 Groundwork |
| **Data structures (arrays/lists)** | #2 Gridlock | #4 Star Drift (sprite/Copper tables) | #6 (object pools) |
| **Scrolling** | #3 Tarmac (smooth) | #6 Skyfire (multi-layer/parallax) | #6 Skyfire |
| **Hardware sprites** | primer → #4 Star Drift | #6 (sprites over playfields) | #6 |
| **Copper** | primer (colour cycle) → #4 (split) | #6 (per-line playfield trickery) | #6 |
| **Collision** | primer → #1 | #3 (object vs track), #5 (against terrain) | #6 |

## Locked anchors

| # | Module | Status | Role |
|---|---|---|---|
| 0 | **Meet Blitz** | shipped · **locked** | 15-unit primer — Ted, modes, Slices/Shapes/Blit, double-buffer, joystick, collision, Copper colour, hardware sprites, scrolling |
| 1 | **Flashpoint** | coming-soon (stub) | Keep as rung 1 — fast shooter, "compiled speed is the point" |
| 2 | **Gridlock** | coming-soon (stub) | Keep as rung 2 — data-driven structured puzzle |
| 3 | **Tarmac** | coming-soon (stub) | Keep as rung 3 — top-down racer on smooth scroll |

The current catalogue has only **three** game stubs after the primer. This
proposal keeps all three in place and **extends** the ladder to a proper climax
(rungs 4–6) so the track has the same spiral depth as AMOS and assembly.

## Proposed lineup (gentle — max 2 new things per game)

| # | Game (working) | Genre | Amiga classic anchor | NEW headline (rung) | Revisits |
|---|---|---|---|---|---|
| 1 | **Flashpoint** | Fast arcade shooter | *SWIV* / *Battle Squadron* | **Rung 1: many objects at compiled speed** — frame loop, player, scoring | Shapes, Blit, double-buffer (primer) |
| 2 | **Gridlock** | Structured puzzle | *Bombuzal* / *Atomino* | **Rung 2: arrays + lists + structured program** — grid logic & state | frame loop, collision |
| 3 | **Tarmac** | Top-down racer | *Super Skidmarks* (Blitz-built!) | **Rung 3: smooth hardware scrolling** + fast object handling | many objects, collision |
| 4 | **Star Drift** | Horizontal shooter | *Project-X* / *Apidya* | **Rung 4: hardware sprites + Copper split** combined | scrolling, many objects, arrays |
| 5 | **Groundwork** | Terrain / dig puzzle | *Lemmings* (Blitter-as-tool) | **Rung 5: Blitter as the mechanic** — dig/build/fill drive play | Shapes, collision-against-terrain |
| 6 | **Skyfire** | Parallax shoot-'em-up (climax) | *Agony* / *Lionheart* (layered look) | **Rung 6: dual-playfield / parallax + sprites at full speed** | *everything* — the compiled-speed climax |
| 7 | **Overdrive** | Capstone racer/action | *Super Skidmarks* (scope) / original | integrate-and-polish: multi-layer, sprites, full game loop | *all rungs* — depth + finish, no new headline |

Notes:
- **#3 Tarmac → Super Skidmarks** is the anchor with the strongest provenance:
  the *Skidmarks* line was Blitz-built (decision record, verified). It makes the
  "scene shipped real games in Blitz" point concrete inside the lineup.
- **#5 Groundwork** is a *Lemmings*-style terrain puzzle — the same Blitter-as-
  mechanic conceit as the **assembly** track's *Exodus*, deliberately. Genre
  overlap across tracks is allowed; here Blitz reaches the Blitter through its
  own `Blit`/Shapes verbs rather than raw register pokes, which is the contrast.
- **#6 Skyfire** is the honest Blitz climax — multi-layer hardware feeding off
  compiled speed, the thing that would crawl under interpreted AMOS. This is
  where the track shows *why the scene reached for Blitz*, per the decision
  record's "Blitz climax" note — stated as Blitz's strength, never as a rank.

## Spiral check (sample families)

- **Many objects:** intro #1 → +scroll #3 → +layers #6.
- **Scrolling:** smooth #3 → parallax/dual-playfield #6.
- **Hardware sprites:** primer → over Copper split #4 → over playfields #6.
- **Blitter:** render #1 → mechanic #5 → bulk under load #6.

## Diff vs current catalogue

- **Kept:** Flashpoint (1), Gridlock (2), Tarmac (3) — unchanged slugs, now
  anchored to named classics (Tarmac → the Blitz-built *Skidmarks*).
- **Added:** **Star Drift** (#4, hardware sprites + Copper), **Groundwork** (#5,
  Blitter-as-mechanic), **Skyfire** (#6, parallax climax), **Overdrive** (#7,
  capstone). The current 3-stub list has no climax or capstone; these give the
  track a real spiral and a finish.
- **Re-framed:** the primer already ships hardware sprites + scrolling + Copper
  colour, so the games *apply* those rather than introduce them — the ladder is
  about foregrounding one power as a game's spine, keeping ≤2 new things/game.

## Settled

- **Blitz owns compiled speed + reaching the hardware.** Climax (Skyfire) is the
  multi-layer/parallax-at-speed effect AMOS can't reach.
- **Tarmac anchors to the Blitz-built Skidmarks** — provenance the decision
  record verified; makes the track's reason-for-being concrete.
- **Ladder = Blitz capabilities, not difficulty rank** vs AMOS/assembly.

## Still open (refine any time)

- **Groundwork** overlaps *Exodus* (assembly) on the Lemmings conceit by design
  — keep the deliberate cross-track echo, or pick a different Blitter-mechanic
  game (e.g. a *Worms*-style destructible-terrain artillery game, which has
  strong Blitz provenance) to avoid any "same game twice" read?
- A **Worms** anchor is available and exceptionally well-sourced (Worms was
  written in Blitz BASIC 2). Consider swapping Groundwork → a turn-based
  artillery game to name-drop Worms directly. Flagged for your call.
- Working titles throughout — swap freely.
