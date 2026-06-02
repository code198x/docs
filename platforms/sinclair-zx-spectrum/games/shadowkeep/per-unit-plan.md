# Shadowkeep — The Plan (re-paced, cell-based)

> **Re-paced 2026-05-29** per [`spectrum-assembly-gentle-ramp.md`](../../../../decisions/spectrum-assembly-gentle-ramp.md).
> Shadowkeep is now a **cell-based atmospheric flick-adventure** that **builds on the tiny first
> game**, not a from-scratch engine course. The advanced rendering Trunk (pre-shift / masking /
> Y-sort) is **gone from here** — relocated to the rendering games. The prior engine-first per-unit
> specs are preserved in git history (pre-2026-05-29). This is a re-paced **outline** (per-unit
> headlines + intent); full magazine-class unit prose is authored during build.

> *"The keep at night, complete. A place, then its inhabitants and identity. The first chapter of a longer game."*

> **Build status (2026-06-02): all 16 units authored and live — the Place is complete (Arc 1 done).**
> Sub-arc **1.1 Into the Keep** ✅ (A Hooded Figure · The First Hall · A Place to Move · The Keep's
> Hand), **1.2 A Keep of Rooms** ✅ (The Room Graph · Through the Doorway · The Hero Remembers ·
> Three Rooms), **1.3 Mood and Light** ✅ (Light and Shadow · Furnishings · Mood through Constraint ·
> A Keep with Character), **1.4 The Keep Has a Voice** ✅ (Footsteps and Doors · The Keep's Gold ·
> A Theme in One Voice · The Keep Stands). As-built closely follows the outline below; the chief
> addition was **bitmap dithering** as the stone-and-lighting technique (Units 2, 9–12). The Place is
> a finishable, replayable cell-based flick-adventure. **Deferred:** a video-capture-quality bump +
> recapture of the dither-heavy units (2, 3, 9–12) with crisp output.

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

## Module shape — Shadowkeep is a game across several modules

> **Added 2026-06-02.** Reconciles this plan with [`modules-not-games.md`](../../../../decisions/modules-not-games.md)
> and the no-fixed-counts stance in [`curriculum-structure.md`](../../../../decisions/curriculum-structure.md).

Per the module model, a game can be taught by **several modules**, and a *revisit* returns to it
after intervening games. Shadowkeep is **not one ~64-unit block** — it is a game whose chapters are
separate modules, each slotted into the lineup where the spiral wants it:

- **Module `shadowkeep` (pass 1) — *the Place.*** The module authored for October. Roughly **Arc 1**
  below: a multi-room, lit, atmospheric keep you explore and clear. Deliberately **an extension of
  Gloaming in technique** — it carries Gloaming's engine wholesale and adds, at most, the one or two
  majors a single module's budget allows (the flick-screen world, then atmosphere). A complete,
  winnable game on its own.
