# Game 13: Parallax Patrol - Complete 256-Unit Outline

## Game Overview
**Platform:** Commodore 64
**Genre:** Side-scrolling shooter
**Concept:** R-Type/Gradius-style horizontal shooter with multi-layer parallax scrolling, option drones, charge shots, and epic boss battles. Advanced VIC-II techniques for smooth scrolling with multiple speed layers.

**Technical Focus:**
- Multi-layer parallax scrolling (3+ layers)
- Advanced sprite multiplexing for heavy action
- Option drone following algorithms
- Charge shot mechanics
- Complex bullet patterns
- Level compression and streaming

---

## Phase 1: Foundation (Units 1-16)
Unit 1: Project setup
Unit 2: Memory layout for large shooter
Unit 3: Display configuration
Unit 4: Single-layer scroll setup
Unit 5: Hardware scroll registers
Unit 6: Fine/coarse scroll coordination
Unit 7: Colour RAM scrolling
Unit 8: Player ship sprite
Unit 9: Ship positioning
Unit 10: Basic movement
Unit 11: Screen bounds
Unit 12: Ship animation
Unit 13: Engine glow effect
Unit 14: Banking animation
Unit 15: Ship feel tuning
Unit 16: Phase 1 integration
**Runnable each unit**

---

## Phase 2: Parallax System (Units 17-32)
Unit 17: Parallax concept
Unit 18: Layer speed ratios
Unit 19: Far background layer
Unit 20: Mid background layer
Unit 21: Near background layer
Unit 22: Foreground layer
Unit 23: Layer synchronisation
Unit 24: Raster splits for layers
Unit 25: Colour per layer
Unit 26: Layer tile sets
Unit 27: Seamless layer scroll
Unit 28: Performance budgeting
Unit 29: Layer priorities
Unit 30: Visual depth tuning
Unit 31: Parallax polish
Unit 32: Phase 2 integration
**Runnable each unit**

---

## Phase 3: Weapons (Units 33-48)
Unit 33: Weapon framework
Unit 34: Default shot
Unit 35: Bullet sprites
Unit 36: Bullet pool
Unit 37: Fire rate control
Unit 38: Rapid fire
Unit 39: Power-up capsules
Unit 40: Capsule collection
Unit 41: Spread shot (S)
Unit 42: Spread pattern
Unit 43: Laser beam (L)
Unit 44: Laser rendering
Unit 45: Wave shot (W)
Unit 46: Sine wave bullets
Unit 47: Weapon switching
Unit 48: Phase 3 integration
**Runnable each unit**

---

## Phase 4: Charge Shot (Units 49-64)
Unit 49: Charge concept
Unit 50: Charge meter
Unit 51: Charge accumulation
Unit 52: Charge levels
Unit 53: Level 1 charge shot
Unit 54: Level 2 charge shot
Unit 55: Level 3 mega shot
Unit 56: Charge sprites
Unit 57: Charge sound
Unit 58: Release timing
Unit 59: Charge while moving
Unit 60: Charge interruption
Unit 61: Visual feedback
Unit 62: Charge strategy
Unit 63: Charge balance
Unit 64: Phase 4 integration
**Runnable each unit**

---

## Phase 5: Options (Units 65-80)
Unit 65: Option concept
Unit 66: Option sprite
Unit 67: Position history buffer
Unit 68: Following algorithm
Unit 69: Option delay tuning
Unit 70: Single option
Unit 71: Two options
Unit 72: Maximum options (4)
Unit 73: Option firing
Unit 74: Option formations
Unit 75: Formation - Trail
Unit 76: Formation - Spread
Unit 77: Formation - Rotate
Unit 78: Formation switching
Unit 79: Option collision
Unit 80: Phase 5 integration
**Runnable each unit**

---

## Phase 6: Enemies (Units 81-96)
Unit 81: Enemy framework
Unit 82: Enemy data structure
Unit 83: Spawn system
Unit 84: Wave spawning
Unit 85: Formation patterns
Unit 86: V-formation
Unit 87: Line formation
Unit 88: Circle formation
Unit 89: Dive bomber
Unit 90: Straight shooter
Unit 91: Aimed shooter
Unit 92: Turret enemy
Unit 93: Large enemy
Unit 94: Enemy bullets
Unit 95: Bullet patterns
Unit 96: Phase 6 integration
**Runnable each unit**

---

## Phase 7: Level System (Units 97-112)
Unit 97: Level data format
Unit 98: RLE compression
Unit 99: Decompression routine
Unit 100: Tile streaming
Unit 101: Enemy spawn data
Unit 102: Spawn triggers
Unit 103: Terrain collision
Unit 104: Destructible terrain
Unit 105: Level sections
Unit 106: Section transitions
Unit 107: Speed variations
Unit 108: Auto-scroll sections
Unit 109: Checkpoint markers
Unit 110: Level metadata
Unit 111: Level flow
Unit 112: Phase 7 integration
**Runnable each unit**

---

## Phase 8: Bosses (Units 113-128)
Unit 113: Boss framework
Unit 114: Boss arena setup
Unit 115: Scroll lock
Unit 116: Boss health bar
Unit 117: Multi-sprite boss
Unit 118: Boss 1 design
Unit 119: Boss 1 patterns
Unit 120: Boss 1 phases
Unit 121: Weak point system
Unit 122: Part destruction
Unit 123: Boss explosions
Unit 124: Boss defeat sequence
Unit 125: Boss rewards
Unit 126: Boss music trigger
Unit 127: Boss polish
Unit 128: Phase 8 integration
**Runnable each unit**

---

