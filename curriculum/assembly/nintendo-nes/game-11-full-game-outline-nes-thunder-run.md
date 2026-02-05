# Game 11: Thunder Run - Complete 256-Unit Outline

## Game Overview
**Platform:** Nintendo Entertainment System
**Genre:** Vertical scrolling shooter
**Concept:** 1942-style military shooter with formations, power-ups, and epic boss battles. Introduces MMC1 mapper for expanded ROM and CHR banking.

**Technical Focus:**
- Vertical scrolling
- Formation enemy patterns
- Bullet patterns
- **MMC1 mapper basics**
- **Extended CHR banks**
- **PRG bank switching**

---

## Phase 1: Foundation (Units 1-16)
Unit 1: Project setup with MMC1
Unit 2: Mapper configuration
Unit 3: Bank layout planning
Unit 4: Display setup
Unit 5: Vertical scroll basics
Unit 6: Scroll register usage
Unit 7: Nametable for vertical
Unit 8: Row loading
Unit 9: Player plane sprite
Unit 10: Plane animation
Unit 11: 8-way movement
Unit 12: Screen bounds
Unit 13: Basic shooting
Unit 14: Bullet sprites
Unit 15: Simple enemy
Unit 16: Phase 1 integration
**Runnable each unit**

---

## Phase 2: Mapper Fundamentals (Units 17-32)
Unit 17: **MMC1 overview**
Unit 18: **Control register**
Unit 19: **CHR bank 0 register**
Unit 20: **CHR bank 1 register**
Unit 21: **PRG bank register**
Unit 22: **Serial writing**
Unit 23: **Bank switch routine**
Unit 24: **CHR bank switching**
Unit 25: **Animated tiles via CHR**
Unit 26: **Multiple tilesets**
Unit 27: **PRG bank switching**
Unit 28: **Code in switchable bank**
Unit 29: **Data in switchable bank**
Unit 30: **Fixed bank usage**
Unit 31: **Mapper stability**
Unit 32: Phase 2 integration
**Runnable each unit**

---

## Phase 3: Scrolling System (Units 33-48)
Unit 33: Vertical scroll mechanics
Unit 34: Row streaming
Unit 35: Level data format
Unit 36: Metatile system
Unit 37: Row decompression
Unit 38: Attribute updates
Unit 39: Smooth scrolling
Unit 40: Scroll speed control
Unit 41: Variable scroll
Unit 42: Scroll pause (boss)
Unit 43: Level structure
Unit 44: Section markers
Unit 45: Level length
Unit 46: Level transitions
Unit 47: Scroll polish
Unit 48: Phase 3 integration
**Runnable each unit**

---

## Phase 4: Player System (Units 49-64)
Unit 49: Player controls
Unit 50: Movement speed
Unit 51: Screen position
Unit 52: Plane banking animation
Unit 53: Shooting system
Unit 54: Fire rate
Unit 55: Shot types
Unit 56: Shot spread
Unit 57: Bomb system
Unit 58: Bomb drop
Unit 59: Bomb explosion
Unit 60: Bomb limits
Unit 61: Player hitbox
Unit 62: Death handling
Unit 63: Respawn
Unit 64: Phase 4 integration
**Runnable each unit**

---

## Phase 5: Enemies (Units 65-80)
Unit 65: Enemy framework
Unit 66: Enemy spawning
Unit 67: Small plane
Unit 68: Medium plane
Unit 69: Large plane
Unit 70: Formation patterns
Unit 71: V-formation
Unit 72: Line formation
Unit 73: Circle formation
Unit 74: Dive attack
Unit 75: Ground targets
Unit 76: Turrets
Unit 77: Tanks
Unit 78: Ships
Unit 79: Enemy variety
Unit 80: Phase 5 integration
**Runnable each unit**

---

## Phase 6: Bullets & Patterns (Units 81-96)
Unit 81: Enemy bullet system
Unit 82: Aimed shots
Unit 83: Spread shots
Unit 84: Burst patterns
Unit 85: Spiral patterns
Unit 86: Wall patterns
Unit 87: Random patterns
Unit 88: Bullet speed variety
Unit 89: Bullet limits
Unit 90: Bullet pooling
Unit 91: Bullet collision
Unit 92: Graze system
Unit 93: Bullet cancelling
Unit 94: Pattern balance
Unit 95: Pattern variety
Unit 96: Phase 6 integration
**Runnable each unit**

---

## Phase 7: Power-Ups (Units 97-112)
Unit 97: Power-up framework
Unit 98: Power-up drops
Unit 99: P - Power up
Unit 100: Shot upgrade levels
Unit 101: S - Speed up
Unit 102: Speed levels
Unit 103: B - Bomb refill
Unit 104: L - Laser weapon
Unit 105: W - Wide shot
Unit 106: H - Homing missiles
Unit 107: Weapon switching
Unit 108: Power-up carrier
Unit 109: Formation bonus
Unit 110: Score items
Unit 111: Power balance
Unit 112: Phase 7 integration
**Runnable each unit**

---

## Phase 8: Levels (Units 113-128)
Unit 113: Level 1 - Ocean
Unit 114: Level 1 layout
Unit 115: Level 1 enemies
Unit 116: Level 2 - Jungle
Unit 117: Level 2 layout
Unit 118: Level 3 - Desert
Unit 119: Level 3 layout
Unit 120: Level 4 - Mountains
Unit 121: Level 4 layout
Unit 122: Level 5 - Enemy base
Unit 123: Level 5 layout
Unit 124: Level variety
Unit 125: CHR banks per level
Unit 126: Level themes
Unit 127: Level polish
Unit 128: Phase 8 integration
**Runnable each unit**

