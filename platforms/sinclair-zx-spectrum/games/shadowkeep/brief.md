# Shadowkeep — Brief

**Title (working):** Shadowkeep
**System / Track:** ZX Spectrum / Assembly
**Position:** Volume 1, Game 1 of 44 (per [decisions/spectrum-assembly-track.md](../../../../decisions/spectrum-assembly-track.md))
**Headline (design concept):** *Atmosphere (Sense of Place)*
**Total scope:** 64 units across 4 arcs (per [decisions/shadowkeep-four-arc-framing.md](../../../../decisions/shadowkeep-four-arc-framing.md))
**October 2026 ship:** Arcs 1+2 — 32 units (per [decisions/shadowkeep-32-unit-commitment.md](../../../../decisions/shadowkeep-32-unit-commitment.md))
**Constraint position:** Period-faithful through Arcs 1-2; period-possible techniques arrive in Arcs 3-4
**Status:** Active. v2.0 (2026-05-20) — consolidated from v1.0 brief + Phase 1 design doc into a single current-state document aligned to the 32-unit / four-arc framing.

Formal spec format: [docs/specifications/brief.md](../../../../specifications/brief.md). Companion docs (all in this folder): [per-unit-plan.md](per-unit-plan.md) (the canonical 32-unit reference), [engineering-plan.md](engineering-plan.md), [memory-budget.md](memory-budget.md), [object-system.md](object-system.md), [sprite-shifter.md](sprite-shifter.md), [tile-map.md](tile-map.md), [beeper-spec.md](beeper-spec.md).

---

## 1. Pedagogical Role

Teach the ZX Spectrum's craft tradition at commercial bar: pixel-level sprite movement, masked drawing, Y-sorted layered rendering, decoupled attribute and collision, hand-pixelled tiles, beeper composition, attribute-driven atmosphere. By the end of Arc 2 the learner has built a complete three-room flick-adventure at the bar of *Atic Atac*, *Knight Lore*, and *Cybernoid II* — a game CRASH would have reviewed. Subsequent volumes inherit Shadowkeep's engine vocabulary (Y-sort, masking, tile-collision) as their Trunk Layers; Shadowkeep is the curriculum's engine introduction, not just its first game.

The headline *Atmosphere (Sense of Place)* traces back through every unit. Every technique decision serves the player's sense of being *in* the keep.

---

## 2. Classic Ancestors

Three reference points, ordered by load-bearing weight:

- ***Atic Atac*** (Ultimate, 1983) — multi-room top-down adventure with Y-sorted layered rendering. The engine archetype. 148 rooms in 48K.
- ***Knight Lore*** (Ultimate, 1984) — atmospheric monochrome, masked sprite, animated character with weight. The mood archetype.
- ***Cybernoid II*** (Hewson, 1988) — dense visual design, hand-crafted level art, Tim Follin music. The polish archetype.

Flick-adventure lineage extends to *Sabre Wulf* (Ultimate, 1984), *Pentagram* (Ultimate, 1986), and *Underwurlde* (Ultimate, 1984). Shadowkeep's Arcs 3-4 inherit from these for items / multiple keeps / atmospheric cycles per the genre-honesty discussion in [decisions/shadowkeep-four-arc-framing.md](../../../../decisions/shadowkeep-four-arc-framing.md).

Opening-screen archetype: ***The Hobbit*** (Melbourne House, 1982) — economical title presentation, sparse but suggestive.

---

## 3. Remix Unit

**Same flick-adventure tropes, the engine evolution is the curriculum.** The Ultimate top-down keep-exploration tropes are preserved (hooded figure, multi-room layout, find-the-thing-and-escape, environmental hazards). What's new — and what makes this a *curriculum* rather than a *clone* — is that the engine evolves progressively across Arc 1, with each sub-arc introducing one of the three commercial-bar engine commitments:

