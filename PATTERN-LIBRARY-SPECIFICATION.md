# Pattern Library: Specification

## Overview

The Pattern Library is a comprehensive reference collection of reusable code patterns, routines, and techniques taught throughout the Code Like It's 198x curriculum. Each pattern provides production-ready implementations that learners can use directly in their own projects, with clear explanations of how they work, when to use them, and what trade-offs they involve.

**Key Principles:**
- **Standalone utility** - Usable independently of curriculum, enhanced when used together
- **Production-ready code** - Copy-paste-adapt for real projects
- **Evolution tracked** - Simple → complex versions with clear progression
- **Lesson-linked** - Reference back to where each pattern was taught
- **Multiple variations** - Separate entries for different approaches, cross-linked
- **Platform-specific** - Code implementations tailored to each platform's architecture

---

## Organization Structure

### Multi-Dimensional Classification

Patterns are organized by **three dimensions**:

1. **Platform:** Commodore 64, ZX Spectrum, Amiga, NES (platform-specific implementations)
2. **Technique Category:** What the pattern does
3. **Genre Application:** Where the pattern is commonly used (cross-referenced)

**Primary Organization:** `/patterns/{platform}/{category}/{pattern-name}`

**Categories:**
- **Rendering:** Graphics display, sprites, scrolling, effects
- **Input:** Controller reading, keyboard handling, input buffering
- **Audio:** Music playback, sound effects, mixing
- **Physics:** Collision detection, movement, gravity, projectiles
- **AI:** Enemy behavior, pathfinding, decision-making
- **Data:** Compression, loading, save systems
- **Optimization:** Speed-ups, memory management, code tricks
- **Framework:** Game loops, state machines, utility routines

---

## Pattern Entry Format

### Required Sections

Every pattern entry must include:

#### 1. Frontmatter Metadata

```yaml
---
title: "Sprite Multiplexing (Basic)"
platform: "Commodore 64"
category: "Rendering"
difficulty: "Intermediate"
phase_introduced: 2
lesson_first_taught: "Phase 2, Tier 1, Lesson 8"
evolution:
  - pattern: "sprite-multiplexing-basic"
    phase: 2
  - pattern: "sprite-multiplexing-sorted"
    phase: 3
  - pattern: "sprite-multiplexing-advanced"
    phase: 5
related_patterns:
  - "raster-interrupts"
  - "sprite-animation"
related_vault:
  - "/vault/techniques/c64-sprite-multiplexing"
  - "/vault/hardware/vic-ii"
genres: ["Shoot 'Em Up", "Platform Game", "Beat 'Em Up"]
tags: ["sprites", "multiplexing", "raster", "vic-ii"]
---
```

#### 2. Overview

**Purpose:** One-paragraph explanation of what the pattern does and why you'd use it.

```markdown
## Overview

Displays more than 8 sprites on-screen by reusing the same hardware sprites multiple times per frame. When the screen beam passes below the first set of sprites, a raster interrupt repositions them further down the screen. Essential for games needing 16-40 sprites (enemies, bullets, collectibles).
```

#### 3. When to Use This Pattern

**Purpose:** Clear guidance on appropriate use cases.

```markdown
## When to Use This Pattern

**Use when:**
- You need 9-40 sprites on screen
- Sprites are roughly distributed vertically (not all clustered)
- You can tolerate occasional flickering when >8 sprites share a scanline

**Don't use when:**
- 8 sprites or fewer suffice (unnecessary complexity)
- All sprites cluster at same Y position (multiplexing won't help)
- You need rock-solid 50fps with no IRQ overhead (use sprite-less rendering)
```

#### 4. How It Works

**Purpose:** Technical explanation of the approach.

```markdown
## How It Works

1. **Setup:** Sort all active sprites by Y position
2. **IRQ Chain:** Set up raster interrupts at the Y position where each group of 8 sprites ends
3. **Reposition:** In each IRQ, update hardware sprite positions to the next group
4. **Handle Overflow:** When >8 sprites share a scanline, choose which to display (or flicker between frames)

**Key Timing:**
- IRQ must trigger below the bottom sprite of current group
- Sprite positioning takes ~63 cycles per sprite
- Must complete before raster beam catches up
```

#### 5. Code Implementation

**Purpose:** Complete, working, well-commented code.

