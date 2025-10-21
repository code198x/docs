# Phase 2: Action Foundations (Lessons 513-1024)

**Total:** 512 lessons across 8 tiers (64 lessons per tier)

**Phase Goal:** Master action game development through building 8 complete games across action sub-genres. Learn advanced combat, enemy AI, scrolling, and animation techniques.

**Prerequisites:** Phase 1 complete - assembly fundamentals, sprites, collision, basic physics, simple AI.

**Phase Philosophy:**
- Action = movement + combat + enemies + polish
- 64 lessons per game allows proper depth
- Progress from shooting to melee to hybrid
- Each game complete with multiple levels/stages
- Professional-quality animation and feel

**Game Progression:**
- **Tier 1:** Contra (Run-and-gun) - 8-direction shooting while moving
- **Tier 2:** Double Dragon (Beat-em-up) - Melee combat, group enemies
- **Tier 3:** Mega Man (Advanced platformer) - Weapons, stage select, bosses
- **Tier 4:** Castlevania (Gothic platformer) - Whip combat, sub-weapons, stages
- **Tier 5:** Barbarian (Hack-and-slash) - Sword combat, smooth animation
- **Tier 6:** Smash TV (Arena shooter) - Twin-stick, enemy waves, power-ups
- **Tier 7:** Prince of Persia (Cinematic platformer) - Precise physics, traps
- **Tier 8:** Shinobi (Complete synthesis) - Platforming + shooting + melee

**What Students Master:**
- Advanced sprite animation (multi-frame)
- Smooth scrolling (4-way, multi-directional)
- Complex enemy AI (state machines, formations, group behavior)
- Combat systems (melee, ranged, hybrid)
- Weapon and power-up systems
- Boss battle patterns
- Multiple simultaneous enemies
- Screen transitions and level structure
- Polish and game feel (impact, feedback, juice)
- Object pooling for bullets/enemies

---

## Phase 2 Overview

| Tier | Game | Deliverable | Key Skills |
|------|------|-------------|------------|
| 1 | Contra | Run-and-gun shooter | 8-direction aim, shooting while moving, enemy waves |
| 2 | Double Dragon | Beat-em-up | Melee combat, depth axis, group enemies, grab/throw |
| 3 | Mega Man | Boss rush platformer | Stage select, weapon switching, boss patterns |
| 4 | Castlevania | Gothic platformer | Whip combat, sub-weapons, hearts, stage progression |
| 5 | Barbarian | Sword fighter | Smooth animation, sword strikes, decapitation |
| 6 | Smash TV | Arena shooter | Twin-stick shooting, massive enemy counts, chaos |
| 7 | Prince of Persia | Cinematic platformer | Precise movement, environmental hazards, traps |
| 8 | Shinobi | Ninja action | Platforming + shooting + melee synthesized |

**Technical Progression:**
- Tiers 1-2: Shooting and melee fundamentals
- Tiers 3-4: Advanced platforming with combat
- Tiers 5-6: Specialized combat systems
- Tiers 7-8: Polish and synthesis

---

## Tier 1: Contra (Lessons 513-576)

**Goal:** Build Contra-style run-and-gun with 8-direction aiming and intense action.

**Why this game:** The definitive run-and-gun. Teaches shooting while moving, enemy waves, and action pacing.

**Game Requirements:**
- Player runs and shoots (8 directions)
- 3 stages (jungle, base, alien lair)
- Enemy waves (soldiers, turrets, alien creatures)
- Power-ups (spread gun, rapid fire, laser, barrier)
- Boss at end of each stage
- Lives system (3 lives, continues)
- Co-op 2-player (optional)

**Skills Introduced:**
- 8-direction aiming while moving
- Advanced bullet pooling
- Enemy wave spawning
- Power-up system architecture
- Stage progression
- Boss patterns (multiple phases)
- Scrolling with action
- Impact feedback

### Lesson Structure

**Lessons 513-520: Movement and Aiming**
- L513-514: 8-direction player movement
- L515-516: Separate aim direction from move direction
- L517-518: Player animation (running frames)
- L519-520: Smooth diagonal movement

**Lessons 521-528: Shooting System**
- L521-522: Bullet pooling (32 bullets)
- L523-524: 8-direction shooting
- L525-526: Bullet speed and movement
- L527-528: Bullet-enemy collision

**Lessons 529-536: Enemies**
- L529-530: Basic enemy (soldier)
- L531-532: Enemy spawning system
- L533-534: Enemy AI (run toward player, shoot)
- L535-536: Enemy waves (timing, variety)

