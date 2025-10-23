# Phase 10: Racing & Driving (Lessons 5505-5888)

**Total:** 384 lessons across 8 tiers (48 lessons per tier)

**Phase Goal:** Master pseudo-3D racing techniques and vehicle physics. Learn scaling sprites, track rendering, opponent AI, and high-speed gameplay.

**Prerequisites:** Phases 1-9 complete (especially physics from Phase 4, scrolling from Phase 6)

**Phase Philosophy:**
- Speed = primary feeling
- Pseudo-3D techniques (no true 3D, but looks 3D)
- Physics simulation (acceleration, friction, collision)
- Track design (curves, elevation, hazards)
- 48 lessons sufficient for each style
- Complete racing games

**Game Progression:**
- **Tier 1:** Out Run - Sprite scaling, branching tracks, arcaderacer
- **Tier 2:** Pole Position - Track rendering, lap racing, rival cars
- **Tier 3:** Lotus Esprit Turbo Challenge - Realistic handling, weather
- **Tier 4:** Super Sprint - Top-down, multiplayer, track variety
- **Tier 5:** Stunt Car Racer - 3D tracks, jumps, damage system
- **Tier 6:** Buggy Boy - Off-road, obstacles, timer gates
- **Tier 7:** Pitstop II - Pit stops, damage, tire wear
- **Tier 8:** Formula One Grand Prix - Realistic F1, qualifying, synthesis

**What Students Master:**
- Pseudo-3D rendering (sprite scaling, road)
- Track data structures (segments, curves, elevation)
- Vehicle physics (acceleration, braking, turning, drifting)
- Opponent AI (racing line, overtaking, rubber-banding)
- Collision detection (cars, barriers, obstacles)
- Lap timing and positions
- Weather effects (rain affects handling)
- Damage systems (car damage affects performance)
- Pit stops (repair, tires, fuel)
- Track variety (city, desert, snow, off-road)
- Multiplayer racing

---

## Phase 10 Overview

| Tier | Game | Style | Deliverable | Key Skills |
|------|------|-------|-------------|------------|
| 1 | Out Run | Sprite scaler | Branching tracks, scenic, music | Sprite scaling, branching paths |
| 2 | Pole Position | Track racer | Laps, position, rivals | Lap racing, track rendering |
| 3 | Lotus | Sim racer | Realistic handling, weather | Physics simulation, weather |
| 4 | Super Sprint | Top-down | 4-player, track variety | Top-down view, multiplayer |
| 5 | Stunt Car Racer | 3D racer | Jumps, elevated tracks, damage | Pseudo-3D elevation, jumps |
| 6 | Buggy Boy | Off-road | Obstacles, gates, timer | Off-road, obstacle courses |
| 7 | Pitstop II | Pit stop racer | Damage, tire wear, repairs | Pit stop management, wear |
| 8 | Formula One GP | F1 sim | Qualifying, race, realistic | Realism, qualifying, synthesis |

**Technical Progression:**
- Tiers 1-2: Sprite scaling and track basics
- Tiers 3-4: Physics and multiplayer
- Tiers 5-6: Pseudo-3D and obstacles
- Tiers 7-8: Simulation depth and synthesis

---

## Tier 1: Out Run (Lessons 5505-5552)

**Goal:** Build Out Run with sprite scaling and branching tracks.

**Why this game:** THE arcade racer. Sprite scaling. Branching tracks. Music selection. Ferrari. Sunset. Iconic.

**Game Requirements:**
- Sprite scaling (road, cars, scenery appear to approach)
- Ferrari Testarossa (convertible, girlfriend passenger)
- Branching tracks (5 routes, choose at forks)
- 15 stages total (multiple paths)
- Rival cars (overtake, avoid)
- Scenery (palm trees, signs, buildings scale)
- Music selection (choose radio station at start)
- Timer (reach checkpoint before time runs out)
- Crash on collision (spin out, lose time)
- Multiple endings (beach, Stonehenge, etc.)

