# Phase 4: Platformers Deep Dive (Lessons 1537-2048)

**Total:** 512 lessons across 8 tiers (64 lessons per tier)

**Phase Goal:** Master all platformer sub-genres. Learn jump physics variations, advanced tile collision, scrolling optimization, and exploration-based design.

**Prerequisites:** Phase 2 complete (Donkey Kong, Mega Man, Castlevania), Phase 3 complete (grid systems)

**Phase Philosophy:**
- Platformers = physics + level design + exploration
- Each sub-genre requires different physics
- 64 lessons allows deep implementation of each style
- From precision to momentum to exploration
- Complete games with multiple worlds/stages

**Game Progression:**
- **Tier 1:** Super Mario Bros - Precision platforming, power-ups, secrets
- **Tier 2:** Metroid - Exploration, gated progression, abilities
- **Tier 3:** Sonic - Momentum physics, speed, loops
- **Tier 4:** Kirby - Copy abilities, floating, transformations
- **Tier 5:** Ghouls 'n Ghosts - Armor system, difficulty, gothic
- **Tier 6:** Rick Dangerous - Traps, puzzle-platforming, inventory
- **Tier 7:** Rainbow Islands - Rainbow mechanics, vertical scrolling
- **Tier 8:** New Zealand Story - Flight, vehicle transformation, mazes

**What Students Master:**
- Jump physics variations (floaty, tight, momentum, variable)
- Advanced tile collision (slopes, one-way platforms, moving platforms)
- Scrolling optimization (4-way smooth, parallax)
- Power-up architecture (temporary, permanent, stackable)
- World maps and overworld navigation
- Secret areas and hidden collectibles
- Checkpoint and save systems
- Ability-gated progression (Metroidvania)
- Level design principles (flow, challenge, reward)

---

## Phase 4 Overview

| Tier | Game | Deliverable | Key Skills |
|------|------|-------------|------------|
| 1 | Super Mario Bros | 8 worlds, 32 levels | Tight jump, power-ups, pipes, secrets |
| 2 | Metroid | Exploration platformer | Gated progression, item abilities, mapping |
| 3 | Sonic | Speed platformer | Momentum physics, loops, rings, special stages |
| 4 | Kirby | Copy ability platformer | Enemy absorption, floating, transformations |
| 5 | Ghouls 'n Ghosts | Gothic platformer | Armor system, weapon variety, high difficulty |
| 6 | Rick Dangerous | Puzzle platformer | Traps, inventory items, precise timing |
| 7 | Rainbow Islands | Vertical platformer | Rainbow creation, enemy bouncing, ascending |
| 8 | New Zealand Story | Flight platformer | Balloon mechanics, vehicle changes, mazes |

**Technical Progression:**
- Tiers 1-2: Classic precision and exploration
- Tiers 3-4: Physics variations (momentum, floating)
- Tiers 5-6: Difficulty and puzzle integration
- Tiers 7-8: Unique mechanics and synthesis

---

## Tier 1: Super Mario Bros (Lessons 1537-1600)

**Goal:** Build Super Mario Bros with precise jump physics, power-ups, and world structure.

**Why this game:** THE definitive platformer. Perfect jump physics, power-up progression, level design excellence.

**Game Requirements:**
- Precise jump physics (variable height based on button hold)
- 8 worlds × 4 levels = 32 levels
- Power-ups: Mushroom (big Mario), Fire Flower, Star (invincibility)
- Enemies: Goombas, Koopas, Piranha Plants, Lakitu, Hammer Bros
- Coins and 1-up mushrooms
- Pipes (some lead to bonus rooms)
- Hidden blocks (coins, power-ups)
- Flagpole ending
- Boss battles (Bowser or Hammer Bros)
- Lives system
- Warp zones

**Skills Introduced:**
- Variable jump height (button hold duration)
- Power-up state management (small → big → fire)
- Downgrade on hit (fire → big → small → death)
- Pipe transitions (enter/exit)
- Hidden blocks (bump from below)
- Enemy stomping (vs projectile defeat)
- Scrolling (screen follows player, no backtracking)
- World map structure

### Lesson Structure (Condensed)

**Lessons 1537-1544: Jump Physics**
- Variable height jump (hold duration affects apex)
- Gravity and acceleration
- Landing detection
- Jump buffer (press before landing)

**Lessons 1545-1552: Power-ups**
- Power-up state machine (small/big/fire)
- Mushroom movement AI (walks off platforms)
- Fire flower shooting
- Star invincibility timer

