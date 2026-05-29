# Shadowkeep — The 32-Unit Plan

> **SUPERSEDED IN PART, 2026-05-29 — pending re-pace. See [spectrum-assembly-gentle-ramp.md](../../../../decisions/spectrum-assembly-gentle-ramp.md).**
> Shadowkeep is re-scoped to a **cell-based atmospheric** flick-adventure. The pre-shifted-sprite,
> masked-drawing and Y-sorted-rendering units below (notably sub-arcs 1.2–1.3) are **removed** —
> those techniques relocate to later games (Smooth Motion → Overlap → Greypeak). A learner now
> reaches Shadowkeep already onboarded by the Primer + a tiny first game. The full unit-by-unit
> re-pace to cell-based atmosphere is downstream content work and **not yet applied**; treat the
> plan below as the superseded engine-first version until that re-pace lands.

The canonical reference for Shadowkeep's October 2026 launch deliverable. Anchored to [`docs/decisions/shadowkeep-32-unit-commitment.md`](../../../../decisions/shadowkeep-32-unit-commitment.md) and extended by [`docs/decisions/shadowkeep-four-arc-framing.md`](../../../../decisions/shadowkeep-four-arc-framing.md) (Arcs 3-4, post-October).

> *"The keep at night, complete. Foundations, a place, inhabitants, identity. The first chapter of a longer game."*

## Position in curriculum

**Volume 1, Game 1** of the Spectrum Assembly track (per [`docs/decisions/spectrum-assembly-track.md`](../../../../decisions/spectrum-assembly-track.md)). The flick-adventure tradition — descends from Atic Atac, Knight Lore, Sabre Wulf, Pentagram, Underwurlde.

**Headline (Design Concept):** *Atmosphere (Sense of Place).*

Every unit in Shadowkeep traces back to this headline. Atmosphere is what the player feels; Sense of Place is the generalizable design concept; the techniques (Y-sort rendering, masking, lighting, pre-shifted sprites, etc.) are how the engine delivers it.

## Shape

32 units in two arcs of 16. Each arc in four sub-arcs of four. Each sub-arc has a thematic identity; each unit has a single specific contribution.

```
Arc 1 — Foundations and a Place         Arc 2 — Inhabitants and Identity
─────────────────────────────           ──────────────────────────────
1.1  First Pixels       (1-4)           2.1  Sound and Motion      (17-20)
1.2  The Hooded Thief   (5-8)           2.2  A Presence in the Dark (21-24)
1.3  A World with Depth (9-12)          2.3  A Game Knows Itself   (25-28)
1.4  The Keep Stands    (13-16)         2.4  Completion            (29-32)
```

## Reference points

The work is calibrated against, in order of relevance:

- **[Atic Atac](/vault/games/atic-atac)** (Ultimate, 1983) — multi-room adventure with Y-sorted layered rendering; the engine archetype.
- **[Knight Lore](/vault/games/knight-lore)** (Ultimate, 1984) — atmospheric monochrome, masked sprite, animated character; the mood archetype.
- **[Cybernoid II](/vault/games/cybernoid)** (Hewson, 1988) — dense visual design, hand-crafted level art, [Tim Follin](/vault/people/tim-follin) music; the polish archetype.
- **[The Hobbit](/vault/games/the-hobbit)** (Melbourne House, 1982) — economical title presentation, sparse but suggestive; the opening-screen archetype.

## Engine commitments

Three fundamental changes from the prior 8-unit slice's engine:

1. **Pixel-level sprite movement.** Hero moves 2 or 4 pixels per frame. Pre-shifted sprite tables (8 versions per sprite, one per X-offset 0-7). Masked sprite drawing preserves background pixels.
2. **Back-to-front layered rendering.** Y-sorted object list, drawn each frame. Hero passes behind/in-front of pillars depending on Y.
3. **Decoupled attribute / collision.** Collision lives in a separate tile-map structure. Attribute area is purely cosmetic — used for lighting and decoration.

These are introduced *progressively* across Arc 1 — the curriculum *teaches* the engine evolution, not just uses it.

---

## Arc 1 — Foundations and a Place

End-of-arc deliverable: a complete two-room game (Great Hall + Antechamber). Hand-pixelled tiles. Hooded thief animated with weight. Pillars the hero walks behind. Atmospheric lighting near torches. Gold cells with sparkle. A composed title theme. Hand-pixelled title artwork. Title→play→victory→title loop.

### Sub-arc 1.1 — First Pixels (Units 1-4)

*Thematic identity: the keep takes shape, one designed tile at a time.*

#### Unit 1 — *A pixel in the dark*

**Design concept:** *The framebuffer as canvas* — the Spectrum's bitmap is geography, addressable to the byte. Every pixel has a coordinate; every coordinate has a pixel.

**Read alongside:** Atic Atac's title-screen colour cascade (Ultimate's first byte-level pixel work — colours sweeping across the keep silhouette).

**Modern equivalent:** Pico-8's `pset(x, y, c)` — the smallest unit of "draw" is the same primitive, four decades on.

**Contribution:** First framebuffer write. Direct byte poke at one screen address. The Spectrum bitmap layout introduced.

**Code primitive:** `LD A, value / LD ($4045), A` (single pixel at row 0, col 5).

**Art deliverable:** None — this unit teaches the framebuffer mechanic with single bytes.

**Inherits from:** existing Unit 1 (mostly intact, MDX prose largely survives).

#### Unit 2 — *The first stone*

**Design concept:** *Composition begins* — the first deliberate tile is the first design choice. Stone is not just stone; it's stone *as the designer drew it*.

**Read alongside:** Atic Atac's stone-wall tile (the moss-and-mortar detailing that establishes the haunted-house mood within the first room).

**Modern equivalent:** Stardew Valley's tilesets — every tile is a designed unit, not a procedural texture; the artist's hand visible in each.