```markdown
## Code Implementation

### Basic Sprite Multiplexing (8-24 sprites)

` ``asm
; =============================================================================
; BASIC SPRITE MULTIPLEXING
; Handles 8-24 sprites using simple zone-based multiplexing
; First taught: Phase 2, Tier 1, Lesson 8
; =============================================================================

; --- Constants ---
MAX_SPRITES = 24
SPRITE_ZONES = 3        ; Screen divided into 3 zones
SPRITES_PER_ZONE = 8

; --- Zero Page Variables ---
sprite_count:       .byte 0         ; Total active sprites (0-24)
sprite_x_lo:        .res MAX_SPRITES
sprite_x_hi:        .res MAX_SPRITES
sprite_y:           .res MAX_SPRITES
sprite_frame:       .res MAX_SPRITES

; --- IRQ Raster Positions ---
irq_zone1 = 80      ; First multiplexing zone
irq_zone2 = 160     ; Second multiplexing zone
irq_zone3 = 240     ; Third multiplexing zone

; =============================================================================
; Initialize Multiplexing System
; =============================================================================
init_multiplexing:
    ; Set up raster IRQ chain
    sei
    lda #<irq_zone1_handler
    sta $0314
    lda #>irq_zone1_handler
    sta $0315

    lda #irq_zone1
    sta $d012               ; Trigger at scanline 80

    lda #$1b
    sta $d011               ; Enable raster IRQ
    lda #$01
    sta $d01a               ; Enable raster interrupt
    cli
    rts

; =============================================================================
; Zone 1 IRQ Handler (Scanline 80)
; Displays sprites 0-7
; =============================================================================
irq_zone1_handler:
    pha
    txa
    pha
    tya
    pha

    ; Update hardware sprites 0-7 from logical sprites 0-7
    ldx #7
:   lda sprite_x_lo,x
    sta $d000,x,x          ; X position low byte
    lda sprite_x_hi,x
    sta $d010              ; X position MSB (via bit manipulation)
    lda sprite_y,x
    sta $d001,x,x          ; Y position
    lda sprite_frame,x
    sta $07f8,x            ; Sprite pointer
    dex
    bpl :-

    ; Chain to next IRQ
    lda #<irq_zone2_handler
    sta $0314
    lda #>irq_zone2_handler
    sta $0315
    lda #irq_zone2
    sta $d012

    asl $d019              ; Acknowledge IRQ

    pla
    tay
    pla
    tax
    pla
    rti

; =============================================================================
; Zone 2 IRQ Handler (Scanline 160)
; Displays sprites 8-15
; =============================================================================
irq_zone2_handler:
    ; [Similar structure, using logical sprites 8-15]
    ; ...

; =============================================================================
; Zone 3 IRQ Handler (Scanline 240)
; Displays sprites 16-23
; =============================================================================
irq_zone3_handler:
    ; [Similar structure, using logical sprites 16-23]
    ; ...

    ; Chain back to zone 1
    lda #<irq_zone1_handler
    sta $0314
    lda #>irq_zone1_handler
    sta $0315
    lda #irq_zone1
    sta $d012

    asl $d019
    pla
    tay
    pla
    tax
    pla
    rti
` ``

**Usage:**
` ``asm
; In your game initialization:
jsr init_multiplexing

; Update sprite positions in main loop:
lda #20                ; Set sprite count
sta sprite_count

lda #100               ; Sprite 0 X position
sta sprite_x_lo+0
lda #0
sta sprite_x_hi+0
lda #50                ; Sprite 0 Y position
sta sprite_y+0
lda #64                ; Sprite 0 frame (sprite pointer)
sta sprite_frame+0

; Repeat for other sprites...
` ``
```

#### 6. Variations

**Purpose:** Link to related patterns with different approaches.

```markdown
## Variations

This is the **basic zone-based** approach. Other implementations:

- **[Sorted Multiplexing](/patterns/c64/rendering/sprite-multiplexing-sorted)** (Phase 3) - Dynamic Y-sorting for variable sprite counts
- **[Advanced Multiplexing](/patterns/c64/rendering/sprite-multiplexing-advanced)** (Phase 5) - Handles 40-60 sprites with flicker management
- **[Sprite Pooling](/patterns/c64/rendering/sprite-pooling)** (Phase 4) - Object pooling for bullet/particle systems

**Comparison:**
- **Basic (this):** Fixed zones, 8-24 sprites, simplest implementation
- **Sorted:** Variable zones, 16-40 sprites, Y-sorting overhead
- **Advanced:** 40-60+ sprites, complex flicker management, highest performance cost
```

