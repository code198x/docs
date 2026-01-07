# Unit Specification

**Version:** 2.0
**Last Updated:** 2026-01-07
**Purpose:** Complete specification for unit structure, content, and formatting across all platforms and games.

---

## Overview

Every unit is a standalone MDX file containing:
- Frontmatter metadata (YAML)
- Unit content (Markdown + MDX components)
- Code examples (platform-specific syntax)
- Screenshots demonstrating working code
- Cross-links to Vault entries and Pattern Library

**Key Principles:**
- Each unit produces a working, runnable result
- Code must compile/run and be verified with screenshots
- British English throughout (except "program" for computer programs)
- Platform-specific technical accuracy
- Progressive complexity within each game

---

## File Locations

### Unit MDX Files

```
/website/src/pages/{platform}/game-{NN}-{game-slug}/unit-{NN}-{unit-slug}.mdx
```

**Examples:**
- `/website/src/pages/commodore-64/game-01-sid-symphony/unit-01-first-notes.mdx`
- `/website/src/pages/sinclair-zx-spectrum/game-05-chambers/unit-12-enemy-chase.mdx`
- `/website/src/pages/nintendo-entertainment-system/game-09-pixel-plains/unit-03-scroll-basics.mdx`

### Code Samples

```
/code-samples/{platform}/game-{NN}-{game-slug}/unit-{NN}-{unit-slug}/
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
/website/public/images/{platform}/game-{NN}-{game-slug}/unit-{NN}-{unit-slug}/
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

Every unit MDX file starts with YAML frontmatter:

```yaml
---
title: "Unit Title - Active Voice, No Gerunds"
description: "One-sentence description of what this unit teaches and what the learner will build—concise, specific, outcome-focused."
pubDate: YYYY-MM-DD
game: 1
gameSlug: "sid-symphony"
unit: 1
unitSlug: "first-notes"
tags: ["tag1", "tag2", "tag3", "tag4"]
prevUnit: "/{platform}/game-{NN}-{slug}/unit-{NN}-{slug}"
nextUnit: "/{platform}/game-{NN}-{slug}/unit-{NN}-{slug}"
layout: "../../../layouts/UnitLayout.astro"
---
```

### Field Specifications

#### `title` (required)
- Clear, descriptive title indicating what the unit teaches
- Active voice preferred ("Setting Sprite Positions" not "How to Set Sprite Positions")
- No gerunds when possible ("Sprite Positioning" not "Positioning Sprites")
- 3-8 words typical
- No platform name (context is clear from URL)

**Examples:**
- "First Notes on the SID"
- "Reading Joystick Input"
- "Scroll Register Basics"
- "Enemy Chase Behaviour"

#### `description` (required)
- One sentence describing the unit content and outcome
- Should answer "What will I learn?" and "What will I build?"
- 15-30 words typical
- End with period

**Examples:**
- "Play your first notes on the SID chip, learning voice registers and basic waveform selection to create simple tones."
- "Read joystick input from CIA port to control sprite movement, implementing 8-directional control with hardware polling."
- "Implement horizontal scrolling using VIC-II scroll registers, creating a smoothly moving background for the runner game."

#### `pubDate` (required)
- ISO 8601 format: `YYYY-MM-DD`
- Date unit was created/published
- Used for sorting and "last updated" tracking

#### `game` (required)
- Integer 1-16+ (game number within platform curriculum)
- Matches game sequence in curriculum document

#### `gameSlug` (required)
- Lowercase, hyphen-separated game name
- Must match directory name exactly
- Examples: `sid-symphony`, `maze-raider`, `pixel-plains`

#### `unit` (required)
- Integer 1-64+ (unit number within game)
- Sequential within the game

#### `unitSlug` (required)
- Lowercase, hyphen-separated unit name
- Should be descriptive of unit content
- Examples: `first-notes`, `joystick-input`, `enemy-patterns`

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
tags: ["assembly", "6502", "ppu", "scrolling", "platformer"]
```

#### `prevUnit` / `nextUnit` (required)
- Absolute path to previous/next unit
- Use `null` for first/last unit in game
- Path format: `/{platform}/game-{NN}-{slug}/unit-{NN}-{slug}`

#### `layout` (required)
- Relative path to Astro layout component
- Typically `../../../layouts/UnitLayout.astro`
- Adjust `../` depth based on folder nesting

