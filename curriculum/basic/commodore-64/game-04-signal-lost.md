# Game 04: Signal Lost

**Track:** C64 BASIC
**Genre:** Turn-based space survival with SID atmosphere
**Units:** 64 (4 phases × 16 units)
**Language:** Stock BASIC V2
**Max lines:** ~500
**Save/load:** No — each run is 15-30 minutes

---

## Premise

Your ship drops out of hyperspace in an uncharted sector. The navigation computer is damaged. The distress beacon is offline. Between you and the nearest starbase are 20 sectors of empty space — and it's not empty.

Each turn, you choose: move to an adjacent sector, scan for threats, repair a system, or charge weapons. Fuel depletes with every move. Hostile ships patrol some sectors. Debris fields damage your hull. Supply caches offer temporary relief. The SID chip is your bridge: engine hum, scanner pings, shield impacts, weapon fire, and the rising tension drone when hostiles are near.

The game is turn-based — BASIC speed is irrelevant. The SID is everything: without it, the game is a silent spreadsheet. With it, you're commanding a ship.

---

## Core Mechanics

### The Sector Map

A 5×4 grid of 20 sectors. The player starts at one edge; the starbase is at the opposite edge. Each sector contains one of:

| Contents | Frequency | Description |
|----------|-----------|-------------|
| Empty space | 40% | Safe. Costs fuel to traverse. |
| Hostile ship | 20% | Combat encounter. Must fight or flee. |
| Debris field | 15% | Hull damage on entry. Can be scanned first to avoid. |
| Supply cache | 10% | Restore fuel, hull, or ammo. Random. |
| Nebula | 10% | Sensors blocked. Can't scan adjacent sectors. |
| Starbase | 1 sector | The goal. Reach it to win. |

The map is hidden. Sectors are revealed by visiting them or scanning. The player sees only their current sector and any scanned adjacent sectors.

### Ship Systems

| System | Range | Depletes by | Restored by |
|--------|-------|-------------|-------------|
| Hull | 0-100 | Debris (−15), combat (−10-25) | Supply cache (+20) |
| Fuel | 0-50 | Moving (−1 per sector), fleeing combat (−3) | Supply cache (+10) |
| Shields | 0-5 charges | Absorbing hits (−1 per hit) | Repair action (+1, costs 1 turn) |
| Weapons | 0-10 ammo | Firing (−1 per shot) | Supply cache (+5) |
| Scanner | Functional/damaged | Nebula entry (temporary) | Repair action (1 turn) |

### Turn Actions

Each turn, the player chooses one:

| Action | Effect | SID sound |
|--------|--------|-----------|
| **MOVE** [direction] | Enter adjacent sector. Costs 1 fuel. Reveals sector. | Engine throb (pulse wave, pitch varies with fuel level) |
| **SCAN** [direction] | Reveal adjacent sector without entering. Free. | Scanner ping (triangle, rising pitch, echo) |
| **REPAIR** [system] | Restore 1 shield charge or fix scanner. Costs 1 turn. | Wrench sounds (noise channel, rhythmic) |
| **FIRE** | In combat only. Spend 1 ammo, deal damage. | Weapon blast (all three voices, sharp attack) |
| **FLEE** | In combat only. Escape to previous sector. Costs 3 fuel. | Engine roar (pulse wave, ascending pitch, urgent) |
| **WAIT** | Do nothing. Hostile ships may move. | Ambient hum only |

### Combat

When the player enters a sector with a hostile ship, combat begins. Turn-based rounds:

1. Player acts: FIRE, FLEE, or use a shield charge
2. Enemy acts: fires at player (automatic, chance to hit based on enemy type)
3. Repeat until one side is destroyed or the player flees

Enemy types:

| Type | Hull | Damage | Accuracy | Points |
|------|------|--------|----------|--------|
| Scout | 10 | 5 | 40% | 50 |
| Fighter | 20 | 10 | 60% | 100 |
| Cruiser | 35 | 15 | 75% | 200 |

Combat is simple but tense because every hit costs hull or shields, ammo is limited, and fleeing costs precious fuel.

### Winning and Losing

