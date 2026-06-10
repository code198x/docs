# Lineup replan — Amiga · Assembly (PROPOSAL — not applied)

> **APPLIED 2026-06-10.** This proposal was applied to the catalogue and the per-track decision record under `decisions/`; the "not applied" status below is historical. Kept as the signed-off provenance record. Some game names predate the 2026-06-10 naming pass.

> **Status: proposal for review.** Not applied. On sign-off → written into
> `website/src/content/modules/commodore-amiga/assembly.yaml` + a decision
> record. Counts flexible; genres may recur across tracks; progressive + spiral.
> Follows the [`spectrum-assembly.md`](spectrum-assembly.md) template — a
> **hardware ladder** decomposing the hard custom-chip material one-new-thing-
> per-game, an explicit spiral spine, a sequenced lineup, a diff.
>
> Assembly is the **metal** path — a deeper, harder road than AMOS/Blitz, **not
> a reward for finishing them** and not "above" them in worth (decision record:
> "assembly is a deeper path, not a rung below Blitz"). This doc ranks
> *techniques* by hardware difficulty; it does not rank the *tracks*.

## The hardware ladder (the decomposed climb)

The Amiga's hard part is driving the custom chips — Agnus/Denise/Paula — by hand
to draw moving things cleanly. Instead of one flagship teaching all of it (the
current *Exodus* is a 128-unit monolith at 16/128), each rung is **one game's
headline**; every later game inherits the rungs below.

| Rung | Hardware technique | Why it's its own game |
|---|---|---|
| 0 | **Bitplanes** — a screen as planar memory | Primer endpoint — the foundation |
| 1 | **Blitter copy** — move a block of pixels via DMA | The first "the chip does the work" aha; one moving object |
| 2 | **Masked Blit (cookie-cut)** — clean object over a background | The single biggest pixel-rendering lesson; deserves its own game |
| 3 | **Copper effects** — split the screen, colour by scanline | Background mood/UI by display list; cheap, dramatic |
| 4 | **Hardware sprites** — the chip overlay, SPRxPOS/CTL by hand | "Free" moving objects independent of the playfield |
| 5 | **Paula sample audio** — DMA-driven sampled sound | Real Amiga sound: pointers, length, period, channels |
| 6 | **Smooth scrolling** — hardware scroll + bitplane modulo | Pixel scroll without redraw; the Amiga-defining effect |
| 7 | **Dual playfield** — two independent scrolling layers | Parallax in hardware; two playfields at once |
| 8 | **Depth / Y-sort + large Blitter objects** | Layered rendering; the hardest composition problem |

## Spiral spine — concept families across the lineup

(introduce · revisit-deeper · own)

| Family | Introduce | Revisit deeper | Own |
|---|---|---|---|
| **Blitter** | #1 Exodus (copy/clear) | #2 Signal (masked), #4 Ascent (cookie-cut sprites) | #11 Onslaught+ (bulk under load) |
| **Bitplanes** | primer → #1 | #6 (scroll modulo), #7 (dual playfield) | capstone |
| **Copper** | #2 Shatter Point (split/gradient) | #5 Crypt (transitions), #9 Highway (Copper road) | #9 |
| **Hardware sprites** | #3 Signal | #6 Gobble, #4 Ascent (enemies) | #10 Parallax (sprites + layers) |
| **Paula audio** | #2 Shatter Point (samples) | #7 Onslaught (MOD replay) | capstone (full MOD score) |
| **Scrolling** | #6 Wanderer (smooth) | #10 Parallax (dual playfield) | capstone |
| **State / world** | #5 Crypt (rooms) | #8 Fortress (iso world) | #12 Echoes (connected world) |
| **Depth / sort** | #8 Fortress (iso) | #11 Brawler (Y-sort) | capstone |

## Locked anchors

| # | Module | Status | Role |
|---|---|---|---|
| 0 | **Meet the Machine** | shipped · **locked** | 19-unit primer — 68000, registers, data sizes, bitplane screen, Copper, Blitter |
| 1 | **Exodus** | **in-progress (16/128)** | Treat as in-flight; **re-scope from 128-unit monolith to the rung-1/2 Blitter game** (see below) |

