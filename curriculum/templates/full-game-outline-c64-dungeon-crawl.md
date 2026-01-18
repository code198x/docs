# Game 11: Dungeon Crawl - Complete 256-Unit Outline

## Game Overview
**Platform:** Commodore 64
**Genre:** Top-down adventure/RPG
**Concept:** Zelda-style dungeon exploration with inventory, NPCs, quests, and combat. Introduces C64 disk I/O for save games. Multi-room architecture with puzzles, keys, and boss encounters.

**Technical Focus:**
- Multi-room map architecture
- Inventory and item system
- NPC dialogue system
- Quest/objective tracking
- Combat mechanics
- **Disk I/O fundamentals**
- **Save/load system**

---

## Phase 1: Foundation (Units 1-16)
Unit 1: Project setup
Unit 2: Memory layout for large game
Unit 3: Display configuration
Unit 4: Character set design
Unit 5: Tile system (8x8)
Unit 6: Room grid layout
Unit 7: Single room display
Unit 8: Tile types
Unit 9: Player sprite
Unit 10: 4-direction animation
Unit 11: Basic movement
Unit 12: Tile collision
Unit 13: Room boundaries
Unit 14: Screen rendering
Unit 15: Performance baseline
Unit 16: Phase 1 integration
**Runnable each unit**

---

## Phase 2: Room System (Units 17-32)
Unit 17: Room data structure
Unit 18: Room storage format
Unit 19: Multi-room map
Unit 20: Room connections
Unit 21: Door tiles
Unit 22: Room transitions
Unit 23: Transition animation
Unit 24: Player position on transition
Unit 25: Room state tracking
Unit 26: Persistent room changes
Unit 27: Room memory management
Unit 28: Map layout design
Unit 29: Dungeon structure
Unit 30: Multiple dungeon levels
Unit 31: Stairs/ladders
Unit 32: Phase 2 integration
**Runnable each unit**

---

## Phase 3: Inventory (Units 33-48)
Unit 33: Inventory data structure
Unit 34: Item definitions
Unit 35: Key items
Unit 36: Consumables
Unit 37: Equipment
Unit 38: Item collection
Unit 39: Inventory display
Unit 40: Item selection
Unit 41: Item use
Unit 42: Key/door system
Unit 43: Multiple key types
Unit 44: Item dropping
Unit 45: Item limits
Unit 46: Equipment effects
Unit 47: Inventory polish
Unit 48: Phase 3 integration
**Runnable each unit**

---

## Phase 4: NPCs & Dialogue (Units 49-64)
Unit 49: NPC data structure
Unit 50: NPC sprites
Unit 51: NPC placement
Unit 52: NPC states
Unit 53: Dialogue system design
Unit 54: Text display
Unit 55: Dialogue boxes
Unit 56: Multiple responses
Unit 57: Branching dialogue
Unit 58: NPC movement
Unit 59: Patrol patterns
Unit 60: Shopkeeper NPCs
Unit 61: Buy/sell system
Unit 62: Quest-giver NPCs
Unit 63: Dialogue flags
Unit 64: Phase 4 integration
**Runnable each unit**

---

## Phase 5: Quest System (Units 65-80)
Unit 65: Quest data structure
Unit 66: Quest states
Unit 67: Objective tracking
Unit 68: Quest items
Unit 69: Quest triggers
Unit 70: Quest completion
Unit 71: Quest rewards
Unit 72: Multiple active quests
Unit 73: Main quest line
Unit 74: Side quests
Unit 75: Quest log display
Unit 76: Quest hints
Unit 77: Quest dependencies
Unit 78: Story progression
Unit 79: Quest polish
Unit 80: Phase 5 integration
**Runnable each unit**

---

## Phase 6: Combat (Units 81-96)
Unit 81: Combat design
Unit 82: Player attack
Unit 83: Sword swing
Unit 84: Attack animation
Unit 85: Attack hitbox
Unit 86: Enemy types
Unit 87: Enemy AI
Unit 88: Enemy attacks
Unit 89: Damage system
Unit 90: Health display
Unit 91: Player death
Unit 92: Respawn system
Unit 93: Enemy respawn
Unit 94: Combat feedback
Unit 95: Combat balance
Unit 96: Phase 6 integration
**Runnable each unit**

---

## Phase 7: Puzzles (Units 97-112)
Unit 97: Puzzle types
Unit 98: Push blocks
Unit 99: Pressure plates
Unit 100: Switch doors
Unit 101: Hidden passages
Unit 102: Bombable walls
Unit 103: Light puzzles
Unit 104: Sequence puzzles
Unit 105: Timed puzzles
Unit 106: Multi-room puzzles
Unit 107: Puzzle state saving
Unit 108: Puzzle reset
Unit 109: Puzzle hints
Unit 110: Puzzle rewards
Unit 111: Puzzle variety
Unit 112: Phase 7 integration
**Runnable each unit**

---

## Phase 8: Disk I/O (Units 113-128)
Unit 113: **Kernal disk routines**
Unit 114: **Opening files**
Unit 115: **Reading files**
Unit 116: **Writing files**
Unit 117: **Closing files**
Unit 118: **Error handling**
Unit 119: **Save game design**
Unit 120: **Game state serialisation**
Unit 121: **Save to disk**
Unit 122: **Load from disk**
Unit 123: **Multiple save slots**
Unit 124: **Save verification**
Unit 125: **D64 disk image creation**
Unit 126: **Disk-based level loading**
Unit 127: Password backup (no disk)
Unit 128: Phase 8 integration
**Runnable each unit**