- **Win**: Reach the starbase with hull > 0
- **Lose (hull)**: Hull reaches 0 — ship destroyed
- **Lose (fuel)**: Fuel reaches 0 — adrift, game over
- **Rating**: Based on hull remaining, sectors explored, hostiles destroyed, fuel efficiency

---

## The SID as Atmosphere Engine

This is the game's central design principle. The SID chip has three voices, each with waveform, frequency, ADSR envelope, and filter control. Every game event maps to specific SID registers:

### Voice Allocation

| Voice | Primary role | Registers |
|-------|-------------|-----------|
| Voice 1 ($D400-$D406) | Engine/movement sounds | Pulse wave, low frequency, slow filter sweep |
| Voice 2 ($D407-$D40D) | Scanner/UI sounds | Triangle wave, mid frequency, sharp envelope |
| Voice 3 ($D40E-$D414) | Combat/alert sounds | Sawtooth/noise, variable frequency, aggressive envelope |
| Filter ($D415-$D418) | Atmosphere shaping | Low-pass for muffled ambience, band-pass for tension |

### Sound Design

| Event | Voices | Waveform | Frequency | ADSR | Filter | Feel |
|-------|--------|----------|-----------|------|--------|------|
| Engine idle | 1 | Pulse (50% duty) | Very low (~100 Hz) | A:0 D:8 S:12 R:8 | Low-pass, low cutoff | Constant background throb |
| Engine move | 1 | Pulse (narrowing) | Low→mid sweep | A:2 D:4 S:8 R:4 | Low-pass, rising cutoff | Power surge on movement |
| Engine flee | 1 | Pulse (rapid duty cycle) | Mid→high sweep | A:0 D:0 S:15 R:0 | Low-pass, high cutoff | Urgent, panicked |
| Scanner ping | 2 | Triangle | Mid, descending | A:0 D:8 S:0 R:12 | None | Clean sonar ping |
| Scanner contact | 2 | Triangle | Rising two-note | A:0 D:4 S:8 R:8 | Band-pass | Something's there |
| Weapon fire | 1+2+3 | Pulse+saw+noise | High, descending | A:0 D:4 S:0 R:2 | Band-pass, high res | Full three-voice blast |
| Shield absorb | 3 | Triangle | Mid, stable | A:0 D:12 S:6 R:12 | Low-pass | Dull impact absorbed |
| Hull damage | 3 | Noise | N/A | A:0 D:0 S:12 R:4 | Low-pass, low cutoff | Crunch, structural stress |
| Hostile near | 3 | Sawtooth | Low, pulsing | A:4 D:4 S:10 R:4 | Band-pass, resonance sweep | Tension drone |
| Supply found | 2 | Triangle | Ascending arpeggio | A:0 D:6 S:8 R:6 | None | Relief, three rising notes |
| Starbase reached | 1+2+3 | Triangle+triangle+triangle | Major chord | A:2 D:8 S:12 R:12 | None | Triumph, three-voice harmony |
| Ship destroyed | 1+2+3 | Noise+noise+saw | Descending | A:0 D:0 S:15 R:15 | Low-pass, descending cutoff | Everything fading out |

### The Engine Idle

The most important sound: a constant low pulse-wave throb that runs whenever the game is at the command prompt. This is the ship's heartbeat. It changes subtly based on ship state:
- Full fuel: steady, confident pitch
- Low fuel: slightly lower, wavering (modulate duty cycle)
- Damaged hull: add occasional noise-channel creak
- Shields down: filter cutoff drops, sound becomes muffled

The player learns to read their ship's health by ear before they look at the numbers.

---

## Visual Design

### Screen Layout

```
╔══════════════════════════════════════╗
║ SIGNAL LOST          SECTOR: 3,2    ║
║ ─────────────────────────────────── ║
║                                      ║
║  HULL: ████████░░ 65%  SHIELDS: ██░  ║
║  FUEL: ███████░░░ 34   AMMO: ████ 7  ║
║                                      ║
║  ┌─────────────────────┐            ║
║  │  ?   ?   ?   ?   ?  │            ║
║  │  ?   .   ☼   ?   ?  │  SECTOR    ║
║  │  ?   .   @   !   ?  │  CONTENTS: ║
║  │  ?   ?   .   ?   ?  │  Empty     ║
║  └─────────────────────┘            ║
║                                      ║
║  @ = You   . = Explored  ? = Unknown ║
║  ! = Scanned (hostile)  ☼ = Supply   ║
║                                      ║
║  SCANNER: Contact detected EAST      ║
║                                      ║
║  > COMMAND: _                        ║
╚══════════════════════════════════════╝
```

