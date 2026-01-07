# Knuckle Brawl: 128-Unit Outline

**Game:** 13 of 16
**Platform:** ZX Spectrum
**Units:** 128 (8 phases)
**Concept:** Side-scrolling beat 'em up. Fight through city streets, combo enemies, rescue the hostage. Double Dragon territory.

---

## Why This Game Thirteenth?

Knuckle Brawl introduces belt-scrolling combat with depth:

1. **2.5D movement** - Up/down creates depth illusion
2. **Melee combat** - Punch, kick, grab, throw
3. **Combo systems** - Chained attacks
4. **Enemy AI swarms** - Multiple attackers coordinating
5. **Weapons pickup** - Environmental combat

This genre requires tight collision and animation.

---

## Skills Applied from Previous Games

| Skill | From | Application in Knuckle Brawl |
|-------|------|----------------------------|
| Scrolling | Blitz/Exodus | Belt scrolling |
| Object arrays | All | Enemy management |
| Animation | All | Combat animations |
| Collision | All | Hit detection |
| Enemy AI | Chambers/Chomp | Attack behaviours |
| Co-op | Recoil | Two-player mode |

## New Skills Introduced

| Skill | Phase | Description |
|-------|-------|-------------|
| 2.5D depth | 1 | Y-axis creates depth |
| Depth sorting | 1 | Draw order by Y position |
| Melee combat | 2 | Close-range attacks |
| Combo chains | 2 | Sequential attacks |
| Grab mechanics | 3 | Grappling enemies |
| Throw attacks | 3 | Tossing grabbed enemies |
| Weapon pickups | 4 | Found weapons |
| Crowd AI | 5 | Managing multiple attackers |

---

## Phase 1: Belt Scroll Foundation (Units 1-16)
*2.5D movement and depth.*

### Units 1-4: 2.5D Space
- **Unit 1:** Depth concept - Y position as depth
- **Unit 2:** Ground plane - walkable area bounds
- **Unit 3:** Depth boundaries - top/bottom limits
- **Unit 4:** Perspective scale - slight size change with depth

### Units 5-8: Depth Sorting
- **Unit 5:** Sort by Y - draw back to front
- **Unit 6:** Dynamic sorting - resort as objects move
- **Unit 7:** Shadow depth - shadows indicate position
- **Unit 8:** Overlap handling - clean depth overlap

### Units 9-12: Player Character
- **Unit 9:** Fighter sprite - brawler character
- **Unit 10:** 4-way movement - including depth axis
- **Unit 11:** Walk animation - 8-frame cycle
- **Unit 12:** Idle animation - standing pose

### Units 13-16: Belt Scrolling
- **Unit 13:** Horizontal scroll - side-scrolling view
- **Unit 14:** Scroll triggers - advance when enemies cleared
- **Unit 15:** Screen lock - can't advance during combat
- **Unit 16:** Playable foundation - walk around 2.5D space

**Phase Goal:** 2.5D movement with belt scrolling.

---

## Phase 2: Basic Combat (Units 17-32)
*Punching, kicking, and combos.*

### Units 17-20: Attack Animations
- **Unit 17:** Punch animation - quick jab
- **Unit 18:** Kick animation - stronger but slower
- **Unit 19:** Attack hitbox - active damage area
- **Unit 20:** Attack timing - frame-perfect detection

### Units 21-24: Hit Detection
- **Unit 21:** Depth-aware collision - same depth required
- **Unit 22:** Depth tolerance - how close in depth
- **Unit 23:** Hit confirmation - enemy takes damage
- **Unit 24:** Knockback - enemy pushed back

### Units 25-28: Combo System
- **Unit 25:** Combo window - time to chain attacks
- **Unit 26:** Combo counter - track current chain
- **Unit 27:** Combo finishers - special final move
- **Unit 28:** Combo variety - different combo paths

### Units 29-32: Basic Enemies
- **Unit 29:** Grunt enemy - basic attacker
- **Unit 30:** Enemy walking - approach player
- **Unit 31:** Enemy attacking - throw punches
- **Unit 32:** Enemy stagger - reaction to hits

**Phase Goal:** Functional melee combat with combos.

---

