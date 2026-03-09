# Full Game Outline: C64 Coldframe (256 Units)

**Game:** Coldframe (Game 2)
**Units:** 256 (8 phases × 32 units)
**Genre:** Stealth-puzzle platformer
**Inspired by:** Impossible Mission, Montezuma's Revenge, Raid on Bungeling Bay
**Target Quality:** Commercial-grade exploration game (1986–88 era)

---

## Premise

Dr. Coldframe's underground complex holds the prototype. You have 60 minutes to infiltrate, find the access codes, and escape. Guards patrol the corridors. Security systems scan the rooms. Terminals hold fragments of the final code. Search everything. Trust no one. Stay a while. Stay forever.

The complex is built from large scrolling rooms — each wider than the screen. The player somersaults across platforms, rides lifts between floors, searches furniture for code fragments, and avoids robot guards that patrol fixed routes. The SID creates claustrophobic tension: humming machinery, echoing footsteps, the synthesised voice that taunts you.

---

## Why This Game

Impossible Mission is the C64 at its most atmospheric. The large animated sprites, the scrolling rooms, the speech synthesis ("Another visitor..."), the tension of a ticking clock. It proved the C64 could do more than shooters — it could create mood.

Coldframe teaches:
- **VIC-II hardware scrolling** ($D016 fine scroll) — rooms wider than the screen
- **Large animated sprites** — the player's somersault is 8+ frames
- **Raster interrupts for scroll stability** — smooth scrolling without tearing
- **SID as atmosphere** — tension, not just action
- **Timer-driven gameplay** — the 60-minute countdown shapes every decision
- **Room-based exploration** — each room is a self-contained puzzle

This is the bridge between Nova Storm's action and Warfront's complex scrolling. The learner masters hardware scrolling and large sprites in a game that rewards patience over reflexes.

---

## 6510 Progression

| Phase | 6510 Focus |
|-------|-----------|
| 1 (Infiltration) | VIC-II scroll registers ($D016), screen/charset setup, smooth horizontal scroll |
| 2 (Corridors) | Large sprite animation, multi-frame character, sprite positioning during scroll |
| 3 (Security) | Robot patrol AI, collision systems, lift mechanics, floor transitions |
| 4 (Surveillance) | Search mechanics, terminal interaction, inventory, code fragment system |
| 5 (Tension) | SID atmosphere: ambient drones, footstep synthesis, tension escalation |
| 6 (Protocol) | Timer system, speech synthesis (SID digi-playback), countdown pressure |
| 7 (Clearance) | Room variety (30+ rooms), room data format, memory management |
| 8 (Extraction) | Puzzle completion, ending sequence, difficulty, high scores, distribution |

---

## Phase 1: Infiltration (Units 1–32)

**Goal:** One scrolling room with a player character.

| Unit | You Add | 6510 Skill | Result |
|------|---------|------------|--------|
| 1-4 | Screen setup, VIC bank configuration | VIC bank ($DD00), screen/charset pointers ($D018) | Display configured |
| 5-8 | Horizontal fine scroll | $D016 bits 0-2, 8-pixel shift cycle (fine scroll 0-7, then coarse shift) | **Screen scrolls** |
| 9-12 | Room tile map | Room wider than screen (64+ columns). Tile data feeds the scroll edge. | Room data drives scroll |
| 13-16 | Platform terrain | Floor tiles, wall tiles, empty space. Attribute-based or character-code-based collision. | Walkable room |
| 17-20 | Player character | Sprite on the scrolling background. Moves left/right, the scroll follows. | **Player in scrolling room** |
| 21-24 | Gravity and platforms | Player falls when no floor below. Lands on platforms. Jump from one level to another. | Platforming |
| 25-28 | Somersault | Jump is a somersault: 8-frame sprite animation cycling during the arc. Signature Impossible Mission move. | Animated jump |
| 29-32 | Room boundaries | Scroll stops at room edges. Door at each end leads to the next room (transition). | Room containment |