### Sector Map Symbols

| Symbol | Colour | Meaning |
|--------|--------|---------|
| @ | White (1) | Player position |
| . | Grey (11) | Explored, empty |
| ? | Dark grey (12) | Unexplored |
| ! | Red (2) | Scanned hostile |
| ☼ | Yellow (7) | Scanned supply |
| ≈ | Cyan (3) | Nebula |
| # | Green (5) | Debris (scanned) |
| ★ | Light green (13) | Starbase |

### Combat Screen

During combat, the display changes:

```
╔══════════════════════════════════════╗
║ !! COMBAT !!    ENEMY: FIGHTER      ║
║                                      ║
║  YOUR SHIP          ENEMY SHIP       ║
║  Hull:  65%         Hull:  20/20     ║
║  Shields: 2         Status: ACTIVE   ║
║  Ammo: 7                             ║
║                                      ║
║  [F]IRE  [S]HIELD  [R]UN            ║
║                                      ║
║  > _                                 ║
╚══════════════════════════════════════╝
```

---

## Phase Breakdown

### Phase 1: The Ship (Units 1-16)

The SID makes sound. The ship has systems. The player enters commands. No map, no enemies yet — just the bridge.

| Unit | Title | What the learner builds | Code concepts |
|------|-------|------------------------|---------------|
| 1 | First Sound | POKE 54296, 15 (volume). POKE 54273, 28: POKE 54272, 49 (frequency). POKE 54276, 17 (triangle, gate on). A note plays. The SID lives. | SID volume, frequency, waveform, gate |
| 2 | Attack and Decay | POKE 54277, $09 (attack 0, decay 9). POKE 54278, $00 (sustain 0, release 0). Gate on then off → the note fades. ADSR shapes the sound. | ADSR envelope, gate on/off |
| 3 | Three Voices | Voice 2 at $D407. Voice 3 at $D40E. Play three notes simultaneously — a chord. Each voice is independent. | Three SID voices, register offsets |
| 4 | Waveforms | Same note, different waveforms: triangle (smooth), sawtooth (bright), pulse (hollow), noise (harsh). POKE control register with 17, 33, 65, 129. | Waveform selection, tonal character |
| 5 | The Engine Idle | Voice 1: pulse wave, very low frequency, long sustain. It throbs continuously. This is the ship's heartbeat. Play it and leave it running. | Continuous sound, pulse wave, low frequency |
| 6 | The Scanner Ping | Voice 2: triangle wave, mid frequency, short decay, no sustain. Gate on then immediately off → a clean ping that fades. | Short percussive sound, triangle |
| 7 | Ship Status Display | PRINT the ship status: hull bar, fuel counter, shields, ammo. Formatted layout. No POKE to screen — PRINT is fine for a strategy game. | Status display, bar rendering |
| 8 | Commands | INPUT "COMMAND: "; C$. Parse the first word: MOVE, SCAN, REPAIR, WAIT. Dispatch to GOSUB. | Command parsing, dispatch |
| 9 | Fuel and Movement | MOVE N/S/E/W. Fuel decreases by 1. Position updates. Engine sound plays during move (brief pulse surge). | Resource depletion, directional input |
| 10 | The Filter | POKE 54293 (filter cutoff), 54294 (resonance + filter mode). Low-pass filter makes sounds muffled. Sweep the cutoff → sounds open up and close down. | SID filter, cutoff, resonance, filter modes |
| 11 | Engine + Filter | Tie filter cutoff to fuel level. Full fuel: open filter, bright engine sound. Low fuel: closed filter, muffled and ominous. The ship sounds sick when it's running out. | Dynamic filter control, state-driven audio |
| 12 | Repair Action | REPAIR SHIELDS restores 1 charge. Costs a turn. Repair sound: noise channel with rhythmic pattern (wrench turning). | New command, noise waveform |
| 13 | Hull Damage Sound | When hull takes damage: noise burst + low-frequency pulse thud. Two voices simultaneously for impact. | Multi-voice sound effect |
| 14 | Supply Found Sound | Three ascending triangle notes (arpeggio). Voice 2 plays note 1, brief pause, note 2, pause, note 3. Relief and reward. | Sequential notes, timed playback |
| 15 | Sound Library | Organise all sounds into GOSUBs: GOSUB 8000 (engine idle), GOSUB 8100 (ping), GOSUB 8200 (fire), etc. Clean, reusable. | Sound as subroutines, code organisation |
| 16 | The Bridge | Status display, command input, engine idle running, sounds for every action. No map, no enemies — but the bridge feels alive. | Integration, atmosphere |

