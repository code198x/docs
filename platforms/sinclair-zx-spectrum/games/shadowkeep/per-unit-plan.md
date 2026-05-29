# Shadowkeep — The Plan (re-paced, cell-based)

> **Re-paced 2026-05-29** per [`spectrum-assembly-gentle-ramp.md`](../../../../decisions/spectrum-assembly-gentle-ramp.md).
> Shadowkeep is now a **cell-based atmospheric flick-adventure** that **builds on the tiny first
> game**, not a from-scratch engine course. The advanced rendering Trunk (pre-shift / masking /
> Y-sort) is **gone from here** — relocated to the rendering games. The prior engine-first per-unit
> specs are preserved in git history (pre-2026-05-29). This is a re-paced **outline** (per-unit
> headlines + intent); full magazine-class unit prose is authored during build.

> *"The keep at night, complete. A place, then its inhabitants and identity. The first chapter of a longer game."*

## Position in curriculum

**Volume 1, Game 2** of the Spectrum Assembly track — immediately after the Primer + tiny first
game, and **before** the rendering games (Smooth Motion → Overlap → Greypeak). The order is
deliberate: Shadowkeep is the cell-based flick-adventure, and the rendering games later *upgrade*
its look once the learner has felt the limits of cell-snapped movement and single-draw sprites
(the deprecation-pair pedagogy). The gentle-ramp lineup table is the source of truth for numbering.

**Headline (Design Concept):** *Atmosphere (Sense of Place).*
**Tradition:** the flick-adventure — Atic Atac, Knight Lore, Sabre Wulf, Pentagram, Underwurlde.
**Engine:** cell-based throughout. Cell-snapped movement, single-draw sprites with save/restore,
attribute-driven lighting, tile-map collision — every one of these **carried in from the tiny game**.

## The premise shift — what changed

**Shadowkeep no longer teaches the foundations.** The tiny first game
([`../first-game/outline.md`](../first-game/outline.md)) already taught, and the learner has
already shipped: the cell→screen-address helper, room-as-data, a cell sprite with save/restore, the
game loop, the full keyboard matrix, cell-snapped movement, tile-map collision, a beeper blip, and a
title→play→win state machine.

**Shadowkeep reuses all of that and deepens it** (the spiral model: revisit and grow at the game
boundary). Its genuinely *new* work is what makes it a *place*:

| New to Shadowkeep | Sub-arc |
|---|---|
| Multi-room world + flick-screen transitions | 1.2 |
| Atmosphere — attribute lighting, mood, designed decoration | 1.3 |
| Audio depth — SFX driver + composed theme (beyond the blip) | 1.4 |
| Inhabitants — cell-based NPCs, threat, lives | 2.1–2.2 |
| Identity — numeric HUD, room names, score persistence | 2.3 |
| Completion — polish, audio depth, hardware, presentation | 2.4 |

**Removed and relocated** (do not teach in Shadowkeep): pixel-level/pre-shifted movement → *Smooth
Motion*; masked sprite drawing → *Overlap*; Y-sorted layered rendering → *Greypeak*. The freed
budget goes into **atmosphere, more designed rooms, and polish** — the "make it beautiful" work the
old plan never had a unit for. Unit count stays at 32 for Arcs 1–2 (per the 32-unit commitment's
own drift trigger: surplus goes to polish, not new units), re-weighted engine → atmosphere.

## October cut — "the start of Shadowkeep"

The October launch artefact is *opening + complete tiny game + **the start of Shadowkeep***. Proposed
October slice: **sub-arcs 1.1–1.2 (units 1–8)** — the keep established with its hooded hero, two or
three designed rooms, and working flick-screen transitions. That shows the flick-adventure *begin*
at the atmosphere bar. Arc 1.3 onward is post-October. (Author/Steve to confirm the exact cut.)

## Conventions (unchanged from the prior plan)

- Each unit's **title is the design concept**; the **code primitive** sits beneath it.
- **Read-Alongside + Modern Equivalent** line per unit: a specific Atic Atac / Knight Lore moment
  the unit descends from, plus a modern game using the same design idea.
