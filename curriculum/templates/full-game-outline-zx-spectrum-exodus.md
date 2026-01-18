# Game 10: Exodus - Complete 256-Unit Outline

## Game Overview
**Platform:** Sinclair ZX Spectrum
**Genre:** Scrolling platformer
**Concept:** Vast scrolling world with full platformer physics. Combines Blitz's software scrolling mastery with Cavern's platformer mechanics. Epic adventure across multiple themed worlds.

**Technical Focus:**
- Software scrolling + platformer physics
- Camera systems with dead zones
- Large level compression
- Scrolling collision detection
- Level streaming
- Attribute-aware scrolling

---

## Phase 1: Foundation (Units 1-16)
*Scrolling system setup*

Unit 1: Project setup for large game
Unit 2: Memory layout planning
Unit 3: Screen buffer configuration
Unit 4: Tile system design
Unit 5: 8x8 tile graphics
Unit 6: Tile map structure
Unit 7: Basic tile rendering
Unit 8: Pixel-level scroll concept
Unit 9: Character-level scroll
Unit 10: Combined scroll technique
Unit 11: Scroll buffer management
Unit 12: Initial scroll implementation
Unit 13: Scroll direction handling
Unit 14: Performance baseline
Unit 15: Attribute scroll basics
Unit 16: Phase 1 integration - basic scroll
**Runnable each unit**

---

## Phase 2: Scroll Optimisation (Units 17-32)
*High-performance scrolling*

Unit 17: Scroll profiling
Unit 18: Unrolled scroll loops
Unit 19: Self-modifying scroll
Unit 20: Stack-based scroll tricks
Unit 21: Column update system
Unit 22: Efficient column copy
Unit 23: Attribute column handling
Unit 24: Colour clash minimisation
Unit 25: Double buffer concept
Unit 26: Buffer switching
Unit 27: Contended memory timing
Unit 28: Non-contended optimisation
Unit 29: Smooth 8-pixel scroll
Unit 30: Sub-pixel positioning
Unit 31: Scroll polish
Unit 32: Phase 2 integration - fast scroll
**Runnable each unit**

---

## Phase 3: Player Core (Units 33-48)
*Platformer character*

Unit 33: Player sprite design
Unit 34: Animation frames (walk)
Unit 35: Animation frames (jump)
Unit 36: Sprite rendering system
Unit 37: Pre-shifted sprites
Unit 38: Sprite-background interaction
Unit 39: Basic movement input
Unit 40: Walking mechanics
Unit 41: Walk animation timing
Unit 42: Direction facing
Unit 43: Acceleration/deceleration
Unit 44: Movement feel tuning
Unit 45: Idle animation
Unit 46: Player state machine
Unit 47: State transitions
Unit 48: Phase 3 integration - animated player
**Runnable each unit**

---

## Phase 4: Physics (Units 49-64)
*Platformer physics*

Unit 49: Gravity concept
Unit 50: Fall speed
Unit 51: Terminal velocity
Unit 52: Air state tracking
Unit 53: Jump initiation
Unit 54: Jump velocity
Unit 55: Jump curve
Unit 56: Variable jump height
Unit 57: Jump release detection
Unit 58: Coyote time
Unit 59: Jump buffer
Unit 60: Landing detection
Unit 61: Land animation
Unit 62: Physics tuning
Unit 63: Feel refinement
Unit 64: Phase 4 integration - full physics
**Runnable each unit**

---

## Phase 5: Camera System (Units 65-80)
*World navigation*

Unit 65: Camera position tracking
Unit 66: World vs screen coordinates
Unit 67: Basic camera following
Unit 68: Dead zone concept
Unit 69: Horizontal dead zone
Unit 70: Dead zone tuning
Unit 71: Look-ahead
Unit 72: Vertical camera
Unit 73: Vertical dead zone
Unit 74: Camera smoothing
Unit 75: Camera bounds
Unit 76: Room/area transitions
Unit 77: Camera shake
Unit 78: Camera events
Unit 79: Camera polish
Unit 80: Phase 5 integration - smooth camera
**Runnable each unit**