**Skills Introduced:**
- Sprite scaling (simulate depth by scaling)
- Road rendering (curved road using scaling)
- Branching paths (choose routes at forks)
- Timer pressure (checkpoint racing)
- Scenery scaling (parallax with scaling)
- Music selection (player choice)

### Lesson Structure

**Lessons 5505-5510: Sprite Scaling**
- L5505-5506: Scaling algorithm (multiply sprite by distance factor)
- L5507-5508: Road rendering (draw road segments at different scales)
- L5509-5510: Horizon and perspective

**Lessons 5511-5516: Track System**
- L5511-5512: Track segments (straight, curve left, curve right, hill)
- L5513-5514: Track data structure (branching paths)
- L5515-5516: Camera position on track

**Lessons 5517-5522: Vehicle Physics**
- L5517-5518: Acceleration and speed
- L5519-5520: Steering (left/right movement on road)
- L5521-5522: Braking and friction

**Lessons 5523-5528: Rival Cars**
- L5523-5524: Opponent cars (spawn, movement)
- L5525-5526: Overtaking and blocking
- L5527-5528: Collision (crash, spin out)

**Lessons 5529-5534: Scenery**
- L5529-5530: Roadside objects (trees, signs, buildings)
- L5531-5532: Scaling scenery by distance
- L5533-5534: Parallax background (mountains, sky)

**Lessons 5535-5540: Branching & Timing**
- L5535-5536: Track forks (choose left or right)
- L5537-5538: Checkpoint timer (reach next checkpoint)
- L5539-5540: Time extension on checkpoint

**Lessons 5541-5546: Music & Endings**
- L5541-5542: Music selection (choose at start)
- L5543-5544: Multiple endings (based on route)
- L5545-5546: Girlfriend comments (encouragement, complaints)

**Lessons 5547-5552: Polish & Completion**
- L5547-5548: Crash animation (spin, recover)
- L5549-5550: Traffic variety (different car types)
- L5551-5552: Final polish

---

## Tier 2: Pole Position (Lessons 5553-5600)

**Goal:** Build lap-based racing with qualifying and positions.

**Why this game:** First true racing game. Qualifying lap. Track position. Rivals. Laps. Formula One style.

**Game Requirements:**
- Qualifying lap (set best time, determines starting position)
- Race (4 laps, 8 rival cars)
- Track (curves, chicanes, straightaways)
- Position tracking (1st - 9th place)
- Lap timing (best lap, total time)
- Trackside billboards (Atari, etc.)
- Collision (crash = explosion, respawn)
- Finish positions (1st-3rd = extended play)
- Top-down minimap (optional)

**Skills Introduced:**
- Qualifying system (time trial for position)
- Lap racing (complete laps, track position)
- Position tracking (where am I in race?)
- Chicanes and track variety

---

## Tier 3: Lotus Esprit Turbo Challenge (Lessons 5601-5648)

**Goal:** Build realistic racing sim with weather effects.

**Why this game:** Realistic handling. Weather (rain, snow). Lotus cars. Split-screen multiplayer. Beautiful courses.

**Game Requirements:**
- 8 tracks (courses across seasons/weather)
- Weather effects (rain = slippery, snow = very slippery)
- Realistic handling (momentum, tire grip)
- Lotus Esprit Turbo (specific car)
- Split-screen 2-player (race against friend)
- Rival AI (challenging, realistic racing line)
- Lap times and championship points
- Turbo boost (limited use, speed burst)

**Skills Introduced:**
- Realistic physics (tire grip, momentum-based)
- Weather simulation (affects handling)
- Split-screen rendering (2-player simultaneously)
- Turbo boost mechanic
- Championship progression

---

## Tier 4: Super Sprint (Lessons 5649-5696)

**Goal:** Build top-down racing with 4-player multiplayer.

**Why this game:** Top-down view. 4-player simultaneous. Track variety. Helicopter drops wrenches for upgrades.