**Key Teaching Moment (Units 5-8):**
$D016 bits 0-2 are the fine scroll offset (0-7 pixels). Each frame, increment the offset. When it reaches 7, reset to 0 and shift the screen data by one character column (coarse scroll using LDIR-equivalent on 6510, or self-modifying code for speed). This is C64 hardware scrolling — the same technique every scrolling C64 game uses.

**End of Phase 1:** A scrolling room with platforming and the signature somersault. The C64 is scrolling.

---

## Phase 2: Corridors (Units 33–64)

**Goal:** Large sprite animation, room variety, lift mechanics.

| Unit | You Add | 6510 Skill | Result |
|------|---------|------------|--------|
| 33-36 | Player walk animation | 4-frame walk cycle per direction. Sprite pointer swap per frame. | Smooth walking |
| 37-40 | Player idle and search animations | Standing, searching (crouch at furniture), interaction poses | Character expressiveness |
| 41-44 | Lifts | Platforms that move vertically on command. Player rides the lift between floors. Sprite Y-tracking. | Vertical traversal |
| 45-48 | Multi-floor rooms | Rooms with 3-4 platform levels connected by lifts. More vertical gameplay. | Room depth |
| 49-52 | Room transitions | Walk to a door → screen wipe → new room loads from data → scroll resets. | Room loading |
| 53-56 | Colour RAM scrolling | Colour RAM must scroll in sync with the screen. Character-by-character shift. | Colour scroll |
| 57-60 | Room themes | Different tile sets per complex section: labs (white/cyan), offices (brown/yellow), server rooms (green/black). | Visual variety |
| 61-64 | 5 connected rooms | A corridor of 5 rooms linked by doors. Full scroll + platforms + lifts in each. | Explorable space |

**Key Teaching Moment (Units 53-56):**
Colour RAM ($D800-$DBFF) doesn't scroll with the screen — it's fixed. When the screen scrolls, the colour data must be manually shifted to match. This is an extra cost per frame: copy 1000 bytes (or the visible portion) one column left/right. On the C64, this is done character-by-character since the colour RAM isn't in the VIC bank.

**End of Phase 2:** 5 scrolling rooms with lifts, multiple floors, colour scroll, and full player animation. The complex feels real.

---

## Phase 3: Security (Units 65–96)

**Goal:** Robot guards, collision, danger.

| Unit | You Add | 6510 Skill | Result |
|------|---------|------------|--------|
| 65-72 | Robot guards | Sprites on patrol routes. Walk back and forth on platforms. Turn at edges. | Guards patrol |
| 73-76 | Guard-player collision | Touch a guard = death (or electrocution animation + life lost). | Danger |
| 77-80 | Guard variety | Slow guards (predictable), fast guards (tight timing), stationary laser barriers | Threat types |
| 81-84 | Guard sprites | Distinct robot designs. Walk animation. Alert flash when player is near (visual, not gameplay). | Visual menace |
| 85-88 | Guard timing patterns | Some guards pause at endpoints. Others reverse immediately. The player reads patterns and times crossings. | Stealth gameplay |
| 89-92 | Death and respawn | Electrocution animation (sprite flash + SID zap). Respawn at room entrance. Lose time, not just lives. | Consequence |
| 93-96 | Guards per room | Room data includes guard definitions (position, route, speed). Different rooms have different guard configurations. | Room-specific threat |

**End of Phase 3:** Robot guards patrol scrolling rooms. The player reads patterns and times their movement. Tension without combat.

---

## Phase 4: Surveillance (Units 97–128)

**Goal:** Search mechanics, terminals, code fragments — the puzzle layer.