**Exodus — DECIDED-PENDING: re-scope (don't abandon).** Exodus is the partial
flagship. Its current frontmatter promises *128 units across 8 phases* —
the all-in-one model the ladder replaces. Proposal: **keep Exodus as the
Blitter game (rungs 1–2)** — the Lemmings-tradition terrain puzzle where "the
Blitter IS the gameplay" is exactly rung-1 copy + rung-2 masked-blit — and move
its later-phase material (Copper, Paula, sprites, scrolling) **out** into the
dedicated rung-games below. The 16 shipped units are preserved; the *scope* of
the module shrinks to one rung pair, matching one-new-thing-per-game. This
refines the implicit "Exodus teaches everything" framing into "Exodus is the
Blitter rung," recorded on apply.

## Proposed lineup (gentle — max 2 new things per game)

Each game adds **one hardware rung** (occasionally a rung + one secondary
family) and revisits the rest. Every game anchored to a real Amiga classic.

| # | Game (working) | Genre | Amiga classic anchor | NEW headline (rung) | Revisits |
|---|---|---|---|---|---|
| 1 | **Exodus** | Terrain puzzle | *Lemmings* | **Rungs 1–2: Blitter copy + masked blit** — the Blitter is the gameplay | bitplanes (primer) |
| 2 | **Shatter Point** | Bat-and-ball | *Batty* / *Arkanoid* | **Rung 3: Copper splits/gradients** + **Rung 5: Paula samples** (ball hits) | Blitter draw, masked blit |
| 3 | **Signal** | Lane-crosser | *Frogger* / *Skweek* | **Rung 4: hardware sprites** — chip overlay for the hazards | Blitter, Copper, Paula |
| 4 | **Ascent** | Single-screen platformer | *Rick Dangerous* / *Gods* | **Jump physics + Blitter cookie-cut** enemies | sprites, masked blit, Copper |
| 5 | **Crypt** | Flip-screen dungeon | *Cadaver* / *Dungeon Master* (mood) | **Room structures + Copper transitions + state** | sprites, Blitter, Paula |
| 6 | **Gobble** | Maze chase | *Pac-Man* / *Zool* | **Blitter tiles + ghost AI personalities** | sprites, state, Copper |
| 7 | **Wanderer** | Scrolling platformer | *Shadow of the Beast* | **Rung 6: smooth hardware scrolling** + camera dead zones | sprites, tiles, AI |
| 8 | **Onslaught** | Vertical shooter | *SWIV* / *Banshee* | **MOD replay (Paula, full)** + bullet patterns | scroll, sprites, Blitter, Paula |
| 9 | **Highway** | Pseudo-3D racer | *Lotus Esprit Turbo Challenge* | **Copper road rendering + sprite scaling** | Copper, sprites, scroll |
| 10 | **Parallax** | Horizontal shooter | *Project-X* / *Agony* | **Rung 7: dual playfield** — multi-layer parallax + boss | scroll, sprites, MOD, bullets |
| 11 | **Brawler** | Beat-'em-up | *Shadow Fighter* / *Pit-Fighter* | **Rung 8: Y-depth sorting + large Blitter objects** | sprites, scroll, AI |
| 12 | **Fortress** | Isometric adventure | *Cadaver* / *Knight Lore* lineage | **Isometric projection + depth sort** (composition) | depth, Blitter, state |
| 13 | **Echoes of the Ancients** | Metroidvania | *Turrican II* (connected world) | **Connected world + ability-gating + multi-disk** | scroll, sprites, state, audio |
| 14 | **Ascension: The Guru Meditation** | Capstone action-adventure | original | integrate-and-polish: custom disk loading, deep combat, full save | *all rungs* — depth + finish, no new headline |

## Pacing fixes applied (the 2-new-max rule)

The current catalogue dumps **four** skills per game (the YAML `skills:` arrays
list 4 each). Several would break the ≤2-new-things rule if all four were
genuinely *new*. The re-sequencing fixes this by making most of each game's four
skills **revisits**, with one (occasionally two) genuinely new:

- **Shatter Point (#2)** introduces Copper *and* Paula — exactly the 2-new
  ceiling; ball physics + Blitter fills are revisits. Acceptable at 2.
- **Signal** moved **after** Shatter Point so hardware sprites land as the *one*
  new thing (it previously listed Copper + sprites + Blitter + Paula as if all
  four were new — that's a 4-new game, split by re-sequencing).
- **Highway (#9)** keeps Copper-road + sprite-scaling as its pair (split-screen
  and championship modes become revisits/polish, not new rungs).
- Any game still implying 3+ new rungs on apply gets **split** — e.g. if
  *Echoes* tries to introduce connected-world *and* ability-gating *and*
  multi-disk as three firsts, multi-disk moves to a small interval module or to
  the capstone.

## Spiral check (sample families)

- **Blitter:** copy #1 → masked #2 → cookie-cut #4 → bulk #11.
- **Sprites:** intro #3 → enemies #4 → ghosts #6 → over layers #10.
- **Copper:** split #2 → transitions #5 → road #9.
- **Scrolling:** smooth #7 → dual-playfield #10 → capstone.
- **Audio:** samples #2 → MOD #8 → full score #14.

## Diff vs current catalogue

- **Exodus re-scoped** from a 128-unit, 8-phase, teaches-everything flagship to
  the **Blitter rung-pair game** (rungs 1–2). The 16 shipped units stay; the
  module's promised scope shrinks. This is the single biggest change and the
  one that brings the ladder into being.
- **Signal re-sequenced** after Shatter Point so hardware sprites are its lone
  new rung (was implicitly a 4-new game).
- **Order broadly preserved** otherwise — the existing 16-module list already
  roughly ascends in difficulty; the proposal re-anchors each to a named classic
  (Wanderer → *Shadow of the Beast*, Highway → *Lotus*, Echoes → *Turrican II*)
  and tags each game with its *one* new rung, demoting the other listed skills to
  explicit revisits.
- **No new games added** — assembly already has the breadth (16 modules);
  unlike AMOS/Blitz it needs *pacing discipline and anchoring*, not more games.

## Settled

- **Assembly owns the metal** — the climax is composition under hardware
  constraints (Y-sort, dual playfield, custom loaders), not "harder AMOS".
- **Exodus stays, re-scoped** — preserve shipped units, shrink scope to the
  Blitter rung.
- **Ladder ranks techniques, not tracks** — assembly is a deeper path, peer in
  worth to AMOS/Blitz.

## Still open (refine any time)

- **Exodus re-scope** is the load-bearing call — confirm shrinking its scope
  (vs. letting it remain the everything-flagship) is the intended direction.
  This contradicts Exodus's current 128-unit frontmatter, so it needs an
  explicit yes before apply.
- **Fortress vs Echoes ordering** — both are large late-game worlds; confirm iso
  (Fortress) before metroidvania (Echoes), or swap.
- Whether to insert a small **interval module** (academic depth — e.g. "How
  Copper DMA actually works") between rungs, per
  `decisions/between-game-intervals.md`. Flagged, not assumed.
- Working titles where not already shipped — Ascension/Echoes/etc. can change.
