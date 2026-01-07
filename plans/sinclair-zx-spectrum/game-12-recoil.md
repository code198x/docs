# Recoil: 128-Unit Outline

**Game:** 12 of 16
**Platform:** ZX Spectrum
**Units:** 128 (8 phases)
**Concept:** Run'n'gun action platformer. Fight through enemy hordes, upgrade weapons, defeat bosses. Contra-style intensity.

---

## Why This Game Twelfth?

Recoil combines scrolling platforming with intense combat:

1. **8-way shooting** - Aim in any direction
2. **Weapon systems** - Multiple guns, upgrades
3. **Boss battles** - Large multi-part enemies
4. **Destructible terrain** - Environment interaction
5. **Two-player co-op** - Simultaneous play

This builds on Exodus's scrolling platformer with combat depth.

---

## Skills Applied from Previous Games

| Skill | From | Application in Recoil |
|-------|------|---------------------|
| Scrolling platformer | Exodus | Core movement |
| Projectile pools | Skyfire | Bullet management |
| Enemy patterns | Skyfire | Enemy behaviours |
| World coordinates | Exodus | Large levels |
| Checkpoints | Exodus | Progress saving |
| Object arrays | All | Entities management |

## New Skills Introduced

| Skill | Phase | Description |
|-------|-------|-------------|
| 8-way aiming | 1 | Directional shooting |
| Weapon switching | 2 | Multiple weapon types |
| Weapon power-ups | 2 | Upgrade drops |
| Boss health bars | 4 | Multi-hit bosses |
| Boss patterns | 4 | Complex attack sequences |
| Destructible terrain | 5 | Breaking environment |
| Co-op gameplay | 6 | Two players simultaneously |
| Spread shot | 2 | Multi-bullet weapons |

---

## Phase 1: Core Combat (Units 1-16)
*Basic shooting mechanics.*

### Units 1-4: Player Soldier
- **Unit 1:** Soldier sprite - armed character design
- **Unit 2:** Walk animation - 8-frame cycle
- **Unit 3:** Aim poses - 8 directional sprites
- **Unit 4:** Death animation - hit sequence

### Units 5-8: 8-Way Aiming
- **Unit 5:** Aim direction - tracking where player faces
- **Unit 6:** Input for aim - diagonal detection
- **Unit 7:** Sprite selection - correct pose for aim
- **Unit 8:** Smooth aim transition - changing direction

### Units 9-12: Basic Shooting
- **Unit 9:** Bullet spawn - create at gun position
- **Unit 10:** Bullet direction - 8-way projectile movement
- **Unit 11:** Bullet pool - multiple active bullets
- **Unit 12:** Fire rate - shooting speed limit

### Units 13-16: Basic Combat
- **Unit 13:** Enemy targets - simple enemies to shoot
- **Unit 14:** Bullet-enemy collision - hitting enemies
- **Unit 15:** Enemy destruction - kill sequence
- **Unit 16:** Combat foundation - shoot enemies while moving

**Phase Goal:** 8-way shooting mechanics working.

---

## Phase 2: Weapons System (Units 17-32)
*Multiple weapons and upgrades.*

### Units 17-20: Weapon Types
- **Unit 17:** Default rifle - standard weapon
- **Unit 18:** Spread gun - 3-way shot
- **Unit 19:** Laser - piercing beam
- **Unit 20:** Rapid fire - faster shooting

### Units 21-24: Weapon Switching
- **Unit 21:** Current weapon - tracking equipped gun
- **Unit 22:** Weapon state - ammo/power for each
- **Unit 23:** Switch input - change weapon
- **Unit 24:** Weapon HUD - show current weapon

### Units 25-28: Power-Up Drops
- **Unit 25:** Power-up spawning - enemies drop items
- **Unit 26:** Power-up types - weapon, health, shield
- **Unit 27:** Power-up collection - pickup mechanics
- **Unit 28:** Weapon upgrade - improve current weapon

### Units 29-32: Weapon Effects
- **Unit 29:** Bullet graphics - different per weapon
- **Unit 30:** Fire sounds - distinct weapon sounds
- **Unit 31:** Impact effects - hit visuals
- **Unit 32:** Muzzle flash - firing effect

