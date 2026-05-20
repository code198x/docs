# Shadowkeep — 32-Unit Engineering Plan

> *The 32-unit plan ([shadowkeep-32-unit-plan.md](shadowkeep-32-unit-plan.md)) is the **spec** — what each unit produces. This document is the **execution plan** — how we actually get there without embarrassing ourselves at CRASH! Live.*

**Anchored to:** [shadowkeep-32-unit-commitment.md](../decisions/shadowkeep-32-unit-commitment.md). **Date:** 2026-05-18. **Target launch:** October 2026.

---

## Executive summary

- 32 units in two arcs across ~21 weeks (May 18 → mid-October).
- Three engine commitments: pixel sprites, Y-sort layered render, decoupled tile-collision.
- Four work streams in parallel: **engine**, **pixel art**, **music/audio**, **MDX**.
- Plus a separate fifth stream: **BASIC track** (5 games still to build, ~50 BASIC units).
- Critical path: hero sprite (Unit 5) → walk cycle (Unit 6) → object system (Unit 9) → composed music (Unit 15) → title art (Unit 16). Everything else flexes around these.
- **Pre-flight phase (weeks 1-4): infrastructure-first.** No new units publish until engine, asset pipeline, and music workflow are committed and tested. Existing 8 units stay live during this phase.
- **Critical decisions outstanding** (see section 11): pixel-art tool, hero sprite dimensions, music composition approach, real-hardware test access.

---

## 1. The standard the work has to meet

"Don't embarrass ourselves at CRASH! Live" is the bar. Concretely, a visitor at the event scans the QR code, lands at `/crash-live/`, and within 60 seconds:

1. Recognises Shadowkeep as a *real game*, not a *programming demo*. Hero looks like a character. Walls look designed. Music is composed.
2. Plays Unit 1 (or the latest unit) and sees code that reads as crafted, not template-generated. The MDX prose has voice.
3. If they're a CRASH-era person: they recognise the visual and editorial reference points. The work earns its place in their nostalgia.
4. If they're a beginner: they can follow Unit 1 and see how it leads to the title screen they just saw.
5. If they're a journalist or scene historian: they can read the vault and find the work serious.

Anything less is embarrassment. We plan accordingly.

---

## 2. Critical path

The longest dependency chain — what blocks what — is roughly:

```
[Pre-flight: tool decisions, engine infra, asset pipeline]
    ↓ (weeks 1-4)
[Hero sprite art] ─── [Walk-cycle art] ─── [Walk cycle integrated]
    ↓                       ↓                       ↓
Unit 5                  Unit 6                  Unit 7-8 (pixel + mask)
    ↓
[Pre-shifted sprite tooling working]
    ↓
[Y-sort engine] ── [Decoration sprites] ── Unit 9-10
    ↓
[Tile collision engine] ── Unit 13
    ↓
[Composed music] ── [Title art] ── Unit 15-16
    ↓
[Arc 1 ship gate]
    ↓
Arc 2 begins (units 17-32)
```

If any link in this chain slips, the next ones slip behind it. The plan's job is keeping non-critical work *ahead* of where critical-path work catches up.

**Total critical-path length, optimistic:** 14 weeks.
**Critical path with realistic per-step slack:** 17-18 weeks.
**Available calendar:** ~21 weeks.

Slack: 3-4 weeks. That's enough if we don't waste it; not enough if we discover critical assumptions are wrong late.

---

## 3. Work streams (parallel tracks)

### Stream A — Engine code

| Phase | Deliverable | Weeks |
|---|---|---|
| A1 | Tile rendering primitives (8×8 cell draw, attribute decoupled) | 1-2 |
| A2 | Sprite shifter (pre-shifted tables, masked draw primitive) | 2-3 |
| A3 | Y-sort object list (insertion sort, dispatch, draw loop) | 4-5 |
| A4 | Tile-map collision (decoupled query) | 6-7 |
| A5 | Music driver hardening (existing Unit 7 driver, plus SFX overlay) | 8-9 |
| A6 | NPC behaviour (patrol state machine) | 12-13 |
| A7 | HUD render (top-of-screen reserved zone, glyph rendering) | 14-15 |
| A8 | Title/state-machine refinement (TITLE/PLAY/VICTORY/GAMEOVER) | 16-17 |
| A9 | Real-hardware test pipeline (Spectrum Next deployment) | 18 |

Mostly sequential — later phases depend on earlier. ~18 weeks total but most overlaps with other streams.

### Stream B — Pixel art