| Unit | You Add | 6510 Skill | Result |
|------|---------|------------|--------|
| 97-100 | Searchable furniture | Stand at a desk/cabinet → press button → search animation → result | Interactive objects |
| 101-104 | Code fragments | Some furniture contains code fragments (letters/numbers). Collected into an inventory. | Puzzle pieces |
| 105-108 | Terminals | Special objects: approach → terminal screen (overlay) → password entry. Need correct code fragments. | Terminal interaction |
| 109-112 | Inventory display | Press a key → overlay shows collected fragments. Player sees their progress toward the final code. | Inventory UI |
| 113-116 | Red herring items | Some searches find nothing. Some find decoy codes. The player must figure out which fragments are real. | Deduction |
| 117-120 | Room reset on re-entry | Furniture resets (can search again). Guards reset. But collected codes persist. | Room state |
| 121-124 | The final code | All fragments assembled → enter at the master terminal → complex unlocked → escape route opens. | Win condition |
| 125-128 | 15 rooms | Expand to 15 rooms with varied furniture, terminals, guards. The complex has scale. | Substantial world |

**End of Phase 4:** 15 scrolling rooms with searchable objects, terminals, code fragments, and a solvable puzzle. The game is content-complete at a basic level.

---

## Phase 5: Tension (Units 129–160)

**Goal:** SID as atmosphere engine.

| Unit | You Add | 6510 Skill | Result |
|------|---------|------------|--------|
| 129-136 | Ambient SID | Machinery hum (low pulse wave, filter sweep). Different ambient per room section. | Background atmosphere |
| 137-144 | Footstep synthesis | Player footsteps: short noise bursts timed to walk animation. Pitch varies by surface. | Audio-visual sync |
| 145-148 | Guard sounds | Robot servo whir when guards move. Electrical zap on death. | Threat audio |
| 149-152 | Lift sounds | Mechanical clunk on lift start/stop. Motor hum during travel. | Environmental audio |
| 153-156 | Search sounds | Drawer opening, paper rustling, terminal beep on code found. | Interaction audio |
| 157-160 | Tension escalation | As timer decreases: ambient pitch rises slightly, filter cutoff drops, mood darkens. | Dynamic atmosphere |

**End of Phase 5:** The SID creates claustrophobic tension. Every action has a sound. The complex hums and clanks around you.

---

## Phase 6: Protocol (Units 161–192)

**Goal:** Timer, speech synthesis, countdown pressure.

| Unit | You Add | 6510 Skill | Result |
|------|---------|------------|--------|
| 161-168 | 60-minute countdown | CIA timer-driven countdown displayed in HUD. Ticks regardless of game state. | Time pressure |
| 169-172 | Timer warnings | At 30 minutes: SID alarm. At 10 minutes: border flashes. At 5 minutes: urgent pulse. | Escalating urgency |
| 173-180 | Speech synthesis | SID digi-playback: "Stay a while. Stay forever." At game start. "Destroy him, my robots!" on detection. | **The voice** |
| 181-184 | Speech technique | 4-bit samples played via SID volume register ($D418 bits 0-3). Timer interrupt drives playback. | Digi-audio on SID |
| 185-188 | Time bonus scoring | More time remaining = higher score. Incentivises efficient play. | Speed reward |
| 189-192 | Time-out game over | Timer reaches zero → "You have failed." → game over. The clock is the ultimate enemy. | Timer as antagonist |

**Key Teaching Moment (Units 173-180):**
SID speech synthesis: store 4-bit audio samples. A CIA timer interrupt fires at ~8KHz. Each interrupt writes the next sample to $D418 (volume register). The rapid volume changes create an audible waveform — speech from a chip designed for synthesis, not sampling. The quality is rough but unmistakable. "Stay a while. Stay forever." is one of gaming's most iconic audio moments.

**End of Phase 6:** The ticking clock shapes every decision. Speech synthesis adds personality. The game has genuine tension.

---

## Phase 7: Clearance (Units 193–224)

**Goal:** 30+ rooms, full complex, varied challenges.

| Unit | You Add | 6510 Skill | Result |
|------|---------|------------|--------|
| 193-200 | Rooms 16-22: Laboratory section | New tile set, new guard patterns, glass barriers (visible but passable in one direction) | Lab wing |
| 201-208 | Rooms 23-28: Server section | Dim lighting (dark colour RAM), terminal-heavy, more code fragments | Server wing |
| 209-216 | Rooms 29-32: Security section | Dense guards, laser barriers, the master terminal | Final section |
| 217-220 | Room map | Pause screen shows complex layout. Visited rooms marked. Terminal locations shown. | Navigation aid |
| 221-224 | Memory management | 30+ rooms × tile data + guard data. Bank switching or compression for 64K fit. | Data management |

