# Lesson Specification

**Version:** 1.0
**Last Updated:** 2025-01-15
**Purpose:** Complete specification for lesson structure, content, and formatting across all platforms and phases.

---

## Overview

Every lesson is a standalone MDX file containing:
- Frontmatter metadata (YAML)
- Lesson content (Markdown + MDX components)
- Code examples (platform-specific syntax)
- Screenshots demonstrating working code
- Cross-links to Vault entries and Pattern Library

**Key Principles:**
- Each lesson teaches ONE core concept
- Code must compile/run and be verified with screenshots
- British English throughout (except "program" for computer programs)
- Platform-specific technical accuracy
- Progressive disclosure (simple in Phase 1, complex in Phase 8)

---

## File Locations

### Lesson MDX Files

```
/website/src/pages/{platform}/phase-{N}/tier-{NN}/lesson-{NNN}.mdx
```

**Examples:**
- `/website/src/pages/commodore-64/phase-1/tier-1/lesson-001.mdx`
- `/website/src/pages/sinclair-zx-spectrum/phase-2/tier-5/lesson-137.mdx`
- `/website/src/pages/nintendo-entertainment-system/phase-1/tier-1/lesson-001.mdx`

### Code Samples

```
/code-samples/{platform}/phase-{N}/tier-{NN}/lesson-{NNN}/
```

**Naming conventions:**
- `example-1.{ext}` - Simple demonstration (5-15 lines)
- `example-2.{ext}` - Complex/complete demonstration (15-40 lines)
- `{concept-name}.{ext}` - Descriptive names for specific techniques

**Extensions by platform:**
- C64 BASIC: `.bas`
- C64 Assembly: `.asm`
- ZX Spectrum BASIC: `.bas`
- ZX Spectrum Assembly: `.asm`
- Amiga AMOS: `.amos`
- Amiga Assembly: `.asm`
- NES Assembly: `.asm`

### Screenshots

```
/website/public/images/{platform}/phase-{N}/tier-{NN}/lesson-{NNN}/
```

**Naming conventions:**
- `example-1.png` - Screenshot of example-1 running
- `example-2.png` - Screenshot of example-2 running
- `{descriptive-name}.png` - For specific visual concepts

**Additional media:**
- `.wav` files for audio demonstrations (SID, beeper, etc.)
- `.mp4` files for animation demonstrations (rare, prefer PNG sequences)

---

## Frontmatter Structure

Every lesson MDX file starts with YAML frontmatter:

```yaml
---
title: "Lesson Title - Active Voice, No Gerunds"
description: "One-sentence description of what this lesson teaches and what the learner will build—concise, specific, outcome-focused."
pubDate: YYYY-MM-DD
phase: N
tier: NN
lessonNumber: NNN
tags: ["tag1", "tag2", "tag3", "tag4"]
prevLesson: "/{platform}/phase-{N}/tier-{NN}/lesson-{NNN}"
nextLesson: "/{platform}/phase-{N}/tier-{NN}/lesson-{NNN}"
layout: "../../../../layouts/LessonLayout.astro"
---
```

### Field Specifications

#### `title` (required)
- Clear, descriptive title indicating what the lesson teaches
- Active voice preferred ("Setting Sprite Positions" not "How to Set Sprite Positions")
- No gerunds when possible ("Sprite Positioning" not "Positioning Sprites")
- 3-8 words typical
- No platform name (context is clear from URL)

**Examples:**
- "Sprite Positioning Basics"
- "Reading Joystick Input"
- "SID Chip Envelope Control"
- "Nametable Updates"

#### `description` (required)
- One sentence describing the lesson content and outcome
- Should answer "What will I learn?" and "What will I build?"
- 15-30 words typical
- End with period

**Examples:**
- "Learn to position hardware sprites using VIC-II registers, creating a moving player character controlled by X and Y coordinates."
- "Read joystick input from CIA port to control sprite movement, implementing 8-directional control with hardware polling."
- "Control ADSR envelope on SID chip voices to shape sound effects, creating laser, explosion, and coin collection sounds."

