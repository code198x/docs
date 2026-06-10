# Lineup replan — Commodore 64 · Assembly (PROPOSAL)

> **Status: PROPOSAL — not applied.** For review. Not written to any catalogue.
> On sign-off → reconciled into
> `website/src/content/modules/commodore-64/assembly.yaml` (reorder + retagline
> the 15 coming-soon stubs) + a decision record. Counts flexible; genres may
> recur across tracks; progressive + spiral, one new hardware rung per game.
> Follows the format set by [`spectrum-assembly.md`](spectrum-assembly.md): a
> decomposed hardware ladder, an explicit spiral spine, a sequenced lineup,
> locked anchors, a diff, settled/open sections.
>
> **Where the C64 differs from the Spectrum.** The Spectrum's hard part is
> *software* — drawing moving things cleanly over a coloured background (masking,
> pre-shift, Y-sort). The C64's hard part is *the hardware* — the VIC-II gives
> you sprites, a raster beam you can interrupt, and a smooth-scroll register for
> free, but each is a doorway to a deeper technique (multiplexing, split screens,
> raster-time budgeting). So the C64 ladder is a **VIC-II / 6502 hardware
> ladder**, not a software-rendering one. Same shape — one rung per game, every
> later game inherits the rungs below — different rungs.

## The VIC-II / 6502 hardware ladder (decomposed)

The C64 hands you generous hardware, but each gift has a "now do it properly"
behind it. Each rung is **one game's headline**; later games inherit everything
below:

| Rung | Technique | Why it's its own game |
|---|---|---|
| 0 | **Char / screen + colour memory** (no moving hardware) | Meet the Machine + Starfield foundation — the screen and colour RAM as the canvas |
| 1 | **Hardware sprites** — VIC-II sprites, the C64's headline feature | Sprites *are* the C64; one game on placing, moving, animating, colliding them properly |
| 2 | **Custom charsets + tile maps** — redefine the font, build worlds from chars | The cheap, fast C64 world-building idiom; collision against a tile map |
| 3 | **Raster interrupts / split screens** — stable IRQ at a scanline, two zones | The first taste of the raster beam as a clock; a fixed status panel over a play area |
| 4 | **Smooth hardware scrolling** — the VIC-II scroll register + column/row shift | The Amiga-envy effect the C64 does *in hardware*; a scrolling world that streams |
| 5 | **Sprite multiplexing** — reuse 8 sprites down the screen for 16-32 objects | "Many things at once"; raster-timed sprite re-positioning, the canonical C64 trick |
| 6 | **SID interrupt-driven music** — a player ticking under a running game | Music that plays *while the game runs*, not blocking it; the Hubbard paradigm |
| 7 | **Raster-time budgeting** — stable IRQ chains, doing it all inside one frame | The capstone discipline: scroll + multiplex + music + logic, all inside 50Hz |

Rung 0 is already shipped (Meet the Machine + Starfield). Rung 1 (hardware
sprites) is *introduced* inside Starfield at primer level — so the next game
**deepens** sprites rather than introducing them, exactly as Spectrum's
Lamplight deepened masking after Shadowkeep introduced it. Keeps the ramp gentle
and reuses the shipped flagship-opening.

## Locked anchors

| # | Module | Status | Role |
|---|---|---|---|
| 0 | **Meet the Machine** | shipped · locked | 6510 + screen/colour memory + control flow + first SID note (16 units) |
| 1 | **Starfield** | shipped · locked | First *complete* game — hardware sprites, joystick, SID SFX, a first raster interrupt (16 units, rung 0→1 intro) |

Both ship complete and stay untouched. Starfield already lights up the *intro*
level of sprites, SID and raster interrupts (per its unit skills) — so the
ladder treats those as **introduced**, and the games below **deepen** them. This
is the C64 equivalent of "Shadowkeep introduces masking; Lamplight deepens it."

**Cadence (the flagship) stays deferred — it is the post-launch capstone**, not
a ladder rung. Cadence is the locked-concept showcase (horizontal music-driven
shooter, Otocky × Hubbard) that sits where Shadowkeep's later arcs sit: off the
finishable-opening critical path. The capstone *in this ladder* (#11 below,
working title **Overdrive**) is the raster-budgeting integration game that
*earns* you Cadence later — it is not Cadence itself.

## Proposed lineup (gentle, one-new-thing-per-game)

Each game adds **one rung or one new family**, and revisits the rest.
Inspirations are real C64 classics (the commercial-bar anchor — Hubbard-grade
SID, fast scrolling, sprite work).

