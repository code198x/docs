# Game 8: Pixel Plains - Complete 128-Unit Outline

## Game Overview
**Platform:** Nintendo Entertainment System
**Genre:** Side-scrolling platformer
**Concept:** The NES's signature genre - a scrolling platformer in the style of Super Mario Bros. Take the mechanics from Crate Escape (Game 2) and expand them into a larger, scrolling world with multiple levels.

**Technical Focus:**
- NES hardware scrolling fundamentals
- Scroll registers and nametable management
- Camera following player
- Large level data structures
- Scrolling collision detection
- Enemies in scrolling world
- Metatile-based level design

---

## Phase 1: Foundation (Units 1-16)
*Establish scrolling display*

### Unit 1: Project Setup
- Create pixel-plains project
- NES memory layout
- iNES header (mapper 0)
- Basic initialisation
- **Runnable:** Clean startup

### Unit 2: Display Configuration
- PPU setup for scrolling
- Background tiles loaded
- Palette configuration
- Screen ready
- **Runnable:** Display initialised

### Unit 3: Tile Design
- Platformer tileset
- Ground, blocks, sky
- Decorative tiles
- Cohesive style
- **Runnable:** Tiles in CHR

### Unit 4: Colour Palette
- Background palettes
- Sprite palettes
- Outdoor theme colours
- Pleasant visuals
- **Runnable:** Palettes set

### Unit 5: Nametable Concept
- Two nametables for scrolling
- Horizontal mirroring
- Seamless scroll
- PPU architecture
- **Runnable:** Concept understood

### Unit 6: Static Level Display
- Draw level to nametable
- Tile placement
- Visible level section
- Foundation display
- **Runnable:** Level visible

### Unit 7: Scroll Register Basics
- PPUSCROLL ($2005)
- Horizontal scroll value
- Smooth pixel scrolling
- Scroll demonstration
- **Runnable:** Screen scrolls

### Unit 8: NMI Scroll Update
- Update scroll in NMI
- Consistent timing
- Stable display
- Proper scroll handling
- **Runnable:** Stable scrolling

### Unit 9: Metatile Concept
- 2x2 tile blocks
- Level compression
- Metatile definitions
- Efficient storage
- **Runnable:** Metatiles defined

### Unit 10: Metatile Data
- Metatile lookup table
- Tile indices per metatile
- Attribute data
- Complete metatiles
- **Runnable:** Metatile system

### Unit 11: Level Data Format
- Column-based storage
- Metatile references
- Compressed format
- Level organisation
- **Runnable:** Level format defined

### Unit 12: Level 1 Data
- First level layout
- Platform placement
- Ground and gaps
- Playable level
- **Runnable:** Level 1 data ready

### Unit 13: Draw Column
- Render metatile column
- Nametable writing
- Attribute updates
- Column complete
- **Runnable:** Columns draw

### Unit 14: Scroll and Update
- Scroll increments
- New column at edge
- Seamless streaming
- Continuous level
- **Runnable:** Level streams

### Unit 15: Nametable Switching
- Cross nametable boundary
- Seamless transition
- Handle wrap-around
- Infinite scroll feel
- **Runnable:** Nametable switching

### Unit 16: Phase 1 Integration
- Smooth scrolling level
- Metatile streaming
- Foundation complete
- **Runnable:** Scrolling world

---

## Phase 2: Core Mechanics (Units 17-32)
*Player movement in scrolling world*

### Unit 17: Player Sprite Design
- Hero character design
- Running frames
- Jump frames
- Idle pose
- **Runnable:** Player sprites ready

### Unit 18: Player Display
- Sprite positioning
- OAM setup
- Player visible
- Screen position
- **Runnable:** Player displayed

### Unit 19: Player Input
- Controller reading
- D-pad movement
- A button jump
- Responsive input
- **Runnable:** Input working

### Unit 20: Horizontal Movement
- Left/right walking
- Acceleration/friction
- Max speed
- Smooth movement
- **Runnable:** Player walks

### Unit 21: Animation System
- Frame cycling
- Walk animation
- Animation timer
- Smooth animation
- **Runnable:** Walking animates

### Unit 22: World Position
- Position in level (not screen)
- 16-bit coordinates
- World vs screen position
- Accurate tracking
- **Runnable:** World position tracked

### Unit 23: Camera Following
- Camera tracks player
- Scroll follows camera
- Smooth following
- Player stays on screen
- **Runnable:** Camera follows

