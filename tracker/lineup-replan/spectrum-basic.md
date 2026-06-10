# Lineup replan — Spectrum · BASIC (PROPOSAL — not applied)

> **APPLIED 2026-06-10.** This proposal was applied to the catalogue and the per-track decision record under `decisions/`; the "not applied" status below is historical. Kept as the signed-off provenance record. Some game names predate the 2026-06-10 naming pass.
>
> **SUPERSEDED IN PART 2026-06-10 (fixed counts retired).** This doc repeatedly asserts the "32-game / 4-volume / ~8-per-volume frame preserved" — that frame was retired later the same day. Volumes are now uncounted named arcs sized by genre breadth + technique budget; slot numbers are dropped. See [`spectrum-basic-lineup.md`](../../decisions/spectrum-basic-lineup.md) and [`curriculum-structure.md`](../../decisions/curriculum-structure.md). Read the count/slot framing below as historical; the game lineup and progression notes still hold.

> **Status: proposal for review.** Not applied. On sign-off → written into
> `website/src/content/modules/sinclair-zx-spectrum/basic.yaml` (re-sequence the
> coming-soon stubs; the 17 shipped modules are untouched) + a decision-record
> amendment to [`spectrum-basic-lineup.md`](../../decisions/spectrum-basic-lineup.md).
> Counts flexible; genres may recur across tracks; progressive + spiral; each game
> anchored to a real Spectrum classic; prefer more small games over fewer overwhelming ones.
>
> **Sibling format:** matches [`spectrum-assembly.md`](spectrum-assembly.md), with the
> steer that **for BASIC the "ladder" is a CONCEPT ladder** (programming concepts,
> one-new-thing-per-game) — not a rendering ladder. BASIC's hard part is not drawing
> cleanly; it is **building a world that runs, reasons, and persists in interpreted code**.

## The concept ladder (the spine of the track)

BASIC's hard material is *program structure under growing state*. Each rung is one
game's headline concept; every later game inherits the rungs below it. The **lower
rungs are already shipped** (Volumes 1–2) — this replan extends the ladder from where
the shipped flagship volumes leave off.

| Rung | Concept | Status | Home (first taught) |
|---|---|---|---|
| 0 | **Output** — PRINT / CLS / a screen you control | shipped | Story Builder |
| 1 | **Variables + input** — LET / INPUT / strings | shipped | Story Builder → Lucky Number |
| 2 | **Decisions** — IF/THEN, RND, chained selection | shipped | Oracle Stone |
| 3 | **Loops + timing** — FOR/NEXT, INKEY$, PAUSE, the turn loop | shipped | Reflex / Bright Spark |
| 4 | **Subroutines + accumulation** — GO SUB, tallies, a live dashboard | shipped | Dice Roller / Hi-Lo |
| 5 | **The real-time game loop** — continuous loop, erase-and-redraw, physics | shipped | Touchdown |
| 6 | **Data-driven design** — DATA/READ/RESTORE, content vs logic | shipped | Cipher / Quiz Master |
| 7 | **1D + 2D arrays as state** — DIM, indexed storage, parallel arrays | shipped | Quiz Master → Sonar |
| 8 | **The array as a writable world** — 2D grid you mutate, real-time INKEY$ | shipped | Crates |
| 9 | **The world that won't wait** — frame-paced continuous motion, self-collision, game states | **NEW** | Tail Chase |
| 10 | **Feel through physics** — bounce, angle-of-deflection, pixel collision (POINT) | **NEW** | Volley → Brick Bash |
| 11 | **Motion under maths** — SIN/COS/PI, inertia, vectors | **NEW** | Drift |
| 12 | **Reading the screen back** — ATTR/SCREEN$/POINT as sensors, hazard timing | **NEW** | Quickstep |
| 13 | **Opponents that pursue** — chase AI, state reversal | **NEW** | The Hungry Maze |
| 14 | **Many things at once** — multi-entity arrays, OVER 1, DATA-driven waves | **NEW** | Night Patrol |
| 15 | **Speed + custom characters** — UDGs, BIN, difficulty curves, optimisation | **NEW** | Blockstorm |
| 16 | **Authored worlds** — animation frames, tile design, multi-screen state | **NEW** | Rooftops / Stonefall arc |
| 17 | **Generated worlds** — DEF FN, procedural layout, persistence (SAVE/LOAD) | **NEW** | Dungeons of Dorin arc |
| 18 | **Systems + language** — parsing, dispatch tables, living-world flags | **NEW** | Thornwood Manor arc |

