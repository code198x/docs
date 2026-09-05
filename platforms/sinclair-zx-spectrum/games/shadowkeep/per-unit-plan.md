# Shadowkeep — The Plan (re-paced, cell-based)

> **Design material for review.** This existing game plan does not establish current project policy or implementation status. Apply the [project charter](../../../../PROJECT.md) when re-specifying it; retain useful mechanics and evidence, and replace superseded scope, quality or prerequisite assumptions.

> **Existing plan, re-paced 2026-05-29.** Reconcile with the [current sequence review](../../../../work.md#spectrum-sequences).
> Shadowkeep is now a **cell-based atmospheric flick-adventure** that **builds on the tiny first
> game**, not a from-scratch engine course. The advanced rendering Trunk (pre-shift / masking /
> Y-sort) is **gone from here** — relocated to the rendering games. The prior engine-first per-unit
> specs are preserved in git history (pre-2026-05-29). This is a re-paced **outline** (per-unit
> headlines + intent); full magazine-class unit prose is authored during build.

> *"The keep at night, complete. A place, then its inhabitants and identity. The first chapter of a longer game."*

> **Build status (2026-06-02): units 1–16 authored and live** — the Place explores, lights, sounds
> and *finishes*. As-shipped sub-arcs (numbering pre-dates the 2026-07-04 weave below, which
> reassigns 1.3 onward): **Into the Keep** ✅ (A Hooded Figure · The First Hall · A Place to Move ·
> The Keep's Hand), **A Keep of Rooms** ✅ (The Room Graph · Through the Doorway · The Hero Remembers ·
> Three Rooms), **Mood and Light** ✅ (Light and Shadow · Furnishings · Mood through Constraint · A
> Keep with Character), **The Keep Has a Voice** ✅ (Footsteps and Doors · The Keep's Gold · A Theme in
> One Voice · The Keep Stands). As-built closely follows the outline below; the chief addition was
> **bitmap dithering** as the stone-and-lighting technique (shipped Units 2, 9–12). **Deferred:** a
> video-capture-quality bump + recapture of the dither-heavy units with crisp output.
>
> **Existing Warden sequence:** the plan introduces the curse during construction rather than appending it after the finale. For this design, the objective, threat and failure response come together after the world exists (Sub-arc 1.3, units 9–12); atmosphere and audio then deepen the experience. This is a game-specific choice, not a universal definition of a game. The threat is a **curse, not combat**, as described in [the game brief](brief.md).
> The closed design is **prototype-proven** — winnable *and* losable, headless and deterministic (see
> [`design-stress-2026-07-04.md`](design-stress-2026-07-04.md) § Prototype verification).
>
> **What this re-opens.** Units **1–8 are unchanged** (the engine and the world). Units **9–19 are
> re-derived**: the old atmosphere sub-arc (shipped units 9–12) moves back to 13–16; the old audio +
> gold + theme + finale (shipped 13–16) redistribute (gold → new 9, SFX → 17, theme → 18, the
> win-loop that was unit 16 folds into new unit 11's win/lose state machine); the game-core units
> 10–12 are net-new. The warden is **lighting-agnostic** (its save/restore/draw preserve whatever
> stone sits under it, textured or lit), so it builds cleanly on the pre-lighting base and the
> atmosphere units layer on top without disturbing it. **Now authored and live** — each unit its
> own byte-identity-gated build, the Gloaming way. The old append-style "1.5 Hold Back the Dark"
> (units 17–22) is superseded by this weave.
>
> **Live (2026-07-05).** The weave is authored, verified, and **flipped live**. Units 9-19 rebuilt:
> the code chain (each seam byte-identical back to unit 8, every unit winnable *and* losable by
> memory-probed headless runs); 11 magazine-class MDX units with figures, gameplay video and beeper
> audio; the catalogue renumbered to **five** sub-arcs (adding **1.3 The keep is a game**, 9-12,
> with 1.4 Mood and Light at 13-16 and 1.5 The keep's voice at 17-19). The Place becomes a game at
> unit 11 and is fully contested by 12; atmosphere and voice deepen a thing that already plays.
> Per-unit `capture/manifest.json` recipes regenerate every still, clip and WAV via `capture.py`.
> `units.yaml` is the live source of truth for titles and order; this plan is the design record.

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

> **Added 2026-06-02.** Reconciles this plan with [Content model](../../../../website.md#content-and-navigation)
> and the no-fixed-counts stance in [Curriculum design](../../../../specifications/curriculum.md).

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
count. The "Arc N (Units X–Y)" and the sub-arc groupings that follow are **illustrative
structure, not targets**; the project holds no fixed unit counts.

## The premise shift — what changed

**Knowledge used by this existing plan.** Its starting engine comes from Gloaming. Explain these routines locally and provide access to their sources without assuming the reader attended that game: the cell→screen-address helper, room-as-data, a cell sprite with save/restore, the
game loop, the full keyboard matrix, cell-snapped movement, tile-map collision, a beeper blip, and a
title→play→win state machine.

**Shadowkeep reuses all of that and deepens it** (the spiral model: revisit and grow at the game
boundary). Its genuinely *new* work is what makes it a *place*:

| New to Shadowkeep | Sub-arc |
|---|---|
| Multi-room world + flick-screen transitions | 1.2 |
| The game core — the gold (want), the Warden (a second mover + deterministic patrol), contact = loss | 1.3 |
| Atmosphere — attribute lighting, mood, designed decoration | 1.4 |
| Audio depth — SFX driver + composed theme (beyond the blip) | 1.5 |
| Inhabitants *elaborated* — varied/multiple NPCs, the allies-as-lives economy | 2.1–2.2 |
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
  for textured, shaded stone (Unit 2), introduced gently here and exploited for lighting in 1.4.
  The deliberate gentle on-ramp into the bigger game.*

### Sub-arc 1.2 — A Keep of Rooms (5–8) · **flick-screen world** *(major)*
- **5 — The Room Graph.** Data for many rooms and how they connect (which room lies through each
  edge). *New: the world as a graph.*
- **6 — Through the Doorway.** Flick-screen transition: walk off an edge → load + draw the next
  room, hero re-enters from the opposite edge. *New: the flick-adventure core.*
- **7 — The Hero Remembers.** Hero position across rooms; the keep persists as you move through it.
- **8 — Three Rooms.** Two or three designed, connected rooms — a small keep you can explore.
- **Sub-arc major:** **multi-room world + flick transitions** (the defining flick-adventure mechanic).

### Sub-arc 1.3 — The Keep is a Game (9–12) · **the game core: want + threat + fail** *(major)*

> **Woven 2026-07-04** per [Current game quality requirements](../../../../PROJECT.md)
> and Steve's "weave it earlier." A game is **want + threat + fail** — those three assemble *here*,
> right after the world exists, so the Place is a game for most of its construction (not a coda after
> the finale). The threat is a **curse, not combat** (the no-combat anti-goal in
> [the game brief](brief.md) holds):
> caught, you join the sleepers, frozen mid-stride. Closed design **prototype-proven** and re-gated
> (win *and* loss) — see [`design-stress-2026-07-04.md`](design-stress-2026-07-04.md). Built on the
> pre-lighting rooms of 1.2; the Warden is lighting-agnostic, so 1.4's atmosphere layers on top of it.

- **9 — The Keep's Gold.** The **want**: gold scattered through the rooms, collect-all to clear the
  keep — and the win half of the loop, reused from the tiny game's title → explore → win → title
  state machine, scaled to the world (collect the last coin → THE KEEP STANDS → replay). *Reuse
  collect/win + the state machine; the goal that the threat will contest.* Read-Alongside: Atic Atac's
  treasure hunt.
- **10 — Something in the Dark.** The **threat**: the Warden — a spectral hooded sentinel with its own
  save / restore / draw and a private under-buffer (the two-mover shape the thief already uses, now a
  *second occupant*), walking a **deterministic patrol** — a row or column, reversing at walls, after
  a gather beat. A route you *learn and time* — Sabre Wulf's roaming beasts, **not** The Long Night's
  hunting dark (a patroller, not a hunter). *Reuse the two-mover; new: a second sprite with a designed
  spectral glyph, and patrol-movement state (propose-then-commit stepping).* Read-Alongside: Knight
  Lore's guardians · Sabre Wulf's patrol.
- **11 — Join the Sleepers.** The **fail**: contact is loss — the thief stepping toward the Warden
  *and* the Warden's step landing on the thief; the loop gains its lose arm (title → explore → win
  *or* lose → title); "THE KEEP SLEEPS" and a plunge-then-lock caught-sting. **This is the unit where
  the Warden threat gains its consequence** — a failure mechanic chosen for this design. *New: the
  fail state; the win/lose state machine complete.* Read-Alongside: Atic Atac (touched = lost).
- **12 — A Warden for Every Room.** From one Warden to a keep of them, **from data**: a warden table
  (start cell, route, axis per room), each room instantiating its Warden on entry — gathering **clear
  of the entry cell** so you never materialise onto it — and the **gold moved onto the routes** so
  reaching a coin means reading the patrol and taking the gap (contested ground, want-*against*-threat
  from the first placement, never taught safe-then-moved). *A second mover is a table entry — like
  Gloaming's lamps, like the torches. New: the per-room table + jeopardy-first level design.*
  Read-Alongside: Atic Atac's contested rooms.
- **Sub-arc major:** **the game core — a want, a deterministic threat that contests it across the
  keep, and a fail state. The Place is a game (playable, winnable, losable) from here.**

### Sub-arc 1.4 — Mood and Light (13–16) · **atmosphere** *(major)*

> The rooms of 1.1–1.3 carry textured *dithered stone* (Unit 2) but not yet lit modelling; this
> sub-arc lights the keep the Warden already haunts. (Shipped as units 9–12; renumbered by the 1.3
> weave — same content, now enriching a working game rather than an empty place.)

- **13 — Light and Shadow.** Lighting on two axes: attribute *colour* per cell/region, and **dither
  density** (from Unit 2) varied by distance from a light — denser-to-black in the dark, sparser
  near a torch. Shading falls straight out of the stone technique. *New: atmosphere as a discipline.*
- **14 — Furnishings.** Decoration objects — pillars, altars, sconces — as non-blocking cell scenery
  that make a room *a place*.
- **15 — Mood through Constraint.** Dark rooms, lit pools, contrast — sense of place within the two-
  colours-per-cell limit, dither density buying the shades between them (the constraint *is* the
  vocabulary).
- **16 — A Keep with Character.** Atmosphere applied across all rooms; each room reads as somewhere —
  and the Warden's patrol now reads *against* lit stone, the threat legible in the mood.
- **Sub-arc major:** **atmosphere — lighting, mood, designed decoration.**

### Sub-arc 1.5 — The Keep's Voice (17–19) · **audio depth + the sealed chapter** *(major)*
- **17 — Footsteps and Doors.** An **SFX driver** (beyond the tiny game's single blip): footsteps, a
  door creak, the gold's chime — sound as place, joining the caught-sting the loss already sounds.
  *New: audio depth.*
- **18 — A Theme in One Voice.** A composed **beeper theme** for the title — single-channel
  composition discipline.
- **19 — Stand or Sleep.** The **sealed chapter**: the title screen (hand-pixelled logo) over the
  complete title → explore → **win or lose** → title loop, re-gated with **both** endings (THE KEEP
  STANDS *and* THE KEEP SLEEPS) — the per-game winnability gate met properly (a scripted run to each
  ending in `capture/`). The game built at 1.3 is dressed and closed: **losable and winnable.**
- **Sub-arc major:** **audio depth + the sealed, re-gated first chapter.**

**End of Arc 1:** a complete, beautiful, cell-based multi-room flick-adventure — explore the keep,
collect the gold, **hold back the dark**, win *or* join the sleepers — with light, mood and sound.
A real game, because it can be lost — and a game for most of its build, not just its last unit.

---

## Arc 2 — *Inhabitants and Identity* — **later revisit modules (pass 2+)**

> **Not pass 1, not October.** This material becomes one or two *later* `game: shadowkeep` revisit
> modules — *inhabitants* (NPCs, threat, lives) and *identity* (HUD, names, score) — slotted into
> the lineup after intervening games, each within its own 1–2-majors budget. It is the design
> backlog for those revisits, not the back half of a single Shadowkeep block.

> **Re-scoped 2026-07-04 by Sub-arc 1.3.** Minimal jeopardy — *one* deterministic Warden and a fail
> state — now lands in **pass 1** (1.3 above, the game core), so 2.1–2.2 are no longer where threat
> *first* appears.
> They become the **elaboration**: 2.1 "Something Moves" widens the single Warden to varied,
> multiple, animated inhabitants (behaviour tables, an object list); 2.2 "A Presence in the Dark"
> replaces pass-1's one-hit-to-title with the **allies-as-lives economy** (the *Waking* vision —
> lives *are* rescued sleepers), respawn, and threat tied to the lighting. What 1.5 proves in the
> small, Arc 2 grows. Update 2.1's "A Presence" / "A Path of Its Own" and 2.2's "Caught" / "Lives and
> Loss" headlines at authoring time so they build *on* the Warden rather than re-introduce it.

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

The earlier plan proposes later modules that remain **cell-based-friendly** (items, multiple keeps, tape save/load, secrets &
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