### Unit 24: Camera Bounds
- Camera stops at level edges
- No scroll past boundaries
- Left edge handling
- Right edge handling
- **Runnable:** Camera bounded

### Unit 25: Gravity System
- Downward acceleration
- Terminal velocity
- Falling state
- Gravity physics
- **Runnable:** Player falls

### Unit 26: Jump Mechanic
- Variable jump height
- Jump velocity
- Button hold = higher
- Satisfying jump
- **Runnable:** Player jumps

### Unit 27: Ground Collision
- Detect floor below
- Stop on ground
- Land from jump
- Solid ground
- **Runnable:** Landing works

### Unit 28: World Collision
- Check metatile solidity
- Collision vs world position
- Tile-based collision
- Accurate detection
- **Runnable:** World collision

### Unit 29: Wall Collision
- Horizontal blocking
- Can't walk through walls
- Side collision
- Proper physics
- **Runnable:** Walls block

### Unit 30: Ceiling Collision
- Head bump detection
- Stop upward momentum
- Ceiling contact
- Complete collision
- **Runnable:** Ceilings work

### Unit 31: Animation States
- Idle, walk, jump, fall
- State-based animation
- Correct animation per state
- Visual feedback
- **Runnable:** State animations

### Unit 32: Phase 2 Integration
- Player in scrolling world
- Full movement physics
- Camera following
- World collision
- **Runnable:** Playable platformer

---

## Phase 3: Game Systems (Units 33-48)
*Enemies, items, and game flow*

### Unit 33: Enemy Sprite Design
- Basic enemy type
- Walk animation frames
- Death frame
- Visual design
- **Runnable:** Enemy sprites ready

### Unit 34: Enemy Spawn System
- Enemies in level data
- Spawn when on screen
- Spawn tracking
- Object management
- **Runnable:** Enemies spawn

### Unit 35: Enemy Movement
- Simple patrol AI
- Walk and turn at edges
- Consistent behaviour
- Predictable patterns
- **Runnable:** Enemies patrol

### Unit 36: Enemy World Position
- Enemies have world coords
- Screen position calculated
- Off-screen handling
- Position management
- **Runnable:** Enemy positioning

### Unit 37: Player vs Enemy
- Collision detection
- Stomp from above = kill
- Touch from side = hurt
- Classic platformer rules
- **Runnable:** Enemy interaction

### Unit 38: Enemy Death
- Squash animation
- Remove from active list
- Point reward
- Satisfying defeat
- **Runnable:** Enemies die

### Unit 39: Player Health
- Hearts or hit points
- Damage and recovery
- Invincibility frames
- Health display
- **Runnable:** Health system

### Unit 40: Lives System
- Multiple lives
- Death and respawn
- Life counter
- Game over condition
- **Runnable:** Lives work

### Unit 41: Collectible Coins
- Coin tiles in level
- Collection detection
- Coin counter
- 100 coins = extra life
- **Runnable:** Coins collect

### Unit 42: Power-Up Items
- Power-up blocks
- Item spawning
- Collection effects
- Power state
- **Runnable:** Power-ups

### Unit 43: Checkpoint System
- Mid-level checkpoints
- Respawn position
- Progress saving
- Reduced frustration
- **Runnable:** Checkpoints

### Unit 44: Level End
- Goal/flagpole
- Level complete trigger
- Score bonus
- Victory moment
- **Runnable:** Level end works

### Unit 45: Score System
- Points for enemies
- Points for coins
- Score display
- Running total
- **Runnable:** Scoring

### Unit 46: HUD Display
- Score at top
- Lives counter
- Coin counter
- Clean HUD
- **Runnable:** HUD visible

### Unit 47: Title Screen
- Game title
- Press start
- High score
- Attractive title
- **Runnable:** Title screen

### Unit 48: Phase 3 Integration
- Enemies working
- Items and power-ups
- Score and lives
- Complete game flow
- **Runnable:** Full platformer game

---

## Phase 4: Polish & Feel (Units 49-64)
*Visual and audio refinement*

### Unit 49: Enhanced Animation
- More walk frames
- Skid animation
- Look up/down
- Richer animation
- **Runnable:** Better animation

### Unit 50: Jump Animation Polish
- Ascent pose
- Descent pose
- Landing squash
- Satisfying jumps
- **Runnable:** Jump polish

### Unit 51: Enemy Animation
- Better enemy walk
- Turn animation
- More character
- Living enemies
- **Runnable:** Enemy animation