Rungs 0–8 are the shipped Volumes 1–2 and are **locked**. The replan is rungs 9–18:
Volume 3 (Worlds and Rules) and Volume 4 (Stories and Systems), today's coming-soon
stubs, sequenced so each game introduces exactly one new rung.

## Spiral spine (concept families × introduce / revisit-deeper / own)

The shipped volumes already model the spiral; these families thread through the new games:

| Family | Introduce | Revisit deeper | Own |
|---|---|---|---|
| **State (arrays as world)** | Sonar / Crates (2D grid) | Tail Chase (live array), Night Patrol (many entities) | Dorin (generated + saved) |
| **Real-time loop / timing** | Touchdown | Tail Chase (frame-paced), Quickstep (hazard timing) | Blockstorm (speed-tuned) |
| **Collision** | Crates (cell lookahead) | Tail Chase (self/wall), Brick Bash (pixel/POINT) | Night Patrol (multi-target) |
| **Physics / maths** | Touchdown (gravity) | Brick Bash (deflection angle) | Drift (SIN/COS inertia) |
| **Opponents / AI** | Three in a Row (rule priority) | The Hungry Maze (chase + reversal) | Thornwood (living-world reactions) |
| **Data-driven content** | Cipher / Quiz Master (DATA) | Night Patrol (DATA waves), Stonefall (DATA levels) | Dorin (procedural generation) |
| **Graphics / characters** | Touchdown (PLOT/DRAW) | Brick Bash (CHR$ blocks), Blockstorm (UDGs) | Rooftops/Stonefall (animation, tiles) |
| **Persistence / systems** | — | Dorin (SAVE/LOAD) | Thornwood (parser, world-state) |

Every new game **introduces one** family-rung and **revisits** at least two earlier ones
at greater depth — the one-new-thing-per-game discipline the assembly ladder uses.

## Locked anchors (17 shipped modules — do not churn)

| # | Module | Volume | Role |
|---|---|---|---|
| 0 | **Meet BASIC** | Primer | The editor, PRINT/LET/INPUT, IF/FOR/GO SUB, screen+colour+sound+motion |
| 1–8 | **Story Builder → Touchdown** | V1 First Programs | Output → variables → decisions → loops → real-time loop (rungs 0–5) |
| 9–16 | **Cipher → Crates** | V2 Patterns of State | Data-driven design, 1D/2D arrays, the array as a writable world (rungs 6–8) |

The spine is built **on** these. The replan reorders and re-headlines only the
coming-soon stubs (slots 17–32); no shipped slug, order, or skill set changes.

## Proposed lineup (gentle, one-new-thing-per-game)

Each game adds **one rung** and revisits earlier families deeper. Inspirations are real
Spectrum classics / Usborne type-in lineage (the commercial-bar + type-in anchor).
Volume names and the 4-volume / ~8-per-volume frame from
[`spectrum-basic-lineup.md`](../../decisions/spectrum-basic-lineup.md) are preserved.

### Volume 3 — Worlds and Rules (slots 17–24) — the pivot to real-time