**Contribution:** One properly-designed 8×8 stone tile. Hand-pixelled — real stonework patterns (block edges, mortar shadows, occasional cracks or moss). Drawn at one cell.

**Code primitive:** `draw_tile_at(row, col, tile_id)` — bitmap copy with the address-computing bit-twiddle.

**Art deliverable:** *Stone tile #1* — the canonical wall tile. ~30 minutes of pixel work; multiple iterations to land.

**Replaces:** existing Unit 2's stippled stone block.

#### Unit 3 — *Walls that vary*

**Design concept:** *Variety as character* — repetition reads as flatness; variation reads as place. Walls become walls *because* they vary.

**Read alongside:** Atic Atac's per-room tile palette (kitchen, library, attic — each room reads as different because its tiles vary).

**Modern equivalent:** Celeste / Hollow Knight tilesets per area — variety established through tile-set switching as the player traverses regions.

**Contribution:** Multiple tile types — plain stone, decorated stone (carved relief), corner pieces, arched lintel. Drawn from a tile-id index. The great hall takes shape with character.

**Code primitive:** Tile-id-keyed dispatch in the renderer. Tile data table at a fixed address.

**Art deliverables:** *Stone tile #2-5* — at minimum a corner-piece tile, a decorated wall tile, and an arched-lintel tile. Each unique, hand-pixelled.

**Replaces:** existing Unit 2's loop-rendering approach (which only knew one tile).

#### Unit 4 — *A room as data*

**Design concept:** *Decoupling* — separating concerns is what lets each evolve. Tile-map holds *what's there*; attribute holds *how it looks*. The two are no longer the same byte.

**Read alongside:** how Atic Atac packed 50+ rooms into 48K — the compact tile-map data structure that made the keep possible at all.

**Modern equivalent:** Tiled (the level editor) and every modern engine's separate level-data / visual-rendering split (Unity Tilemaps, Godot TileMaps).

**Contribution:** Tile-map data structure, separated from attribute bytes. Multiple cell types renderable from a single data table. Foundations for Arc 1.3's lighting (attributes free for decoration) and Arc 1.4's collision (read from tile-map, not attribute).

**Code primitive:** `room_data[]` byte array; `draw_room()` walks it and dispatches to tile renderers. **`attr_data[]` becomes purely cosmetic** — set independently from tile-map.

**Art deliverable:** The Great Hall room composed properly — tiles placed for atmosphere, not just functionally. Columns hinted, central altar area established (decoration comes in 1.3).

**Replaces:** existing Unit 3's room rendering (which used cell-aligned attribute as the source of truth).

---

### Sub-arc 1.2 — The Hooded Thief (Units 5-8)

*Thematic identity: a character with weight.*

#### Unit 5 — *The hooded thief*

**Design concept:** *Identity in silhouette* — an 8×8 sprite must read on a magazine cover. Character is what survives extreme reduction.

**Read alongside:** Sabreman's silhouette in Sabre Wulf — the distinctive hat-and-robe shape that became Ultimate's signature character at tiny resolution.

**Modern equivalent:** Hyper Light Drifter's protagonist sprite — silhouette-first design where character identity reads from the outline alone.

**Contribution:** One designed hero sprite. Hand-pixelled hooded figure — hood-and-cloak silhouette, posture suggesting stealth, distinctive enough to read on a magazine cover at 8×8.

**Code primitive:** `draw_hero(row, col)` — bitmap-copy a single 8-byte sprite to a cell-aligned position. Same primitive as `draw_tile`.

**Art deliverable:** *The thief, one frame.* The defining sprite of the game. Multiple iterations expected; this is the single most-load-bearing piece of pixel art.

**Replaces:** existing Unit 3's static stick-figure hero.

#### Unit 6 — *He walks*

**Design concept:** *Weight through motion* — the walk cycle is character. Four frames carry posture, mass, intent.

**Read alongside:** Sabreman's walk in Sabre Wulf — the weight transfer rendered in 4 frames at 8×8, defining how a hero *moves through* space.

**Modern equivalent:** Hollow Knight's Knight walk cycle — character-as-animation; the walk is the personality.

**Contribution:** Four-frame walk cycle. Animation logic — frame index advances per movement step. Idle frame when stationary.

**Code primitive:** `hero_frame` byte; animation state machine; frame-data table (5 frames × 8 bytes = 40 bytes).

**Art deliverable:** *The thief, walk cycle.* Four frames showing weight transfer — foot down, mid-step, foot down, mid-step. Plus the idle frame. The hardest piece of pixel work in Arc 1.

#### Unit 7 — *Sub-cell*

**Design concept:** *Fluidity* — pixel-level positioning is what makes motion feel real. The 8-pixel-jump betrays the grid; 2-pixel motion makes it disappear.

**Read alongside:** Cybernoid II's player ship — pixel-accurate movement at 50Hz; Crow's masterclass in making the ship feel weightless yet precise.

**Modern equivalent:** Celeste's pixel-perfect movement — sub-pixel positioning still matters when the player can feel a single-pixel difference.

**Contribution:** Pixel-level positioning. Hero moves 2 pixels per frame (or 4, depending on tuning), not 8. Pre-shifted sprite tables — eight versions of the hero sprite, one per X-offset 0-7.

**Code primitive:** Pre-shifted sprite tables generated at assembly time. `draw_hero_at_pixel(pixel_row, pixel_col)` selects the right shifted version based on `col & 7`.

**Art deliverable:** Re-export of the walk cycle into pre-shifted form. (Done by tooling, not by hand; but the tooling is built this unit.)

**Replaces:** existing Unit 4's cell-snapped movement.

#### Unit 8 — *Sprite that hides*

**Design concept:** *Presence without footprint* — the character is *in* the keep, not on top of it. Masked sprite drawing preserves what was there; the hero passes through without erasing.

