# Gloaming — Brief (DRAFT for review)

> **Reshape settled 2026-07-01 — see §10.** The antagonist's fiction is decided (the draught
> is the dark itself, a malign intelligence), and with it the three Finish-test gaps this brief
> shipped with: behaviour (seek the nearest light), curve (the night deepens), go-again (your
> longest night). §10 is the design contract for the validate-and-repair pass; the full
> alignment of this brief to the current 14-section spec happens in that pass.

**Title (working):** Gloaming  *(name now settled: Gloaming)*
**System / Track:** ZX Spectrum / Assembly
**Position:** Volume 1, **Game 1** — the tiny first game, ahead of Shadowkeep (which becomes Game 2). Per [decisions/spectrum-assembly-gentle-ramp.md](../../../../decisions/spectrum-assembly-gentle-ramp.md).
**Headline (design concept):** *Completion (I finished a real game, in assembly).*
**Total scope:** ~16–18 units — **illustrative, not a target** (the project holds no fixed unit counts; the budget is on techniques, per the gentle-ramp).
**October 2026 ship:** complete and playable end-to-end on Spectrum Next — it is one of the three pieces of the launch's assembly opening (Primer → **this** → start of re-scoped Shadowkeep).

Governs nothing on its own — sits under the gentle-ramp decision. Companion docs to follow once the concept is blessed (per-unit-plan, engineering-plan, beeper-spec), matching the Shadowkeep folder.

---

## 1. Pedagogical role

The first game a learner *builds* in assembly — deliberately small. The win is the sentence **"I finished a real game, in assembly,"** not ambition. It carries exactly the two majors the gentle-ramp assigns it, and nothing heavier:

1. **The structured game loop** — input → update → draw → repeat, locked to the 50 Hz frame (`HALT`/IRQ). The shape every later game reuses.
2. **A cell-based moving character with background save/restore, and simple cell-type collision** — move a glyph one cell at a time; save the cell beneath it and restore it on leaving; read the cell ahead to decide whether you can move and what happens when you arrive.

It also teaches the **"before" half of the track's deprecation pairs**: cell-step movement (which *Smooth Motion* later upgrades to pre-shifted sub-cell glide) and one-thing-per-cell save/restore (which *Overlap* later upgrades to masked drawing). Those upgrades only land if the learner has *felt* the simple version first. Gloaming is that felt version — honestly, not as a strawman.

**Explicitly NOT here** (the drift-trigger guard): no pre-shifted sprites, no masked drawing, no Y-sort, no multi-room/flick, no tile-map decoupled from attributes. One screen, one character, cells. If a unit reaches for any of those, the cliff is returning — stop.

**Audience signpost (recommend, never gate):** assumes the reader has done the Primer ("Meet the Machine") and met variables/loops/subroutines somewhere. A never-programmed learner is pointed at the BASIC course but never blocked.

## 2. Classic ancestors

The archetype is **Ultimate's 1983 single-screen line — *Jetpac*, *Pssst*, *Cookie***: small, single-screen, *complete*, and good enough to be classics. Jetpac especially proved that a tiny game, finished and polished, beats a sprawling unfinished one — exactly the lesson this unit embodies. Period-faithful: every technique here shipped in 1983 Spectrum games.

The lamplighter premise nods to the cosy-dusk mood of later atmospheric games without competing with Shadowkeep's dark-keep adventure — Gloaming is warm and small where Shadowkeep is shadowed and large.

## 3. Concept / core experience

**Dusk in a small square. You are the lamplighter; the screen is darkening cell by cell. Walk the square and light every lamp before night falls — light them all and the square holds back the dark. You win.**

- **Single screen.** A walled town square (cells: cobbles you can walk, buildings/walls you cannot, lamps you can light).
- **The character** is the lamplighter — one cell, stepping cell-to-cell.
- **The mechanic** is collision-as-rules read from the cell you step toward: a wall blocks; an unlit lamp lights (its attribute brightens to a warm yellow, it stays lit, score ticks up); cobbles you simply move onto.
- **Win** = every lamp lit. **Score** = lamps lit / total. The screen visibly warms as you go — the gentle taste of attribute atmosphere that Shadowkeep then makes its whole craft.