| # | Game | Genre | Inspiration (Spectrum/type-in) | NEW headline (rung) | Revisits |
|---|---|---|---|---|---|
| 17 | **Tail Chase** | Snake | *Nibbler* / Snake type-ins | **Rung 9: the world that won't wait** — frame-paced (PEEK 23672) continuous motion, circular-array body, self-collision, game states | real-time loop (Touchdown), arrays (Sonar), collision (Crates) |
| 18 | **Volley** | Bat-and-ball (1 paddle) | *Pong* type-ins | **paddle physics** — reflection, the rally as a feedback loop (gentle on-ramp to Brick Bash) | continuous motion, INKEY$ steering, ABS |
| 19 | **Brick Bash** | Breakout | *Krakout* (Gremlin) / Arkanoid | **Rung 10: feel through physics** — CHR$ block bricks, CIRCLE/POINT pixel collision, bat-angle deflection | paddle physics (Volley), real-time loop |
| 20 | **Drift** | Asteroids-style | *Asteroids* / *Meteor Storm* | **Rung 11: motion under maths** — SIN/COS/PI, inertia, wrap-around vectors | physics (Brick Bash), arrays, real-time loop |
| 21 | **Quickstep** | Frogger-style crossing | *Frogger* / *Frostbite* type-ins | **Rung 12: reading the screen back** — ATTR/POINT as sensors, lane timing, hazard patterns | continuous motion, collision, data-driven lanes |
| 22 | **The Hungry Maze** | Maze chase | *Pac-Man* / *Cookie* (Ultimate) | **Rung 13: opponents that pursue** — chase AI, power-pill state reversal | 2D world (Crates), rule-priority AI (Three in a Row), timing |
| 23 | **Night Patrol** | Multi-target defence | *Missile Command* / *Penetrator* | **Rung 14: many things at once** — multi-entity arrays, OVER 1 XOR draw, DATA-driven waves | arrays-as-world, collision (now multi-target), data-driven |
| 24 | **Blockstorm** | Wave/falling-block action | *Tetris* type-ins / wave shooters | **Rung 15: speed + custom characters** — UDGs (USR/BIN), difficulty escalation, BASIC speed optimisation | many-entity loop, real-time pacing, graphics |

### Volume 4 — Stories and Systems (slots 25–32) — tour-then-deepen, in pairs

V4 keeps the **2-deep tour-then-deepen** ordering and the Pt 1 / Pt 2 splits required by
the 32-game decision: introduce two storytelling forms (Rooftops, Stonefall), deepen both;
introduce two more (Dorin, Thornwood), deepen both.

| # | Game | Genre | Inspiration | NEW headline (rung) | Revisits |
|---|---|---|---|---|---|
| 25 | **Rooftops** (Pt 1) | Platformer | *Manic Miner* / *Jet Set Willy* | **Rung 16a: authored worlds** — hand-designed UDG sprites, animation frames, jump physics, platform collision | UDGs (Blockstorm), physics, real-time loop |
| 26 | **Stonefall** (Pt 1) | Boulder Dash-style | *Boulder Dash* / *Gilligan's Gold* | **Rung 16b: tile worlds** — custom character set, falling-rock cellular physics, tile design | 2D world (Crates), data-driven layouts, collision |
| 27 | **Skyhold** (Rooftops Pt 2) | Multi-screen platformer | *Jet Set Willy* exploration | **multi-screen state** — room connections, persistent across-screen position (deepens Rooftops) | authored sprites, platform collision, state |
| 28 | **Deepworks** (Stonefall Pt 2) | Level-design Boulder Dash | *Boulder Dash* level packs | **designed worlds (level design)** — readable affordances, DATA-string level packs (deepens Stonefall) | tile physics, data-driven levels |
| 29 | **Dungeons of Dorin** (Pt 1) | Roguelike explorer | *Sword of Fargoal* / type-in dungeons | **Rung 17: generated worlds** — DEF FN, procedural layout, RND-seeded maps | arrays-as-world, data-driven, navigation (The Caverns) |
| 30 | **Thornwood Manor** (Pt 1) | Text/parser adventure | *The Hobbit* / *Twin Kingdom Valley* | **Rung 18: systems + language** — two-word parser, dispatch tables, SAVE/LOAD/VERIFY | strings/slicing (Cipher), data-driven content |
| 31 | **Dungeons of Dorin II** (Pt 2) | Roguelike RPG | *Fargoal* combat/items | **systems design** — combat, items, persistence (deepens Dorin) | generated worlds, SAVE/LOAD, arrays |
| 32 | **Thornwood Manor II** (Pt 2) | Living-world adventure | *The Hobbit*'s reactive NPCs | **living worlds** — world-state flags, reactive NPCs, narrative ecology (deepens Thornwood) | parser, opponents/reactions, persistence |

