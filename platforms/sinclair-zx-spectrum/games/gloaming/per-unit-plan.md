# Gloaming — The Plan (the tiny first game)

> **Outline, 2026-06-01.** Derived from [`brief.md`](brief.md) and governed by
> [`spectrum-assembly-gentle-ramp.md`](../../../../decisions/spectrum-assembly-gentle-ramp.md).
> This is the per-unit **outline** — headlines, intent, and the one code primitive each unit
> introduces. Full magazine-class prose, the `.asm` listings (in `code-samples/`, referenced via
> `CodeFromFile`), screenshots and audio captures are the **authoring** step, not done here.

> *"Dusk in a small square. Light every lamp before the dark wins. The first game you finish in assembly."*

## Position in curriculum

**Volume 1, Game 1** of the Spectrum Assembly track — after the **Primer** ("Meet the Machine"),
before **Shadowkeep**. Gloaming is where the track's foundations are *born*; Shadowkeep and every
later assembly game **reuse** them (Shadowkeep's plan lists them as "carried in from the tiny game").
It teaches the two majors the gentle-ramp assigns it and nothing heavier — no pre-shift, no masking,
no Y-sort, no multi-room. One screen, one character, cells.

**Headline (Design Concept):** *Completion — "I finished a real game, in assembly."*
**Tradition:** Ultimate's 1983 single-screen line — *Jetpac*, *Pssst*, *Cookie*: small, finished, classic.

## October role

Unlike Shadowkeep (which ships only its *start* in October), **Gloaming ships complete** — it is the
"*complete* tiny first game" in the launch's assembly opening (Primer → **Gloaming** → start of
Shadowkeep), per [`october-2026-launch-spec.md`](../../../../decisions/october-2026-launch-spec.md).
A learner finishes a real assembly game by October.

## What Gloaming establishes (and who reuses it)

The inverse of Shadowkeep's "what's new" table — Gloaming *invents* the primitives:

| Primitive (born here) | Unit | Reused / upgraded by |
|---|---|---|
| Attribute memory + the map as data | 1 | every game; Shadowkeep's rooms |
| Cell→screen-address helper + 8×8 glyph draw | 2 | every sprite, everywhere |
| The frame-locked game loop (**major 1**) | 3 | every game |
| Keyboard half-row scan (`IN A,($FE)`) | 4 | every game |
| Cell sprite + 9-byte save/restore + cell collision (**major 2**) | 5–7 | Shadowkeep; *Overlap* upgrades it to masking |
| Coloured-cell (pip) progress readout | 11 | Shadowkeep upgrades to **digit** HUD |
| Title → play → win/lose → title state machine | 16, 19 | every game |
| Single beeper blip | 17 | Shadowkeep upgrades to an SFX driver + theme |

## Conventions (as the rest of the track)

- Each unit's **title is the design concept**; the **code primitive** sits beneath it.
- **Read-Alongside + Modern Equivalent** line per unit (authored in build): a specific 1983
  single-screen moment it descends from, plus a modern game using the same idea.
- Each unit meets the per-unit **Definition of Done**: assembles on **pasmonext → `.sna`**; runs on
  **Emu198x** (script-mode capture); magazine-class prose; ≥1 verified screenshot; `CodeFromFile`
  refs exist + assemble; ≥2 "Try this"; "If it doesn't work"; vault refs resolve.
- **British English**; warm, technical, never condescending. **Always-runnable**: the reader can run
  the project after every unit.

---

## Phase A — A character on a screen (Units 1–4) · *the loop begins*

*Each light: one idea, a trivial task. "Feels easy" is correct here.*

- **1 — The Empty Square.** Write the attribute grid (cobbles, walls) straight to attribute memory —
  `attr = $5800 + row*32 + col`. The screen *is* the map; one attribute write, one cell. *New: attribute memory; the map as data.*