The pleasure is small and complete: a tidy loop of *see the dark cell → walk to it → light it → the square brightens*, ending in a screen you brought back to light. No twitch, no death required (see §7 for an optional pinch of jeopardy).

## 4. The two majors, paced

| Major | Introduced | The simple version (what later games upgrade) |
|-------|------------|-----------------------------------------------|
| Structured game loop | Phase A | Frame-locked input→update→draw→repeat at 50 Hz. |
| Cell character + save/restore + cell collision | Phases B–C | Cell-step movement (jerky — *Smooth Motion* fixes); one-thing-per-cell save/restore (no simultaneous overlap — *Overlap* fixes); collision = a bit-test on the cell's attribute. |

Everything else (title screen, a blip of beeper, the warming-atmosphere touch, play-again) is **supporting craft** — paced unit-by-unit but not counted against the two-major budget.

## 5. Constraint position

**Period-faithful, 1983.** Bitmap memory ($4000–$57FF) for the lamplighter glyph; attribute memory ($5800–$5AFF) as the visual *and* rules vocabulary (cobble / wall / unlit lamp / lit lamp are attribute compositions, and collision is a `BIT n,A` on the attribute byte); port `$FE` for keyboard half-row scanning and the beeper (bit 4); an IRQ/`HALT`-driven 50 Hz loop; ROM-font text for the title and messages. The score shows as **coloured pips, not rendered digits** — digit rendering is Shadowkeep's major, and the pip bar is the honest "before" of that deprecation pair. Nothing here a 1983 developer didn't have.

## 6. Visual direction

**The attribute palette *is* the art, the rules, and the signposting at once.** Gloaming holds exactly one element per 8×8 cell (cobble, wall, lamp, or a single character), so attribute clash never bites — each cell owns its two colours cleanly. The whole look is built from **colour temperature**: *warm = light / safe / progress, cold = dark / threat / to-do.* The player reads it in seconds; there is no tutorial. The mood is **dusk turning to night** — a cold dark square (black/blue ground) that the lamplighter pushes back with **pools of BRIGHT warm yellow**. The drama lives entirely in that contrast: the Manic Miner / Atic Atac route to the commercial bar (art and readability), not engine tricks.

### Cell vocabulary (attribute-driven)

| Cell | PAPER | INK | Bright/Flash | Pattern | Role |
|------|-------|-----|--------------|---------|------|
| Cobbles (walkable) | black | blue | — | sparse stipple | cold dark ground; recedes |
| Wall / building (blocks) | blue | white | — | brick/stone | pale dusk-lit stone; reads as built, solid |
| Unlit lamp | black | cyan | steady | lantern-on-post | a lamp, but cold/off — the "to-do" |
| Lit lamp | black | yellow | **BRIGHT** | same glyph, glowing | the warm pool — "done" |
| Lamplighter (player) | black | white | **BRIGHT** | hooded figure + pole | warm-white; never yellow (≠ lamps), never cyan (≠ unlit/draught) |
| The draught (threat) | black | cyan | **FLASH** | wisp / gust | cold, flickering, alive — the lamps' antithesis |

**Forbidden combinations** (Gloaming's take on Shadowkeep's "never a red floor under a red hero"): no walkable cell may use white INK on black — it would hide the white player; unlit lamps use cyan *steady* only, never FLASH, so they never read as the draught; lit lamp and player are both BRIGHT but differ in hue (yellow vs white) so they never merge.

### Layout & a screen sketch

256×192 = 32×24 cells. Row 0 is the HUD; rows 1–23 are the square — a wall border with one gate, interior buildings for routing, ~8 lamps at posts, the lamplighter at the gate, the draught entering from a far corner.