### Unit 52: Background Decoration
- Clouds, bushes, hills
- Parallax via palette
- Visual depth
- Richer world
- **Runnable:** Decorated background

### Unit 53: Particle Effects
- Coin sparkle
- Dust on land
- Simple particles
- Visual feedback
- **Runnable:** Particles

### Unit 54: Block Hit Effect
- Question block bounce
- Brick break animation
- Satisfying hits
- Impact feedback
- **Runnable:** Block effects

### Unit 55: Sound Engine Setup
- APU sound driver
- Sound effect system
- Music system
- Audio foundation
- **Runnable:** Sound ready

### Unit 56: Jump Sound
- Jump sound effect
- Pitch variation
- Satisfying audio
- Classic sound
- **Runnable:** Jump sound

### Unit 57: Coin Sound
- Collection jingle
- Positive feedback
- Encouraging audio
- Reward sound
- **Runnable:** Coin sound

### Unit 58: Enemy Stomp Sound
- Stomp sound
- Victory audio
- Impact sound
- Combat feedback
- **Runnable:** Stomp sound

### Unit 59: Background Music
- Level music track
- Catchy melody
- Looping
- Platformer feel
- **Runnable:** Level music

### Unit 60: Title Music
- Title screen theme
- Memorable
- Sets mood
- Game identity
- **Runnable:** Title music

### Unit 61: Death Jingle
- Player death sound
- Brief jingle
- Clear feedback
- Restart cue
- **Runnable:** Death music

### Unit 62: Level Complete Music
- Victory fanfare
- Celebration
- Achievement feel
- Reward audio
- **Runnable:** Victory music

### Unit 63: HUD Polish
- Clean number display
- Icon graphics
- Professional layout
- Readable HUD
- **Runnable:** Polished HUD

### Unit 64: Phase 4 Integration
- Full animation set
- Complete audio
- Visual polish
- Professional feel
- **Runnable:** Polished game

---

## Phase 5: Advanced Features (Units 65-80)
*Advanced mechanics and content*

### Unit 65: Moving Platforms
- Platform entities
- Movement patterns
- Player rides platform
- Level variety
- **Runnable:** Moving platforms

### Unit 66: Platform Types
- Horizontal movers
- Vertical movers
- Falling platforms
- Platform variety
- **Runnable:** Platform types

### Unit 67: Spring Jumps
- Bouncy objects
- Super jump height
- Fun mechanic
- Vertical traversal
- **Runnable:** Springs work

### Unit 68: Water Areas
- Water tiles
- Swim physics
- Slower movement
- Different feel
- **Runnable:** Swimming

### Unit 69: Underwater Enemies
- Fish enemies
- Water-specific hazards
- Themed content
- Environment variety
- **Runnable:** Water enemies

### Unit 70: Flying Enemy
- Aerial enemy type
- Flying patterns
- Air hazard
- Dodge challenge
- **Runnable:** Flying enemies

### Unit 71: Boss Enemy Design
- Large boss sprite
- Multiple sprites combined
- Imposing presence
- End-of-world boss
- **Runnable:** Boss sprites

### Unit 72: Boss Battle Room
- Locked arena
- Boss introduction
- Fight area
- Climactic setup
- **Runnable:** Boss room

### Unit 73: Boss Patterns
- Attack phases
- Vulnerable moments
- Learnable patterns
- Fair challenge
- **Runnable:** Boss fights

### Unit 74: Boss Death
- Multi-hit health
- Death explosion
- Victory celebration
- Boss defeated
- **Runnable:** Boss defeated

### Unit 75: World Map Concept
- Multiple worlds
- World themes
- Map screen
- Progress display
- **Runnable:** World map design

### Unit 76: World Map Display
- Map screen graphics
- Level nodes
- Player position
- Path display
- **Runnable:** Map screen

### Unit 77: World Themes
- Grassland, cave, sky themes
- Themed tilesets
- Visual variety
- Distinct worlds
- **Runnable:** World themes

### Unit 78: World 2 Levels
- New level designs
- Increased difficulty
- New challenges
- Content expansion
- **Runnable:** World 2

### Unit 79: World 3 Levels
- Third world content
- Advanced challenges
- Expert levels
- Extended game
- **Runnable:** World 3

### Unit 80: Phase 5 Integration
- Advanced mechanics
- Boss battles
- Multiple worlds
- Feature-complete
- **Runnable:** Full platformer

