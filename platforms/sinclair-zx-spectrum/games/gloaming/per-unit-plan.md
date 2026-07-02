# Gloaming — The Plan (two modules, one game)

> **Outline, 2026-07-02.** Supersedes the 2026-06-01 single-module outline. Derived from
> [`brief.md`](brief.md) (with its §10 reshape contract), the fifteen-round
> [`prototype-log.md`](prototype-log.md), and the proven prototype
> (`code-samples/.../gloaming/prototype/gloaming.asm`, gate suite in `prototype/capture/`).
> Governed by [`spectrum-assembly-gentle-ramp.md`](../../../../decisions/spectrum-assembly-gentle-ramp.md)
> (2026-07-02 amendment: one game, two modules). This is the per-unit **outline** —
> headlines, the one idea, the primitive, and the confession each unit carries. Prose,
> listings, and captures are the authoring step.

> *"Dusk in a small square. Light every lamp before the dark wins. The first game you
> finish in assembly — and then the game that teaches you what finishing really means."*

## The decomposition principle

The prototype's commit history is the **discovery** order; this plan is the **teaching**
order, and they deliberately diverge. The rule applied throughout: the learner builds an
iteration only where *feeling the failure teaches* (the wall-magnet, the eraser problem);
where the iteration was just us being wrong (the bounce, rules-before-canvas), the learner
builds the final design and hears the story as a confession. Every confession below is
lived history from the prototype log, told where it pedagogically belongs — not where it
happened.

Decisions taken with Steve, 2026-07-02: the bounce is never built (confessed in prose);
nearest-then-oldest targeting are both taught (the eraser problem is the track's best
design lesson); texture is unit 2 (the canvas precedes the paint); audio consolidates in
each module's finish phase; and the tiny-game tension resolves as **two modules** rather
than trimming the reshape or growing the promise.

---

## Module 1 — Gloaming (the tiny first game)

**Headline:** *Completion — "I finished a real game, in assembly."*
**Endpoint:** the derived cut of the proven prototype — single dusk, a draught that hunts
the player (no snuffing, no tendril, no watches), win = all eight lamps, loss = lives.
To build and gate before authoring (never-regress: this cut replaces the shipped game
only when it passes).

### Phase A — a square at dusk

| # | Unit | The one idea | Primitive / confession |
|---|------|--------------|------------------------|
| 1 | The Empty Square | The screen is the map: one attribute write per cell | Attribute memory; cobble/wall vocabulary |
| 2 | The Cobbles and the Brick | The canvas: bitmap texture under the attributes | `blit_tex`, `fill_ground`, `fill_walls`. **Confession:** the shipped game skipped this — weeks later, whole mechanics were built *invisible* because there were no pixels to recolour. The canvas precedes the paint. |
| 3 | The Lamplighter | A glyph drawn from a bitmap definition | Cell-sized character data |
| 4 | The Heartbeat | The structured loop, locked to the frame | `HALT`; input→update→draw→repeat |

### Phase B — movement done honestly

| # | Unit | The one idea | Primitive / confession |
|---|------|--------------|------------------------|
| 5 | Reading the Keys | Scan a half-row; detect a press | Port `$FE` |
| 6 | One Step | Erase old cell, draw new cell | Works because the floor is uniform — named aloud |
| 7 | Taming the Key | One press ≠ fifty presses a second | The repeat gate (`PLAYER_REPEAT`). **Try This first:** hold a key on the ungated build and feel the wall-magnet — the playtest's exact words were "WAY TOO FAST". Teaches the countdown-timer idiom *the night will reuse*. |
| 8 | Save and Restore | The ground survives your passage | The under-buffer (the "before" of masking) |
| 9 | Walls | Collision is a bit-test on the attribute | `wall_at`; interior buildings as rectangle data — routing exists from here on |
| 10 | Edges | Stay inside the square | Bounds |

### Phase C — a game

