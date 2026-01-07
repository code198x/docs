# Pavement Justice: 128-Unit Outline

**Game:** 13 of 16
**Platform:** Nintendo Entertainment System
**Units:** 128 (8 phases)
**Concept:** Side-scrolling beat 'em up. Walk the streets, punch enemies, clean up crime. Double Dragon-style action with Y-depth.

---

## Why This Game Thirteenth?

Pavement Justice introduces belt-scrolling combat with depth:

1. **Y-axis depth** - Walking "into" the screen
2. **Depth sorting** - Draw order by Y position
3. **Melee combat** - Punch, kick, grab
4. **Combo systems** - Chained attacks
5. **Crowd management** - Multiple attackers

This genre pushes NES sprite limits.

---

## Skills Applied from Previous Games

| Skill | From | Application in Pavement Justice |
|-------|------|-------------------------------|
| Scrolling | Pixel Plains | Belt scrolling |
| Animation | All | Combat animations |
| Object management | All | Enemy management |
| Collision | All | Hit detection |
| Sprite flickering | Stellar Barrage | Many sprites |

## New Skills Introduced

| Skill | Phase | Description |
|-------|-------|-------------|
| Y-depth | 1 | Walking in 2.5D |
| Depth sorting | 1 | Draw back-to-front |
| Melee combat | 2 | Close-range attacks |
| Combo chains | 2 | Sequential attacks |
| Grab mechanics | 3 | Grappling enemies |
| Throw attacks | 3 | Tossing enemies |
| Crowd AI | 5 | Managing attackers |

---

## Phase 1: Belt Scroll Foundation (Units 1-16)
*2.5D movement and depth.*

### Units 1-4: 2.5D Space
- **Unit 1:** Depth concept - Y as depth
- **Unit 2:** Ground plane - walkable bounds
- **Unit 3:** Depth boundaries - limits
- **Unit 4:** Perspective - slight size change

### Units 5-8: Depth Sorting
- **Unit 5:** Sort by Y - back to front
- **Unit 6:** Dynamic sorting - each frame
- **Unit 7:** Shadow sprites - ground shadow
- **Unit 8:** Clean overlap - depth display

### Units 9-12: Player Character
- **Unit 9:** Fighter sprite - brawler
- **Unit 10:** 4-way movement - including depth
- **Unit 11:** Walk animation - 8 frames
- **Unit 12:** Idle stance - standing pose

### Units 13-16: Belt Scrolling
- **Unit 13:** Horizontal scroll - side movement
- **Unit 14:** Scroll triggers - advance on clear
- **Unit 15:** Screen lock - combat stops scroll
- **Unit 16:** Belt foundation - 2.5D movement

**Phase Goal:** 2.5D belt scrolling.

---

## Phase 2: Basic Combat (Units 17-32)
*Punching, kicking, combos.*

### Units 17-20: Attack System
- **Unit 17:** Punch animation - quick jab
- **Unit 18:** Kick animation - stronger/slower
- **Unit 19:** Attack hitbox - active area
- **Unit 20:** Attack timing - frame detection

### Units 21-24: Hit Detection
- **Unit 21:** Depth-aware collision - same plane
- **Unit 22:** Depth tolerance - collision range
- **Unit 23:** Hit confirmation - enemy takes hit
- **Unit 24:** Knockback - pushed back

### Units 25-28: Combo System
- **Unit 25:** Combo window - chain timing
- **Unit 26:** Combo counter - track chain
- **Unit 27:** Combo finishers - special final hit
- **Unit 28:** Combo variety - different paths

### Units 29-32: Basic Enemies
- **Unit 29:** Grunt enemy - basic attacker
- **Unit 30:** Enemy walking - approach
- **Unit 31:** Enemy attacking - throw punches
- **Unit 32:** Enemy stagger - hit reaction

**Phase Goal:** Melee combat working.

---

## Phase 3: Advanced Combat (Units 33-48)
*Grabs, throws, special moves.*

### Units 33-36: Grab Mechanics
- **Unit 33:** Grab input - close-range
- **Unit 34:** Grab state - holding enemy
- **Unit 35:** Grabbed sprite - helpless
- **Unit 36:** Grab attacks - knee, headbutt

### Units 37-40: Throw System
- **Unit 37:** Throw direction - aim throw
- **Unit 38:** Throw animation - release
- **Unit 39:** Thrown enemy - projectile
- **Unit 40:** Throw damage - impact

### Units 41-44: Special Moves
- **Unit 41:** Jump kick - aerial
- **Unit 42:** Back attack - behind hit
- **Unit 43:** Ground attack - hit downed
- **Unit 44:** Desperation - crowd clear

### Units 45-48: Player Damage
- **Unit 45:** Health bar - HP display
- **Unit 46:** Taking damage - hit by enemy
- **Unit 47:** Knockdown - player falls
- **Unit 48:** Getting up - recovery

**Phase Goal:** Deep combat with grabs.

---

## Phase 4: Weapons (Units 49-64)
*Pickup and use weapons.*

### Units 49-52: Weapon System
- **Unit 49:** Weapon objects - bats, pipes
- **Unit 50:** Weapon pickup - grab from ground
- **Unit 51:** Armed state - holding weapon
- **Unit 52:** Weapon drop - lose on hit

### Units 53-56: Weapon Combat
- **Unit 53:** Weapon attacks - different per type
- **Unit 54:** Weapon range - longer reach
- **Unit 55:** Weapon damage - stronger
- **Unit 56:** Weapon durability - breaks

