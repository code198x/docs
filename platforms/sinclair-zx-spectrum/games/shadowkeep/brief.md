# Shadowkeep — Brief

**Title (working):** Shadowkeep
**System / Track:** ZX Spectrum / Assembly
**Position:** The second game of the assembly track, after *Gloaming* (the tiny first game) and the *Meet the Machine* Primer.
**Module model:** Shadowkeep is a **game taught across several modules** ([modules-not-games.md](../../../../decisions/modules-not-games.md)). This brief covers **pass 1 — _the Place_**: a complete, finishable cell-based keep. Later content (inhabitants, identity, items, multiple keeps) becomes **later revisit modules**, not part of this pass.
**Headline (design concept):** *Atmosphere (Sense of Place)*
**Engine:** carries **Gloaming's engine** wholesale — cell-snapped movement, single-draw sprites with save/restore, attribute-coupled collision, a frame-locked loop, a title→play→win state machine. The Place adds *content and atmosphere*, not a new engine.
**Counts:** illustrative, never targets ([curriculum-structure.md](../../../../decisions/curriculum-structure.md)). Pass 1 ran to ~16 units across four sub-arcs.
**Status:** Active. **v3.0 (2026-06-02)** — rewritten for the cell-based Place after the 2026-05-29 re-pace and the module-model reconciliation. Supersedes v2.0's engine-first / 64-unit-four-arc framing (preserved in git).

Formal spec format: [docs/specifications/brief.md](../../../../specifications/brief.md). Companion docs in this folder: [per-unit-plan.md](per-unit-plan.md) (the canonical per-unit reference) and [beeper-spec.md](beeper-spec.md) (the title-theme composition spec, for sub-arc 1.4). The original engine-first specs (sprite-shifter, object-system, tile-map, engineering-plan, memory-budget) are archived under [`superseded/`](superseded/) — they describe techniques **relocated** to later rendering games and are not current guidance.

---

## 1. Pedagogical role

Teach the ZX Spectrum's *atmospheric* craft tradition at commercial bar — not by building a new engine, but by taking the engine the learner already finished in *Gloaming* and growing it into a place worth being in. The load-bearing techniques are **bitmap dithering** (density as shade, then as light), **room-as-data** (a tile palette + readable maps), a **multi-room flick-screen world**, **persistent per-room state**, and **beeper sound**. By the end of pass 1 the learner has a complete cell-based flick-adventure — lit, furnished, composed, and winnable — at the bar of *Atic Atac* and *Knight Lore*.

The headline *Atmosphere (Sense of Place)* traces through every unit: every decision serves the player's sense of being *in* the keep, and it's reached through **art, light and sound within the cell**, not through pixel-level rendering.

> The three commercial-bar *rendering* techniques the old plan put here — pre-shifted/masked sprites, Y-sorted layered rendering, attribute-decoupled collision — are **relocated** to later rendering games (Smooth Motion, Overlap, Greypeak), each motivated by the felt limit of the Place's cell-based look (the deprecation-pair pedagogy). Shadowkeep is the curriculum's *atmosphere* introduction; those games are its *rendering* introduction.

---

## 2. Classic ancestors

- ***Atic Atac*** (Ultimate, 1983) — the multi-room flick-screen adventure archetype. 148 rooms in 48K; the screen *is* the map; you flick room to room. The structural model for the Place.
- ***Knight Lore*** (Ultimate, 1984) — the mood archetype: atmospheric, dark, every room a composed place. The Place chases this feeling with dither-lighting, not with Knight Lore's filmation/masking (that's Greypeak's tradition).
- ***Sabre Wulf*** / ***Pentagram*** / ***Underwurlde*** (Ultimate, 1984–86) — flick-adventure lineage; the source of the explore-a-connected-world feel, and of the items / multiple-keeps content that later Shadowkeep *revisit* modules will carry.
- ***Cybernoid II*** (Hewson, 1988) — held as the *polish* bar (dense hand-crafted art, Tim Follin audio), the standard the Place's atmosphere aims at.

Opening-screen archetype: ***The Hobbit*** (Melbourne House, 1982) — economical, suggestive title presentation.

---

## 3. What's new (beyond Gloaming)

