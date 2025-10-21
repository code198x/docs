# Phase 9: Strategy Games (Lessons 4993-5504)

**Total:** 512 lessons across 8 tiers (64 lessons per tier)

**Phase Goal:** Master strategic thinking and AI. Learn real-time strategy, turn-based tactics, pathfinding algorithms, resource management, and complex AI decision-making.

**Prerequisites:** Phases 1-8 complete (all foundational systems, especially AI from previous phases)

**Phase Philosophy:**
- Strategy = thinking, not reflexes
- AI opponents must be intelligent and challenging
- Pathfinding essential (A*, flow fields)
- Resource management systems
- Turn-based allows perfect information decisions
- Real-time requires juggling priorities
- 64 lessons per game for depth
- Complete games with campaign modes

**Game Progression:**
- **Tier 1:** Civilization - Turn-based 4X (explore, expand, exploit, exterminate)
- **Tier 2:** Dune II - Real-time strategy, base building, resource harvesting
- **Tier 3:** X-COM - Tactical turn-based combat, base management, research
- **Tier 4:** Populous - God game, terrain manipulation, indirect control
- **Tier 5:** SimCity - City building simulation, no win condition
- **Tier 6:** Lemmings Tactical - Puzzle strategy hybrid, unit management
- **Tier 7:** Cannon Fodder - Real-time tactics, squad management, missions
- **Tier 8:** Syndicate - Tactical squad shooter, cyberpunk, research tree

**What Students Master:**
- Pathfinding algorithms (A*, Dijkstra, flow fields)
- AI decision making (state machines, goal-oriented behavior)
- Resource management (collection, spending, economy)
- Tech trees (research progression)
- Base building systems
- Unit production and management
- Fog of war
- Turn-based combat systems
- Real-time strategy mechanics
- Terrain manipulation
- Multiple unit selection
- Formation movement
- Strategic AI (build order, attack timing, defense)
- Campaign progression
- Mission objectives

---

## Phase 9 Overview

| Tier | Game | Sub-genre | Deliverable | Key Skills |
|------|------|-----------|-------------|------------|
| 1 | Civilization | Turn-based 4X | World map, cities, tech tree, AI civs | 4X mechanics, tech tree, diplomacy |
| 2 | Dune II | RTS | Base building, harvesting, combat | Real-time, resource economy, build queue |
| 3 | X-COM | Tactical TBS | Base management, tactical missions | Turn-based tactics, destructible terrain |
| 4 | Populous | God game | Terrain manipulation, followers | Indirect control, terrain editing |
| 5 | SimCity | City sim | Zone placement, simulation | No win condition, simulation loops |
| 6 | Lemmings Tactical | Puzzle-strategy | Lemmings + strategy objectives | Hybrid genre, creative solutions |
| 7 | Cannon Fodder | Real-time tactics | Squad control, mission objectives | Direct unit control, small squads |
| 8 | Syndicate | Tactical shooter | Cyberpunk squads, research, missions | Research tree, squad tactics, synthesis |

**Technical Progression:**
- Tiers 1-2: Core strategy (turn-based, then real-time)
- Tiers 3-4: Tactical combat and god games
- Tiers 5-6: Simulation and hybrid genres
- Tiers 7-8: Real-time tactics and synthesis

---

## Tier 1: Civilization (Lessons 4993-5056)

**Goal:** Build turn-based 4X strategy game with tech tree and AI opponents.

**Why this game:** THE turn-based strategy game. Tech tree. Multiple paths to victory. AI civilizations. Complex but elegant.

**Game Requirements:**
- World map (50×80 tiles, randomly generated)
- 4 civilizations (player + 3 AI)
- Cities (found, grow, produce units/buildings)
- Units (settlers, warriors, phalanx, knights, catapults, etc.)
- Tech tree (40+ technologies, prerequisite chains)
- Production (cities build units/buildings over turns)
- Resources (food, production, trade, science)
- Combat (unit strength, terrain bonuses, fortification)
- Diplomacy (war, peace, alliances, trade)
- Victory conditions (conquest, space race, score)
- AI opponents (expand, build, attack, defend)
- Fog of war (unexplored terrain)
- Save/load

**Skills Introduced:**
- 4X mechanics (explore, expand, exploit, exterminate)
- Tech tree (research progression, prerequisites)
- City management (production queue, growth)
- Unit production (build queues, maintenance costs)
- AI civilization (strategic decision-making)
- Diplomacy systems (relationships, agreements)
- Multiple victory conditions
- Turn-based strategy on large scale

### Lesson Structure

**Lessons 4993-5000: World & Map**
- L4993-4994: World generation (continents, oceans, resources)
- L4995-4996: Tile types (grassland, plains, forest, mountains, ocean)
- L4997-4998: Fog of war (explored, visible, hidden)
- L4999-5000: Map scrolling and display