**Phase Goal:** Complete weapon system with upgrades.

---

## Phase 3: Enemies and AI (Units 33-48)
*Enemy variety and behaviours.*

### Units 33-36: Infantry Enemies
- **Unit 33:** Basic soldier - walks and shoots
- **Unit 34:** Prone soldier - lying shooter
- **Unit 35:** Running soldier - fast attacker
- **Unit 36:** Jumping soldier - mobile enemy

### Units 37-40: Heavy Enemies
- **Unit 37:** Turret - stationary gunner
- **Unit 38:** Armoured soldier - takes multiple hits
- **Unit 39:** Sniper - accurate long-range
- **Unit 40:** Grenadier - lobbing explosives

### Units 41-44: Special Enemies
- **Unit 41:** Jumping alien - creature enemy
- **Unit 42:** Wall crawler - climbs surfaces
- **Unit 43:** Flying enemy - aerial threats
- **Unit 44:** Suicide bomber - charges player

### Units 45-48: Enemy Spawning
- **Unit 45:** Spawn triggers - enemies appear at points
- **Unit 46:** Wave spawning - groups of enemies
- **Unit 47:** Spawn doors - enemies from environment
- **Unit 48:** Despawn rules - off-screen handling

**Phase Goal:** Enemy variety with distinct behaviours.

---

## Phase 4: Boss Battles (Units 49-64)
*Large multi-phase bosses.*

### Units 49-52: Boss Structure
- **Unit 49:** Boss data - health, parts, patterns
- **Unit 50:** Boss health - large HP pool
- **Unit 51:** Health bar - visual HP display
- **Unit 52:** Boss arena - locked fight area

### Units 53-56: Boss Patterns
- **Unit 53:** Attack patterns - sequence of moves
- **Unit 54:** Pattern switching - change behaviour
- **Unit 55:** Vulnerable windows - when to attack
- **Unit 56:** Damage feedback - boss reacts to hits

### Units 57-60: Multi-Part Bosses
- **Unit 57:** Boss segments - destroyable parts
- **Unit 58:** Part health - independent HP
- **Unit 59:** Part destruction - changes boss
- **Unit 60:** Core weakness - final target

### Units 61-64: Boss Variety
- **Unit 61:** Level 1 boss - tank or mech
- **Unit 62:** Level 2 boss - organic creature
- **Unit 63:** Level 3 boss - wall of guns
- **Unit 64:** Final boss - multi-form challenge

**Phase Goal:** Epic boss battles.

---

## Phase 5: Level Design (Units 65-80)
*Environments and hazards.*

### Units 65-68: Environment Types
- **Unit 65:** Jungle level - outdoor terrain
- **Unit 66:** Base level - industrial interior
- **Unit 67:** Alien hive - organic environment
- **Unit 68:** Fortress level - military complex

### Units 69-72: Destructible Terrain
- **Unit 69:** Breakable blocks - shoot to destroy
- **Unit 70:** Hidden paths - secret routes
- **Unit 71:** Environmental hazards - fires, explosions
- **Unit 72:** Chain reactions - spreading destruction

### Units 73-76: Level Mechanics
- **Unit 73:** Lifts - vertical transport
- **Unit 74:** Conveyor belts - moving floors
- **Unit 75:** Closing walls - trap sections
- **Unit 76:** Timed platforms - disappearing ground

### Units 77-80: Level Flow
- **Unit 77:** Level transitions - stage complete
- **Unit 78:** Mid-level checkpoints - progress saves
- **Unit 79:** Branching paths - optional routes
- **Unit 80:** Secrets - hidden bonuses

**Phase Goal:** Varied levels with interactive environments.

---

## Phase 6: Two-Player Mode (Units 81-96)
*Cooperative gameplay.*

### Units 81-84: Co-op Setup
- **Unit 81:** Two player objects - both active
- **Unit 82:** Separate inputs - player 1 and 2 controls
- **Unit 83:** Both on screen - camera handling
- **Unit 84:** Life sharing - shared or separate lives

### Units 85-88: Co-op Camera
- **Unit 85:** Wider view - accommodate both players
- **Unit 86:** Split decisions - who camera follows
- **Unit 87:** Catch-up - teleport lagging player
- **Unit 88:** Screen boundaries - keep both visible