---

## Phase 6: Content & Variety (Units 81-96)
*Expanded content*

### Unit 81: World 1 Polish
- 4-5 levels
- Gradual difficulty
- Tutorial-like flow
- Welcoming start
- **Runnable:** World 1 complete

### Unit 82: World 2 Polish
- Cave/underground theme
- New hazards
- Moderate difficulty
- Distinct feel
- **Runnable:** World 2 complete

### Unit 83: World 3 Polish
- Sky/cloud theme
- Falling platforms
- Wind effects
- Unique challenges
- **Runnable:** World 3 complete

### Unit 84: World 4 Design
- Castle/fortress theme
- Final world
- Hardest levels
- End-game content
- **Runnable:** World 4

### Unit 85: Final Boss
- Ultimate boss
- Complex patterns
- Epic confrontation
- Game climax
- **Runnable:** Final boss

### Unit 86: Ending Sequence
- Victory scene
- Credits display
- Celebration
- Satisfying ending
- **Runnable:** Ending

### Unit 87: Bonus Levels
- Hidden bonus stages
- Secret access
- Extra rewards
- Discovery content
- **Runnable:** Bonus levels

### Unit 88: Secret Exits
- Alternative level exits
- Hidden paths
- Warp zones
- Exploration reward
- **Runnable:** Secret exits

### Unit 89: Extra Enemy Types
- Additional enemies
- Per-world enemies
- Variety
- Fresh challenges
- **Runnable:** More enemies

### Unit 90: Time Limit
- Level timer
- Urgency mechanic
- Time bonus
- Classic feature
- **Runnable:** Timer active

### Unit 91: One-Up Mushrooms
- Extra life items
- Hidden placement
- Valuable reward
- Discovery item
- **Runnable:** 1-ups work

### Unit 92: Star Power
- Invincibility star
- Temporary power
- Fun reward
- Power fantasy
- **Runnable:** Star power

### Unit 93: Game Save
- Battery/password save
- Progress saving
- Resume later
- Player convenience
- **Runnable:** Save system

### Unit 94: Password System
- Level passwords
- Progress codes
- Alternative to battery
- Accessibility
- **Runnable:** Passwords

### Unit 95: Options Menu
- Sound test
- Difficulty options
- Player settings
- Customisation
- **Runnable:** Options

### Unit 96: Phase 6 Integration
- All worlds complete
- Full content
- Secrets and bonuses
- Complete adventure
- **Runnable:** Full game

---

## Phase 7: Optimisation & Effects (Units 97-112)
*Performance and polish*

### Unit 97: Performance Analysis
- Frame timing check
- Slowdown identification
- CPU usage
- Optimisation targets
- **Runnable:** Performance data

### Unit 98: Scroll Optimisation
- Efficient column updates
- Minimal VRAM writes
- Fast streaming
- Smooth performance
- **Runnable:** Fast scrolling

### Unit 99: Sprite Optimisation
- Efficient OAM updates
- Sprite flickering handling
- Priority management
- Better sprites
- **Runnable:** Optimised sprites

### Unit 100: Collision Optimisation
- Faster tile checks
- Efficient world lookup
- Reduced calculations
- Quick collision
- **Runnable:** Fast collision

### Unit 101: Screen Transitions
- Level transition effect
- Fade or wipe
- Smooth between levels
- Professional flow
- **Runnable:** Transitions

### Unit 102: Pause Screen
- Pause functionality
- Pause display
- Resume game
- Player convenience
- **Runnable:** Pause screen

### Unit 103: Continue System
- Game over continues
- Limited continues
- Progress preservation
- Reduced frustration
- **Runnable:** Continues

### Unit 104: High Score Display
- Best scores
- Per-world scores
- Score tracking
- Competition element
- **Runnable:** High scores

### Unit 105: Demo Mode
- Attract sequence
- AI plays demo
- Shows gameplay
- Title attraction
- **Runnable:** Demo mode

### Unit 106: Sprite Flicker Management
- Handle >8 sprites/line
- Priority cycling
- Minimise flicker
- Better visuals
- **Runnable:** Flicker managed

### Unit 107: PRG Bank Switching
- If using mapper with banks
- Level data in banks
- More content space
- Expanded ROM
- **Runnable:** Bank switching

### Unit 108: CHR Bank Switching
- Animated tiles
- Theme swapping
- Visual variety
- Dynamic graphics
- **Runnable:** CHR switching