**Milestone:** A living ship bridge. The SID provides a constant engine throb that changes with fuel level. Every action has a sound. The learner has POKEd every SID register category: frequency, waveform, ADSR, filter. The ship feels real.

### Phase 2: The Void (Units 17-32)

The sector map, scanning, hazards, and the journey to the starbase.

| Unit | Title | What the learner builds | Code concepts |
|------|-------|------------------------|---------------|
| 17 | The Sector Map | A 5×4 grid of sectors, displayed with PRINT. Player position shown. All sectors start as "?" (unknown). | Grid display, hidden state |
| 18 | Map Generation | Random sector contents: 40% empty, 20% hostile, 15% debris, 10% supply, 10% nebula. Starbase at opposite edge. | Random generation, DIM for map array |
| 19 | Movement on Map | MOVE N/S/E/W moves between sectors. Current sector revealed (? → contents). Map redraws. | Map traversal, state reveal |
| 20 | Scanning | SCAN E reveals the sector to the east without entering. "SCANNER: Contact detected — HOSTILE." Ping sound plays. | Scan mechanic, adjacent cell peek |
| 21 | Scanner Contact Sound | Different scan results: empty = single ping. Hostile = rising two-note warning. Supply = cheerful double-ping. | Context-dependent sound |
| 22 | Debris Fields | Enter a debris sector: hull takes 15 damage. Crunch sound (noise + pulse). "HULL BREACH — DAMAGE SUSTAINED." | Hazard encounter, damage sound |
| 23 | Supply Caches | Enter a supply sector: random restoration (fuel, hull, or ammo). Ascending arpeggio sound. "SUPPLY CACHE FOUND — FUEL +10." | Supply pickup, random reward |
| 24 | Nebulae | Enter a nebula: scanner disabled until you leave. No scan results. Ambient sound changes (filter closes, muffled). | Environmental effect, disabled system |
| 25 | The Tension Drone | When adjacent to a hostile sector (whether known or unknown), Voice 3 plays a low sawtooth drone with filter sweep. Tension builds. | Proximity-based ambient sound |
| 26 | Fuel Pressure | At fuel 10: warning message + engine pitch drops. At fuel 5: urgent warning + engine stutters (gate on/off rapidly). At fuel 0: game over. | Resource pressure, audio warning |
| 27 | The Starbase | Reach the starbase sector: victory. Three-voice major chord. "STARBASE REACHED — SIGNAL RESTORED." Score and rating. | Win condition, victory sound |
| 28 | Running on Empty | Game over at fuel 0: engine sound fades (frequency descends, volume descends). "FUEL EXHAUSTED — ADRIFT." Silence. Powerful ending. | Fade-out sound, defeat atmosphere |
| 29 | Ship Destroyed | Hull at 0: explosion sound (all three voices, noise + descending pitch). "HULL INTEGRITY ZERO." Silence. | Destruction sound |
| 30 | The Full Journey | 20 sectors from start to starbase. Random map, hazards, supplies. Playable. Is 50 fuel enough? Is the starbase reachable? Balance. | First complete playthrough, balance |
| 31 | Sector Descriptions | Each sector type has flavour text. "Empty space stretches in every direction. Your engine hums." "Twisted metal drifts past — a debris field." | Atmospheric writing, immersion |
| 32 | Sound Atmosphere | Review every game state's sound. Is the engine always running? Does the tension drone trigger correctly? Does combat feel distinct? | Audio continuity, atmosphere review |