### Units 89-92: Co-op Combat
- **Unit 89:** Friendly fire - on/off option
- **Unit 90:** Revive mechanics - help downed partner
- **Unit 91:** Score sharing - combined or separate
- **Unit 92:** Power-up priority - who gets drops

### Units 93-96: Co-op Balance
- **Unit 93:** Enemy scaling - more enemies for two
- **Unit 94:** Boss adjustments - harder with two
- **Unit 95:** Continue system - co-op continues
- **Unit 96:** Victory together - both must survive

**Phase Goal:** Full two-player cooperative mode.

---

## Phase 7: Polish and Feedback (Units 97-112)
*Effects, sound, and game feel.*

### Units 97-100: Visual Effects
- **Unit 97:** Explosion animations - multiple sizes
- **Unit 98:** Screen shake - impact feedback
- **Unit 99:** Damage flash - hit indication
- **Unit 100:** Death effects - enemy destruction

### Units 101-104: Audio Design
- **Unit 101:** Weapon sounds - per weapon type
- **Unit 102:** Explosion sounds - size-based
- **Unit 103:** Enemy sounds - attack, death
- **Unit 104:** Boss music - intense themes

### Units 105-108: Player Feedback
- **Unit 105:** Hit indicators - showing damage direction
- **Unit 106:** Low health warning - danger state
- **Unit 107:** Score popups - points earned
- **Unit 108:** Combo counter - kill streaks

### Units 109-112: Presentation
- **Unit 109:** Title screen - game logo
- **Unit 110:** Story intro - mission briefing
- **Unit 111:** Level intro - stage start
- **Unit 112:** Results screen - stage complete

**Phase Goal:** Polished game feel.

---

## Phase 8: Release (Units 113-128)
*Final content and release.*

### Units 113-116: Game Modes
- **Unit 113:** Normal mode - standard game
- **Unit 114:** Hard mode - reduced lives, faster enemies
- **Unit 115:** Boss rush - sequential boss fights
- **Unit 116:** Practice mode - level select

### Units 117-120: Progression
- **Unit 117:** Lives system - continues and game over
- **Unit 118:** Score tracking - high scores
- **Unit 119:** Weapon persistence - keep guns between lives
- **Unit 120:** Achievement markers - completion tracking

### Units 121-124: Extra Content
- **Unit 121:** Bonus level - hidden stage
- **Unit 122:** Alternate weapons - secret guns
- **Unit 123:** Character skins - visual variants
- **Unit 124:** Ending variants - different endings

### Units 125-128: Release
- **Unit 125:** Instructions screen
- **Unit 126:** Difficulty balance - tuning enemy damage
- **Unit 127:** Performance testing - smooth action
- **Unit 128:** Release build - final TAP file

**Phase Goal:** Complete run'n'gun game.

---

## Summary

**Recoil** teaches combat-intensive platforming:

**Phase 1 (Combat):** 8-way aiming, shooting.

**Phase 2 (Weapons):** Multiple guns, upgrades.

**Phase 3 (Enemies):** Enemy variety, AI.

**Phase 4 (Bosses):** Multi-phase boss battles.

**Phase 5 (Levels):** Environments, destruction.

**Phase 6 (Co-op):** Two-player mode.

**Phase 7 (Polish):** Effects, feedback.

**Phase 8 (Release):** Modes, release.

### Skills Transferred Forward

1. **8-way aiming** → Directional combat
2. **Weapon systems** → Inventory and upgrades
3. **Boss patterns** → Complex enemy AI
4. **Destructible terrain** → Environmental interaction
5. **Co-op gameplay** → Multiplayer design
6. **Combat feedback** → Game feel

### Game Specifications

- **Levels:** 4-6 stages
- **Player:** 16×16 sprite, 8 aim directions
- **Weapons:** 4+ types with upgrades
- **Enemies:** 12+ types
- **Bosses:** 1 per level, multi-phase
- **Players:** 1 or 2 cooperative
- **Lives:** 3, with continues
- **Controls:** 8-way move, 8-way aim, fire, weapon switch
- **Audio:** Beeper effects, simple music
- **Distribution:** TAP file
