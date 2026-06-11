# Flock — The Plan (the first Amiga game)

> **Outline, 2026-06-11.** Derived from [`brief.md`](brief.md) and governed by
> [`amiga-assembly-lineup.md`](../../../../decisions/amiga-assembly-lineup.md) (sprites-first
> reorder) and [`curriculum-structure.md`](../../../../decisions/curriculum-structure.md)
> (uncapped techniques; one new thing per unit). This is the per-unit **outline** — headlines,
> intent, and the one new thing each unit introduces. Full magazine-class prose, the `.asm`
> listings (in `code-samples/`, referenced via `CodeFromFile`), screenshots and audio captures
> are the **authoring** step, not done here.

> *"Get the daft flock home. One sheep at a time, across the lane and over the stream — and mind the duck."*

## Position in curriculum

**Rung 1** of the Amiga Assembly track — after the **Primer** ("Meet the Machine"), before
**Exodus** (the Blitter game). Flock is where the track's moving-graphics foundations are *born*:
hardware sprites, sprite collision in both its modes, the joystick loop, lives/score/state. Every
later Amiga game reuses them; Signal deepens the sprite work (multiplexing) and Exodus brings the
Blitter for what sprites can't do. No Blitter here, no scrolling, no samples — a static bitplane
scene and eight sprite channels, used well.

**Headline (Design Concept):** *Reading the world — "time the gap, commit, breathe."*
**Tradition:** the lane-crosser line — *Frogger* (1981), *Freeway* (1981) — worn warm and farmyard,
with a Llamasoft twinkle.

## What Flock establishes (and who reuses it)

| Primitive (born here) | Unit | Reused / upgraded by |
|---|---|---|
| Composing a static bitplane playfield (Copper + bitplanes, from the Primer) | 1 | every game; Exodus reshapes it with the Blitter |
| Hardware sprite — data, position/control words, DMA | 2 | every sprite everywhere; Signal multiplexes them |
| Joystick read + grid-step movement | 3 | every direct-control game |
| Sprite animation by data-swap | 4 | every animated sprite |
| Deterministic hazard loops (read-and-time the lanes) | 5 | Gobble's ghosts, Highway's traffic |
| **Avoid-mode** hardware collision (`CLXCON`/`CLXDAT`) | 6 | every game that asks "what touched what" |
| Life pool + respawn + game over | 7 | every game |
| **Ride-mode** collision (carried by a platform; absence kills) | 12 | Ascent's platforms, Wanderer's terrain |
| Paula tone SFX (a blip, not a driver) | 11 | Shatter Point upgrades to samples |
| Title → play → win/lose → title state machine | 17 | every game |

## Conventions (as the rest of the track)

- Each unit's **title is the design concept**; the **code primitive** sits beneath it.
- **Read-Alongside + Modern Equivalent** line per unit (authored in build): a specific era
  lane-crosser moment it descends from, plus a modern game using the same idea.
- Each unit meets the per-unit **Definition of Done**: assembles on **vasm → bootable ADF**; runs
  on **Emu198x** (`emu198x-amiga`, script-mode capture); magazine-class prose; ≥1 verified
  screenshot; `CodeFromFile` refs exist + assemble; ≥2 "Try this"; "If it doesn't work"; vault refs
  resolve. (Real-hardware verification is suspended — see
  [`commercial-bar-revamp.md`](../../../../decisions/commercial-bar-revamp.md).)
- **The 8-channel budget is a design rule, not a footnote.** Each level's on-screen cast — the
  sheep plus every hazard and rideable — must fit eight sprite channels. Level layouts are
  budgeted in the level table during authoring; sprite reuse down the screen is **Signal's**
  technique, never smuggled in here.
- **British English**; warm, technical, never condescending. **Always-runnable**: the reader can
  run the project after every unit.

---

## Arc 1 — Cross the lane *(a complete road game by Unit 11)*

### Phase A — A sheep on the farm (Units 1–4) · *the sprite is born*

- **1 — The Farmyard.** Compose the scene: Copper list + bitplanes painting field (bottom), lane,
  and the fold with its pens (top). The Primer taught the parts; this unit makes a *place* from
  them. *New: composing a playfield (revisit of Copper + bitplanes, now with intent).*