**Lessons 5001-5008: Cities**
- L5001-5002: City founding (settler → city)
- L5003-5004: City growth (population, food surplus)
- L5005-5006: City production (shields per turn)
- L5007-5008: City UI (view production, population, resources)

**Lessons 5009-5016: Units**
- L5009-5010: Unit types (settler, warrior, phalanx, horseman, etc.)
- L5011-5012: Unit movement (MP, terrain costs)
- L5013-5014: Unit stacking (multiple units per tile)
- L5015-5016: Unit orders (sentry, fortify, go-to)

**Lessons 5017-5024: Combat**
- L5017-5018: Combat resolution (attacker strength vs defender)
- L5019-5020: Terrain bonuses (river, forest, city walls)
- L5021-5022: Veteran units (experience bonuses)
- L5023-5024: City conquest (capture cities)

**Lessons 5025-5032: Tech Tree**
- L5025-5026: Technology structure (40 technologies)
- L5027-5028: Research (science points → tech)
- L5029-5030: Prerequisites (Bronze Working → Iron Working)
- L5031-5032: Tech effects (unlock units, buildings, abilities)

**Lessons 5033-5040: Production**
- L5033-5034: Build queue (cities produce over turns)
- L5035-5036: Buildings (granary, barracks, library, temple, etc.)
- L5037-5038: Wonders (pyramids, colossus, great wall)
- L5039-5040: Production overflow (excess shields)

**Lessons 5041-5048: AI Civilizations**
- L5041-5042: AI decision making (what to build, where to settle)
- L5043-5044: AI exploration (send settlers, scouts)
- L5045-5046: AI military (build armies, attack weaknesses)
- L5047-5048: AI difficulty levels (bonuses, aggression)

**Lessons 5049-5056: Diplomacy & Victory**
- L5049-5050: Diplomacy (war, peace, trade agreements)
- L5051-5052: Relationships (friendly, neutral, hostile)
- L5053-5054: Victory conditions (conquest, space race, 2050 AD)
- L5055-5056: Save/load and final polish

---

## Tier 2: Dune II (Lessons 5057-5120)

**Goal:** Build real-time strategy with base building and resource harvesting.

**Why this game:** THE RTS template. Harvesting, base building, unit production, fog of war. Defined the genre.

**Game Requirements:**
- 3 houses (Atreides, Harkonnen, Ordos) - different unit strengths
- Spice harvesting (harvesters collect, return to refinery)
- Base building (construction yard → buildings)
- Unit production (barracks, factory, high-tech produce units)
- Power system (need power plants for buildings)
- Real-time combat (units auto-attack)
- Campaign (9 missions per house)
- Fog of war (explored but not currently visible)
- Limited unit selection (one at a time or small groups)
- Sandworms (destroy harvesters randomly)
- Save between missions

**Skills Introduced:**
- Real-time strategy (vs turn-based)
- Resource harvesting (harvesters, refineries)
- Build queue (real-time construction)
- Power management (enough power for buildings)
- Unit production queue
- Fog of war (RTS style)
- Campaign missions (objectives, progression)
- Real-time AI (expansion, attacks)

---

## Tier 3: X-COM (Lessons 5121-5184)

**Goal:** Build tactical turn-based combat with base management and research.

**Why this game:** Best tactical combat. Base building between missions. Research tree. Terror missions. Difficulty curve.

**Game Requirements:**
- Base management (build facilities, hire soldiers, research)
- Tactical missions (turn-based squad combat)
- Destructible terrain (blow holes in walls)
- Action points (time units for movement, shooting)
- Research tree (alien technology, new weapons)
- Manufacturing (build equipment from research)
- Geoscape (world map, UFO detection, interception)
- Multiple bases (build worldwide)
- Funding (countries give money, can withdraw)
- Soldier progression (experience, stats increase)
- Terror missions (save civilians)
- Final mission (Cydonia)

**Skills Introduced:**
- Tactical turn-based combat (action points, cover)
- Destructible terrain (blast through walls)
- Research system (unlock new tech)
- Manufacturing system (build items)
- Base building (facility placement, adjacency)
- Geoscape strategy layer
- Funding and economy
- Campaign narrative (escalating threat)

---

## Tier 4: Populous (Lessons 5185-5248)

**Goal:** Build god game with terrain manipulation and indirect control.

