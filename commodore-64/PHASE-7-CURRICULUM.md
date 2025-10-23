# Phase 7: RPG Systems (Lessons 3457-4480)

**Total:** 1024 lessons across 8 tiers (128 lessons per tier)

**Phase Goal:** Master RPG development - the most complex single-player genre. Build 8 complete RPGs spanning all sub-genres. Learn stats, inventory, save systems, dialogue, quests, and multi-disk management.

**Prerequisites:** Phases 1-6 complete (all foundational systems, especially grid systems from Phase 3, exploration from Phase 4)

**Phase Philosophy:**
- RPGs = most complex systems
- 128 lessons per game allows proper depth
- Stats, inventory, combat, progression, story
- Multi-disk management essential
- Each sub-genre requires different approach
- Save systems critical
- 10+ hours gameplay per game

**Game Progression:**
- **Tier 1:** Ultima IV - Western RPG, overworld exploration
- **Tier 2:** Zelda - Action RPG, real-time combat
- **Tier 3:** Bard's Tale - First-person dungeon crawler
- **Tier 4:** Final Fantasy - JRPG, turn-based, jobs
- **Tier 5:** Wasteland - Post-apocalyptic, choices, consequences
- **Tier 6:** Rogue - Roguelike, procedural, permadeath
- **Tier 7:** Diablo-style - Loot-focused action RPG
- **Tier 8:** Betrayal at Krondor - Tactical RPG, story

**What Students Master:**
- Stats systems (attributes, derived stats, calculations)
- Inventory management (grids, weight, stacking)
- Equipment systems (slots, bonuses, sets)
- Magic/abilities (MP, spell lists, targeting)
- Turn-based combat (initiative, targeting, animations)
- Real-time combat (action RPG)
- Save/load systems (serialize full game state)
- Multi-disk management (disk swapping, chunked loading)
- Dialogue systems (text display, choices, branching)
- Quest tracking (flags, completion, rewards)
- Party management (4-character parties, formation)
- Leveling systems (XP, curves, stat increases)
- Procedural generation (dungeons, loot)
- World persistence (state between saves)
- NPC AI and schedules
- Economy (shops, prices, supply/demand)

---

## Phase 7 Overview

| Tier | Game | Sub-genre | Deliverable | Key Skills |
|------|------|-----------|-------------|------------|
| 1 | Ultima IV | Western RPG | Virtue system, open world, party | Overworld, towns, dungeons, morality |
| 2 | Zelda | Action RPG | Real-time combat, items, dungeons | Items unlock areas, heart pieces, bosses |
| 3 | Bard's Tale | Dungeon Crawler | First-person, party, spells | Grid movement, spell casting, party |
| 4 | Final Fantasy | JRPG | Turn-based, jobs, world map, airship | Job system, ATB, story, world travel |
| 5 | Wasteland | Post-Apoc RPG | Skills, choices, consequences, branching | Skill checks, dialogue choices, endings |
| 6 | Rogue | Roguelike | Procedural, permadeath, ASCII/tiles | Random dungeons, permadeath, items |
| 7 | Diablo-style | Loot ARPG | Real-time, randomized loot, grinding | Loot generation, fast combat, grind loop |
| 8 | Betrayal at Krondor | Tactical RPG | Turn tactics, story, riddles, exploration | Tactical combat, riddles, deep story |

**Technical Progression:**
- Tiers 1-2: Exploration RPGs (overworld, real-time)
- Tiers 3-4: Party management RPGs (turn-based, jobs)
- Tiers 5-6: Choice-driven and procedural RPGs
- Tiers 7-8: Specialized systems (loot, tactics)

---

## Tier 1: Ultima IV (Lessons 3457-3584)

**Goal:** Build Ultima IV with virtue system, open world, and party management.

**Why this game:** THE definitive Western RPG. Morality system. Open-world exploration. Party of 8.

**Game Requirements:**
- 8 Virtues (Honesty, Compassion, Valor, Justice, Sacrifice, Honor, Spirituality, Humility)
- Become Avatar (master all virtues)
- Overworld (256×256 tiles)
- 8 towns (one per virtue)
- 8 dungeons (multi-level, 3D-ish)
- Party (up to 8 characters, different classes)
- Turn-based combat
- Ships (sail between continents)
- Moongates (teleportation based on moon phases)
- Quest for the Codex
- Save system (persist world state)