#### 7. Performance & Trade-offs

**Purpose:** Clear understanding of costs.

```markdown
## Performance & Trade-offs

**CPU Cost:**
- ~200-300 cycles per IRQ (×3 = 900 cycles/frame)
- Raster time: Must complete before beam catches sprites
- Sorting cost (if using sorted variation): ~500-2000 cycles/frame

**Memory Cost:**
- 4 bytes per logical sprite (x_lo, x_hi, y, frame)
- IRQ handlers: ~300 bytes total

**Visual Quality:**
- **Flickering:** Occurs when >8 sprites share Y coordinate
- **Timing:** Occasional glitches if IRQ timing fails
- **Sprite Priority:** Can't change per-zone (hardware limitation)

**Optimization Tips:**
- Sort only when sprite positions change significantly
- Use fewer zones if sprites cluster vertically
- Pre-calculate sprite pointers when possible
```

#### 8. Prerequisites

**Purpose:** What learner should know first.

```markdown
## Prerequisites

**Required Knowledge:**
- Raster interrupts ([Pattern: Raster Interrupts](/patterns/c64/framework/raster-interrupts))
- Sprite basics ([Pattern: Basic Sprite Display](/patterns/c64/rendering/sprite-basics))
- VIC-II sprite registers ([Vault: VIC-II](/vault/hardware/vic-ii))

**Required Phase:**
- Phase 2 minimum (raster IRQs introduced in Phase 2, Tier 1, Lesson 3)
```

#### 9. Curriculum Integration

**Purpose:** Where this pattern appears in lessons.

```markdown
## Curriculum Integration

**First Introduced:**
- **Phase 2, Tier 1, Lesson 8** - "Displaying More Sprites"
  - Basic zone-based multiplexing
  - 3 zones, 24 sprites maximum
  - Simple shooting game example

**Expanded:**
- **Phase 3, Tier 2, Lessons 12-14** - "Dynamic Sprite Management"
  - Y-sorting algorithm
  - Variable zone positioning
  - Shoot 'em up with 30+ enemies

**Mastered:**
- **Phase 5, Tier 1, Lessons 18-20** - "Advanced Multiplexing"
  - Flicker management strategies
  - 50+ sprites with priority handling
  - Bullet hell shmup example

**Referenced In:**
- Phase 3, Tier 5 (Horizontal Shooter)
- Phase 4, Tier 3 (Vertical Shooter)
- Phase 5, Tier 8 (Beat 'Em Up)
```

#### 10. Genre Applications

**Purpose:** Where this pattern is commonly used.

```markdown
## Genre Applications

**Essential For:**
- **Shoot 'Em Ups:** Many enemies + bullets simultaneously
- **Beat 'Em Ups:** Multiple on-screen enemies
- **Platform Games:** Enemies + collectibles + hazards

**Not Needed For:**
- **Puzzle Games:** Usually ≤8 distinct sprites
- **Racing Games:** Often use character-based graphics
- **Text Adventures:** Minimal sprite usage
```

#### 11. Related Patterns

**Purpose:** Cross-references to complementary patterns.

```markdown
## Related Patterns

**Dependencies:**
- [Raster Interrupts](/patterns/c64/framework/raster-interrupts) - Required foundation

**Commonly Used With:**
- [Sprite Animation](/patterns/c64/rendering/sprite-animation) - Animating multiplexed sprites
- [Bullet Pool Management](/patterns/c64/physics/bullet-pooling) - Managing many projectiles
- [Enemy Update Routines](/patterns/c64/ai/enemy-updates) - Updating many enemies efficiently

**Alternatives:**
- [Character-Based Sprites](/patterns/c64/rendering/char-sprites) - No multiplexing needed, different aesthetic
- [Software Sprites](/patterns/c64/rendering/software-sprites) - More sprites possible, much slower
```

#### 12. Related Vault Entries

**Purpose:** Links to deeper context.

