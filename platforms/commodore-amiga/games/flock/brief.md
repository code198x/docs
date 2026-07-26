# Flock — Brief

**Title (working):** Flock
**System / Track:** Commodore Amiga / assembly
**Position:** Rung 1 — the first game after the *Meet the Machine* primer; the **hardware-sprite** opener. See [amiga-assembly-lineup.md](../../../../decisions/amiga-assembly-lineup.md).
**Scope:** indicative ~16 units across two build arcs; counts illustrative, not a target (per [curriculum-structure.md](../../../../decisions/curriculum-structure.md)).
**Constraint position:** period-faithful — see Section 5.
**Status:** draft

> **The new Amiga front door (sprites-first reorder, 2026-06-11).** Game 1 leads with **hardware
> sprites** — the gentlest, most rewarding way to get a thing moving that a learner *steers* — not the
> Blitter (which moves to rung 2). This keeps the Amiga consistent with the other platforms' direct-
> control first games (Dash / Starfield / Gloaming). Flock is a **new** game, not the re-themed
> `exodus` build; the "Flock" name and sheep theme moved here from that parked Blitter puzzle. A
> brand-new sprite game with no salvage from the `exodus` units. Authored under the uncapped-technique
> model (per [curriculum-structure.md](../../../../decisions/curriculum-structure.md)): it *opens* with
> sprites and layers collision, sound, score and lives across its units, Dash-style — one new thing
> per unit.

---

## Section 1: Pedagogical Role

Teach the Amiga's **hardware sprites** — define, position, move, animate, and above all **collide** them — as the platform's first and gentlest moving-graphics tool, so the reader leaves able to put a character they *steer* on screen and detect what it touches, before the Blitter (rung 2) arrives for everything sprites can't do.

The load-bearing skill is **hardware sprite collision** (`CLXCON`/`CLXDAT`): every later Amiga game leans on knowing what touched what, and Flock teaches it in its two opposite forms at once (see Section 3).

---

## Section 2: Classic Ancestors

- **Frogger** (Konami / Sega, 1981) — the lane-crossing gauntlet: thread deterministic moving hazards to reach the far side, fill the home slots.
- **Freeway** (Activision, 1981) — David Crane's "chicken crosses the road"; the same crossing verb in a barnyard register, and proof the skin can be an animal.
- **Sheep in Space** / the Llamasoft canon (Jeff Minter, 1984) — the lineage of warm, absurd, animal-led arcade games the *tone* belongs to (the daft farmyard, not the leering version of the joke).

---

## Section 3: Remix Unit

*Same verb, new container.* The verb is Frogger's — cross a gauntlet of deterministic moving lanes by timing the gaps — relocated wholesale into a **farmyard shepherding** world: you guide one dim sheep at a time across a country lane and a stream into the **fold**, filling its pens. The container does real work: the hazards become a cohesive barnyard cast (tractors, ambling cows, drifting hay bales, diving ducks), the home slots become pens, the meta-goal becomes "get the whole flock home", and the signature **black sheep** gives it an identity Frogger never had.

---

## Section 4: Core Experience

A warm, tense **top-down** crossing: steer one daft sheep up from the field, reading the lanes — wait for the gap between the tractor and the lumbering cow, dart across, breathe; ride a drifting hay bale over the stream but not the duck that's about to dip — and trot it safe into a pen. Relief as each pen fills; a small comic-tragic gut-punch when one's lost. Moment-to-moment it's *time the gap and commit*; across a session it's *fill the fold, don't lose the flock, and chase the black sheep when you dare*.

---

## Section 5: Constraint Position

**Period-faithful.** Hardware sprites, sprite collision, and a static bitplane playfield are bog-standard 1985 Amiga; Frogger-class crossers were everywhere.

