# Game 10: Raster Rider - Complete 256-Unit Outline

## Game Overview
**Platform:** Commodore 64
**Genre:** Pseudo-3D racing (Outrun-style)
**Concept:** High-speed racing with pseudo-3D road perspective using advanced raster techniques. Master per-line colour manipulation, road mathematics, sprite scaling, and the complete Outrun-style racing experience.

**Technical Focus:**
- Advanced raster interrupt chains
- Per-line colour/scroll manipulation
- Perspective road mathematics
- Sprite scaling illusion
- Track data compression
- Full championship mode

---

## Phase 1: Foundation (Units 1-16)
*Display and raster basics*

Unit 1: Project setup and memory layout
Unit 2: Display configuration for racing
Unit 3: Basic raster interrupt setup
Unit 4: Stable raster timing (double IRQ)
Unit 5: Horizon line concept
Unit 6: Road perspective mathematics
Unit 7: Basic road shape calculation
Unit 8: Road width per scanline
Unit 9: Static road display
Unit 10: Road centre positioning
Unit 11: Colour palette for road
Unit 12: Grass/road colour split
Unit 13: Per-line colour basics
Unit 14: Raster colour timing
Unit 15: Player car sprite setup
Unit 16: Phase 1 integration - static road with car
**Runnable each unit**

---

## Phase 2: Road Animation (Units 17-32)
*Moving road effect*

Unit 17: Road stripe concept
Unit 18: Stripe position tracking
Unit 19: Stripe animation loop
Unit 20: Speed-based stripe movement
Unit 21: Colour cycling for speed
Unit 22: Acceleration visual effect
Unit 23: Deceleration visual effect
Unit 24: Road edge markings
Unit 25: Kerb stripe animation
Unit 26: Centre line animation
Unit 27: Multiple stripe colours
Unit 28: Stripe synchronisation
Unit 29: Performance optimisation
Unit 30: Raster timing refinement
Unit 31: Visual polish pass
Unit 32: Phase 2 integration - animated road
**Runnable each unit**

---

## Phase 3: Curves (Units 33-48)
*Road curvature system*

Unit 33: Curve mathematics concept
Unit 34: Per-line offset calculation
Unit 35: Left curve implementation
Unit 36: Right curve implementation
Unit 37: Curve data format
Unit 38: Curve transitions (straight to curve)
Unit 39: S-curve handling
Unit 40: Gentle curves
Unit 41: Sharp curves
Unit 42: Hairpin turns
Unit 43: Curve sequence data
Unit 44: Smooth curve interpolation
Unit 45: Player position in curves
Unit 46: Centrifugal effect
Unit 47: Curve visual polish
Unit 48: Phase 3 integration - curving roads
**Runnable each unit**

---

## Phase 4: Hills (Units 49-64)
*Vertical road variation*

Unit 49: Hill mathematics concept
Unit 50: Horizon position changes
Unit 51: Uphill perspective
Unit 52: Downhill perspective
Unit 53: Hill data format
Unit 54: Hill transitions
Unit 55: Gentle slopes
Unit 56: Steep hills
Unit 57: Crest visibility
Unit 58: Dip visibility
Unit 59: Combined curves and hills
Unit 60: Road segment system
Unit 61: Segment transitions
Unit 62: Complex road shapes
Unit 63: Hill visual polish
Unit 64: Phase 4 integration - 3D road
**Runnable each unit**

---

## Phase 5: Player Control (Units 65-80)
*Driving mechanics*

Unit 65: Acceleration input
Unit 66: Speed accumulation
Unit 67: Maximum speed
Unit 68: Braking mechanics
Unit 69: Steering input
Unit 70: Position on road
Unit 71: Speed-based steering
Unit 72: Road boundaries
Unit 73: Off-road detection
Unit 74: Off-road slowdown
Unit 75: Crash state
Unit 76: Spin-out mechanics
Unit 77: Recovery system
Unit 78: Steering feel tuning
Unit 79: Control responsiveness
Unit 80: Phase 5 integration - driveable car
**Runnable each unit**