- **2 — The Sheep.** The first hardware sprite: sprite data with its position/control words, the
  sprite DMA channel, a white sheep standing in the field. No Blitter, no bitplane tricks — the
  chip draws her for you. *New: a hardware sprite **(the track's moving-graphics opener)**.*
- **3 — Steering.** Read the joystick; grid-step the sheep in four directions; hold her inside the
  screen. The sheep goes where you point. *New: joystick input + grid-step movement.*
- **4 — The Amble.** Two-frame walk by swapping the sprite data pointer as she steps — the
  Amiga's cheapest animation. *New: sprite animation by data-swap.*

### Phase B — The lane (Units 5–8) · **avoid-mode collision** *(the core arrives)*

- **5 — The Tractor.** A second sprite that nobody steers: the tractor crosses its lane on a fixed
  loop, off one edge and on at the other, the same every time. Deterministic is the point —
  you *read* it. *New: the auto-moving hazard loop.*
- **6 — Squashed.** Hardware collision: set `CLXCON`, read `CLXDAT` each frame; sheep touches
  tractor → a squashed beat and back to the field. The chip tells you they met — you decide what
  it means. *New: **avoid-mode** sprite collision **(the load-bearing skill)**.*
- **7 — The Flock in Hand.** Lives are sheep: a row of small sheep icons, one fewer per loss; none
  left → the flock's done and so are you. *New: the life pool + game over.*
- **8 — Busy Lanes.** The hay cart and the farmer's Land Rover join, each lane its own speed and
  direction. Now there's a rhythm to read and a gap to choose. *New: multi-lane choreography
  (within the 8-channel budget).*

### Phase C — The fold (Units 9–11) · **the goal, the score, the sound**

- **9 — The Fold.** Reach a pen at the top and the sheep trots in, safe for good; the next one
  ambles up from the field. Fill every pen → the level is won. *New: goal slots +
  one-sheep-at-a-time.*
- **10 — Keeping Score.** Points per crossing and per pen; the tally written into the playfield
  with a CPU-copied font (no Blitter — the bitplane is ours to write). *New: score + HUD text.*
- **11 — A Soft Baa.** Paula speaks: a hop *baa*, a squashed *splat*, a contented bleat at the pen.
  Tones only — a blip, not a driver; samples are Shatter Point's rung. *New: Paula tone SFX.*

*By Unit 11 the learner has a complete road-crossing game — lanes, lives, pens, score, sound.
That's the Arc 1 deliverable, and it already plays.*

## Arc 2 — The river and the flock *(the inversion, the cast, the finish)*

### Phase D — Ride or drown (Units 12–13) · **ride-mode collision** *(the inversion)*

- **12 — The Stream.** A river band above the lane; hay bales drift along it. The rule flips:
  in the water you drown — *on a bale* you're safe, and it carries you. Same `CLXDAT` read, the
  opposite meaning. *New: **ride-mode** collision + carried-by-platform movement.*
- **13 — The Duck.** A rideable duck paddles the stream — then dips under to feed, on a cycle you
  can learn. Don't be standing on her when she does. *New: the timed treacherous platform.*

### Phase E — The farmyard cast (Units 14–15) · **identity**

- **14 — The Cow.** A slow, wide lane all her own: no gap to time — you squeeze past the bulk.
  A second rhythm on the road, and pure farmyard. *New: the bulk hazard (slow-wide vs fast-narrow).*
- **15 — The Black Sheep.** Rarely, the next sheep up is black: worth a fat bonus, and a touch
  more skittish about it. Risk it or play safe — her chime when she's penned is the game's best
  sound. *New: the bonus spawn (risk/reward).*

### Phase F — Make it finished (Units 16–18) · **pressure + polish**

- **16 — The Nervous Sheep.** Late levels bring the clock: dither too long mid-crossing and she
  gets the wind up and bolts. Introduced as an escalator, never from level one. *New: time
  pressure.*
- **17 — The Title.** "FLOCK" over the farmyard, a daft Paula jingle, press fire to begin — and the
  title → play → win/lose → title state machine underneath it. *New: the game state machine.*
- **18 — The Whole Flock Home.** Level table and escalation (lanes quicken, the duck dips sooner,
  the clock tightens); the clean-level shepherd's bonus; the game-over and all-safe beats; final
  feel pass on the hop. *Consolidation — the finished game.*

**End of Flock:** a complete, charming, period-faithful arcade crosser — a steerable animated
sprite, two opposite collision rules, a farmyard of deterministic hazards, pens to fill, lives,
score, a black sheep, a clock, sound, a title and a play-again loop. The Amiga's first game, and
a real one.

---

## Deprecation-pair seeds (what Flock plants for later games)

- Eight sparse, timing-led sprite lanes (here) → **multiplexed / Copper-reused** sprite swarms (*Signal*).
- A static bitplane scene the CPU writes once (here) → a world the **Blitter** redraws and reshapes (*Exodus*).
- Paula tone blips (here) → **sampled** instruments and an SFX driver (*Shatter Point*).
- One screen (here) → **smooth hardware scrolling** worlds (*Wanderer*).
- Sprite-on-sprite `CLXDAT` (here) → playfield-collision and depth questions (*Ascent*, *Brawler*).

Teaching moments *across games*, motivated by Flock's felt limits — not something Flock reaches for.

## Open for the author

- **Per-level sprite-budget table.** The full cast (sheep, tractor, cart, Land Rover, cow, two
  bales, duck) exceeds eight channels — by design, no level fields them all at once. Each level's
  layout names its cast and proves it ≤ 8; the cow may want an attached pair (two channels) for
  her width — budget her as two.
- **Pen count.** Five is the working figure (Frogger's home slots); the fold art decides.
- **Black-sheep spawn rule.** Fixed cadence (every Nth sheep) or seeded-deterministic? Keep it
  plannable — no RNG mid-crossing; her skittishness should be readable, not random.
- **The nervous clock's face.** A visible meter, or behavioural only (she fidgets, then bolts)?
  Behavioural is more charming; the meter is more legible. Author's call at the screen.
- **River in the Arc 1 scene.** Paint the stream from Unit 1 with a footbridge the early levels
  use (so the scene never changes shape), or repaint the playfield when Arc 2 opens? The bridge
  is the gentler read.
- **Unit count.** ~18 here is an illustrative marker; phases may merge or split during authoring
  as the prose decides, provided one-new-thing-per-unit holds and a finished game lands at the end
  of each arc.
