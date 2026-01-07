# Iron Assault: 128-Unit Outline

**Game:** 12 of 16
**Platform:** Nintendo Entertainment System
**Units:** 128 (8 phases)
**Concept:** Run'n'gun action platformer. Contra-style combat with 8-way shooting, weapons, and intense boss fights. Heavy metal assault on enemy forces.

---

## Why This Game Twelfth?

Iron Assault combines platforming with intense combat:

1. **8-way aiming** - Directional shooting while moving
2. **Weapon variety** - Multiple gun types
3. **Boss battles** - Multi-phase encounters
4. **Two-player co-op** - Simultaneous play
5. **Advanced sprite management** - Many sprites on screen

This is classic NES action at its finest.

---

## Skills Applied from Previous Games

| Skill | From | Application in Iron Assault |
|-------|------|---------------------------|
| Platformer physics | Crate Escape/Pixel Plains | Running, jumping |
| Scrolling | Pixel Plains | Side-scroll levels |
| Projectiles | Stellar Barrage/Ion Trail | Bullet management |
| Boss patterns | Thunder Run | Boss encounters |
| MMC1 mapper | Thunder Run | Extended content |

## New Skills Introduced

| Skill | Phase | Description |
|-------|-------|-------------|
| 8-way aiming | 1 | Directional shooting |
| Prone shooting | 2 | Ducking mechanic |
| Weapon switching | 3 | Multiple weapon types |
| Co-op gameplay | 5 | Two players simultaneously |
| Sprite priority | 5 | Managing two players |
| Base levels | 6 | Behind-the-back perspective |

---

## Phase 1: Core Combat (Units 1-16)
*Basic 8-way shooting mechanics.*

### Units 1-4: Player Soldier
- **Unit 1:** Soldier sprite - armed commando
- **Unit 2:** Walk animation - 8-frame cycle
- **Unit 3:** Aim poses - 8 directional sprites
- **Unit 4:** Death animation - hit sequence

### Units 5-8: 8-Way Aiming
- **Unit 5:** Aim direction tracking - where player faces
- **Unit 6:** Diagonal input - detecting diagonals
- **Unit 7:** Sprite selection - correct pose for aim
- **Unit 8:** Smooth aiming - direction changes

### Units 9-12: Basic Shooting
- **Unit 9:** Bullet spawn - from gun position
- **Unit 10:** Bullet direction - 8-way travel
- **Unit 11:** Bullet pool - active bullets
- **Unit 12:** Fire rate - shooting speed

### Units 13-16: Basic Combat
- **Unit 13:** Enemy targets - simple enemies
- **Unit 14:** Bullet-enemy collision - hitting
- **Unit 15:** Enemy destruction - kill sequence
- **Unit 16:** Combat foundation - shoot while moving

**Phase Goal:** 8-way shooting working.

---

## Phase 2: Movement and Cover (Units 17-32)
*Advanced movement mechanics.*

### Units 17-20: Prone Position
- **Unit 17:** Duck input - down to prone
- **Unit 18:** Prone sprite - lying down
- **Unit 19:** Prone shooting - fire while ducked
- **Unit 20:** Stand up - return to normal

### Units 21-24: Jumping Combat
- **Unit 21:** Jump physics - reusing platformer
- **Unit 22:** Jump shooting - fire in air
- **Unit 23:** Jump aim - 8-way while jumping
- **Unit 24:** Landing transition - smooth land

### Units 25-28: Enemy Types
- **Unit 25:** Running enemy - charges player
- **Unit 26:** Shooting enemy - fires back
- **Unit 27:** Turret enemy - stationary gunner
- **Unit 28:** Enemy variety - mixed combat

### Units 29-32: Scrolling Combat
- **Unit 29:** Side-scrolling - auto and push scroll
- **Unit 30:** Scroll triggers - advance on clear
- **Unit 31:** Enemy spawning - scroll-triggered
- **Unit 32:** Scrolling action - complete combat flow

**Phase Goal:** Full movement with scrolling.

---

## Phase 3: Weapons System (Units 33-48)
*Multiple weapon types.*

### Units 33-36: Default Rifle
- **Unit 33:** Standard shot - basic bullet
- **Unit 34:** Fire rate - normal speed
- **Unit 35:** Ammunition - unlimited
- **Unit 36:** Starting weapon - default setup

### Units 37-40: Weapon Types
- **Unit 37:** Spread gun - 5-way shot
- **Unit 38:** Laser - piercing beam
- **Unit 39:** Fire ball - circular shots
- **Unit 40:** Machine gun - rapid fire

### Units 41-44: Weapon Pickup
- **Unit 41:** Power-up pods - flying pickups
- **Unit 42:** Pod collision - touch to collect
- **Unit 43:** Weapon switching - immediate change
- **Unit 44:** Weapon loss - lose on death

### Units 45-48: Weapon Balance
- **Unit 45:** Spread effectiveness - situations
- **Unit 46:** Laser effectiveness - boss damage
- **Unit 47:** Strategic choice - which weapon
- **Unit 48:** Balanced arsenal - all useful

**Phase Goal:** Complete weapon system.

---

## Phase 4: Boss Battles (Units 49-64)
*Multi-phase boss encounters.*

### Units 49-52: Boss Structure
- **Unit 49:** Boss data - health, patterns
- **Unit 52:** Boss sprites - large constructs
- **Unit 51:** Boss arena - fight area
- **Unit 52:** Boss health - damage tracking

### Units 53-56: Boss Patterns
- **Unit 53:** Attack phases - different modes
- **Unit 54:** Vulnerable windows - when to attack
- **Unit 55:** Pattern transitions - changing attacks
- **Unit 56:** Rage mode - low health aggression