---

## Unit Content Structure

### Standard Section Order

1. **Opening paragraph** (required) - What this unit teaches, why it matters
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
The SID chip has three independent voices, each capable of producing sound.
This unit shows how to enable a voice and select a waveform, playing your
first notes through the C64's legendary sound chip.
```

```markdown
The NES PPU renders background graphics using tiles stored in nametables.
You'll write tile data to create a static playfield with borders, learning
PPU addressing and VRAM updates.
```

**Avoid:**
- "In this unit you will learn..."
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
## Your First Sound

This program plays a tone on SID voice 1:

\```basic
10 POKE 54296,15
20 POKE 54277,240
30 POKE 54273,28:POKE 54272,49
40 POKE 54276,17
50 FOR T=1 TO 500:NEXT
60 POKE 54276,0
\```

Run this and you'll hear a tone from the SID chip.
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
- Explain hardware registers, memory addresses, chip behaviour
- Reference chip names (VIC-II, SID, CIA, PPU, APU)
- Include memory addresses and their purposes
- Technical accuracy is critical

**Example:**
```markdown
## SID Voice Registers

Each SID voice is controlled by a set of registers:

- **$D400-$D401 (54272-54273):** Voice 1 frequency (16-bit)
- **$D404 (54276):** Voice 1 control (waveform, gate)
- **$D405 (54277):** Voice 1 attack/decay
- **$D406 (54278):** Voice 1 sustain/release

The frequency registers set the pitch. Higher values = higher pitch.
The control register selects the waveform and gates the sound on/off.
```

**Include:**
- Chip names and register addresses
- Bit-level details when relevant
- Hardware timing considerations
- Limitations and gotchas

**Avoid:**
- Repeating code line-by-line
- Excessive beginner hand-holding in later games
- Claiming BASIC matches assembly speed
- Modern programming analogies unless genuinely useful

#### From the Vault (Optional)

**Purpose:** Link to related Vault entries for deeper context.

**Format:**
```markdown
## From the Vault

- [SID Chip](/vault/hardware/sid-6581) - Complete register reference
- [Rob Hubbard](/vault/people/rob-hubbard) - SID music pioneer
- [Commando](/vault/games/commando-c64) - Classic SID soundtrack
```

**When to include:**
- People: Programmers, musicians, artists who pioneered relevant techniques
- Companies: Studios who innovated in this area
- Games: Titles that used this technique notably
- Techniques: Related programming methods
- Hardware: Chip/component deep dives

**When to omit:**
- Early units in Game 1 (learners need core concepts first)
- When links would be redundant
- When forcing historical connections

#### Pattern Library (Optional)

**Purpose:** Link to reusable code patterns demonstrated in this unit.

**Format:**
```markdown
## Pattern Library

This unit demonstrates these reusable patterns:

- [SID Voice Initialisation](/patterns/commodore-64/audio/sid-voice-init) - Setting up voices
- [Note Frequency Table](/patterns/commodore-64/audio/note-frequencies) - Pitch lookup

You can adapt these patterns for your own projects.
```

**When to include:**
- When unit introduces a reusable technique
- When code is production-ready (not just conceptual)
- Later in games when patterns accumulate

**When to omit:**
- First few units (too early)
- Highly specific one-off code
- Incomplete demonstrations

#### What You've Learnt (Required)

**Purpose:** Concrete bullet-point summary of new capabilities.

**Format:**
```markdown
## What You've Learnt