**Lessons 537-544: Power-ups**
- L537-538: Power-up drops
- L539-540: Spread gun (3 bullets)
- L541-542: Rapid fire (faster shooting)
- L543-544: Laser (penetrating beam)

**Lessons 545-552: Stages**
- L545-546: Stage structure (3 stages)
- L547-548: Stage 1: Jungle (scrolling backgrounds)
- L549-550: Stage 2: Base (industrial hazards)
- L551-552: Stage 3: Alien Lair (organic enemies)

**Lessons 553-560: Bosses**
- L553-554: Boss 1: Defense Wall (turrets)
- L555-556: Boss 2: Tank (multiple phases)
- L557-558: Boss 3: Alien Heart (weak point)
- L559-560: Boss patterns and timing

**Lessons 561-568: Polish**
- L561-562: Explosion effects
- L563-564: Screen shake on hits
- L565-566: Sound effects (shooting, explosions, hits)
- L567-568: Lives and continues

**Lessons 569-576: Completion**
- L569-570: Stage transitions
- L571-572: Difficulty progression
- L573-574: Ending sequence
- L575-576: Final polish and testing

---

## Tier 2: Double Dragon (Lessons 577-640)

**Goal:** Build beat-em-up with melee combat, depth axis, and group enemies.

**Why this game:** Introduces depth (Y-axis movement), group AI, grab/throw mechanics.

**Game Requirements:**
- Side-scrolling with depth (walk up/down)
- Punch/kick combos
- Grab and throw enemies
- Multiple enemies on screen (3-5 simultaneous)
- Weapon pickups (bat, knife, barrel)
- Boss fights
- 2-player co-op
- 4 stages

**Skills Introduced:**
- Depth sorting (Y-axis determines draw order)
- Group AI (surround player, take turns attacking)
- Grab/throw system
- Combo system
- Weapon mechanics
- Crowd management
- Co-op collision handling

---

## Tier 3: Mega Man (Lessons 641-704)

**Goal:** Build Mega Man with stage select, weapon switching, and boss battles.

**Why this game:** Teaches weapon systems, stage select UI, boss patterns, rock-paper-scissors design.

**Game Requirements:**
- Stage select screen (8 robot masters)
- 8 stages (any order)
- Weapon system (8 weapons from bosses)
- Boss weaknesses (rock-paper-scissors)
- Energy tanks (health refills)
- Password system
- Lives system
- Final castle (4 stages)

**Skills Introduced:**
- Stage select UI
- Weapon switching
- Boss AI (complex patterns)
- Weapon effectiveness system
- Password generation/entry
- Energy management (health, weapon energy)
- Stage variety

---

## Tier 4: Castlevania (Lessons 705-768)

**Goal:** Build Castlevania with whip combat, sub-weapons, and gothic atmosphere.

**Why this game:** Teaches weapon arc/range, sub-weapon system, stage-based progression.

**Game Requirements:**
- Whip weapon (upgradeable)
- Sub-weapons (axe, holy water, cross, knife)
- Hearts (sub-weapon ammo)
- Candles drop items
- 6 stages
- Boss at end of each stage
- Lives and continues
- Password/checkpoint system

**Skills Introduced:**
- Weapon arc/range (whip)
- Sub-weapon system
- Resource management (hearts)
- Item drops (randomized)
- Stage atmosphere (gothic tileset)
- Boss variety
- Checkpoint system

---

## Tier 5: Barbarian (Lessons 769-832)

**Goal:** Build sword fighter with smooth animation and brutal combat.

**Why this game:** Teaches smooth multi-frame animation, impact feedback, dueling combat.

**Game Requirements:**
- Sword combat (slashes, overhead, thrust)
- Smooth animation (8+ frames per move)
- Block/parry system
- Decapitation finisher
- 1v1 duels
- Arena backgrounds
- Tournament progression
- 2-player vs mode

**Skills Introduced:**
- Multi-frame sprite animation
- Animation state machine
- Impact feedback (freeze frame, shake)
- Block/parry timing
- Special finishers
- 1v1 AI opponent
- Tournament structure

---

## Tier 6: Smash TV (Lessons 833-896)

**Goal:** Build arena shooter with twin-stick controls and massive enemy counts.

**Why this game:** Teaches twin-stick controls, extreme object counts, chaos management.

**Game Requirements:**
- Twin-stick shooting (move + aim separately)
- Arena rooms (clear all enemies to progress)
- Massive enemy counts (20+ on screen)
- Power-ups (spread, speed, shields)
- Cash/prizes for score
- 4 levels (TV shows)
- Boss at end of each level

