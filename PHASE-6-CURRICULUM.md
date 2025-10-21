# Phase 6: Shoot-em-ups (Lessons 2433-3456)

**Total:** 1024 lessons across 16 tiers (64 lessons per tier)

**Phase Goal:** Master THE defining C64 genre. Build 16 complete shoot-em-ups spanning all sub-genres. Achieve sprite multiplexing mastery (100+ sprites on screen).

**Prerequisites:** Phases 1-5 complete (all foundational systems, especially Contra, Smash TV from Phase 2)

**Phase Philosophy:**
- Shoot-em-ups = THE C64 genre
- Deserves 1024 lessons for comprehensive coverage
- Sprite multiplexing is the most important advanced technique
- 16 games covers all shmup sub-genres
- Bullet patterns are an art form
- Boss battles define the experience
- Professional-quality required

**Game Progression:**
- **Vertical Shooters (Tiers 1-4):** 1942, 1943, Xevious, Twin Cobra
- **Horizontal Shooters (Tiers 5-10):** Silkworm, R-Type, Gradius, Nemesis, Katakubi, Delta
- **Multi-directional (Tiers 11-13):** Robotron, Smash TV Advanced, Berzerk
- **Hybrid Shooters (Tiers 14-16):** Uridium, Zynaps, Armalyte

**What Students Master:**
- **Sprite multiplexing** (100+ sprites with 8 hardware sprites)
- Bullet pattern design (spreads, spirals, aimed, bullet hell)
- Enemy formations (waves, V-formations, swoops)
- Parallax scrolling (3-4 background layers)
- Power-up systems (weapon bars, options, shields)
- Boss battles (multi-phase, complex patterns, weak points)
- Scoring systems (combos, grazing, multipliers)
- Screen-filling effects (explosions, bullets)
- IRQ optimization for smooth multiplexing
- Collision optimization (spatial partitioning)

---

## Phase 6 Overview

| Tier | Game | Sub-genre | Deliverable | Key Skills |
|------|------|-----------|-------------|------------|
| 1 | 1942 | Vertical | WWII plane shooter | Formations, power-ups, loop mechanic |
| 2 | 1943 | Vertical | Enhanced 1942 | Energy bar, ship upgrades, battleship boss |
| 3 | Xevious | Vertical | Ground + air targeting | Dual-axis combat, Solvalou ship |
| 4 | Twin Cobra | Vertical | Intense vertical | Heavy bullet patterns, speed |
| 5 | Silkworm | Horizontal | Helicopter + jeep | Co-op asymmetry, ground/air split |
| 6 | R-Type | Horizontal | Force pod classic | Charge beam, grotesque enemies, stages |
| 7 | Gradius | Horizontal | Power-up bar | Options, volcano, weapon selection |
| 8 | Nemesis | Horizontal | Multiple weapons | Shield system, weapon variety |
| 9 | Katakubi | Horizontal | Speed-based | Scoring system, fast action |
| 10 | Delta | Horizontal | Weapon variety | Enemy diversity, complex stages |
| 11 | Robotron 2084 | Multi-dir | Twin-stick classic | Save humans, 100+ enemies, chaos |
| 12 | Smash TV Advanced | Multi-dir | Arena perfection | Extreme multiplexing, prizes, insanity |
| 13 | Berzerk | Multi-dir | Room-based | Evil Otto, voice synthesis, escape |
| 14 | Uridium | Hybrid | Low-flying dreadnought | Large ships, side-view, exploration |
| 15 | Zynaps | Hybrid | Weapon pods | Transforming ship, pod system |
| 16 | Armalyte | Hybrid | Technical showcase | Advanced graphics, smooth, synthesis |

**Technical Progression:**
- Tiers 1-4: Vertical scrolling, formations, basic multiplexing
- Tiers 5-10: Horizontal scrolling, advanced multiplexing, boss mastery
- Tiers 11-13: Multi-directional, extreme sprite counts, chaos management
- Tiers 14-16: Hybrid styles, all techniques synthesized, professional quality

---

## Tier 1: 1942 (Lessons 2433-2496)

**Goal:** Build 1942 with vertical scrolling, enemy formations, and loop mechanic.