- **SID voices** - Three independent sound generators, each with full control
- **Frequency registers** - 16-bit value controls pitch ($D400-$D401 for voice 1)
- **Waveforms** - Triangle, sawtooth, pulse, and noise via control register
- **Gate bit** - Bit 0 of control register starts/stops the sound
- **ADSR envelope** - Attack, decay, sustain, release shape the sound
```

**Guidelines:**
- 4-8 bullet points
- Start with bold concept name
- Follow with concrete capability or knowledge
- Focus on what they can NOW DO, not just abstract concepts
- Use past tense ("learnt") per British English

**Avoid:**
- Vague statements ("You learned about sound")
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
   - Blank screen (crash or initialisation failure)

**Example of proper verification:**
```markdown
Screenshot verified: Shows blue background (VIC-II $D021=#6), white sprite
positioned at centre screen, sprite pointer correctly set. No error messages
visible. ✅
```

**Failure cases require code fix:**
- Error message visible → Fix code, recompile, recapture
- Blank screen → Debug initialisation, recapture
- Wrong output → Verify code logic, recapture

### Audio Output

**For SID, beeper, Paula, APU units:**
- Capture `.wav` file of audio output
- Note duration and characteristics in unit
- Include waveform visualisation if helpful

---

## Platform-Specific Rules

### Commodore 64

**BASIC (Gateway games):**
- NO indentation (BASIC V2 standard)
- Lowercase keywords in `.bas` files
- Uppercase keywords in MDX display
- British English (colour, learnt)
- EXCEPT "program" for computer programs

**Reserved variables - NEVER USE:**
- `ST` - I/O status (causes syntax error)
- `TI` - Jiffy clock (conflicts with timing)
- `TI$` - Time string (runtime issues)

**Assembly (main curriculum):**
- ACME assembler syntax
- Lowercase mnemonics
- Lowercase hex (`$d020` not `$D020`)
- Include comments explaining VIC-II, SID, CIA registers

**Sprite positioning requirements (BASIC and Assembly):**

**X-coordinate MSB ($D010) - CRITICAL:**
- The C64 screen is 320 pixels wide, but sprite X registers only hold 0-255
- **MUST use $D010 (53264) MSB register** for X positions > 255
- Introduce MSB concept in first sprite positioning unit
- ALL sprite examples after introduction must handle MSB correctly

**Boundary checking - MANDATORY:**
- Negative coordinates cause `?ILLEGAL QUANTITY ERROR` crashes
- X coordinates must be 0-511 (with MSB)
- Y coordinates must be 0-255
- **Always validate before POKE**

### ZX Spectrum

**BASIC (Gateway games):**
- NO indentation
- Lowercase keywords in `.bas` files
- Uppercase keywords in MDX display
- British English throughout
- Sinclair BASIC syntax (no extended keywords)

**Assembly (main curriculum):**
- Z80 mnemonics
- Software sprites (no hardware sprite system)
- Attribute system colour management
- UDG (User-Defined Graphics) techniques

**Specific challenges:**
- Attribute clash explanations
- Beeper vs AY-3-8912 sound
- Memory contention on display access

### Commodore Amiga

**AMOS (Gateway games):**
- AMOS BASIC syntax
- BOB (Blitter Object) sprite system
- Screen and Palette commands

**Assembly (main curriculum):**
- 68000 assembly syntax
- Custom chipset (Agnus, Denise, Paula)
- Copper list programming
- Blitter operations
- OCS/ECS/AGA progression in later games

### Nintendo NES

**Assembly only (no gateway):**
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
- PPU address latch behaviour

---

## Cross-Linking Strategy

### Vault Links

**Inline contextual links:**
```markdown
The SID chip's distinctive sound, showcased by composers like
[Rob Hubbard](/vault/people/rob-hubbard) in titles like
[Commando](/vault/games/commando-c64), came from its analog filter
and three independent voices.
```

**"From the Vault" section:**
- Link to 3-5 most relevant Vault entries
- Include brief description of what reader will find
- Don't link to same entry in every unit

### Pattern Library Links

**"Pattern Library" section:**
- Link to patterns demonstrated in this unit
- Brief description of pattern utility
- Note which game introduced the pattern

**Example:**
```markdown
## Pattern Library

- [Sprite Multiplexing (Basic)](/patterns/commodore-64/rendering/sprite-multiplex-basic) -
  Game 9 technique for 16 sprites using sorted lists
- [Sprite Multiplexing (Advanced)](/patterns/commodore-64/rendering/sprite-multiplex-advanced) -
  Game 12 optimisation with raster-stable timing
```

---

## Progressive Complexity

### Early Games (1-4)
- Simple, direct explanations
- Focus on immediate results
- Minimal theory
- Short code examples (5-15 lines)

**Example tone:**
> POKE 54296,15 sets the SID volume to maximum. Without this, you won't
> hear anything regardless of what else you configure.

### Middle Games (5-10)
- More complex code (20-40 lines)
- Explain "why" alongside "how"
- Introduce optimisation concepts
- Multiple examples showing variations

**Example tone:**
> The SID's filter is controlled by registers $D415-$D418. By sweeping
> the cutoff frequency during playback, you create the classic "wah"
> effect heard in countless C64 soundtracks.

### Later Games (11-16)
- Production-quality code
- Performance optimisation details
- Multiple techniques compared
- Hardware timing precision

**Example tone:**
> Multi-speed playback requires cycle-exact timing. This implementation
> uses raster interrupts to call the player routine multiple times per
> frame, enabling the complex arrangements heard in late-era SID music.

**Key principle:** Early games explain more, later games assume more.

---

## Writing Style

### British English

**Always:**
- colour (not color)
- learnt (not learned)
- optimise (not optimize)
- grey (not gray)
- behaviour (not behavior)
- centre (not center)

**Exception:**
- "program" for computer programs (not "programme")

### Voice and Tone

**Do:**
- Direct, clear explanations
- Active voice
- Present tense for code behaviour
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
10 REM INITIALISE SID
20 POKE 54296,15     : REM VOLUME MAX
30 POKE 54277,240    : REM ATTACK/DECAY
```

**Assembly examples:**
```asm
    lda #$0f
    sta $d418       ; Volume max
    lda #$f0
    sta $d405       ; Attack/decay voice 1
```

**Guidelines:**
- Comment hardware register writes
- Explain non-obvious logic
- Don't comment obvious operations
- Early games: More comments
- Later games: Fewer comments (assume knowledge)

---

## Validation Checklist

Before unit publication, verify:

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
- [ ] "What You've Learnt" summarises actual capabilities
- [ ] Code formatting matches platform standards

---

## Example: Complete Unit Template

```markdown
---
title: "First Notes on the SID"
description: "Play your first notes on the SID chip, learning voice registers and waveform selection to create simple tones."
pubDate: 2026-01-07
game: 1
gameSlug: "sid-symphony"
unit: 1
unitSlug: "first-notes"
tags: ["basic", "sid", "sound", "rhythm"]
prevUnit: null
nextUnit: "/commodore-64/game-01-sid-symphony/unit-02-adsr-envelopes"
layout: "../../../layouts/UnitLayout.astro"
---

The SID chip has three independent voices, each capable of producing sound.
This unit shows how to enable a voice and select a waveform, playing your
first notes through the C64's legendary sound chip.

## Your First Sound

This program plays a tone on SID voice 1:

\```basic
10 POKE 54296,15
20 POKE 54277,240
30 POKE 54273,28:POKE 54272,49
40 POKE 54276,17
50 FOR T=1 TO 500:NEXT
60 POKE 54276,0
\```

![SID playing a note](/images/commodore-64/game-01-sid-symphony/unit-01-first-notes/example-1.png)

Run this and you'll hear a tone from the SID chip.

## SID Voice Registers

Each voice is controlled by a set of registers. For voice 1:

- **$D400-$D401 (54272-54273):** Frequency (16-bit, low byte first)
- **$D404 (54276):** Control register (waveform and gate)
- **$D405 (54277):** Attack/Decay
- **$D406 (54278):** Sustain/Release
- **$D418 (54296):** Volume (bits 0-3)

The frequency value determines pitch. We're using 7217 (28×256+49),
which produces a middle-C note.

## Control Register

The control register ($D404) combines waveform selection with the gate:

- Bit 0: Gate (1=start sound, 0=release)
- Bit 4: Triangle wave
- Bit 5: Sawtooth wave
- Bit 6: Pulse wave
- Bit 7: Noise

We used 17 ($11), which is triangle (16) + gate (1).

## From the Vault

- [SID Chip](/vault/hardware/sid-6581) - Complete register reference
- [Rob Hubbard](/vault/people/rob-hubbard) - Master of SID composition

## What You've Learnt

- **SID voices** - Three independent sound generators
- **Frequency registers** - 16-bit value controls pitch
- **Control register** - Waveform selection and gate bit
- **Volume register** - Global volume at $D418
- **Gate bit** - Starts and releases the sound
```

---

## Version History

- **2.0 (2026-01-07):** Complete rewrite for games/units model. Renamed from LESSON-SPECIFICATION.md.
- **1.0 (2025-01-15):** Original specification using phases/tiers/lessons model.