---

## Phase 9: World Design (Units 129-144)
Unit 129: Overworld design
Unit 130: Town area
Unit 131: Forest area
Unit 132: Mountain area
Unit 133: Dungeon 1 layout
Unit 134: Dungeon 1 rooms
Unit 135: Dungeon 1 puzzles
Unit 136: Dungeon 2 layout
Unit 137: Dungeon 2 rooms
Unit 138: Dungeon 3 layout
Unit 139: Dungeon 3 rooms
Unit 140: Secret areas
Unit 141: Optional content
Unit 142: World connections
Unit 143: Fast travel
Unit 144: Phase 9 integration
**Runnable each unit**

---

## Phase 10: Bosses (Units 145-160)
Unit 145: Boss framework
Unit 146: Boss health
Unit 147: Boss patterns
Unit 148: Boss 1 design
Unit 149: Boss 1 attacks
Unit 150: Boss 1 implementation
Unit 151: Boss 2 design
Unit 152: Boss 2 implementation
Unit 153: Boss 3 design
Unit 154: Boss 3 implementation
Unit 155: Final boss design
Unit 156: Final boss phase 1
Unit 157: Final boss phase 2
Unit 158: Boss rewards
Unit 159: Boss polish
Unit 160: Phase 10 integration
**Runnable each unit**

---

## Phase 11: Items & Equipment (Units 161-176)
Unit 161: Weapon variety
Unit 162: Weapon upgrades
Unit 163: Shield items
Unit 164: Armour system
Unit 165: Magic items
Unit 166: Health potions
Unit 167: Special items
Unit 168: Dungeon items (map, compass)
Unit 169: Heart containers
Unit 170: Item shops
Unit 171: Hidden items
Unit 172: Rare drops
Unit 173: Equipment stats
Unit 174: Item balance
Unit 175: Collection tracking
Unit 176: Phase 11 integration
**Runnable each unit**

---

## Phase 12: Audio (Units 177-192)
Unit 177: SID setup
Unit 178: Sound effects
Unit 179: Attack sound
Unit 180: Damage sound
Unit 181: Item collect
Unit 182: Door open
Unit 183: Puzzle solve
Unit 184: Music system
Unit 185: Overworld music
Unit 186: Dungeon music
Unit 187: Town music
Unit 188: Boss music
Unit 189: Victory fanfare
Unit 190: Game over
Unit 191: Audio mixing
Unit 192: Phase 12 integration
**Runnable each unit**

---

## Phase 13: Polish (Units 193-208)
Unit 193: Visual polish
Unit 194: Animation polish
Unit 195: Transition effects
Unit 196: Screen effects
Unit 197: Dialogue polish
Unit 198: Combat feel
Unit 199: Puzzle balance
Unit 200: Quest flow
Unit 201: Difficulty tuning
Unit 202: Playtest 1
Unit 203: Feedback integration
Unit 204: Playtest 2
Unit 205: Bug fixes
Unit 206: Edge cases
Unit 207: Performance
Unit 208: Phase 13 integration
**Runnable each unit**

---

## Phase 14: Game Structure (Units 209-224)
Unit 209: Title screen
Unit 210: Title music
Unit 211: File select
Unit 212: New game
Unit 213: Continue game
Unit 214: Options menu
Unit 215: Control config
Unit 216: Intro sequence
Unit 217: Story scenes
Unit 218: Ending sequence
Unit 219: Credits
Unit 220: Completion percentage
Unit 221: Second quest
Unit 222: Unlockables
Unit 223: New Game+
Unit 224: Phase 14 integration
**Runnable each unit**

---

## Phase 15: Testing (Units 225-240)
Unit 225: Full playthrough
Unit 226: All quests test
Unit 227: All items test
Unit 228: All puzzles test
Unit 229: All bosses test
Unit 230: Save/load testing
Unit 231: Disk error handling
Unit 232: Long session test
Unit 233: Memory stability
Unit 234: Edge cases
Unit 235: Regression testing
Unit 236: Balance testing
Unit 237: Emulator testing
Unit 238: Real hardware
Unit 239: Final fixes
Unit 240: Phase 15 integration
**Runnable each unit**

---

## Phase 16: Release (Units 241-256)
Unit 241: D64 mastering
Unit 242: Multi-disk (if needed)
Unit 243: Fast loader option
Unit 244: Loading screen
Unit 245: Documentation
Unit 246: Manual content
Unit 247: Map poster
Unit 248: Final testing
Unit 249: Release candidate
Unit 250: Version number
Unit 251: Distribution prep
Unit 252: Community release
Unit 253: Bug support
Unit 254: Retrospective
Unit 255: Skills summary
Unit 256: Complete Dungeon Crawl
**Runnable each unit**

---

## Technical Summary

### Key C64 Features
- Multi-room architecture
- Inventory system
- NPC/dialogue system
- **Kernal disk I/O**
- **D64 save files**
- SID music and effects

### Code Pattern
```asm
; Kernal file save
save_game:
    lda #filename_len
    ldx #<filename
    ldy #>filename
    jsr SETNAM
    lda #$01          ; File number
    ldx #$08          ; Device 8 (disk)
    ldy #$00          ; Secondary address
    jsr SETLFS
    lda #<save_data
    sta $C1
    lda #>save_data
    sta $C2
    ldx #<save_end
    ldy #>save_end
    lda #$C1
    jsr SAVE
    rts
```

---

## Version History
- v1.0 - Initial 256-unit outline
