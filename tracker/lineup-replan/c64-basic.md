# Lineup replan — Commodore 64 · BASIC (PROPOSAL)

> **APPLIED 2026-06-10.** This proposal was applied to the catalogue and the per-track decision record under `decisions/`; the "not applied" status below is historical. Kept as the signed-off provenance record. Some game names predate the 2026-06-10 naming pass.

> **Status: PROPOSAL — not applied.** Not written into any catalogue. On sign-off →
> sequenced into `website/src/content/modules/commodore-64/basic.yaml` (Volume 2+ as
> `coming-soon` modules) plus a decision record. Counts FLEXIBLE; genres may recur
> across volumes; progressive + spiral (one new concept per game, revisit deeper);
> each game anchored to a real C64 classic; gentle pacing — more small games over
> fewer overwhelming ones.
>
> **What this plan does:** Volume 1 ("First Programs": `meet-c64-basic` + 8 games) is
> **shipped and complete** — locked. C64 BASIC has **no coming-soon modules catalogued
> beyond those 9**, so this plan proposes the Volume 2+ lineup essentially fresh,
> grounded in the C64 twist: **Commodore BASIC v2 is bare-bones, so the machine's
> hardware (VIC-II screen/colour/sprites/raster, SID) is reached by POKE/PEEK.** That
> POKE-the-hardware thread is sequenced here as a first-class spine alongside the
> language-concept ladder.

## The C64 twist — two ladders climbed together

Spectrum BASIC and C64 BASIC teach the **same programming-concept ladder** (output →
variables → decisions → loops → arrays → state → real-time → data). What makes the C64
track *its own thing* is that **CBM BASIC v2 gives you almost nothing for the hardware.**
There is no `SPRITE`, no `SOUND`, no `PLOT`, no `SCREEN`. Everything the C64 is famous
for — its 16 colours, hardware sprites, raster effects, the SID — is reached by writing
numbers into memory with **POKE** and reading them back with **PEEK**.

So the track climbs **two ladders at once**:

- a **concept ladder** (the portable programming ideas), and
- a **POKE-the-hardware ladder** (turning the bare language into a games machine).

Volume 1 already started both — `POKE` to screen memory (Skyline), the jiffy clock and
`POKE 53281` (Reflex), SID registers as a voice (Bleeper), joystick by `PEEK 56320`
(Rover). Volume 2+ deepens each rung deliberately, one new memory-mapped capability per
game.

### The concept ladder (portable programming ideas)