~16 games post-V2, each introducing one rung, gentle pacing maintained by the V3 pairing
(Volley→Brick Bash) and V4's Pt 1/Pt 2 deepen splits.

## Spiral check (sample families)

- **Collision:** cell-lookahead #16 (Crates) → self/wall #17 → pixel/POINT #19 → multi-target #23 → tile #26.
- **Real-time timing:** game loop #8 (Touchdown) → frame-paced #17 → hazard timing #21 → speed-tuned #24.
- **Physics / maths:** gravity #8 → deflection angle #19 → SIN/COS inertia #20.
- **Opponents:** rule-priority #13 (Three in a Row) → chase + reversal #22 → reactive NPCs #32.
- **Data-driven:** DATA lists #9 (Cipher) → DATA waves #23 → DATA level packs #28 → procedural #29.
- **Persistence:** none → SAVE/LOAD #29 → world-state systems #30/#32.

## Diff vs the current catalogue

The catalogue (`basic.yaml`) already lists slots 17–32 as coming-soon stubs with thin
skill lists. This replan **keeps the same 16 games, slugs, volume assignments, and the
32-game / 4-volume frame** — it does not add, drop, or re-genre any game. What changes:

- **Headlines made explicit and laddered.** Each stub gains a single NEW-rung headline
  drawn from the ladder, where today several stubs carry only a one-or-two-line skill
  list (e.g. Volley: "Paddle physics"; Drift: "SIN/COS/PI, Inertia").
- **Spiral made explicit.** Each game's "revisits" are named, so the one-new-thing
  discipline is visible and enforceable per game (today implicit in the prose spec only).
- **Volley positioned as a gentle on-ramp to Brick Bash** (paddle physics first, then
  pixel-collision + deflection), keeping V3's hardest early jump gentle — consistent with
  "more small games over fewer overwhelming ones."
- **Skill lists in the YAML stubs to be enriched** on apply to match the headline + the
  named revisits (mechanical, no structural change).

No churn to the 17 shipped modules. No new games. No genre changes. This is a
**re-headline + spiral-annotation** of the existing coming-soon stubs, not a re-lineup.

## Settled

- **17 shipped modules locked** — Primer + V1 + V2 untouched (rungs 0–8).
- **32-game / 4-volume / ~8-per-volume frame preserved** — per
  [`spectrum-basic-lineup.md`](../../decisions/spectrum-basic-lineup.md); no cut, no add.
- **V4 Pt 1/Pt 2 splits preserved** — merging them is a drift trigger in the 32-game record.
- **Concept ladder, not rendering ladder** — BASIC's spine is program structure under
  growing state; pixel-rendering rungs belong to the assembly track.

## Still open (refine any time)

- **Volley as a standalone game vs a Brick Bash arc.** Volley (Pong) and Brick Bash share
  paddle/ball mechanics; the 32-game frame lists them as two games. Keep separate (current
  proposal, gentler ramp) — or is Volley better as a Brick Bash "Pt 0" revisit? Flag for
  the user; default is keep-separate (no churn to the catalogue count).
- **Drift's trig vs Brick Bash's trig.** The prose spec puts the full SIN/COS/TAN/PI intro
  at Brick Bash; the 32-game decision moved trig to Asteroids (Drift, slot 20) and cut
  TAN/ASN/ACS. **Proposal follows the decision:** Drift owns the trig headline (rung 11);
  Brick Bash uses only POINT + simple deflection. Confirm this is the intended split — the
  older `basic.md` prose still shows the full trig family at Brick Bash and needs aligning.
- **UDG placement.** 32-game decision pins UDGs at Blockstorm (slot 24); the proposal
  honours that (rung 15). Rooftops then *uses* UDGs for sprites rather than introducing them.
- Working titles for the Pt 2 games (Skyhold, Deepworks) match the catalogue; swap freely.