**Why this game:** God game. Indirect control (influence followers, don't command). Terrain manipulation. Unique genre.

**Game Requirements:**
- Terrain manipulation (raise/lower land)
- Followers (your people, they act autonomously)
- Influence vs control (nudge behavior, not command)
- Miracles (earthquake, flood, volcano, armageddon)
- Mana system (power for miracles)
- Enemy god (AI opponent with own followers)
- Settle land (followers build settlements)
- Population growth (more followers = more mana)
- Combat (followers fight enemy followers)
- 500 worlds (levels, increasing difficulty)
- Goal: Destroy enemy god's followers

**Skills Introduced:**
- God game mechanics (indirect control)
- Terrain manipulation (raise, lower, level, flatten)
- Autonomous agents (followers act on own)
- Mana/power system
- Miracle casting (big effects, high cost)
- Territory control (settle land, population density)

---

## Tier 5: SimCity (Lessons 5249-5312)

**Goal:** Build city simulation with no win condition.

**Why this game:** Pure simulation. No enemies. Goal = build thriving city. Zoning system. Budgets and taxes.

**Game Requirements:**
- Zoning (residential, commercial, industrial)
- Infrastructure (roads, power lines, power plants)
- Services (police, fire, hospitals, schools)
- Budget (income from taxes, expenses for services)
- Tax rates (affect growth and income)
- Disasters (fire, tornado, monster, earthquake)
- Population growth (Sims move in based on conditions)
- Pollution (industry creates, affects desirability)
- Traffic (roads get congested)
- City ordinances (policies affect city)
- No win condition (sandbox, high score = population)
- Time progression (game runs, city evolves)

**Skills Introduced:**
- Simulation loops (update population, traffic, pollution)
- Zoning systems (land use designation)
- Budget management (balance income and expenses)
- Service coverage (range-based effects)
- Emergent gameplay (no set objectives)
- Disasters and recovery
- Policy systems (ordinances)

---

## Tier 6: Lemmings Tactical (Lessons 5313-5376)

**Goal:** Hybrid puzzle-strategy game combining Lemmings mechanics with objectives.

**Why this game:** Creative hybrid. Apply Phase 3 Lemmings to strategy objectives. Unique challenge.

**Game Requirements:**
- Lemmings mechanics (from Phase 3)
- Strategic objectives (capture flags, destroy enemy structures)
- Multiple lemming types (workers, soldiers, engineers)
- Resource management (limited job assignments)
- Enemy lemmings (AI controlled)
- Terrain manipulation (dig to enemy base)
- Build structures (bridges to reach objectives)
- Time limits and quotas
- Campaign (20 missions, increasing complexity)
- Combine puzzle-solving with strategy

**Skills Introduced:**
- Hybrid genre design (puzzle + strategy)
- Asymmetric objectives (different ways to win)
- Creative problem solving (Lemmings-style in strategy context)
- Multi-unit types with different roles

---

## Tier 7: Cannon Fodder (Lessons 5377-5440)

**Goal:** Real-time squad tactics with mission-based gameplay.

**Why this game:** Direct unit control. Small squads (1-8 soldiers). Mission variety. Dark humor. Real-time tactics.

**Game Requirements:**
- Squad control (select individuals or groups)
- Point-and-click movement (click to move, click to shoot)
- Missions (destroy enemy base, rescue hostages, survive waves)
- Recruits (soldiers die, new recruits join)
- Vehicles (jeeps, helicopters - transport and weapons)
- Grenades and rockets (explosive weapons)
- Line of sight (can't see through walls)
- Permadeath (soldiers die permanently)
- Campaign (72 missions across war zones)
- Promotions (soldiers gain rank if they survive)

**Skills Introduced:**
- Real-time squad tactics (small unit control)
- Direct unit control (point-and-click commands)
- Permadeath progression (lose soldiers permanently)
- Mission variety (different objectives)
- Vehicles in tactics games
- Line of sight mechanics

---

## Tier 8: Syndicate (Lessons 5441-5504)

**Goal:** Cyberpunk tactical squad game with research tree. Synthesis of Phase 9.

**Why this game:** Isometric tactics. 4-agent squads. Cyberpunk setting. Research tree. Missions. Synthesis of Phase 9.

**Game Requirements:**
- Isometric view (3/4 perspective)
- 4-agent squads (control simultaneously)
- Cyberpunk setting (2096, corporations, augments)
- Augmentations (research and install in agents)
- Weapons (pistols, shotguns, flamethrowers, gauss guns)
- Missions (assassinate, persuade, capture, protect)
- Persuadetron (mind control civilians and enemies)
- Research tree (new weapons, augments, equipment)
- Territory control (complete missions to own regions)
- Real-time with pause
- Destructible environment (blow up cars, buildings)
- Crowd simulation (civilians flee from combat)

**Skills Introduced:**
- Isometric tactical combat
- Agent augmentation system
- Mind control mechanics
- Research progression
- Territory conquest (missions unlock regions)
- Real-time with pause (RTwP)
- Destructible urban environment
- Everything from Phase 9 synthesized

### Lesson Structure

**Lessons 5441-5448: Isometric Rendering**
- L5441-5442: Isometric tile projection (3/4 view)
- L5443-5444: Depth sorting (draw order for overlapping objects)
- L5445-5446: Camera scrolling (follow squad)
- L5447-5448: Sprite rendering in isometric space

**Lessons 5449-5456: Squad Control**
- L5449-5450: 4-agent squad (select, move, attack)
- L5451-5452: Formation movement (maintain relative positions)
- L5453-5454: Individual vs group commands
- L5455-5456: Agent stats (health, energy, augments)

**Lessons 5457-5464: Combat & Weapons**
- L5457-5458: Real-time combat (auto-attack in range)
- L5459-5460: Weapon types (pistol, shotgun, uzi, laser, gauss, flamethrower)
- L5461-5462: Line of sight (can't shoot through walls)
- L5463-5464: Destructible objects (cars explode, walls crumble)

**Lessons 5465-5472: Persuadetron**
- L5465-5466: Mind control mechanic (persuade civilians, enemies)
- L5467-5468: Persuaded followers (join your squad)
- L5469-5470: Energy cost (persuadetron drains energy)
- L5471-5472: Uses (human shields, army building)

**Lessons 5473-5480: Augmentations**
- L5473-5474: Augmentation types (legs, chest, arms, eyes, brain, heart)
- L5475-5476: Effects (speed, health, accuracy, perception, IQ, stamina)
- L5477-5478: Installation (equip agents between missions)
- L5479-5480: Leveling (better augments from research)

**Lessons 5481-5488: Research Tree**
- L5481-5482: Research system (invest money, unlock tech)
- L5483-5484: Weapon research (better guns)
- L5485-5486: Augmentation research (better augments)
- L5487-5488: Equipment research (mods, shields)

**Lessons 5489-5496: Missions**
- L5489-5490: Mission types (assassinate, persuade, capture, protect)
- L5491-5492: Mission objectives (briefing, success conditions)
- L5493-5494: Territory (complete missions to control regions)
- L5495-5496: Difficulty progression (harder regions)

**Lessons 5497-5504: Polish & Completion**
- L5497-5498: Crowd simulation (civilians react to violence)
- L5499-5500: Police response (cops attack if detected)
- L5501-5502: Save between missions
- L5503-5504: Final polish and balance

---

## Phase 9 Outcome

Students have built **8 complete strategy games** and mastered:

**Pathfinding & Movement:**
- A* pathfinding (optimal routes)
- Flow fields (multiple units to destination)
- Movement costs (terrain types)
- Formation movement (maintain relative positions)
- Go-to orders (automated pathfinding)

**AI Systems:**
- Strategic AI (build order, expansion, attack timing)
- Tactical AI (unit positioning, target selection)
- Goal-oriented behavior (satisfy needs, pursue objectives)
- Difficulty levels (bonuses, aggression, intelligence)
- Autonomous agents (Populous followers, Lemmings)

**Resource Management:**
- Resource collection (spice, food, production)
- Resource spending (building, units, research)
- Economy balancing (income vs expenses)
- Resource types (renewable vs finite)

**Base Building:**
- Construction systems (build queues, placement)
- Facility types (production, research, defense)
- Power management (generators, consumption)
- Adjacency effects (X-COM base layout)

**Tech/Research Trees:**
- Research progression (prerequisites, unlocks)
- Tech effects (new units, buildings, abilities)
- Research investment (time, resources)
- Manufacturing (build unlocked items)

**Combat Systems:**
- Turn-based combat (action points, initiative)
- Real-time combat (auto-attack, formations)
- Tactical combat (cover, line of sight)
- Unit types and counters (rock-paper-scissors)
- Terrain effects (bonuses, obstacles)

**Strategic Layer:**
- World maps (exploration, territory control)
- Fog of war (explored, visible, hidden)
- Diplomacy (relationships, agreements)
- Campaign progression (missions, narrative)
- Multiple victory conditions

**Simulation:**
- Emergent behavior (SimCity population, traffic)
- Feedback loops (growth, decline, disasters)
- Policy systems (ordinances, decisions affect outcomes)
- No-win-condition gameplay (sandbox)

**Specialized Mechanics:**
- Terrain manipulation (Populous raise/lower)
- Indirect control (god games)
- Mind control (Persuadetron)
- Augmentation systems (agent upgrades)
- Permadeath (Cannon Fodder soldiers)
- Destructible environments

**Ready for Phase 10:** Students transition from strategic thinking to high-speed vehicle control with racing and driving games.

---

**Version:** 3.0
**Date:** 2025-10-21
**Status:** Complete restructure for 512-lesson phase
**Focus:** 8 strategy games from Civilization to Syndicate - strategic thinking mastery