1. **Pixel-level sprite movement.** Hero moves 2 or 4 pixels per frame, not 8. Pre-shifted sprite tables (8 versions per sprite, one per X-offset 0-7). Masked sprite drawing preserves background pixels. Introduced Sub-arc 1.2.
2. **Back-to-front layered rendering.** Y-sorted object list, drawn each frame. Hero passes behind pillars with lower Y; in front of pillars with higher Y. Introduced Sub-arc 1.3.
3. **Decoupled attribute / collision.** Collision lives in a separate tile-map data structure. Attribute bytes become purely cosmetic — used for lighting, decoration, mood. Introduced Sub-arc 1.4.

The earlier "every game rule is a bit-test on the attribute byte" mechanic (which defined the original 16-unit Arc 1 spine) is retired. Attribute remains the **visual vocabulary** — cells still look like floor, wall, treasure, hazard via attribute composition — but the game's *rules* read from a separate tile-map.

---

## 4. Core Experience

Walk the keep one pixel at a time, reading colour-coded space before stepping into it. The pleasure is in pattern recognition — learning to read the keep's vocabulary at a glance, then exploring confidently as it becomes intuitive. The game rewards careful observation rather than twitch reflex; a single session is a slow build of mastery over a small, dense, hand-painted world.

What the player feels: *atmosphere*. What the design teaches: *sense of place* as a generalisable design concept — that constraint-rich worlds become memorable through what they show, not what they say.

---

## 5. Constraint Position

**Period-faithful through Arcs 1-2.** Every technique used in October ship — from the unit-1 framebuffer poke to the unit-32 verified Spectrum Next hardware test — appeared in commercial Spectrum games of 1984-89. A 1987 Ultimate or Hewson developer could have built any unit using only techniques in their day-to-day toolbox.

**Arcs 3-4** introduce period-possible techniques (tape save/load, more sophisticated location data, time-of-day cycles) — all post-October.

**Hardware in active use (Arcs 1-2):**
- Bitmap memory ($4000-$57FF) — hand-pixelled tiles, masked sprite drawing
- Attribute memory ($5800-$5AFF) — purely cosmetic; lighting, mood, room theming
- Port `$FE` — keyboard half-row scanning + beeper bit 4
- IRQ-driven update loop at 50Hz
- ROM-font character output (HUD)

**Hardware reserved for later arcs:**
- Tape save/load (Arc 3 Sub-arc 3.3)
- Bank-switched 128K rooms (later post-October — possibly Arc 5+)
- AY-3-8912 audio (deferred — flick-adventure tradition is beeper)

**Hardware deliberately avoided in Shadowkeep entirely:**
- Software pixel scrolling — reserved for V3 entries (Ironstreak, Skylash)
- Modern-scene techniques (Saukas-era 8x1 multicolour, post-2010 AY tricks) — out of scope
- Combat state machine, projectile system, character classes — redistributed to V1.6 Embergate, V1.7 Lantern Path, V3.17 Hostraider, V3.20 Edge of Iron per the genre-honesty table

---

## 6. Visual Direction

**Hand-pixelled stonework.** The keep's walls are designed tiles, not stippled blocks. By Unit 4, multiple wall types (plain stone, decorated stone, corner pieces, arched lintels) read as built architecture rather than abstract grid. Reference: Atic Atac's per-room tile palettes.

**Cell visual vocabulary** (attribute-driven, collision-decoupled):

| Cell | Attribute composition | Role |
|---|---|---|
| Floor | PAPER 7 (white), INK 0 | clean walking surface |
| Wall | INK 1 (blue) on PAPER 1 | solid stone (cosmetic — collision via tile-map) |
| Open door | PAPER 5 (cyan), INK 0 | humming, passable |
| Locked door | PAPER 5 + FLASH | pulsing cyan, requires key |
| Treasure | PAPER 6 (yellow) + BRIGHT | gold, collectible |
| Key | PAPER 6 + BRIGHT + FLASH | gold *and* shining, distinct from treasure |
| Hazard | PAPER 2 (red) + FLASH | pulsing shadow, deadly |
| Exit | PAPER 4 (green) | the winning cell |

Each room can shift its base PAPER colour for mood — dungeon cool, kitchen warm, cloister magenta. Wall colour stays INK 1 for visual consistency. **Forbidden combination:** never PAPER 2 (red) for floor — the hero is INK 2 (red) and would vanish.

**Sprite ambition (per arc):**

