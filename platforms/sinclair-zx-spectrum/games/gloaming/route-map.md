# Gloaming module 1 — the route map

> **Skeleton session deliverable, 2026-07-02.** One row per unit: method,
> the one-sentence diff narration, the named proof shot, gate status.
> Produced to the authoring contract in [`per-unit-plan.md`](per-unit-plan.md)
> §"The route skeleton and the teachability gate". **Steve reviews this map
> before any prose is written.** Findings that move or reinterpret a planned
> boundary are flagged inline and expanded below the table.

## What was built

Twenty unit end-states in
`code-samples/.../gloaming/prototype/skeleton/unit-01.asm … unit-20.asm`,
derived by [`derive-skeleton.py`](../../../../../code-samples/sinclair-zx-spectrum/assembly/gloaming/prototype/skeleton/derive-skeleton.py)
— the same scripted, assert-anchored subtraction that produced the m1 cut
itself. Every non-detour line is verified verbatim-in-`gloaming-m1.asm` by the
script's audit; detour text is an explicit allowlist. Gate scripts live in
`skeleton/capture/` (poke addresses derived from each unit's `.sym`, never
hardcoded); artefacts land in `skeleton/capture/artefacts/` (not committed).

**Gate evidence, whole-skeleton:**

- 20/20 units (plus the unit-04 pulse variant) assemble under pasmonext and
  run headless under Emu198x.
- `unit-20.sna` is **byte-identical** to the gated `gloaming-m1.sna`, so the
  proven m1 suite (won / sting / probe) transfers to unit 20 as-is; its script
  here is m1-won with paths rewritten.
- Every boundary diff was audited: each N→N+1 diff contains exactly the
  declared insertion (the narration column *is* the diff).
- Detour convergence is mechanical: the 08→09 diff contains only unit 9's
  walls (no detour residue); the 09→10 diff is purely the scaffold clamp
  coming out.

## The map

| # | Unit | Method | The diff, in one sentence | Proof shot | Gate |
|---|------|--------|---------------------------|------------|------|
| 1 | The Empty Square | subset | One attribute write per cell: a cobble field and a wall border make a square at dusk. | `u01-square` — blue-walled square on black | ✅ |
| 2 | The Cobbles and the Brick | subset | The bitmap canvas arrives under the attributes: cobble stipple on the ground, mortar courses on the walls. | `u02-texture` — the same square, now built | ✅ |
| 3 | The Lamplighter | subset | A glyph drawn from an 8-byte definition stands at the square's centre. | `u03-lamplighter` | ✅ |
| 4 | The Heartbeat | subset | The program becomes a frame-locked loop: HALT, step, repeat — and the square holds steady. | `u04-steady` pair (identical, 100 frames apart) + `u04-pulse` pair (differ) — **see flag 2** | ✅ |
| 5 | Reading the Keys | detour | Scan a half-row; a zero bit is a pressed key — the lamplighter glows while one is down. | `u05-idle` / `u05-glow` (white → yellow) | ✅ |
| 6 | One Step | detour | Each direction key moves him a cell per frame: erase old, draw new — and the erase gouges the stipple. | `u06-gouge` — the L-shaped trail | ✅ |
| 7 | Taming the Key | detour | The repeat gate: instant first step, then one per `PLAYER_REPEAT` frames, re-armed on release — the same held keys now walk three cells, not fourteen. | `u07-tamed` vs `u06-gouge` (same input script) | ✅ |
| 8 | Save and Restore | detour → rejoin | Save the cell before you stand on it, restore it as you leave — the ground survives your passage. | `u08-intact` (same walk as 6/7, stipple unbroken) | ✅ |
| 9 | Walls | subset + scaffold | `wall_at` bit-tests the target attribute: the border turns solid and two brick buildings arrive as rectangle data. | `u09-blocked` — pinned beside a building | ✅ |
| 10 | Edges | subset | The numeric clamp comes out: the square's own walls are the boundary — collision is data now. **See flag 1.** | `u10-edge` — pinned against the east wall + the convergence diff | ✅ |
| 11 | The Lamps | subset | Eight unlit lanterns drawn from a table — and your passage leaves them standing. | `u11-lanterns` / `u11-stand` / `u11-passed` | ✅ |
| 12 | Light It | subset | Stepping onto an unlit lamp rewrites its saved-under byte: the state change *is* the rule. | `u12-lit` — the lantern glows behind him | ✅ |
| 13 | The Tally | subset | `lit_count` and the pip bar: progress as coloured cells, no digits. | `u13-pips` — two warm pips after two lamps | ✅ |
| 14 | The Square Warms | subset | `warm_walls` indexes a ramp by `lit_count`: progress as atmosphere, warmth as yellow. | `u14-gold` — the border aglow at eight | ✅ |
| 15 | The Night Is Held | subset | `game_state` arrives with the win: all eight lamps lit → THE NIGHT IS HELD. | `u15-held` | ✅ |
| 16 | The Draught | subset | One compare-and-step rule reads as intent: the wisp hunts you, ghosts through stone, and pins you — its touch not yet priced. | `u16-hunt` / `u16-pinned` (idle player, adjacent wisp) | ✅ |
| 17 | Lives, and the Fall of Night | subset | Contact costs a life and recoils the wisp to its far corner; out of lives, NIGHT FALLS. | `u17-lifelost` / `u17-nightfalls` (idle-probe run) | ✅ |
| 18 | A Small Sound | subset | One beep routine, three voices: the catching blip, the held fanfare, the nightfall sting. **See flag 3.** | `u18-blip-fanfare.wav` (blip → fanfare in sequence) + `u18-held` | ✅ |
| 19 | The Title | subset | The title owns starting a game: GLOAMING, PRESS SPACE, the dusk chime — and setup becomes `init_game`. | `u19-title` / `u19-play` | ✅ |
| 20 | Again | verbatim copy | Win or lose, SPACE returns to a title that remembers your best night — the state machine closes. | `u20-held` / `u20-title` (best-lives pip row) | ✅ |