| Phase | Deliverable | Weeks (target) |
|---|---|---|
| B1 | Stone tile set (5+ variations) | 2 |
| B2 | Hero sprite, single frame | 3-4 |
| B3 | Hero walk cycle (4 frames) + idle | 4-5 |
| B4 | Hero pre-shifted export tooling | 5 |
| B5 | Hero mask data export | 5 |
| B6 | Decorations: pillars, altar, sconces | 7-8 |
| B7 | Floor tile variations | 8 |
| B8 | Lighting attribute palette | 9 |
| B9 | Antechamber composition | 9-10 |
| B10 | Gold sprite + sparkle frames | 11 |
| B11 | Title screen artwork + logo type | 12-13 |
| B12 | Door animation frames | 14 |
| B13 | Hero idle animation refinement | 14 |
| B14 | NPC sprite (the presence) | 16 |
| B15 | Death/respawn animation | 17 |
| B16 | Third room composition | 19-20 |

Substantially parallel to engine. The art deliverables block their corresponding units; otherwise free to start as soon as the tool pipeline is established (B1 by end of week 2).

### Stream C — Music and audio

| Phase | Deliverable | Weeks (target) |
|---|---|---|
| C1 | Music composition tooling decision (Beepola? hand-compose?) | 1-2 |
| C2 | Title theme composition (statement / variation / bridge / return) | 3-6 |
| C3 | SFX library design (footstep, door, pickup, death, victory) | 7-8 |
| C4 | Footstep SFX | 11 |
| C5 | Door creak SFX + animation timing | 12 |
| C6 | Pickup chime | 11 |
| C7 | Death sound | 16 |
| C8 | Victory chord composed (3-5 notes + held tonic) | 13 |
| C9 | Music polish pass (Arc 2) | 20 |

The title theme composition (C2) is the highest-risk audio task. It's a 30-60-second piece of beeper music in D minor with proper structure — composing real beeper music is hard. C2 can start *immediately*, before any engine work, because the driver from existing Unit 7 already works.

### Stream D — MDX prose

| Phase | Deliverable | Weeks (target) |
|---|---|---|
| D1 | Unit 1-4 MDX (drafts can pre-date code; finalised when code lands) | 4-7 |
| D2 | Unit 5-8 MDX | 8-10 |
| D3 | Unit 9-12 MDX | 11-13 |
| D4 | Unit 13-16 MDX | 14-16 |
| D5 | Unit 17-20 MDX | 17-18 |
| D6 | Unit 21-24 MDX | 18-19 |
| D7 | Unit 25-28 MDX | 19-20 |
| D8 | Unit 29-32 MDX | 20-21 |

Each MDX needs the code and the screenshots and audio captures, so it can't fully complete before the unit's code/art is done. But ~50% of each MDX (intro prose, conceptual sections, "try this" exercises, troubleshooting) can be drafted in advance.

### Stream E — BASIC track (separate)

| Phase | Deliverable | Weeks |
|---|---|---|
| E1 | Game 9 (Brick Bash) — 8-10 units | 6-7 |
| E2 | Game 11 (Tarmac) — 8-10 units | 9-10 |
| E3 | Game 12 (Ink Spill) — 8-10 units | 12-13 |
| E4 | Game 13 (Rooftops) — 8-10 units | 15-16 |
| E5 | Game 16 (Thornwood Manor) — 10-12 units | 18-19 |

BASIC games are smaller than Shadowkeep units — each game ~1.5-2 weeks, sequential. Slots into weeks where Shadowkeep is on a lighter task. **Cannot slip into Shadowkeep's budget.** Per the decision record, if BASIC overruns it's BASIC that flexes.

---

## 4. Phase-by-phase, week-by-week

Five-month plan. Each phase has an explicit deliverable; deliverables gate the next phase.

### Phase 0 — Pre-flight (Weeks 1-4: May 18 → June 14)

**Goal:** decide tool choices, build engine infrastructure, validate end-to-end pipeline. **No new units publish.**

**Week 1 (May 18-24):**
- D1: Pre-flight decisions (§11) ratified ✓ (2026-05-18)
- A1: Tile rendering primitives — write and test
- C1: Music tool decision; first composition sketch
- B0: Pixel-art tool installed; first stone tile drawn as proof-of-pipeline
- A2-pilot: ✓ End-to-end sprite pipeline proven on test pattern (2026-05-18)
  - `tools/convert_sprite.py` written and tested
  - 16×16 test pattern PNG → 8 pre-shifted .inc bytes → SNA → Emu198x screenshot
  - All 8 shifts render correctly with masked draw; no overlap, no garbage
  - Test program: `code-samples/sinclair-zx-spectrum/test/sprite-shifter-validation/`