**Skills Introduced:**
- Virtue/morality system (choices affect virtues)
- Large overworld (256×256, chunked loading)
- Party management (8 characters, different classes)
- Turn-based combat (party vs enemies)
- Ships (water travel)
- Moongates (time-based teleportation)
- Multi-level dungeons (3D first-person in dungeons)
- Dialogue system (keyword-based)
- Quest tracking (virtue progress)

### Lesson Structure

**Lessons 3457-3464: Overworld**
- L3457-3458: 256×256 tile map (chunked loading)
- L3459-3460: Player movement (tile-based)
- L3461-3462: Town entrances
- L3463-3464: Dungeon entrances

**Lessons 3465-3472: Party System**
- L3465-3466: Party data structure (8 characters)
- L3467-3468: Character classes (fighter, mage, bard, etc.)
- L3469-3470: Party formation
- L3471-3472: Recruiting party members

**Lessons 3473-3480: Stats & Inventory**
- L3473-3474: Character stats (STR, DEX, INT, HP, MP)
- L3475-3476: Inventory system (items, weapons, armor)
- L3477-3478: Equipment slots
- L3479-3480: Gold and resources

**Lessons 3481-3488: Turn-Based Combat**
- L3481-3482: Combat initiation (random encounters)
- L3483-3484: Turn order (based on DEX)
- L3485-3486: Attack command (physical)
- L3487-3488: Magic command (spell casting)

**Lessons 3489-3496: Combat Continued**
- L3489-3490: Defend, flee commands
- L3491-3492: Enemy AI (target selection)
- L3493-3494: Damage calculation
- L3495-3496: Victory (XP, gold, items)

**Lessons 3497-3504: Virtue System**
- L3497-3498: 8 Virtues tracking
- L3499-3500: Choices affect virtues (donate to beggar = Compassion)
- L3501-3502: Virtue progression
- L3503-3504: Avatar requirements (all virtues mastered)

**Lessons 3505-3512: Towns**
- L3505-3506: Town layout (8 towns)
- L3507-3508: NPCs and dialogue (keyword system)
- L3509-3510: Shops (weapons, armor, food)
- L3511-3512: Healers and temples

**Lessons 3513-3520: Dungeons**
- L3513-3514: Dungeon entrances (8 dungeons)
- L3515-3516: First-person 3D view (wire-frame style)
- L3517-3518: Dungeon levels (8 levels deep)
- L3519-3520: Dungeon monsters and treasures

**Lessons 3521-3528: Dungeons Continued**
- L3521-3522: Dungeon navigation
- L3523-3524: Altars and stones
- L3525-3526: Finding the Codex pieces
- L3527-3528: Dungeon boss battles

**Lessons 3529-3536: Ships & Travel**
- L3529-3530: Ship acquisition
- L3531-3532: Sailing (water tiles)
- L3533-3534: Wind direction
- L3535-3536: Docking at ports

**Lessons 3537-3544: Moongates**
- L3537-3538: Moon phases (cycle through 8 phases)
- L3539-3540: Moongate spawning (based on phase and location)
- L3541-3542: Moongate travel (teleportation)
- L3543-3544: Strategic moongate use

**Lessons 3545-3552: Magic System**
- L3545-3546: Spell list (26 spells, A-Z)
- L3547-3548: Reagents (8 types, required for spells)
- L3549-3550: Spell mixing (combine reagents)
- L3551-3552: Spell effects (damage, heal, buff)

**Lessons 3553-3560: Quest for Codex**
- L3553-3554: Quest structure (collect runes, stones)
- L3555-3556: Codex location (Abyss)
- L3557-3558: Final challenge
- L3559-3560: Becoming the Avatar

**Lessons 3561-3568: Save System**
- L3561-3562: Save game structure (party, world state, progress)
- L3563-3564: Save to disk
- L3565-3566: Load game
- L3567-3568: Multiple save slots

**Lessons 3569-3576: World Persistence**
- L3569-3570: NPC state (alive/dead, dialogue progress)
- L3571-3572: Town state (shops inventory)
- L3573-3574: Dungeon state (explored rooms, items taken)
- L3575-3576: Quest flags