- **In active use:** **hardware sprites** (data, the position/control words, sprite DMA) for the sheep and every hazard; **hardware sprite collision** (`CLXCON`/`CLXDAT`) — the core mechanic, in both its modes (Section 3); the **Copper** for playfield/colour setup; a **static bitplane** background (the farmyard scene, set up once); **joystick** input; simple **Paula** SFX.
- **Deliberately avoided** (each reserved for its rung): the **Blitter** — the background is a static bitplane and every moving thing is a sprite, so nothing is blitted (the Blitter is rung 2); **scrolling** — single-screen (later); **sampled Paula instruments** — light tone-and-SFX only (Shatter Point's rung); **sprite multiplexing / Copper sprite-reuse** — Flock lives within the **8-sprite budget** (sparse, timing-focused lanes); populating busier lanes by reusing sprites down the screen is a *deepening* reserved for a later sprite game (Signal). **AGA** — OCS/A500 period hardware.

---

## Section 6: Visual Direction

- **Palette strategy.** OCS bitplanes, a confident pastoral palette: green field (bottom), grey lane, blue stream, the fold and its pens (top), plus the sprite colours. Sprites get 3 colours each (15 via attachment if a hazard wants it); the static background carries the scene.
- **Sprite ambition.** Small, characterful 16×16 sprites with a gentle 2-frame amble for the sheep; the **black sheep** is a recoloured variant. Hazards are sprites too: tractor, hay cart, the farmer's Land Rover; a wide slow **cow**; a drifting **hay bale** / log; a **duck** with a "dip" frame. Frame budgets stay small — charm over animation spectacle.
- **Per-screen richness.** One screen reads instantly as a place: field, a busy lane, a drifting stream, the fold half-full at the top. The hazards' motion tells you the rules without a word.
- **Visual identity.** Cosy, daft, hand-tended farmyard — the Minter twinkle, never the postcard leer.
- **Magazine-screenshot test.** A lone white sheep stranded mid-lane between a bearing-down tractor and a lumbering cow; a duck dipping under in the stream above; the fold's pens three-of-five full at the top; one **black sheep** waiting in the field. Readable at a glance, unmistakably a game.

---

## Section 7: Audio Direction

- **Title.** A short, daft pastoral jingle — simple Paula tones, not samples.
- **In-game.** Silence-led so the SFX land — the quiet field makes the near-miss tense.
- **SFX scope.** A soft "baa" on each hop; a squelchy *splat* (squashed) and a *sploosh* (drowned) on a loss; a contented bleat as a sheep reaches a pen; a little fanfare when the fold fills; a distinct **chime for the black sheep** home.
- **Integration.** A couple of Paula channels, no mixing complexity — audio never becomes the lesson.

---

## Section 8: Level Design Direction

- **Scale.** Single-screen, self-contained levels; a finished game of roughly six to eight. No scrolling — the whole gauntlet is always on screen.
- **Pacing (the technique ramp).** The road alone (avoid) → faster/more road → the **river inversion** (ride) → road + river both → **diving ducks** (the treacherous-platform timing layer) → the **black sheep** bonus → the **nervous-sheep timer** as the late escalator. Each level/unit adds one new idea, then combines.
- **Signposting.** Entirely visual: the field is the start, the fold is the goal, hazards *are* the farmyard (a tractor reads as "avoid", a hay bale as "ride"). Lives show as little sheep icons; the fold shows progress as it fills.
- **Difficulty curve.** Level one is near-trivial — a single slow lane to a pen — teaching the contract (read the lane, commit). Difficulty comes from lane speed/density, the ride/avoid combination, diving timing, and finally the clock — never from fiddly controls.
- **Onboarding.** First crossing teaches everything: one sheep, one gap, one pen. Cause and effect is immediate.

---

## Section 9: Polish Direction

- **Title screen.** "FLOCK", a sheep (and a cheeky black one), the soft farmyard. Cosy and inviting.
- **Attract mode.** Optional/deferred; if present, a hands-off crossing demoing the lanes.
- **Options.** Minimal — SFX on/off; joystick is the only control (4-way grid steps).
- **Ending.** Per level: the fold fills, a fanfare, on to a busier field. A **clean level (no losses) pays a shepherd's bonus**, so "don't lose one" rewards rather than merely avoids. Game end: a warm "whole flock safe" beat.
- **Loss feel.** A lost sheep is a small, legible, comic-tragic moment (baa + splat/sploosh), a life-sheep gone — never punishing UI.
- **Shippable criteria.** Plays cleanly start to finish, no soft-locks; the hop feel is crisp; the lanes read; the black-sheep risk/reward bites. Would sit happily beside a contemporary cosy arcade game.

---

## Section 10: Anti-goals

- **No Blitter.** Static bitplane background; every moving thing is a hardware sprite. The Blitter is rung 2.
- **No sprite multiplexing / Copper sprite-reuse.** Flock stays within the 8-sprite budget (sparse, timing-led lanes). Busier lanes via sprite-reuse are a later sprite game's deepening.
- **No scrolling.** Single-screen. Scrolling is a later game.
- **No sampled Paula music.** Light tone-and-SFX audio only.
- **No controlling more than one sheep at a time.** One under control; the rest wait in the field. (Multi-control is the rung-2 puzzle's territory — keep them distinct.)
- **No gravity / verticality.** Top-down, grid-step movement. (The side-on, gravity-driven design is the parked rung-2 puzzle.)
- **No random hazards.** Lanes are deterministic loops — you read and time them; that's the skill.
- **No edginess.** The farmyard charm is innocent (the black sheep is as edgy as it gets); no nudge-nudge skin on the sheep theme.

---

## Section 11: Build Trajectory

Two build arcs, indicative unit counts (per [curriculum-structure.md](../../../../decisions/curriculum-structure.md) — counts firm up at build time; the cap is one new thing per unit, not a unit total; techniques-per-game is uncapped). Each arc ends in a complete, playable game.

**Arc 1 — Cross the lane.**
*New:* the static farmyard playfield (Copper + bitplane), the sheep as a hardware sprite (define, position, **steer** with the joystick, grid-step + a 2-frame amble), deterministic road-hazard sprites (tractor/cart/Land Rover looping across lanes), **avoid-mode sprite collision** (`CLXDAT` — touch a vehicle, you're lost), the field/fold, one-sheep-at-a-time, filling the pens, the life-pool, score, a hop SFX.
*Revisits:* —
*Deliverable:* a complete road-crossing game — steer sheep across a busy lane to fill the fold, lives and score, lose-and-respawn. Already a real, finishable arcade game.

**Arc 2 — The river, the farmyard, the flock.**
*New:* the **river inversion** (**ride-mode** collision — you must be *on* a hay bale/log or you drown), **diving ducks** (a rideable platform that periodically submerges — the timing layer), the slow wide **cow** (a second road rhythm — squeeze past bulk vs time the gap), the **black sheep** bonus (rare, high-score, a touch trickier), the **clean-level bonus**, the **nervous-sheep timer** as a late escalator, title screen + the rest of the Paula SFX, escalating level layouts.
*Revisits:* sprite collision (now in both modes in one level), the lane-reading (now road + river combined), the sprite budget (now juggling player + vehicles + rideables within 8).
*Deliverable:* the full Flock — road *and* river, tractors-and-cows / bales-and-ducks, the black sheep, the clock; a complete, distinctive, charming arcade game.

*(Per-unit mapping lives in a sibling `per-unit-plan.md`, written after this brief is accepted.)*

---

## Section 12: Ship Test (Multi-axis)

Per arc, all five axes (verification is emulator-based — real-hardware verification is currently suspended per [commercial-bar-revamp.md](../../../../decisions/commercial-bar-revamp.md)).

**Arc 1**
- **Code:** all units assemble (vasm); the sheep sprite steers crisply; avoid-mode collision is correct (`CLXDAT` read per frame); lanes loop deterministically; passes the Definition of Done.
- **Visuals:** sheep and vehicles render as clean sprites; the field/lane/fold playfield reads; magazine-screenshot test met for a road level.
- **Audio:** hop baa, squashed splat present.
- **Level design:** the road levels are solvable by reading the lanes; level one onboards in one crossing; the fold-fill loop is satisfying.
- **Polish:** lives-as-sheep, pen-fill feedback, respawn, no soft-locks.
- **Within budget:** ≤8 sprites on screen.

**Arc 2**
- **Code:** ride-mode collision correct (carried by the platform; drown in open water); duck dive timing frame-stable; cow as a slow wide hazard; black-sheep spawn + scoring; the timer.
- **Visuals:** hay bale/log/duck and cow render; the duck-dip reads; title screen done.
- **Audio:** drown sploosh, pen bleat, fold fanfare, black-sheep chime, title jingle.
- **Level design:** river and combined levels solvable; the ride/avoid inversion teaches cleanly; the black sheep is a real risk/reward; difficulty crests fairly into the timer.
- **Polish:** clean-level bonus, game-over, SFX toggle; plays start to finish.

---

## Section 13: Pattern Library Extractions

- **rendering** — hardware sprite setup and motion (sprite data, position/control words, sprite DMA). The Amiga's cheapest movable graphic. Amiga-specific.
- **physics / framework** — hardware sprite collision (`CLXCON`/`CLXDAT`) read per frame, in **avoid** mode (contact = fail) *and* **ride** mode (contact = carried; absence = fail). The two-modes-from-one-feature pattern. Amiga-specific in implementation; the design idea (one collision test, two game meanings) generalises.
- **framework** — deterministic lane-hazard loops (objects cycling across a fixed path you read and time). Cross-platform.
- **framework** — fill-the-slots meta-goal (N targets to complete a level) with a life-pool. Cross-platform.
- **input** — 4-way grid-step joystick movement. Cross-platform.

---

## Section 14: Vault Tie-ins

- *Frogger* (Konami / Sega, 1981) — direct ancestor *(vault entry needed)*.
- *Freeway* (Activision, 1981) — the animal-crosser ancestor; David Crane *(vault entry needed)*.
- *Sheep in Space* / Llamasoft / Jeff Minter (1984) — the farmyard-absurd tone lineage *(vault entry needed)*.
- Amiga hardware sprite reference — sprite data, position/control words, DMA (hardware page).
- Amiga sprite collision reference — `CLXCON` / `CLXDAT` (hardware page).
- Amiga Copper reference — playfield/colour setup (hardware page).
- Paula reference — light, for the SFX layer (hardware page).

---

## Optional: Risks

1. **8-sprite budget vs a busy Frogger.** A dense crosser wants more than 8 sprites. *Mitigation:* design the lanes **sparse and timing-led** (Frogger is tense even with few objects per lane); reserve sprite multiplexing / Copper sprite-reuse for a later sprite game (Signal) rather than smuggling it into rung 1.
2. **Inspired-by, not clone.** "Frogger with sheep" must not read as a reskin. *Mitigation:* the farmyard cast (cow rhythm, diving ducks), the fold meta, and especially the **black sheep** are the distinctive identity — lean on them; they're in Arc 2 for a reason.
3. **Broad-but-shallow.** Under the uncapped-technique model, the danger is many systems half-built. *Mitigation:* Arc 1 ships a *complete* road game before Arc 2 starts; each system finished, not all started.
4. **Sprite collision specifics.** `CLXCON`/`CLXDAT` masking and the per-frame read are fiddly. *Mitigation:* introduce collision on a single hazard first (Arc 1), one new wrinkle (ride-mode, then the duck dive) per later unit.