- A1-pilot: ✓ Tile-rendering primitive proven (2026-05-18)
  - 22×16 tile-map renderer; 4 distinct 8×8 tile patterns
  - row × 22 + col indexing, char-cell → screen address, 8-byte blit with inc-h scanline stepping
  - Test program: `code-samples/sinclair-zx-spectrum/test/tile-renderer-validation/`
  - Visual verification: wall border, top-left and bottom-right inset blocks, mid-room deco square — all land at expected cells
- C1-pilot: ◐ Beeper music pipeline structurally complete; audio verification deferred (2026-05-18)
  - Text score format defined (note name + octave + duration denominator; tempo / octave directives)
  - `tools/compile_music.py` written — text → .inc with (period, cycles) pairs
  - Custom Z80 beeper (no ROM dependency); 16-bit period inner loop, T-state math documented in source
  - Test program: `code-samples/sinclair-zx-spectrum/test/beeper-validation/`
  - **Blocked:** Audio capture in Emu198x didn't work in this session. Initial diagnosis ("ROM IM 1 handler clobbers port $FE 50×/sec") was wrong — the IM 1 handler at $0038 doesn't write to port $FE. The real issue was an [Emu198x session-stuck bug](memory: emu198x-session-stuck) where load_snapshot calls stopped taking effect after a sequence of video-recording + audio-capture operations. Audio verification will rerun on Spectrum Next or a freshly-started Emu198x session.

**Week 2 (May 25-31):**
- A1: Tile rendering primitives complete and tested
- A2: Sprite shifter — design and start build
- B1: Stone tile set (5 variations) completed
- C2: Title theme composition — sketch phase
- E1: Game 9 (Brick Bash) — start

**Week 3 (June 1-7):**
- A2: Sprite shifter complete and tested (round-trip: art → pre-shifted bytes → emulator)
- B2: Hero sprite, single frame — multiple iterations
- C2: Title theme composition — refinement
- E1: Game 9 mid-build

**Week 4 (June 8-14):**
- A3: Y-sort object list — start build
- B3: Hero walk cycle — start
- B4, B5: Hero pre-shifted + mask tooling validated on first frame
- C2: Title theme — alpha version playable
- E1: Game 9 complete (8-10 BASIC units)
- D1: Unit 1-4 MDX drafts begin

**Phase 0 ship gate (end of Week 4):**
- ✓ Tile rendering works
- ✓ Pre-shifted sprite tooling works end-to-end (art file → bytes → emulator)
- ✓ Mask drawing primitive works
- ✓ Hero single-frame sprite exists and reads as designed
- ✓ Title theme composition is committed (even if not final)
- ✓ Game 9 (Brick Bash) published

**If Phase 0 ship gate fails, the plan slips and we must replan.** This is the most important gate of the project. The decisions made and infrastructure built here determine everything that follows.

### Phase 1 — Arc 1.1 + 1.2 (Weeks 5-8: June 15 → July 12)

**Goal:** publish units 1-8. First half of Arc 1. The keep takes shape; the thief is born.

**Week 5 (June 15-21):**
- A3: Y-sort object list complete
- B3: Hero walk cycle complete (4 frames + idle)
- D1: Unit 1, 2 MDX final + screenshots
- **Publish Unit 1 (replacing existing)**

**Week 6 (June 22-28):**
- **Publish Unit 2, Unit 3**
- A4: Tile-map collision — start
- E2: Game 11 (Tarmac) — start
- B6: Decorations (pillars) start

**Week 7 (June 29 → July 5):**
- **Publish Unit 4 (the first new unit beyond existing range)**
- A4: Tile-map collision complete (will be used in Unit 13)
- B6: Decorations (pillars + altar) complete
- D2: Unit 5-8 MDX drafts begin

**Week 8 (July 6-12):**
- **Publish Unit 5, Unit 6**
- B7: Floor variations
- C3: SFX library design committed
- E2: Game 11 mid-build

**Phase 1 ship gate (end of Week 8):**
- ✓ Units 1-6 live, replacing existing equivalents
- ✓ Hero animates with walk cycle on screen
- ✓ Existing Unit 7-8 still live, marked as "to be revised"

### Phase 2 — Arc 1.3 + 1.4 (Weeks 9-12: July 13 → August 9)

**Goal:** publish units 7-16. Arc 1 complete.

**Week 9 (July 13-19):**
- **Publish Unit 7 (pixel-level positioning)**
- **Publish Unit 8 (masked sprite)** — hero now leaves no trail
- B8: Lighting attribute palette decisions made
- B9: Antechamber composition started
- C2: Title theme — beta version (compositional structure complete)

**Week 10 (July 20-26):**
- **Publish Unit 9 (Y-sort layered render)** — hero walks behind pillars
- **Publish Unit 10 (architecture — pillars, altar, sconces)**
- B9: Antechamber composition complete
- B10: Gold sprite + sparkle frames
- E3: Game 12 (Ink Spill) — start