```
 YYY.....                             * * *     <- HUD: lamp pips (Y lit / . unlit), no digits; * = lives
 #######################################
 #.........i...............Y...........#
 #...####..............####............#       @  lamplighter   (white BRIGHT)
 #...#  #....Y.........#  #......i......#       ~  draught       (cyan FLASH)
 #...####........@.....####............#       Y  lit lamp      (yellow BRIGHT)
 #....................................~#       i  unlit lamp    (cyan steady)
 #........Y........[gate]......i........#       #  wall         (white on blue)
 #######################################       .  cobbles      (blue stipple on black)
```

### The magazine-screenshot test

A *Crash* reviewer's screenshot, mid-play: a dark blue-black square, pale dusk-lit stone walls, three or four lamps already glowing BRIGHT yellow with their pools, the white lamplighter mid-stride reaching for a cold cyan lamp, a cyan FLASH draught drifting in from the corner toward a lit one, a pip bar showing five of eight lit and three lamp-pips for lives in the HUD. Instantly Spectrum, period-correct, warm-against-cold, readable at a glance. That readability *is* the design.

### Motion & feedback (supporting craft)

- Lamplighter: a 2-frame cell walk, cell-stepped — deliberately *not* smooth; the jerk is the honest "before" that *Smooth Motion* later fixes.
- Lighting a lamp: a one-frame bright flash + a rising beeper blip. Snuffing: the lamp drops to cold cyan + a lower note.
- Border (`OUT ($FE)`): held **black** — the night beyond the square. (It can't be the walls' blue, or the wall frame vanishes into it; verified in Unit 1.)

## 7. The unit spine (illustrative ~16–18 units)

One idea per unit, always-runnable at every step (the reader can run the project after each unit), gently and near-monotonically rising. Counts are markers, not a contract.

**Phase A — A character on a screen, and a loop (the foundation; "feels easy" is correct).**
1. **The empty square** — lay the attribute grid: cobbles, walls. The screen *is* the map; one attribute write, one cell.
2. **The lamplighter** — draw the character glyph into one cell from a bitmap definition.
3. **The heartbeat** — the structured loop: `HALT` to the frame, do nothing yet, repeat. Prove it runs at 50 Hz.
4. **Reading the keys** — scan port `$FE`; detect a direction press (one half-row, one idea).

**Phase B — Movement done honestly (cell sprite + save/restore).**
5. **One step** — erase the old cell, draw at the new cell. It works because the floor is blank — name that assumption out loud.
6. **Save and restore** — store the cell beneath the lamplighter, restore it on leaving, so movement survives over *any* background. (The naive preservation — flagged as the "before" of masking.)
7. **Walls** — read the cell ahead; if it's a wall, refuse the step. Collision as a bit-test on the attribute.
8. **Edges** — stay inside the square (bounds).

**Phase C — The game (rules, score, win).**
9. **The lamps** — place unlit lamps as cells around the square.
10. **Light it** — step onto an unlit lamp; brighten its attribute; it stays lit. (The background under you is *state* you control.)
11. **The tally** — a row of pip cells (one per lamp) that brighten as you light, mirrored in the HUD. Coloured-cell progress — *not* rendered digits (that's Shadowkeep's major; the pip bar is the "before").
12. **Nightheld** — all lamps lit → win state + a closing line; the square glows.

**Phase D — Jeopardy (core — a game needs a way to lose).**
13. **The draught** — a cold wisp drifts in and moves by a simple rule (a slow patrol). It *reuses* the Phase-B cell-sprite + save/restore — the established major used a second time, **not** a new rendering technique — so it stays inside the budget.
14. **It snuffs the light** — when the draught reaches a lit lamp, the lamp goes cold again (attribute back to unlit). Now the dark pushes back, and routing matters.
15. **Lives, and the fall of night** — touching the draught costs a life; out of lives → night falls → you lose. The lose-state the game was missing.