| # | Game (working) | Genre | Inspiration | NEW headline | Revisits |
|---|---|---|---|---|---|
| 2 | **Platform Panic** | Single-screen platformer | Bounder / Monty on the Run | **Rung 1 deepened: hardware sprites** — gravity, jump physics, sprite-vs-background collision | screen/colour memory, joystick, SID SFX (Starfield) |
| 3 | **Maze Raider** | Maze chase | Pac-Man / Ghost'n Goblins maze sections | **Rung 2: custom charsets + tile maps** — redefined font, tile collision, simple chase AI | sprites, jump-free movement, SID SFX |
| 4 | **Brick Basher** | Bat-and-ball | Arkanoid / Krakout | **ball physics + reflection angles** on a char playfield; power-up state | sprites (ball/bat/blocks), tile/char layout, collision |
| 5 | **Night Raid** | Side-view shooter w/ status panel | Scramble / Hyper Sports | **Rung 3: raster interrupt split screen** — locked status panel over the play zone; fuel/terrain | sprites, charset terrain, SID SFX, collision |
| 6 | **Scroll Runner** | Horizontal runner / shooter | Uridium / Armalyte | **Rung 4: smooth hardware scrolling** — VIC-II scroll register, column shift, level streaming, camera | raster split (panel over scroller), sprites, tiles |
| 7 | **Sprite Storm** | Arena / wave shooter | Wizball / Sanxion | **Rung 5: sprite multiplexing** — 16-32 objects via raster-timed sprite reuse, sorting | scrolling, raster IRQ, sprites, collision |
| 8 | **SID Symphony** | Rhythm / music toy | Master of Magic intros / Galway demos | **Rung 6: SID interrupt-driven music** — a player ticking under the game on the raster IRQ | raster IRQ, sprites for the visualiser, input |
| 9 | **Catacombs** | Dungeon explorer (scrolling) | Gauntlet / Druid | **map systems + item management** over a large scrolling world | scroll, multiplex (enemies), tiles, SID music |
| 10 | **Raster Rider** | Pseudo-3D racer | Pole Position / Buggy Boy | **raster-effect road** — per-scanline colour/scroll tricks, perspective illusion | raster IRQ (deepened), sprites, SID music |
| 11 | **Overdrive** | Vertical / multi-dir shooter | Delta / Mega-Apocalypse | **Rung 7: raster-time budgeting** — scroll + multiplex + music + logic in one stable 50Hz frame | *everything* — the integration game |
| 12 | **Dungeon Crawl** | Adventure w/ disk I/O | The Last Ninja / Times of Lore | **disk I/O + save system** — large game design, persistence | scroll, multiplex, tiles, music, raster budget |
| 13 | **Isometric Quest** | Isometric adventure | Zaxxon / The Last Ninja iso scenes | **isometric projection + depth sorting** (the hard render, *now* — everything below is owned) | multiplex (sorted), tiles, save, music |

Optional later genre-breadth games (sequence when their rung is owned, not
launch-gating): **Arena Fighter** (beat-'em-up — animation states, hit
detection, two-player; revisits sprites + multiplex), **Parallax Patrol**
(multi-layer parallax shooter — deepens scroll into layered parallax; revisits
multiplex + raster budget), **Mega Blaster** (Turrican-style large-sprite action
platformer — deepens scroll-action + boss state machines). These were stubs;
they recur the shooter/platformer genres at greater depth and slot in once the
ladder rungs they lean on (scroll, multiplex, raster budget) are taught.