| Rung | Concept | Where introduced |
|---|---|---|
| 0 | **Output** — PRINT, the screen as a surface | `meet-c64-basic` / Skyline (shipped) |
| 1 | **Variables + input** — LET, INPUT, RND | Oracle (shipped) |
| 2 | **Decisions** — IF/THEN, comparison | Oracle / Safe Cracker (shipped) |
| 3 | **Loops** — FOR/NEXT, the loop-with-a-goal | Tally / Safe Cracker (shipped) |
| 4 | **Arrays** — numeric arrays as counters/sequences | Tally / Bleeper (shipped) |
| 5 | **Real-time loop** — the continuous game loop, live input | Rover / Dropzone (shipped) |
| 6 | **Simulation state** — velocity/gravity as accumulating numbers | Dropzone (shipped) |
| 7 | **2D arrays** — a grid held in memory (board / map) | **Vol 2** (new) |
| 8 | **String handling** — LEFT$/MID$/RIGHT$/LEN, parsing words | **Vol 2** (new) |
| 9 | **State machines** — game states, turn structure, menus | **Vol 2–3** (new) |
| 10 | **READ/DATA** — table-driven design, level/lookup data | **Vol 2–3** (new) |
| 11 | **Maths for motion** — INT/ABS/SGN, then SIN/COS for vectors | **Vol 3** (new) |
| 12 | **Persistence** — files/strings to disk (OPEN/PRINT#/INPUT#) | **Vol 4** (new) |

### The POKE-the-hardware ladder (the distinctive C64 spine)

| Rung | Hardware reached by POKE/PEEK | Register(s) | Where |
|---|---|---|---|
| H0 | **Screen + colour RAM** — characters, the separate colour map | `$0400` / `$D800` | shipped (Skyline) |
| H1 | **Border + background, screen flash** | `53280`/`53281` (`$D020`/`$D021`) | shipped (Reflex) |
| H2 | **SID as a voice** — freq/waveform/ADSR, one note | `$D400…` | shipped (Bleeper) |
| H3 | **Joystick + the loop** — read the port, move a thing | `56320`/`56321` | shipped (Rover) |
| H4 | **Custom characters** — copy the ROM charset to RAM, redefine glyphs | `53272` (`$D018`) + char RAM | **Vol 2** |
| H5 | **Hardware sprites** — enable, position, shape pointer, colour | `$D000…$D02E` | **Vol 2** (the headline rung) |
| H6 | **Sprite collision + multicolour** — hardware collision registers | `$D01E`/`$D01F`, `$D01C` | **Vol 2–3** |
| H7 | **SID, full** — three voices, filter, music + SFX together | `$D400…$D418` | **Vol 3** |
| H8 | **Raster reads** — read the raster line for timing/flicker-free updates | `$D012` | **Vol 3** |
| H9 | **Scrolling** — smooth (fine) scroll register + coarse scroll | `$D016`/`$D011` | **Vol 4** |

The whole track's identity is that **every famous C64 effect is a memory poke you can
read about in a magazine and type in.** Sequencing it as its own ladder keeps the
"one new poke per game" promise honest: hardware sprites (H5) is the single biggest
"now it's a real C64 game" moment and earns its own headline game.

## Locked anchors (shipped — do not reorder)

| # | Module | Kind | Status | Role |
|---|---|---|---|---|
| 0 | **Meet C64 BASIC** | teaching | shipped · locked | Type/run/edit/debug; first taste of POKE/PEEK for screen, colour, sound, joystick |
| 1 | **Skyline** | game | shipped · locked | POKE to screen memory + colour RAM, screen codes (concept rung 0 / H0) |
| 2 | **Oracle** | game | shipped · locked | RND, INPUT, IF/THEN (rungs 1–2) |
| 3 | **Reflex** | game | shipped · locked | Jiffy clock (TI), GET, screen flash POKE 53281 (rung 5 seed / H1) |
| 4 | **Tally** | game | shipped · locked | Numeric arrays as counters, index, POKEd bar chart (rung 4) |
| 5 | **Bleeper** | game | shipped · locked | SID registers as a voice, array sequence, GET echo (rung 4 / H2) |
| 6 | **Safe Cracker** | game | shipped · locked | Loop-with-a-goal, higher/lower deduction, guess limit (rungs 2–3) |
| 7 | **Rover** | game | shipped · locked | Joystick PEEK 56320, continuous loop, look-ahead collision (rung 5 / H3) |
| 8 | **Dropzone** | game | shipped · locked | Velocity/gravity/thrust, physics loop, win/lose/fuel (rung 6) |

Volume 1 already covers concept rungs 0–6 and hardware rungs H0–H3. Volume 2 onward picks
up at concept rung 7 and hardware rung H4 — the new material is **2D grids, strings, state
machines, custom characters, and hardware sprites**.

## Proposed lineup (gentle, one-new-thing-per-game)

Each game adds **one concept rung or one POKE-hardware rung** and revisits the rest.
Inspirations are real C64 classics (the commercial-bar anchor). Counts are illustrative,
not targets — volumes group ~8 games to mirror the shipped Volume 1 and the Spectrum BASIC
lattice, but the budget is on *one new thing per game*, not a count.

### Volume 2 — Boards and Sprites (grids, strings, the first real sprites)

| # | Game (working) | Genre | C64 inspiration | NEW headline | Revisits |
|---|---|---|---|---|---|
| 9 | **Gridlock** | Turn-based puzzle | Boulder Dash (grid feel) / Tic-Tac-Toe | **Concept rung 7: 2D arrays** — a board held in a grid, row/col indexing | screen POKE, IF/THEN, loops |
| 10 | **Codebreaker** | Word / deduction | Hangman / Mastermind | **Concept rung 8: string handling** — LEFT$/MID$/LEN, compare letters | 2D arrays (the guess grid), INPUT |
| 11 | **Glyph** | Maze (single screen) | — (interlude: the workshop game) | **Hardware rung H4: custom characters** — copy charset to RAM, redefine a maze tileset | screen + colour RAM, grids |
| 12 | **Skater** | Single-screen action | Frogger | **Hardware rung H5: hardware sprites** — enable, position, shape pointer (the headline) | custom chars (background), joystick loop |
| 13 | **Nibbler** | Maze chase | Pac-Man / snake | **Concept rung 9: state machines** — chase/flee states, a turn-by-turn grid mover | sprites, 2D map, joystick |
| 14 | **Bouncer** | Bat-and-ball | Krakout / Arkanoid | **Hardware rung H6: sprite collision** — read the collision registers, brick grid | sprites, 2D arrays, physics-lite |
| 15 | **Treasure Map** | Tile adventure (rooms) | Jet Set Willy feel / Atic Atac | **Concept rung 10: READ/DATA** — rooms and items as table data | custom chars, sprites, state |
| 16 | **Quizmaster** | Quiz / game-show | period type-in quiz games | **Menus + multi-state flow** (deepens rung 9) | strings, READ/DATA (question bank), arrays |

### Volume 3 — Worlds and Sound (motion maths, full SID, raster)

| # | Game (working) | Genre | C64 inspiration | NEW headline | Revisits |
|---|---|---|---|---|---|
| 17 | **Vectors** | Asteroids-style | Asteroids / Sentinel | **Concept rung 11: SIN/COS for motion** — angle → dx/dy, thrust in a direction | sprites, real-time loop, collision |
| 18 | **Cascade** | Falling-block puzzle | Tetris / Boulder Dash | **Gravity over a grid** (deepens 2D arrays + state) | 2D arrays, custom chars, state machine |
| 19 | **Soundsmith** | Music/rhythm toy → game | period SID music type-ins | **Hardware rung H7: full SID** — three voices, ADSR, filter; music + SFX | SID-as-voice (Bleeper), arrays, READ/DATA |
| 20 | **Raster** | Shooter (vertical) | Uridium / Zynaps | **Hardware rung H8: raster reads** — D012 for flicker-free, timed updates | sprites, collision, motion maths |
| 21 | **Defender Lite** | Horizontal action | Defender / Hover Bovver | **Many sprites + a scrolling readout** (deepens sprites/state) | sprites, collision, SID, state |
| 22 | **Dungeon** | Top-down adventure | Gauntlet feel / The Sword of Fargoal | **Procedural data + inventory** (deepens READ/DATA) | rooms/state, sprites, strings |
| 23 | **Trackside** | Racer (top-down) | Pitstop / Spy Hunter | **Pseudo-3D / scrolling track via chars** | motion maths, custom chars, collision |
| 24 | **Showtime** | Mini-game collection | Track & Field / Daley Thompson | **A multi-event collection** — several tiny mechanics in one module | everything light: sprites, SID, input, timing |

### Volume 4 — Systems and Saves (persistence, scrolling, the capstone)

| # | Game (working) | Genre | C64 inspiration | NEW headline | Revisits |
|---|---|---|---|---|---|
| 25 | **Smooth** | Scrolling platformer Pt 1 | Great Giana Sisters / Wonder Boy | **Hardware rung H9: smooth scrolling** — D016 fine scroll + coarse char shift | sprites, custom chars, collision |
| 26 | **Smooth** Pt 2 | (same game, deepened) | — | **Multi-screen world via scroll + map data** | scrolling, READ/DATA, state |
| 27 | **Vault** | Adventure with save Pt 1 | Below the Root / The Hobbit | **Concept rung 12: persistence** — OPEN/PRINT#/INPUT#, save/load to disk | rooms/state, strings, inventory |
| 28 | **Vault** Pt 2 | (same game, deepened) | — | **Save the whole game state** (deepens persistence) | persistence, state machine |
| 29 | **Arena** | Beat-'em-up / brawler | The Way of the Exploding Fist / IK+ | **Two-sprite combat + sprite animation frames** | sprites, collision, state, joystick |
| 30 | **Conductor** | Audio-driven game | period demoscene SID feel | **SID-synced gameplay** (deepens full SID + raster timing) | SID, raster, state |
| 31 | **Builder** | Construction / sim | Little Computer People / sim-lite | **Save-backed sandbox** (integrates persistence + grids) | persistence, grids, READ/DATA |
| 32 | **Showpiece** | Capstone | original | **Integrates everything** — sprites, scroll, SID, save, polish | *everything* |

~24 games post-anchor across three volumes, each introducing **one** new concept or one
new hardware poke. Hardware sprites (H5, **Skater #12**) is moved as early as the language
allows — by then the learner has grids and the joystick loop, so sprites add *one* thing
(memory-mapped sprite registers), not six. Smooth scrolling (H9) is deliberately last on
the hardware ladder: it is the C64's Amiga-envy effect and sits in Volume 4 where every
sprite/char/collision rung below it is already owned.

## Spiral check (sample families)

- **2D grids / arrays:** intro #9 (board) → map #13 → falling-block #18 → save-backed grid #31.
- **Strings:** intro #10 (compare letters) → question bank #16 → inventory/parse #22 → save text #27.
- **Sprites (H5):** intro #12 (one sprite) → collision #14 → many #20/#21 → animation frames #29.
- **SID:** one voice #5 (shipped) → full three-voice #19 → SID-synced gameplay #30.
- **State machines:** intro #13 (chase/flee) → menus #16 → gravity+state #18 → save state #28.
- **Motion maths:** seeded by Dropzone's velocity (shipped) → SIN/COS vectors #17 → pseudo-3D #23.
- **Persistence:** intro #27 → full state #28 → sandbox #31 → capstone #32.

## Diff vs current catalogue

`basic.yaml` currently holds **9 modules, all `status: complete`** (`meet-c64-basic` +
Skyline…Dropzone) and **no coming-soon entries**. This proposal adds **24 new
`coming-soon` game modules** in three volumes (`phase:` "Boards and Sprites" / "Worlds and
Sound" / "Systems and Saves"), continuing the array after Dropzone. Nothing shipped is
reordered, renamed, or dropped — Volume 1 is untouched. No `game-NN-` slugs (order is
catalogue position per `modules-not-games.md`). On apply, only catalogue rows are added;
slugs are working titles and can be swapped freely before they ship.

## Settled

- **Volume 1 locked.** The 9 shipped modules are anchors; this plan only appends.
- **Two-ladder framing.** The POKE-the-hardware ladder is sequenced as a first-class spine
  alongside the portable concept ladder — this is the C64 BASIC track's distinctive shape
  and the thing that differentiates it from Spectrum BASIC.
- **Format matches the family.** ~8 games/volume mirrors shipped Volume 1 and the Spectrum
  BASIC lattice, but counts stay flexible (the budget is one-new-thing-per-game, not a
  total).
- **Real-classic anchoring.** Every game names a real C64 classic (or is a deliberate
  workshop interlude / capstone, flagged as such).

## Still open (refine any time)

- **Custom characters (H4) vs hardware sprites (H5) ordering.** Proposed H4 (Glyph #11)
  before H5 (Skater #12) so a redefined-char *background* exists before the first sprite
  moves over it. Could fold both into one game if Glyph feels too thin as a standalone.
- **Whether Volume 2 needs a dedicated "Meet the VIC-II / sprite registers" teaching
  module** (a `kind: teaching` interlude, like `meet-c64-basic`) before Skater, rather than
  teaching sprite registers inside a game. The shipped Volume 1 taught hardware inside
  games; H5 is heavier, so a short teaching module is a candidate.
- **Volume 4 split pairs (Smooth, Vault).** Borrowed from the Spectrum BASIC V4
  tour-then-deepen pattern; confirm the C64 deepest games actually want splitting, or keep
  them single.
- **Showtime (#24) as a mini-game collection** — sanctioned by `modules-not-games.md` but
  watch the ceiling (only so many genres fit one collection before it wants splitting).
- **Names are working titles** — swap freely; some (Skater, Defender Lite, Builder) are
  placeholders pending an `inspired-by-not-clones` naming pass.