```markdown
## Related Vault Entries

**Techniques:**
- [Sprite Multiplexing](/vault/techniques/c64-sprite-multiplexing) - Comprehensive technique overview
- [Raster Interrupts](/vault/techniques/c64-raster-interrupts) - How raster IRQs work

**Hardware:**
- [VIC-II Chip](/vault/hardware/vic-ii) - Hardware sprite system details
- [6510 CPU](/vault/hardware/6510-cpu) - Timing and cycle counting

**Games Using This:**
- [Mayhem in Monsterland](/vault/games/mayhem-in-monsterland) - 50+ sprite multiplexing
- [Turrican](/vault/games/turrican) - Advanced multiplexing example
```

---

## Evolution Tracking

### Pattern Progression

Many patterns have **simple → complex** progressions taught across phases:

**Example: Sprite Multiplexing**
- **Phase 2:** Basic zone-based (fixed 3 zones, 24 sprites)
- **Phase 3:** Sorted dynamic (variable zones, 40 sprites)
- **Phase 5:** Advanced (60+ sprites, flicker management)
- **Phase 7:** Optimized (cycle-perfect, maximum performance)

**Each version is a separate pattern entry** with:
- Cross-links to earlier/later versions
- "Evolution" metadata showing progression
- Clear explanation of what's new vs. previous version
- When to upgrade from previous version

---

## Code Standards

### Commenting

**Every pattern must include:**
- File/section header explaining purpose
- Inline comments for non-obvious code
- Register usage documentation
- Timing notes where critical

```asm
; =============================================================================
; SPRITE MULTIPLEXING - BASIC ZONE IMPLEMENTATION
; Handles 8-24 sprites across 3 fixed vertical zones
; First taught: Phase 2, Tier 1, Lesson 8
;
; Performance: ~300 cycles per zone IRQ (900 cycles/frame total)
; Memory: 4 bytes per sprite + 300 bytes code
; =============================================================================

; Registers on entry: N/A (IRQ handler)
; Registers on exit: All preserved
; Zero page used: None (uses only IRQ-safe locations)
```

### Code Style