**Milestone:** A complete journey from start to starbase across 20 random sectors. Scanning, hazards, supplies, nebulae. The SID creates tension (hostile proximity), relief (supply found), and dread (low fuel). Playable and atmospheric.

### Phase 3: Combat and Depth (Units 33-48)

Combat encounters, enemy variety, and the systems that create replayability.

| Unit | Title | What the learner builds | Code concepts |
|------|-------|------------------------|---------------|
| 33 | Combat Encounter | Enter a hostile sector: switch to combat display. "HOSTILE VESSEL DETECTED — FIGHTER CLASS." | Screen mode switch, combat state |
| 34 | Fire Command | FIRE: spend 1 ammo, calculate hit (RND vs accuracy). Hit: damage enemy hull. Miss: "SHOT MISSED." | Combat RNG, hit calculation |
| 35 | Weapon Fire Sound | All three voices: pulse high + sawtooth mid + noise burst. Sharp attack, fast decay. The most satisfying sound in the game. | Three-voice sound effect, coordinated ADSR |
| 36 | Enemy Fires Back | After player acts, enemy fires. Hit chance based on enemy type. Shield absorbs first, then hull damage. | Enemy turn, damage routing |
| 37 | Shield Absorb Sound | Shield hit: triangle wave, mid frequency, long decay. Dull but reassuring — damage blocked. | Defensive sound, contrast with hull damage |
| 38 | Enemy Destroyed | Enemy hull reaches 0: "HOSTILE DESTROYED." Explosion sound. Points awarded. Return to map. | Combat victory, score |
| 39 | Flee | FLEE command: costs 3 fuel, returns to previous sector. Engine roar sound (ascending pulse, urgent). Enemy gets one free shot as you flee. | Escape mechanic, risk/reward |
| 40 | Three Enemy Types | Scout (weak, inaccurate), Fighter (medium), Cruiser (strong, accurate). Different combat feel. | Enemy variety, parameterised combat |
| 41 | Cruiser Dread | When scan reveals a cruiser: a deeper, slower tension drone than fighter/scout. The player HEARS the danger level before reading the text. | Threat-level audio, fear through sound |
| 42 | Ring Modulation | POKE 54276 with bit 2 set: ring modulation. Voice 1 modulates Voice 3. Metallic, alien sound for cruiser encounters. | Ring mod register, advanced SID |
| 43 | Pulse Width Modulation | Vary the pulse width (POKE 54274/54275) during engine idle. Slowly sweeping from thin to thick pulse creates a living, breathing engine sound. | PWM, duty cycle sweep |
| 44 | Hard Sync | POKE 54276 with bit 1 set: hard sync. Voice 1 syncs to Voice 3. Buzzy, cutting sound for alarms and warnings. | Hard sync register, advanced SID |
| 45 | Difficulty Levels | Easy: 60 fuel, weak enemies, more supplies. Normal: 50 fuel, mixed enemies. Hard: 40 fuel, strong enemies, fewer supplies. | Difficulty parameters |
| 46 | Score and Rating | Score based on: sectors explored, hostiles destroyed, hull remaining, fuel efficiency. Rank: Cadet → Lieutenant → Commander → Admiral. | Scoring formula, rank thresholds |
| 47 | High Score | Session high score tracked. Displayed on title screen. | Best score tracking |
| 48 | Balance Pass | Play all three difficulties. Is Hard possible but punishing? Is Easy too easy? Does every encounter feel meaningful? | Full balance testing |

**Milestone:** Complete combat system with three enemy types. Advanced SID techniques (ring mod, hard sync, PWM) create distinct sounds for different threats. The player reads danger by ear.

### Phase 4: Polish and Legacy (Units 49-64)

Title screen, presentation, the SID showcase, and the bridge to assembly.

