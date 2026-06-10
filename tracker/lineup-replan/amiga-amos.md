# Lineup replan — Amiga · AMOS (PROPOSAL — not applied)

> **Status: proposal for review.** Not applied. On sign-off → written into
> `website/src/content/modules/commodore-amiga/amos.yaml` + a decision-record
> amendment under `decisions/amiga-basic-amos-and-blitz.md`. Counts flexible;
> genres may recur across tracks; progressive + spiral. Follows the
> [`spectrum-assembly.md`](spectrum-assembly.md) template (capability ladder →
> spiral spine → sequenced lineup → diff → settled/open).
>
> **AMOS is a peer path to Blitz, not a rung below or above it.** This doc never
> ranks the two. Where AMOS and Blitz share a genre (both have a Breakout, both
> have a Pac-Man), each track climaxes on its *own* strengths — AMOS on
> immediacy and its built-in toolkit, Blitz on compiled speed and the hardware.
> See `decisions/amiga-basic-amos-and-blitz.md` ("the fork is the curriculum",
> drift triggers).

## What AMOS *is* — the climax target

AMOS is interpreted, immediate, batteries-included. The lessons it owns that no
other Amiga track can teach as cleanly:

- **Bobs** — software blitter objects you place and move with a single keyword.
- **AMAL** — the AMOS Animation Language: a tiny co-processor that runs
  movement/animation independently of your main program, in the background.
- **Built-in hardware sprites** and **sprite/Bob collision** as one-line calls.
- **Screens** — open, recolour, overlay, offset and scroll with stock commands.
- **SAM** sampled audio and AMOS Music — sound that "just plays".
- The **seconds-long edit-run loop** — type, F1, see it move.

The capability ladder below is an *AMOS-capability* ladder: one new built-in
power per game. It is **not** a difficulty ranking against Blitz or assembly.

## The AMOS capability ladder (the decomposed climb)

The primer (*Meet AMOS*, 17 units, shipped/LOCKED) already taught: editor +
language, screens/colour/drawing, a Bob you steer, AMAL movement, joystick
input, collision detection, a sound. So the games **start above** "first Bob" —
each rung is one game's headline, inheriting the rungs below.

| Rung | AMOS capability | Why it earns its own game |
|---|---|---|
| 0 | **Bob + AMAL + collision** (primer endpoint) | Already taught — the floor, not a game |
| 1 | **Sprite handling at speed** — many SPRITEs, AMAL-driven, collision groups | First "real game" — falling objects to catch, AMAL doing the motion |
| 2 | **Bobs + gravity + level data** | Platforming verbs: a Bob under physics, reading a level from data |
| 3 | **Sprite arrays + projectiles** — many things spawned/recycled | "Lots of objects" the AMOS way: arrays of sprites, waves |
| 4 | **SCREEN SWAP double-buffer** — flicker-free Bob motion | Clean fast redraw without tearing; the buffered-screen idiom |
| 5 | **Banks + PASTE BOB + multi-screen** | Stamping graphics from Banks; chase AI across linked screens |
| 6 | **Persistent state — room data + save/load** | Flip-screen world that remembers; AMOS save/load |
| 7 | **SAM sampled audio + AMOS Music as a system** | Sound design, not one beep: samples on events, a music bed |
| 8 | **SCREEN OFFSET scrolling + many objects** — AMOS at full stretch | The climax: how far immediacy carries you, and where it strains |

Rung 8 is the honest AMOS climax: a scrolling game that leans on every built-in
power at once and lets the learner *feel* the interpreted ceiling — not as
failure, but as the line where a different tool (Blitz, assembly) is the right
pick for *that* job. This is the "how far you get, how fast" lesson the decision
record names, told without ranking the languages.

## Spiral spine — concept families across the lineup

Each family is introduced once, revisited deeper, then owned. (introduce ·
revisit-deeper · own)

| Family | Introduce | Revisit deeper | Own |
|---|---|---|---|
| **Moving objects (Bobs/sprites)** | #1 Star Catcher (sprites, AMAL) | #2 Crate Stack (Bobs + gravity), #3 Space Swarm (arrays) | #8 Scroll Quest (many, scrolling) |
| **Collision** | #1 (catch the star) | #2 (platform/floor), #5 (ghost contact) | #8 (player vs world + enemies) |
| **Level / world data** | #2 Crate Stack (level layout) | #5 Maze Runner (map), #6 Dungeon Doors (rooms) | #8 (large levels) |
| **Game state / persistence** | #3 (score + waves) | #6 Dungeon Doors (save/load) | #9 Star-Lord (full save + progression) |
| **Sound** | primer (one sound) | #4 Bounce Back (music bed) | #7 Knight Watch (SAM design + music system) |
| **Buffered / clean redraw** | #4 Bounce Back (SCREEN SWAP) | #5, #8 (under load) | #8 Scroll Quest |
| **AI / behaviour** | #1 (falling motion) | #5 Maze Runner (ghost chase) | #9 (mixed enemy behaviours) |

## Locked anchors

| # | Module | Status | Role |
|---|---|---|---|
| 0 | **Meet AMOS** | shipped · **locked** | 17-unit primer — editor, screens, Bobs, AMAL, joystick, collision, sound |
| 1 | **Star Catcher** | coming-soon (stub) | Keep as rung 1 — first full AMOS game |
| 8 | **Scroll Quest** | coming-soon (stub) | Keep as the AMOS-ceiling climax (rung 8) |

