# Lineup replan — Spectrum · Assembly (PROPOSAL v2)

> **Status: proposal for review.** Not applied. On sign-off → written into
> `website/src/content/modules/sinclair-zx-spectrum/assembly.yaml` + a decision
> record. Counts flexible; genres may recur across tracks; progressive + spiral.
> **v2 change (your steer):** the hard-rendering "Trunk" is *decomposed* into a
> **rendering ladder** — one hard technique per game, gentler — instead of dumped
> into one Greypeak. This refines [`spectrum-assembly-gentle-ramp.md`](../../decisions/spectrum-assembly-gentle-ramp.md)
> (Trunk → a sub-sequence, not a single game), to be recorded on apply.

## The rendering ladder (the decomposed Trunk)

The Spectrum's hard part is drawing moving things cleanly over a coloured
background. Instead of one game teaching all of it, each rung is **one game's
headline** — every later game inherits the rungs below it:

| Rung | Technique | Why it's its own game |
|---|---|---|
| 0 | **Attribute cells** (no pixel work) | Gloaming / Shadowkeep — the cell-based foundation |
| 1 | **Masked sprite** — one object drawn cleanly over a background | The single biggest "aha"; deserves a whole game with *one* moving sprite |
| 2 | **Pre-shifted sprite** — smooth, fast pixel motion | Speed without flicker; a focused mechanic |
| 3 | **Tile-map collision** — world geometry decoupled from attributes | Platforming needs it; a natural home |
| 4 | **Sprite multiplexing** — many masked sprites + flicker management | "Many things at once" at the pixel level |
| 5 | **Smooth scrolling** — pixel scroll + buffer | The Amiga-envy effect, done in software |
| 6 | **Y-sort / depth** — layered & isometric rendering | The hardest; **now** Greypeak, with everything below already learnt |

## Locked-ish anchors

| # | Module | Status | Role |
|---|---|---|---|
| 1 | **Meet the Machine** | shipped · locked | Z80 + screen-as-memory + control flow |
| 2 | **Gloaming** | shipped · locked | Cell-based complete game (rung 0) |
| 3 | **Shadowkeep** | shipped Arc 1 · **expand (B)** | Cell-based atmosphere/rooms → grows into the cell→masked bridge |

**Shadowkeep — DECIDED: B (expand).** A later Shadowkeep arc introduces the
**first masked sprite** (rung 1) — a creature that moves cleanly through the
rooms — so Shadowkeep *becomes* the cell→pixel bridge. Rung 1 is taught inside the
already-shipped flagship rather than a new game; **Lamplight (#4)** then *deepens*
masking rather than introducing it (one creature → a screen of hazards). This
keeps the ramp gentle and reuses the flagship.

## Proposed lineup (gentle, one-new-thing-per-game)

Each game adds **one rung or one new family**, and revisits the rest. Inspirations
are real Spectrum classics (the commercial-bar anchor).

| # | Game (working) | Genre | Inspiration | NEW headline | Revisits |
|---|---|---|---|---|---|
| 4 | **Lamplight** | Single-screen collect-and-dodge | Jetpac / Wanted: Monty Mole | **Rung 1: masked sprite** — one creature, clean over the room | cell graphics → pixel, one-threat AI (Gloaming) |
| 5 | **Ricochet** | Bat-and-ball | Arkanoid / Batty | **Rung 2: pre-shifted** smooth motion + bounding-box pixel collision | masking |
| 6 | **Deepdelve** | Single-screen platformer | Manic Miner | **Rung 3: tile-map collision** + jump physics, hazard timing | pre-shift, masking |
| 7 | **Nibble Run** | Maze chase | Pac-Man / Cookie | **chase / pathing AI**, power-up state | tile movement, masking, beeper |
| 8 | **Skyhawk** | Horizontal shooter | Uridium / Cobra | **Rung 4 + 5: multiplexing + smooth scroll**, formation AI | masking, sprite-vs-sprite collision |
| 9 | **Greypeak** | Isometric adventure | Knight Lore / Head Over Heels | **Rung 6: Y-sort / depth** | masking, tiles, rooms/state (Shadowkeep) — *only* Y-sort is new |
| 10 | **Starfall** | Vertical shooter (128K) | Xevious / Slap Fight | **128K AY** music + SFX, bullet patterns | multiplexing, scroll, AI |
| 11 | **Hard Rain** | Run-and-gun | Green Beret | **bosses / state-machine AI**, multi-dir scroll-action | scroll, multiplexing, AI |
| 12 | **Wyrmhold** | Arcade-adventure (large world) | Sabre Wulf / Atic Atac | **big world, inventory, save** | rooms/state, Y-sort, AI, mood |
| 13 | **Spectral Legacy** | Capstone | original | parallax, multiload, polish — integrates all | *everything* |

~10 games post-anchor (more than v1's 8 — your "introduce additional games" steer),
each introducing **one** hard thing. Greypeak moved from #4 → #9: by the time you
reach isometric Y-sort you've already met masking, pre-shift, tiles and
multiplexing, so it adds *one* concept, not six.

## Spiral check (sample families)

- **Masking:** intro #4 (one sprite) → many #8 (multiplexed) → layered #9 (Y-sort) → owned everywhere after.
- **Collision:** cell #2 → bounding-box #5 → tile #6 → sprite-vs-sprite #8 → depth-aware #9.
- **Scrolling:** — → smooth #8 → multi-directional #11 → parallax #13.
- **AI:** one threat #2 → chase #7 → formation #8 → bosses #11.

## Diff vs current catalogue

15 stubs → ~10 sequenced games. **Greypeak** demoted from the all-in-one Trunk game
to the Y-sort capstone of the ladder. New gentle rungs added (**Lamplight**,
**Ricochet**) that the old list lacked. Dropped/merged: `ink-war`, `stack`,
`slither`→Nibble Run, the redundant scroller pile (`blitz`/`expanse`/`redline`)→
Skyhawk + Hard Rain, `chambers`→Wyrmhold, `bastion`→Greypeak.

## Settled

- **Shadowkeep: B (expand)** — becomes the cell→masked bridge (rung 1).
- **Format locked** — this v2 (rendering ladder + one-new-thing-per-game + spiral
  spine) is the template the other seven tracks follow.

## Still open (refine any time)

- **Ladder pacing** — one rung per game, or fold two where a genre carries both (#8 already carries rungs 4+5)?
- Names are working titles — swap freely.
