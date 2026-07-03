# Gloaming module 2 (The Long Night) — the route map

> **Skeleton session deliverable, 2026-07-03.** One row per unit: method,
> the one-sentence diff narration, the named proof shot, gate status.
> Produced to the authoring contract in [`per-unit-plan.md`](per-unit-plan.md)
> §"The route skeleton and the teachability gate" and the module-2 runbook
> section. **Steve reviews this map before any prose is written.** The three
> flags queued in the runbook are resolved-as-built below; new findings
> (including one real bug in the shipped prototype) follow them.

## What was built

Ten unit end-states in
`code-samples/.../gloaming/prototype/skeleton-m2/unit-01.asm … unit-10.asm`,
plus the seam witness `unit-00-seam.asm`, all derived by
[`derive-skeleton-m2.py`](../../../../../code-samples/sinclair-zx-spectrum/assembly/gloaming/prototype/skeleton-m2/derive-skeleton-m2.py)
— the same scripted, assert-anchored subtraction as m1's skeleton, run
newest-first from `gloaming.asm`. The detour spine's nearest-light hunt is
the prototype's own history: the `manhattan`/`seek_best` fragments are
verbatim from the `b601157` tree (introduced `7463ded`, retired `87bf8ce`),
and the script re-verifies them against `git show b601157:…` on every run.
Everything else is verbatim `gloaming.asm` or (where m1 machinery is
carried, units 5–8) verbatim `gloaming-m1.asm` — the audit asserts it
line-by-line. Gate scripts live in `skeleton-m2/capture/` (poke addresses
derived from each unit's `.sym`, never hardcoded); artefacts land in
`skeleton-m2/capture/artefacts/` (not committed).

**Gate evidence, whole-skeleton:**

- 11/11 files (units 1–10 + the seam witness) assemble under Asm198x
  (`--dialect pasmonext --sna`) and run headless under Emu198x. The local
  `pasmo` cross-assembly is byte-identical on every unit (it also supplies
  the `.sym` files, since asm198x doesn't emit them yet).
- **Both chain anchors bind.** `unit-10.sna` is byte-identical to the gated
  `gloaming.sna`, so the proven m2 suite transfers (unit 10's gate scripts
  *are* `dawn`/`dawnwav` with paths rewritten). And the chain bottoms out at
  the module seam: `unit-00-seam.asm` (unit 01 minus its declared
  insertions) is **byte-identical to `gloaming-m1.asm`**, its `.sna` to
  `gloaming-m1.sna` — module 2 begins exactly where module 1's proven build
  ends.
- **Convergence is mechanical.** The 04→05 diff is exactly commit `87bf8ce`
  ("oldest-lit targeting") inverted: the six declared sites and nothing
  else. The runbook's assert — unit-04 == unit-05 with the queue/oldest
  swap inverted — holds.
- Every boundary diff was audited as one idea (05→06 removals are only the
  single-watch consts/init the tables replace; 06→07 is pure addition;
  08→09 is the near-symmetric metric swap, 18 out / 20 in).
- 12 capture scripts ran; every screenshot was read and verified; the three
  WAVs are non-silent with the expected shapes (bells 10 s dense, snuff a
  single short blip in 4.4 s of play, dawn sequence 8 s phrase–sweep–phrase).

## The map

| # | Unit | Method | The diff, in one sentence | Proof shot | Gate |
|---|------|--------|---------------------------|------------|------|
| 1 | The Dark Seeks the Light | detour (history: `7463ded`) | The hunt generalises from you to the *nearest light* — your flame is a candidate too — and a reached lamp is snuffed by the same saved-under rewrite that lit it, silently for now. **See flag 1.** | `u01-turned` (wisp crosses to the lit lamp, ignoring the distant player) / `u01-snuffed` (pip out, lamp unlit again) | ✅ |
| 2 | It Carries Its Prize Home | detour (history: `456cd3a`+`b601157`) | A mode flag gives the night rhythm — hunt, snuff, withdraw home, rest — so every snuff buys the lamplighter a window. | `u02-prize` (withdrawing after the snuff) / `u02-home` (resting at its corner) | ✅ |
| 3 | The Pools of Light | detour (final-form pools) | Lit lamps claim ground: `recompute_pools` re-derives every glow ring from lamp truth, restoring both movers first so their under-buffers stay honest through the recolour. | `u03-pool` — the glow ring on the stipple around the first lit lamp | ✅ |
| 4 | The Tendril | detour (final-form tendril) | The wisp's walk darkens the ground behind it into a fixed-length ring of night whose oldest claim releases — territory, bounded by construction. | `u04-vein` / `u04-later` (the vein advances; the old tail heals) | ✅ |
| 5 | The Night Bears Grudges | subset (convergence point) | The eraser problem answered: greedy-nearest camped your work, so the night now reclaims the ground it lost *first* — the lit-order queue replaces the Manhattan scan (the 4→5 diff is commit `87bf8ce`, exactly). | `u05-grudge` (two lamps lit; the wisp crosses the square for the older one, ignoring the nearer player and prize) / `u05-snuffed` | ✅ |
| 6 | The Night Deepens | subset + m1 carry | Escalation becomes data on two axes — `dusk_table` pace, `dusk_lentab` reach, a new corner per watch — the held screen becomes an interstitial, and lives become a *carried* quantity the redraw must respect. **See flags 3 and 5.** | `u06-held` / `u06-deeper` (watch 2 opens with the wisp probing from the SE corner and the carried two lives surviving the redraw) | ✅ |
| 7 | Dawn Breaks | subset + m1 carry | A run gains an ending you can reach: hold the fifth watch and morning sweeps the square gold — the honest endless (watch 5 wrapping forever) dies here. | `u07-dawn` — DAWN BREAKS over the swept square | ✅ |
| 8 | The Dusk Bells | subset + m1 carry | The one-shot dusk chime becomes the dusk bells — a tune that must yield the keyboard, polling between cells and listening through its rests — and the snuff finds its voice. **See flags 1 and 4.** | `u08-bells.wav` + `u08-title` / `u08-snuff.wav` + `u08-snuffed` | ✅ |
| 9 | Your Longest Night | subset | What deserves to survive changed — the night got longer than a life: the best row counts watches now, not lives, and a lost night still banks the watches it survived. **See flag 2.** | `u09-nightfalls` / `u09-longest` (title with 2 of 5 watch pips lit after a lost dusk-2 run) | ✅ |
| 10 | The Dawn Phrase | verbatim copy | The dawn finds its phrase — dusk's bell answered and reversed, the held G5 completed by the fanfare — and unit 10 is `gloaming.asm`, byte for byte. | `u10-dawn-sequence.wav` + `u10-au-dawn` / `u10-au-title-pips` (the full 5/5 longest-night row) | ✅ |

## Flags — the three queued in the runbook, resolved as built

**1. `blip_snuff` placement — built as proposed: silent at unit 1, voiced
at unit 8.** The snuff arrives at unit 1 as pure mechanism (the buffer-edit
trick performed by the villain; `u01-snuffed` shows the pip die without a
sound) and finds its voice in unit 8's audio batch alongside the bells
(`u08-snuff.wav` is the evidence). m1 precedent holds: sound is a
finish-phase concern, and the cut hierarchy (trim 8–10 first, never the
night) stays intact — a trimmed module still has a complete, silent snuff.
The alternative (voiced from unit 1, feedback-with-event) remains a one-line
re-cut of the derive script if you want it — say the word.

**2. Unit 9's metric swap — the boundary reads as one idea, with one
honest wrinkle to confirm.** The 8→9 diff is the flagged replacement: the
best-lives update leaves the win path, the dawn fills `best_dusk`, the lose
path gains the watch-earned max (m1 recorded nothing on a loss — "a watch
survived is a watch earned" is genuinely new), the title row moves from
lives (3 pips at +14) to watches (5 pips at +13), and the data byte swaps.
One sentence covers it: *what deserves to survive changed — the night got
longer than a life.* The wrinkle: in units 5–8 the carried m1 machinery
updates `best_lives` at m1's own site, the per-dusk win path — so on a
multi-watch night it means "most lives you ever held a dusk with", a
slightly odd interim metric that exists only inside those four unit states
and is never taught as a headline. **Decided (Steve, 2026-07-03): unit 8's
prose names it** — the interim metric is the strain that motivates unit 9's
swap ("the row still counts lives, but a night is longer than a life now —
something has to give"), so unit 9 opens with a problem the learner has
already felt.

**3. Interstitial ownership — the 6/7 boundary survives the
one-sentence test.** Unit 6's diff owns *all* of `end_step`'s change (the
STATE_WIN check and `.deeper`: the held screen becomes the interstitial);
unit 7 never touches `end_step` — STATE_DAWN falls into the existing
"anything else waits for SPACE, then title" branch, so dawn's return to the
title costs zero new state-machine code. Narrations stayed one sentence
each; the derive audit confirms 06→07 contains no `end_step` lines.

## New findings

**4. Units 5–7 carry m1's dusk chime — the "pure subsets" claim bends,
by the seam's own logic (approved by Steve, 2026-07-03).** The module
seam forces the chain bottom to be
`gloaming-m1.asm`, which plays `chime_dusk` at boot and on every return to
the title; `gloaming.asm` replaced it with the title tune. So units 5–7
keep the chime (verbatim m1 text, cut by anchor — same treatment as the
best-lives carry), and unit 8's diff is honestly *replace*, not add: the
chime leaves as the bells arrive. This strengthens the unit's confession —
the input-contract lesson now has a concrete "before" (a blocking one-shot
chime) against the "after" (a tune that must poll). The audit's method
column marks these units `subset + m1 carry`.

**5. A real display bug found in `gloaming.asm` — fixed the same day
(Steve's call, 2026-07-03).** `init_game` (which re-runs at each
`.deeper`) calls `draw_lives`, and `draw_lives` painted `LIVES` (the
constant, 3) pips regardless of the carried `(lives)`. Reproduced against
the byte-identical unit-10 build: lose a life in watch 1, hold the dusk,
and watch 2 opened showing three red pips while `(lives)` was 2; a later
loss then erased pip index 1, leaving a lit–dark–lit row. The bug arrived
with the run/watch split and survived all fifteen playtest rounds; m1 is
unaffected (lives reset per game). **The fix:** `draw_lives` reads the
carried `(lives)` — display-only, the loss logic always read memory.
Re-gated end to end: the six-script m2 suite green (poke addresses
re-derived from the fresh `.sym`, a +2 shift; capture README updated), the
skeleton re-derived against the rebuilt `gloaming.sna`, both anchors
re-verified. On the route, units 1–5 keep m1's constant-count repaint —
honest with a single watch, where lives are set once per game — and the
fix arrives with unit 6's diff: the deepening is what turns lives into a
*carried* quantity, so the redraw must read memory. `u06-deeper` now shows
it — watch 2 opens with the carried two pips.

**6. The stale draught banner is history speaking — units 1–4 make it
true again.** `gloaming.asm`'s `draught_step` banner still says the wisp
"steps one cell toward the *nearest* light source" — 7463ded-era prose the
round-12 queue swap never updated. On the detour spine the banner is
accurate; from unit 5 it's the final file's own quirk. Unit 5's prose can
confess it (the commit that changed the rule forgot its comment — a real
lesson). Related: m1 carries neither this banner nor `paint_buildings`'s
(the m1 cut dropped them), so both arrive with unit 1's diff.

**7. Smaller authored-shape decisions** (all inside the derive script's
allowlist; visible in `derive-skeleton-m2.py`): unit 9's `.thedawn` calls
`dawn_sweep`/`fanfare_held` without the "…the sweep holds the breath…"
comment trio — the ellipses reference the chime, so the trio arrives with
`chime_dawn` at unit 10 (the only authored line this needs is a bare
`call dawn_sweep`); the tendril's reach in units 4–5 is the data byte's
fixed 6 (history's own value until the deepening made it per-watch data);
and unit 6's proof shot leans on the corner probe (SE entry at watch 2)
plus the carried life row, because pace isn't visible in a still — the
lives-carry half only became photographable once finding 5 was fixed.

## Reproducing the gate

```
cd code-samples/sinclair-zx-spectrum/assembly/gloaming/prototype/skeleton-m2
python3 derive-skeleton-m2.py         # regenerate + audit + seam assert
# assemble each (canonical): asm198x --dialect pasmonext --sna unit-NN.asm -o unit-NN.sna
# symbols (until asm198x emits them): pasmo --sna unit-NN.asm /tmp/x.sna unit-NN.sym
cd capture && python3 gen-scripts.py  # regenerate scripts (pokes from .sym)
emu198x-spectrum --headless --script unit-NN.script.json
```

Anchor checks: `cmp unit-10.sna ../gloaming.sna` and
`cmp unit-00-seam.sna ../gloaming-m1.sna`.

## Next (after this map is approved)

Module-2 prose at the module-1 cadence (worktree branch, MDX at shipped
paths, capture via capture.py), opening with the module intro (the playtest
sheet + the two-axis fork, per the plan). Every flag and finding is now
settled: snuff silent at 1 / voiced at 8, unit 8's prose names the interim
best-lives strain, the 6/7 boundary holds, the chime carry is approved, and
draw_lives is fixed and re-gated. The flags above cost a conversation here;
they'd have cost rewritten units later.