- **Later Shadowkeep revisit modules (pass 2, 3, …)** — each its own `game: shadowkeep` module,
  placed *after* intervening games, each carrying its own one-or-two majors:
  - *inhabitants* — cell-based NPCs, threat, lives (Arc 2's first half);
  - *identity* — the numeric HUD / digit rendering Gloaming deferred, room names, score (Arc 2's
    second half);
  - the **Arc 3–4** content — items that matter, multiple keeps, tape save/load, secrets & lore,
    atmospheric cycles, collection endings.

This is why pass 1 stays small: the per-game **1–2-majors budget** is honoured by making each
Shadowkeep chapter its own budget-sized module, not by cramming four arcs into one. The arc material
below is the **design backlog** for those modules — not a single module's unit list, and not a fixed
count. The "Arc N (Units X–Y)" and "four sub-arcs of four" labels that follow are **illustrative
structure, not targets**; the project holds no fixed unit counts.

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
old plan never had a unit for. Scope holds at roughly Arc 1–2's existing ambition,
re-weighted engine → atmosphere (the "32" is an illustrative marker, not a target — the project
holds no fixed unit counts; the budget freed by dropping the rendering Trunk goes to atmosphere and
polish, not new mechanics, per the 32-unit commitment's own drift trigger).

## October cut — "the start of Shadowkeep"

The October launch artefact is *opening + complete tiny game (Gloaming) + **the start of
Shadowkeep***. The "start of Shadowkeep" **is the pass-1 module — *the Place*** (Arc 1 below). How
much of pass 1 ships *by* October is the only open cut: the minimum is the keep established with its
hooded hero, two or three designed rooms, and working flick-screen transitions (the early sub-arcs)
— enough to show the flick-adventure *begin* at the atmosphere bar — with the rest of pass 1
following. Inhabitants, identity and Arcs 3–4 are **later revisit modules**, never part of the
October cut. (Author/Steve to confirm how much of pass 1 lands by October.)

## Conventions (unchanged from the prior plan)

- Each unit's **title is the design concept**; the **code primitive** sits beneath it.
- **Read-Alongside + Modern Equivalent** line per unit: a specific Atic Atac / Knight Lore moment
  the unit descends from, plus a modern game using the same design idea.
- Each unit meets the per-unit **Definition of Done** (compiles on pasmonext → SNA; runs on Emu198x;
  magazine-class prose; screenshots; audio captures where relevant; CodeFromFile refs; ≥2 "Try
  this"; "If it doesn't work"; vault refs resolve; headline + design concept explicit).

---

## Arc 1 — *Foundations and a Place* — **module `shadowkeep` (pass 1)**

*The foundations are the tiny game; this arc is **the Place** — turning that engine into the keep,
giving it rooms, light, mood and a voice. This is the pass-1 module: an extension of Gloaming in
technique, complete and winnable on its own.* The sub-arcs below are an illustrative shape, not a
unit count.

### Sub-arc 1.1 — Into the Keep (1–4) · *the tiny engine becomes Shadowkeep*
- **1 — A Hooded Figure.** The hero re-drawn as Shadowkeep's hooded thief (designed 8×8 sprite +
  idle), on the tiny game's `draw_hero`/save-restore. *Reuse + identity.*
- **2 — The First Hall.** One designed keep room at the atmosphere bar — varied wall/floor tiles, a
  composed layout (not the tiny game's debug room). **Stone is *dithered*** here: mixing INK and
  PAPER pixels in the bitmap yields perceived shades *between* the cell's two colours (e.g. black
  over blue → dim → dark slate by density), giving textured, properly dark stone that a flat
  attribute wash (Unit 1's deliberate "before") cannot. No engine change — Gloaming's save/restore
  already preserves the 8 bitmap bytes under the hero, so he walks over textured stone intact.
  *Reuse room-from-map; raise the art bar; introduce bitmap dithering.*
- **3 — A Place to Move.** Walk the hall: the tiny game's keyboard + cell movement + wall collision,
  now in the keep. *Reuse, confirm the engine carried over.*
- **4 — The Keep's Hand.** Tooling for the keep: a clean tile/attribute palette + the room-data
  format Shadowkeep's many rooms will share. *Sets up 1.2.*
- **Sub-arc major:** *consolidation + identity, with one new craft technique — **bitmap dithering**
  for textured, shaded stone (Unit 2), introduced gently here and exploited for lighting in 1.3.
  The deliberate gentle on-ramp into the bigger game.*

### Sub-arc 1.2 — A Keep of Rooms (5–8) · **flick-screen world** *(major)*
- **5 — The Room Graph.** Data for many rooms and how they connect (which room lies through each
  edge). *New: the world as a graph.*
- **6 — Through the Doorway.** Flick-screen transition: walk off an edge → load + draw the next
  room, hero re-enters from the opposite edge. *New: the flick-adventure core.*
- **7 — The Hero Remembers.** Hero position across rooms; the keep persists as you move through it.
- **8 — Three Rooms.** Two or three designed, connected rooms — a small keep you can explore.
- **Sub-arc major:** **multi-room world + flick transitions** (the defining flick-adventure mechanic).

### Sub-arc 1.3 — Mood and Light (9–12) · **atmosphere** *(major)*
- **9 — Light and Shadow.** Lighting on two axes: attribute *colour* per cell/region, and **dither
  density** (from Unit 2) varied by distance from a light — denser-to-black in the dark, sparser
  near a torch. Shading falls straight out of the stone technique. *New: atmosphere as a discipline.*
- **10 — Furnishings.** Decoration objects — pillars, altars, sconces — as non-blocking cell scenery
  that make a room *a place*.
- **11 — Mood through Constraint.** Dark rooms, lit pools, contrast — sense of place within the two-
  colours-per-cell limit, dither density buying the shades between them (the constraint *is* the
  vocabulary).
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

## Arc 2 — *Inhabitants and Identity* — **later revisit modules (pass 2+)**

> **Not pass 1, not October.** This material becomes one or two *later* `game: shadowkeep` revisit
> modules — *inhabitants* (NPCs, threat, lives) and *identity* (HUD, names, score) — slotted into
> the lineup after intervening games, each within its own 1–2-majors budget. It is the design
> backlog for those revisits, not the back half of a single Shadowkeep block.

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

## Arcs 3–4 — **further revisit modules (post-October)**

Unchanged in spirit by the re-pace — [`shadowkeep-four-arc-framing.md`](../../../../decisions/shadowkeep-four-arc-framing.md)
already specifies them as **cell-based-friendly** (items, multiple keeps, tape save/load, secrets &
lore, atmospheric cycles, collection endings — none need pre-shift/mask/Y-sort). Each becomes its
own later `game: shadowkeep` revisit module, building on the pass-1 Place. *Beyond the Walls*;
*The Greater World* — illustrative groupings, not fixed unit blocks.

## Deprecation-pair seeds (what later games upgrade)

- Cell-snapped movement (here) → **pre-shifted** smooth (Smooth Motion).
- Single-draw sprite + save/restore (here) → **masked** drawing (Overlap).
- Flat draw order (here) → **Y-sorted** depth + isometric (Greypeak).

These are *teaching moments across games*, motivated by the felt limits of Shadowkeep's cell-based
look — not refactors, and not something Shadowkeep itself should reach for.

## Open for the author

- **How much of pass 1 lands by October** — the whole Place, or the keep + flick-screen early
  sub-arcs with the rest following? (The module is `shadowkeep` pass 1 either way.)
- **Sub-arc 1.1** is deliberately consolidation (no new major) to ease from Gloaming into the bigger
  game — confirm that gentle on-ramp is wanted, or tighten 1.1 into 1.2 if it feels slack.
- **Where the revisit modules sit** — which intervening games precede *inhabitants* and *identity*
  in the lineup (the catalogue array is the source of truth for order).
- Full magazine-class per-unit prose, code samples, screenshots and audio captures are the
  **authoring** step, not done in this plan.