### Units 57-60: Boss Variety
- **Unit 57:** Stage 1 boss - wall of guns
- **Unit 58:** Stage 2 boss - giant mech
- **Unit 59:** Stage 3 boss - alien creature
- **Unit 60:** Final boss - main antagonist

### Units 61-64: Boss Polish
- **Unit 61:** Boss music - intense theme
- **Unit 62:** Damage feedback - hit indication
- **Unit 63:** Boss death - explosion sequence
- **Unit 64:** Victory transition - stage complete

**Phase Goal:** Epic boss battles.

---

## Phase 5: Two-Player Mode (Units 65-80)
*Cooperative gameplay.*

### Units 65-68: Co-op Setup
- **Unit 65:** Two player objects - both active
- **Unit 66:** Separate inputs - two controllers
- **Unit 67:** Both on screen - shared view
- **Unit 68:** Life sharing - continue rules

### Units 69-72: Sprite Management
- **Unit 69:** Sprite allocation - dividing OAM
- **Unit 70:** Priority management - who shows
- **Unit 71:** Flickering strategy - fair display
- **Unit 72:** Performance - maintaining speed

### Units 73-76: Co-op Mechanics
- **Unit 73:** Friendly fire - off by default
- **Unit 74:** Shared continues - limited pool
- **Unit 75:** Score comparison - competitive scoring
- **Unit 76:** Respawn timing - rejoin flow

### Units 77-80: Co-op Balance
- **Unit 77:** Enemy scaling - more enemies
- **Unit 78:** Boss adjustments - harder with two
- **Unit 79:** Power-up priority - who gets pickup
- **Unit 80:** Balanced fun - both players engaged

**Phase Goal:** Full two-player cooperative.

---

## Phase 6: Level Variety (Units 81-96)
*Different level types.*

### Units 81-84: Side-Scroll Levels
- **Unit 81:** Jungle stage - outdoor terrain
- **Unit 82:** Base stage - indoor facility
- **Unit 83:** Waterfall stage - vertical elements
- **Unit 84:** Alien hive - organic environment

### Units 85-88: Base Levels (3D perspective)
- **Unit 85:** Base level concept - behind player
- **Unit 86:** Corridor rendering - pseudo-3D
- **Unit 87:** Enemy placement - in corridor
- **Unit 88:** Base boss - end of base

### Units 89-92: Level Flow
- **Unit 89:** Level transitions - stage changes
- **Unit 90:** Mid-boss encounters - mini-bosses
- **Unit 91:** Difficulty progression - harder stages
- **Unit 92:** Level variety - different challenges

### Units 93-96: Environmental Hazards
- **Unit 93:** Pits - instant death
- **Unit 94:** Fire - damage zones
- **Unit 95:** Crushers - timing hazards
- **Unit 96:** Water - drowning mechanic

**Phase Goal:** Varied level types.

---

## Phase 7: Polish (Units 97-112)
*Audio, effects, and presentation.*

### Units 97-100: Audio
- **Unit 97:** Weapon sounds - per weapon
- **Unit 98:** Explosion sounds - variety
- **Unit 99:** Stage music - per level
- **Unit 100:** Sound mixing - balanced audio

### Units 101-104: Visual Effects
- **Unit 101:** Explosions - multiple sizes
- **Unit 102:** Muzzle flash - weapon fire
- **Unit 103:** Screen shake - impact feedback
- **Unit 104:** Death effects - player/enemy

### Units 105-108: Presentation
- **Unit 105:** Title screen - game logo
- **Unit 106:** Stage intro - mission briefing
- **Unit 107:** Results screen - stage stats
- **Unit 108:** Ending sequence - victory

### Units 109-112: Game Modes
- **Unit 109:** 1-player mode - solo play
- **Unit 110:** 2-player mode - cooperative
- **Unit 111:** Difficulty settings - easy/normal/hard
- **Unit 112:** Options menu - settings

**Phase Goal:** Polished presentation.

---

## Phase 8: Release (Units 113-128)
*Final content and release.*

### Units 113-116: Extra Content
- **Unit 113:** Hidden weapons - secret guns
- **Unit 114:** Bonus stage - secret level
- **Unit 115:** Unlockables - extra features
- **Unit 116:** Score attack - high score mode

### Units 117-120: Balance
- **Unit 117:** Difficulty tuning - fair challenge
- **Unit 118:** Weapon balance - all viable
- **Unit 119:** Boss balance - challenging but fair
- **Unit 120:** Co-op balance - both players matter

### Units 121-124: Testing
- **Unit 121:** Single player testing
- **Unit 122:** Two player testing
- **Unit 123:** Edge cases - unusual situations
- **Unit 124:** Performance testing

### Units 125-128: Release
- **Unit 125:** Instructions screen
- **Unit 126:** Credits
- **Unit 127:** Final testing
- **Unit 128:** Release build - final iNES ROM

**Phase Goal:** Complete run'n'gun game.

---

## Summary

**Iron Assault** teaches combat-intensive action:

**Phases 1-2:** 8-way aiming, movement.
**Phases 3-4:** Weapons, bosses.
**Phases 5-6:** Co-op, level variety.
**Phases 7-8:** Polish, release.

### Game Specifications

- **Levels:** 8 stages
- **Player:** Commando, 8-way aim
- **Weapons:** 4 types
- **Enemies:** 15+ types
- **Bosses:** 1 per stage
- **Players:** 1-2 cooperative
- **Lives:** 3 each
- **Mapper:** MMC1
- **ROM Size:** 128KB PRG + 64KB CHR
- **Controls:** D-pad + A (fire) + B (jump)
- **Audio:** APU effects + music
- **Distribution:** iNES ROM file