---

## Phase 6: Opponents (Units 81-96)
*Traffic and racing*

Unit 81: Opponent sprite design
Unit 82: Multiple car colours
Unit 83: Z-position tracking
Unit 84: Y-position from Z
Unit 85: Sprite scaling illusion
Unit 86: Small/medium/large sprites
Unit 87: Opponent spawning
Unit 88: Approach speed
Unit 89: Lane positioning
Unit 90: Opponent AI basics
Unit 91: Overtaking behaviour
Unit 92: Multiple opponents
Unit 93: Collision detection
Unit 94: Crash on collision
Unit 95: Opponent variety
Unit 96: Phase 6 integration - traffic
**Runnable each unit**

---

## Phase 7: Track System (Units 97-112)
*Track data and variety*

Unit 97: Track data format design
Unit 98: Segment-based tracks
Unit 99: Track compression
Unit 100: Track streaming
Unit 101: Track 1 - Coastal design
Unit 102: Track 1 - implementation
Unit 103: Track 2 - Desert design
Unit 104: Track 2 - implementation
Unit 105: Track 3 - Forest design
Unit 106: Track 3 - implementation
Unit 107: Track 4 - Mountain design
Unit 108: Track 4 - implementation
Unit 109: Track 5 - Night design
Unit 110: Track 5 - implementation
Unit 111: Track selection system
Unit 112: Phase 7 integration - multiple tracks
**Runnable each unit**

---

## Phase 8: Scenery (Units 113-128)
*Roadside objects*

Unit 113: Scenery sprite system
Unit 114: Object Z-positioning
Unit 115: Object scaling
Unit 116: Trees/posts graphics
Unit 117: Left-side objects
Unit 118: Right-side objects
Unit 119: Object spawning
Unit 120: Track-specific scenery
Unit 121: Billboards
Unit 122: Buildings
Unit 123: Natural features
Unit 124: Scenery variety
Unit 125: Parallax effect
Unit 126: Depth layering
Unit 127: Scenery polish
Unit 128: Phase 8 integration - rich scenery
**Runnable each unit**

---

## Phase 9: HUD & Scoring (Units 129-144)
*Interface and progression*

Unit 129: Speedometer design
Unit 130: Speed display
Unit 131: Timer display
Unit 132: Lap/checkpoint display
Unit 133: Position display
Unit 134: Score system
Unit 135: Distance scoring
Unit 136: Checkpoint bonuses
Unit 137: Time extension
Unit 138: Checkpoint gates
Unit 139: Lap system
Unit 140: Race completion
Unit 141: Results screen
Unit 142: High score tracking
Unit 143: HUD optimisation
Unit 144: Phase 9 integration - complete HUD
**Runnable each unit**

---

## Phase 10: Audio (Units 145-160)
*Sound and music*

Unit 145: SID setup for racing
Unit 146: Engine sound design
Unit 147: Speed-based pitch
Unit 148: Acceleration sound
Unit 149: Deceleration sound
Unit 150: Gear change effect
Unit 151: Skid/screech sound
Unit 152: Crash sound
Unit 153: Checkpoint sound
Unit 154: Music system
Unit 155: Title music
Unit 156: Racing music
Unit 157: Results music
Unit 158: Audio mixing
Unit 159: Engine + music balance
Unit 160: Phase 10 integration - full audio
**Runnable each unit**

---

## Phase 11: Game Modes (Units 161-176)
*Modes and features*

Unit 161: Single race mode
Unit 162: Time trial mode
Unit 163: Championship mode design
Unit 164: Championship structure
Unit 165: Points system
Unit 166: Season progression
Unit 167: Standings display
Unit 168: Championship completion
Unit 169: Practice mode
Unit 170: Track preview
Unit 171: Difficulty settings
Unit 172: Easy mode
Unit 173: Medium mode
Unit 174: Hard mode
Unit 175: Two-player alternating
Unit 176: Phase 11 integration - all modes
**Runnable each unit**

