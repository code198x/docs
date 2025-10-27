# Phase 0: AMOS Professional

**Lessons:** 1-64 (4 tiers � 16 lessons)
**Language:** AMOS Professional
**Approach:** Game-first discovery learning

## Philosophy

Learn programming by building games, not by memorising syntax. Each short arc (2-3 lessons) produces a complete playable game. Concepts emerge naturally from trying to make games better, faster, and more interesting.

The Amiga represented a quantum leap in home computing power. Released in 1985, it combined dedicated graphics co-processors, 4-channel PCM audio, and multitasking in ways that wouldn't become mainstream until the mid-1990s. This curriculum embraces both the power and the unique architectural constraints that made Amiga game development distinctive.

AMOS Professional (1990) was specifically designed for game creation on the Amiga. Unlike traditional BASIC, it provides:

- **No line numbers** - Structured programming with labels and procedures
- **BOB system** - Blitter OBjects for hardware-accelerated sprites
- **Built-in animation** - AMAL (AMOS Animation Language) for scripted movement
- **Direct hardware access** - Copper lists, blitter operations, Paula audio
- **Immediate mode graphics** - Screen, Plot, Draw, Circle commands with double buffering
- **Fast compilation** - Near-assembly speed for action games

Experience both the revolutionary capabilities (custom chipsets, hardware acceleration) and the architectural constraints (attribute conflicts, memory management) that defined Amiga game development.

## Amiga-Specific Advantages

1. **BOB sprite system** - Hardware-accelerated blitter operations for fast sprite movement
2. **Copper co-processor** - Display list programming for per-scanline effects
3. **Blitter** - Hardware block copying and fill operations
4. **Paula 4-channel audio** - Sample-based sound with independent volume/pitch control
5. **Dual playfield** - Hardware scrolling and parallax without CPU involvement
6. **Hold-and-modify (HAM) mode** - 4096 colours on screen from 16.8 million palette
7. **Multitasking OS** - Run multiple programs simultaneously (Workbench integration)

## Amiga-Specific Challenges

1. **Memory management** - Chip RAM vs Fast RAM (graphics must be in Chip RAM)
2. **Screen mode complexity** - Low-res, high-res, interlace, overscan, HAM modes
3. **Sprite limitations** - Only 8 hardware sprites (use BOBs for more)
4. **Blitter conflicts** - CPU must yield to blitter during operations
5. **Chipset versions** - OCS, ECS, AGA differences affect capabilities
6. **Copper timing** - Display list programming requires understanding raster positions

## Structure

### Tier 1: Discovery (L1-16) - Foundation Games

**Philosophy:** Quick wins with AMOS's structured approach
**Code Range:** 10-80 lines

#### Arc 1: Text Adventures (L1-3)
- AMOS's structured programming (procedures, no line numbers)
- Locate for screen positioning
- Input$ for user interaction
- **Deliverable:** Text-based adventure game (~50 lines)

#### Arc 2: Knowledge Base (L4-6)
- Data and Read statements
- Arrays and string handling
- Restore for quiz resets
- **Deliverable:** Quiz game with scoring (~60 lines)

#### Arc 3: BOB Graphics (L7-9)
- Creating and displaying BOBs (Blitter OBjects)
- Screen modes and double buffering
- Ink, Paper, Cls commands
- **Deliverable:** Interactive sprite demo (~80 lines)

#### Arc 4: Paula Audio (L10-11)
- Sample Bank and Music Bank
- Play, Sam Play for sound effects
- Volume, pitch, and channel control
- **Deliverable:** Music/sound effects demonstration

#### Arc 5: Moving BOBs (L12-14)
- BOB movement and collision detection
- Joypad and Inkey$ input
- Screen scrolling basics
- **Deliverable:** Character movement game

#### Arc 6: Mini Action Game (L15-16)
- Combine movement, collision, scoring
- Simple AMAL animation
- **Deliverable:** Complete arcade-style game (~80 lines)

### Tier 2: Building (L17-32) - Complete Systems

**Philosophy:** Professional game systems with hardware acceleration
**Code Range:** 80-200 lines

#### Arc 1: Animation System (L17-21)
- AMAL (AMOS Animation Language)
- Multi-frame sprite animation
- Animation channels and synchronisation
- Collision detection refinement
- **Deliverable:** Animated sprite showcase

#### Arc 2: Arcade Action (L22-27)
- Fast BOB movement techniques
- Blitter optimisation
- Multiple moving objects
- HUD and score display
- **Deliverable:** Space shooter with waves

#### Arc 3: Platform Game (L28-32)
- Gravity and jumping physics
- Tile-based collision
- Level data structures
- Enemy AI basics
- **Deliverable:** Platform game with multiple screens

### Tier 3: Mastery (L33-48) - Professional Games

**Philosophy:** Genre mastery with custom chipset exploitation
**Code Range:** 150-300 lines

#### Arc 1: Puzzle Game (L33-37)
- Grid-based logic
- Block-falling mechanics (Tetris-style)
- Level progression and difficulty scaling
- **Deliverable:** Puzzle game with 10+ levels