## Phase 3: Advanced Combat (Units 33-48)
*Grabs, throws, and special moves.*

### Units 33-36: Grab Mechanics
- **Unit 33:** Grab input - close-range grab
- **Unit 34:** Grab state - holding enemy
- **Unit 35:** Grabbed enemy - helpless state
- **Unit 36:** Grab attacks - knee, headbutt

### Units 37-40: Throw System
- **Unit 37:** Throw direction - aim throw
- **Unit 38:** Throw animation - releasing enemy
- **Unit 39:** Thrown enemy - projectile physics
- **Unit 40:** Throw damage - to thrown and hit enemies

### Units 41-44: Special Moves
- **Unit 41:** Jump kick - aerial attack
- **Unit 42:** Back attack - behind player hit
- **Unit 43:** Ground attack - hit downed enemies
- **Unit 44:** Desperation move - crowd clearer

### Units 45-48: Player Damage
- **Unit 45:** Health bar - player HP
- **Unit 46:** Taking damage - hit by enemies
- **Unit 47:** Knockdown - player falls
- **Unit 48:** Getting up - recovery state

**Phase Goal:** Deep combat with grabs and throws.

---

## Phase 4: Weapons (Units 49-64)
*Pickup and use weapons.*

### Units 49-52: Weapon System
- **Unit 49:** Weapon objects - bats, pipes, knives
- **Unit 50:** Weapon pickup - grab from ground
- **Unit 51:** Armed state - holding weapon
- **Unit 52:** Weapon drop - lose weapon on hit

### Units 53-56: Weapon Combat
- **Unit 53:** Weapon attacks - different per weapon
- **Unit 54:** Weapon range - longer than fists
- **Unit 55:** Weapon damage - stronger attacks
- **Unit 56:** Weapon durability - breaks after uses

### Units 57-60: Thrown Objects
- **Unit 57:** Throwable weapons - knives, barrels
- **Unit 58:** Throw input - release weapon
- **Unit 59:** Throw trajectory - arc through air
- **Unit 60:** Thrown impact - damage on hit

### Units 61-64: Environmental Objects
- **Unit 61:** Barrels - break for items
- **Unit 62:** Crates - obstacles and weapons
- **Unit 63:** Phone booths - destructible scenery
- **Unit 64:** Environmental hazards - pits, traffic

**Phase Goal:** Weapon combat and environment interaction.

---

## Phase 5: Enemy Variety (Units 65-80)
*Enemy types and crowd behaviour.*

### Units 65-68: Enemy Types
- **Unit 65:** Punk - fast, weak
- **Unit 66:** Thug - slow, strong
- **Unit 67:** Knife wielder - dangerous reach
- **Unit 68:** Acrobat - jumping attacks

### Units 69-72: Special Enemies
- **Unit 69:** Female enemy - different animations
- **Unit 70:** Fat enemy - takes more hits
- **Unit 71:** Boss henchman - mini-boss tier
- **Unit 72:** Armed enemy - guns or heavy weapons

### Units 73-76: Crowd AI
- **Unit 73:** Surround player - positioning
- **Unit 74:** Attack timing - don't all attack at once
- **Unit 75:** Backup behaviour - wait for opening
- **Unit 76:** Aggression scaling - pressure varies

### Units 77-80: Spawning and Waves
- **Unit 77:** Wave spawning - groups of enemies
- **Unit 78:** Entry points - where enemies appear
- **Unit 79:** Wave completion - when to advance
- **Unit 80:** Difficulty ramping - harder waves

**Phase Goal:** Varied enemies with smart behaviour.

---

## Phase 6: Bosses and Levels (Units 81-96)
*Boss fights and level variety.*

### Units 81-84: Boss Fights
- **Unit 81:** Boss character - larger sprite
- **Unit 82:** Boss health - extended HP bar
- **Unit 83:** Boss patterns - attack sequences
- **Unit 84:** Boss damage - high damage attacks

### Units 85-88: Boss Variety
- **Unit 85:** Stage 1 boss - gang leader
- **Unit 86:** Stage 2 boss - martial artist
- **Unit 87:** Stage 3 boss - heavy weapon user
- **Unit 88:** Final boss - main antagonist