**Read alongside:** Knight Lore's iso hero passing through doors — the masking that lets the player navigate complex backgrounds without trail or smear.

**Modern equivalent:** any 2D engine's alpha channel — masking is the same idea at hardware support; Pico-8's transparent palette index honours the spirit.

**Contribution:** Masked sprite drawing. Two-bitmap approach — mask (AND with screen to clear) and image (OR over screen to paint). Hero preserves background pixels behind him; no trail.

**Code primitive:** `draw_hero_masked` — for each sprite byte, `AND mask_byte` then `OR image_byte`. Two passes per row.

**Art deliverable:** Mask version of each hero frame — generated by tooling from the image data (mask = "where is the sprite opaque").

---

### Sub-arc 1.3 — A World with Depth (Units 9-12)

*Thematic identity: the keep becomes a place.*

#### Unit 9 — *Behind the column*

**Design concept:** *Depth* — Y-sort gives 2D pixels a three-dimensional reading. The keep gains a *behind* and an *in front of*.

**Read alongside:** Atic Atac's hero walking behind room features (chests, doors, candles) — Ultimate's iconic Y-sort that made the keep feel three-dimensional in a 2D engine.

**Modern equivalent:** Stardew Valley, Hyper Light Drifter, Death's Door — Y-sort is still the standard for 2D action games with depth.

**Contribution:** Y-sorted layered rendering. Object list (hero + decorative objects), drawn each frame in order of Y position. Lower-Y objects drawn first (appear behind); higher-Y objects drawn last (appear in front).

**Code primitive:** `object_list[]` with (x, y, sprite_id) entries. Sort-by-Y each frame (insertion sort, ≤16 objects). `draw_objects()` walks sorted list.

**Art deliverable:** First decorative object — a *pillar*. Tall, atmospheric, distinct silhouette. The hero will walk behind it in this unit's demo.

#### Unit 10 — *Architecture*

**Design concept:** *Architecture as mood* — decoration is what makes a hall feel like a hall. Pillars, altars, sconces — the hall earns its name through what stands in it.

**Read alongside:** Atic Atac's room decoration (chest of drawers, paintings, candelabras) — each prop placed for atmosphere, not just visual fill.

**Modern equivalent:** modern level designers' prop-placement workflows (Unreal's actor placement, Unity prefabs, Tiled object layers).

**Contribution:** Decorative objects properly. Multiple pillars in the great hall. An *altar* at the centre with detail. Wall sconces. The great hall earns its name.

**Code primitive:** Object types extended — pillar, altar, sconce. Each with its own sprite data. Placement defined per-room in a decoration table.

**Art deliverables:** *Altar* (a centrepiece — multiple cells wide, real detail). *Sconce* (wall-mounted torch holder, hint of flame). Additional pillar variations if needed.

#### Unit 11 — *Light against stone*

**Design concept:** *Mood through constraint* — the 8×8 attribute clash IS the design tool, not the obstacle. Lighting emerges from picking which cells brighten near a torch.

**Read alongside:** Knight Lore's torches affecting attribute area — the chrome-yellow glow that made the iso world feel inhabited rather than diagrammed.

**Modern equivalent:** Hyper Light Drifter, Death's Door — limited-palette atmospheric lighting where the palette IS the lighting model.

**Contribution:** Attribute-aware lighting. Cells within N positions of a torch/sconce get brighter attributes (PAPER 6 yellow at INK boost; or BRIGHT 1 on dark cells); cells far from light stay dim. The keep transitions from flatly-lit room to *atmospheric place*.

**Code primitive:** `compute_lighting()` — for each cell, find distance to nearest light source, set attribute byte accordingly. Runs once per room load (not per frame).

**Art deliverable:** Light/dark attribute palette decisions. Designer-level work — picking which attribute combinations read as "candlelit" vs "shadowed."

#### Unit 12 — *The other room*

**Design concept:** *Threshold* — a second place sharpens the first. Only when there's somewhere else does *here* become specific.

**Read alongside:** Atic Atac's room-by-room transitions — the moment of crossing through a door, when the player realises the keep has *layout*.

**Modern equivalent:** Hollow Knight's room transitions — the cinematic flick of crossing into a new place; each transition reframes what came before.

**Contribution:** The antechamber as a designed *place* — distinct in feel from the great hall (narrower, more shadowed, threshold mood). Door transition between the two rooms.

**Code primitive:** Multi-room data structure. `current_room` index. `transition_to(room_id)` handler with brief screen-fade or flip.

**Art deliverable:** Antechamber room composition. Different tile choices from the great hall (more decorated edges, less open central space). Atmospheric.

---

### Sub-arc 1.4 — The Keep Stands (Units 13-16)

*Thematic identity: a complete first arc.*

#### Unit 13 — *Walls refuse*

**Design concept:** *Collision as design* — game-logical boundaries and visual boundaries are now separable. Decoration can have visual extents that don't block movement; walls can be visually narrower or wider than their collision.

**Read alongside:** Knight Lore's iso collision — visual extent vs. game-logical extent fully separated, which is what made iso playable at all on Spectrum.

**Modern equivalent:** every modern engine's collision-shape vs. visual-mesh distinction (Unity colliders, Godot CollisionShapes, Box2D fixtures).

**Contribution:** Tile-map collision. Walls (and pillars and altar) block movement. **Collision read from `room_data[]`, not from attribute area.** Attribute area remains purely cosmetic — colour boundaries can run independently of game-logical boundaries.

**Code primitive:** `can_move_to(pixel_row, pixel_col)` — query the tile-map for hero's destination. Return false if destination is wall/pillar/altar; true otherwise.

**Art deliverable:** None new — but this is where collision and visual design *fully* separate. Walls can be visually narrower or wider than collision; decorations can have visual extents that don't block movement; etc.

