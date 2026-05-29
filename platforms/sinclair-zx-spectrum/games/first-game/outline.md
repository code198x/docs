# The Tiny First Game (outline)

> **Status:** Draft outline, 2026-05-29. The assembly track's second opening artefact, per
> [`spectrum-assembly-gentle-ramp.md`](../../../../decisions/spectrum-assembly-gentle-ramp.md).
> Sits *after* the Primer and *before* Shadowkeep. `first-game` is a working slug and the title is
> deferred (working concept: **"Strongroom"** — a single room, collect the scattered gems). Design
> outline, not authored unit prose.

## What the tiny first game is

A **complete, winnable, single-screen, cell-based** game — deliberately small. The achievement is
*"I finished a real game, in assembly,"* not ambition. It is the bridge between knowing the machine
(the Primer) and building at scale (Shadowkeep).

**Concept:** a single walled room holds a handful of scattered gems. You move a character
cell-by-cell with the cursor keys, blocked by the walls. Step onto a gem to collect it. Collect
them all to win. One screen, no enemies — the point is *finishing*, not difficulty.

Why no enemy: a moving enemy needs AI, a third major technique. The budget is two (below), so the
threat/inhabitant idea is **Shadowkeep's** ("A Presence in the Dark"), not the first game's.

## The two major techniques it owns (the budget)

1. **The game loop** — the structured `input → update → draw → repeat` cycle with frame timing.
2. **A cell-based moving sprite with simple collision** — a single 8×8 sprite at a cell position
   in RAM, moved cell-by-cell with background save/restore, colliding against a tile map.

Everything else (screen layout, full keyboard read, room-as-data, collect/win, a beeper blip, a
restart state machine, a "make it look finished" pass) is *supporting work paced across units* to
keep those two majors gentle — not extra majors.

## It resolves the Primer's two cliff-hangers

- **The screen-thirds / interleaved layout** (Primer Beat 5) — needed to draw a sprite at an
  arbitrary cell. Resolved in Unit 1.
- **The full 8-half-row keyboard matrix** (Primer Beat 8) — needed to read several movement keys.
  Resolved in Unit 7.

## It reuses the Primer in full

The learner arrives able to assemble/run, move bytes between registers and memory, write screen
($4000) and attributes ($5800), compare-and-branch, read one key, loop with `DJNZ`, structure with
`CALL`/`RET`, and debug by observing state. The first game spends that fluency — it teaches *no new
machine primitives*, only how to compose them into a game.

## Pacing (one capability per unit; ~16 units)

Per the technique budget, **incremental within the game** (one capability per unit), **spiralling**
from the Primer. Same "feels manageable is correct" discipline — don't pack units to look busy.

---

## The units

### Phase A — A Room You Can See *(the world)*