### Units 89-92: Level Themes
- **Unit 89:** Street level - urban environment
- **Unit 90:** Warehouse level - industrial setting
- **Unit 91:** Club level - indoor nightclub
- **Unit 92:** Final level - enemy headquarters

### Units 93-96: Level Features
- **Unit 93:** Level transitions - scene changes
- **Unit 94:** Elevator sections - confined spaces
- **Unit 95:** Bonus stages - weapon breaking
- **Unit 96:** Story cutscenes - narrative moments

**Phase Goal:** Boss fights and level variety.

---

## Phase 7: Two-Player Mode (Units 97-112)
*Cooperative brawling.*

### Units 97-100: Co-op Setup
- **Unit 97:** Two players - both active
- **Unit 98:** Separate controls - two input sets
- **Unit 99:** Character selection - different fighters
- **Unit 100:** Shared screen - both visible

### Units 101-104: Co-op Mechanics
- **Unit 101:** Friendly fire - optional or forced
- **Unit 102:** Team attacks - combo together
- **Unit 103:** Rescue mechanic - help downed partner
- **Unit 104:** Item priority - who grabs pickups

### Units 105-108: Co-op Balance
- **Unit 105:** More enemies - scale for two
- **Unit 106:** Enemy targeting - split attention
- **Unit 107:** Score comparison - competitive scoring
- **Unit 108:** Continue system - co-op continues

### Units 109-112: Presentation
- **Unit 109:** Title screen - game logo
- **Unit 110:** Character select - choose fighter
- **Unit 111:** Stage intro - level name
- **Unit 112:** Ending sequence - victory cutscene

**Phase Goal:** Full two-player cooperative mode.

---

## Phase 8: Release (Units 113-128)
*Polish and release.*

### Units 113-116: Audio
- **Unit 113:** Punch sounds - impact effects
- **Unit 114:** Voice samples - grunts, yells
- **Unit 115:** Music loops - per stage
- **Unit 116:** Boss music - intense theme

### Units 117-120: Visual Polish
- **Unit 117:** Hit effects - impact stars
- **Unit 118:** Damage numbers - optional display
- **Unit 119:** Screen effects - boss entry
- **Unit 120:** Attract mode - demo play

### Units 121-124: Game Modes
- **Unit 121:** Story mode - full game
- **Unit 122:** Survival mode - endless waves
- **Unit 123:** Boss rush - sequential bosses
- **Unit 124:** Difficulty levels - easy to hard

### Units 125-128: Release
- **Unit 125:** Instructions screen
- **Unit 126:** Balance testing - damage tuning
- **Unit 127:** Performance testing - many sprites
- **Unit 128:** Release build - final TAP file

**Phase Goal:** Complete beat 'em up game.

---

## Summary

**Knuckle Brawl** teaches belt-scroll combat:

**Phase 1 (Foundation):** 2.5D space, depth sorting.

**Phase 2 (Combat):** Punching, kicking, combos.

**Phase 3 (Advanced):** Grabs, throws, specials.

**Phase 4 (Weapons):** Pickup weapons, environment.

**Phase 5 (Enemies):** Variety, crowd AI.

**Phase 6 (Bosses):** Boss fights, levels.

**Phase 7 (Co-op):** Two-player mode.

**Phase 8 (Release):** Polish, release.

### Skills Transferred Forward

1. **2.5D depth** → Isometric, pseudo-3D games
2. **Depth sorting** → Any layered display
3. **Melee combat** → Fighting games
4. **Combo systems** → Action games
5. **Grab/throw** → Wrestling, physics
6. **Crowd AI** → Group enemy behaviour

### Game Specifications

- **Levels:** 4-6 stages
- **Player:** 24×32 sprite with full animation set
- **Moves:** Punch, kick, grab, throw, jump, special
- **Weapons:** 4+ types (bat, pipe, knife, chain)
- **Enemies:** 8+ types plus bosses
- **Bosses:** 1 per level
- **Players:** 1 or 2 cooperative
- **Lives:** 3 per player
- **Health:** Bar-based HP
- **Controls:** 8-way move, punch, kick, jump
- **Audio:** Beeper effects + music
- **Distribution:** TAP file