**Lessons 3577-3584: Polish & Completion**
- L3577-3578: Music and sound effects
- L3579-3580: Difficulty balancing
- L3581-3582: Ending sequence (Avatar achievement)
- L3583-3584: Final polish

---

## Tier 2: Zelda (Lessons 3585-3712)

**Goal:** Build Zelda with real-time combat, item-gated progression, and dungeons.

**Why this game:** Defines action RPG. Items unlock areas. Heart pieces. Perfect pacing.

**Game Requirements:**
- Overworld (128 screens)
- 9 dungeons (themed, each with boss)
- Real-time combat (sword, bow, bombs)
- Items (boomerang, raft, ladder, wand, etc.)
- Item-gated progression (need ladder to cross gaps)
- Heart pieces (increase max health)
- Triforce pieces (collect from dungeons)
- Boss keys (unlock boss room)
- Shops (buy items, upgrades)
- Secret caves (hidden passages)

**Skills Introduced:**
- Real-time combat (swing sword, no turns)
- Item-gated progression (Metroidvania-style)
- Dungeon design (keys, puzzles, bosses)
- Heart piece collection (scattered throughout)
- Secret discovery (bomb walls, burn bushes)
- Boss battles (patterns, weak points)

---

## Tier 3: Bard's Tale (Lessons 3713-3840)

**Goal:** Build first-person dungeon crawler with party and spell casting.

**Why this game:** First-person perspective. Party management. Spell-heavy combat.

**Game Requirements:**
- First-person 3D dungeons (wire-frame)
- Party of 6 (create characters, choose classes)
- Classes (Warrior, Paladin, Rogue, Bard, Mage, Conjurer, etc.)
- Turn-based combat
- Spell system (99 spells across classes)
- Equipment (weapons, armor, special items)
- Multiple dungeons (sewers, catacombs, castle)
- Save anywhere
- Permadeath option

**Skills Introduced:**
- First-person dungeon rendering (3D wire-frame)
- Party creation (roll stats, choose class)
- Class-specific spells
- Spell points (MP) management
- Complex spell effects (summon, buff, debuff)
- Dungeon mapping (player creates map)

---

## Tier 4: Final Fantasy (Lessons 3841-3968)

**Goal:** Build JRPG with job system, world map, and airship.

**Why this game:** JRPG mechanics. Job system. Epic scope. World travel.

**Game Requirements:**
- 4-character party (Light Warriors)
- Job system (Warrior, Thief, Monk, Red Mage, White Mage, Black Mage)
- Turn-based combat (ATB-style)
- World map (multiple continents)
- Airship (fly anywhere)
- Ship (sail between continents)
- Dungeons and towns
- 4 Orbs of Light (main quest)
- Boss battles (Lich, Marilith, Kraken, Tiamat, Chaos)
- Magic system (levels 1-8 spells, charges per level)

**Skills Introduced:**
- Job system (choose 4 jobs for party)
- ATB combat (active time battle, timed turns)
- Magic levels (spells organized by level, limited casts)
- World map travel (multiple continents, vehicle transitions)
- Airship mechanics (fly over obstacles)
- Epic story structure (4 orbs, time travel)

---

## Tier 5: Wasteland (Lessons 3969-4096)

**Goal:** Build post-apocalyptic RPG with skills, choices, and consequences.

**Why this game:** Skill-based (not class). Dialogue choices matter. Multiple solutions.

**Game Requirements:**
- Skill system (Assault Rifle, Demolitions, Toaster Repair, etc.)
- Skill checks (dialogue, obstacles require specific skills)
- Party (4 Desert Rangers, recruit NPCs)
- Turn-based combat (cover, action points)
- Dialogue choices (affect outcomes, reputation)
- Multiple solutions (violence, stealth, speech)
- Branching storyline
- Multiple endings
- Post-apocalyptic setting

**Skills Introduced:**
- Skill-based progression (not classes, individual skills)
- Skill checks in dialogue and exploration
- Choices and consequences (reputation, story branches)
- Multiple solution paths (same goal, different approaches)
- Cover system (tactical combat)
- Action points (limited actions per turn)

---

## Tier 6: Rogue (Lessons 4097-4224)

**Goal:** Build roguelike with procedural generation and permadeath.

**Why this game:** Procedural dungeons. Permadeath. Item identification. Replayability.