**Symphony's End** (the old "capstone with demo-scene techniques") is **folded
into Cadence's territory** — the demo-scene / full-showcase capstone is the
flagship's job (Cadence), so a *second* all-techniques capstone is redundant. Its
demo-effect content (stable IRQ chains, raster bars, all-techniques-at-once) is
what **Overdrive (#11)** teaches as rung 7. Recommend dropping `symphonys-end` as
a separate module; its name could later return as a Cadence-track finale.

~12 games post-anchor, each introducing **one** hard hardware thing. Isometric
depth-sort moved to #13 (the end): by the time you reach it you already own
multiplexing-with-sorting, tiles, save, and music, so it adds *one* concept, not
six — same move the Spectrum exemplar made with Greypeak.

## Spiral spine (concept families × introduce / revisit-deeper / own)

| Family | Introduce | Revisit deeper | Own |
|---|---|---|---|
| **Hardware sprites** | Starfield (#1, place/move one) | Platform Panic #2 (physics), Maze Raider #3 (multiple) | Sprite Storm #7 (multiplexed) → everywhere after |
| **Charset / tile worlds** | Maze Raider #3 | Night Raid #5 (terrain), Scroll Runner #6 (streamed) | Catacombs #9, Isometric Quest #13 (iso tiles) |
| **Raster interrupts** | Starfield #1 (one IRQ) | Night Raid #5 (split screen), Raster Rider #10 (per-line effects) | Overdrive #11 (stable IRQ chains, budgeted) |
| **Smooth scrolling** | Scroll Runner #6 | Catacombs #9 (large world), Overdrive #11 (multi-dir) | Parallax Patrol (layered parallax) |
| **Sprite multiplexing** | Sprite Storm #7 | Catacombs #9 (enemy hordes) | Overdrive #11, Isometric Quest #13 (sorted) |
| **SID music** | Meet the Machine #0 (one note), Starfield #1 (SFX) | SID Symphony #8 (interrupt-driven player) | every game from #9 on runs music under play |
| **Raster-time budgeting** | implicit from #5 on | Sprite Storm #7, Raster Rider #10 | Overdrive #11 (the capstone discipline) |
| **Collision** | Starfield #1 (sprite-sprite) | Platform Panic #2 (sprite-bg), Brick Basher #4 (reflection), Maze Raider #3 (tile) | scaled across all later games |
| **AI** | Maze Raider #3 (chase) | Sprite Storm #7 (formation), Catacombs #9 (hordes) | Overdrive #11 (patterns), Arena Fighter (opponent) |

The two threads the brief calls out explicitly:

- **SID music thread** — `sid-symphony` (#8) is the *introduce* point for an
  interrupt-driven player (rung 6), seeded by the single note in Meet the Machine
  and the SFX in Starfield; from #9 on, music plays under the running game as a
  matter of course; the demo-scene finale that `symphonys-end` gestured at is
  absorbed into **Cadence** (flagship) — the C64's music-flagship — rather than a
  duplicate capstone.
- **Raster / scroll / multiplex hardware thread** — sequenced as three staggered
  families that *converge*: raster IRQ (intro #1 → split #5 → effects #10),
  scrolling (intro #6 → large #9 → multi-dir #11), multiplexing (intro #7 →
  hordes #9 → sorted #13), all three owned together at **Overdrive (#11)**, which
  is exactly the raster-time-budgeting rung.

## Diff vs current catalogue

Current: 2 complete (Meet the Machine, Starfield) + 15 coming-soon stubs in a
roughly arbitrary order. Proposed: the same 2 anchors + ~12 sequenced ladder
games + 3 optional later breadth games, **1 stub dropped**.

| Stub (current) | Disposition |
|---|---|
| `platform-panic` | Kept → **#2**, retagged as the sprite-physics deepener (rung 1) |
| `maze-raider` | Kept → **#3**, custom charsets + tiles (rung 2) |
| `brick-basher` | Kept → **#4**, ball physics on a char field |
| `night-raid` | Kept → **#5**, raster-split status panel (rung 3) — *re-sequenced earlier* (was #8) to introduce raster split before the scroller needs it |
| `scroll-runner` | Kept → **#6**, smooth hardware scroll (rung 4) |
| `sprite-storm` | Kept → **#7**, sprite multiplexing (rung 5) |
| `sid-symphony` | Kept → **#8**, interrupt-driven SID music (rung 6) |
| `catacombs` | Kept → **#9**, large scrolling world + items |
| `raster-rider` | Kept → **#10**, per-line raster road effects |
| `dungeon-crawl` | Kept → **#12**, disk I/O + save |
| `isometric-quest` | Kept → **#13**, iso depth-sort (the hard render, last) |
| `mega-blaster` | Kept → **optional later** breadth (scroll-action platformer, deepens scroll) |
| `arena-fighter` | Kept → **optional later** breadth (beat-'em-up, deepens sprites) |
| `parallax-patrol` | Kept → **optional later** breadth (layered parallax, deepens scroll) |
| `symphonys-end` | **Dropped** — duplicate all-techniques capstone; its content is rung 7 (**Overdrive**, new) and its showcase role is the flagship's (Cadence) |
| — | **New: `overdrive` (#11)** — the raster-time-budgeting integration capstone the ladder was missing |

Net: stubs reordered into a gentle rung-per-game climb; `night-raid` pulled
earlier so the raster split is taught before scrolling leans on it; one new
integration game (**Overdrive**) added to own rung 7; one redundant capstone
(`symphonys-end`) dropped.

## Settled (in this proposal)

- **Ladder shape** — VIC-II / 6502 hardware ladder, rungs 0-7, one rung per game,
  later games inherit lower rungs. The C64-specific analogue of the Spectrum
  rendering ladder.
- **Anchors locked** — Meet the Machine + Starfield ship as-is; sprites/SID/raster
  are *introduced* there and *deepened* below, not re-introduced.
- **Cadence stays the deferred flagship** — the music-driven showcase capstone,
  off the launch critical path; **Overdrive** is the in-ladder integration game,
  not a flagship substitute.
- **`symphonys-end` dropped**; rung-7 content lands in Overdrive, showcase role to
  Cadence.

## Still open (refine any time)

- **Naming** — `Overdrive` is a working title for the rung-7 integration game;
  swap freely. Could equally be the slot where a re-scoped `symphonys-end` name
  returns if you prefer keeping the existing slug.
- **Optional-breadth placement** — Arena Fighter / Parallax Patrol / Mega Blaster
  are sequenced loosely as "after their rung is owned"; pin exact positions when
  their briefs are written, or let them recur across a later volume.
- **Brick Basher's rung** — currently a *consolidation* game (no new rung, deepens
  collision + sprites). Fine as a gentle breather, or fold its mechanics into
  another game if the ladder wants tightening — the Spectrum exemplar left the
  same "fold two where a genre carries both?" question open.
- **Disk I/O placement** — `dungeon-crawl` (#12) introduces save/load; could move
  earlier if a smaller game wants persistence sooner.