#### `pubDate` (required)
- ISO 8601 format: `YYYY-MM-DD`
- Date lesson was created/published
- Used for sorting and "last updated" tracking

#### `phase` (required)
- Integer 0-8
- Phase 0 = Gateway languages (BASIC, AMOS, etc.)
- Phases 1-8 = Assembly language

#### `tier` (required)
- Integer 1-16
- Represents game genre/complexity tier within phase

#### `lessonNumber` (required)
- Integer 1-4096 (unique across entire platform)
- Calculated as: `(phase × 512) + (tier × 32) + lesson_in_tier`
- Example: Phase 1, Tier 1, Lesson 5 = (1 × 512) + (1 × 32) + 5 = 549

#### `tags` (required)
- Array of 3-6 strings
- Lowercase, hyphen-separated
- Categories: language, chip/hardware, concept, genre

**Tag categories:**
- **Language:** `basic`, `assembly`, `6510`, `z80`, `6502`, `68000`
- **Hardware:** `vic-ii`, `sid`, `cia`, `ppu`, `apu`, `sprites`, `raster`, `copper`
- **Concepts:** `input`, `sound`, `graphics`, `physics`, `collision`, `scrolling`
- **Genre:** `shooter`, `platformer`, `puzzle`, `rpg`

**Example tag combinations:**
```yaml
tags: ["assembly", "6510", "vic-ii", "sprites", "shooter"]
tags: ["basic", "sid", "sound", "music"]
tags: ["assembly", "6502", "ppu", "nametable", "platformer"]
```

#### `prevLesson` / `nextLesson` (required)
- Absolute path to previous/next lesson
- Use `null` for first/last lesson in sequence
- Path format: `/{platform}/phase-{N}/tier-{NN}/lesson-{NNN}`

#### `layout` (required)
- Relative path to Astro layout component
- Typically `../../../../layouts/LessonLayout.astro`
- Adjust `../` depth based on folder nesting

---

## Lesson Content Structure

### Standard Section Order

1. **Opening paragraph** (required) - What this lesson teaches, why it matters
2. **Code Example(s)** (required) - Working demonstrations
3. **Explanation section(s)** (required) - How the code works
4. **From the Vault** (optional) - Links to related Vault entries
5. **Pattern Library** (optional) - Links to reusable code patterns
6. **What You've Learnt** (required) - Bullet summary

### Section Guidelines

#### Opening Paragraph

**Purpose:** Orient the learner immediately to what they'll learn and build.

**Structure:**
- 2-4 sentences
- State the concept being taught
- Briefly mention what they'll build/demonstrate
- No forced historical references or hype

**Good examples:**
```markdown
The VIC-II chip can display 8 hardware sprites independently from the background.
This lesson shows how to position sprites using memory-mapped registers,
creating a player character that moves across the screen.
```

```markdown
The NES PPU renders background graphics using tiles stored in nametables.
You'll write tile data to create a static Pong playfield with borders and
center line, learning PPU addressing and VRAM updates.
```

**Avoid:**
- "In this lesson you will learn..."
- "Have you ever wondered how..."
- "This technique powered [famous game]..."
- Marketing speak or excessive enthusiasm

#### Code Examples

**Requirements:**
- Must compile/assemble without errors
- Must run on actual hardware/accurate emulator
- Must be verified with screenshots (see Screenshot Requirements)
- Lowercase keywords in `.bas` files (petcat compatibility)
- Uppercase keywords in MDX display
- Platform-specific syntax rules

**Simple example pattern:**
```markdown
## Your First Sprite

This program enables sprite 0 and positions it at X=100, Y=50:

\```basic
10 POKE 53269,1
20 POKE 53248,100
30 POKE 53249,50
40 GOTO 40
\```

Run this and you'll see the sprite appear on screen.
```