---

## Phase 6: Level System (Units 81-96)
*World data*

Unit 81: Level data format design
Unit 82: Metatile system (2x2)
Unit 83: Metatile definitions
Unit 84: Level map storage
Unit 85: RLE compression
Unit 86: Decompression routine
Unit 87: Level streaming concept
Unit 88: Column decompression
Unit 89: Streaming implementation
Unit 90: Multi-screen levels
Unit 91: Level boundaries
Unit 92: Level loading
Unit 93: Level transitions
Unit 94: Level metadata
Unit 95: Level editor format
Unit 96: Phase 6 integration - streaming levels
**Runnable each unit**

---

## Phase 7: Collision (Units 97-112)
*World interaction*

Unit 97: Tile collision types
Unit 98: Solid tiles
Unit 99: Platform tiles (one-way)
Unit 100: Hazard tiles
Unit 101: Collision detection points
Unit 102: Ground detection
Unit 103: Wall detection
Unit 104: Ceiling detection
Unit 105: Scrolling collision mapping
Unit 106: World coordinate collision
Unit 107: Slope tiles
Unit 108: Slope physics
Unit 109: Moving platform detection
Unit 110: Platform riding
Unit 111: Collision optimisation
Unit 112: Phase 7 integration - world collision
**Runnable each unit**

---

## Phase 8: Enemies (Units 113-128)
*Hostile creatures*

Unit 113: Enemy system design
Unit 114: Enemy data structure
Unit 115: World position tracking
Unit 116: Active enemy management
Unit 117: Spawn/despawn system
Unit 118: Basic patrol enemy
Unit 119: Patrol AI
Unit 120: Edge detection
Unit 121: Flying enemy
Unit 122: Sine wave motion
Unit 123: Chasing enemy
Unit 124: Player tracking
Unit 125: Shooting enemy
Unit 126: Projectile system
Unit 127: Enemy variety
Unit 128: Phase 8 integration - enemy population
**Runnable each unit**

---

## Phase 9: Combat & Items (Units 129-144)
*Interaction systems*

Unit 129: Health system
Unit 130: Damage from enemies
Unit 131: Invincibility frames
Unit 132: Death state
Unit 133: Respawn system
Unit 134: Lives system
Unit 135: Attack/stomp mechanic
Unit 136: Enemy defeat
Unit 137: Collectible items
Unit 138: Coins/gems
Unit 139: Collection feedback
Unit 140: Power-ups
Unit 141: Health restore
Unit 142: Extra life
Unit 143: Score system
Unit 144: Phase 9 integration - combat complete
**Runnable each unit**

---

## Phase 10: Progression (Units 145-160)
*Game structure*

Unit 145: Checkpoint system
Unit 146: Checkpoint placement
Unit 147: Checkpoint activation
Unit 148: Respawn at checkpoint
Unit 149: Level exit/goal
Unit 150: Exit detection
Unit 151: Level completion
Unit 152: Inter-level screen
Unit 153: World map concept
Unit 154: World themes
Unit 155: World 1 - Grasslands
Unit 156: World 2 - Caves
Unit 157: World 3 - Factory
Unit 158: World 4 - Sky
Unit 159: World progression
Unit 160: Phase 10 integration - game progression
**Runnable each unit**

---

## Phase 11: Level Design (Units 161-176)
*Content creation*

Unit 161: World 1 Level 1
Unit 162: World 1 Level 2
Unit 163: World 1 Level 3
Unit 164: World 1 Boss area
Unit 165: World 2 Level 1
Unit 166: World 2 Level 2
Unit 167: World 2 Level 3
Unit 168: World 2 Boss area
Unit 169: World 3 Level 1
Unit 170: World 3 Level 2
Unit 171: World 3 Level 3
Unit 172: World 3 Boss area
Unit 173: World 4 Level 1
Unit 174: World 4 Level 2
Unit 175: World 4 Final level
Unit 176: Phase 11 integration - all levels
**Runnable each unit**