### Units 57-60: Thrown Objects
- **Unit 57:** Throwable items - knives, barrels
- **Unit 58:** Throw input - release weapon
- **Unit 59:** Throw trajectory - arc
- **Unit 60:** Thrown impact - damage

### Units 61-64: Environment
- **Unit 61:** Barrels - destructible
- **Unit 62:** Crates - obstacles
- **Unit 63:** Environmental hazards - pits
- **Unit 64:** Interactive objects - full system

**Phase Goal:** Weapon combat.

---

## Phase 5: Enemy Variety (Units 65-80)
*Enemy types and crowd AI.*

### Units 65-68: Enemy Types
- **Unit 65:** Punk - fast/weak
- **Unit 66:** Thug - slow/strong
- **Unit 67:** Knife wielder - dangerous
- **Unit 68:** Acrobat - jumping

### Units 69-72: Special Enemies
- **Unit 69:** Female enemy - different animation
- **Unit 70:** Fat enemy - more HP
- **Unit 71:** Boss henchman - mini-boss
- **Unit 72:** Armed enemy - guns

### Units 73-76: Crowd AI
- **Unit 73:** Surround player - positioning
- **Unit 74:** Attack timing - staggered attacks
- **Unit 75:** Backup behaviour - wait turns
- **Unit 76:** Aggression scaling - pressure

### Units 77-80: Spawning
- **Unit 77:** Wave spawning - groups
- **Unit 78:** Entry points - spawn locations
- **Unit 79:** Wave completion - clear trigger
- **Unit 80:** Difficulty ramp - harder waves

**Phase Goal:** Varied enemies with AI.

---

## Phase 6: Bosses and Levels (Units 81-96)
*Boss fights and stages.*

### Units 81-84: Boss Fights
- **Unit 81:** Boss character - large sprite
- **Unit 82:** Boss health - extended HP
- **Unit 83:** Boss patterns - attack sequences
- **Unit 84:** Boss damage - high attacks

### Units 85-88: Boss Variety
- **Unit 85:** Stage 1 boss - gang leader
- **Unit 86:** Stage 2 boss - martial artist
- **Unit 87:** Stage 3 boss - weapon master
- **Unit 88:** Final boss - main villain

### Units 89-92: Level Themes
- **Unit 89:** Street level - urban
- **Unit 90:** Warehouse - industrial
- **Unit 91:** Subway - underground
- **Unit 92:** Crime boss HQ - final

### Units 93-96: Level Features
- **Unit 93:** Level transitions - scene changes
- **Unit 94:** Elevator sections - confined
- **Unit 95:** Bonus stages - weapon destroy
- **Unit 96:** Story moments - cutscenes

**Phase Goal:** Boss fights and levels.

---

## Phase 7: Two-Player Mode (Units 97-112)
*Cooperative brawling.*

### Units 97-100: Co-op Setup
- **Unit 97:** Two players - both active
- **Unit 98:** Separate inputs - two controllers
- **Unit 99:** Character selection - different fighters
- **Unit 100:** Shared screen - both visible

### Units 101-104: Co-op Mechanics
- **Unit 101:** Friendly fire - optional
- **Unit 102:** Team attacks - combo together
- **Unit 103:** Rescue - help downed partner
- **Unit 104:** Item priority - pickup rules

### Units 105-108: Co-op Balance
- **Unit 105:** More enemies - scale for two
- **Unit 106:** Enemy targeting - split attention
- **Unit 107:** Score comparison - competitive
- **Unit 108:** Continue system - co-op continues

### Units 109-112: Presentation
- **Unit 109:** Title screen - logo
- **Unit 110:** Character select - choose fighter
- **Unit 111:** Stage intro - level name
- **Unit 112:** Ending - victory scene

**Phase Goal:** Two-player cooperative.

---

## Phase 8: Release (Units 113-128)
*Polish and release.*

### Units 113-116: Audio
- **Unit 113:** Punch sounds - impact
- **Unit 114:** Enemy sounds - grunts
- **Unit 115:** Stage music - per level
- **Unit 116:** Boss music - intense

### Units 117-120: Visual Polish
- **Unit 117:** Hit effects - impact stars
- **Unit 118:** Screen effects - flash
- **Unit 119:** Attract mode - demo
- **Unit 120:** Visual variety - colours

### Units 121-124: Game Modes
- **Unit 121:** Story mode - full game
- **Unit 122:** Survival mode - endless
- **Unit 123:** Boss rush - sequential
- **Unit 124:** Difficulty levels - easy/hard

### Units 125-128: Release
- **Unit 125:** Instructions screen
- **Unit 126:** Balance testing
- **Unit 127:** Performance testing
- **Unit 128:** Release build - final ROM

**Phase Goal:** Complete beat 'em up.

---

## Summary

**Pavement Justice** teaches belt-scroll combat.

### Game Specifications

- **Levels:** 4-6 stages
- **Player:** 24×32 sprite with full animations
- **Combat:** Punch, kick, grab, throw, specials
- **Weapons:** 4+ types
- **Enemies:** 8+ types plus bosses
- **Players:** 1-2 cooperative
- **Lives:** 3 per player
- **Health:** Bar-based HP
- **Mapper:** MMC1
- **ROM Size:** 128KB PRG + 64KB CHR
- **Controls:** D-pad + A (attack) + B (jump)
- **Distribution:** iNES ROM file
