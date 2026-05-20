# Shadowkeep — Brief

**Title (working):** Shadowkeep
**System / Track:** ZX Spectrum / Assembly
**Position:** Game 1 of 4
**Target unit count:** 256
**Constraint position:** Period-faithful (across all phases) — see Section 5
**Status:** Active (v1.0, 2026-05-13)

Formal spec: [`docs/specifications/brief.md`](../../../../specifications/brief.md). Companion design doc: [`knowledge/curriculum/shadowkeep-phase-1-design.md`](../../../../../knowledge/curriculum/shadowkeep-phase-1-design.md). Composition spec: [`docs/platforms/sinclair-zx-spectrum/games/shadowkeep/beeper-spec.md`](../../../../../platforms/sinclair-zx-spectrum/games/shadowkeep/beeper-spec.md).

---

## 1. Pedagogical Role

Teach the ZX Spectrum's attribute system as the entirety of game logic — every gameplay rule is a bit-test on a single attribute byte — so the reader leaves with the platform's defining hardware feature as a working tool that subsequent games build on.

---

## 2. Classic Ancestors

*Atic Atac* (Ultimate, 1983) and *Sabre Wulf* (Ultimate, 1984). Both are top-down, multi-room, find-the-thing-and-escape adventures from the 1983–84 Ultimate Play the Game catalogue, defining the attribute-driven Spectrum adventure genre.

---

## 3. Remix Unit

**Same tropes, new core mechanic.** The Atic Atac top-down keep-exploration tropes are preserved (hooded figure, multi-room layout, find-and-escape, environmental hazards) — but the mechanic is "every game rule is a bit-test on the screen attribute byte." No sprites for hazards. No separate collision tables. No map editor. The screen *is* the map; the attribute byte *is* the rule.

---

## 4. Core Experience

Walk the keep one cell at a time, reading the colour-coded rules off the screen before stepping forward. The pleasure is in pattern recognition — learning to read the keep's vocabulary at a glance (walls blue, doors cyan, treasure gold, hazards red), then exploring confidently as the rules become intuitive. The game rewards careful observation rather than twitch reflex; a single session is a slow build of mastery over a small, dense, hand-painted world.

---

## 5. Constraint Position

**Period-faithful across all phases.** Every technique used by Shadowkeep — from the unit-1 attribute writes to the unit-256 turbo loader — appeared in commercial Spectrum games of the period (1984–89). A 1987 Hewson or Mikro-Gen developer with a hard project deadline could have built any phase of this game using only techniques in their day-to-day toolbox.

This is a deliberate choice. Modern-scene techniques (Saukas-era 8x1 multicolour, modern AY routines, software sprite engines codified post-2010) are reserved for a later game on the platform or remain out of curriculum scope entirely. Shadowkeep demonstrates that genuinely period-faithful Spectrum work can reach mid-tier full-price quality on its own merits.

**Hardware in active use:**

- Attribute memory ($5800–$5AFF) — INK, PAPER, BRIGHT, FLASH bits.
- Bitmap memory ($4000–$57FF) — single 8×8 hero sprite, with cell preservation underneath.
- Port `$FE` (keyboard half-row scanning + beeper bit 4).
- IRQ-driven update loop.
- ROM-font character output (HUD).
- (Later phases) AY-3-8912 on 128K, bank-switched memory pages, +3 floppy controller.

**Hardware deliberately avoided:**

- Software pixel scrolling — reserved for Game 2 (Ionfire).
- Contended-memory mastery beyond ULA-aware IRQ timing — Game 2 territory.
- Isometric projection — Game 3 (Grimstone).
- Modern-scene techniques on the Spectrum (8x1 multicolour, software sprite engines) — out of curriculum scope.

---

## 6. Visual Direction

**Palette strategy.** Eight cell types decoded from a single attribute byte:

| Cell | Attribute pattern |
|---|---|
| Floor | PAPER 7 (white), INK 0 — clean walking surface |
| Wall | INK 1 (blue) on PAPER 1 — solid stone, fixed across all rooms for collision consistency |
| Door (open) | PAPER 5 (cyan), INK 0 — humming, passable |
| Door (locked) | PAPER 5 + FLASH — pulsing cyan, requires key |
| Treasure | PAPER 6 (yellow) + BRIGHT — gold, collectible |
| Key | PAPER 6 + BRIGHT + FLASH — gold *and* shining, distinct from treasure |
| Hazard | PAPER 2 (red) + FLASH — pulsing shadow, deadly |
| Exit | PAPER 4 (green) — the winning cell |