## Phase 9: Stage 1-2 (Units 129-144)
Unit 129: Stage 1 - Space theme
Unit 130: Stage 1 parallax layers
Unit 131: Stage 1 enemy waves
Unit 132: Stage 1 mid-boss
Unit 133: Stage 1 boss
Unit 134: Stage 1 complete
Unit 135: Stage 2 - Asteroid field
Unit 136: Stage 2 parallax
Unit 137: Stage 2 hazards
Unit 138: Stage 2 enemy waves
Unit 139: Stage 2 mid-boss
Unit 140: Stage 2 boss
Unit 141: Stage 2 complete
Unit 142: Stage transition
Unit 143: Difficulty scaling
Unit 144: Phase 9 integration
**Runnable each unit**

---

## Phase 10: Stage 3-4 (Units 145-160)
Unit 145: Stage 3 - Mechanical base
Unit 146: Stage 3 parallax
Unit 147: Stage 3 turrets
Unit 148: Stage 3 enemy waves
Unit 149: Stage 3 mid-boss
Unit 150: Stage 3 boss
Unit 151: Stage 3 complete
Unit 152: Stage 4 - Organic cavern
Unit 153: Stage 4 parallax
Unit 154: Stage 4 hazards
Unit 155: Stage 4 enemy waves
Unit 156: Stage 4 mid-boss
Unit 157: Stage 4 boss
Unit 158: Stage 4 complete
Unit 159: Stage variety
Unit 160: Phase 10 integration
**Runnable each unit**

---

## Phase 11: Stage 5-7 (Units 161-176)
Unit 161: Stage 5 - Fire zone
Unit 162: Stage 5 hazards
Unit 163: Stage 5 boss
Unit 164: Stage 6 - Ice cavern
Unit 165: Stage 6 hazards
Unit 166: Stage 6 boss
Unit 167: Stage 7 - Final fortress
Unit 168: Stage 7 gauntlet
Unit 169: Final boss arena
Unit 170: Final boss phase 1
Unit 171: Final boss phase 2
Unit 172: Final boss phase 3
Unit 173: Final boss defeat
Unit 174: Ending sequence
Unit 175: Credits roll
Unit 176: Phase 11 integration
**Runnable each unit**

---

## Phase 12: Game Systems (Units 177-192)
Unit 177: Lives system
Unit 178: Continue system
Unit 179: Score system
Unit 180: High scores
Unit 181: Rank system
Unit 182: Difficulty modes
Unit 183: Easy mode
Unit 184: Normal mode
Unit 185: Hard mode
Unit 186: Second loop
Unit 187: True ending
Unit 188: Checkpoint respawn
Unit 189: Power-up retention
Unit 190: Death penalty
Unit 191: Balance tuning
Unit 192: Phase 12 integration
**Runnable each unit**

---

## Phase 13: Two-Player (Units 193-208)
Unit 193: Two-player concept
Unit 194: Player 2 ship
Unit 195: Controller 2 input
Unit 196: Both ships active
Unit 197: Sprite allocation
Unit 198: Shared screen
Unit 199: Cooperative scoring
Unit 200: Shared power-ups
Unit 201: Individual options
Unit 202: Revive mechanic
Unit 203: Two-player balance
Unit 204: Alternating mode
Unit 205: Versus mode
Unit 206: Two-player bosses
Unit 207: Two-player polish
Unit 208: Phase 13 integration
**Runnable each unit**

---

## Phase 14: Audio (Units 209-224)
Unit 209: SID setup
Unit 210: Weapon sounds
Unit 211: Explosion sounds
Unit 212: Power-up sounds
Unit 213: Charge sound
Unit 214: Boss warning
Unit 215: Music driver
Unit 216: Title music
Unit 217: Stage 1-2 music
Unit 218: Stage 3-4 music
Unit 219: Stage 5-7 music
Unit 220: Boss music
Unit 221: Victory fanfare
Unit 222: Game over music
Unit 223: Audio mixing
Unit 224: Phase 14 integration
**Runnable each unit**

---

## Phase 15: Polish (Units 225-240)
Unit 225: Visual effects
Unit 226: Explosion variety
Unit 227: Muzzle flash
Unit 228: Hit sparks
Unit 229: Screen shake
Unit 230: Death animations
Unit 231: Gameplay feel
Unit 232: Weapon balance
Unit 233: Enemy balance
Unit 234: Boss balance
Unit 235: Difficulty curve
Unit 236: Playtest 1
Unit 237: Feedback integration
Unit 238: Playtest 2
Unit 239: Bug fixes
Unit 240: Phase 15 integration
**Runnable each unit**

---

## Phase 16: Release (Units 241-256)
Unit 241: Title screen
Unit 242: Title animation
Unit 243: Main menu
Unit 244: Options screen
Unit 245: High score entry
Unit 246: Attract mode
Unit 247: Demo play
Unit 248: Performance verify
Unit 249: Memory check
Unit 250: D64 mastering
Unit 251: Documentation
Unit 252: Final testing
Unit 253: Release candidate
Unit 254: Retrospective
Unit 255: Parallax mastery
Unit 256: Complete Parallax Patrol
**Runnable each unit**

---

## Technical Summary

### Key C64 Features
- Multi-layer parallax scrolling
- Advanced sprite multiplexing
- Option following algorithm
- Charge shot mechanics
- RLE level compression

### Code Pattern
```asm
; Option following with position history
update_option:
    ldx option_delay        ; Frames of delay
    lda player_x_history,x  ; Get delayed position
    sta option_x
    lda player_y_history,x
    sta option_y
    ; Shift history buffer
    ldx #HISTORY_SIZE-1
.shift:
    lda player_x_history-1,x
    sta player_x_history,x
    dex
    bne .shift
    rts
```

---

## Version History
- v1.0 - Initial 256-unit outline