**Week 11 (July 27 → August 2):**
- **Publish Unit 11 (lighting)** — atmosphere appears
- **Publish Unit 12 (antechamber + transition)**
- B11: Title screen artwork begins
- C8: Victory chord composed

**Week 12 (August 3-9):**
- **Publish Unit 13 (tile collision)**
- **Publish Unit 14 (gold pickup + sparkle + SFX)**
- B11: Title screen art complete (or near complete)
- E3: Game 12 mid-build

**Phase 2 mid-gate (end of Week 12):**
- ✓ Engine fundamentals all live (sprite, mask, Y-sort, collision)
- ✓ Two rooms designed
- ✓ Lighting visible
- ✓ Gold pickup with feedback works
- ✓ Half of Arc 1 still to ship (Units 15-16)

### Phase 3 — Arc 1.4 finish + Arc 2.1 (Weeks 13-16: August 10 → September 6)

**Goal:** publish units 15-20. Arc 1 ships. Arc 2 begins.

**Week 13 (August 10-16):**
- **Publish Unit 15 (composed title theme)** — major audio milestone
- **Publish Unit 16 (title screen with artwork)** — major visual milestone
- **🎉 Arc 1 ship gate**

**Week 14 (August 17-23):**
- **Publish Unit 17 (footstep SFX)**
- **Publish Unit 18 (animated doors)**
- B12: Door animation frames complete
- E4: Game 13 (Rooftops) — start

**Week 15 (August 24-30):**
- **Publish Unit 19 (hero idle animation)**
- **Publish Unit 20 (floor variations + attribute mood)**
- B13: Hero idle animation refinements
- B14: NPC sprite begins
- C7: Death sound composed

**Week 16 (August 31 → September 6):**
- **Publish Unit 21 (first NPC, patrol)** — the keep is not empty
- **Publish Unit 22 (NPC collision, BORDER red flash)**
- B14: NPC sprite final
- E4: Game 13 mid-build

**Phase 3 ship gate (end of Week 16):**
- ✓ Arc 1 complete (Units 1-16, all at the bar)
- ✓ Arc 2 sub-arc 2.1 complete (sound and motion)
- ✓ First NPC alive in the keep

### Phase 4 — Arc 2.2 + 2.3 (Weeks 17-20: September 7 → October 4)

**Goal:** publish units 23-28. Lives, HUD, third room.

**Week 17 (September 7-13):**
- **Publish Unit 23 (lives, deaths, respawn)**
- **Publish Unit 24 (second NPC / behavior variation)**
- B15: Death/respawn animation
- E5: Game 16 (Thornwood Manor) — start
- A7: HUD render system begins

**Week 18 (September 14-20):**
- **Publish Unit 25 (HUD bar — score, gold, lives)**
- **Publish Unit 26 (room names on transition)**
- A8: State machine refinement
- E4: Game 13 complete

**Week 19 (September 21-27):**
- **Publish Unit 27 (best-score persistence)**
- **Publish Unit 28 (third room)** — the keep grows
- B16: Third room composition complete
- E5: Game 16 mid-build

**Week 20 (September 28 → October 4):**
- **Publish Unit 29 (atmosphere unified — polish pass)**
- **Publish Unit 30 (audio depth — SFX library expansion + music polish)**
- E5: Game 16 complete
- C9: Music polish pass

**Phase 4 ship gate (end of Week 20):**
- ✓ Arc 2 sub-arcs 2.1, 2.2, 2.3, half of 2.4 all live
- ✓ Three rooms with depth, atmosphere, NPCs, lives, HUD, score
- ✓ BASIC track complete (16 games)

### Phase 5 — Final pass and launch (Week 21: October 5-12, launch ~Oct 10-15)

**Week 21 (October 5-11):**
- **Publish Unit 31 (real hardware testing — Spectrum Next)**
- **Publish Unit 32 (final title presentation + completion state)**
- Real-hardware playtest log
- Final landing-page review
- Vault touch-ups
- Press kit / launch announcement preparation

**🎉 LAUNCH WEEK** — CRASH! Live event window

---

## 5. Engine infrastructure specification

Concrete sub-systems and their dependencies.

### 5.1 Tile rendering (A1)

**Inputs:** room_data[] byte array (22×16 = 352 bytes per room), tile_id → sprite_data lookup table.

**Outputs:** bitmap area $4000-$57FF drawn from room_data. **Attribute area $5800-$5AFF written separately** — by the lighting pass (5.4), not by tile rendering.