#### Arc 2: Shooter (L38-43)
- Bullet management systems
- Wave patterns and formations
- Power-up systems
- Parallax scrolling with dual playfield
- **Deliverable:** Scrolling shooter with bosses

#### Arc 3: Adventure/RPG (L44-48)
- Room/area navigation
- Inventory system with icons
- Simple combat mechanics
- Save/load to disk
- **Deliverable:** Multi-area adventure game

### Tier 4: Limits (L49-64) - AMOS's Ceiling

**Philosophy:** Discover AMOS Professional's performance boundaries
**Code Range:** 200-400 lines

#### Arc 1: Speed Limit (L49-53)
- Action game with many BOBs
- Measure frame rate
- Optimisation techniques (blitter vs CPU)
- **Conclusion:** AMOS reaches 25-30fps ceiling with many objects

#### Arc 2: Copper Programming (L54-58)
- Direct copper list manipulation
- Per-scanline palette changes
- Raster effects (rainbow, splits)
- **Conclusion:** Copper opens effects impossible in structured code

#### Arc 3: Blitter Mastery (L59-64)
- Direct blitter programming
- Cookie-cut operations
- Mask and stencil techniques
- **Finale:** Complete game using all Phase 0 techniques, measuring limits

## Key Differences from Other Platforms

| Aspect | Commodore 64 | ZX Spectrum | Amiga |
|--------|--------------|-------------|-------|
| **Graphics** | Hardware sprites, flexible colour | Software sprites, attribute clash | BOBs (blitter), dual playfield |
| **Sound** | SID chip (3 voices) | BEEP (1-bit) / AY chip (128K) | Paula (4-channel PCM samples) |
| **Colours** | 16 colours, per-pixel | 8 colours, per-character block | 32 colours (64 in EHB), per-pixel, 4096 in HAM |
| **Memory** | 64K | 48K (128K model) | 512K-1MB+ (Chip + Fast RAM) |
| **Language speed** | BASIC (slow) | BASIC (fast) | AMOS (near-assembly) |
| **Screen access** | POKE screen memory | PRINT AT, PLOT, DRAW | Screen, Locate, Plot, Draw (double buffered) |
| **Co-processors** | None | None | Copper, Blitter, Paula |

## Learning Outcomes

By completing Phase 0, you will have:

- Mastered AMOS Professional fundamentals and structured programming
- Built 16+ complete games leveraging Amiga's custom chipsets
- Understood BOB system (Blitter OBjects) for sprite management
- Created hardware-accelerated graphics with the blitter
- Programmed Paula's 4-channel audio system with samples
- Used AMAL (AMOS Animation Language) for scripted movement
- Experienced AMOS's speed advantages over traditional BASIC
- Explored copper programming for raster effects
- **Discovered:** AMOS is fast for action games but direct hardware access offers more
- **Motivation established:** Ready for 68000 assembly to unlock full chipset potential

## Prerequisites

None - Phase 0 is the entry point.

## Builds Toward

**Phase 1:** 68000 Assembly Language + Custom Chipset Mastery
- Leverage AMOS foundation and hardware understanding
- Learn 68000 instruction set
- Master custom chipset programming (Agnus, Denise, Paula)
- Achieve 50fps smooth scrolling with hundreds of sprites
- Advanced copper and blitter programming
- Direct Paula audio control

## Amiga-Specific Resources

**Hardware:**
- Motorola 68000 CPU (7.14MHz PAL / 7.16MHz NTSC)
- Agnus (memory controller + blitter)
- Denise (video output)
- Paula (audio + I/O)
- Custom chipset versions: OCS (Original), ECS (Enhanced), AGA (Advanced)

**Development Tools:**
- WinUAE / FS-UAE emulators
- AMOS Professional 2.00
- Turbo assembler (Phase 1+)
- Protracker (music)

**Memory Layout:**
- Chip RAM: 512K-2MB (accessible by all chips)
- Fast RAM: Optional expansion (CPU only)
- ROM: Kickstart 1.3-3.1 (512K-1MB)

## Notes for Lesson Creators

**Embrace the architecture:**
- BOBs are easier than direct blitter but understand both
- Copper programming opens creative possibilities
- Sample-based audio is powerful but requires memory management
- Dual playfield enables parallax without CPU involvement

**AMOS Professional advantages:**
- Structured programming (procedures, functions, labels)
- No line numbers (modern code organisation)
- Fast compilation (~100x faster than interpreting)
- Built-in game development commands
- Direct hardware access when needed

**Amiga constraints to teach:**
- Chip RAM vs Fast RAM (graphics must be in Chip RAM)
- Blitter conflicts (CPU must wait)
- Sprite limitations (8 hardware sprites, use BOBs for more)
- Chipset differences (OCS/ECS/AGA)

**British spelling throughout:** colour, centre, etc. (Amiga was UK-designed)

---

**Version:** 1.1
**Last Updated:** 2025-10-27
**Status:** Tier 1 (L1-16) complete, Tier 2 (L17-32) specs complete, Tier 3-4 to be created