The existing stubs (`star-catcher`, `crate-stack`, `space-swarm`, `bounce-back`,
`maze-runner`, `dungeon-doors`, `block-drop`, `scroll-quest`) are largely sound —
this proposal **re-sequences and re-anchors** them to real classics and the
ladder rather than replacing wholesale.

## Proposed lineup (gentle — max 2 new things per game)

Each game adds **one capability rung** plus at most one secondary new family, and
revisits the rest. Every game anchored to a real Amiga classic.

| # | Game (working) | Genre | Amiga classic anchor | NEW headline (rung) | Revisits |
|---|---|---|---|---|---|
| 1 | **Star Catcher** | Catch / fixed-screen | *Gem'X* / catch-'em arcade | **Rung 1: sprite handling at speed** — many SPRITEs, AMAL motion, JOY, SAM hit | primer Bob, collision |
| 2 | **Crate Stack** | Single-screen platformer | *Rainbow Islands* (stacking/climb) | **Rung 2: Bobs + gravity + level data** | sprites, collision |
| 3 | **Space Swarm** | Fixed-screen shooter | *Galaga* / *SWIV* (fixed) | **Rung 3: sprite arrays + projectiles**, wave progression | gravity-free motion, collision, score |
| 4 | **Bounce Back** | Bat-and-ball | *Batty* / *Arkanoid* | **Rung 4: SCREEN SWAP double-buffer** + AMOS Music bed | ball physics, collision |
| 5 | **Maze Runner** | Maze chase | *Pac-Man* / *Zool* (maze feel) | **Rung 5: Banks + PASTE BOB + multi-screen**, ghost chase AI | collision, level data |
| 6 | **Dungeon Doors** | Flip-screen exploration | *Dizzy* / *Gobliiins* | **Rung 6: persistent state — room data + save/load** | multi-screen, map |
| 7 | **Knight Watch** | Arena defend / wave survival | *Chaos Engine* (arena feel) | **Rung 7: SAM sampled audio + AMOS Music as a system** | sprite arrays, AI, state |
| 8 | **Scroll Quest** | Side-scroller (AMOS climax) | *Turrican* (the ambition) / *Rick Dangerous* | **Rung 8: SCREEN OFFSET scroll + many objects** — AMOS at full stretch | *everything*; reveals the interpreted ceiling |
| 9 | **Star-Lord** | Capstone arcade-adventure | *Flashback* (scope) / original | integrate-and-polish: progression, mixed AI, full save | *all rungs* — no new headline, depth + finish |

Notes:
- **Block Drop** (Tetris-like) from the current stub is **deferred / optional** —
  rotation+line-clear is a clean mechanic but adds a *third* new thing if folded
  into any rung-game, so it's parked as a candidate revisit/bonus rather than
  forced into the spine (pacing rule). It can return as a standalone later.
- **#7 Knight Watch** is a *new* game replacing the audio-heavy slot — it gives
  SAM/Music a genre that wants a soundtrack (waves of enemies, audio cues)
  instead of bolting full audio onto an existing rung and breaking the 2-new-max.

## Spiral check (sample families)

- **Moving objects:** sprites #1 → Bobs+gravity #2 → arrays #3 → many+scroll #8.
- **Collision:** catch #1 → platform #2 → enemy-contact #5 → world+enemies #8.
- **Sound:** one beep (primer) → music bed #4 → full SAM+Music system #7.
- **State:** score/waves #3 → save/load #6 → full progression #9.

## Diff vs current catalogue

- **Kept & re-anchored:** Star Catcher (1), Crate Stack (2), Space Swarm (3),
  Bounce Back (4), Maze Runner (5), Dungeon Doors (6), Scroll Quest (8) — same
  slugs, now each tied to a named classic and an explicit capability rung.
- **Added:** **Knight Watch** (#7) — gives the SAM-audio rung its own game so
  audio isn't a third concept on an existing one; **Star-Lord** (#9) capstone —
  the current catalogue has no AMOS capstone (it stops at Scroll Quest).
- **Deferred:** **Block Drop** — parked to keep pacing at ≤2 new things; returns
  as a standalone/bonus, not in the core spine.
- **Re-framed:** Scroll Quest's old "Why assembly" skill is reworded to "where
  AMOS strains" — the ceiling is a *tool-fit* lesson, not a push toward another
  track ranked above AMOS.

## Settled

- **AMOS owns immediacy + built-in toolkit.** Climax is Scroll Quest stretching
  every built-in power, not a hand-off "up" to Blitz/assembly.
- **Ladder = AMOS capabilities, not difficulty rank** vs the other tracks.

## Still open (refine any time)

- **Knight Watch** is the one genuinely new title — keep, or move SAM audio into
  Bounce Back's slot and accept a slightly fuller game there?
- **Block Drop** — fully drop, or schedule as a post-capstone bonus?
- Genre overlap with Blitz (both have Breakout, both have a maze, both have a
  fixed shooter) is **intended** — each climaxes differently. Confirm the
  overlap list is acceptable, or diverge a genre or two for variety.
- Working titles throughout — swap freely.