- **Sub-arc 1.2 (Units 5-8):** Single-frame hooded thief, then four-frame walk cycle, then pixel-level positioning + pre-shifted sprites, then masked drawing
- **Sub-arc 2.1 (Units 17-20):** Hero idle animation
- **Sub-arc 2.2 (Units 21-24):** Wandering shadow enemies — 2 NPC types with animation
- **Arc 3+ post-October:** Item active states (torch lit, glyph revealed), more enemy variation

**Layered depth (Sub-arc 1.3):** Decorative objects (pillars, altars, sconces) sit in a Y-sorted object list. The hero passes behind objects with lower Y, in front of objects with higher Y. Attribute-driven lighting near torches.

**Per-room visual richness target.** Every room visually distinct. Atmospheric details via PAPER variation, attribute composition, and Y-sorted decorative objects. Each room should be identifiable from a screenshot alone.

**Magazine-screenshot test.** A screenshot of the antechamber at sub-arc 1.3 endpoint: cool blue PAPER for floor, magenta-tinted walls, a stone pillar with the hero passing behind it, a single FLASH cyan door humming at the eastern wall, attribute-driven torchlight rim near a sconce. Reads as atmospheric, period-correct, instantly Spectrum. A *Crash* reviewer in 1987 would have screenshotted this.

---

## 7. Audio Direction

**Title music.** Single-voice beeper, ~30-60 seconds, looping. D minor, ~110 BPM. *Manic Miner*'s "In the Hall of the Mountain King" precedent — period-faithful beeper carrying a real melody, monophonic and noisy but composed with care. Full composition spec in [beeper-spec.md](beeper-spec.md). Lands Unit 15.

**Pre-music in-game (Arc 1):** Period-correct silence broken only by event SFX. Atic Atac was largely silent in-game; we honour the precedent.

**SFX layers:**
- **Sub-arc 1.4 (Unit 14):** SFX driver introduced (door open, treasure pickup, hazard hit, victory)
- **Sub-arc 2.1 (Unit 17):** Footstep SFX overlay during movement; animated doors gain creak
- **Sub-arc 2.4 (Unit 31):** SFX library expansion + music polish pass

**Arc 4 (post-October):** Atmospheric layer (wind, distant echoes) interleaved on the single beeper channel; remains period-faithful.