---

## Phase 9: Bosses (Units 129-144)
Unit 129: Boss framework
Unit 130: Large sprite bosses
Unit 131: Boss health
Unit 132: Boss patterns
Unit 133: Boss 1 - Battleship
Unit 134: Boss 1 attacks
Unit 135: Boss 2 - Giant plane
Unit 136: Boss 2 attacks
Unit 137: Boss 3 - Fortress
Unit 138: Boss 3 attacks
Unit 139: Boss 4 - Carrier
Unit 140: Boss 4 attacks
Unit 141: Final boss design
Unit 142: Final boss phases
Unit 143: Boss defeat
Unit 144: Phase 9 integration
**Runnable each unit**

---

## Phase 10: Audio (Units 145-160)
Unit 145: APU setup
Unit 146: Sound effect system
Unit 147: Shoot sound
Unit 148: Explosion small
Unit 149: Explosion large
Unit 150: Power-up sound
Unit 151: Player death
Unit 152: Boss warning
Unit 153: Music driver
Unit 154: Title music
Unit 155: Stage 1-2 music
Unit 156: Stage 3-4 music
Unit 157: Stage 5 music
Unit 158: Boss music
Unit 159: Victory music
Unit 160: Phase 10 integration
**Runnable each unit**

---

## Phase 11: Game Systems (Units 161-176)
Unit 161: Lives system
Unit 162: Continue system
Unit 163: Score system
Unit 164: High score
Unit 165: Rank system
Unit 166: Difficulty scaling
Unit 167: Two-player mode
Unit 168: Alternating play
Unit 169: Score comparison
Unit 170: Extends (extra lives)
Unit 171: Loop 2 harder
Unit 172: True ending
Unit 173: Secrets
Unit 174: Hidden bonuses
Unit 175: Achievements
Unit 176: Phase 11 integration
**Runnable each unit**

---

## Phase 12: Polish (Units 177-192)
Unit 177: Visual polish
Unit 178: Explosion variety
Unit 179: Death animations
Unit 180: Background detail
Unit 181: Parallax tricks
Unit 182: Sprite priorities
Unit 183: Flicker management
Unit 184: Gameplay feel
Unit 185: Hit feedback
Unit 186: Power-up feel
Unit 187: Balance pass
Unit 188: Difficulty tuning
Unit 189: Playtest 1
Unit 190: Feedback integration
Unit 191: Playtest 2
Unit 192: Phase 12 integration
**Runnable each unit**

---

## Phase 13: Structure (Units 193-208)
Unit 193: Title screen
Unit 194: Title animation
Unit 195: Plane demo
Unit 196: Menu system
Unit 197: Mode select
Unit 198: Difficulty select
Unit 199: Options
Unit 200: High scores
Unit 201: Name entry
Unit 202: Instructions
Unit 203: Credits
Unit 204: Attract mode
Unit 205: Demo play
Unit 206: Ending sequence
Unit 207: Staff roll
Unit 208: Phase 13 integration
**Runnable each unit**

---

## Phase 14: Testing (Units 209-224)
Unit 209: Full playthrough
Unit 210: All levels test
Unit 211: All bosses test
Unit 212: All weapons test
Unit 213: Two-player test
Unit 214: Mapper stability
Unit 215: Bank switch verify
Unit 216: Memory testing
Unit 217: Long session
Unit 218: Edge cases
Unit 219: Regression
Unit 220: Hardware testing
Unit 221: Emulator testing
Unit 222: Final fixes
Unit 223: Performance verify
Unit 224: Phase 14 integration
**Runnable each unit**

---

## Phase 15: Distribution (Units 225-240)
Unit 225: ROM finalisation
Unit 226: Mapper header
Unit 227: Bank verification
Unit 228: CRC check
Unit 229: Documentation
Unit 230: Controls guide
Unit 231: Enemy guide
Unit 232: Manual content
Unit 233: Final testing
Unit 234: Release candidate
Unit 235: Version number
Unit 236: Distribution prep
Unit 237: Community release
Unit 238: Support
Unit 239: Patch planning
Unit 240: Phase 15 integration
**Runnable each unit**

---

## Phase 16: Release (Units 241-256)
Unit 241: Final ROM
Unit 242: Cartridge specs
Unit 243: Label design
Unit 244: Box concept
Unit 245: Complete package
Unit 246: Final verification
Unit 247: Release
Unit 248: Post-release
Unit 249: Community feedback
Unit 250: Retrospective
Unit 251: Mapper mastery
Unit 252: Shmup techniques
Unit 253: Skills summary
Unit 254: Future projects
Unit 255: Knowledge sharing
Unit 256: Complete Thunder Run
**Runnable each unit**

---

## Technical Summary

### Key NES Features
- Vertical scrolling
- Formation patterns
- Bullet systems
- **MMC1 mapper**
- **CHR bank switching**
- **PRG bank switching**

### Code Pattern
```asm
; MMC1 bank switch (serial write)
mmc1_write:
    ; Write bit 0
    sta MMC1_REG
    lsr a
    ; Write bit 1
    sta MMC1_REG
    lsr a
    ; Write bit 2
    sta MMC1_REG
    lsr a
    ; Write bit 3
    sta MMC1_REG
    lsr a
    ; Write bit 4 (triggers)
    sta MMC1_REG
    rts
```

---

## Version History
- v1.0 - Initial 256-unit outline