Each room can shift its base PAPER colour to give different rooms different moods — the dungeon uses cool blue PAPER (cold), the kitchen warm yellow, the cloister magenta (otherworldly). Wall colour stays INK 1 throughout for collision-detection consistency. **Forbidden combination:** never PAPER 2 (red) for floor — the hero is INK 2 (red) and would vanish.

**Sprite ambition.**

- **Arc 1 (Phases 1–2):** single-frame 8×8 hooded thief. Symmetric (top-down — no rotation needed). No facial detail (hood reads as shadow over face). No weapon visible.
- **Arc 2 (Phases 3+):** 2-frame walking cycle. Wandering shadow enemy sprite (1–2 types initially), each with simple 2-frame animation.
- **Arc 3 (Phases 6+):** richer animation (death sequence, item-pickup feedback), more enemy types with distinct silhouettes.
- **Arc 4 (Phases 11+):** loading screen art (full hand-painted screen, magazine-quality).

**Per-room visual richness target.** Every room visually distinct. Atmospheric details via PAPER variation and attribute composition: the great hall warm and broad, the cloister cool and narrow, the dungeon cold and tight, the well-shaft vertically constrained. Each room should be identifiable from a screenshot alone.

**Visual identity.** The attribute grid *is* the visual. Shadowkeep is a hand-painted impressionist colour study where every brushstroke encodes a game rule. The constraint that produced the Spectrum's notorious "attribute clash" reputation is, here, the medium of expression.

**Magazine-screenshot test.** A screenshot of the cloister at moonlight: cool blue PAPER for floor, magenta-tinted walls, a single FLASH cyan door humming at the eastern wall, the red hero crossing the centre. Reads as atmospheric, period-correct, and instantly Spectrum. A *Crash* reviewer in 1987 would have screenshotted this.

---

## 7. Audio Direction

**Title music.** Single-voice beeper, ~30–60 seconds, looping. D minor, ~110 BPM. *Manic Miner*'s "In the Hall of the Mountain King" precedent — period-faithful beeper carrying a real melody, monophonic and noisy but composed with care. Full composition spec in [`shadowkeep-beeper-spec.md`](../../../../../platforms/sinclair-zx-spectrum/games/shadowkeep/beeper-spec.md).

**In-game music.**

- **Arc 1:** deliberately absent. Atic Atac was largely silent in-game; period-correct silence, broken only by SFX.
- **Arc 2 (Phases 3+):** ambient beeper layer introduced (occasional atmospheric tones — wind, distant echoes — interleaved on the single beeper channel).
- **Arc 4 (Phase 11+, 128K):** AY-3-8912 three-channel music in-game. 48K builds retain the silent-with-SFX experience as the fallback path.

**SFX scope.**

- **Phase 1 (vertical slice):** minimal — title theme + a few simple events (door open, hazard hit if encountered).
- **Phase 2:** full event SFX layer — door open/close, key pickup, treasure pickup, hazard hit, death, victory.
- **Arc 2+:** richer SFX (footsteps optional, layered enemy proximity tones, room-transition sounds).
- **Arc 4 (AY):** 3-channel SFX with envelope/noise; richer per-event signature.

**Sound integration.** On 48K, music and SFX share port `$FE` bit 4 via interleaved scheduling — music can be temporarily preempted by an SFX event. On 128K (Arc 4), AY chip provides 3 voices for music; SFX layer onto AY noise channel or share voices via priority. The 48K↔128K split is detected at boot and the audio pipeline branches accordingly.

---

## 8. Level Design Direction

**Scale.**

- Phase 1 (vertical slice): 2 rooms (the great hall + one adjacent connecting room).
- Arc 1 endpoint (Phase 2): 9 rooms (3×3 grid). Each room hand-designed; no procedural generation.
- Arc 2: 9 rooms remain, but the rooms become *busier* — wandering enemies, more cell types, denser gameplay.
- Arc 3: keep expands to 4×4 = 16 rooms with save/load.
- Arc 4 endpoint (Phase 12, 128K): bank-switched additional rooms; total reaches 25+.
- Game endpoint (Phase 17, 256 units): 40–60+ rooms targeted.