| # | Unit | The one idea | Primitive / confession |
|---|------|--------------|------------------------|
| 11 | The Lamps | Unlit lamps as cells | `lamp_data` |
| 12 | Light It | Stepping onto state changes it | The saved-under byte *is* the rule |
| 13 | The Tally | Progress as coloured pips, no digits | The pip bar (digits are Shadowkeep's major) |
| 14 | The Square Warms | Progress as atmosphere | `wall_ramp` — a data table indexed by `lit_count`. **Confession:** the shipped ramp "warmed" blue→magenta — GRB arithmetic, not design; warmth here is yellow. |
| 15 | The Night Is Held | All lamps lit → the win | Win state + a closing line |

### Phase D — jeopardy

| # | Unit | The one idea | Primitive / confession |
|---|------|--------------|------------------------|
| 16 | The Draught | One rule reads as intent: step toward the player | Compare-and-step on the greater axis; the wisp ghosts through stone (the asymmetry named). **Confession:** the shipped draught *bounced*; the playtest called it "just bouncing — not very menacing". We never teach the bounce — Namco's ghosts (credited) knew better in 1980. Reuses unit 7's timer idiom. |
| 17 | Lives, and the Fall of Night | Contact costs a life; out of lives, night falls | Loss state. **Confession — the recoil:** respawning the player but leaving the hunter at the catch-site strips every life in seconds. A hunting antagonist exposes fairness assumptions wallpaper never tests. |

### Phase E — make it feel finished

| # | Unit | The one idea | Primitive / confession |
|---|------|--------------|------------------------|
| 18 | A Small Sound | The beeper: a rising blip when a lamp catches | Port `$FE` bit 4; the blips quote a motif the learner won't meet in full until module 2 |
| 19 | The Title | Sparse and suggestive; press a key to begin | Title state + input lock |
| 20 | Again | Win or lose → the title; a real game loops | The state machine closes |

**Module 1 ends:** a complete, winnable, losable, tiny game — the original promise, kept.

---

## Module 2 — The Long Night

**Headline:** *Iteration — "a finished game becomes a better game."*
**Endpoint:** the proven prototype exactly as gated 2026-07-02 (five watches, dawn,
audio). The only module in the track where the learner redesigns a game they already
own — and every redesign step is a real playtest finding from the prototype log.

**Module intro (framing, not a build unit):** the playtest sheet — what a winnability
gate proves and what only hands can. The module retells the pass's fifteen rounds as its
own arc.

| # | Unit | The one idea | Primitive / confession |
|---|------|--------------|------------------------|
| 1 | The Dark Seeks the Light | Targeting generalises: nearest light, and your flame counts | The Manhattan scan; snuffing (the night undoes your work) |
| 2 | It Carries Its Prize Home | Behaviour needs rhythm, not just rules | The mode flag: hunt → snuff → withdraw → rest. **Confession:** relentless efficiency isn't menace, it's a slog — "a pain in the bum to win". Pac-Man's scatter, credited. |
| 3 | The Pools of Light | Claimed ground: light with a radius | `recompute_pools`, `glow_ring`; the restore-both-movers discipline |
| 4 | The Tendril | The night takes territory: a ring buffer of darkness | `tendril_push`; fixed-length release = no permanent walls by construction. **Confessions:** the gap bugs — re-crossing your own tail (the claim scan) and pool immunity punching holes (immunity became self-healing). |
| 5 | The Night Bears Grudges | The eraser problem: greedy-nearest camps your work | The lit-order queue; oldest-lit targeting. The track's sharpest design lesson: *optimal for the AI is boring for the player*. |
| 6 | The Night Deepens | Escalation as data, on two axes | `dusk_table` + `dusk_lentab`; watches; the held screen becomes an interstitial; corners + the gathering. **Confession:** front-loaded reach — "a practised player lost at watch 2"; readable before it's a threat. |
| 7 | Dawn Breaks | A run needs an ending you can *reach* | `STATE_DAWN`; the sweep. **Confession:** pace 8 was the human wall — the final watch is the climax, not the ceiling; endless-arcade died at the playtest. |
| 8 | The Dusk Bells | A title tune that yields the keyboard | Phrase stepping between polls. **Confession:** a tune changes the input contract of every screen that returns to the title. |
| 9 | Your Longest Night | A best that survives the loop | The pip row; still no digits |
| 10 | The Dawn Phrase | Motif discipline: dusk's bell, reversed | `.bpr` notation + `build198x beeper`; the audition sheet (three candidates) as the worked example of choosing by ear |

**Module 2 ends:** the five-watch night the author beat on 2026-07-02 — and a learner
who has watched a real game get better under their own hands.

---

## Carried forward

- **Deprecation pairs intact:** cell-step movement and one-thing-per-cell save/restore
  remain the honest "before"; Smooth Motion / Overlap remain later revisit candidates.
- **The cliff guard holds across both modules:** no pre-shift, no masking, no Y-sort, no
  multi-room. Cells, attributes, tables, and straight-line code throughout.
- **Cut hierarchy:** module 1 trims phase E first, never the game; module 2 trims units
  8–10 (audio/pips) first, never the night.
- **Next steps:** build + gate the module-1 cut; realign `brief.md` to the 14-section
  spec (two-module structure noted); then author module 1 to the DoD.