**Why this game:** Classic WWII vertical shooter. Foundation for all vertical shmups. Introduces formations and power-up systems.

**Game Requirements:**
- Vertical scrolling (auto-scroll upward)
- Player plane (limited horizontal movement)
- Enemy formations (bombers, fighters in V-shapes)
- Power-ups (weapon upgrades, extra lives)
- Loop maneuver (brief invincibility, limited uses)
- 32 stages
- Boss every 4 stages (large bombers)
- Continues

**Skills Introduced:**
- Vertical auto-scrolling
- Enemy formation patterns (V-formation, waves)
- Power-up spawning (from destroyed enemies)
- Loop mechanic (temporary invincibility)
- Stage progression (repeating backgrounds)
- WWII theme aesthetics

### Lesson Structure

**Lessons 2433-2440: Vertical Scrolling**
- L2433-2434: Auto-scrolling background (smooth pixel scroll)
- L2435-2436: Tile-based scrolling (character redraw)
- L2437-2438: Parallax layers (clouds move slower)
- L2439-2440: Scrolling optimization

**Lessons 2441-2448: Player Ship**
- L2441-2442: Player movement (horizontal only, confined)
- L2443-2444: Player shooting (auto-fire bullets)
- L2445-2446: Bullet pooling (32 bullets)
- L2447-2448: Player collision (enemy bullets, ships)

**Lessons 2449-2456: Enemy Formations**
- L2449-2450: Formation data structure (spawn patterns)
- L2451-2452: V-formation (classic wedge)
- L2453-2454: Wave formation (side-to-side)
- L2455-2456: Diving formation (break from formation, attack)

**Lessons 2457-2464: Enemy Types**
- L2457-2458: Fighter plane (fast, diving attacks)
- L2459-2460: Bomber (slow, more health)
- L2461-2462: Ground targets (boats, buildings)
- L2463-2464: Enemy shooting patterns

**Lessons 2465-2472: Power-ups**
- L2465-2466: Power-up drops (from certain enemies)
- L2467-2468: Weapon upgrade (twin shot, spread)
- L2469-2470: Extra life
- L2471-2472: Power-up collection

**Lessons 2473-2480: Loop Maneuver**
- L2473-2474: Loop activation (button press, resource)
- L2475-2476: Loop animation (plane loops)
- L2477-2478: Invincibility during loop
- L2479-2480: Limited uses (3 per life)

**Lessons 2481-2488: Bosses**
- L2481-2482: Large bomber boss (multi-segment)
- L2483-2484: Weak points (turrets)
- L2485-2486: Boss patterns (movement, shooting)
- L2487-2488: Boss defeat (explosion sequence)

**Lessons 2489-2496: Stage Progression & Polish**
- L2489-2490: 32 stages (background variety)
- L2491-2492: Difficulty curve (faster enemies, more bullets)
- L2493-2494: Lives, continues, scoring
- L2495-2496: Sound effects, music, final polish

---

## Tier 2: 1943 (Lessons 2497-2560)

**Goal:** Build 1943 with energy bar, ship upgrades, and battleship boss.

**Why this game:** Evolution of 1942. Energy system replaces lives. Ship upgrades add depth.

**Game Requirements:**
- Energy bar (replaces lives, gradual damage)
- Energy pickups (refill energy)
- Offensive power-ups (weapon upgrades)
- Defensive power-ups (auto-fire, armor)
- 16 stages
- Battleship boss (massive multi-segment)
- Shop between stages (spend points on upgrades)

**Skills Introduced:**
- Energy system (gradual damage vs one-hit death)
- Energy pickups
- Shop system (spend score for upgrades)
- Large boss (battleship, multiple sections)
- Persistent upgrades (carry between stages)

---

## Tier 3: Xevious (Lessons 2561-2624)

**Goal:** Build Xevious with air + ground targeting system.

**Why this game:** Dual-axis combat. Air targets with cannon, ground targets with bombs.

**Game Requirements:**
- Blaster (air-to-air, rapid fire)
- Zapper (air-to-ground, bombs)
- Ground targets (tanks, bases, hidden Sol towers)
- Air targets (flying enemies)
- Solvalou ship (iconic design)
- 16 areas
- Boss battles (Andor Genesis)
- Hidden bonus items (Sol towers)