**Replaces:** existing Unit 5's attribute-based collision teaching.

#### Unit 14 — *A glimpse of gold*

**Design concept:** *Reward, audible* — the moment the player picks up gold is the first time the keep talks back. Sound makes the reward real.

**Read alongside:** Atic Atac's gold-pickup chime — the audio cue that defined the moment of reward and set the rhythm of play.

**Modern equivalent:** Hades' boon-pickup chime, Dead Cells' weapon-pickup tone — the audio-cue-as-feedback pattern, the unbroken thread back to 1983.

**Contribution:** **The SFX driver is introduced here** (previously implicit in later units). Gold as decorative objects (in the object list) with their own sprite. Pickup mechanic — hero overlapping gold object increments gold counter and removes the object from the list. Sparkle animation on pickup (3-frame brief flash). One-shot SFX cue triggered through the new driver.

**Code primitive:** **SFX driver** — main-loop-interleaved one-shot tone playback (single-channel beeper, doesn't block music). Object types extended — gold piece. Per-object animation state for sparkle. Pickup detection inside the object-list draw loop.

**Art deliverables:** *Gold piece sprite* — small, distinctive, with shine highlight. *Sparkle frames* (3 frames). Pickup SFX (one-shot beeper sequence — the first use of the new driver).

**Replaces:** existing Unit 6's flat-yellow gold cells and silent pickup.

**Seeds:** Unit 15 (composed theme can use the driver for the title theme's SFX layer); Unit 17 (footsteps reinforce the driver); Branch G (audio hardware) reinforces with AY when 128K arrives.

#### Unit 15 — *The composed theme*

**Design concept:** *Music as place* — the moment the keep gains an identity beyond what the eye can see. The theme is the keep's signature.

**Read alongside:** Matthew Smith's Manic Miner title theme on beeper (an arrangement of *In the Hall of the Mountain King*) — the canonical Spectrum example of composed beeper music carrying mood.

**Modern equivalent:** Disasterpeace's Hyper Light Drifter score — composed mood music written *for* an atmospheric game rather than chosen from a library.

**Contribution:** **Pure beeper composition focus** — the SFX driver landed in Unit 14, so this unit is *composition*, not engine work. The Shadowkeep title music, *properly composed* per [shadowkeep-beeper-spec.md](shadowkeep-beeper-spec.md): statement (8 bars) / variation (8 bars) / bridge (4 bars) / return (4 bars). ~30-60 seconds at ~110 BPM, D minor.

**Code primitive:** Music data table — the composed piece. Chord/arpeggio beeper techniques (the single-channel polyphony tricks of the period). Music playback interleaved with the U14 SFX driver — both share the beeper without collision.

**Art (audio) deliverable:** The composed title theme. This is real compositional work, in the lineage of [Matthew Smith](/vault/people/matthew-smith), [Tim Follin](/vault/people/tim-follin). Substantial time; the right reference recordings (Manic Miner, Jet Set Willy, Stormlord) help calibrate. Budget honestly — composition can't be rushed.

**Replaces:** existing Unit 7's 12-note placeholder sketch.

**Seeds:** Unit 30 (audio depth deepens with victory chord + ambient music); Branch G (AY hybrid composition arrives at V2.16 / V3.17 in the wider curriculum).

#### Unit 16 — *The keep at night*

**Design concept:** *First and last impression* — the title screen is what the player sees before they play and after they finish. It is the work, distilled to a single image.

**Read alongside:** Knight Lore's title screen — Ultimate's iconic logo + atmospheric illustration, the artefact a player saw on the cassette inlay and on the screen.

**Modern equivalent:** Hollow Knight's main menu — illustrated title screen with composed music underneath; the player meets the game's identity before pressing start.

**Contribution:** Full game loop. Hand-pixelled title screen with designed logo type (not ROM font) plus illustrative artwork (a keep silhouette? the thief in three-quarter view? to-be-designed). Title music plays under it. SPACE starts the game. On victory, return to title.

**Code primitive:** Title-state machine. State transitions (TITLE → PLAY → VICTORY → TITLE). The full Arc-1 loop.

**Art deliverables:** *Title screen illustration* — the single most-load-bearing piece of art. *"SHADOWKEEP" logo type* — designed letters, not ROM font. *Victory presentation* (green BORDER + held music + maybe brief animation).

**Replaces:** existing Unit 8's plain ROM-font title.

---

### Arc 1 ship gate

End-of-Arc-1 must pass before Arc 2 begins. Acceptance criteria:

- Hero moves at pixel-level precision, animated, masked, leaves no trail.
- Hero passes correctly behind and in front of pillars depending on Y.
- Two designed rooms (Great Hall + Antechamber), each with distinct visual character.
- Atmospheric lighting near torches in both rooms.
- Tile-map collision separated from attribute.
- Gold pickup with visible sparkle and audible cue.
- Composed title theme playing under hand-pixelled title screen.
- Complete title → play → victory → title loop.

If any of these fail to land at the bar, the gate doesn't pass. Arc 2 doesn't start. (Drift trigger: "We'll polish later" is the failure mode this guards against.)

---

## Arc 2 — Inhabitants and Identity

End-of-arc deliverable: a three-room game with non-player inhabitants, lives, score tracking, HUD, atmospheric polish, and verified real-hardware playability. The keep gains depth and threat. The game knows itself.

### Sub-arc 2.1 — Sound and Motion (Units 17-20)

*Thematic identity: the keep makes itself heard.*

#### Unit 17 — *Footsteps*

**Design concept:** *The audible heartbeat* — sound is what makes the place breathe. The hero's footsteps are the keep's pulse.

**Read alongside:** Cybernoid II's footstep + bullet SFX layered over Tim Follin's title music — Crow's masterclass in audio layering.

**Modern equivalent:** any modern action game with footsteps overlaid on background score (Hyper Light Drifter, Hollow Knight) — the same layering with richer hardware.

**Contribution:** Beeper SFX during hero movement. One-shot tone per move step, **reinforces the U14 SFX driver** (the driver was introduced there; this is its first interleaved-with-music use). The keep gains an audible heartbeat.

**Code primitive:** SFX channel — interrupt-driven or interleaved with main loop. State so SFX doesn't queue infinitely.

**Audio deliverable:** Footstep sound — short, percussive, atmospheric. Multiple variations if budget allows (regular step, hesitation step).

#### Unit 18 — *Door creaks*

**Design concept:** *Transitions feel real* — the keep no longer teleports the player between rooms; passage takes time and has texture.

**Read alongside:** Knight Lore's door-opening animation — the deliberate slow reveal as the iso door pivots open over a few frames.

**Modern equivalent:** Hollow Knight's gate animations, Hyper Light Drifter's door reveals — transitions as cinematic beats, not cuts.

**Contribution:** **Per-object animation state machine** introduced as a generalisable primitive (was implicit in U6's walk-cycle and U14's sparkle; named and formalised here). The door-open sequence is its first non-character use. Audio cue interleaved through the U14 SFX driver.

**Code primitive:** **Animation state machine** — per-object state byte tracking which frame, how many ticks-per-frame, what happens at end (loop / return / one-shot). Door-open sequence: 3-4 frames, triggered by transition, plays once, then transition completes. Future units (U19 idle, U24 NPC behaviour cycles) extend this.

**Art / audio deliverables:** Door animation frames. Door-creak SFX (medium-length, descending pitch).

**Seeds:** Unit 19 (idle animation extends the state machine); Unit 24 (behaviour tables select among animation states); Arc 3+ (active-item animations — torch lit, key turning — reinforce).

#### Unit 19 — *Idle and breathe*

**Design concept:** *Aliveness without input* — the character must live when the player isn't pressing keys. Idle animation is the difference between a sprite and a presence.

**Read alongside:** Sabreman's idle bob in Sabre Wulf — the small motion at rest that says *alive*; barely-there but unmissable in its absence.

**Modern equivalent:** Celeste's Madeline bobs while idle; Hollow Knight's Knight breathes — every modern character carries this thread.

**Contribution:** Hero idle animation — subtle bob, hood shift, weight sway. When stationary, the hero is *alive*, not frozen. Extends the U18 animation state machine to idle-state detection.

**Code primitive:** Idle frames cycled at slow rate (every ~30 frames). Detection of "no input for N frames" to enter idle state.

**Art deliverable:** Idle animation frames (3-4 frames at very subtle motion).

#### Unit 20 — *Floor and shadow*

**Design concept:** *Variety as mood palette* — repeating the same tile reads as flat; controlled variation reads as place. The keep's *texture* emerges from designed-not-procedural variety.

**Read alongside:** Atic Atac's varied floors and per-room attribute mood — each room reads as a different place because palette varies as much as tile.

**Modern equivalent:** Hyper Light Drifter's per-region palette shifts; Death's Door's biome palettes — palette as a primary design tool, not decoration.

**Contribution:** **Per-room mood palette** as an explicit design choice (was loose "floor and shadow"; now named). Per-room attribute mood, floor variety, palette-led mood decisions. The Great Hall reads warmer; the Antechamber cooler; if a third room exists (U28), its palette differentiates it again.

**Code primitive:** Floor-tile dispatch in renderer, similar to wall tiles. **Per-room palette table** — each room references a palette which determines attribute defaults plus accent ranges. Lighting (U11) overlays on top of palette.

**Art deliverable:** Multiple floor tile variations (≥3 stone variations: clean, damaged, mossy). Per-room palette decisions — attribute combinations that read as cohesive mood.

**Seeds:** Arc 4 sub-arc 4.1 (atmospheric cycles — time-of-day uses per-room palettes as the base layer).

---

### Sub-arc 2.2 — A Presence in the Dark (Units 21-24)

*Thematic identity: the keep is not empty.*

#### Unit 21 — *Something moves*

**Design concept:** *The keep is not empty* — the first inhabitant changes what the place IS. Before this unit, Shadowkeep is architecture; after this unit, it is *inhabited* architecture.

**Read alongside:** Knight Lore's first wandering monster — the moment the iso world stops being empty and starts being *populated*.

**Modern equivalent:** Dark Souls' first hollow patrolling — the moment the level becomes inhabited; the same shift, four decades on.

**Contribution:** First non-player moving sprite. A presence — spectre, guard, watcher — patrolling one room on a simple back-and-forth path. Y-sorted with the hero and decorations.

**Code primitive:** NPC state — position, direction, sprite, animation frame. Per-frame update of position. Inserted into the object list with hero/decorations.

**Art deliverable:** *The presence* — a designed sprite. Must read as different in mood from the hero. Suggested: a hooded figure with no visible face, or a translucent spectre, or a guard with helm and sword.

#### Unit 22 — *The shape closes*

**Design concept:** *Threat made real* — collision is the moment the inhabitant matters. Until two sprites can touch, they share space but not consequence.

**Read alongside:** Atic Atac's first ghost encounter — the moment the inhabitants matter; a flash, a sound, a felt threat.

**Modern equivalent:** Subnautica, Don't Starve — the first enemy contact in any modern survival game; the same shift from *seeing* to *being affected by*.

**Contribution:** Collision detection between hero and presence. When the presence touches the hero, something happens — for Unit 22, this is just a BORDER red flash. (Lives system comes in Unit 23.)

**Code primitive:** Bounding-box overlap test in the object-update loop. Trigger collision handler on overlap.

#### Unit 23 — *Lives, deaths*

**Design concept:** *Stakes* — lives turn threat into consequence. A flash that costs nothing is design noise; a flash that costs a life is the game.

**Read alongside:** Manic Miner's death-and-restart cycle — Matthew Smith's tight loop where dying is part of the rhythm, not the end.

**Modern equivalent:** Celeste's restart-on-death — the modern descendant of MM's discipline; death so fast that it doesn't punish trying.

**Contribution:** Multi-life system. Hero starts with 3 lives. Collision with presence costs one life. On 0 lives, game over → title. Respawn at room entry on death.

**Code primitive:** `lives` state byte. Death routine — visual cue (red flash + audio), respawn placement, life decrement, game-over check.

**Audio deliverable:** Death SFX (descending tone + low note).

#### Unit 24 — *A different threat*

**Design concept:** *Threat variety* — one inhabitant pattern is novel; two reads as ecology. The keep is not predictable.

**Read alongside:** Sabre Wulf's mix of patrol creatures — each behaves differently within the same engine; ecology rather than copy-paste.

**Modern equivalent:** Hollow Knight's bestiary, Dead Cells' enemy types — every modern action game's enemy taxonomy carries this thread.

**Contribution:** **Behaviour tables** introduced as the technique (was loose "second NPC"; now the table is the load-bearing primitive). Behaviour tables let one NPC implementation serve multiple instances with different routines selected at instantiation. Second NPC type or behavioural variation — either a different patrol routine, a stationary hazard, or a different threat kind entirely.

**Code primitive:** **NPC behaviour table** — array of behaviour-function pointers, each NPC instance carries an index. Per-frame dispatch goes through the table. Adding a new behaviour means writing a new function and adding it to the table; instances opt-in.

**Art deliverable:** If new sprite, hand-pixel it (a different inhabitant — guard with helm, animated rat, stationary spike-pit, etc.). Otherwise reuse existing presence with palette/animation variation.

**Seeds:** V3 shooter AI (Hostraider's enemy patterns, Hivefall's formation behaviour, Wayguard's bidirectional patrol — all use behaviour-table-style dispatch). The technique is *introduced* here, *deepened* across V3.

---

### Sub-arc 2.3 — A Game Knows Itself (Units 25-28)

*Thematic identity: self-aware presentation.*

#### Unit 25 — *Score on the wall*

**Design concept:** *Self-aware game* — the HUD is the game telling the player what it knows. Before the HUD, score is invisible; after, the game has metabolism the player can read.

**Read alongside:** Atic Atac's score / lives / time display at the top of the screen — the canonical Ultimate HUD that gave the player a sense of *standing* in the game.

**Modern equivalent:** Hollow Knight's bottom-left status, Dead Cells' top-right HUD — persistent metabolism the player learns to glance at without thought.

**Contribution:** HUD bar. Two-row strip at top of screen — score, gold count, lives count. Updated in real time. Distinct visual styling from the play area.

**Code primitive:** HUD-render routine called each frame (or on state change). Reserved cells (top two rows) that the game-area renderer doesn't touch.

**Art deliverable:** HUD layout design. Number-glyph design (better than ROM font — single-digit highlights, leading-zero handling). Possibly a small icon for "gold" and "lives".

#### Unit 26 — *The keep names itself*

**Design concept:** *Place is named* — room titles give space identity beyond what the eye reads. "The Great Hall" lands as architecture before the player sees the next pillar.

**Read alongside:** Knight Lore's room names appearing briefly on entry — the small text label that turned a screen into a *place*.

**Modern equivalent:** Hollow Knight's area-name reveals — the cinematic moment of arrival; Hyper Light Drifter's region titles do the same.

**Contribution:** Room titles displayed briefly on transition. "The Great Hall" / "The Antechamber" / "The Crypt" (Unit 28's third room). Fades in for ~2 seconds on entering a new room.

**Code primitive:** Room metadata (name string per room). Fade-in/fade-out routine for text. Triggered on `transition_to(room_id)`.

**Art deliverable:** Text-rendering style decisions. Letter spacing, font weight (designed glyphs vs ROM font).

#### Unit 27 — *A trail remembered*

**Design concept:** *History across plays* — the player's best score persists; the keep remembers them between sessions. A small mechanic; a real continuity.

**Read alongside:** Manic Miner's high-score display on the title screen — the player's prior runs visible at the start of every session.

**Modern equivalent:** Tetris' running session stats, Celeste's deaths-per-screen, Hades' run history — modern games carry session memory in many forms.

**Contribution:** Best-score persistence between plays. Not save-to-tape; just in-memory between game-overs and restarts. The title screen shows "BEST: 247" or similar.

**Code primitive:** `best_score` global. Updated on game-over if `score > best_score`. Title screen renders it.

#### Unit 28 — *The keep grows*

**Design concept:** *World as graph* — two rooms is a corridor; three rooms with the right connections is a place. Adding a third room demands the engine think about *connections*, not just rooms.

**Read alongside:** Atic Atac's room-graph design — 50+ rooms with multiple connections each; Ultimate's invention of a real graph rather than a corridor.

**Modern equivalent:** every modern Metroidvania's room layout (Hollow Knight, Ori, Hollow Knight) — graph data is the foundation; map screens visualise it.

**Contribution:** **Room-graph data structure** introduced (was loose "third room with extension"; now the graph is the technique). Multi-room tile-map extended to a real room-graph supporting arbitrary connections (not just the linear A↔B↔C). Per-room theming applied (U20's palette table extends to all three rooms). A third room — crypt (darker, more hazards) or treasury (more gold, more presences) — uses the new graph.

**Code primitive:** **Room-graph data structure** — table of room records, each with N exits (direction, target room, transition type). Replaces hardcoded A↔B antechamber transition. `transition_to(room_id)` walks the graph. Per-room theming index added.

**Art deliverable:** *The third room.* Full composition. Distinct from the other two via the U20 palette system.

**Seeds:** Hollowhalls (V2.10 — Jet Set Willy multi-room platformer extends the graph to many rooms with vertical and horizontal connections); Shadowkeep Arc 3.2 (Beyond One Keep — graph extends across keeps, not just within); Whitewinter (V1.4 — Lords of Midnight's location-graph is the same primitive at vastly larger scale).

---

### Sub-arc 2.4 — Completion (Units 29-32)

*Thematic identity: the shipping artefact.*

#### Unit 29 — *Atmosphere unified*

**Design concept:** *Polish as discipline* — the difference between ships and shines. A unit dedicated to *not adding* anything; to *refining* what is.

**Read alongside:** Knight Lore's late-development polish — the difference between October 1984 screenshots and the shipped Christmas 1984 cassette.

**Modern equivalent:** any indie game's pre-release polish month — the difference between early-access and 1.0; Celeste's *Farewell* update polish.

**Contribution:** Polish pass across all three rooms. Lighting palettes refined. Animation timings tuned. Attribute decisions checked for consistency. Any remaining tile-or-art rough edges fixed.

**Code primitive:** No new code primitives — this is a polish pass.

**Art deliverable:** Multiple small revisions across existing art. The kind of pass that's often skipped but is the difference between "ships" and "shines."

#### Unit 30 — *Audio depth*

**Design concept:** *Audio polish as character* — the final SFX library is when the keep gains full voice. A few extra sounds make a place feel lived-in; the difference is real.

**Read alongside:** Cybernoid II's full audio layer — Tim Follin's hybrid beeper-and-AY composition plus a full SFX library covering every game action.

**Modern equivalent:** Hyper Light Drifter's audio mix — composed score + atmospheric SFX + audio cues — the same layered structure with richer hardware.

**Contribution:** SFX library expanded. Music polish — title theme refined; victory chord composed properly (not just rising notes). Possibly an in-game ambient drone or low-volume music in specific rooms (the crypt, for instance).

**Code primitive:** Multi-channel SFX queue. Music-in-game flag (probably default off — period-accurate).

**Audio deliverable:** Multiple SFX revisions. Music revision pass. Victory chord composed.

#### Unit 31 — *Real hardware*

**Design concept:** *The artefact is real* — testing on hardware is what makes the work real, not just plausible. Emulator-fidelity is a claim; hardware-playability is proof.

**Read alongside:** the era's hardware-testing tradition — every commercial Spectrum game had to survive Issue 2 vs Issue 3 motherboard variations, 48K vs 128K differences, the Microdrive's quirks.

**Modern equivalent:** any indie game's Steam Deck verification — modern cross-hardware testing; the descendant of "we tested on every Spectrum we could find."

**Contribution:** Test on real Spectrum Next (and ideally a real 48K via TZX). Fix anything that drifts from emulator behaviour. Verify tape-loading works. Verify the game feels right on real-hardware-tier responsiveness.

**Code primitive:** No new primitives. Bug fixes only.

**Process deliverable:** Real-hardware playtest log. Documented differences (if any) between emulator and hardware. Fixes applied.

#### Unit 32 — *The keep at midnight*

**Design concept:** *First and last impression, completed* — the final title art is what the work IS in the player's memory after the game is closed. The shipping artefact is the work.

**Read alongside:** Knight Lore's shipping cassette — the artefact that landed on Christmas 1984; the inlay art, the loader screen, the title music; the work as the player encountered it.

**Modern equivalent:** any indie game's launch-day build — the artefact that goes live to players; Celeste's 1.0, Hollow Knight's gold release.

**Contribution:** Final presentation pass. Title screen revised to its shipping form. Victory sequence designed in full ("completed" state — perhaps the keep's silhouette at dawn, perhaps a credits roll, perhaps just a held high score). The shipping artefact.

**Code primitive:** State machine for the "completed" state. Optional credits sequence.

**Art deliverable:** *Final title art.* *Completed-game presentation.* This is the final polish on the work the player sees first and last.

---

### Arc 2 ship gate (= October launch gate)

End-of-Arc-2 must pass before October launch. Acceptance criteria:

- All Arc 1 gates still pass (nothing regressed).
- Three designed rooms with atmospheric depth and lighting.
- One or two NPC types active with patrol behaviour (behaviour-table dispatch working).
- Lives, deaths, respawn working.
- HUD with score / gold / lives.
- Room names shown on transition.
- Best-score persistence.
- Verified playable on Spectrum Next.
- Final title screen and completion state designed and polished.
- Composed music + SFX library complete (SFX driver + composed theme delivered).

---

## Embedded design concepts

Beyond the per-unit headline (Atmosphere — Sense of Place), six concepts weave across the 32 units. Each unit's MDX prose should surface at least one when relevant:

| Embedded concept | Surfaces in units |
|------------------|-------------------|
| **Atmosphere through restraint** | 1, 4, 11, 12, 16, 20, 29 (mood from limit — the attribute clash IS the design tool) |
| **Authored level design** | 4, 10, 12, 14, 20, 28, 29 (the designer's voice in tile placement, decoration, room composition) |
| **Animation budget** | 6, 7, 8, 17, 18, 19, 24 (frames vs story — every animation costs sprite-table memory) |
| **Identity through silhouette** | 5, 6, 7, 8, 21 (the hooded thief reads in 8×8; the presence reads as different) |
| **Audio as place** | 14, 15, 17, 18, 30 (sound is what gives the keep voice — silent it would be unfinished) |
| **Polish as discipline** | 29, 30, 31, 32 (the difference between ships and shines — the unit budget guards against the *we'll polish later* drift trigger) |

These are not headlines — they're the *texture* of the curriculum. Per-unit MDX prose surfaces them in passing; the embedded-concept-rich units make Shadowkeep teach more than just its 32 techniques.

---

## Time budget (rough)

5 months ≈ 100 working days. 32 units. ~3 days per unit average.

**Easier units (~1-2 days):** 1 (mostly inherits), 13 (logic-only), 17 (one SFX), 22 (collision logic only), 27 (persistence), 31 (testing).

**Harder units (~3-4 days):** 5 (the hero sprite — most-load-bearing art), 6 (walk cycle animation), 9 (Y-sort engine introduction), 10 (decoration objects), 15 (composed music), 16 (title screen art), 21 (NPC introduction), 28 (third room).

**Average units (~2-3 days):** all others.

Total ~80-95 working days at average pace. Tight but feasible; the polish-within-the-budget principle (don't slip from one unit to the next) is the discipline that keeps it from slipping past October.

## Per-unit Definition of Done

Each unit, before shipping, must pass:

1. Code compiles on `pasmonext`; SNA generated.
2. SNA runs cleanly on Emu198x; visual + audio verified.
3. MDX prose written at magazine-class bar (CRASH/YS register).
4. Screenshots captured and saved to `website/public/images/.../`.
5. Audio captures (where relevant) saved to `website/public/audio/.../`.
6. CodeFromFile component references active.
7. "Try this" sections (≥2) included.
8. "If it doesn't work" troubleshooting section included.
9. Vault references resolve (every `/vault/...` link points to an existing reviewed entry).
10. **Design concept made explicit in the prose.** Each unit names *what* it teaches at the design level, not just *how* the code works. The MDX makes the headline-and-embedded-concept layer visible to the reader, not implicit in the code.

The Definition of Done from earlier launch-spec carries forward; this list extends it with the new bar's specifics.

---

## Post-October: Arcs 3-4 outline

Per [shadowkeep-four-arc-framing.md](../../../../decisions/shadowkeep-four-arc-framing.md), Shadowkeep continues post-October into Arcs 3-4 (~32 more units, total 64). These stay in the flick-adventure tradition — no RPG / parser / shooter genre-drift. Per-unit detail is to be elaborated when each arc enters build scope; sub-arc-level outline below.

### Arc 3 — *Beyond the Walls* (Units 33-48, post-October Year 1)

*Thematic identity: the keep is no longer alone. Items matter, places connect, the hero remembers, the world holds secrets.*

- **Sub-arc 3.1 — *Items that Matter*** (33-36): inventory state, item-gated transitions, inventory limits, item effects (torch / key / glyph). Sabre Wulf / Knight Lore / Pentagram traditions.
- **Sub-arc 3.2 — *Beyond One Keep*** (37-40): outdoor tile set, multi-location traversal, per-location state persistence, return-and-find mechanic. *(Full location-graph data and Singleton-class day/night cycle are V1.4 Whitewinter's primary teaching — Shadowkeep uses a lighter variation.)*
- **Sub-arc 3.3 — *The Persistent Hero*** (41-44): tape save, tape load + validation, in-memory save/pause/resume, save/load menu UI.
- **Sub-arc 3.4 — *Secrets and Lore*** (45-48): hidden rooms (Atic Atac secret-room mechanic), lore fragments (collectable atmospheric text on item use), active items affecting the world (torch lights nearby cells, key opens specific doors, glyph reveals secrets), the bestiary (visual collection of creatures encountered).

**Arc 3 ship gate:** Inventory with 6+ item types; multi-location traversal with 2-3 areas beyond original keep; working tape save/load on real hardware; secrets-and-lore system with hidden content the player must discover.

### Arc 4 — *The Greater World* (Units 49-64, post-October Year 2)

*Thematic identity: the keep is part of something larger. Time, place, completion all matter.*

- **Sub-arc 4.1 — *Atmospheric Cycles*** (49-52): time-of-day cycle (per-room palette varies with time), weather and mood states, palette shifts per state, the keep's seasons. Knight Lore's atmospheric polish extended via U20's palette system.
- **Sub-arc 4.2 — *Multiple Keeps*** (53-56): outdoor traversal between locations, a second keep with distinct character/tile set, return mechanic between keeps, a third keep (deeper / more dangerous). Pentagram + Underwurlde tradition.
- **Sub-arc 4.3 — *Endings*** (57-60): collection-based unlock (find all lore items / artifacts for true ending), mediocre ending if incomplete, true ending if complete, second-playthrough content. **Endings are completion-based, NOT branching-narrative based.** (Branching narrative is V1.7 The Lantern Path's primary teaching.)
- **Sub-arc 4.4 — *Completion*** (61-64): 64-unit polish discipline, complete soundtrack, shipping cassette artefact (Spectrum Next + TZX 48K), final completed-state machine.

**Arc 4 ship gate:** Time-of-day cycle working; 2-3 distinct keeps beyond Shadowkeep; collection-based true-ending unlock; final polished build on real Spectrum Next + TZX 48K.

### What Arcs 3-4 explicitly do NOT teach

These belong in other curriculum games per [shadowkeep-four-arc-framing.md](../../../../decisions/shadowkeep-four-arc-framing.md):

- Combat depth / hit-states (V3.20 Edge of Iron — beat-em-up canon)
- Spell systems (V1.6 Embergate — action-RPG canon)
- Character classes, XP, leveling (V1.6 Embergate)
- Menu-based dialogue and quest state (V1.7 The Lantern Path — parser canon)
- Branching narrative and multi-quest tracking (V1.7 The Lantern Path)
- Full Singleton-class location-graph and day/night cycle (V1.4 Whitewinter — Lords of Midnight canon)

If a future Shadowkeep unit reaches for these, stop — you've drifted into another game's tradition.

## Live tracker

`docs/tracker/revamp.md` is the live status tracker. Per-unit progress, blockers, and acceptance state live there. This plan is the *spec*; revamp.md is the *state*.
