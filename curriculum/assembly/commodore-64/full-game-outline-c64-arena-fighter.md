# Game 12: Arena Fighter - Complete 256-Unit Outline

## Game Overview
**Platform:** Commodore 64
**Genre:** One-on-one fighting game
**Concept:** Street Fighter II-inspired fighter with four unique characters, special moves, combos, and tournament mode. Deep state machines and frame-perfect timing.

**Technical Focus:**
- Complex animation state machines
- Hitbox/hurtbox collision
- Frame data (startup, active, recovery)
- Motion input detection (QCF, DP)
- Input buffering
- AI opponent system

---

## Phase 1: Foundation (Units 1-16)
Unit 1: Project setup
Unit 2: Fighting game architecture
Unit 3: Display configuration
Unit 4: Arena background
Unit 5: Character sprite (large)
Unit 6: Idle animation
Unit 7: Character positioning
Unit 8: Two-player display
Unit 9: Health bar design
Unit 10: Health bar rendering
Unit 11: Timer display
Unit 12: Round indicator
Unit 13: Basic input reading
Unit 14: Player 2 input
Unit 15: VS screen layout
Unit 16: Phase 1 integration
**Runnable each unit**

---

## Phase 2: State Machine (Units 17-32)
Unit 17: State machine concept
Unit 18: State data structure
Unit 19: Idle state
Unit 20: Walk forward
Unit 21: Walk backward
Unit 22: Crouch state
Unit 23: Jump states
Unit 24: Jump arc physics
Unit 25: Landing state
Unit 26: State transitions
Unit 27: Input to state mapping
Unit 28: State priority
Unit 29: Animation per state
Unit 30: Frame timing
Unit 31: State debugging
Unit 32: Phase 2 integration
**Runnable each unit**

---

## Phase 3: Basic Attacks (Units 33-48)
Unit 33: Attack concept
Unit 34: Light punch
Unit 35: Medium punch
Unit 36: Heavy punch
Unit 37: Light kick
Unit 38: Medium kick
Unit 39: Heavy kick
Unit 40: Attack animation
Unit 41: Attack frame data
Unit 42: Startup frames
Unit 43: Active frames
Unit 44: Recovery frames
Unit 45: Crouching attacks
Unit 46: Jumping attacks
Unit 47: Attack priority
Unit 48: Phase 3 integration
**Runnable each unit**

---

## Phase 4: Hitbox System (Units 49-64)
Unit 49: Hitbox concept
Unit 50: Hurtbox concept
Unit 51: Hitbox data format
Unit 52: Per-frame hitboxes
Unit 53: Hitbox rendering (debug)
Unit 54: Collision detection
Unit 55: Hit registration
Unit 56: Damage application
Unit 57: Hitstun calculation
Unit 58: Blockstun concept
Unit 59: Standing block
Unit 60: Crouching block
Unit 61: Block detection
Unit 62: Push back
Unit 63: Trade hits
Unit 64: Phase 4 integration
**Runnable each unit**

---

## Phase 5: Advanced Movement (Units 65-80)
Unit 65: Dash forward
Unit 66: Dash backward
Unit 67: Dash animation
Unit 68: Dash cancel
Unit 69: Air control
Unit 70: Jump variations
Unit 71: Neutral jump
Unit 72: Forward jump
Unit 73: Back jump
Unit 74: Corner detection
Unit 75: Corner push
Unit 76: Throw range
Unit 77: Movement polish
Unit 78: Responsiveness tuning
Unit 79: Movement feel
Unit 80: Phase 5 integration
**Runnable each unit**

---

## Phase 6: Special Moves (Units 81-96)
Unit 81: Motion input concept
Unit 82: Input buffer
Unit 83: QCF detection (↓↘→)
Unit 84: QCB detection (↓↙←)
Unit 85: DP detection (→↓↘)
Unit 86: Charge detection
Unit 87: Special move data
Unit 88: Fireball (QCF+P)
Unit 89: Fireball projectile
Unit 90: Dragon punch (DP+P)
Unit 91: Invincibility frames
Unit 92: Hurricane kick (QCB+K)
Unit 93: Special priority
Unit 94: Special damage
Unit 95: Special recovery
Unit 96: Phase 6 integration
**Runnable each unit**

---

## Phase 7: Combo System (Units 97-112)
Unit 97: Combo concept
Unit 98: Cancel windows
Unit 99: Normal to special cancel
Unit 100: Chain combos
Unit 101: Link combos
Unit 102: Juggle state
Unit 103: Juggle limit
Unit 104: Combo counter
Unit 105: Combo display
Unit 106: Damage scaling
Unit 107: Hit confirm
Unit 108: Combo routes
Unit 109: Bread and butter combos
Unit 110: Max damage combo
Unit 111: Combo training
Unit 112: Phase 7 integration
**Runnable each unit**

---

## Phase 8: Super Moves (Units 113-128)
Unit 113: Super meter concept
Unit 114: Meter gain
Unit 115: Meter display
Unit 116: Super input (QCFx2+P)
Unit 117: Super flash
Unit 118: Super animation
Unit 119: Super damage
Unit 120: Super invincibility
Unit 121: Super combo
Unit 122: Meter management
Unit 123: EX moves concept
Unit 124: EX fireball
Unit 125: EX dragon punch
Unit 126: Meter strategy
Unit 127: Super polish
Unit 128: Phase 8 integration
**Runnable each unit**

