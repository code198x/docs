# Spectrum assembly — technique ladder

**Status:** Proposal. Nothing here is agreed beyond the route the
[replacement opening](opening.md) already records (Meet Assembly, then
Meteor Storm) and Meteor Storm's extension. Rungs are agreed one at a time; an agreed rung may then gain a
[brief](../../../specifications/brief.md). Genres are suggestions, not
commissioned games. Each game goes [as far as it reasonably can](../../../PROJECT.md#what-makes-a-finished-game),
and the ladder covers as many genres as practical. Per the [charter](../../../PROJECT.md#public-presentation-and-publishing),
nothing on this ladder appears on the site until it is agreed.

## How to read it

The track [ladders up](../../../PROJECT.md#entry-and-progression): each rung
teaches the next technique a reader is ready for, through a game that needs it.
There are no fixed counts. Most readers stop somewhere on the ladder; each game
stands on its own. The capstone gathers the track, and the tiers past it go as
far as the machine goes.

Every rung is a [full game, not a tech demo](../../../PROJECT.md#entry-and-progression).
Sound, loaders, timing tricks and tools enter the track inside a game that
needs them. The one exception is rung 0, Meet Assembly, which is already
published as exercises.

**Evidence** records what `198x/reference/` already supports.
**Needs source** means the rung depends on general knowledge that must be
sourced into `reference/` before the rung is agreed.

## Tier 1: the machine as documented (1982 to 1984)

| Rung | New technique | Genre | Evidence |
|---|---|---|---|
| 0 | *Meet Assembly (published):* instructions, screen memory, loops, routines, keys, frame interrupts, debugging | exercises | yes |
| 1 | *Meteor Storm (published), pushed further:* pre-shifted pixel sprite, frame clock, object pool, collision, scoring, phases; then sound for every event, colour by place, an explosion, a voyage of harder storms, an attract screen and a loading screen | dodge and collect | yes; beeper yes |
| 2 | Grid rules: rotation tables, line clears, a fair random generator | falling-block puzzle | general |
| 3 | Formations, projectiles, attribute clash handled deliberately | fixed-screen shooter | yes |
| 4 | Masked sprites over scenery, tile maps, fixed-point jump physics | single-screen platformer | yes |
| 5 | Enemy behaviour: grid pathfinding, state machines, personalities | maze chase | general |

Meteor Storm is published with one impact sound, a black border, a cyan HUD
and a white playfield. The [proposed extension](../games/meteor-storm/brief.md#proposed-extension)
adds the rest in new units after unit 24, so the published units keep their URLs.
The extension is agreed.

## Tier 2: commercial craft (1984 to 1986)

| Rung | New technique | Genre | Evidence |
|---|---|---|---|
| 6 | A two-word parser, text compression, compact location pictures | text and graphics adventure | needs source |
| 7 | World data: compact rooms, objects, inventory, persistent state, a save; a beeper title tune | flip-screen arcade-adventure | yes; beeper and Follin engine references |
| 8 | Speed: dirty rectangles, compiled sprites, stack blits, a profiled frame budget | bat and ball | Z80 timings, ULA contention |
| 9 | Vector physics: circle collisions, friction, fixed-point angles | pool or snooker | general |
| 10 | Game-tree search: a move generator, minimax, alpha-beta pruning | board game against the computer | general |
| 11 | Smooth software scrolling: character, then pixel, with a back buffer | scrolling shooter | yes |
| 12 | Isometric projection and depth sorting | isometric exploration | general |
| 13 | Two-channel beeper music during play, and what it costs the frame | music-driven action game | beeper and Follin engine references |

## Tier 3: the 128K and the technical peak (1986 to 1989)

| Rung | New technique | Genre | Evidence |
|---|---|---|---|
| 14 | 128K paging for large animation sets; AY music and effects on interrupts | scrolling beat-'em-up | 128K paging, AY-3-8910 |
| 15 | Double buffering with the 128K shadow screen | eight-direction run-and-gun | paging yes; screen flipping needs source |
| 16 | Large maps in paged memory, influence-map AI, fog of war | turn-based strategy | general |
| 17 | Pseudo-3D road and table-driven sprite scaling | racer | needs source |
| 18 | Filled 3D: vectors, clipping, fixed-point trigonometry | 3D combat, tank or flight | needs source |

**Capstone:** a full release that gathers the track: a scrolling or
flip-screen world, AY soundtrack, a save, and tape as part of the design:
a loading screen, its own turbo loader, compressed levels and multiload.
Evidence: TZX yes; compression needs source.

## Tier 4: past the period (demoscene and modern homebrew)

| Rung | New technique | Genre | Evidence |
|---|---|---|---|
| 19 | Cycle-exact timing: racing the beam, contended memory, border effects, the floating bus | arcade game with graphics in the border | ULA timing and snow |
| 20 | Multicolour: attribute changes per scanline beyond the 8×8 limit | top-down role-playing game | needs source |
| 21 | Sampled sound on the beeper and the AY | sports game with a spoken commentator | partly |
| 22 | Procedural worlds: seeded generation of galaxies and landscapes | space trading and exploration | general |

## Genre coverage

The ladder covers puzzle, shooters (fixed, scrolling, run-and-gun), platform,
maze, adventure (text and arcade), bat and ball, sports (cue and commentated),
board game, isometric, music, beat-'em-up, strategy, racing, 3D combat,
role-playing and trading. The branches add a card game and a construction kit.

Not yet placed: one-on-one fighting, pinball, and light-gun games. A
Yearfall revisit would place management simulation. Each needs a technique the ladder does not already teach
through another genre, or a peripheral branch.

## Revisits of BASIC games

Some rungs could be a published BASIC game rebuilt in assembly, with the
speed, sound and detail it could not have in BASIC. A revisit still teaches
its rung's technique, and it must explain its own rules and data for a reader
who comes straight to assembly. Before any public copy says BASIC could not
do something, the [performance-revisit thread](../basic/performance-revisits.md)
must measure it.

| Rung | Candidate revisit | What assembly gives it |
|---|---|---|
| 5 | Night Patrol, in place of the maze chase | patrols with sight lines, many guards, smooth movement; adds stealth as a genre |
| 6 | The Caverns | a parser, compressed text and location pictures |
| 8 | Volley or Brick Bash | pixel movement, several balls, a frame-rate cadence; the thread's first Volley experiment gives the evidence |
| 9 | Touchdown or Drift, in place of pool | fine-grained physics, rotation and smooth scrolling terrain |
| 10 | Three in a Row, grown to a larger board | an opponent that searches ahead instead of following fixed rules |
| 13 | Bright Spark | music and animation that keep running while the player answers |
| 16 | Yearfall, beside or in place of the strategy game | a larger settlement in 128K; places management simulation |

Not yet placed: Tail Chase (several snakes, pixel movement) and Quickstep
(many lanes of smooth traffic) would suit tier 1 or rung 8. Sonar, Locksmith,
Cipher and Crates are paced by the player and have little to gain from speed.
Each can still grow in BASIC.

## Branches beyond the ladder

Branches start after the capstone. They are not rungs: each is its own
direction.

- **Networking.** Interface 1's ZX Net joins Spectrums with a cable. A
  turn-based card game suits it: little data per move, and a real reason for
  two machines to talk. The intended game is a port of **Rachel**, Steve's own
  card game. Modern networking hardware (Spectranet) would add online play;
  see the scope question below. Evidence: Interface 1 reference.
- **Period peripherals.** The +3 disk controller, the Kempston and AMX mice,
  Currah µSpeech and SpecDrum. Evidence: peripherals references, partly.
- **Relatives.** The Pentagon's uncontended timing, and the Timex TC2048's
  extra screen modes. Evidence: Timex reference.
- **Games that ship their tools.** A game with its own construction kit: an
  on-machine level and sprite editor that players use. The deeper tools (an
  assembler, a small compiler, a replacement ROM) connect to Asm198x and
  Foundations rather than this track.
- **Across the Z80 family.** Porting the capstone game to the Amstrad CPC
  and MSX, to learn portable engine design in assembly.

## Open questions

- **Meet Assembly.** It is published as exercises. Decide whether it should
  end in a small game of its own, so the whole track keeps the full-games rule.

- **Scope of modern hardware.** DivMMC, Spectranet and the ZX Spectrum Next
  are outside the period. Decide whether they belong in the curriculum, in the
  Vault only, or (for the Next) in a separate track.
- **Published games.** Gloaming, The Long Night and Shadowkeep are published
  but have no agreed place. Each stays only if it teaches a rung cleanly;
  otherwise it is retired, with redirects, as its own change.
- **Period references.** The historical comparisons implied by the game shapes
  are unchecked and must be sourced before any appears in public copy.