| Unit | Title | What the learner builds | Code concepts |
|------|-------|------------------------|---------------|
| 49 | Title Screen | "SIGNAL LOST" in large text. The engine idle plays from the title screen. A lone ship, a vast void. Set the mood before gameplay begins. | Title design, audio from first screen |
| 50 | Title Music | A simple three-voice theme on the title screen. 8-16 bars of slow, atmospheric music. DATA-driven: note, duration, voice. | Music playback, DATA-driven sequencing |
| 51 | Music Playback System | GOSUB that reads note DATA and POKEs SID registers. Steps through notes at a timed rate. Can play during any screen. | Music engine in BASIC, timed note stepping |
| 52 | Instructions | "HOW TO PLAY" screen with command list, system descriptions, and — crucially — a sound demo. Play each sound with a label. | Audio documentation, sound showcase |
| 53 | Captain's Log | After each turn, a brief log entry appears: "Turn 14: Moved to sector 3,2. Fuel at 31. All quiet." History of the last 5 turns. | Turn log, scrolling history |
| 54 | Sector Atmosphere | Each sector type has a distinct ambient sound that plays continuously while in that sector. Empty = engine only. Nebula = muffled + filter. Debris = occasional creaks. | Per-sector ambient audio, continuous sound |
| 55 | Damaged Ship Sounds | Below 30% hull: random creaking noises between turns (noise channel, brief). Below 15%: alarms (hard sync, piercing). The ship is falling apart. | Conditional ambient sound, damage states |
| 56 | Encounter Intro | Hostile encounter: brief dramatic pause, tension chord (three voices, minor), THEN the combat screen. Build anticipation. | Dramatic timing, musical tension |
| 57 | The SID Reference Card | A unit dedicated to documenting every SID register the learner has used. Print a reference card they can keep. Every address, every bit, every effect. | Documentation, register reference |
| 58 | What Assembly Would Do | Discussion: interrupt-driven music that plays continuously behind game logic. Raster-timed audio updates. Multi-speed playback for complex tunes. None of this is possible in BASIC — the music stops when the game thinks. | Bridge to assembly, SID in assembly context |
| 59 | Edge Cases | What if the player is surrounded by hostiles? (They can still scan and plan.) What if they run out of ammo? (Must flee all combats — expensive in fuel.) | Design validation, no-win scenarios |
| 60 | Bug Sweep | Every sector type, every combat outcome, every sound trigger. Systematic testing across all difficulties. | QA methodology |
| 61 | Sound Continuity | Play a full game focused only on listening. Does the engine always run? Do transitions between sectors reset sounds correctly? Any pops or clicks? | Audio QA, continuity |
| 62 | Atmosphere Review | Play in a dark room. Does the game feel tense? Does the SID create genuine atmosphere? Would it feel the same without sound? (Test: volume 0.) | Atmosphere validation, audio importance |
| 63 | Line Count | Under 500 lines? Sound routines (~80 lines), music data (~40 lines), map/combat logic (~300 lines), display (~80 lines). Tight but achievable. | Code budget |
| 64 | The Finished Game | A turn-based space survival game where the SID chip IS the atmosphere. 20-sector journey, three enemy types, ring mod and hard sync and PWM, title music, and the honest conclusion: BASIC can make the SID sing — but only one note at a time. Assembly makes it an orchestra. | Completion, C64 BASIC track finale |

**Milestone:** The C64 BASIC track's finale. Every SID register mastered through gameplay. Engine hum, scanner pings, weapon blasts, tension drones, title music. The player has felt what the SID can do — and understood what it can't do without assembly's interrupt-driven timing.

---

## Technical Notes

### SID Register Map (Relevant Subset)

```
Voice 1:
  $D400 (54272) - Frequency low
  $D401 (54273) - Frequency high
  $D402 (54274) - Pulse width low
  $D403 (54275) - Pulse width high
  $D404 (54276) - Control: gate, sync, ring mod, waveform
  $D405 (54277) - Attack/Decay
  $D406 (54278) - Sustain/Release

Voice 2: $D407-$D40D (54279-54285) — same layout
Voice 3: $D40E-$D414 (54286-54292) — same layout

Filter:
  $D415 (54293) - Filter cutoff low (bits 0-2)
  $D416 (54294) - Filter cutoff high
  $D417 (54295) - Resonance (bits 4-7) + filter voice routing (bits 0-2)
  $D418 (54296) - Volume (bits 0-3) + filter mode (bits 4-6)
```