**Skills Introduced:**
- Dual weapon system (air and ground simultaneous)
- Target reticle (bomb sight for ground targets)
- Hidden targets (Sol towers, invisible until close)
- Ground scrolling (terrain affects targeting)

---

## Tier 4: Twin Cobra (Lessons 2625-2688)

**Goal:** Build intense vertical shooter with heavy bullet patterns.

**Why this game:** Ramps up difficulty. Dense bullet patterns. Tests multiplexing.

**Game Requirements:**
- Dual weapons (forward shot + homing missiles)
- Weapon power-ups (5 levels each)
- Dense bullet patterns (50+ bullets on screen)
- Enemy variety (helicopters, tanks, turrets)
- 10 stages
- Boss battles (large helicopters, tanks)
- Bomb (screen-clear, limited)

**Skills Introduced:**
- Dense bullet patterns (bullet hell lite)
- Sprite multiplexing (50+ bullets + enemies)
- Homing missiles (target nearest enemy)
- Bomb system (panic button, limited uses)

---

## Tier 5: Silkworm (Lessons 2689-2752)

**Goal:** Build horizontal shooter with asymmetric co-op (helicopter + jeep).

**Why this game:** Introduces horizontal scrolling. Asymmetric co-op is unique. Ground/air split gameplay.

**Game Requirements:**
- Helicopter (air, flies freely)
- Jeep (ground, limited vertical movement)
- 2-player co-op (different capabilities)
- Ground enemies (tanks, soldiers)
- Air enemies (helicopters, jets)
- Boss battles (both ground and air components)
- 5 stages

**Skills Introduced:**
- **Horizontal scrolling** (left-to-right auto-scroll)
- Asymmetric co-op (different player abilities)
- Ground/air layer (separate collision, targets)
- Horizontal multiplexing (different challenges than vertical)

---

## Tier 6: R-Type (Lessons 2753-2816)

**Goal:** Build R-Type with Force pod, charge beam, and grotesque enemies.

**Why this game:** THE definitive horizontal shooter. Force pod changes strategy. Iconic.

**Game Requirements:**
- Force pod (attachable pod, shields, shoots)
- Charge beam (hold fire to charge, release for powerful shot)
- Detach/reattach Force (strategic positioning)
- Grotesque biomechanical enemies (H.R. Giger style)
- 8 stages
- Iconic bosses (Dobkeratops, Gomander, etc.)
- Precise hitbox (1 pixel ship core)
- Unforgiving difficulty

**Skills Introduced:**
- Force pod system (separate entity, attach/detach)
- Charge beam (hold duration = power)
- Precise hitbox (ship sprite large, actual hitbox tiny)
- Grotesque enemy design (biomechanical theme)
- Checkpoint system (restart from mid-stage)

### Key Skills: Force Pod

**Force Pod Mechanics:**
- Spawns as power-up
- Attaches to front or back of ship
- Shields ship from that direction
- Can be launched (shoots forward, boomerangs back)
- Two Force pods = double firepower
- Invulnerability when attached (on that side)

---

## Tier 7: Gradius (Lessons 2817-2880)

**Goal:** Build Gradius with power-up bar, options, and volcano stage.

**Why this game:** Power-up selection bar. Options (drones). Iconic stages.

**Game Requirements:**
- Power-up bar (collect power-ups, select upgrade)
- Speed up (4 levels)
- Missiles (ground attack)
- Double shot
- Laser
- Options (up to 4 drones, mimic your shots)
- Shield
- 7 stages (volcano, crystal, brain, etc.)
- Boss battles (Big Core)

**Skills Introduced:**
- Power-up selection bar (choose upgrade order)
- Options (drones that follow and mimic attacks)
- Multiple weapon types (selectable via power-up bar)
- Iconic stages (volcano with destructible terrain)

---

## Tier 8: Nemesis (Lessons 2881-2944)

**Goal:** Build Nemesis (Gradius sequel) with multiple weapon types.

**Why this game:** Expands Gradius formula. More weapon variety. Shield system.