**Phase E — Make it feel finished (supporting craft; cut hierarchy trims here first, never the bar).**
16. **Title** — "Gloaming", press a key to begin (the sparse-but-suggestive opening, *Hobbit*-style).
17. **A small sound** — a beeper blip when a lamp lights, a colder note when one is snuffed (port `$FE` bit 4).
18. **The square warms** — atmospheric attribute touches as light spreads — the first taste of mood Shadowkeep will build on.
19. **Again** — win *or* lose → back to the title; the game loops, as a real one does.
20. **On real hardware** — verify end-to-end on Spectrum Next (DoD item #4) — the track's hardware-truth beat.

A complete, winnable game exists by unit 12; jeopardy gives it stakes by unit 15; 16–20 polish and verify. ~20 units — still within the gentle-ramp's ~16–20 marker — and the floor (a finished game) is reached well before the count runs out, so the cut hierarchy trims polish (16–19) before anything load-bearing.

## 8. On jeopardy (core)

A game needs a way to lose — so Gloaming has one. **The draught** is the antagonist: a cold wisp that drifts the square, snuffing lit lamps it reaches (the dark literally undoing your work) and costing a life on contact; out of lives, night falls and you lose. This turns the loop from a chore-list into a game — you must *route* against a moving threat that is actively re-darkening the square.

Crucially it stays **within the technique budget**: the draught is a second cell-sprite driven by the *same* save/restore + cell-step movement the player already taught (Phase B) — it adds game-*design* (a threat, lives, a lose-state), not a new engine *technique*. No pursuit AI beyond a simple patrol; no pre-shift/mask/Y-sort. The bar never moves; if the count is tight, the cut hierarchy trims polish (units 16–19), not the jeopardy.

## 9. Decisions settled & next step

Settled with Steve, 2026-06-01:
1. **Name — Gloaming.** Kept.
2. **Premise — lamplighter-at-dusk.** Kept (warm and small, deliberately not a mini-Shadowkeep).
3. **Jeopardy — in, and core.** The draught + lives + lose-state are part of the spine (§7 Phase D, §8), not optional.
4. **Art direction — accepted** (§6). Working defaults, tweakable during authoring: pale dusk-lit stone walls; a *fixed* night backdrop (no darkening sweep — pressure comes from the draught, not a clock); a hooded-figure-with-pole lamplighter glyph. The palette is what the hardware gives us — eight colours, two per cell — and the design leans into that limit rather than fighting it.

**Next step:** the per-unit-plan (unit-by-unit detail + code listings, matching `shadowkeep/per-unit-plan.md`), then wiring the content-collection entries — the authoring the gentle-ramp scopes as the downstream work. The brief is the design contract; authoring builds against it.

## 10. Reshape addendum (2026-07-01) — the dark is the antagonist

Settled with Steve, 2026-07-01, ahead of the validate-and-repair pass
([decisions/endpoint-first-authoring.md](../../../../decisions/endpoint-first-authoring.md),
2026-07-01 amendment). The shipped game passed the winnability gate but fails three of the
Finish test's six questions (curve, go-again, feel — the test postdates this brief). The root
cause is a design gap, not a tuning gap: **the antagonist's fiction was never decided**, so its
behaviour was never designed ("a slow patrol" is a guard's verb, not a wisp's). This section
decides it.

### The fiction: the draught is the dark itself

Not weather. The draught is **a wisp of the night — the gloaming made animate, a malign
intelligence probing the square**. The shipped game already named everything this way (the
title, *Nightheld*, *the fall of night*, the nightfall sting, warm-against-cold throughout);
the brief just never listened. The word "draught" stays (unit 13 is live) with its referent
sharpened: *a draught of the coming night, a cold current of the dark*.

> **Behaviour evolved through play (2026-07-02, rounds 10–12):** greedy
> nearest-light made the wisp a perfectly efficient eraser, so the hunt gained a
> rhythm and a memory: **oldest-lit targeting** (the night reclaims the ground it
> lost *first* — with nothing lit it hunts the lamplighter's own flame, so your
> first lamp turns the hunt away from you), **withdrawal** (after a snuff it
> carries its prize home to the watch's corner), and **the rest** (a fixed beat at
> home, so the snuff window holds however close home sits). The seek mechanics
> below describe the chase step itself, which is unchanged.

### The behaviour: it seeks the nearest light — and the lamplighter is one

One rule: every `DRAUGHT_SPEED` frames, the wisp steps toward the **nearest light source —
lit lamp or the lamplighter, whichever is nearer**. Everything the game needs falls out:

- **At dusk, nothing lit, it hunts *you*.** Menace from the first frame, no tutorial.
- **Every lamp you light is a decoy** — it peels off to snuff the nearer light, so lighting
  the town literally protects you by distracting the night. The premise ("light them all and
  the square holds back the dark") becomes mechanically true.
- **Your progress is its prey.** It snuffs what it reaches (shipped behaviour, kept) and
  retargets — so "all lamps lit at once" is under live pressure and routing is the game.

The intelligence is one compare-and-step rule reading as *intent* — the lesson of Namco's
ghost AI in *Pac-Man*, where simple deterministic per-ghost rules read as personality and
malice. Credited openly per
[decisions/inspired-by-not-clones-naming.md](../../../../decisions/inspired-by-not-clones-naming.md)
(2026-07-01 amendment). Still cell-step + save/restore — no new engine technique; the budget
holds.

### The curve: the night deepens — and the dawn breaks *(amended 2026-07-01, same day)*

Win a dusk → the square holds — then a deeper dusk falls, and the dark comes back faster.
`DRAUGHT_SPEED` stops being a constant and becomes a per-dusk table the loop reads, the
[escalation-as-data](/patterns/cross-platform/framework/escalation-as-data) pattern.

**The night is five watches long, and it ends in dawn.** The original draft here was
endless-arcade (dusks until the night wins). The prototype playtest overturned it: the
human wall sits at one step per 8 frames ("damn near impossible") — an endless table
below that pace is dead data, and every run ending in defeat at the same place is a poor
shape for the track's *completion* headline. Instead: survive five watches — table
**16, 13, 11, 9, 9** (the final watch is the pace the playtest *beat*, hard but winnable:
the climax, not the ceiling) — and **DAWN BREAKS**: a true ending. Lives span the whole
night; THE NIGHT IS HELD is the per-dusk interstitial; NIGHT FALLS is the loss.

### The go-again hook: your longest night

The title screen holds a second pip row — one pip per watch survived, best run, dawn
filling it — surviving the loop back to the title. **Still no rendered digits** (that
stays Shadowkeep's major); the best night is read in lamps, which is the right shape for
this game anyway.

### The dark made visible: the tendril and the pools *(amended 2026-07-02)*

The wisp alone left the dark thin as a character. Amended after the dawn build: the
draught now **trails a tendril of solid night** — cells it crosses go dark and block the
lamplighter (never harm him; the touch of the wisp itself keeps that). A fixed-length
ring releases the oldest cell as each new one is taken, so the tendril snakes and
strangles routes but can never permanently wall the square off; its reach lengthens as
the night deepens (the curve's second axis). The counter-force: **lit lamps cast pools**
— their neighbouring cells warm to dim gold, immune to the tendril. Ground the light
holds. Lighting the square is now cell-by-cell territorial: the premise made mechanical.
The creeping-dark character owes a debt to **Mashadar in Shadar Logoth** (*The Wheel of
Time*) — credited openly per
[decisions/inspired-by-not-clones-naming.md](../../../../decisions/inspired-by-not-clones-naming.md).
The ground gained the §6 cobble stipple in the same stroke — built invisible without it,
the stipple proved load-bearing: it is the visibility substrate for every ground-state
change.

### Feel (pending the human playtest)

Held-key movement at one cell per frame is the sheet's top worry (wall-magnet). Expected fix
is a repeat-gate constant (move on press, then every N frames held) — confirm by hand before
touching. The playtest question for the behaviour sharpens from "menace or wallpaper?" to
**"does the dark feel like it *wants* the lamps?"**

### Blast radius (validate-and-repair, not re-author)

The reshape disproves parts of units 13–15 (behaviour), 12 (*Nightheld* becomes the per-dusk
win), and 19 (*Again* gains the best-night row); it may add one short unit for the dusk table.
The other ~17 shipped units stand. Order of work: baseline human playtest of the shipped game
first (the feel questions survive the reshape), then prototype the reshape, gate it (win *and*
loss scripts re-run), playtest again, then re-author the disproved units.