Gloaming taught and shipped the engine; the Place reuses it and adds what makes a *place*:

1. **Dithered stone (Units 2, 9–12).** Mixing INK/PAPER in the bitmap gives perceived shades between a cell's two colours — texture, then, by distance from a torch, *lighting*; then per-room *mood* (falloff) and *character* (multiple flames). This is the Place's signature technique. (Steve's design call, 2026-06-02.)
2. **Room-as-data (Unit 4).** A tile palette (a glyph names a tile) and rooms authored as readable ASCII maps; collision reads the cell's look (BRIGHT = solid).
3. **A multi-room flick-screen world (Units 5–6, 8).** A room graph with N/S/E/W links; edge-matched doorway transitions (leave one edge, arrive at the opposite edge, same height).
4. **Persistent per-room state (Unit 7).** Rooms live in RAM; what the thief changes (his chalk trail) survives leaving and returning.

The Ultimate flick-adventure tropes are preserved (hooded thief, multi-room keep, explore-and-collect, atmosphere); what makes it a *curriculum* and not a clone is that each of these is a clean, named technique built on the prior game.

---

## 4. Core experience

Walk a hooded thief through a dark keep, room by room, the screen flicking as you cross each threshold. Read the colour-coded, light-pooled space before stepping into it; learn the keep's geography; gather the gold; hold back the dark. The pleasure is exploration and atmosphere — a small, dense, hand-painted world that rewards observation over reflex. What the player feels is *atmosphere*; what the design teaches is *sense of place* as a generalisable idea — constraint-rich worlds become memorable through what they show.

---

## 5. Constraint position

**Period-faithful throughout.** Every technique in the Place appeared in commercial Spectrum games of 1983–89: attribute graphics, bitmap dithering for shade, hand-pixelled tiles, flick-screen rooms, beeper sound, port `$FE` I/O, a 50 Hz `IM 1`/`HALT` loop. A 1986 Ultimate or Hewson developer had all of it in their toolbox.

**Hardware in active use:**
- Bitmap memory (`$4000–$57FF`) — dithered stone tiles, the hero, furniture, title art
- Attribute memory (`$5800–$5AFF`) — colour, and (coupled) the solid/walkable rule
- Port `$FE` — keyboard half-row scanning + beeper bit 4
- `IM 1` + `HALT` 50 Hz frame lock

**Reserved for later Shadowkeep revisit modules:** tape save/load, richer location data. **Reserved for other games entirely:** pre-shift/masking (Smooth Motion / Overlap), Y-sort + isometric (Greypeak), software scrolling (V3 entries), AY audio (the beeper is the flick-adventure tradition).

---

## 6. Visual direction

**Cell-based, hand-composed, atmospheric.** No pixel-level sprite movement; the craft is in the *tiles, the dither, and the light*.

- **Stone is dithered, not flat.** A ramp of blue/black dither tiles gives shades from lit to near-black; walls are a sparse, BRIGHT dither (lit stone), floor a denser dim dither (dark slate).
- **Light is dither density by distance.** A torch (`T` in the map) casts a pool that fades through the shade ramp. Per-room *falloff* sets mood (broad Hall, tight crypt Vault); *multiple torches* (nearest wins) give a room character.
- **Furniture is tiles.** Statues and banners (BRIGHT → solid, walk around), rubble (dim → walkable, walk over) — set-dressing placed by typing a glyph.
- **The hooded thief** is a single 8×8 silhouette in bright red — identity through silhouette (Unit 1). His bytes: `$18, $3C, $7E, $7E, $7E, $7E, $3C, $24`.

**Magazine-screenshot test.** The Vault: a flame on the altar, a tight pool of dithered light, the rest sunk to near-black, the thief a dim figure approaching. Reads as atmospheric, period-correct, instantly Spectrum — a *Crash* reviewer in 1986 would have screenshotted it.

**Forbidden combination:** never red PAPER for floor — the hero is red and would vanish.

---

## 7. Audio direction (sub-arc 1.4)

**Title theme.** Single-voice beeper, ~30–60 s, looping; *Manic Miner* "In the Hall of the Mountain King" precedent — a real melody, monophonic, composed with care. Full spec in [beeper-spec.md](beeper-spec.md).

**In-game.** Period-correct near-silence broken by event SFX — *Atic Atac* was largely silent in-game; we honour it. A small **SFX driver** on port `$FE` bit 4 (footsteps, a door, gold collected, the win) grown from Gloaming's single blip. Music and SFX share the one channel via interleaved scheduling.

AY-3-8912 is deferred — the flick-adventure tradition is beeper; AY arrives elsewhere in the curriculum.

---

## 8. Level design direction

**Hand-designed, cell-based, flick-screen.** Pass 1 ships **a small real keep** — the built three rooms are the **Hall** (pillared, broadly lit), the **Gallery** (split by a wall with one gap to find), and the **Vault** (a central altar lit by its own flame). Doors **align** across connected rooms (east↔west share a row, north↔south a column) so crossings read as steps. Every room reads as somewhere from a screenshot alone.

**Signposting** is the light and the palette; there is no in-game tutorial. **Difficulty** is forgiving in pass 1 (exploration, not threat — threat is a later revisit module). **Onboarding:** the first minutes teach that the keep is dark, a torch lights a pool, QAOP moves the thief, doorways flick to new rooms, gold is the goal.

Later Shadowkeep *revisit* modules grow the keep (more rooms, outdoor traversal, multiple keeps) — out of scope for the Place.

---

## 9. Polish direction (sub-arc 1.4)

- **Title screen** with hand-pixelled logo + the beeper theme; "press a key to enter".
- **The loop:** title → explore → win (the keep's gold cleared) → title.
- **Real hardware:** verified on a Spectrum Next + a 48K tape image, as *Gloaming* closed.

Options (sound on/off, control remap) and richer endings belong to later revisit modules.

---

## 10. Anti-goals

- **No combat, no weapons.** The hooded thief is a stealth intruder; design is explore-and-avoid. Combat lives in V3.20 Edge of Iron; action-RPG in V1.6 Embergate. ([shadowkeep-four-arc-framing.md](../../../../decisions/shadowkeep-four-arc-framing.md) Genre-Honesty table.)
- **No character classes, no parser/quest/branching narrative, no full Singleton-class location-graph.** V1.6 Embergate / V1.7 The Lantern Path / V1.4 Whitewinter respectively.
- **No pre-shifted/masked sprites, no Y-sort, no isometric, no decoupled tile-collision** — these are the *relocated* rendering techniques (Smooth Motion / Overlap / Greypeak). The Place stays cell-based on purpose.
- **No software pixel scrolling** (V3 entries); **no procedural generation** (every room hand-designed); **no modern-scene tricks** (period-faithful).
- **No fixed unit count, no count-creep.** The Place ran to what it needed (~16 units); surplus effort goes into the bar, not into padding.

---

## 11. Module trajectory (the module model)

Shadowkeep is a game across several modules. **Pass 1 — _the Place_** is this brief. The old "Arc 1 + Arc 2 = 32, four arcs = 64" framing is retired; its content maps onto **later revisit modules**, sequenced into the lineup after intervening games, each within the per-game technique budget. Counts below are illustrative.

| Module (pass) | Content | Status |
|---|---|---|
| **Shadowkeep — the Place (pass 1)** | the keep as a lit, furnished, composed, winnable flick-adventure (identity · dithered stone · movement · room-as-data · room graph · doorways · persistence · three rooms · lighting · furnishings · mood · character · audio · win loop · real hardware) | **complete** — 1.1–1.4 done (16 units, Arc 1) |
| Shadowkeep — inhabitants (later revisit) | cell-based NPCs, threat, lives | later |
| Shadowkeep — identity (later revisit) | numeric HUD / digit rendering, room names, score | later |
| Shadowkeep — beyond the walls (later revisits) | items that matter, tape save/load, multiple keeps, secrets & lore, atmospheric cycles, collection endings | later |

Sub-arcs of pass 1 (illustrative; full detail in [per-unit-plan.md](per-unit-plan.md)):
**1.1 Into the Keep** — Hooded Figure · First Hall (dither) · A Place to Move · The Keep's Hand.
**1.2 A Keep of Rooms** — Room Graph · Through the Doorway · The Hero Remembers · Three Rooms.
**1.3 Mood and Light** — Light and Shadow · Furnishings · Mood through Constraint · A Keep with Character.
**1.4 The Keep Has a Voice** — footsteps/SFX · the gold goal · a beeper theme · the title→explore→win→title loop · real hardware.

**Deprecation-pair seeds** (what later games upgrade): cell-snapped movement → pre-shift (Smooth Motion); single-draw sprite → masking (Overlap); flat draw order → Y-sort + isometric (Greypeak).

---

## 12. Build status (2026-06-02)

**All 16 units authored, verified on Emu198x, and live — the Place is complete (Arc 1 done).** Sub-arcs 1.1–1.4 all shipped: identity → dithered stone → movement → room-as-data → graph → doorways → persistence → three rooms → lighting → furnishings → mood → character → footsteps/door SFX → the gold goal + win → a D-minor beeper theme → the title→play→win→title loop. The Place is a finishable, replayable cell-based flick-adventure. Verified via Emu198x screenshot (render + title screen) and beeper audio capture. **Deferred:** a video-capture-quality bump + recapture of the dither-heavy units (2, 3, 9–12) with crisp output. See [per-unit-plan.md](per-unit-plan.md) and the [tracker](../../../../tracker/revamp.md).

---

## 13. Vault tie-ins

Every reference from a shipped unit must resolve (Definition of Done; vault is a launch artefact — [october-2026-launch-spec.md](../../../../decisions/october-2026-launch-spec.md), [lesson-references.md](../../../../tracker/lesson-references.md)).

- **Games:** [Atic Atac](/vault/games/atic-atac), [Knight Lore](/vault/games/knight-lore), Sabre Wulf, Pentagram, Underwurlde, Cybernoid II, The Hobbit.
- **Studios / people:** Ultimate Play the Game (Tim & Chris Stamper); Hewson (via Cybernoid II); Melbourne House (via The Hobbit); [Tim Follin](/vault/people/tim-follin).
- **Hardware refs:** the attribute system (dither/lighting), bitmap memory layout, beeper / port `$FE`.

---

## 14. Risks

1. **Beeper title composition (sub-arc 1.4).** One voice, no harmony — all melody and timing. [beeper-spec.md](beeper-spec.md) scaffolds it; fall back to a paid composer if it stalls.
2. **Atmosphere bar.** The Place lives or dies on the *look* — the dither ramps, the lighting, the furnished rooms reading as a real keep. Iterate the tiles and palettes until a screenshot passes the magazine test.
3. **Authoring rate against October.** Pass 1 + three other Spectrum launch artefacts (BASIC V1 done, landing page done, vault in progress). The October floor (1.1–1.2) is already met, which de-risks this.
4. **Capture fidelity for dithering.** Fine dither is high-frequency; mp4 video averages it to flat colour. Dither-heavy units use crisp PNG stills; a video-pipeline bump + recapture is deferred work.

---

## Changelog

- **v3.1 (2026-06-02):** Sub-arc 1.4 (audio + the complete game loop) authored and verified — the Place is **complete at 16 units** (Arc 1 done). Build status updated; SFX driver, gold goal/win, D-minor beeper theme, and title→play→win→title state machine all live.
- **v3.0 (2026-06-02):** Rewritten for the cell-based **Place** (pass 1) under the module model. The three engine commitments (pre-shift/masked sprites, Y-sort, decoupled collision) removed as Shadowkeep content and noted as **relocated** to the rendering games; engine-first specs archived under `superseded/`. Scope reframed from 64-unit/four-arc to a game across modules with illustrative counts; **bitmap dithering** named as the signature technique. Build status (Units 1–12 live) added. Genre, ancestors, atmosphere, audio, level, anti-goals and vault tie-ins carried forward from v2.0 (reworded off the old engine where needed).
- **v2.0 (2026-05-20):** Consolidated engine-first brief — 32-unit Arc 1+2 October / 64-unit four-arc full game; three engine commitments as the core remix; "attribute byte = rulebook" retired in favour of tile-map collision. Superseded by v3.0; preserved in git.
- **v1.0 (2026-05-13):** Initial brief — 256-unit / 17-phase framing, October vertical slice. Superseded.