## Flags — boundary findings for review

**1. Unit 10 ("Edges") reinterpreted — and the detour needs a scaffold.**
The plan gives unit 10 the primitive "Bounds", but no bounds checks exist in
`gloaming-m1.asm`: the perimeter walls seal the square, so there is nothing to
subtract. Meanwhile the detour has a real hazard the plan didn't name: from
unit 6 until walls turn solid, nothing stops held movement walking off the
map, and a dozen cells past the edge the erase/draw writes corrupt system
variables (a real crash, tested). Resolution built here: unit 6 introduces an
explicitly-marked **scaffold clamp** (four compares, honest in the prose:
"the walls will take this job"); unit 9's walls make it redundant; unit 10
retires it and asserts full convergence — *the square itself is the boundary;
data now does what code did*. That gives unit 10 a real diff, a real lesson,
and keeps the plan's declared convergence-at-8 true for the movement core
(the 8→9 diff is walls-only). If you'd rather keep unit 10 as literal bounds
arithmetic, the skeleton needs re-cutting — say the word.

**2. Unit 4's proof shot is a probe, not the end-state.** A pure subset of
the heartbeat shows a steady screen — its honest capture is two identical
frames 100 apart, which proves stability, not the beat. The named Try This
(`unit-04-pulse.asm`, one `inc (hl)` on a HUD attribute) makes the loop
visible and photographs it; the unit's prose should build the probe, see it
beat, then take it out. (Capture note: the probe cell's ink pixels are
invisible over an empty bitmap — the paper bits are what cycle, every 8
frames.)

**3. Audio grouping at 18.** The plan's row for unit 18 names only the blip;
the fanfare and sting have to arrive by unit 20 and belong to no other unit's
idea. Built here as: unit 18 = the beeper primitive with its three voices
(blip / fanfare / sting — one diff, one idea), the dusk chime arrives with
the title at 19 (it is the title's atmosphere), and 20 adds no audio.

**4. Dead code found in `gloaming-m1.asm`: `unlight_pip` — stripped
(approved by Steve, 2026-07-02).** A snuff-era remnant the m1 subtraction
kept — nothing in m1 called it, and the skeleton never taught it. Removed
from `gloaming-m1.asm` the same day; the variable block shifted −17 bytes,
so the m1 suite's pokes were re-derived from the fresh `.sym` (won / sting /
probe re-run, all green; the capture README's documented addresses updated)
and unit 20 re-copied — still byte-identical to the stripped build. The
19→20 diff is now clean of it.

**5. Smaller authored-shape decisions** (all inside the detour's licence or
forced by subtraction; visible in `derive-skeleton.py`):
unit 5 uses the per-key bit-test shape (the combined `cpl`/`or` scan belongs
to unit 7, where its re-arm purpose exists) with a yellow glow that
foreshadows lit lamps; `paint_walls` is the ramp-less name of `warm_walls`
until unit 14; the `play_step` orchestrator wrapper exists from unit 5 (m1's
shape, trivial until 15); setup is inline in `start` until 19 wraps it into
`init_game` (the title is its m1 caller); unit 16's contact compares are
present but neutered to `ret` (the wisp blocks and pins — the taking waits
for lives), which is also why `u16-pinned` is possible at all.

## Reproducing the gate

```
cd code-samples/sinclair-zx-spectrum/assembly/gloaming/prototype/skeleton
python3 derive-skeleton.py            # regenerate + audit the 20 end-states
# assemble each: docker pasmonext --sna unit-NN.asm unit-NN.sna unit-NN.sym
cd capture && python3 gen-scripts.py  # regenerate scripts (pokes from .sym)
emu198x-spectrum --headless --script unit-NN.script.json
```

## Next (after this map is approved)

Phase A prose as the cadence pilot — four units through `/unit-media` +
`/unit-write` + `/verify-unit`, review, and a per-unit number — then phases
B–E at that cadence. Worktrees enter at prose time (MDX at shipped paths).