**Complex example pattern:**
```markdown
## Moving Sprite with Joystick

\```basic
10 POKE 53269,1:X=100:Y=50
20 J=PEEK(56320)AND 15
30 IF J=14 THEN Y=Y-1
40 IF J=13 THEN Y=Y+1
50 IF J=11 THEN X=X-1
60 IF J=7 THEN X=X+1
70 POKE 53248,X:POKE 53249,Y
80 GOTO 20
\```

![Sprite moving with joystick control](/images/commodore-64/phase-1/tier-1/lesson-003/example-2.png)

This creates smooth joystick-controlled movement using CIA port polling.
```

**Code formatting rules:**

**BASIC (in `.bas` files):**
```basic
10 rem lowercase keywords
20 poke 53280,0
30 print "hello"
```

**BASIC (in MDX display):**
```basic
10 REM UPPERCASE KEYWORDS
20 POKE 53280,0
30 PRINT "HELLO"
```

**Assembly (all contexts):**
```asm
    lda #$00        ; Lowercase mnemonics
    sta $d020       ; Lowercase hex
    rts
```

#### Explanation Sections

**Purpose:** Explain how the code works, why it works that way, and what the hardware is doing.

**Structure:**
- Use descriptive headings (not "How It Works" repeatedly)
- Explain hardware registers, memory addresses, chip behavior
- Reference chip names (VIC-II, SID, CIA, PPU, APU)
- Include memory addresses and their purposes
- Technical accuracy is critical

**Example:**
```markdown
## VIC-II Sprite Registers

Sprite positions are controlled by memory-mapped registers in the VIC-II chip:

- **$D000 (53248):** Sprite 0 X-coordinate (0-255 within screen)
- **$D001 (53249):** Sprite 0 Y-coordinate (0-255)
- **$D015 (53269):** Sprite enable register (bit 0 = sprite 0)

Writing to these registers updates the sprite position immediately. The VIC-II
reads these values 50 times per second (PAL) and draws sprites independently
from your program's execution.

**X-coordinate expansion:** Bit 0 of $D010 extends sprite 0's X position
beyond 255, enabling placement across the full 320-pixel width.
```

**Include:**
- Chip names and register addresses
- Bit-level details when relevant
- Hardware timing considerations
- Limitations and gotchas

**Avoid:**
- Repeating code line-by-line
- Excessive beginner hand-holding in later phases
- Claiming BASIC matches assembly speed
- Modern programming analogies unless genuinely useful

#### From the Vault (Optional)

**Purpose:** Link to related Vault entries for deeper context.

**Format:**
```markdown
## From the Vault

- [VIC-II Chip](/vault/hardware/vic-ii-6569) - Complete register reference
- [Sprites](/vault/techniques/sprites) - Hardware sprite systems across platforms
- [Andrew Braybrook](/vault/people/andrew-braybrook) - Sprite multiplexing pioneer
- [Uridium](/vault/games/uridium-c64) - Advanced sprite techniques
```

**When to include:**
- People: Programmers, musicians, artists who pioneered relevant techniques
- Companies: Studios who innovated in this area
- Games: Titles that used this technique notably
- Techniques: Related programming methods
- Hardware: Chip/component deep dives