**Game Requirements:**
- Procedurally generated dungeons (26 levels, random each playthrough)
- Permadeath (death = start over)
- Hunger system (must eat food)
- Item identification (potions, scrolls unknown until identified)
- Monster variety (50+ types)
- Character growth (XP, level, stats)
- Amulet of Yendor (goal: retrieve and escape)
- ASCII or tile graphics
- Turn-based movement and combat

**Skills Introduced:**
- Procedural dungeon generation (random rooms, corridors)
- Permadeath (no save scumming)
- Item identification (potions are "?" until used/identified)
- Hunger system (resource pressure)
- Procedural item/monster placement
- Random loot generation

---

## Tier 7: Diablo-style (Lessons 4225-4352)

**Goal:** Build loot-focused action RPG with randomized items.

**Why this game:** Loot is the game. Fast combat. Grinding loop. Addictive.

**Game Requirements:**
- Real-time combat (click to attack, fast-paced)
- Randomized loot (items have random stats)
- 3 classes (Warrior, Rogue, Sorcerer)
- 16-level dungeon (descend to defeat Diablo)
- Procedural dungeon levels
- Item affixes (prefixes, suffixes add bonuses)
- Rarity tiers (normal, magic, rare, unique)
- Town (shop, identify items, repair)
- Multiplayer (optional, but system designed for it)

**Skills Introduced:**
- Loot generation system (randomized stats, affixes)
- Rarity tiers
- Click-to-move, click-to-attack
- Fast-paced action RPG combat
- Grinding loop (kill monsters for better loot)
- Item comparison (is this item better?)

---

## Tier 8: Betrayal at Krondor (Lessons 4353-4480)

**Goal:** Build tactical RPG with deep story, riddles, and exploration.

**Why this game:** Tactical turn-based combat. Story-driven. Riddles. Exploration. Synthesis.

**Game Requirements:**
- Tactical turn-based combat (position matters, facing, flanking)
- 3 characters (Locklear, Gorath, Owyn)
- Open-world exploration (multiple regions)
- Chapters (story progresses through chapters, different objectives)
- Riddles (puzzle chests, riddles to unlock)
- Skill system (Swordsmanship, Crossbow, Casting, Barding, etc.)
- Repair system (weapons/armor degrade, must repair)
- Spell system (unique magic)
- Deep story (political intrigue, war)

**Skills Introduced:**
- Tactical combat (position, facing, flanking)
- Riddles (text-based puzzles for treasures)
- Weapon/armor degradation and repair
- Chapter structure (story progresses in chapters)
- Everything from Phase 7 synthesized

---

## Phase 7 Outcome

Students have built **8 complete RPGs** and mastered:

**Core RPG Systems:**
- Stats systems (attributes, derived stats)
- Character classes and jobs
- Skill systems
- Leveling and XP curves

**Combat:**
- Turn-based combat (initiative, commands)
- Real-time combat (action RPG)
- Tactical combat (position, cover, facing)
- ATB systems
- Action points

**Inventory & Equipment:**
- Inventory management (grids, weight)
- Equipment slots
- Item affixes and randomization
- Loot generation
- Rarity tiers
- Weapon/armor degradation

**Magic Systems:**
- Spell lists
- MP/spell charges
- Reagents
- Spell levels
- Spell effects (damage, heal, buff, debuff, summon)

**World Design:**
- Overworld exploration (large maps)
- Dungeon design (levels, puzzles, bosses)
- First-person dungeons
- Procedural generation
- Item-gated progression

**Progression:**
- XP and leveling
- Stat increases
- Skill progression
- Virtue/morality systems
- Quest progression

**Persistence:**
- Save/load systems (full game state)
- Multi-disk management
- World persistence (NPC states, flags)
- Multiple save slots

**Narrative:**
- Dialogue systems (keyword, choice-based)
- Quest tracking
- Branching storylines
- Multiple endings
- Riddles

**Economy:**
- Shops (buy/sell)
- Gold/currency
- Prices
- Item identification

**Party Management:**
- Multiple characters (4-8 party members)
- Party formation
- Recruiting NPCs
- Character switching

**Ready for Phase 8:** Students transition to adventure games with inventory puzzles and narrative focus.

---

**Version:** 3.0
**Date:** 2025-10-20
**Status:** Complete restructure for 1024-lesson phase
**Focus:** 8 RPGs spanning all sub-genres - most complex systems mastered