**Game Requirements:**
- Multiple weapon options (laser, ripple, napalm)
- Shield system (force field absorbs hits)
- Options (up to 4)
- 6 stages
- Boss battles
- Speed control (critical for tight spaces)

**Skills Introduced:**
- Weapon variety (3+ main weapons, each different)
- Shield system (absorbs damage, depletes)
- Speed control importance (too fast = death in tight corridors)

---

## Tier 9: Katakubi (Lessons 2945-3008)

**Goal:** Build fast-paced horizontal shooter with focus on scoring.

**Why this game:** Speed-based gameplay. Scoring combos. Quick reflexes.

**Game Requirements:**
- Fast scrolling
- Score multipliers (destroy chains for combos)
- Multiple weapons
- 6 stages
- Boss battles
- High-score focus

**Skills Introduced:**
- Speed-based gameplay (fast scroll, quick reactions)
- Scoring combos (destroy enemies in quick succession)
- High-score optimization (risk vs reward)

---

## Tier 10: Delta (Lessons 3009-3072)

**Goal:** Build horizontal shooter with weapon variety and enemy diversity.

**Why this game:** Synthesis of horizontal shooters. Weapon mastery. Enemy variety.

**Game Requirements:**
- 5 weapon types (laser, spread, homing, wave, ring)
- Weapon power-ups (3 levels each)
- Enemy diversity (50+ enemy types)
- 8 stages
- Complex bosses
- Option pods

**Skills Introduced:**
- Weapon balancing (each weapon useful in different situations)
- Enemy type variety (requires different strategies)
- Everything from horizontal shooters synthesized

---

## Tier 11: Robotron 2084 (Lessons 3073-3136)

**Goal:** Build Robotron with twin-stick controls and save-the-humans gameplay.

**Why this game:** Multi-directional perfection. 100+ enemies on screen. Chaos management.

**Game Requirements:**
- Twin-stick controls (move + shoot independently)
- Save humans (rescue for bonus)
- 100+ enemies on screen simultaneously
- Enemy variety (grunts, brains, hulks, spheroids)
- Wave-based progression
- Increasing difficulty (faster, more enemies)

**Skills Introduced:**
- **Sprite multiplexing mastery** (100+ sprites)
- Twin-stick controls (8-direction move + 8-direction shoot)
- Rescue mechanics (save humans)
- Chaos management (many simultaneous threats)
- Spatial partitioning (optimize collision for 100+ objects)

### Sprite Multiplexing Deep Dive

**How to display 100+ sprites with 8 hardware sprites:**
- IRQ every scanline
- Reposition hardware sprites mid-frame
- Sort sprites by Y position
- Assign hardware sprites to different screen areas
- Flicker when >8 sprites on same scanline
- Minimize flicker with smart allocation

---

## Tier 12: Smash TV Advanced (Lessons 3137-3200)

**Goal:** Build advanced Smash TV with extreme multiplexing and chaos.

**Why this game:** Pushes multiplexing to limits. 150+ objects on screen. Prizes and power-ups everywhere.

**Game Requirements:**
- Arena rooms (clear all enemies)
- Extreme enemy counts (150+ enemies + bullets + items)
- Prizes drop everywhere (cash, keys, totems)
- Power-ups (speed, triple shot, scatter bombs)
- 4 TV shows (levels)
- Boss battles (Mr. Shrapnel, Mutoid Man)
- Announcer voice ("BIG MONEY! BIG PRIZES! I LOVE IT!")

**Skills Introduced:**
- Extreme multiplexing (150+ objects)
- Prize/item management (hundreds of collectibles)
- Arena room progression
- Everything from Phase 6 at maximum difficulty

---

## Tier 13: Berzerk (Lessons 3201-3264)

**Goal:** Build Berzerk with room-based progression and Evil Otto.

**Why this game:** Room-based shooter. Evil Otto is iconic. Voice synthesis.

**Game Requirements:**
- Room-based (clear room, exit to next)
- Robots (shoot in 8 directions)
- Evil Otto (invincible, chases you if you stay too long)
- Electrified walls (touch = death)
- Voice synthesis ("Intruder alert!", "Chicken, fight like a robot!")
- Infinite rooms (procedural or large map)