**When to omit:**
- Early Phase 1 lessons (learners need core concepts first)
- When links would be redundant (every sprite lesson doesn't need VIC-II link)
- When forcing historical connections

#### Pattern Library (Optional)

**Purpose:** Link to reusable code patterns demonstrated in this lesson.

**Format:**
```markdown
## Pattern Library

This lesson demonstrates these reusable patterns:

- [Sprite Initialization](/patterns/commodore-64/rendering/sprite-init-basic) - Setting up sprite pointers and registers
- [Joystick Polling](/patterns/commodore-64/input/joystick-poll-basic) - Reading CIA port for input

You can adapt these patterns for your own projects.
```

**When to include:**
- When lesson introduces a reusable technique
- When code is production-ready (not just conceptual)
- Later in tiers (Tier 3+) when patterns accumulate

**When to omit:**
- First lessons in Tier 1 (too early)
- Highly specific one-off code
- Incomplete demonstrations

#### What You've Learnt (Required)

**Purpose:** Concrete bullet-point summary of new capabilities.

**Format:**
```markdown
## What You've Learnt

- **Hardware sprites** - VIC-II can display 8 independent moveable objects
- **Sprite registers** - $D000-$D001 control X/Y position, $D015 enables sprites
- **Memory-mapped I/O** - Writing to hardware registers updates display immediately
- **Joystick polling** - Reading CIA port $DC00 detects directional input
- **Coordinate systems** - X (0-255 + extension), Y (0-255) screen positioning
- **Real-time updates** - Updating position registers in loop creates smooth movement
```

**Guidelines:**
- 4-8 bullet points
- Start with bold concept name
- Follow with concrete capability or knowledge
- Focus on what they can NOW DO, not just abstract concepts
- Use past tense ("learnt") per British English

**Avoid:**
- Vague statements ("You learned about sprites")
- Repeating title/description
- Motivational language ("Great job!")

---

## Screenshot Requirements

**MANDATORY:** Every code example that produces visual or audio output MUST have verification.

### Visual Output

1. **Capture screenshot** after code compilation using emulator
2. **Use Read tool** to view the screenshot
3. **Verify contents** - describe what you see
4. **Check for errors:**
   - `?SYNTAX ERROR IN [line]` (compilation failure)
   - `?UNDEF'D STATEMENT ERROR IN [line]` (missing GOSUB target)
   - `?ILLEGAL QUANTITY ERROR IN [line]` (value out of range)
   - Blank screen (crash or initialization failure)

**Example of proper verification:**
```markdown
Screenshot verified: Shows blue background (VIC-II $D021=#6), white sprite
positioned at center screen, sprite pointer correctly set. No error messages
visible. ✅
```

**Failure cases require code fix:**
- Error message visible → Fix code, recompile, recapture
- Blank screen → Debug initialization, recapture
- Wrong output → Verify code logic, recapture

### Audio Output

**For SID, beeper, Paula, APU lessons:**
- Capture `.wav` file of audio output
- Note duration and characteristics in lesson
- Include waveform visualization if helpful

**Example:**
```markdown
![Laser sound effect waveform](/images/commodore-64/phase-1/tier-1/lesson-004/laser.wav)

Sharp attack (A=0, D=9) creates the characteristic laser sound.
```

---

## Platform-Specific Rules

### Commodore 64

**BASIC (Phase 0):**
- NO indentation (BASIC V2 standard)
- Lowercase keywords in `.bas` files
- Uppercase keywords in MDX display
- British English (colour, learnt)
- EXCEPT "program" for computer programs

**Reserved variables - NEVER USE:**
- `ST` - I/O status (causes syntax error)
- `TI` - Jiffy clock (conflicts with timing)
- `TI$` - Time string (runtime issues)

**Assembly (Phases 1-8):**
- ACME assembler syntax
- Lowercase mnemonics
- Lowercase hex (`$d020` not `$D020`)
- Include comments explaining VIC-II, SID, CIA registers

**Sprite positioning requirements (BASIC and Assembly):**

**X-coordinate MSB ($D010) - CRITICAL:**
- The C64 screen is 320 pixels wide, but sprite X registers ($D000, $D002, etc.) only hold 0-255
- **MUST use $D010 (53264) MSB register** for X positions > 255
- Introduce MSB concept in first sprite positioning lesson
- ALL sprite examples after introduction must handle MSB correctly

**Example (Assembly):**
```asm
    lda #200
    sta $d000       ; Sprite 0 X position (low byte)

    lda $d010
    ora #%00000001  ; Set bit 0 for sprite 0 MSB
    sta $d010       ; X = 256 + 200 = 456 (off-screen right)
```

**Example (BASIC):**
```basic
100 X=200
110 POKE 53248,X              : REM LOW BYTE
120 IF X>255 THEN POKE 53264,PEEK(53264) OR 1
130 IF X<=255 THEN POKE 53264,PEEK(53264) AND 254
```

**Boundary checking - MANDATORY:**
- Negative coordinates cause `?ILLEGAL QUANTITY ERROR` crashes
- X coordinates must be 0-511 (with MSB)
- Y coordinates must be 0-255
- **Always validate before POKE:**

```basic
100 X=X+DX:Y=Y+DY
110 IF X<0 THEN X=0
120 IF X>319 THEN X=319
130 IF Y<0 THEN Y=0
140 IF Y>199 THEN Y=199
150 POKE 53248,X AND 255
160 IF X>255 THEN POKE 53264,PEEK(53264)OR 1:GOTO 180
170 POKE 53264,PEEK(53264)AND 254
180 POKE 53249,Y
```

**Assembly boundary checking:**
```asm
    ; Check Y lower bound
    lda sprite_y
    bpl +           ; Branch if positive
    lda #0
    sta sprite_y
+
    ; Check Y upper bound
    cmp #200
    bcc +
    lda #199
    sta sprite_y
+
    ; Similar for X with 0-319 range
```

**Validation:**
```bash
./scripts/validate-bas.sh example-1.bas  # BASIC validation
```

### ZX Spectrum

**BASIC (Phase 0):**
- NO indentation
- Lowercase keywords in `.bas` files
- Uppercase keywords in MDX display
- British English throughout
- Sinclair BASIC syntax (no extended keywords)

**Assembly (Phases 1-8):**
- Z80 mnemonics
- Software sprites (no hardware sprite system)
- Attribute system color management
- UDG (User-Defined Graphics) techniques

**Specific challenges:**
- Attribute clash explanations
- Beeper vs AY-3-8912 sound
- Memory contention on display access

### Commodore Amiga

**AMOS (Phase 0):**
- AMOS BASIC syntax
- BOB (Blitter Object) sprite system
- Screen and Palette commands

**Assembly (Phases 1-8):**
- 68000 assembly syntax
- Custom chipset (Agnus, Denise, Paula)
- Copper list programming
- Blitter operations
- OCS/ECS/AGA progression in later phases

### Nintendo NES

**Assembly (Phases 1-8):**
- 6502 assembly (ca65 syntax)
- PPU tile-based graphics
- CHR-ROM data
- Nametable addressing
- Sprite OAM structure
- APU sound channels
- Controller reading
- Mapper progression (NROM → MMC1 → MMC3)

**Specific challenges:**
- 8 sprites per scanline limit
- VRAM access during VBlank only
- PPU address latch behavior

---

## Cross-Linking Strategy

### Vault Links

**Inline contextual links:**
```markdown
The VIC-II chip's sprite multiplexing technique, pioneered by
[Andrew Braybrook](/vault/people/andrew-braybrook) in
[Uridium](/vault/games/uridium-c64), allows displaying 20+ sprites
using raster interrupts.
```

**"From the Vault" section:**
- Link to 3-5 most relevant Vault entries
- Include brief description of what reader will find
- Don't link to same entry in every lesson

### Pattern Library Links

**"Pattern Library" section:**
- Link to patterns demonstrated in this lesson
- Brief description of pattern utility
- Note which phase introduced the pattern

**Example:**
```markdown
## Pattern Library

- [Sprite Multiplexing (Basic)](/patterns/commodore-64/rendering/sprite-multiplex-basic) -
  Phase 2 technique for 16 sprites using sorted lists
- [Sprite Multiplexing (Advanced)](/patterns/commodore-64/rendering/sprite-multiplex-advanced) -
  Phase 5 optimization with raster-stable timing
```

---

## Progressive Disclosure

### Phase 1: Foundation
- Simple, direct explanations
- Focus on immediate results
- Minimal theory
- Short code examples (5-15 lines)

**Example tone:**
> POKE 53280,0 changes the border color to black. The VIC-II chip reads
> this register and updates the display.

### Phase 3-4: Intermediate
- More complex code (20-40 lines)
- Explain "why" alongside "how"
- Introduce optimization concepts
- Multiple examples showing variations

**Example tone:**
> The VIC-II updates sprite positions during the vertical blank period.
> By synchronizing writes to this timing window, you avoid mid-screen
> sprite glitches.

### Phase 6-8: Advanced
- Production-quality code
- Performance optimization details
- Multiple techniques compared
- Hardware timing precision

**Example tone:**
> Raster-stable sprite multiplexing requires cycle-exact timing. This
> implementation uses double-buffered sort lists to maintain stability
> across PAL/NTSC, compensating for badline delays.

**Key principle:** Early phases explain more, later phases assume more.

---

## Writing Style

### British English

**Always:**
- colour (not color)
- learnt (not learned)
- optimise (not optimize)
- grey (not gray)

**Exception:**
- "program" for computer programs (not "programme")

### Voice and Tone

**Do:**
- Direct, clear explanations
- Active voice
- Present tense for code behavior
- Technical precision
- Honest about limitations (BASIC speed, hardware constraints)

**Don't:**
- Excessive enthusiasm or hype
- "You will learn..." (just teach it)
- Forced nostalgia ("Remember when...")
- Marketing speak
- Apologies for platform limitations

### Code Comments

**BASIC examples:**
```basic
10 REM INITIALIZE SPRITE SYSTEM
20 POKE 53269,1       : REM ENABLE SPRITE 0
30 POKE 2040,13       : REM SET SPRITE POINTER TO BLOCK 13
```

**Assembly examples:**
```asm
    lda #$01
    sta $d015       ; Enable sprite 0
    lda #$0d
    sta $07f8       ; Sprite pointer to block 13
```

**Guidelines:**
- Comment hardware register writes
- Explain non-obvious logic
- Don't comment obvious operations
- Phase 1: More comments
- Phase 8: Fewer comments (assume knowledge)

---

## Validation Checklist

Before lesson publication, verify:

- [ ] Code compiles/assembles without errors
- [ ] Code runs on accurate emulator/hardware
- [ ] Screenshots captured and verified with Read tool
- [ ] No error messages in screenshots
- [ ] No blank screens (indicates crashes)
- [ ] British English throughout (except "program")
- [ ] No American spellings (color, optimize, learned)
- [ ] No reserved variables (ST, TI, TI$) in C64 BASIC
- [ ] Frontmatter complete and accurate
- [ ] Tags appropriate and specific
- [ ] Cross-links functional (Vault, Pattern Library)
- [ ] "What You've Learnt" summarizes actual capabilities
- [ ] Code formatting matches platform standards

---

## Common Mistakes

### Content Errors

❌ **Claiming BASIC matches assembly speed**
```markdown
This BASIC program creates smooth scrolling just like professional games!
```

✅ **Honest about limitations**
```markdown
This BASIC program demonstrates the scrolling concept. Assembly lessons
will show full-speed implementation.
```

---

❌ **Forced historical references**
```markdown
This is the same sprite register that every C64 game used!
```

✅ **Meaningful context when relevant**
```markdown
Andrew Braybrook's sprite multiplexing in Uridium showed 20+ sprites by
repositioning the same 8 hardware sprites mid-screen using raster interrupts.
```

---

❌ **Vague learning outcomes**
```markdown
## What You've Learnt
- You learned about sprites
- Sprites are cool
- You can make games now
```

✅ **Concrete capabilities**
```markdown
## What You've Learnt
- **Sprite enable register** - $D015 controls which sprites are visible
- **Sprite positioning** - $D000/$D001 set X/Y coordinates
- **Sprite pointers** - $07F8 points to 64-byte sprite data
```

---

### Technical Errors

❌ **Unverified code**
```basic
10 GOSUB 1000
20 PRINT "DONE"
30 END
```
(Line 1000 doesn't exist → ?UNDEF'D STATEMENT ERROR)

✅ **Verified with all targets present**
```basic
10 GOSUB 1000
20 PRINT "DONE"
30 END
1000 REM SUBROUTINE
1010 RETURN
```

---

❌ **Platform confusion**
```markdown
The NES VIC-II chip controls sprite display...
```

✅ **Correct chip names**
```markdown
The NES PPU (Picture Processing Unit) controls sprite display...
```

---

### Formatting Errors

❌ **Mixed case in BASIC display**
```basic
10 POKE 53280,0
20 print "hello"
```

✅ **Consistent uppercase in MDX**
```basic
10 POKE 53280,0
20 PRINT "HELLO"
```

---

❌ **American English**
```markdown
Change the color to optimize the display...
```

✅ **British English**
```markdown
Change the colour to optimise the display...
```

---

## Example: Complete Lesson Template

```markdown
---
title: "Sprite Positioning Basics"
description: "Position hardware sprites using VIC-II registers, creating a moveable player character with X and Y coordinate control."
pubDate: 2025-01-15
phase: 1
tier: 1
lessonNumber: 545
tags: ["assembly", "6510", "vic-ii", "sprites", "shooter"]
prevLesson: "/commodore-64/phase-1/tier-1/lesson-544"
nextLesson: "/commodore-64/phase-1/tier-1/lesson-546"
layout: "../../../../layouts/LessonLayout.astro"
---

The VIC-II chip can display 8 hardware sprites independently from the background.
This lesson shows how to position a sprite using memory-mapped registers, creating
a player character that moves across the screen.

## Enable and Position Sprite 0

This program enables sprite 0 and positions it at X=100, Y=50:

\```asm
    lda #$01
    sta $d015       ; Enable sprite 0

    lda #100
    sta $d000       ; X position

    lda #50
    sta $d001       ; Y position

loop:
    jmp loop
\```

![Sprite visible at position 100,50](/images/commodore-64/phase-1/tier-1/lesson-545/example-1.png)

The sprite appears immediately when you run this code.

## VIC-II Sprite Registers

Sprite positions are controlled by memory-mapped registers:

- **$D000 (53248):** Sprite 0 X-coordinate (0-255)
- **$D001 (53249):** Sprite 0 Y-coordinate (0-255)
- **$D015 (53269):** Sprite enable register (bit 0 = sprite 0)

Writing to these registers updates the hardware immediately. The VIC-II reads
these values 50 times per second (PAL) and draws sprites independently from
your program.

### X-Coordinate Extension

For X positions beyond 255, use bit 0 of $D010:

\```asm
    lda #$01
    sta $d010       ; Enable X extension for sprite 0

    lda #100
    sta $d000       ; X = 256 + 100 = 356
\```

This extends the X range to 0-511, covering the full screen width (320 pixels)
and beyond.

## From the Vault

- [VIC-II Chip](/vault/hardware/vic-ii-6569) - Complete register reference
- [Sprites](/vault/techniques/hardware-sprites) - Sprite systems across platforms

## What You've Learnt

- **Hardware sprites** - VIC-II displays 8 independent moveable objects
- **Sprite registers** - $D000/$D001 control X/Y position, $D015 enables
- **Memory-mapped I/O** - Writing to registers updates display immediately
- **Coordinate system** - X (0-511 with extension), Y (0-255)
- **Real-time display** - VIC-II reads registers 50 times per second
\```

---

## Version History

- **1.0 (2025-01-15):** Initial specification after clean slate reset