### Sound Subroutine Pattern

```basic
8000 REM ENGINE IDLE
8010 POKE 54272, 49: POKE 54273, 1: REM LOW FREQUENCY
8020 POKE 54274, 0: POKE 54275, 8: REM PULSE WIDTH 50%
8030 POKE 54277, 9: POKE 54278, 160: REM A:0 D:9 S:10 R:0
8040 POKE 54276, 65: REM PULSE WAVE, GATE ON
8050 RETURN
```

### Note Frequency Table

Common note frequencies for SID (high byte only, low byte = 0 for simplicity):

```basic
9000 DATA 17,18,19,21,22,23,25,26,28,30,31,33: REM C2-B2
9010 DATA 34,36,39,41,44,46,49,52,55,58,62,65: REM C3-B3
9020 DATA 69,73,78,82,87,92,98,104,110,117,123,131: REM C4-B4
```

### Music Data Format

```basic
9100 DATA 34,4, 41,4, 49,4, 52,8: REM NOTE_FREQ, DURATION PAIRS
9110 DATA 0,4: REM 0 = REST
9120 DATA -1: REM END OF MUSIC
```

Music playback GOSUB reads pairs, POKEs frequency, gates on, counts duration ticks, gates off, reads next pair.

### Memory Budget

- Game logic: ~8-10 KB
- Sound routines: ~2-3 KB
- Music data: ~1 KB
- Display routines: ~2 KB
- Map/combat data: ~1 KB
- Total: ~14-17 KB — comfortable

### Line Numbering

- 1-49: Initialisation, SID setup, volume
- 50-99: Title screen, title music
- 100-199: Map display, status display
- 200-299: Main game loop, command parsing
- 300-399: Movement, scanning, sector reveal
- 400-499: Combat loop
- 500-599: Damage, supply, fuel management
- 600-699: Game over, victory, high score
- 700-799: Display routines, combat screen
- 800-899: HUD, captain's log
- 8000-8499: Sound subroutines (engine, ping, fire, damage, etc.)
- 8500-8999: Music data and playback
- 9000-9999: Frequency tables, map generation DATA

---

## Design Notes

### Why a Turn-Based Game

The SID needs time. Playing a three-voice weapon blast takes ~50ms of POKE calls. A music step takes ~20ms. In a real-time game, these pauses would stutter the action. In a turn-based game, they're dramatic beats — the player presses FIRE and HEARS the result. The pause IS the drama.

### The SID Progression

The C64 BASIC track teaches hardware in layers:
1. **Depth Charge**: Pure BASIC. No hardware access.
2. **Neon Nexus**: Screen RAM and colour RAM via POKE/PEEK.
3. **Starswarm**: VIC-II sprite registers via POKE.
4. **Signal Lost**: SID audio registers via POKE.

Each game adds a hardware subsystem. By the end, the learner has POKEd screen memory, colour RAM, VIC-II sprite registers, and SID audio registers. The assembly track replaces POKE with STA — same addresses, same hardware, faster access.

### Sound as Information

The game deliberately encodes game state in audio:
- Fuel level → engine pitch and filter cutoff
- Hull damage → creaking and alarm frequency
- Hostile proximity → tension drone presence and intensity
- Sector type → ambient sound character

A skilled player can assess their situation by ear. This isn't just atmosphere — it's game design. The SID isn't decoration; it's a UI element.

### The Four-Game Arc

1. **Depth Charge**: Logic and deduction (PRINT, INPUT, arrays)
2. **Neon Nexus**: Visual action (POKE screen, PEEK collision)
3. **Starswarm**: Smooth sprites (VIC-II registers, hardware collision)
4. **Signal Lost**: Atmospheric sound (SID registers, filter, ring mod)

Four games, four hardware layers. A complete tour of the C64 through BASIC — and an honest conclusion about why assembly is the next step.

---

## Changelog

- **v1.0 (2026-03-09):** Initial game outline. New Game 4 in the restructured C64 BASIC track. Turn-based space survival with SID atmosphere as the core design principle.