**Lessons 1553-1560: Enemies**
- Goomba (simple walker)
- Koopa (stomp → shell, shell sliding)
- Piranha Plant (timed emergence from pipes)
- Enemy stomping vs projectile defeat

**Lessons 1561-1568: Blocks & Coins**
- Tile types (brick, question, hidden)
- Bumping blocks (item spawn)
- Coin collection
- Brick breaking (big Mario only)

**Lessons 1569-1576: Pipes**
- Pipe detection (down key)
- Transition to bonus room
- Exit pipe
- Piranha Plant pipes (cannot enter)

**Lessons 1577-1584: Scrolling & Camera**
- Screen follows player (right only, no backtracking)
- Smooth scrolling
- Screen boundaries
- Death pits (fall off bottom)

**Lessons 1585-1592: Level Structure**
- Level data format
- 32 levels (8 worlds × 4)
- Flagpole ending
- Castle entry (world complete)

**Lessons 1593-1600: Polish**
- Lives system
- World map
- Warp zones (skip worlds)
- Timer countdown
- Final polish

---

## Tier 2: Metroid (Lessons 1601-1664)

**Goal:** Build Metroidvania with exploration, gated progression, and item abilities.

**Why this game:** Defines exploration-platforming. Abilities unlock new areas. Interconnected world.

**Game Requirements:**
- Large interconnected world (100+ rooms)
- Item-gated progression (bombs open passages, high jump reaches ledges)
- Items: Morph Ball, Bombs, Missiles, Ice Beam, Varia Suit, High Jump, Screw Attack
- Save stations
- Map system (rooms discovered)
- Backtracking (return to previous areas with new abilities)
- Boss battles (Kraid, Ridley, Mother Brain)
- Energy/missile tanks hidden throughout
- Percentage completion tracking

**Skills Introduced:**
- Interconnected world design (room-to-room connections)
- Ability-gated progression (cannot access area without item)
- Save stations (persist game state)
- Map system (track explored rooms)
- Item location tracking
- Backtracking encouragement
- Sequence breaking potential

### Key Skills Per Section

**Exploration Architecture:**
- Room-based world (100+ rooms, 10×10 grid)
- Room transitions (doors, elevators)
- Map data structure (visited flags, item flags)

**Ability Gating:**
- Bombs: Destroy certain blocks
- Morph Ball: Access small passages
- High Jump Boots: Reach high ledges
- Ice Beam: Freeze enemies as platforms
- Varia Suit: Withstand heat areas

**Save System:**
- Save stations (write full state to disk)
- Resume from save
- Energy/missile refill at stations

---

## Tier 3: Sonic (Lessons 1665-1728)

**Goal:** Build Sonic with momentum-based physics, speed, and loops.

**Why this game:** Completely different physics. Speed is the reward. Momentum matters.

**Game Requirements:**
- Momentum physics (velocity carries between actions)
- Speed-based gameplay (fast when momentum high)
- Loops and curves (special collision)
- Rings (health and currency)
- Shields (fire, lightning, water)
- Spring pads, speed boosters
- Special stages (bonus rings/emeralds)
- 3 acts per zone, 6 zones
- Spin dash
- Boss every 3rd act

**Skills Introduced:**
- Momentum physics (velocity accumulates)
- Speed-based animation (faster = different sprites)
- Loop collision (stay on surface regardless of orientation)
- Ring collection (lose all on hit, can recollect)
- Slope acceleration/deceleration
- Underwater physics (slower, air meter)
- Spin dash (rev up for speed burst)

---

## Tier 4: Kirby (Lessons 1729-1792)

**Goal:** Build Kirby with copy abilities and floating mechanics.

**Why this game:** Unique mechanic (copy enemy abilities), floating changes platforming.

**Game Requirements:**
- Inhale enemies
- Copy ability from swallowed enemy
- 10+ copy abilities (sword, beam, fire, ice, hammer, etc.)
- Float (infinite flight, slow descent)
- Puff out air (attack while floating)
- 6 worlds, 5 levels each
- Boss rush mode
- Helper system (spit out copy as ally)

**Skills Introduced:**
- Inhale mechanic (suck enemies)
- Copy ability system (transform based on enemy type)
- Floating (hold jump = float)
- Ability-specific attacks and movement
- Helper AI (ally mimics your copy ability)

---

## Tier 5: Ghouls 'n Ghosts (Lessons 1793-1856)

**Goal:** Build challenging gothic platformer with armor and weapons.