---

## Phase 9: Character 1 (Units 129-144)
Unit 129: Shoto archetype design
Unit 130: Character 1 sprites
Unit 131: Idle and walk
Unit 132: All normals
Unit 133: Crouching normals
Unit 134: Jumping normals
Unit 135: Fireball special
Unit 136: Dragon punch special
Unit 137: Hurricane special
Unit 138: Super move
Unit 139: Throw animation
Unit 140: Win pose
Unit 141: Lose pose
Unit 142: Character balance
Unit 143: Combo routes
Unit 144: Phase 9 integration
**Runnable each unit**

---

## Phase 10: Characters 2-4 (Units 145-160)
Unit 145: Grappler archetype
Unit 146: Character 2 specials
Unit 147: Command grab
Unit 148: Character 2 complete
Unit 149: Charge archetype
Unit 150: Character 3 specials
Unit 151: Sonic boom type
Unit 152: Character 3 complete
Unit 153: Rushdown archetype
Unit 154: Character 4 specials
Unit 155: Rekka series
Unit 156: Character 4 complete
Unit 157: Character balance pass
Unit 158: Matchup testing
Unit 159: Character polish
Unit 160: Phase 10 integration
**Runnable each unit**

---

## Phase 11: AI Opponent (Units 161-176)
Unit 161: AI framework
Unit 162: AI states
Unit 163: Spacing awareness
Unit 164: Anti-air reactions
Unit 165: Block strings
Unit 166: Punish combos
Unit 167: Difficulty easy
Unit 168: Difficulty medium
Unit 169: Difficulty hard
Unit 170: AI adaptation
Unit 171: AI patterns
Unit 172: Per-character AI
Unit 173: AI exploits prevention
Unit 174: AI fairness
Unit 175: AI polish
Unit 176: Phase 11 integration
**Runnable each unit**

---

## Phase 12: Game Modes (Units 177-192)
Unit 177: Versus mode
Unit 178: Character select
Unit 179: Stage select
Unit 180: Arcade mode
Unit 181: Tournament bracket
Unit 182: Round system
Unit 183: Match win
Unit 184: Continue system
Unit 185: Training mode
Unit 186: Move list display
Unit 187: Input display
Unit 188: Hitbox viewer
Unit 189: Survival mode
Unit 190: Time attack
Unit 191: Records
Unit 192: Phase 12 integration
**Runnable each unit**

---

## Phase 13: Audio (Units 193-208)
Unit 193: SID setup
Unit 194: Hit sounds
Unit 195: Block sounds
Unit 196: Whiff sounds
Unit 197: Special move sounds
Unit 198: Super sounds
Unit 199: Announcer samples
Unit 200: Round call
Unit 201: Fight call
Unit 202: KO call
Unit 203: Music system
Unit 204: Character themes
Unit 205: Menu music
Unit 206: Victory music
Unit 207: Audio mixing
Unit 208: Phase 13 integration
**Runnable each unit**

---

## Phase 14: Polish (Units 209-224)
Unit 209: Visual effects
Unit 210: Hit sparks
Unit 211: Block sparks
Unit 212: Super effects
Unit 213: Screen shake
Unit 214: Slow motion (KO)
Unit 215: Animation polish
Unit 216: Gameplay feel
Unit 217: Input responsiveness
Unit 218: Balance tuning
Unit 219: Playtest 1
Unit 220: Feedback integration
Unit 221: Playtest 2
Unit 222: Final balance
Unit 223: Bug fixes
Unit 224: Phase 14 integration
**Runnable each unit**

---

## Phase 15: Structure (Units 225-240)
Unit 225: Title screen
Unit 226: Title animation
Unit 227: Main menu
Unit 228: Options
Unit 229: Button config
Unit 230: Difficulty select
Unit 231: Story scenes
Unit 232: Endings
Unit 233: Credits
Unit 234: High scores
Unit 235: Unlock system
Unit 236: Gallery mode
Unit 237: Sound test
Unit 238: Attract mode
Unit 239: Demo fight
Unit 240: Phase 15 integration
**Runnable each unit**

---

## Phase 16: Release (Units 241-256)
Unit 241: Performance check
Unit 242: Memory verify
Unit 243: Full testing
Unit 244: All characters test
Unit 245: All modes test
Unit 246: Two-player test
Unit 247: AI testing
Unit 248: D64 mastering
Unit 249: Documentation
Unit 250: Move list
Unit 251: Release candidate
Unit 252: Final verification
Unit 253: Release
Unit 254: Retrospective
Unit 255: Fighting game mastery
Unit 256: Complete Arena Fighter
**Runnable each unit**

---

## Technical Summary

### Key C64 Features
- Complex state machines
- Hitbox/hurtbox system
- Motion input detection
- Frame-perfect timing
- Multi-character support

### Code Pattern
```asm
; QCF motion detection
check_qcf:
    ldx input_buffer_pos
    lda input_history-2,x  ; 2 frames ago
    cmp #JOY_DOWN
    bne .fail
    lda input_history-1,x  ; 1 frame ago
    cmp #JOY_DOWNRIGHT
    bne .fail
    lda input_history,x    ; Current
    cmp #JOY_RIGHT
    bne .fail
    lda #1                 ; QCF detected
    rts
.fail:
    lda #0
    rts
```

---

## Version History
- v1.0 - Initial 256-unit outline