**Skills Introduced:**
- Room-based structure
- Evil Otto (unkillable threat, time pressure)
- Voice synthesis (SID-based or sampled)
- Risk/reward (stay for points vs flee from Otto)

---

## Tier 14: Uridium (Lessons 3265-3328)

**Goal:** Build Uridium with low-flying over dreadnoughts.

**Why this game:** Hybrid exploration/shooter. Large ships to destroy. Unique perspective.

**Game Requirements:**
- Fly over large dreadnought ships (scrolling both directions)
- Destroy all towers to land
- Land on ship to complete
- 15 dreadnoughts
- Fuel system
- Fast scrolling (both left and right)
- Tight corridors (precise flying)

**Skills Introduced:**
- Bidirectional scrolling (fly left or right freely)
- Large ships (multi-screen-sized)
- Landing mechanic (must land safely after destroying towers)
- Fuel system (time pressure)

---

## Tier 15: Zynaps (Lessons 3329-3392)

**Goal:** Build Zynaps with weapon pods and transforming ship.

**Why this game:** Weapon pod system. Ship transformation. Technical showcase.

**Game Requirements:**
- Weapon pods (attach to ship, different weapons)
- Ship transformation (changes with weapon loadout)
- 8 stages
- Boss battles
- Power-up system
- Smooth scrolling

**Skills Introduced:**
- Weapon pod system (modular weapons)
- Ship transformation (visual + mechanical changes)
- Pod positioning (front, back, sides)

---

## Tier 16: Armalyte (Lessons 3393-3456)

**Goal:** Build Armalyte - technical perfection and Phase 6 synthesis.

**Why this game:** Pushes C64 to limits. Smooth scrolling. Advanced graphics. Professional quality. Perfect Phase 6 finale.

**Game Requirements:**
- Silky smooth scrolling (optimized)
- Advanced weapon system
- 8 stages
- Complex bosses (multi-phase, weak points)
- Parallax backgrounds (3-4 layers)
- 100+ sprites on screen
- Raster effects (color cycling, splits)
- Professional polish (every detail perfect)

**Skills Introduced:**
- Everything from Phase 6 synthesized
- Professional optimization
- Technical perfection
- Commercial-quality output

**Final Synthesis:**
- All scrolling types mastered
- All multiplexing techniques mastered
- All bullet patterns mastered
- All boss design mastered
- Ready to build ANY shoot-em-up

---

## Phase 6 Outcome

Students have built **16 complete shoot-em-ups** and mastered:

**Sprite Multiplexing:**
- 100+ sprites with 8 hardware sprites
- IRQ-based repositioning
- Sprite sorting by Y position
- Flicker minimization
- Spatial partitioning for collision

**Scrolling:**
- Vertical auto-scrolling
- Horizontal auto-scrolling
- Bidirectional scrolling
- Parallax layers (3-4 backgrounds)
- Smooth pixel scrolling optimization

**Bullet Patterns:**
- Spread patterns
- Aimed patterns (target player)
- Spiral patterns
- Bullet hell density
- Pattern design for difficulty

**Boss Design:**
- Multi-phase bosses
- Weak points
- Complex attack patterns
- Memorization-based patterns
- Fair difficulty curves

**Power-up Systems:**
- Weapon upgrades
- Options/drones
- Shields
- Speed control
- Bomb/special attacks
- Power-up selection (Gradius bar)

**Enemy Formations:**
- V-formations
- Wave patterns
- Diving attacks
- Formation breaking
- Spawn timing

**Game Systems:**
- Lives/continues
- Energy systems
- Scoring (combos, multipliers, grazing)
- High score tables
- Attract mode/demo
- 2-player co-op
- Difficulty progression

**Optimization:**
- Collision optimization (spatial partitioning)
- Scrolling optimization
- IRQ timing perfection
- Memory management
- 50 FPS locked performance

**Ready for Phase 7:** Students transition from reflexes to systems with comprehensive RPG development.

---

**Version:** 3.0
**Date:** 2025-10-20
**Status:** Complete restructure for 1024-lesson phase
**Focus:** 16 shoot-em-ups spanning all sub-genres - THE C64 genre mastered