- **2 — The Lamplighter.** Draw an 8×8 glyph into one cell: the **cell→screen-address helper** (the Spectrum's non-linear bitmap layout; 8 bytes down a cell at +256 stride) copying a sprite definition. *New: the cell→screen helper; drawing a glyph.*
- **3 — The Heartbeat.** The structured loop: `IM 1` + `HALT` locks to the 50 Hz frame; an empty input→update→draw skeleton that just holds steady. *New: the frame-locked game loop **(major 1)**.*
- **4 — Reading the Keys.** Scan one keyboard half-row with `IN A,($FE)` (active-low bits 0–4); detect a direction press. One half-row, one idea. *New: keyboard input.*

## Phase B — Honest movement (Units 5–8) · **cell sprite + save/restore + collision** *(major 2)*

- **5 — One Step.** On a key press, erase the old cell and draw at the new one — the glyph moves cell-by-cell. It works because the floor is blank; *name that assumption out loud.* *New: cell-step movement.*
- **6 — Save and Restore.** Before drawing the lamplighter, save the 8 bitmap bytes + 1 attribute (9 bytes) beneath it; restore on leaving. Movement now survives over *any* cell. *New: 9-byte save/restore — the naive preservation, flagged as the "before" of masking.*
- **7 — Walls.** Read the **attribute of the target cell** and `BIT`-test its type; a wall refuses the step. Collision is a bit-test on the attribute byte. *New: cell-type collision.*
- **8 — Edges.** Bounds — stay inside the square. *Consolidation; the engine is complete.*

## Phase C — The game (Units 9–12) · **rules, score, win**

- **9 — The Lamps.** Place unlit lamps as cells (lantern glyph, cyan attribute) from a small data table. *New: game objects as cell data.*
- **10 — Light It.** Step onto an unlit lamp; mark it lit by setting its *stored* attribute to BRIGHT yellow, so save/restore leaves it glowing behind you. The background under the sprite is **state you control**. *New: collision-as-rule; persistent cell state.*
- **11 — The Tally.** A pip bar — one cell per lamp — brightening as you light, mirrored in the HUD row. Coloured-cell progress, **not** rendered digits (that's Shadowkeep's major; this is the "before"). *New: a visual readout.*
- **12 — Nightheld.** All lamps lit → the win state + a closing line (ROM-font string); the square holds the dark. *New: win condition + end state.*

*By unit 12 the learner has a complete, winnable game.*

## Phase D — Jeopardy (Units 13–15) · **the draught, lives, lose-state**

*Within budget: the draught is a **second** cell-sprite driven by the Phase-B major used again — game design, not a new engine technique.*

- **13 — The Draught.** A cold wisp: a second cell sprite drawn with the same save/restore, stepping each frame by a simple patrol rule (per-object position state). *Reuse the cell-sprite major for a second entity; new: a moving non-player object.*
- **14 — It Snuffs the Light.** When the draught reaches a lit lamp, set it unlit again (cold cyan) — the dark pushes back, and routing matters. *New: entity-vs-world interaction.*
- **15 — Lives, and the Fall of Night.** Hero-vs-draught cell-overlap test → lose a life (a pip removed); out of lives → "night falls", the lose state. *New: lives + lose-state — the stakes the game needed.*

## Phase E — Make it finished (Units 16–20) · **polish + real hardware**

*Supporting craft; the cut hierarchy trims here first, never the bar.*

- **16 — The Title.** A "GLOAMING" title screen (sparse, suggestive — *Hobbit*-style); press a key to begin. Wires the **title → play → win/lose → title** state machine. *New: the game's state machine.*
- **17 — A Small Sound.** A beeper blip via `OUT ($FE),A` bit 4 when a lamp lights; a colder note when one is snuffed. *New: beeper SFX — a single blip, the "before" of an SFX driver.*
- **18 — The Square Warms.** Atmospheric attribute touches as light spreads — the first taste of mood Shadowkeep makes its whole craft. *Reuse attributes; raise the atmosphere bar.*
- **19 — Again.** Win *or* lose → back to the title; the loop closes, as a real game's does. *Consolidate the state machine.*
- **20 — On Real Iron.** Verify end-to-end on **Spectrum Next** (and a 48K `.sna`/`.tzx`); DoD item #4. *New: hardware truth.*

**End of Gloaming:** a complete, polished, period-faithful single-screen game with a loop, a moving
character, collision, a goal, a score, a moving threat, lives, a lose-state, sound, atmosphere, a
title, and a play-again loop — finished, and verified on real hardware. *"I finished a game, in assembly."*

---

## Deprecation-pair seeds (what Gloaming plants for later games)

Gloaming is the **root of the track's deprecation tree** — the honest, felt "before" of each later upgrade:

- Cell-step movement (here) → **pre-shifted** smooth movement (*Smooth Motion*).
- Single-draw glyph + save/restore (here) → **masked** drawing (*Overlap*).
- Coloured-pip progress (here) → rendered **digit** HUD (*Shadowkeep*).
- A single beeper blip (here) → **SFX driver + composed theme** (*Shadowkeep*).
- One screen (here) → **multi-room flick** world (*Shadowkeep*); flat draw order → **Y-sort + iso** (*Greypeak*).

These are teaching moments *across games*, motivated by Gloaming's felt limits — not something Gloaming itself should reach for (the drift-trigger guard).

## Open for the author

- **The draught's patrol** — fixed path, bounce-off-walls, or a gentle drift toward the nearest lit lamp? (Keep it simple — no pursuit AI; the gentle-ramp forbids reaching past the budget.)
- **Lamp count & layout** — ~8 is the working figure; final count and the square's wall layout are a level-design pass (counts are illustrative, never a target).
- **Title art** — hand-pixelled "GLOAMING" logo, or ROM-font set on a dark suggestive screen? Either is period-true; the logo is the richer choice if the budget allows.
- **Unit count** — ~20 here is an illustrative marker; phases may merge or split during authoring as the prose decides, provided the two-major budget holds and a finished game lands well before the count runs out.