**Skills Introduced:**
- Twin-stick controls (2-joystick or joystick + fire directions)
- Massive sprite multiplexing
- Enemy variety (runners, shooters, tanks)
- Power-up stacking
- Arena room structure
- Chaos and pacing

---

## Tier 7: Prince of Persia (Lessons 897-960)

**Goal:** Build cinematic platformer with precise physics and environmental hazards.

**Why this game:** Teaches precise movement, rotoscoped animation, trap timing.

**Game Requirements:**
- Precise platforming (running jumps, careful steps)
- Smooth animation (rotoscoped style)
- Environmental hazards (spikes, guillotines, falling floors)
- Sword duels with guards
- Time limit (60 minutes total)
- Checkpoint rooms
- 12 levels
- Princess rescue

**Skills Introduced:**
- Precise movement physics
- Rotoscoped-style animation
- Environmental hazards
- Trap timing
- Guard AI (sword fighting)
- Time pressure
- Checkpoint saving

---

## Tier 8: Shinobi (Lessons 961-1024)

**Goal:** Build complete ninja action game synthesizing all Phase 2 skills.

**Why this game:** Combines platforming + shooting + melee + magic. Complete action synthesis.

**Game Requirements:**
- Platforming (jumping, wall climbing)
- Shuriken throwing (ranged)
- Sword slashing (melee)
- Ninja magic (screen-clear bomb)
- Hostages to rescue
- 5 missions (multiple stages each)
- Boss battles
- Lives and continues
- Multiple enemy types

**Skills Introduced:**
- Hybrid combat (ranged + melee)
- Magic/special abilities
- Rescue objectives
- Mission structure
- Boss variety
- Everything from Phase 2 synthesized

**Lesson Structure:**

**Lessons 961-968: Movement**
- L961-962: Ninja movement (running, jumping)
- L963-964: Wall climbing
- L965-966: Crouching
- L967-968: Animation blending

**Lessons 969-976: Combat**
- L969-970: Shuriken throwing
- L971-972: Sword slashing
- L973-974: Combat switching
- L975-976: Combo system

**Lessons 977-984: Enemies**
- L977-978: Ninja enemies
- L979-980: Gunners
- L981-982: Dogs and hazards
- L983-984: Enemy formations

**Lessons 985-992: Missions**
- L985-986: Mission 1: Streets
- L987-988: Mission 2: Harbor
- L989-990: Mission 3: Airship
- L991-992: Mission 4: Jungle

**Lessons 993-1000: Bosses**
- L993-994: Boss patterns
- L995-996: Multi-phase bosses
- L997-998: Boss variety
- L999-1000: Final boss

**Lessons 1001-1008: Hostages**
- L1001-1002: Hostage placement
- L1003-1004: Rescue mechanics
- L1005-1006: Bonus points
- L1007-1008: Mission completion

**Lessons 1009-1016: Ninja Magic**
- L1009-1010: Magic meter
- L1011-1012: Screen-clear bomb
- L1013-1014: Magic management
- L1015-1016: Strategic use

**Lessons 1017-1024: Polish**
- L1017-1018: Sound effects
- L1019-1020: Visual feedback
- L1021-1022: Difficulty balance
- L1023-1024: Final polish and completion

---

## Phase 2 Outcome

Students have built **8 complete action games** and mastered:

**Advanced Combat:**
- Shooting (8-direction, twin-stick)
- Melee (punches, kicks, whip, sword)
- Hybrid systems (ranged + melee)
- Weapon switching
- Sub-weapons
- Power-ups

**Enemy AI:**
- Wave spawning
- Group behavior (surround, flank, take turns)
- Boss patterns (multi-phase)
- 1v1 dueling
- Formation attacks
- Crowd management

**Animation:**
- Multi-frame sprites (8+ frames)
- Smooth transitions
- Impact feedback
- Rotoscoped-style movement
- Animation state machines

**Level Design:**
- Stage progression
- Boss battles
- Checkpoint systems
- Environmental hazards
- Arena rooms
- Mission structure

**Game Systems:**
- Lives and continues
- Score and bonuses
- Resource management
- Time limits
- Password systems
- Stage select
- Weapon effectiveness

**Polish:**
- Screen shake
- Explosion effects
- Sound design
- Visual feedback
- Game feel (juice)
- Difficulty pacing

**Ready for Phase 3:** Students are prepared to tackle puzzle games and strategy, shifting from reflex-based action to logic-based challenges.

---

**Version:** 3.0
**Date:** 2025-10-20
**Status:** Complete restructure for 512-lesson phase
**Focus:** 8 action games from Contra to Shinobi