**1 — Where a Cell Lives.** Resolve the screen-thirds layout (Primer cliff-hanger #1): a
`cell → screen address` helper. Draw one wall tile at *any* cell to prove the helper. *(The first
meaty unit — pace it; the interleaved address maths is the one genuinely fiddly idea, met once and
reused forever.)*
- Primitive: a `cell_addr(row,col)` routine; one 8×8 tile blit.

**2 — Four Walls.** Draw the room's wall border with a `DJNZ` loop over the helper. The room exists.
- Primitive: looped tile drawing.

**3 — The Room Is Data.** Store the room as a **tile map** in memory (one byte per cell:
wall / floor / gem); draw the room *from the map*. Change the map, the room changes.
- Primitive: a tile-map array + a draw-from-map routine.
- Forward-seed: this is the simple ancestor of Shadowkeep's room-as-data and collision map.

### Phase B — A Character in the Room *(the hero)*

**4 — A Face in Eight Bytes.** Design the hero as eight `defb` bytes; draw it at a cell taken from a
RAM position (`hero_row`, `hero_col`). Single-draw, no masking.
- Primitive: an 8-byte sprite; `draw_hero` from a RAM position.
- Forward-seed: single-draw → **masking** (Overlap, later).

**5 — Leave No Trail.** Save the cell under the hero before drawing; restore it when the hero
moves, so it leaves no smear. Cell-preservation.
- Primitive: `save_under` / `restore_under` (the cell behind the sprite).
- Forward-seed: the cell-snapped alternative to masking; reused throughout Shadowkeep.

### Phase C — Making It Move *(the loop + control — the two majors)*

**6 — The Heartbeat.** The **game loop** skeleton: `input → update → draw → repeat`, with frame
timing. The hero is still static; the loop simply runs each frame. *(Major #1.)*
- Primitive: the main loop + a per-frame wait.

**7 — All the Keys.** The full 8-half-row **keyboard matrix** (Primer cliff-hanger #2): read the
four movement keys (pressed = bit *clear*). *(Built on Primer Beat 8's one-key read.)*
- Primitive: reading multiple half-rows; a "which directions are held" result.

**8 — A Step at a Time.** Update `hero_row`/`hero_col` from the keys; redraw with save/restore.
Cell-snapped movement — the hero walks the grid. *(Major #2, core.)*
- Primitive: position update + redraw.
- Forward-seed: cell-snapped → **pre-shifted smooth** movement (Smooth Motion, later).

**9 — Walls Stop You.** Collision against the tile map: before a step, check the target cell;
refuse the move into a wall. Simple collision.
- Primitive: read the tile map at the target cell; gate the move.
- Forward-seed: reused and deepened as Shadowkeep's collision.

### Phase D — A Game, Not a Demo *(stakes + win)*

**10 — Treasure.** Step onto a gem cell to collect it: clear it from the map, redraw the cell empty.
- Primitive: detect gem at target; mutate the map; redraw.

**11 — A Blip.** A single-bit **beeper** click on pickup (reuses port $FE bit 4). The game makes a
sound. *(One small, satisfying primitive — not a music driver; that's Shadowkeep.)*
- Primitive: a short beeper tone routine.

**12 — How Many Left.** Show progress as **coloured cells** — one cell lit per gem collected —
reusing attributes from Primer Beat 6. *(No digit rendering; a numeric HUD is Shadowkeep's job.)*
- Primitive: an attribute-based progress strip.

**13 — You Win.** All gems collected → a win state: a message, a colour/border flourish. The game
can be *finished*.
- Primitive: win check after each pickup; a win screen.

**14 — Again?** Title → play → win → restart: a simple **state machine** wiring the whole thing
into a complete, replayable loop.
- Primitive: a state variable + dispatch.
- Forward-seed: the simple ancestor of Shadowkeep's title/play/victory loop.

**15 — Feel.** Frame-rate pacing so movement is deliberate, not twitchy (a `MOVE_INTERVAL`-style
step rate); a settled idle vs moving. The game *feels* right.
- Primitive: movement rate-limiting via a frame counter.

**16 — The Finished Room.** A final art + atmosphere pass *within cell-based limits* — the room
reads as designed, not as debug output. The deliberate "make it look finished" unit the old plan
never had.
- Primitive: tile/attribute polish; a designed first impression.

---

## Exit competencies (handoff to Shadowkeep)

After the tiny game, the learner can build a **complete single-screen cell-based game**: draw from
a tile map, place and move a cell sprite with save/restore, run a real game loop, read the full
keyboard, collide against a map, collect and win, drive a title/play/win state machine, make a
beeper blip, pace movement, and finish a room so it looks designed.

Shadowkeep then **scales this, not replaces it**: many rooms with flick transitions, attribute
lighting and mood, audio depth, the four-arc world — all on the cell-based foundation built here.
The learner reaches Shadowkeep having *already finished a game*, so Shadowkeep is ambition on a
solid base, not the place they learn to ship.

## Deferred on purpose (budget discipline — do not pull forward)

- **A moving enemy / NPC AI** → Shadowkeep Arc 2 ("A Presence in the Dark").
- **Multiple rooms / flick-screen transitions** → Shadowkeep.
- **Numeric score / HUD bar with digits** → Shadowkeep ("A Game Knows Itself").
- **Music / an SFX driver** → Shadowkeep (the blip here is one tone, not a driver).
- **Pre-shift / masking / Y-sort / sub-cell movement** → the rendering games (Smooth Motion →
  Overlap → Greypeak).

## Open for the author

- **Name / slug** — working "Strongroom"; a real inspired-by name when spec'd.
- **A lose condition?** Pure collect-and-win is the simplest complete game. A *step budget* (collect
  all gems within N moves; score = moves to spare) adds stakes and a reason to replay **without** a
  new major technique. Lean: ship pure first, offer the step-budget as a "Try this" or a later unit.
- **Gem count and room size** — small enough to win in well under a minute.
- **Thematic tie to Shadowkeep?** A hooded figure / keep / gold would pre-echo Shadowkeep and ease
  the transition; a neutral character keeps the two games independent. Author's call.
- **Unit split** — 16 is the working count; Units 1–2 or 13–14 could merge, but resist merging to
  "add weight."