**Pacing.** The keep eases the player in. The first room (the great hall) is safe — treasure to collect, an open door north. Mid-keep introduces hazards and locked doors that require keys found elsewhere. Late-keep (Arc 2+) introduces wandering enemies and complex room sequences requiring multiple keys to reach the Heart. The full game's pacing rewards memorising the keep's layout while threatening with active enemies in late rooms.

**Signposting.** The attribute palette *is* the signposting. There is no in-game tutorial. A first-time player learns by stepping carefully: a single death on a flashing red cell teaches the entire hazard rule. The colour vocabulary is consistent and total; once the player has read each cell type once, the rules are learned.

**Difficulty curve.** Forgiving early, peak at 1987 chops late. Per the difficulty discussion in `docs/log.md` and `decisions/real-retro-games.md`:

- Onboarding: early rooms can be cleared without losing a life if the player reads the palette.
- Mid-game: pattern memorisation comes into play; a player may lose a life by misreading a cell.
- Late-game (Arc 2+): wandering enemies introduce twitch-reflex requirements alongside spatial memory.

The peak difficulty sits at where *Sabre Wulf* sat — challenging, memorable, occasionally unfair-feeling in the way good 1987 budget games were unfair-feeling. No skill-adaptive system; no difficulty options (deferred to Arc 4 as a stretch).

**Onboarding.** The first five minutes teach the player: cells have colour; colour means something; the hero responds to QAOP or arrows; doors lead between rooms; treasure is good, hazards are bad; the exit is somewhere worth finding. Nothing said in prose — everything said in colour.

---

## 9. Polish Direction

**Title screen.**

- Arc 1 (Phase 2): functional title — text, "press any key", beeper title theme playing.
- Arc 4 (Phase 11+): magazine-quality loading screen with hand-painted attribute art; title text using ROM font with attribute treatment; beeper theme; "press any key to enter".

**Attract mode.** Not in Phase 1 or Phase 2. Arc 3 introduces a brief gameplay-demo attract mode that engages after 60 seconds of idle on the title screen.

**Options.**

- Arc 1: sound on/off.
- Arc 2: control remap (QAOP, cursor keys, Kempston joystick).
- Arc 4: difficulty levels (easy / normal / hard) — affects enemy speed and hazard density only; the level design itself doesn't change.

**Ending.**