---

## Phase 12: Advanced Features (Units 177-192)
*Enhanced gameplay*

Unit 177: Weather system concept
Unit 178: Rain effect
Unit 179: Rain on handling
Unit 180: Night racing
Unit 181: Night visuals
Unit 182: Headlight effect
Unit 183: Turbo/boost system
Unit 184: Turbo visuals
Unit 185: Turbo limitations
Unit 186: Car selection
Unit 187: Car statistics
Unit 188: Unlockable cars
Unit 189: Ghost replay data
Unit 190: Ghost car display
Unit 191: Time attack with ghost
Unit 192: Phase 12 integration - advanced features
**Runnable each unit**

---

## Phase 13: Optimisation (Units 193-208)
*Performance maximisation*

Unit 193: Performance profiling
Unit 194: Raster timing analysis
Unit 195: Critical path optimisation
Unit 196: Unrolled road rendering
Unit 197: Self-modifying code
Unit 198: Colour table optimisation
Unit 199: Sprite multiplexing
Unit 200: Enemy sprite management
Unit 201: Memory optimisation
Unit 202: Track data efficiency
Unit 203: Stable 50fps
Unit 204: Worst-case testing
Unit 205: Border timing
Unit 206: Badline handling
Unit 207: Final optimisation pass
Unit 208: Phase 13 integration - optimised
**Runnable each unit**

---

## Phase 14: Polish (Units 209-224)
*Final quality*

Unit 209: Visual polish pass
Unit 210: Road colour refinement
Unit 211: Scenery polish
Unit 212: Animation polish
Unit 213: Audio balance
Unit 214: Music/SFX levels
Unit 215: Gameplay feel tuning
Unit 216: Steering refinement
Unit 217: Difficulty balance
Unit 218: Track balance
Unit 219: Bug hunting
Unit 220: Edge case fixes
Unit 221: Playtest round 1
Unit 222: Feedback integration
Unit 223: Playtest round 2
Unit 224: Phase 14 integration - polished
**Runnable each unit**

---

## Phase 15: Content & Extras (Units 225-240)
*Additional content*

Unit 225: Bonus track 1
Unit 226: Bonus track 2
Unit 227: Mirror mode
Unit 228: Reverse tracks
Unit 229: Achievement system
Unit 230: Unlock conditions
Unit 231: Gallery mode
Unit 232: Car gallery
Unit 233: Track gallery
Unit 234: Statistics tracking
Unit 235: Best times
Unit 236: Total distance
Unit 237: Credits sequence
Unit 238: Ending sequence
Unit 239: Content verification
Unit 240: Phase 15 integration - full content
**Runnable each unit**

---

## Phase 16: Release (Units 241-256)
*Distribution*

Unit 241: Title screen polish
Unit 242: Menu flow
Unit 243: Options menu
Unit 244: Save system (disk)
Unit 245: Load times
Unit 246: Full testing
Unit 247: Regression testing
Unit 248: Hardware testing
Unit 249: Documentation
Unit 250: Manual creation
Unit 251: Disk mastering
Unit 252: Release candidate
Unit 253: Final fixes
Unit 254: Release build
Unit 255: Retrospective
Unit 256: Complete Raster Rider
**Runnable each unit**

---

## Technical Summary

### Key C64 Features
- Advanced raster interrupt chains
- Per-scanline colour manipulation
- Sprite multiplexing for cars
- Road perspective mathematics
- SID engine sound synthesis

### Code Pattern
```asm
; Per-line road colour (in IRQ)
road_irq:
    ldy road_line
    lda road_colours,y
    sta $d021
    lda grass_colours,y
    sta $d020
    iny
    sty road_line
    ; Chain to next line
    rts
```

---

## Version History
- v1.0 - Initial 256-unit outline