**Primitives:**
- `draw_tile(tile_id, screen_row, screen_col)` — copy 8 bytes from tile data to the cell's bitmap
- `draw_room(room_id)` — iterate room_data, dispatch to draw_tile per cell
- Tile-data layout: contiguous 8-byte sprites, indexed by tile_id. Tile_id 0 = empty (skip); 1-15 reserved for wall variations; 16-31 reserved for floor; 32+ for decorations and special.

**Memory:** ~256 bytes of tile sprite data; minimal code.

### 5.2 Pre-shifted sprite tables (A2)

**Inputs:** source sprite data (image bytes, mask bytes), width and height.

**Outputs:** 8 versions of each sprite, one per X-offset 0-7. Generated at *assembly time* (via macro or external tool).

**Decision:** **External tool** (Python or Ruby script) that reads art files and emits `.inc` files of `defb` data. Macro approach in pasmonext is possible but harder to debug. External tool keeps the assembler input clean.

**Pipeline:** Aseprite (or chosen art tool) → export PNG → `shift_sprite.py` reads PNG → emits `hero_shift_0.inc` through `hero_shift_7.inc`. Each `.inc` is a `defb` block. Included in main `.asm` via `include`.

**Storage cost per sprite:** 8 shifts × 8 bytes × frames × 2 (image + mask). Hero with 5 frames = 5 × 8 × 8 × 2 = 640 bytes. Affordable.

**Primitives:**
- `draw_sprite_at_pixel(sprite_id, frame_id, pixel_row, pixel_col)` — computes `shift_index = pixel_col & 7`, looks up the right pre-shifted table, copies bytes to bitmap with mask
- `erase_sprite_at_pixel(...)` — used for sprite-saved-background approach

### 5.3 Y-sort object list (A3)

**Inputs:** object array (16-slot max), each with `{ x_pixel, y_pixel, sprite_id, frame_id, type, state }`.

**Outputs:** objects drawn each frame in Y order (smaller Y first, larger Y last; hero among them by Y position).

**Algorithm:** insertion sort, in-place, each frame. 16 objects max → 256 comparisons worst-case → trivial cost (<1000 T-states).

**Memory:** object array ~128 bytes (16 slots × 8 bytes). Sort index ~16 bytes. Object-type dispatch table.

**Primitives:**
- `object_add(type, x, y)` — find empty slot, fill
- `object_remove(slot_index)` — mark slot as empty
- `update_objects()` — per-frame: tick animation frame, update positions for NPCs
- `draw_objects()` — sort by y_pixel, dispatch to type-specific draw routine for each

### 5.4 Tile-map collision (A4)

**Inputs:** room_data[] (the same table used for rendering — but read with different semantics).

**Outputs:** boolean — can the hero move to (target_x, target_y)?

**Implementation:** the room_data byte for the destination cell is checked against the cell type table. WALL/PILLAR/ALTAR = blocked; FLOOR/GOLD/DOOR/EXIT = passable. **No attribute-area read** — collision is independent of cosmetics.

**Cell-type semantics table:**

| Tile ID range | Visual | Collision |
|---|---|---|
| 0 | empty | passable |
| 1-15 | wall variations | blocked |
| 16-31 | floor variations | passable |
| 32-47 | decoration | blocked (mostly) |
| 48-55 | special: gold | passable, triggers pickup |
| 56-63 | special: door | passable, triggers transition |
| 64-71 | special: exit | passable, triggers victory check |

**Primitives:**
- `can_move_to_pixel(target_x, target_y)` — convert pixel to tile coords, look up tile_id, check is_passable[tile_id]

### 5.5 Lighting (A5 — for Unit 11)

**Inputs:** room_data[] + list of light sources per room (e.g., torch/sconce positions).

**Outputs:** attribute area $5800-$5AFF — each byte set based on distance to nearest light.

**Run schedule:** once per room load. Not per frame.

**Algorithm:** flood-fill or simple Manhattan-distance check from each light source. For each cell, set attribute based on light-level.

**Light-level palette:**

| Distance from light | Attribute (PAPER/INK) |
|---|---|
| 0 (the light cell itself) | $46 — BRIGHT 1, PAPER 0, INK 6 (yellow glow) |
| 1-2 cells | $46 — same brightness |
| 3-4 cells | $06 — INK 6 normal, PAPER 0 |
| 5+ cells | $07 — INK 7 white on PAPER 0 (cold/distant) |

(Final palette is a design decision in B8; this is a starting point.)

### 5.6 Music driver + SFX overlay (A6)

The existing Unit 7 beeper driver works (with the audio quality concerns flagged). For Arc 1 and 2 we need:

- Driver continues to play title theme between user actions
- SFX (footstep, pickup, door, death, victory) can play *over* music — they briefly interrupt the music note for the SFX duration, then resume
- Or: music pauses during SFX, resumes after

**Design decision (engineering plan deferred):** simplest acceptable behavior is "SFX briefly silences music for SFX duration." Music sounds slightly choppy but SFX is clear. Better-but-harder: interleave SFX with music at sample rate.

### 5.7 HUD render (A7 — for Unit 25)

**Inputs:** score, gold count, lives count.

**Outputs:** top 2 rows of screen (cells row 0-1, all 32 cols) rendered with HUD content. Reserved zone — game-area renderer must respect.

**Layout:**

```
SCORE  00247    GOLD  03/15    LIVES  ▆▆▆
```

Or similar — designed glyph for digits, icons for gold and lives.

**Memory:** HUD glyph data ~80 bytes; HUD render code ~150 bytes.

### 5.8 State machine (A8 — for Unit 32)

States: TITLE, PLAY, PAUSE (if implemented), VICTORY, GAME_OVER, COMPLETED (after Unit 32 final state).

Transitions per state machine diagram. Implementation: a single byte `game_state` plus a per-frame dispatch table.

---

## 6. Asset pipeline

### Pixel art — Piskel + Python conversion

**Tool:** Piskel (browser-based, free).

**Source files:** `code-samples/sinclair-zx-spectrum/assets/sprites/` — per-sprite folders containing the `.piskel` source file plus exported PNGs (single frames and animation sheets).

**Conversion pipeline:**

```
.piskel (edit) → PNG export → python convert_sprite.py → .inc (defb data)
```

**`convert_sprite.py`** — to be written in Phase 0:
- Reads PNG (RGBA or paletted)
- Maps colours to Spectrum palette indices
- Determines bit value per pixel (threshold or designated colour)
- Computes mask data (alpha or specified transparent colour)
- For pre-shifted sprites: generates 8 shifted versions, output as separate `.inc` blocks
- Emits assembly-ready `defb` blocks with comments documenting source frame, shift offset, etc.

**Build step:** `make assets` runs `convert_sprite.py` on changed source PNGs. Generated `.inc` files committed to git (for reproducibility and easy review of byte changes).

**Versioning:** `.piskel` source files + PNG exports + `.inc` outputs all in git. Lockstep — never commit `.inc` without the source it came from.

### Music composition

**Tool:** hand-compose in MIDI (DAW of choice) or directly in byte arrays.

**Source files:** `code-samples/sinclair-zx-spectrum/assets/music/`
- `title-theme.mid` (or DAW format) — the editable composition
- `title-theme.notes` — text file documenting the byte-pair translation
- `title-theme.inc` — generated `defb` block for inclusion

**Build step:** primarily manual translation from MIDI to byte pairs, per the [beeper spec](shadowkeep-beeper-spec.md). A small Python helper (`midi_to_beeper.py`) may help with the pitch-table mapping. Generated `.inc` checked into git.

### Audio capture

For MDX inline players. Emu198x audio capture → WAV → `website/public/audio/.../*.wav`. Already working.

### Screenshot capture

Emu198x screenshot → PNG → `website/public/images/.../*.png`. Each unit captures per-stage snapshots. Already working.

### Real-hardware test pipeline (Spectrum Next confirmed on-hand)

```
SNA build → SD card / USB → Spectrum Next NextSync → Load → Play test
```

**Test cadence:** weekly during Phases 1-5. Document divergences in `docs/tracker/hardware-test-log.md`.

**Test checklist per unit:** does it load? does it run? does it play? does audio sound right? does the visual look right? Compare to Emu198x screenshots.

---

## 7. Risk register

| # | Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| 1 | Pixel art quality below bar — hero looks bad, walls look bad | **High** | **Critical** | Iterate hero sprite multiple times in week 3-4 before committing. Reference 1987 Hewson directly. Consider hiring pixel artist for hero + title art (most-load-bearing). |
| 2 | Title theme composition doesn't land — sounds amateur | **Medium** | **High** | Start composition C2 immediately, week 1. Multiple iterations. Reference Manic Miner / Sabre Wulf / Stormlord directly. Consider hiring composer if self-compose fails. |
| 3 | Engine complexity introduces bugs — sprite shifter wrong, Y-sort wrong | Medium | High | Build engine first (Phase 0), test thoroughly with isolated test programs, only proceed to unit writing after each subsystem passes. |
| 4 | Schedule slip from per-unit overruns | Medium | High | Track per-unit estimates weekly. If a unit blows budget, raise its bar within the budget (don't extend the budget). If repeated overruns, declare drift and replan. |
| 5 | BASIC track slips into Shadowkeep budget | Medium | Medium | Strict separation — BASIC work happens in dedicated weeks (E1-E5 in the schedule). If BASIC overruns, BASIC count cuts, not Shadowkeep time. |
| 6 | Real-hardware testing surfaces issues late | Medium | High | Test on Spectrum Next during Phase 1, not just Phase 5. Catch divergences from emulator early. |
| 7 | Memory pressure — 48 KB fills up | Low | Medium | Memory budget audit in Phase 0 (task #103). If tight, drop pre-shifted sprites for less-used objects (runtime-shift those). |
| 8 | MDX writing becomes time-sink | Low | Medium | Pre-draft prose where possible (concept/intro sections can pre-date code). Use templated structure. |
| 9 | Asset pipeline doesn't work — Aseprite export → assembly bytes wrong | Medium | High | Validate pipeline end-to-end in Week 1 with a trivial sprite. If broken, decide tool change immediately, not week 5. |
| 10 | Tooling/setup change breaks build (pasmonext update, Docker change) | Low | High | Pin all tool versions in Docker images. Lock now. Don't update during the launch window. |
| 11 | I (the developer) burn out or get sick for >1 week | Low | Critical | Plan has 3-4 weeks slack. One week loss is recoverable. Longer than that = scope reduction (cut hierarchy in commitment doc applies). |
| 12 | CRASH! Live event date moves | Low | Low | If event moves earlier: scope cut hierarchy applies. If later: more time, raise bar within units. |

---

## 8. Quality gates

Each unit must pass the **9-item Definition of Done** before being declared shipped:

1. Code compiles on pasmonext; SNA generated; no warnings.
2. SNA runs cleanly on Emu198x. Visual + audio verified.
3. MDX prose written at magazine-class bar (CRASH/YS register). Drafted, reviewed, polished.
4. Screenshots captured for each stage; saved to `website/public/images/.../`.
5. Audio captures (where relevant) saved to `website/public/audio/.../`.
6. CodeFromFile component references active and resolving.
7. "Try this" sections (≥2) included.
8. "If it doesn't work" troubleshooting section included.
9. Vault references resolve (every `/vault/...` link points to an existing reviewed entry).

Plus three new gates for the 32-unit plan:

10. **Art deliverable matches the unit's bar.** Hand-pixelled sprite, designed tile, composed music — whatever the unit's art deliverable is, the artist (you / I / contributor) signs off on it being at the 1987 Hewson bar.
11. **Real-hardware compatible.** SNA tested on Spectrum Next at least once during the unit's development. (Final unified test in Unit 31.)
12. **No regression on prior units.** Each new unit is reviewed against the previous one. The new engine work doesn't break anything that worked before.

---

## 9. Status discipline

**Weekly check-in.** Every Friday: review the past week's targets, log progress in `docs/tracker/revamp.md`, identify next week's targets.

**Per-unit log.** When a unit is published, append to `docs/tracker/revamp.md`:

```markdown
- 2026-08-15 — Unit 9 published. Y-sort engine live. Pillar sprite shipped. ~3 days actual vs 3 days budgeted.
```

**Drift alarms.** If any of these fire, *stop and assess* before continuing:

- A unit overruns budget by >50%
- A phase ship gate fails
- A risk in §7 materialises
- The week-by-week schedule slips >1 week

When drift fires: re-read this engineering plan; assess what to cut, replan, or accept; document the decision.

---

## 10. What we do NOT do (explicit non-goals)

These are not in scope. If discussion drifts toward them, name as non-goal and defer.

- **A third-person isometric view.** Knight Lore's isometric is a separate engine commitment we're not making.
- **Save-to-tape / save-to-disk persistence.** Score is in-memory only.
- **Multi-load / multi-tape distribution.** Single SNA / single TAP.
- **Inventory system.** Hero carries no items beyond the gold count.
- **Character classes.** One hero, one playstyle.
- **Multiple maps / level select.** One keep, three rooms, one playthrough loop.
- **Multiplayer.** Single-player only.
- **A boss fight.** Inhabitants are atmospheric, not encounter-driven.
- **Procedural anything.** All content hand-authored.
- **A custom Z80 IDE / debugger / build pipeline beyond what we have.** Use pasmonext + Docker + Make.

---

## 11. Pre-flight decisions — resolved 2026-05-18

### 11.1 Pixel-art tool — **Piskel** (free, web-based)

Browser-based pixel-art editor. Animation timeline, layer support, PNG export (single frame and sprite sheet), GIF preview.

**Pipeline implications:** the conversion tool reads PNG exports (single-frame or sprite-sheet). PNG → assembly bytes via Python script with Pillow/PIL. Each pixel's brightness threshold determines bit value; mask is computed from alpha or a designated "transparent" colour. The script outputs `.inc` files with `defb` blocks.

**Source-of-truth files:** Piskel `.piskel` files (proprietary JSON-ish), kept in `assets/sprites/` alongside the PNG exports. PNG exports are the canonical input to the conversion tool — `.piskel` is for re-editing.

**Storage:** Piskel offers cloud-save, but we keep canonical sources in git (the `.piskel` file is text-based and diff-friendly).

### 11.2 Hero sprite — **16×16, 2×2 cells** (Atic Atac scale)

The hooded thief is a 2-cell-wide, 2-cell-tall sprite. 32 bytes of pixel data per frame (16 rows × 2 bytes = 32; double that for mask = 64 bytes per frame). With 4 walk frames + 1 idle = 5 frames × 64 = 320 bytes raw. Pre-shifted (8 versions per frame for X-offset) = 320 × 8 = 2560 bytes for the full hero set.

**Collision box:** 16×16. Sub-cell positioning lets the hero stand on the *visual* boundary of a cell without colliding — collision check is against the *logical* tile boundaries.

**Implication for room design:** the hero must fit through 16-pixel-wide gaps. Wall designs and door positions accommodate this. Designed-cell width of 1 tile (8 pixels) is too narrow for a passage; passages must be ≥2 tiles wide.

### 11.3 Music composition — **self-compose, reference-driven**

Compose by hand in MIDI (DAW of choice — Logic, Ableton, GarageBand, whatever) or by direct hex-byte composition. Use reference tracks for calibration:

- Manic Miner title (Matthew Smith, 1983)
- Jet Set Willy title (Smith, 1984)
- Sabre Wulf title (Ultimate, 1984)
- Stormlord title (Tim Follin, 1989) — aspirational reference
- The Hobbit opening tones (Melbourne House, 1982)

**Workflow:** sketch in MIDI piano roll, get the tune right, translate to byte arrays (pitch + duration pairs) per the [beeper composition spec](shadowkeep-beeper-spec.md). Verify in Emu198x. Iterate until satisfied. Substantial work; start Week 1, target Week 6 alpha, Week 13 final.

**Fallback plan:** if by Week 8 the composition isn't landing, escalate to hiring (§11.5).

### 11.4 Real hardware — **Spectrum Next on-hand**

Testing pipeline:

1. Build SNA + TAP via Docker pasmonext
2. Transfer SNA to SD card or USB stick
3. Load on Spectrum Next via NextSync or copy to NEXT browser
4. Test interactively
5. Document any divergences from Emu198x in `docs/tracker/hardware-test-log.md`

**Test frequency:** every week during active development. Catch hardware/emulator divergences as soon as they appear.

### 11.5 Composer / pixel artist hire — **deferred, fallback only**

Default: self-art and self-compose. If by Week 6:
- Hero sprite hasn't landed at the bar → consider hiring pixel artist for hero + title art (most-load-bearing pieces)
- Title theme composition isn't working → consider hiring beeper composer

Budget for these as escalation options. Don't commit to hire pre-emptively; commit when needed.

---

## 12. The bar, restated

We are not shipping a programming curriculum. We are shipping a *real Spectrum game* that comes with a programming curriculum attached. The standard is: a 1988 *CRASH* reviewer, given a tape of this, would award it a Smash. Or at the very least, give it a serious review without condescension.

That bar:

- The hero looks designed.
- The walls look designed.
- The music sounds composed.
- The title screen reads like a presentation card.
- The collision and movement feel weighty, not jerky.
- The atmosphere is *of the keep* — moody, considered, hand-crafted.

If we hit that, CRASH! Live attendees will read the work as serious. If we miss it, they'll read it as an interesting project with shortcomings. The 32-unit plan is calibrated to hit it. This engineering plan is calibrated to make sure we don't miss.

---

## 13. Anchors

- **Spec:** [shadowkeep-32-unit-plan.md](shadowkeep-32-unit-plan.md)
- **Decision record:** [../decisions/shadowkeep-32-unit-commitment.md](../decisions/shadowkeep-32-unit-commitment.md)
- **Live tracker:** [revamp.md](revamp.md) — this is where day-to-day status lives
- **Beeper composition spec:** [shadowkeep-beeper-spec.md](shadowkeep-beeper-spec.md)
- **Project bar:** [../decisions/commercial-bar-revamp.md](../decisions/commercial-bar-revamp.md), [../decisions/real-retro-games.md](../decisions/real-retro-games.md)

## Log

| Date | Event |
|---|---|
| 2026-05-18 | Plan written. Phase 0 (pre-flight) begins. Pre-flight decisions in §11 must be answered before Phase 0 effort starts. |