- Phase 1 (vertical slice): the player reaches the exit cell; "the keep stands" message; restart.
- Arc 1 endpoint: full lives system; complete title → play → win-or-die → title loop with hit-flash and brief invulnerability.
- Arc 3: narrative ending sequence — "you have recovered the Heart; the shadows recede" with discoverable backstory referenced in item descriptions.
- Arc 4: end-credits scroll (composer, designer, the team — even if it's one name); attract mode loops the title.

**Accessibility.**

- Control remap (covered above).
- Phase 12+: FLASH-off option for photosensitivity (hazards become solid red instead of flashing; visually less alarming, gameplay unchanged).
- ROM-font HUD text remains legible at all stock Spectrum colour combinations.

**"Shippable" criteria.**

A learner's Phase-2 build of Shadowkeep should be playable cleanly on Spectrum Next + Fuse for ten-plus minutes per session, never confuse a first-time player about the goal, and could plausibly be uploaded to Itch.io alongside contemporary indie retro work as a small-scope Mastertronic-tier release. By Arc 3 endpoint, the same Itch.io upload would read as a mid-tier full-price release in the Hewson/Gremlin tradition.

---

## 10. Anti-goals

- **No combat, no weapons.** The hooded thief is a stealth intruder. Design is exploration-and-avoidance, not action. *Sabre Wulf*-style monster slashing is explicitly out of scope; the bar for "intense interaction" is what Atic Atac did — dodge, run, find the key.
- **No character class choice.** Atic Atac had one (knight/wizard/serf), each with different routes. Shadowkeep deliberately doesn't — single hero, single playstyle.
- **No save/load in Arc 1.** Atic Atac had none; the 9-room keep is a memorisable run. Save/load arrives in Arc 3.
- **No software pixel scrolling.** Reserved for Game 2 (Ionfire). Shadowkeep is screen-flip on room transitions; no horizontal or vertical scrolling within rooms.
- **No isometric projection.** Reserved for Game 3 (Grimstone). Shadowkeep is straight top-down.
- **No turbo-loader theatrics in Arc 1.** Standard ROM tape loader for Phase 1–2; turbo loader arrives in Phase 13.
- **No procedural generation.** Every room hand-designed. Discovery comes from learning the keep's geography, not from a random seed.
- **No modern-scene techniques.** 8x1 multicolour, software sprite engines, post-2010 AY tricks — all out of scope. Per Section 5.
- **No vertical-slice unit count creep.** Phase 1 is 8 units. If runway slack appears, raise the per-unit bar; do not add a ninth unit (per [`october-2026-vertical-slice`](../../../../../decisions/shadowkeep-32-unit-commitment.md)).

---

## 11. Phase Trajectory

**Total: 256 units across 17 phases.** Arc 1 phases at 8 units each (the existing 16-unit spine split); subsequent phases at 16 units each.

| Phase | Units | Arc | Theme |
|---|---|---|---|
| 1 | 8 | Arc 1 | **Vertical slice (October 2026 launch)** |
| 2 | 8 | Arc 1 | Arc 1 completion — small complete game |
| 3 | 16 | Arc 2 | Animation and life |
| 4 | 16 | Arc 2 | Wandering enemies |
| 5 | 16 | Arc 2 | Audio depth |
| 6 | 16 | Arc 3 | Save state and persistence |
| 7 | 16 | Arc 3 | Scale (4×4 keep) |
| 8 | 16 | Arc 3 | Level design pass |
| 9 | 16 | Arc 4 | Narrative and ending |
| 10 | 16 | Arc 4 | Attract mode and polish pass |
| 11 | 16 | Arc 5 | 128K AY music |
| 12 | 16 | Arc 5 | Bank-switched rooms (25+ rooms) |
| 13 | 16 | Arc 5 | Turbo loader |
| 14 | 16 | Arc 5 | +3 disk version |
| 15 | 16 | Arc 6 | Multi-model compatibility |
| 16 | 16 | Arc 6 | Accessibility + options |
| 17 | 16 | Arc 6 | Final polish and packaging |

### Per-phase detail

**Phase 1 (8 units) — Vertical slice.**
- *New:* one attribute write, attribute reads, drawing a room, hero sprite design + placement, movement, attribute-based collision, room transition, beeper title theme, complete title→play→end loop.
- *Revisits:* n/a (foundational).
- *Phase-end deliverable:* two beautifully designed rooms with attribute-driven gameplay, polished hero, working room transition, beeper title theme, complete title → play → end → restart loop. Vertical slice as defined in [`october-2026-vertical-slice`](../../../../../decisions/shadowkeep-32-unit-commitment.md).

**Phase 2 (8 units) — Arc 1 completion.**
- *New:* full 9-room (3×3) keep, complete cell vocabulary (treasure, keys, locked doors, hazards, exit), lives system with hit-flash, score display, beeper SFX layer for key events.
- *Revisits:* room engine generalises from 2 rooms to 9; rendering loop optimised for repeated draws; title-screen layout extended for score and lives icons.
- *Phase-end deliverable:* a 9-room Shadowkeep, complete win/die loop, Mastertronic-budget-tier small complete game. *Atic Atac*-shaped at smaller scale.

**Phase 3 (16 units) — Animation and life.**
- *New:* 2-frame hero walking cycle, in-game beeper SFX layer with priority scheduling against music, footstep audio cues.
- *Revisits:* movement (now interleaved with animation timing), hero sprite design (multi-frame, with palette implications), beeper driver (handles SFX overlay).
- *Phase-end deliverable:* the 9-room keep with an animated hero and ambient in-game audio. Stepping toward *Sabre Wulf*-tier presence.

**Phase 4 (16 units) — Wandering enemies.**
- *New:* 1–2 wandering shadow enemy types with simple AI (random walk + chase patterns), enemy-vs-hero collision logic, death/respawn handling, animated enemy sprites.
- *Revisits:* hazard handling (now extended from static to animated dynamic); collision detection (now distinguishes hero vs hazard vs enemy); room state (tracks enemy positions across transitions).
- *Phase-end deliverable:* dynamic 9-room adventure with wandering threats; *Sabre Wulf*-tier at small scale.

**Phase 5 (16 units) — Audio depth.**
- *New:* richer SFX vocabulary (room-transition sounds, enemy-proximity tones, death/victory stings), longer/richer title composition, in-game ambient layer.
- *Revisits:* beeper driver (now multi-track aware on a single channel through tighter interleaving); title screen integrates audio polish.
- *Phase-end deliverable:* small-but-dense, audibly rich adventure. *Sabre Wulf* audio bar at small scale.

**Phase 6 (16 units) — Save state and persistence.**
- *New:* save/load to tape (and from 1989, +3 disk); game-state serialisation; loading state restoration.
- *Revisits:* game state machine (now must persist and restore cleanly); room state, inventory, score, lives — all serialised.
- *Phase-end deliverable:* a game with persistent state; players can resume mid-keep.

**Phase 7 (16 units) — Scale (4×4 keep).**
- *New:* keep expands from 3×3 to 4×4 (16 rooms); two new cell types (e.g., pressure plate + matching door); richer room palette variety.
- *Revisits:* room data format (now 16 rooms in pointer table); connection tables (16 rooms' N/S/E/W); visual identity per room (each new room hand-designed).
- *Phase-end deliverable:* 16-room keep with extended cell vocabulary; mid-tier exploration at small-but-meaningful scale.

**Phase 8 (16 units) — Level design pass.**
- *New:* pacing review (item placement, hazard distribution, key-route gating); dedicated "tutorial room" placement at keep entrance; victory-condition refinement.
- *Revisits:* every room from Phases 2–7 may be visually re-tuned; difficulty curve from forgiving start to peak finish locked in.
- *Phase-end deliverable:* the 16-room keep with intentional level design — the work that turns a working game into a *playable* one.

**Phase 9 (16 units) — Narrative and ending.**
- *New:* discoverable backstory via found items with short lore text; proper ending sequence ("the keep stands" expanded to a narrative beat); item descriptions in ROM font.
- *Revisits:* HUD layout (now must surface item descriptions); end-game state (transitions cleanly to ending sequence).
- *Phase-end deliverable:* a game with a *story*, not just mechanics. The 16-room keep with a meaningful conclusion.

**Phase 10 (16 units) — Attract mode and polish pass.**
- *New:* attract mode after 60s idle (brief gameplay demo); title sequence refinement; transitions between modes polished.
- *Revisits:* title screen (now layered for idle/play states); state machine (mode transitions tested for soft-lock).
- *Phase-end deliverable:* a presentation-polished game from title to end-screen; ready for player handoff.

**Phase 11 (16 units) — 128K AY music.**
- *New:* 128K detection at boot; AY-3-8912 driver (3 channels — pulse, triangle, noise); composed multi-voice title piece; in-game ambient AY layer.
- *Revisits:* audio pipeline branches (48K beeper fallback path preserved and tested in parallel with 128K AY); title screen integrates AY composition.
- *Phase-end deliverable:* a 48K/128K dual-mode game with rich AY music on the larger model and faithful beeper experience on the smaller. Period-faithful — every 1986–87 128K title did this.

**Phase 12 (16 units) — Bank-switched rooms.**
- *New:* bank-switched memory pages on 128K; additional rooms beyond the 4×4 grid (taking total to 25+ rooms); 128K-only visual touches (richer attribute work in certain rooms).
- *Revisits:* room engine (now bank-aware on 128K, falls back to 48K data set when needed); save/load (handles cross-bank state).
- *Phase-end deliverable:* a larger keep on 128K (25+ rooms); 48K mode preserves the 16-room experience. Pre-Knight Lore-scale but real exploration.

**Phase 13 (16 units) — Turbo loader.**
- *New:* custom tape loader (faster than ROM standard) with magazine-quality multicolour loading screen; load progress indicator; period-correct turbo timing.
- *Revisits:* loading screen art (mid-tier full-price magazine-cover quality bar); boot sequence (now branches between turbo and ROM-standard loader for compatibility).
- *Phase-end deliverable:* tape-loaded game with professional loader; presentation-equivalent to 1987 Hewson product.

**Phase 14 (16 units) — +3 disk version.**
- *New:* +3 floppy controller (uPD765) access; disk-based load path; alternate save/load using disk; +3-specific menu options.
- *Revisits:* boot sequence (detects tape/disk source); save/load (now supports both media).
- *Phase-end deliverable:* a +3 disk version of the full game; user-experience on +3 is faster and quieter than tape.

**Phase 15 (16 units) — Multi-model compatibility.**
- *New:* testing pass across 48K, 128K, +2, +2A, +3; minor compatibility fixes; +2A/+3 specific quirks handled (memory contention differences, ROM differences).
- *Revisits:* boot detection logic; bank-switching logic on differing 128K variants.
- *Phase-end deliverable:* a game that runs cleanly on every Spectrum model the period produced. Multi-model is what separated full-price product from budget releases.

**Phase 16 (16 units) — Accessibility + options.**
- *New:* options menu with sound on/off, FLASH-off (photosensitivity), control remap (QAOP/cursor/Kempston), difficulty levels (easy/normal/hard).
- *Revisits:* game state machine (options menu as a new mode); FLASH-rendered cells (now conditional); enemy AI parameters (now difficulty-driven).
- *Phase-end deliverable:* a game with real player accessibility — period-uncommon, but a 2025-curriculum standard worth establishing.

**Phase 17 (16 units) — Final polish and packaging.**
- *New:* end-credits scroll; final balancing pass on all difficulty levels; .tap/.tzx/+3 disk image packaging; Itch.io-ready presentation; on-disk/on-tape README for distribution.
- *Revisits:* every prior phase's deliverable revalidated on real hardware; final QA pass.
- *Phase-end deliverable:* **the full Shadowkeep release.** Could plausibly ship at £7.95 in 1987 alongside Hewson's catalogue. Itch.io-ready as a 2026 retro release.

---

## 12. Ship Test (Multi-axis)

Per-phase pass criteria across the five disciplines. Each phase passes only when *every* axis clears its row at the relevant bar. Definition of Done in `docs/tracker/revamp.md` applies to every unit in addition.

| Phase | Code | Visuals | Audio | Level design | Polish |
|---|---|---|---|---|---|
| 1 | Assembles cleanly; runs on Fuse + Spectrum Next; passes DoD per unit | 2 rooms each visually distinct at mid-tier full-price bar; hero sprite polished | Beeper title theme composed and integrated; door SFX | 2-room loop playable; room transition reliable; first-time player understands goal in <60s | Title screen with theme; press-any-key; clean restart |
| 2 | 9-room engine stable; pointer/connection tables right | Each room visually identifiable from screenshot alone; palette work atmospheric | Full event SFX layer; title still loops | 9-room layout supports memorisable run; hazards/keys/treasure placed for fair play | Lives/score HUD; victory and death states; magazine-quality screenshot achievable |
| 3 | Animation timing stable at IRQ rate; no flicker | Walking cycle reads as character animation, not jitter | Beeper SFX overlay doesn't break title music | Ambient layer doesn't interfere with cue legibility | Animation polish: hero feels alive |
| 4 | Enemy AI deterministic but unpredictable to player | Enemy sprites animated and distinct from hero | Enemy proximity audio cue clear | Enemy placement supports avoidance gameplay; not gotcha | Dynamic feel: rooms have life |
| 5 | Audio pipeline supports 3+ concurrent events | n/a (no visual change) | Richer composition; layered SFX | Audio supports level cues without overwhelming | Audibility test on real hardware |
| 6 | Save/load reliable across reset; tape-cassette write tested | Loading screen for save state (Phase 11+ deeper) | Save/load doesn't interrupt music | Save points appropriate; no save abuse | Save/load discoverable and reliable |
| 7 | 16-room engine performs at 50Hz | New cell types visually distinct from existing | Audio handles 16 rooms' transitions | 4×4 layout has discoverable structure | Larger keep feels intentional, not padded |
| 8 | No regressions from levels 1–7 | Each room re-tuned to atmospheric bar | Audio cues tied to level beats | Pacing: tutorial → mid → late curve verified | Level designer's pass complete |
| 9 | Narrative state persists across save/load | Item descriptions render legibly | Ending sequence music if applicable | Backstory discoverable but not required | Ending feels earned |
| 10 | Mode transitions soft-lock free | Attract mode visually polished | Audio carries across title/attract/play | Attract mode reads as gameplay, not noise | Title→play→end→title→attract cycle smooth |
| 11 | 128K detection reliable; 48K fallback path tested | 128K title screen visually richer | 3-channel AY composition at full bar; beeper version preserved | Audio cues differ appropriately per model | 128K experience demonstrably better; 48K still good |
| 12 | Bank switching reliable; cross-bank save/load works | New rooms at same atmospheric bar | Audio extends to new rooms | 25-room layout has discoverable structure | 128K mode feels expansive |
| 13 | Turbo load reliably across cassette decks | Multicolour loading screen at magazine bar | Loader doesn't interfere with main game audio | n/a (loader is presentation) | Loader is part of the product experience |
| 14 | Disk image valid on +3; file-system access correct | Disk loading screen alternative if desired | Disk variant doesn't introduce audio bugs | Disk save/load UX clearer than tape | +3 experience faster, quieter |
| 15 | All Spectrum models tested on real hardware where available | Visual rendering consistent across models | Audio consistent across AY variants | Gameplay consistent across models | Cross-model parity verified |
| 16 | Options changes don't break game state | FLASH-off option visually consistent | Sound-off works cleanly | Difficulty levels differentiate enemy speed/density meaningfully | Options menu reads as professional |
| 17 | Final QA pass: zero known bugs; passes all unit DoDs | Loading screen, in-game art, end-credits at endpoint bar | Audio polish pass complete | Final balancing pass per difficulty | Itch.io upload ready; .tap/.tzx/+3 image packaged with README |

---

## 13. Pattern Library Extractions

Reusable techniques Shadowkeep surfaces for promotion to the Pattern Library, per [`pattern-library`](../../../../../decisions/pattern-library.md). Each extraction is a candidate; promotion happens when the technique proves reusable across multiple games.

**framework:**

- **Incremental scaffold pattern** — Unit 1 starts from nothing; each unit adds exactly one mechanic. Cross-platform (the pattern applies to any platform's curriculum).
- **Multi-room engine** — room pointer table, N/S/E/W connection tables, current-room state byte, generalised transition. Cross-platform.
- **Game state machine** — title → play → win/die → restart loop. Cross-platform.
- **Options/settings state** — extends the state machine with a configurable mode. Cross-platform (Phase 16 surfacing).
- **Save/load state serialisation** — game-state-to-bytes and back (Phase 6 surfacing). Cross-platform.

**rendering:**

- **Attribute-byte read/write as primary game-state mechanism** — Spectrum-specific in implementation; the design principle (encode all cell state in one byte readable with one instruction) generalises as a cross-platform conceptual pattern.
- **Bitmap sprite over attribute-driven world with cell preservation** — Spectrum-specific (`player_under` technique).
- **HUD layout pattern** — lives/score/inventory/room-name strip in screen top rows. Cross-platform.
- **Multicolour loading screen** (Phase 13 surfacing) — Spectrum-specific period-faithful technique.

**input:**

- **Port `$FE` half-row keyboard scanning** — Spectrum-specific.
- **Control remap pattern** (Phase 16 surfacing) — translates physical input to game commands. Cross-platform.

**physics (loosely):**

- **Cell-grid movement with attribute-based collision** — Spectrum-specific in implementation; the design idea (move on a grid, query the cell beneath) is cross-platform.

**audio:**

- **Single-voice beeper melody driver** — Spectrum-specific (port `$FE` bit 4 toggle, tick-counter timing, byte-pair pattern).
- **Beeper SFX overlay** (Phase 3 surfacing) — single-channel music + SFX interleaving. Cross-platform (the design pattern; implementation per chip).
- **AY-3-8912 driver** (Phase 11 surfacing) — 3-channel music. Spectrum 128K-specific.
- **48K/128K dual-audio architecture** (Phase 11 surfacing) — branching at boot. Spectrum-specific.

**ai:**

- **Simple wandering enemy AI** (Phase 4 surfacing) — random walk + chase. Cross-platform.
- **Enemy state machine** (Phase 4 surfacing) — idle/wander/chase/stunned. Cross-platform.

**assembly (language-specific):**

- **Z80 idioms surfaced repeatedly:** indexed iteration via `LD HL,table` + `LD A,(HL)` + `INC HL`; bit-test via `BIT n,A`; register-pair pointer arithmetic; `DJNZ` loops. These appear in many patterns above.

---

## 14. Vault Tie-ins

Vault entries this curriculum threads through. Per the Definition of Done in `docs/tracker/revamp.md`, every reference must resolve. Entries marked **GAP** need creating before the referencing units ship.

**Direct ancestors:**

- *Atic Atac* (Ultimate, 1983) — referenced in Phases 1–17. **GAP** — vault entry needs verification.
- *Sabre Wulf* (Ultimate, 1984) — referenced in Phases 4, 5, 8. **GAP** — vault entry needs verification.

**Adjacent references:**

- *Manic Miner* (Software Projects, 1983) — beeper-music precedent, referenced in Phases 1, 5, 11.
- *Knight Lore* (Ultimate, 1984) — Spectrum-genre context, referenced in Phase 12 (when scale discussion arises). **GAP** — vault entry referenced in lesson-references; create if absent.
- *Head Over Heels* (Ocean, 1987) — late-period Spectrum achievement reference, Phase 17.

**Studio entries:**

- Ultimate Play the Game — referenced in Phases 1–4 ancestry discussion. **GAP** — confirm existence.
- Hewson Consultants — referenced in Phase 13 (turbo loader era) and Phase 17 (mid-tier full-price reference). **GAP**.
- Mikro-Gen, Gremlin Graphics — referenced indirectly for the £7.95 mid-tier full-price tier (Phase 17). **GAP**.

**Hardware reference pages:**

- ZX Spectrum attribute system reference — referenced in Phases 1, 2, 7. **GAP** — verify.
- ZX Spectrum beeper / port `$FE` reference — referenced in Phases 1, 3, 5. **GAP** — verify.
- AY-3-8912 reference — referenced in Phase 11. **GAP**.
- ZX Spectrum 128K bank switching — referenced in Phases 11, 12. **GAP**.
- uPD765 floppy disk controller (+3) — referenced in Phase 14. **GAP**.

**People entries (low priority, but useful):**

- Tim and Chris Stamper (Ultimate founders) — referenced indirectly via Atic Atac/Sabre Wulf/Knight Lore.
- Tim Follin / Matthew Smith / Rob Hubbard (era audio reference) — referenced via Phase 5 audio discussion.

**Pattern-library cross-references:** every pattern listed in Section 13 will eventually cross-link back here from its pattern entry.

---

## Risks (Optional)

1. **The multi-room engine spike (Phases 2 → 3 → 4).** Generalising the room engine from 2 rooms (Phase 1) to 9 rooms (Phase 2) to 9-rooms-with-active-enemies (Phase 4) is the design's largest technical jump. The existing 16-unit Arc 1 spine in `shadowkeep-phase-1-design.md` already flagged units 9–10 as the prototype-first spike. Mitigation: prototype the engine ahead of Phase 2 authoring; treat Phase 3 enemy-aware variant as a separate spike.

2. **Beeper title composition (Phase 1).** Beeper music is unforgiving — one voice, no harmony, all timing and melody. The October launch hinges on the title theme landing. Mitigation: `shadowkeep-beeper-spec.md` scaffolds the composition; if Steve's composition stalls, fall back to a paid composer per the Cadence approach in `revamp.md`.

3. **Hero sprite on attribute-driven world cell preservation (Phase 1).** The hero must preserve the attribute beneath when moving, and restore it on departure. Edge cases at room transitions (the destination cell's attribute must be respected). The existing `player_under` technique handles this but needs careful audit during Phase 1 review.

4. **Authoring rate against October deadline.** Eight multi-disciplinary units before October at the new bar requires roughly 160–240 hours of focused authoring (per the math in `curriculum-structure.md`). Combined with the other three Spectrum launch artefacts (BASIC track, landing page, vault), runway is tight. Mitigation: cut hierarchy from `october-2026-vertical-slice.md` allows trimming to 4 units if needed; BASIC track has separate cut hierarchy.

5. **128K/+3 testing on real hardware (Phases 11–15).** Phases 11–15 introduce hardware dependencies that need real-iron testing. Mitigation: defer hardware acquisition decisions to Arc 5 timing; these are post-October phases, so no October-critical risk.

6. **Acceleration assumption (curriculum-wide, surfaces here in scope).** The 256-unit total assumes acceleration as patterns and infrastructure mature. If Shadowkeep Phase 1 takes substantially longer than projected, the post-October trajectory may compress (per `curriculum-structure.md`). Mitigation: track per-phase authoring time against projection; surface acceleration shortfall promptly.

---

## Changelog

- **v1.0 (2026-05-13):** Initial brief. First brief authored against `docs/specifications/brief.md` v1.0. Replaces the ad-hoc design content previously distributed across `knowledge/curriculum/shadowkeep-phase-1-design.md` (which remains as the operational design doc) and various log entries. Anchors 256-unit total scope, 17-phase trajectory, period-faithful constraint position, mid-tier full-price endpoint bar, October vertical-slice deliverable.