**End of Phase 7:** 30+ rooms across three complex sections. A real Impossible Mission-scale facility.

---

## Phase 8: Extraction (Units 225–256)

**Goal:** Commercial polish, ship it.

| Unit | You Add | 6510 Skill | Result |
|------|---------|------------|--------|
| 225-228 | Ending sequence | Master terminal activated → alarms sound → escape route opens → run to exit → extraction | Narrative climax |
| 229-232 | Title screen | "COLDFRAME" with complex schematic. Speech plays on title: "Another visitor..." | Presentation |
| 233-236 | High scores with initials | Ranked by time remaining (faster = better) | Competition |
| 237-240 | Difficulty select | Easy (90 min, slow guards), Normal (60 min), Hard (45 min, fast guards, fewer codes) | Accessibility |
| 241-244 | Attract mode | Automated player explores the first room. Shows scrolling and somersault. | Demo mode |
| 245-248 | PAL/NTSC detection | Timer calibration, speed adjustment | Platform correct |
| 249-252 | Final testing | 30+ rooms, all guards, all terminals, all difficulties, timer accuracy | Release quality |
| 253-256 | Distribution | .PRG with autostart, loading screen, crunched binary | **Ship it** |

---

## Technical Notes

### Horizontal Scrolling

```asm
; Fine scroll: $D016 bits 0-2 (0-7 pixels)
; Coarse scroll: shift screen RAM + colour RAM by one character column

scroll_update:
    lda scroll_fine
    clc
    adc scroll_speed
    cmp #8
    bcc .fine_only

    ; Coarse scroll: shift screen data
    sbc #8
    sta scroll_fine
    jsr shift_screen_left
    jsr shift_colour_left
    jsr draw_new_column
    bra .set_register

.fine_only:
    sta scroll_fine

.set_register:
    lda $d016
    and #$f8            ; Clear bits 0-2
    ora scroll_fine     ; Set new fine scroll
    sta $d016
    rts
```

### Room Data Format

```
Room header:
  - Width (in character columns, typically 64-128)
  - Floor count (2-4 levels)
  - Guard count
  - Furniture count
  - Terminal count
  - Colour theme ID

Tile data: width × 25 bytes (one byte per character cell)
Guard data: per guard — x_start, x_end, y, speed, pause_frames
Furniture data: per item — x, y, contents_type (nothing, code_fragment, decoy)
Terminal data: per terminal — x, y, required_code_index

Compressed via RLE: ~200-400 bytes per room
30 rooms × 300 bytes average = ~9KB
```

### Memory Map

```
$0800-$0FFF: Screen RAM (VIC bank 0)
$1000-$1FFF: Character set (custom tiles)
$2000-$3FFF: Sprite data (player frames, guards, items)
$4000-$7FFF: Game code (~16KB)
$8000-$BFFF: Room data (compressed, ~12KB) + speech samples (~4KB)
$C000-$CFFF: Music data + sound routines
$D000-$DFFF: I/O space (VIC, SID, CIA)
$E000-$FFFF: Kernal ROM (or additional data if banked out)
```

---

## What This Teaches Beyond the Game

Coldframe bridges Nova Storm and Warfront:
- **From Nova Storm:** Sprite management, SID sound, raster interrupts — all reused
- **New in Coldframe:** Hardware scrolling, colour RAM sync, large sprites, room data, timer-driven gameplay
- **To Warfront:** Scrolling becomes 8-way. Large sprites become multi-sprite bosses. Room data becomes level streaming. The techniques scale up.

---

## Changelog

- **v1.0 (2026-03-09):** Initial outline. New Game 2 for the restructured C64 assembly track. Stealth-puzzle with scrolling rooms, robot guards, and code-fragment puzzle.