**Why this game:** Difficulty, weapon variety, two-loop structure.

**Game Requirements:**
- Armor system (hit once = armor off, hit again = death)
- 5 weapons (lance, knife, axe, torch, shield)
- Each weapon has powered-up version
- Must complete game twice (loop 1, then loop 2 with special weapon)
- 6 stages
- Jumping while shooting (limited arc control)
- Chest drops (weapons, armor, score)
- Boss battles

**Skills Introduced:**
- Armor state (armored → boxers → dead)
- Weapon variety (different arcs, speeds)
- Two-loop structure (beat game, then harder mode required)
- Jump arc control (limited air control)
- High difficulty design

---

## Tier 6: Rick Dangerous (Lessons 1857-1920)

**Goal:** Build puzzle-platformer with traps and inventory.

**Why this game:** Traps everywhere. Memorization. Inventory items solve puzzles.

**Game Requirements:**
- 4 levels (jungle, pyramid, castle, UFO)
- Traps (spikes, boulders, arrows, falling blocks)
- Inventory: Bullets (limited ammo), Bombs, Sticks
- Use items to solve puzzles (bomb opens wall, stick wedges trap)
- Memorization-based gameplay (die, learn, retry)
- Stealth elements (guards with sight lines)

**Skills Introduced:**
- Trap systems (triggered vs timed)
- Inventory puzzle solving (right tool for right obstacle)
- Memorization gameplay loop
- Limited resources (ammo, bombs)
- One-hit death (unforgiving)

---

## Tier 7: Rainbow Islands (Lessons 1921-1984)

**Goal:** Build vertical platformer with rainbow mechanics.

**Why this game:** Unique mechanic (create your own platforms). Vertical scrolling.

**Game Requirements:**
- Create rainbows (walk on them as platforms)
- Rainbows kill enemies when they collapse
- Vertical scrolling (climb to top)
- Rising water (forces upward progress)
- Power-ups (speed shoes, extended rainbows, double rainbows)
- Boss every 10 levels
- 100 levels total
- Secret items (collect diamonds for true ending)

**Skills Introduced:**
- Player-created platforms (rainbow generation)
- Vertical scrolling (upward progression)
- Rising water hazard (time pressure without timer)
- Rainbow as attack (collapse on enemies)
- Long level progression (100 levels)

---

## Tier 8: New Zealand Story (Lessons 1985-2048)

**Goal:** Build flight-based platformer with vehicle transformations.

**Why this game:** Flight mechanics, vehicle variety, maze-like levels. Synthesis of Phase 4.

**Game Requirements:**
- Kiwi bird protagonist (balloon allows limited flight)
- Pop balloon = lose flight, get new balloon
- Vehicles (laser gun, bow, bomb)
- Maze-like levels (multiple paths, exploration)
- Save friends (bonus points)
- 5 worlds, 4 rounds each
- Boss battles
- Continues

**Skills Introduced:**
- Limited flight mechanics (balloon can pop)
- Vehicle transformation (different attacks/movement)
- Maze navigation (non-linear levels)
- Multiple objectives (reach goal, save friends)
- Everything from Phase 4 synthesized

---

## Phase 4 Outcome

Students have built **8 complete platformers** and mastered:

**Physics Systems:**
- Precise jump (Mario)
- Variable height jump
- Momentum-based (Sonic)
- Floating (Kirby)
- Flight (New Zealand Story)
- Gravity variations

**Tile Collision:**
- Standard platforms
- Slopes and curves
- One-way platforms
- Moving platforms
- Loop collision (Sonic)

**Level Design:**
- Linear progression (Mario)
- Exploration/Metroidvania (Metroid)
- Speed-based (Sonic)
- Vertical scrolling (Rainbow Islands)
- Maze navigation (New Zealand Story)

**Progression Systems:**
- Power-ups (Mario, Sonic)
- Ability gating (Metroid)
- Copy abilities (Kirby)
- Weapon variety (Ghouls 'n Ghosts)
- Inventory puzzles (Rick Dangerous)

**Game Systems:**
- World maps
- Save stations
- Secret areas
- Collectibles
- Boss battles
- Multiple endings
- Difficulty curves

**Ready for Phase 5:** Students transition from solo platforming to group combat with beat-em-ups.

---

**Version:** 3.0
**Date:** 2025-10-20
**Status:** Complete restructure for 512-lesson phase
**Focus:** 8 platformer sub-genres from Mario to New Zealand Story