**Game Requirements:**
- Top-down view (see entire track)
- 8 tracks (different layouts)
- 4-player simultaneous (split input, not split-screen)
- Upgrades (wrenches improve speed, traction, acceleration)
- Laps (3 laps per race)
- Obstacles (oil slicks, tornadoes)
- Points system (1st = 9 points, 2nd = 6, etc.)
- Tournament mode (8 tracks, total points)

**Skills Introduced:**
- Top-down racing view
- 4-player simultaneous (vs split-screen)
- Vehicle upgrades (persistent across races)
- Obstacles on track
- Points-based championship

---

## Tier 5: Stunt Car Racer (Lessons 5697-5744)

**Goal:** Build pseudo-3D racing with elevated tracks and jumps.

**Why this game:** 3D tracks (elevated, drops, jumps). Damage system. First-person perspective. Unique.

**Game Requirements:**
- First-person 3D view (driver's seat)
- Elevated tracks (rollercoaster-style, suspended in air)
- Jumps (land cleanly or take damage)
- Damage system (hit too hard = damaged chassis, slower)
- Opponent (1v1 races)
- Track variety (loops, jumps, drops, curves)
- League mode (progress through divisions)
- Repair between races (costs money from winnings)

**Skills Introduced:**
- First-person pseudo-3D racing
- Elevated track rendering (hills, jumps, drops)
- Damage system (affects performance)
- Jump physics (airtime, landing impact)

---

## Tier 6: Buggy Boy (Lessons 5745-5792)

**Goal:** Build off-road racing with obstacles and gates.

**Why this game:** Off-road. Obstacle course. Timer gates. Flags to collect. Unique gameplay.

**Game Requirements:**
- Off-road racing (dirt, rocks, terrain)
- Obstacles (rocks, logs, fences - avoid or jump)
- Timer gates (pass through to extend time)
- Flags (collect for points, 5 colors)
- Jumps (ramps, hills)
- 5 courses (different terrains)
- Score based on time remaining and flags collected
- Buggy vehicle (bouncy suspension)

**Skills Introduced:**
- Off-road terrain (different surfaces)
- Obstacle avoidance (steering challenge)
- Timer gates (checkpoint extensions)
- Collectibles (flags, bonus points)
- Jump mechanics in racing

---

## Tier 7: Pitstop II (Lessons 5793-5840)

**Goal:** Build racing with pit stop strategy and damage.

**Why this game:** Pit stops. Tire wear. Damage repair. Fuel management. Strategy racing.

**Game Requirements:**
- Race (multiple laps, long race)
- Tire wear (tires degrade, lose grip)
- Fuel consumption (run out = retire)
- Damage (collisions damage car, reduce speed)
- Pit stops (repair damage, change tires, refuel)
- Pit crew mini-game (faster pit = less time lost)
- 2-player split-screen
- Strategy (when to pit? Risk vs reward)

**Skills Introduced:**
- Pit stop mechanics (strategic timing)
- Tire wear simulation
- Fuel management
- Damage affecting performance
- Pit crew mini-game (player skill affects pit time)

---

## Tier 8: Formula One Grand Prix (Lessons 5841-5888)

**Goal:** Build realistic F1 sim with qualifying, race, and realism. Synthesis of Phase 10.

**Why this game:** Realistic F1. Qualifying. Race. Pit strategy. Weather. Real tracks. Synthesis.

**Game Requirements:**
- Qualifying session (set grid position)
- Race (adjustable laps, 5-80)
- Real F1 tracks (Monaco, Silverstone, Spa, etc.)
- Realistic physics (F1 handling, downforce)
- Weather (wet vs dry, affects tires and grip)
- Pit strategy (tire choice, fuel, damage)
- Damage (chassis, engine, gearbox)
- Rival drivers (realistic AI, fighting for position)
- Championship mode (multiple races, points)
- Cockpit view (realistic F1 perspective)

**Skills Introduced:**
- F1 simulation depth
- Qualifying vs race structure
- Real-world track layouts
- Tire compounds (soft, medium, hard, wet)
- Championship points system
- Everything from Phase 10 synthesized

### Lesson Structure

**Lessons 5841-5846: Qualifying**
- L5841-5842: Qualifying session (1 lap time trial)
- L5843-5844: Grid positions (1st to 26th based on time)
- L5845-5846: Practice vs qualifying

**Lessons 5847-5852: Race Weekend**
- L5847-5848: Race structure (formation lap, start, laps, finish)
- L5849-5850: Starting grid (positions based on qualifying)
- L5851-5852: Formation lap and start

**Lessons 5853-5858: Realistic Physics**
- L5853-5854: F1 handling (high speed, downforce, grip)
- L5855-5856: Braking zones (late braking, lock-ups)
- L5857-5858: Racing line (optimal path through corners)

**Lessons 5859-5864: Weather & Tires**
- L5859-5860: Weather (dry, wet, changing conditions)
- L5861-5862: Tire compounds (soft, medium, hard, intermediates, wets)
- L5863-5864: Tire wear and grip loss

**Lessons 5865-5870: Pit Strategy**
- L5865-5866: Pit stops (tire changes, fuel, repairs)
- L5867-5868: Strategy (one-stop, two-stop, aggressive vs conservative)
- L5869-5870: Pit lane rules (speed limit, pit entry/exit)

**Lessons 5871-5876: Rival Drivers**
- L5871-5872: AI drivers (realistic racing behavior)
- L5873-5874: Overtaking and defending
- L5875-5876: Blue flags (lapped cars must yield)

**Lessons 5877-5882: Championship**
- L5877-5878: Points system (25-18-15-12-10-8-6-4-2-1 for top 10)
- L5879-5880: Championship standings (after each race)
- L5881-5882: Season progression (16 races)

**Lessons 5883-5888: Polish & Completion**
- L5883-5884: Cockpit view (realistic F1 perspective)
- L5885-5886: HUDs (telemetry, positions, lap times)
- L5887-5888: Final polish and balance

---

## Phase 10 Outcome

Students have built **8 complete racing games** and mastered:

**Pseudo-3D Techniques:**
- Sprite scaling (simulate depth)
- Road rendering (segments, curves, hills)
- Horizon and perspective
- Elevated tracks (Stunt Car Racer)
- First-person vs third-person views

**Vehicle Physics:**
- Acceleration and top speed
- Braking and friction
- Steering (arcade vs realistic)
- Drifting and grip
- Momentum-based handling (Lotus)
- Tire physics (grip, wear, compounds)
- Fuel consumption
- Damage affects performance

**Track Systems:**
- Track data structures (segments, curves, elevation)
- Branching paths (Out Run)
- Lap racing (Pole Position)
- Top-down tracks (Super Sprint)
- Off-road terrain (Buggy Boy)
- Real-world circuits (F1)

**Opponent AI:**
- Racing line (optimal path)
- Overtaking behavior
- Blocking and defending
- Rubber-banding (keep races close)
- Realistic AI (F1 rivals)

**Gameplay Systems:**
- Lap timing and positions
- Qualifying vs racing
- Checkpoints and timer gates
- Pit stops (strategy, crew mini-game)
- Weather effects (rain, snow affect handling)
- Damage systems (visual and performance)
- Tire wear and compound choice
- Championship points and progression

**Multiplayer:**
- Split-screen 2-player (Lotus, Pitstop II)
- 4-player simultaneous (Super Sprint)

**Game Feel:**
- Speed sensation (scaling, motion blur effects)
- Collision and crashes (spin-outs, explosions)
- Turbo boosts
- Music and sound effects (engine, tires, collisions)

**Ready for Phase 11:** Students transition from high-speed racing to precision combat with fighting games.

---

**Version:** 3.0
**Date:** 2025-10-21
**Status:** Complete restructure for 384-lesson phase
**Focus:** 8 racing games from Out Run to Formula One - speed and physics mastery