**Sound integration.** Music and SFX share port `$FE` bit 4 via interleaved scheduling — music can be temporarily preempted by an SFX event. AY-3-8912 work is deferred — flick-adventure tradition is beeper, and AY arrives elsewhere in the curriculum (V2.16 Witch's Year introduces; V3.17 Hostraider deepens per [decisions/spectrum-assembly-track.md](../../../../decisions/spectrum-assembly-track.md)).

---

## 8. Level Design Direction

**Scale per arc:**

| Arc | Rooms | Notes |
|---|---|---|
| Arc 1 (October) | 2 designed rooms | Great Hall + Antechamber; hand-pixelled tilework |
| Arc 2 (October) | 3 designed rooms | Plus a third room introduced in Sub-arc 2.3; HUD + room names |
| Arc 3 (post-October Year 1) | + outdoor traversal + 2-3 areas beyond original keep | Multi-location traversal via per-location state |
| Arc 4 (post-October Year 2) | + 2-3 distinct additional keeps | Outdoor traversal between locations; collection-based endings |

Pre-procedural; every room hand-designed. The 16-room and 9-room scopes from earlier framings are retired — Arc 1+2 prioritises depth (three rooms at the visual/atmospheric bar of *Knight Lore*) over breadth.

**Pacing.** The keep eases the player in. The Great Hall (Sub-arc 1.4) is safe — treasure, an open door. The Antechamber (Sub-arc 1.3) introduces the layered-rendering depth and the lighting work. Arc 2's third room (Sub-arc 2.3) introduces the score / HUD systems against the player's growing familiarity.

**Signposting.** The attribute palette *is* the signposting. There is no in-game tutorial. The colour vocabulary is consistent; once the player has read each cell type once, the rules are learned.

**Difficulty curve.** Forgiving early, peak at 1987 chops by Arc 2 sub-arc 2.2 (NPCs introduce twitch-reflex). Per the difficulty discussion in [docs/log.md](../../../../log.md) and [decisions/real-retro-games.md](../../../../decisions/real-retro-games.md). Peak difficulty sits where *Sabre Wulf* sat — memorable, occasionally unfair-feeling in the way good 1987 budget games were.

**Onboarding.** The first five minutes teach the player: cells have colour, colour means something, the hero responds to QAOP or arrows, doors lead between rooms, treasure is good, hazards are bad, the exit is somewhere worth finding. Nothing said in prose — everything said in colour and layered space.

---

## 9. Polish Direction

**Title screen.**
- **Sub-arc 1.4 (Unit 16):** Hand-pixelled title screen with logo art. Beeper theme playing. "Press any key to enter."
- **Sub-arc 2.4 (Unit 32):** Title art polish + victory sequence + "completed" state.

**Attract mode:** post-October (Arc 3 stretch).

**Options:**
- Arc 2: sound on/off
- Arc 2.4 / Arc 3: control remap (QAOP, cursor keys, Kempston joystick)
- Post-Arc 4: difficulty levels (post-October)

**Ending:**
- Arc 1 (Sub-arc 1.4): Title → play → victory → title loop
- Arc 2 (Sub-arc 2.4): "Completed" state with credit; final presentation pass
- Arc 4 (post-October): Collection-based true ending (find all lore items for full ending)

**Accessibility:**
- Control remap (Arc 2.4)
- FLASH-off option for photosensitivity (post-October stretch)
- ROM-font HUD text remains legible at all stock Spectrum colour combinations

**"Shippable" criteria.** Arc 2 endpoint Shadowkeep should be playable cleanly on Spectrum Next + Fuse for ten-plus minutes per session, never confuse a first-time player about the goal, and could plausibly be uploaded to Itch.io alongside contemporary indie retro work as a small-but-polished release in the *Atic Atac* / *Knight Lore* tradition. By Arc 4 endpoint, the same Itch.io upload would read as a mid-tier full-price release with multi-keep scope and collection-based completion.

---

## 10. Anti-goals

- **No combat, no weapons.** The hooded thief is a stealth intruder. Design is exploration-and-avoidance. Combat-as-mechanic lives in V3.20 Edge of Iron; action-RPG lives in V1.6 Embergate. See [decisions/shadowkeep-four-arc-framing.md](../../../../decisions/shadowkeep-four-arc-framing.md) Genre Honesty table.
- **No character class choice.** Single hero, single playstyle. Class systems live in V1.6 Embergate.
- **No parser dialogue, no quest state, no branching narrative.** Lives in V1.7 The Lantern Path.
- **No full Singleton-class location-graph or day/night cycle.** Lives in V1.4 Whitewinter (Lords of Midnight tradition); Shadowkeep Arc 4 uses a lighter mood-palette variation only.
- **No save/load in Arcs 1-2.** Arrives in Arc 3 Sub-arc 3.3 (tape save/load).
- **No software pixel scrolling within rooms.** Reserved for V3 entries (Ironstreak, Skylash). Shadowkeep is screen-flip on room transitions.
- **No isometric projection.** Reserved for V1.2 Greypeak (Knight Lore tradition).
- **No procedural generation.** Every room hand-designed. Discovery comes from learning the keep's geography.
- **No modern-scene techniques.** Shadowkeep is period-faithful through Arcs 1-2; period-possible in Arcs 3-4.
- **No unit-count creep within October.** 32 units is the commitment. Surplus time goes into polish within the existing units, not new units. (Per [decisions/shadowkeep-32-unit-commitment.md](../../../../decisions/shadowkeep-32-unit-commitment.md) drift triggers.)
- **No vertical-slice framing creeping back into marketing copy.** What ships is *"Shadowkeep, Arc 1 + Arc 2: foundations, a place, inhabitants, identity. The first chapter of a longer game."* Not a slice, not a demo, not a vertical-anything.

---

## 11. Arc Trajectory

**Total: 64 units across 4 arcs of 16. October 2026 ships Arcs 1+2.**

Each arc has four sub-arcs of four units. Each sub-arc has a thematic identity; each unit has a single specific contribution. Full per-unit detail lives in [per-unit-plan.md](per-unit-plan.md).

| Arc | Theme | Sub-arcs (units) | Status |
|---|---|---|---|
| **Arc 1** | *Foundations and a Place* | 1.1 First Pixels (1-4); 1.2 The Hooded Thief (5-8); 1.3 A World with Depth (9-12); 1.4 The Keep Stands (13-16) | **October ship** |
| **Arc 2** | *Inhabitants and Identity* | 2.1 Sound and Motion (17-20); 2.2 A Presence in the Dark (21-24); 2.3 A Game Knows Itself (25-28); 2.4 Completion (29-32) | **October ship** |
| **Arc 3** | *Beyond the Walls* | 3.1 Items that Matter (33-36); 3.2 Beyond One Keep (37-40); 3.3 The Persistent Hero (41-44); 3.4 Secrets and Lore (45-48) | post-October Year 1 |
| **Arc 4** | *The Greater World* | 4.1 Atmospheric Cycles (49-52); 4.2 Multiple Keeps (53-56); 4.3 Endings (57-60); 4.4 Completion (61-64) | post-October Year 2 |

### Per-arc end-state deliverable

**End of Arc 1 (16 units):** A complete two-room game with atmosphere, depth, and a designed first impression. Title → play → victory → title loop. Hand-pixelled tiles, hooded thief animated with weight, pillars the hero walks behind, atmospheric lighting near torches, gold cells with sparkle, composed beeper title music, hand-pixelled title screen with logo art.

**End of Arc 2 (32 units, October ship):** A three-room game with inhabitants, lives, score, HUD, atmospheric polish, and verified real-hardware playability on Spectrum Next. Footstep SFX, animated doors, hero idle animation, varied floor tiles, a moving NPC, hero-vs-NPC collision, lives and respawn, HUD bar (score / gold / lives), room names, score persistence, atmosphere polish across all rooms, audio depth, final presentation pass.

**End of Arc 3 (48 units, post-October Year 1):** Inventory with 6+ item types; multi-location traversal with 2-3 areas beyond the original keep; working tape save/load on real hardware; secrets-and-lore system with hidden content the player must discover.

**End of Arc 4 (64 units, post-October Year 2):** Time-of-day cycle; 2-3 distinct additional keeps; collection-based true-ending unlock; final polished build on real Spectrum Next + TZX 48K. The complete game.

### Spiral revisits across arcs

- Arc 2 revisits **movement** (now interleaved with animation timing), **the beeper driver** (now handles SFX overlay), **the hero sprite** (now multi-frame with idle), **rendering** (now with NPCs in the Y-sort list).
- Arc 3 revisits **collision** (now extends to inventory-affecting items), **room engine** (now multi-location traversal), **game state** (now must persist and restore via tape).
- Arc 4 revisits **atmosphere** (now with time-of-day variation), **endings** (now collection-based), **integration** (final polish across all rooms and systems).

### Cut hierarchy (per shadowkeep-32-unit-commitment)

If runway tightens during October, cut order works backwards from Sub-arc 2.4:

1. Trim Sub-arc 2.4 (units 29-32) — *Completion* polish defers. 28 units remains.
2. Trim Sub-arc 2.3 (units 25-28) — HUD and room names defer. 24 units remains.
3. Trim Sub-arc 2.2 (units 21-24) — NPCs and lives defer. 20 units remains. **Real lowest acceptable floor.**
4. Trim Sub-arc 2.1 (units 17-20) — Arc 1 alone (16 units). **Genuine retreat — requires re-marketing.**
5. Below 16: decision-record violation.

Cuts apply only after a runway slip is identified. Default plan is *both arcs, 32 units, October.*

---

## 12. Ship Test (Multi-axis)

Per-sub-arc pass criteria across the five disciplines. Each sub-arc passes only when *every* axis clears its row at the relevant bar. Definition of Done in [docs/tracker/revamp.md](../../../../tracker/revamp.md) applies to every unit in addition.

| Sub-arc | Code | Visuals | Audio | Level design | Polish |
|---|---|---|---|---|---|
| 1.1 First Pixels (1-4) | Framebuffer fundamentals stable; tile-map data structure; assembles on Fuse + Spectrum Next | Stone tiles hand-pixelled at mid-tier full-price bar; varied wall types; Great Hall composed | n/a | Great Hall reads as a designed room, not a grid | Tile-map and attribute decoupling clean |
| 1.2 The Hooded Thief (5-8) | Pre-shifted sprite tables generated; pixel-level positioning; masked drawing preserves background | Hooded thief sprite reads on a magazine cover at 8×8; 4-frame walk cycle has weight | n/a (silent) | Movement feels fluid (2-4 pixels per frame) | Animation polish: hero feels alive |
| 1.3 A World with Depth (9-12) | Y-sorted object list draws each frame; hero passes behind/in-front correctly | Decorative objects (pillars, altars, sconces) hand-pixelled; attribute-driven lighting visible near torches | n/a | Antechamber as designed second place; the room reads three-dimensional | Atmospheric depth from layered objects + lighting |
| 1.4 The Keep Stands (13-16) | Tile collision works (decoupled from attribute); SFX driver introduced | Hand-pixelled title screen with logo art at magazine bar | Beeper title theme composed per beeper-spec.md; door open + treasure pickup SFX | Title → play → victory → title loop tight; first-time player understands goal in <60s | Title screen + theme + clean restart — Arc 1 complete |
| 2.1 Sound and Motion (17-20) | Footstep timing stable at IRQ rate; door animation primitive | Animated doors; hero idle animation; varied floor tiles read as different | Footstep SFX overlay on beeper; doors creak | Sound supports place without overwhelming | Animation: keep feels inhabited |
| 2.2 A Presence in the Dark (21-24) | NPC AI deterministic but unpredictable; hero-vs-NPC collision; lives + respawn | First NPC sprite animated and distinct from hero; second NPC variation reads as different threat | NPC proximity beeper cue | NPC placement supports avoidance gameplay; not gotcha | Dynamic feel: rooms have life |
| 2.3 A Game Knows Itself (25-28) | HUD render robust; score persistence across death | HUD bar visually clean (score / gold / lives); room names render in ROM font at top centre | Score-tick SFX subtle | Third designed room introduces new spatial puzzle | HUD reads as professional |
| 2.4 Completion (29-32) | No regressions across Arcs 1-2; runs cleanly on real Spectrum Next | Atmosphere polish across all rooms; victory sequence polished | SFX library expansion + music polish | Final balance pass on cell placement | "Completed" state; Arc 2 deliverable shippable |

Arc 3 / Arc 4 ship tests defined post-October.

---

## 13. Pattern Library Extractions

Reusable techniques Shadowkeep surfaces for promotion to the Pattern Library, per [decisions/pattern-library.md](../../../../decisions/pattern-library.md). Promotion happens when a technique proves reusable across multiple games.

**Framework:**
- **Incremental scaffold pattern** — Unit 1 starts from nothing; each unit adds one capability. Cross-platform.
- **Spiral revisit pattern** — phase boundaries revisit earlier work at higher levels. Cross-platform (also a curriculum-wide principle per [decisions/spiral-and-incremental.md](../../../../decisions/spiral-and-incremental.md)).
- **Multi-room engine** — room pointer table, N/S/E/W connection tables, current-room state byte, generalised transition. Cross-platform.
- **Game state machine** — title → play → win/die → restart loop. Cross-platform.

**Rendering (Spectrum-specific in implementation; design ideas cross-platform):**
- **Pre-shifted sprite tables** — 8 versions per sprite for sub-cell horizontal positioning. Spectrum-specific.
- **Masked sprite drawing** — mask + image two-pass write preserves background. Spectrum-specific implementation; the design pattern (alpha-style masking) is cross-platform.
- **Y-sorted object list** — back-to-front draw order from a sorted list. Cross-platform.
- **Decoupled attribute / tile-map / collision** — visual vocabulary, game data, and collision query as three separate stores. Cross-platform conceptually.
- **Hand-pixelled tile palette** — multiple wall/floor tile types loaded from a designer-authored tile set. Cross-platform.
- **Attribute-driven lighting** — atmospheric mood via attribute composition near sources. Spectrum-specific (uses attribute granularity); idea generalises.
- **HUD layout pattern** — lives / score / inventory / room-name strip in screen top rows. Cross-platform.

**Input:**
- **Port `$FE` half-row keyboard scanning** — Spectrum-specific.
- **Control remap pattern** (Arc 2.4 surfacing) — translates physical input to game commands. Cross-platform.

**Physics (loosely):**
- **Tile-map collision query** — hero position resolves to tile coordinates; collision answered by tile-map lookup. Cross-platform.

**Audio:**
- **Single-voice beeper melody driver** — Spectrum-specific (port `$FE` bit 4 toggle, tick-counter timing).
- **SFX overlay on single-channel** (Sub-arc 1.4 surfacing) — channel-sharing interleaving. Cross-platform design pattern.

**AI:**
- **Wandering NPC AI** (Sub-arc 2.2 surfacing) — random walk + chase patterns. Cross-platform.
- **Per-object behaviour state machine** — Cross-platform.

**Assembly (language-specific):**
- Z80 idioms surfaced repeatedly: pre-shifted sprite table lookup; masked sprite inner loop; tile address arithmetic; `DJNZ` loops; `LDIR` for tile blits; stack-as-data for object lists.

---

## 14. Vault Tie-ins

Vault entries this curriculum threads through. Per the Definition of Done in [docs/tracker/revamp.md](../../../../tracker/revamp.md), every reference must resolve. Status (✓ live / GAP needs creating) noted.

**Direct ancestors (Arcs 1-2):**
- [Atic Atac](/vault/games/atic-atac) — Ultimate, 1983. The engine archetype. Referenced throughout.
- [Knight Lore](/vault/games/knight-lore) — Ultimate, 1984. The mood archetype.
- [Cybernoid II](/vault/games/cybernoid) — Hewson, 1988. The polish archetype.

**Flick-adventure lineage references (Arcs 3-4 referencing):**
- Sabre Wulf (Ultimate, 1984)
- Pentagram (Ultimate, 1986)
- Underwurlde (Ultimate, 1984)
- The Hobbit (Melbourne House, 1982) — opening-screen archetype

**Studio entries:**
- Ultimate Play the Game — referenced in Arcs 1-2 ancestry; also throughout Arcs 3-4
- Hewson Consultants — referenced via Cybernoid II
- Melbourne House — referenced via The Hobbit

**People entries:**
- Tim and Chris Stamper (Ultimate founders) — referenced indirectly via Atic Atac / Knight Lore / Sabre Wulf
- [Tim Follin](/vault/people/tim-follin) — referenced via Cybernoid II audio

**Hardware reference pages:**
- ZX Spectrum attribute system — referenced in Sub-arc 1.1 and 1.3 (lighting work)
- ZX Spectrum beeper / port `$FE` — referenced in Sub-arc 1.4 (SFX driver) and Unit 15 (title theme)
- ZX Spectrum bitmap memory layout — referenced in Sub-arc 1.1 (framebuffer fundamentals)

**Pattern-library cross-references:** every pattern listed in Section 13 will cross-link back here from its pattern entry.

Vault completeness is a launch artefact — see [docs/decisions/october-2026-launch-spec.md](../../../../decisions/october-2026-launch-spec.md) and [docs/tracker/lesson-references.md](../../../../tracker/lesson-references.md).

---

## Risks

1. **Engine evolution must read clearly across Arc 1.** The three engine commitments are introduced progressively, each replacing simpler precedents (cell-snapped → pre-shifted; single-draw → Y-sort; attribute-collision → tile-map-collision). Each transition needs to land as a *teaching moment*, not a refactor. Mitigation: per-unit-plan explicitly names the deprecation pair in each transitional unit; existing 8 published units stay live until each is hard-replaced (per [decisions/shadowkeep-32-unit-commitment.md](../../../../decisions/shadowkeep-32-unit-commitment.md) — engine evolution is the curriculum).

2. **Pixel-art bar is the load-bearing visual risk.** Sub-arc 1.2's hooded thief sprite and Sub-arc 1.1's stone tile palette are the magazine-cover artefacts. If they don't land at the bar, the entire Arc 1 deliverable misses commercial bar. Mitigation: multiple iterations expected; treat the sprite as the project's single most-load-bearing piece of pixel art.

3. **Beeper title composition (Unit 15).** Beeper music is unforgiving — one voice, no harmony, all timing and melody. The October launch hinges on the title theme landing. Mitigation: [beeper-spec.md](beeper-spec.md) scaffolds the composition; if Steve's composition stalls, fall back to a paid composer per the Cadence approach in [docs/tracker/revamp.md](../../../../tracker/revamp.md).

4. **Build-before-publish window.** The new engine (pre-shifted sprites, masked drawing, Y-sort, tile-collision, pixel-art tooling, music workflow) requires ~1-2 months of infrastructure work before any new units publish. During that window, visitors see the existing 8 units at the old engine bar. Mitigation: communicate the engine evolution story; the early new units carry the case for the rest.

5. **Authoring rate against October.** Thirty-two multi-disciplinary units against the engine-evolution commitment, alongside three other Spectrum launch artefacts (BASIC Volume 1, landing page, vault). Runway tight. Mitigation: cut hierarchy in [decisions/shadowkeep-32-unit-commitment.md](../../../../decisions/shadowkeep-32-unit-commitment.md) trims Arc 2 sub-arcs back-to-front; BASIC track has separate cut hierarchy.

6. **Sub-arc 2.2 NPC dynamic-spike risk.** Adding the first moving NPC to the Y-sort list (Unit 21) is a non-trivial integration — the object list now contains the hero plus NPCs, all Y-sorted, all with per-frame movement and collision queries. Mitigation: prototype the multi-object Y-sort + collision pass ahead of Sub-arc 2.2 authoring.

7. **Real-hardware testing target (Sub-arc 2.4).** Unit 31 is "Spectrum Next hardware testing" — a real-hardware-only discipline. Mitigation: real Spectrum Next access confirmed; testing cadence scheduled per [engineering-plan.md](engineering-plan.md).

8. **Genre-drift in Arcs 3-4 planning.** Combat / classes / parser / branching narrative are NOT Shadowkeep — they're redistributed to V1.6 Embergate, V1.7 Lantern Path, V3.17 Hostraider, V3.20 Edge of Iron per [decisions/shadowkeep-four-arc-framing.md](../../../../decisions/shadowkeep-four-arc-framing.md). If future-session work reaches for those mechanics within Shadowkeep, that's drift to flag.

---

## Changelog

- **v2.0 (2026-05-20):** Consolidated from v1.0 brief + `shadowkeep-phase-1-design.md` + `shadowkeep-unit-3-plan.md` into a single current-state document. Aligned to 32-unit Arc 1+2 October commitment (per [decisions/shadowkeep-32-unit-commitment.md](../../../../decisions/shadowkeep-32-unit-commitment.md)) and four-arc full-game framing (per [decisions/shadowkeep-four-arc-framing.md](../../../../decisions/shadowkeep-four-arc-framing.md)). Three engine commitments (pixel-level sprite movement, Y-sorted layered rendering, decoupled attribute/collision) introduced as the core remix. Genre honesty: combat / classes / parser / branching narrative are NOT Shadowkeep, redistributed to canonical-legend games per the redistribution table. Reference points expanded from *Atic Atac / Sabre Wulf* to *Atic Atac / Knight Lore / Cybernoid II*. Phase trajectory restructured from 17 phases / 256 units to 4 arcs / 64 units (with Arcs 3-4 post-October). Per-unit detail delegated to [per-unit-plan.md](per-unit-plan.md). The earlier "attribute byte is the rulebook" mechanic retired; attribute remains visual vocabulary, collision lives in a separate tile-map.
- **v1.0 (2026-05-13):** Initial brief. First brief authored against `docs/specifications/brief.md` v1.0. Anchored 256-unit total scope, 17-phase trajectory, period-faithful constraint position, mid-tier full-price endpoint bar, October vertical-slice deliverable. Superseded by v2.0 above; preserved in git history.