---

## Phase 12: Bosses (Units 177-192)
*Boss encounters*

Unit 177: Boss framework
Unit 178: Boss health system
Unit 179: Boss attack patterns
Unit 180: Boss 1 design
Unit 181: Boss 1 implementation
Unit 182: Boss 1 polish
Unit 183: Boss 2 design
Unit 184: Boss 2 implementation
Unit 185: Boss 3 design
Unit 186: Boss 3 implementation
Unit 187: Final boss design
Unit 188: Final boss phase 1
Unit 189: Final boss phase 2
Unit 190: Boss defeat sequence
Unit 191: Boss rewards
Unit 192: Phase 12 integration - all bosses
**Runnable each unit**

---

## Phase 13: Audio (Units 193-208)
*Sound and music*

Unit 193: AY-3-8910 setup
Unit 194: Sound effect system
Unit 195: Jump sound
Unit 196: Land sound
Unit 197: Collect sound
Unit 198: Damage sound
Unit 199: Enemy defeat sound
Unit 200: Death sound
Unit 201: Music system
Unit 202: Title music
Unit 203: World 1-2 music
Unit 204: World 3-4 music
Unit 205: Boss music
Unit 206: Victory music
Unit 207: Audio mixing
Unit 208: Phase 13 integration - full audio
**Runnable each unit**

---

## Phase 14: Polish (Units 209-224)
*Quality refinement*

Unit 209: Visual polish
Unit 210: Animation polish
Unit 211: Particle effects
Unit 212: Screen transitions
Unit 213: Gameplay feel tuning
Unit 214: Jump refinement
Unit 215: Difficulty balance
Unit 216: Enemy placement tuning
Unit 217: Checkpoint balance
Unit 218: Playtest session 1
Unit 219: Feedback integration 1
Unit 220: Playtest session 2
Unit 221: Feedback integration 2
Unit 222: Bug fixing
Unit 223: Edge cases
Unit 224: Phase 14 integration - polished
**Runnable each unit**

---

## Phase 15: Game Structure (Units 225-240)
*Complete package*

Unit 225: Title screen
Unit 226: Title animation
Unit 227: Main menu
Unit 228: Options menu
Unit 229: Difficulty settings
Unit 230: High score table
Unit 231: Name entry
Unit 232: Save/load (128K)
Unit 233: Password system (48K)
Unit 234: Ending sequence
Unit 235: Credits
Unit 236: Unlockables
Unit 237: Bonus content
Unit 238: Time attack mode
Unit 239: Boss rush mode
Unit 240: Phase 15 integration - complete structure
**Runnable each unit**

---

## Phase 16: Release (Units 241-256)
*Distribution*

Unit 241: Performance verification
Unit 242: 48K compatibility check
Unit 243: 128K features
Unit 244: Memory optimisation
Unit 245: Loading system
Unit 246: Multi-load structure
Unit 247: Tape mastering
Unit 248: Full testing
Unit 249: Regression testing
Unit 250: Hardware testing
Unit 251: Emulator testing
Unit 252: Documentation
Unit 253: Final fixes
Unit 254: Release build
Unit 255: Retrospective
Unit 256: Complete Exodus
**Runnable each unit**

---

## Technical Summary

### Key ZX Spectrum Features
- Optimised software scrolling
- Attribute-aware rendering
- Level compression/streaming
- Pre-shifted sprite system
- AY-3-8910 audio

### Code Pattern
```z80
; Camera dead zone
update_camera:
    ld a,(player_x)
    ld hl,camera_x
    sub (hl)
    cp DEAD_LEFT
    jr c,scroll_left
    cp DEAD_RIGHT
    jr nc,scroll_right
    ret
```

---

## Version History
- v1.0 - Initial 256-unit outline