- **Assembly:** Platform-appropriate assembler syntax (ACME for C64, sjasmplus for ZX, vasm for Amiga, ca65 for NES)
- **Indentation:** Consistent (labels flush left, instructions indented)
- **Constants:** Named constants, not magic numbers
- **Optimization:** Phase-appropriate (don't over-optimize Phase 2 examples)

---

## File Structure

```
/patterns/
  /commodore-64/
    /rendering/
      sprite-multiplexing-basic.md
      sprite-multiplexing-sorted.md
      sprite-multiplexing-advanced.md
      scrolling-character-based.md
      scrolling-pixel-smooth.md
    /input/
      joystick-reading-basic.md
      joystick-debouncing.md
      keyboard-multi-key.md
    /audio/
      sid-music-playback.md
      sfx-interrupting-music.md
    /physics/
      collision-sprite-sprite.md
      collision-sprite-background.md
      gravity-platformer.md
    /ai/
      enemy-patrol-pattern.md
      pathfinding-simple.md
    /framework/
      raster-interrupts.md
      game-loop-basic.md
      state-machine.md
    /optimization/
      unrolled-loops.md
      table-lookups.md

  /sinclair-zx-spectrum/
    /rendering/
      software-sprite-xor.md
      attribute-management.md
      scrolling-character.md
    /input/
      keyboard-reading.md
    /audio/
      beeper-sound-effects.md
      beeper-music.md
    /physics/
      collision-detection.md
    /framework/
      interrupt-handlers.md

  /commodore-amiga/
    /rendering/
      bob-sprite-basic.md
      hardware-sprite-multiplexing.md
      copper-palette-effects.md
      blitter-rectangle-fill.md
    /input/
      mouse-reading.md
      joystick-reading.md
    /audio/
      paula-sample-playback.md
      protracker-mod-playback.md
    /framework/
      vertical-blank-interrupt.md

  /nintendo-nes/
    /rendering/
      sprite-management.md
      ppu-scrolling.md
      nametable-updates.md
    /input/
      controller-reading.md
    /audio/
      apu-music-playback.md
      apu-sound-effects.md
    /physics/
      tile-collision.md
    /framework/
      nmi-handler.md
      game-loop.md
```

---

## Integration with Curriculum

### Lesson → Pattern Flow

1. **Lesson teaches concept** with step-by-step implementation
2. **Lesson references Pattern Library** at end: "See [Pattern: Sprite Multiplexing Basic] for production-ready implementation"
3. **Pattern provides reference code** ready to copy/adapt
4. **Pattern links back to lesson** where it was taught

### Standalone Usage

**Patterns work independently:**
- Complete working code (no "fill in the blanks")
- Clear prerequisites listed
- Self-contained explanations
- Copy-paste-adapt for own projects

**Enhanced with curriculum:**
- Context from lessons provides deeper understanding
- Evolution across phases shows progression
- Genre applications from curriculum examples

---

## Integration with Vault

**Pattern → Vault Links:**
- Every pattern links to related Vault technique entries
- Links to hardware entries for technical context
- Links to games that exemplify the pattern

**Vault → Pattern Links:**
- Vault technique entries link to Pattern implementations
- Example: Vault's "Sprite Multiplexing" technique → links to all Pattern variations

**Relationship:**
- **Vault** = "What it is and why it matters" (context, history, significance)
- **Pattern** = "Here's working code you can use" (implementation, usage, trade-offs)

---

## Quality Standards

**Before Publishing a Pattern:**
- [ ] All required sections completed
- [ ] Code compiles and runs correctly
- [ ] Comments explain non-obvious logic
- [ ] Prerequisites clearly stated
- [ ] At least 3 cross-links (related patterns, vault entries)
- [ ] Evolution metadata (if part of progression)
- [ ] Genre applications identified
- [ ] Performance trade-offs documented
- [ ] Lesson references accurate

---

## Usage Examples in Lessons

### How Lessons Reference Patterns

**In Lesson Text:**
```markdown
Now that we understand how sprite multiplexing works, we can implement it in our game. For a complete, production-ready implementation with additional optimizations, see [Pattern: Sprite Multiplexing (Basic)](/patterns/c64/rendering/sprite-multiplexing-basic).
```

**In Lesson "Further Reading" Section:**
```markdown
## Further Reading

**Pattern Library:**
- [Sprite Multiplexing (Basic)](/patterns/c64/rendering/sprite-multiplexing-basic) - Production implementation
- [Raster Interrupts](/patterns/c64/framework/raster-interrupts) - Foundation technique

**Vault:**
- [Sprite Multiplexing Technique](/vault/techniques/c64-sprite-multiplexing) - Historical context
- [VIC-II Chip](/vault/hardware/vic-ii) - Hardware details
```

---

## Search and Discovery

**Multiple Access Paths:**

1. **By Platform:** Browse C64 → Rendering → find all rendering patterns
2. **By Technique Category:** All collision detection patterns across platforms
3. **By Genre:** All patterns commonly used in Shoot 'Em Ups
4. **By Phase:** All patterns introduced in Phase 3
5. **By Evolution:** Follow progression from basic → advanced versions
6. **From Lessons:** Direct links from lesson content
7. **From Vault:** Cross-links from technique entries

**Metadata Enables:**
- Filter by difficulty level
- Show patterns for specific genres
- Track evolution across phases
- Relate patterns to lessons taught

---

## Content Priorities

**Phase 1 Pattern Needs (Immediate):**
- Core framework patterns (game loop, state machine, interrupts)
- Basic rendering (sprites, scrolling, collision)
- Simple input (controller/keyboard reading)
- Basic audio (sound effect playback)

**Phase 2-4 Expansion:**
- Intermediate rendering (multiplexing, smooth scrolling)
- Physics systems (gravity, projectiles, platformer mechanics)
- Simple AI (patrol patterns, basic pathfinding)
- Audio integration (music + SFX without conflicts)

**Phase 5-8 Completion:**
- Advanced rendering (maximum sprites, complex effects)
- Sophisticated AI (behavior trees, advanced pathfinding)
- Optimization patterns (unrolled loops, table lookups, cycle counting)
- Professional production patterns (save systems, compression, loaders)

---

## Future Enhancements

**Potential Additions:**
- **Interactive Examples:** Embedded live code editors, web-based emulators
- **Video Demonstrations:** Patterns demonstrated in working games
- **Performance Profiling:** Actual cycle counts and memory usage visualized
- **Community Contributions:** Verified pattern submissions with editorial review
- **Cross-Platform Comparisons:** Show same pattern implemented across all platforms
- **Downloadable Archives:** Complete working examples as downloadable .zip files

---

*The Pattern Library transforms lessons from "how to build this game" into "here's reusable code for your own games" - giving learners a professional toolkit they can use long after completing the curriculum.*