### Unit 109: Sound Optimisation
- Efficient sound driver
- Minimal CPU usage
- Clean audio
- No glitches
- **Runnable:** Clean audio

### Unit 110: Edge Cases
- Screen edge behaviour
- Spawn edge handling
- Camera edge cases
- Robust system
- **Runnable:** Edge cases fixed

### Unit 111: Memory Optimisation
- RAM usage audit
- Efficient structures
- Maximum headroom
- Optimised RAM
- **Runnable:** Optimised memory

### Unit 112: Phase 7 Integration
- All optimisations
- Professional performance
- Polished effects
- Release quality
- **Runnable:** Optimised game

---

## Phase 8: Final Polish & Release (Units 113-128)
*Final quality and release*

### Unit 113: Bug Hunt
- Systematic testing
- All levels played
- Bug fixes
- Stable build
- **Runnable:** Bug-free

### Unit 114: Balance Testing
- Difficulty curve
- Enemy placement
- Item distribution
- Fair challenge
- **Runnable:** Balanced

### Unit 115: Control Tuning
- Jump feel
- Acceleration curves
- Responsive controls
- Tight gameplay
- **Runnable:** Tuned controls

### Unit 116: Audio Balance
- Music/SFX levels
- Channel balance
- Pleasant audio
- No clipping
- **Runnable:** Balanced audio

### Unit 117: Visual Consistency
- Tile set coherence
- Palette harmony
- Consistent style
- Professional look
- **Runnable:** Visual polish

### Unit 118: Loading/Title
- Clean title screen
- Quick startup
- Professional intro
- Good first impression
- **Runnable:** Title polish

### Unit 119: Credits
- Development credits
- Music credits
- Thanks
- Complete credits
- **Runnable:** Credits screen

### Unit 120: Instructions
- How to play
- Control display
- Move list
- Help available
- **Runnable:** Instructions

### Unit 121: Region Testing
- NTSC timing
- PAL consideration
- Both regions
- Wide compatibility
- **Runnable:** Region tested

### Unit 122: Emulator Testing
- Test on emulators
- Accuracy check
- Compatibility
- Accessible play
- **Runnable:** Emulator compatible

### Unit 123: Hardware Testing
- Real NES testing
- PowerPak/Everdrive
- Authentic experience
- Hardware verified
- **Runnable:** Hardware tested

### Unit 124: ROM Format
- iNES header correct
- Mapper verified
- Clean ROM
- Distribution ready
- **Runnable:** ROM ready

### Unit 125: Final Playthrough
- Complete game test
- All paths
- All secrets
- Full verification
- **Runnable:** Fully tested

### Unit 126: Documentation
- Game manual
- Technical notes
- Source comments
- Complete docs
- **Runnable:** Documented

### Unit 127: Release Build
- Final ROM
- Version number
- Release notes
- Ready for release
- **Runnable:** Release ROM

### Unit 128: Project Retrospective
- NES scrolling mastered
- Platformer expertise
- Camera systems
- Metatile architecture
- **Runnable:** Complete Pixel Plains

---

## Technical Summary

### Key NES Features Used
- Hardware scrolling (PPUSCROLL)
- Nametable management
- Metatile-based levels
- Sprite animation
- APU sound/music

### Code Patterns Introduced
```asm
; Camera following player
update_camera:
    ; Camera follows player with bounds
    lda player_world_x
    sec
    sbc #CAMERA_OFFSET
    bcs @not_neg
    lda #0              ; Clamp to 0
@not_neg:
    cmp level_max_scroll
    bcc @not_max
    lda level_max_scroll
@not_max:
    sta camera_x
    rts

; Metatile collision
check_tile_solid:
    ; Convert world X,Y to metatile index
    ; Look up metatile type
    ; Return solid flag in carry
    lda world_x+1       ; High byte = tile
    lsr                 ; Divide by 2 for metatile
    sta temp_x
    lda world_y+1
    lsr
    ; Calculate metatile index
    ; Look up solidity
    rts
```

### Skills Progression
| Phase | Primary Skills |
|-------|---------------|
| 1 | Hardware scrolling, metatiles |
| 2 | Player physics, camera |
| 3 | Enemies, items, game flow |
| 4 | Animation, audio |
| 5 | Advanced mechanics, bosses |
| 6 | Full content, worlds |
| 7 | Optimisation, effects |
| 8 | Polish, release |

---

## Version History
- v1.0 - Initial 128-unit outline