- Each unit meets the per-unit **Definition of Done** (compiles on pasmonext → SNA; runs on Emu198x;
  magazine-class prose; screenshots; audio captures where relevant; CodeFromFile refs; ≥2 "Try
  this"; "If it doesn't work"; vault refs resolve; headline + design concept explicit).

---

## Arc 1 — *Foundations and a Place* (Units 1–16)

*The foundations are the tiny game; this arc is **the Place** — turning that engine into the keep,
giving it rooms, light, mood and a voice.* Four sub-arcs of four.

### Sub-arc 1.1 — Into the Keep (1–4) · *the tiny engine becomes Shadowkeep*
- **1 — A Hooded Figure.** The hero re-drawn as Shadowkeep's hooded thief (designed 8×8 sprite +
  idle), on the tiny game's `draw_hero`/save-restore. *Reuse + identity.*
- **2 — The First Hall.** One designed keep room at the atmosphere bar — varied wall/floor tiles, a
  composed layout (not the tiny game's debug room). *Reuse room-from-map; raise the art bar.*
- **3 — A Place to Move.** Walk the hall: the tiny game's keyboard + cell movement + wall collision,
  now in the keep. *Reuse, confirm the engine carried over.*
- **4 — The Keep's Hand.** Tooling for the keep: a clean tile/attribute palette + the room-data
  format Shadowkeep's many rooms will share. *Sets up 1.2.*
- **Sub-arc major:** *(none new — consolidation + identity; this is the deliberate gentle on-ramp
  into the bigger game.)*

### Sub-arc 1.2 — A Keep of Rooms (5–8) · **flick-screen world** *(major)*
- **5 — The Room Graph.** Data for many rooms and how they connect (which room lies through each
  edge). *New: the world as a graph.*
- **6 — Through the Doorway.** Flick-screen transition: walk off an edge → load + draw the next
  room, hero re-enters from the opposite edge. *New: the flick-adventure core.*
- **7 — The Hero Remembers.** Hero position across rooms; the keep persists as you move through it.
- **8 — Three Rooms.** Two or three designed, connected rooms — a small keep you can explore.
- **Sub-arc major:** **multi-room world + flick transitions** (the defining flick-adventure mechanic).

### Sub-arc 1.3 — Mood and Light (9–12) · **atmosphere** *(major)*
- **9 — Light and Shadow.** Attribute-driven lighting: mood through colour per cell/region (the
  decoupled attribute layer the tiny game met as colour). *New: atmosphere as a discipline.*
- **10 — Furnishings.** Decoration objects — pillars, altars, sconces — as non-blocking cell scenery
  that make a room *a place*.
- **11 — Mood through Constraint.** Dark rooms, lit pools, contrast — sense of place within the 8×8
  attribute limit (the constraint *is* the vocabulary).
- **12 — A Keep with Character.** Atmosphere applied across all rooms; each room reads as somewhere.
- **Sub-arc major:** **atmosphere — lighting, mood, designed decoration.**

### Sub-arc 1.4 — The Keep Has a Voice (13–16) · **audio + the complete chapter** *(major)*
- **13 — Footsteps and Doors.** An **SFX driver** (beyond the tiny game's single blip): footsteps,
  a door creak — sound as place. *New: audio depth.*
- **14 — The Keep's Gold.** The goal across the keep: collect the gold scattered through the rooms;
  a win when the keep is cleared. *Reuse collect/win; scale to the world.*
- **15 — A Theme in One Voice.** A composed **beeper theme** for the title — single-channel
  composition discipline.
- **16 — The Keep Stands.** Title screen (hand-pixelled logo) + the complete title → explore → win →
  title loop for the multi-room keep.
- **Sub-arc major:** **audio depth + the complete first-chapter loop.**

**End of Arc 1:** a complete, beautiful, cell-based multi-room flick-adventure — explore the keep,
collect the gold, win — with light, mood and sound. A real game.

---

## Arc 2 — *Inhabitants and Identity* (Units 17–32)

*The keep is no longer empty, and the game knows itself. All cell-based — NPCs move cell-by-cell,
drawn single-pass with save/restore (no masking; that's Overlap, a later game).*

### Sub-arc 2.1 — Something Moves (17–20) · **cell-based NPC** *(major)*
- **17 — A Presence.** A cell-based moving NPC: drawn with save/restore, stepping cell-by-cell.
- **18 — A Path of Its Own.** A patrol pattern (per-object movement state) — the NPC walks the keep.
- **19 — Two of a Kind.** A second NPC instance — a small object list (cell-based, no Y-sort).
- **20 — The Keep Breathes.** Idle/animation variety as *mood*, not just motion.
- **Sub-arc major:** **cell-based inhabitants in motion.**

### Sub-arc 2.2 — A Presence in the Dark (21–24) · **threat + lives** *(major)*
- **21 — Caught.** Hero-vs-NPC collision (cell overlap test).
- **22 — Lives and Loss.** Lives, loss, respawn — stakes.
- **23 — Danger in the Dark.** Threat tied to the lighting — the dark rooms become dangerous.
- **24 — Behaviour and Variation.** A second behaviour table — varied threat, hand-authored.
- **Sub-arc major:** **threat + lives.**

### Sub-arc 2.3 — A Game Knows Itself (25–28) · **identity / HUD** *(major)*
- **25 — The Readout.** A numeric **HUD** (gold / lives) — **digit rendering** (deferred from the
  tiny game's coloured-cell progress; now done properly). *New: digits.*
- **26 — Names of Places.** Room names — the keep's geography named.
- **27 — A Best Yet.** Best-score persistence.
- **28 — Room-Graph + Theming.** The room-graph data structure + per-room theming, deepened (seeds
  Arc 3.2 and later games' load-bearing techniques).
- **Sub-arc major:** **identity — HUD, names, score.**

### Sub-arc 2.4 — Completion (29–32) · **polish** *(major)*
- **29 — Every Room a Place.** Atmosphere polish across all rooms.
- **30 — A Fuller Voice.** Audio depth — SFX library expansion + music polish.
- **31 — On Real Iron.** Spectrum Next + TZX 48K hardware testing.
- **32 — Completed.** Final presentation — title art, victory sequence, "completed" state.
- **Sub-arc major:** **completion + polish discipline.**

**End of Arc 2:** a complete cell-based flick-adventure with inhabitants, threat, lives, a HUD,
identity, atmospheric polish, and verified real-hardware playability.

---

## Arcs 3–4 (post-October)

Unchanged in spirit by the re-pace — [`shadowkeep-four-arc-framing.md`](../../../../decisions/shadowkeep-four-arc-framing.md)
already specifies them as **cell-based-friendly** (items, multiple keeps, tape save/load, secrets &
lore, atmospheric cycles, collection endings — none need pre-shift/mask/Y-sort). They build on this
re-paced Arc 1–2 foundation. Arc 3 *Beyond the Walls* (33–48); Arc 4 *The Greater World* (49–64).

## Deprecation-pair seeds (what later games upgrade)

- Cell-snapped movement (here) → **pre-shifted** smooth (Smooth Motion).
- Single-draw sprite + save/restore (here) → **masked** drawing (Overlap).
- Flat draw order (here) → **Y-sorted** depth + isometric (Greypeak).

These are *teaching moments across games*, motivated by the felt limits of Shadowkeep's cell-based
look — not refactors, and not something Shadowkeep itself should reach for.

## Open for the author

- **October cut** — is 1.1–1.2 (units 1–8) the right "start of Shadowkeep" for October, or fewer/more?
- **Sub-arc 1.1** is deliberately consolidation (no new major) to ease from the tiny game into the
  bigger game — confirm that gentle on-ramp is wanted, or tighten 1.1 into 1.2 if it feels slack.
- **Volume position** — Shadowkeep is "Game 1" by theme but reached after the opening + rendering
  inserts; confirm how the lineup numbers it (the gentle-ramp lineup table is the source of truth).
- Full magazine-class per-unit prose, code samples, screenshots and audio captures are the
  **authoring** step, not done in this re-pace.
