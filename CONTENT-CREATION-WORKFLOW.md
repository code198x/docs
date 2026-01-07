# Content Creation Workflow

**Last Updated:** 2026-01-07
**Version:** 2.0
**Purpose:** Complete end-to-end guide for creating curriculum units, from initial planning through publication
**Scope:** Universal workflow applying to all platforms and games

---

## Overview and Philosophy

**Purpose:** Complete end-to-end guide for creating curriculum units, from initial planning through publication.

**Scope:** Universal workflow applying to all platforms and games, with platform-specific and language-specific sections where needed.

**Core Principles:**
- **Curriculum alignment is mandatory** - No work begins without verified alignment to specifications
- **Quality over speed** - Three core criteria must be met
- **Platform skills handle execution** - This workflow defines process, platform skills execute technical details
- **Integration by design** - Vault, Pattern Library, and cross-references built in, not bolted on

**Unit Archetypes (Design Tools, Not Labels):**

Units fall into natural patterns. Content communicates purpose; no visual markers needed.

- **Discovery** - Standard teaching unit (most common)
- **Challenge** - Problem-solving exercise using recent skills
- **Synthesis** - Combining multiple concepts into complete program
- **Deep Dive** - Hardware internals and "why it works"
- **Tutorial** - Step-by-step guided construction
- **Showcase** - Demonstrates what's possible (inspirational, before teaching)

**Three Core Quality Criteria:**

1. **It Works Fast** - Immediate visible/audible feedback, creates something impressive
2. **It's Real** - Hardware connection visible, honest about limitations
3. **It's Clear** - Focused concept, builds logically, invites experimentation

---

## Strategic Principles (Non-Negotiable)

These principles define what this project IS and IS NOT. Violations are grounds for rejection.

### What We Are

1. **Game-First Pedagogy** - Concepts taught through game implementation, never isolated theory
2. **Hardware Intimacy** - Direct hardware access (sprites, registers, sound chips), not abstraction layers
3. **Original Creation** - Inspired by classics, NOT reproductions of existing games
4. **Mastery Through Repetition** - Skills reinforced across multiple units and games
5. **Self-Directed Learning** - Learners assess their own progress; no instructor required

### What We Are NOT

1. **NOT Nostalgia Tourism** - Focus on skills and hardware, not "remember when" feelings
2. **NOT Modern Engines** - No Unity, Unreal, Godot, GameMaker. Zero tolerance.
3. **NOT Reproductions** - No "pixel-perfect Donkey Kong". Respect copyright.
4. **NOT Quick Fixes** - Honest about difficulty and time investment
5. **NOT Shallow Coverage** - Deep treatment of each platform, not surface surveys
6. **NOT Instructor-Dependent** - Working code = success; no grades or submissions
7. **NOT Abstract Theory** - Games teach concepts; no "memorize these, apply later"

### Quick Violation Check

```bash
# Copyright violations
grep -iE "exact|replica|reproduction|recreat(e|ing)|pixel.perfect" unit-NN-*.mdx

# Nostalgia tourism
grep -iE "remember|nostalg|childhood|magical|back in the day" unit-NN-*.mdx

# Modern engines (ZERO TOLERANCE)
grep -iE "Unity|Unreal|Godot|GameMaker" unit-NN-*.mdx

# Abstract theory
grep -iE "theor(y|etical)|memorize|memorise|later units" unit-NN-*.mdx

# Instructor dependency
grep -iE "submit|grading|instructor|feedback|assignment" unit-NN-*.mdx
```

---

## Workflow Phases

The workflow has **five main phases**, each with detailed steps:

### Phase 1: Planning (Pre-Work)
**Purpose:** Verify curriculum alignment and make key decisions before writing begins.

**Steps:**
- Locate and read curriculum specification (`/docs/curriculum/{platform}-curriculum.md`)
- Locate game outline (if exists): `/docs/plans/{platform}/game-NN-{slug}.md`
- Verify current unit matches specification (if editing existing)
- Choose unit archetype based on concept
- Identify prerequisites from previous units
- Check for existing Pattern Library entries
- Identify required Vault entries (hardware chips, essential context)

**Hard Stop:** If unit doesn't match curriculum specification, STOP. Follow decision matrix (archive mismatch, don't edit).

### Phase 2: Creation
**Purpose:** Write unit content and working code.

**Steps:**
- Write unit MDX following structure
- Create runnable code examples
- Write clear explanations
- Include experimentation suggestions
- Tag potential patterns as you write (lightweight tracking)

### Phase 3: Validation
**Purpose:** Ensure code works and unit meets quality criteria.

**Steps:**
- Platform-specific code validation (delegate to platform skill)
- Runtime testing (no crashes, correct output)
- Apply three quality criteria
- Screenshot/media capture and verification
- British English check

### Phase 4: Integration
**Purpose:** Connect unit to broader curriculum ecosystem.

**Steps:**
- Create required Vault entries (hardware, essential context)
- Track nice-to-have Vault entries for later
- Update pattern tags/notes
- Cross-reference related units
- Update navigation

### Phase 5: Publication
**Purpose:** Commit and make unit available.

**Steps:**
- Final verification checklist
- Commit with proper message format
- Update game landing page
- Mark unit as published

---

## Phase 1: Planning (Detailed)

### Step 1.1: Curriculum Alignment Verification (MANDATORY)

**Before creating or editing ANY unit:**

1. **Locate specification** (check in order):
   - Platform curriculum: `/docs/curriculum/{platform}-curriculum.md`
   - Game outline: `/docs/plans/{platform}/game-NN-{slug}.md`
   - BASIC gateway curriculum (if applicable): `/docs/curriculum/{platform}-basic-curriculum.md`

2. **Read specification completely** - Note game name, unit position, key concepts, skills taught

3. **If editing existing unit, compare:**
   - Does current title match spec? ✅/❌
   - Do learning objectives match? ✅/❌
   - Do key concepts match? ✅/❌

**Decision Matrix:**

- **All ❌ (Complete Mismatch):** Archive current unit (`unit-NN-OLD.mdx.bak`), create new unit from spec
- **Mixed ✅❌ (Partial Match):** Archive current, extract reusable elements, create new unit
- **All ✅ (Strong Match):** Proceed with editing, document minor differences in commit

**Hard Stop:** If specification doesn't exist at ANY level, STOP. Cannot create unit without specification.

### Step 1.2: Archetype Selection

Choose archetype based on what you're teaching:
- New concept/technique → **Discovery**
- Consolidating recent skills (problem) → **Challenge**
- Consolidating recent skills (building something) → **Synthesis**
- Hardware internals explanation → **Deep Dive**
- Step-by-step guided construction → **Tutorial**
- Inspirational demonstration → **Showcase**

### Step 1.3: Prerequisites and Context

- List concepts from previous units this builds on
- Identify BASIC/Assembly knowledge required
- Check Pattern Library for existing patterns covering this technique
- Note which hardware chips will be discussed

### Step 1.4: Required Vault Entries Check

Identify **must-create** Vault entries:
- Hardware chips mentioned (VIC-II, SID, CIA, etc.)
- Core platform components (memory maps, character sets)
- Essential context the unit depends on

Track **nice-to-have** for later:
- Games referenced
- Programmers/designers mentioned
- Companies/publishers

---

## Phase 2: Creation (Detailed)

### Step 2.1: Unit Structure

**File Location:** `/website/src/pages/{platform}/game-NN-{game-slug}/unit-NN-{unit-slug}.mdx`

**Frontmatter (YAML):**
```yaml
---
layout: ../../../layouts/UnitLayout.astro
title: "[Clear, Descriptive Title]"
platform: "commodore-64"
language: "basic-v2"  # or "6510-assembly", "z80-assembly", etc.
game: 1
gameSlug: "sid-symphony"
unit: 1
unitSlug: "first-notes"
totalUnits: 64
prevUnit: "/commodore-64/game-01-sid-symphony/unit-00-..." # or null
nextUnit: "/commodore-64/game-01-sid-symphony/unit-02-..." # or null
objectives:
  - 'First learning objective'
  - 'Second learning objective'
  - 'Third learning objective'
---
```

**Content Sections (adapt as needed for archetype):**

1. **Opening** - Context and motivation (2-4 sentences)
2. **Key Concepts** - Bullet points of what's covered
3. **Example Program** - Simple demonstration with explanation
4. **Experiment Section** - Variations to try, more complex example
5. **How It Works** - Technical explanation, hardware details
6. **Game Integration** - Practical applications
7. **From the Vault** - Links to Vault entries (if relevant)
8. **Quick Reference** - Tables, addresses, syntax for this unit
9. **What You've Learnt** - Summary and next unit preview

**Important:** Structure is flexible. Adapt sections to unit archetype and content.

### Step 2.2: Code Examples

**Location:** `/code-samples/{platform}/game-NN-{game-slug}/unit-NN/example-N.{ext}`

**Requirements:**
- Must run standalone (all DATA, all setup)
- **BASIC gateway games:** NO indentation (BASIC line numbers flush left)
- **Assembly games:** Follow platform assembly conventions
- Use chip names in comments (VIC-II, SID, not "video chip")
- Include clear comments explaining key concepts
- Progressive complexity (simple example → complex example)

### Step 2.3: Pattern Tagging (Lightweight)

As you write, note reusable techniques:
- Add comment in code: `REM PATTERN: SID initialization sequence`
- Or note in unit planning doc: "Pattern candidate: sprite MSB handling"

Don't create Pattern Library entries yet - just tag for later extraction.

### Step 2.4: Writing Guidelines

**Tone:**
- Conversational but precise
- British English (colour, learnt, programme for non-code)
- Use "program" for computer programs
- Name hardware designers/engineers when relevant
- Let concepts speak for themselves - no hype

**Avoid:**
- Excessive exclamation marks
- Forced historical connections every unit
- Claiming BASIC and Assembly are equivalent speed
- Apologizing for hardware limitations
- Formulaic openings

---

## Phase 3: Validation (Detailed)

### Step 3.1: Code Validation (MANDATORY)

**Delegate to platform-specific skill** - Each platform has validation requirements:

**BASIC Gateway Games - Example C64:**
```bash
# Syntax validation
petcat -text -o /dev/null -- example-1.bas

# Generate executable
petcat -w2 -o example-1.prg -- example-1.bas

# Runtime test (no crashes, no errors)
x64sc -autostart example-1.prg -limitcycles 100000000 +sound +confirmonexit
echo $? # Must be 0
```

**Assembly Games:**
- Platform-specific assembler (ACME, ca65, vasm, pasmonext)
- Semantic validation if available
- Runtime testing in emulator

**⚠️ USE PLATFORM SKILL HERE:** See "Platform-Specific Details" section for skill paths. The platform skill provides complete validation commands, semantic checks, and screenshot capture instructions.

**Required:** All validation must pass before proceeding. Fix errors immediately.

### Step 3.2: Apply Three Quality Criteria

Ask these questions:

**1. Does It Work Fast?**
- Something visible/audible within 10 seconds? ✅/❌
- Creates something impressive or useful? ✅/❌

**2. Is It Real?**
- Hardware connection visible (chip names, addresses)? ✅/❌
- Honest about limitations (BASIC speed, constraints)? ✅/❌

**3. Is It Clear?**
- Concept is focused (one main thing)? ✅/❌
- Builds on previous units logically? ✅/❌
- Invites experimentation (clear parameters to modify)? ✅/❌

**Quality Bar:** At least 2/3 criteria strongly met. If not, revise unit.

### Step 3.3: Screenshot and Audio Capture

**When to capture:**
- After code validation passes
- When impressive moment is visible/audible
- For each major example in unit

**Screenshot Capture:**
- Platform-specific (see platform skill for emulator instructions)
- PNG format (lossless)
- Descriptive filenames: `unit-NN-main.png`, `unit-NN-step1.png`
- Location: `/website/public/images/{platform}/game-NN-{slug}/unit-NN/`

**Audio Capture (for sound/music units):**
- Capture audio output from emulator
- WAV or OGG format (lossless or high-quality)
- Descriptive filenames: `unit-NN-sound.wav`, `unit-NN-music.ogg`
- Location: `/website/public/media/{platform}/game-NN-{slug}/unit-NN/`

**Platform Considerations:**
- **PAL vs NTSC timing differences** - SID frequencies differ between PAL (50Hz) and NTSC (60Hz)
- Specify which timing used in unit
- Note differences in unit if relevant: "PAL C64 used for audio examples; NTSC timing will be slightly higher pitch"

**Screenshot Verification (CRITICAL):**

Use Read tool to VIEW every screenshot after capture:
1. **Describe visible elements** - sprites, text, colors, game state
2. **Check for error messages** - `?SYNTAX ERROR`, `?ILLEGAL QUANTITY ERROR`, etc. = automatic failure
3. **Check for blank screens** - indicates crash or initialization bug
4. **Verify expected output matches actual screenshot**

**Audio Verification (for sound units):**

Listen to captured audio and verify:
1. **Correct frequency** - Use frequency analyzer if needed for precise tones
2. **No distortion or clipping** - Check waveform for clean signal
3. **Expected sound** - Triangle wave sounds like triangle, not noise
4. **Timing correct** - Note duration, rhythm matches code
5. **PAL/NTSC noted** - Document which system timing was used

If errors found: Fix code → Revalidate → Recapture → Re-verify (repeat until clean)

**No claiming "verified ✅" without Read tool evidence (screenshots) and listening verification (audio).**

### Step 3.4: British English Check

Run grep pattern to find American spellings:
```bash
grep -n "color\|flavor\|center\|learned" unit-NN-*.mdx
```

**Exceptions:** The word "program" for computer programs (not "programme")

---

## Phase 4: Integration (Detailed)

### Step 4.1: Vault Entry Creation

**Required entries (create before unit completion):**

Create Vault entries for:
- Hardware chips discussed (VIC-II, SID, CIA, etc.)
- Core platform components (memory maps, character sets, PETSCII)
- Essential context the unit depends on

**Vault entry location:** `/website/src/pages/vault/{category}/{entry-name}.mdx`

**Vault Categories (14 total):**
- `hardware` - Chips, components (VIC-II, SID, CIA, etc.)
- `games` - Game titles
- `people` - Programmers, designers, musicians, artists
- `companies` - Publishers, developers
- `platforms` - Platform overviews
- `techniques` - Programming techniques
- `events` - Historical milestones
- `culture` - Demoscene, magazines, communities
- `publications` - Magazines, books, manuals
- `tools` - Development tools, utilities
- `peripherals` - Hardware add-ons
- `formats` - File formats (SID, PRG, TAP, etc.)
- `concepts` - Programming concepts
- `terminology` - Glossary entries

**Basic Vault entry structure:**
```yaml
---
layout: ../../../layouts/VaultLayout.astro
title: "[Component Name]"
subtitle: "[Brief description]"
summary: "[One-sentence overview]"
system_tags: [C64, Spectrum, ...]
tech_tags: ["Hardware", "Graphics", ...]
years: [1982]
---

## Overview
[What it is, what it does]

## Technical Details
[Registers, addresses, capabilities]

## Unit Connections
- Game 1 (SID Symphony), Unit 7: Border colours
- Game 2 (Starfield), Unit 18: Sprite positioning

## See Also
- [Related Vault Entry](/vault/{category}/related)
```

**Nice-to-have entries (track for later):**

Add to `/docs/vault-todo.md`:
```markdown
## From Game N, Unit NN

**Games:**
- [ ] **Game Name** - Description, Developer, Publisher Year
  - Referenced in: Game N, Unit NN
  - Technique: What technique was mentioned

**People:**
- [ ] **Person Name** - Role, notable work
  - Referenced in: Game N, Unit NN
```

### Step 4.2: Pattern Library Tagging

**During unit creation, you tagged potential patterns.**

Now formalize the tracking:

Add to unit frontmatter or planning doc:
```yaml
patternCandidates:
  - "SID initialization sequence"
  - "Sprite MSB handling for X > 255"
  - "Joystick port polling loop"
```

**Pattern extraction happens after game completion** (see Step 4.3)

### Step 4.3: Post-Game Pattern Extraction (After Game Complete)

**When you've completed all units in a game:**

1. **Review all pattern tags** from the game's units
2. **Identify recurring techniques** that appear in multiple units
3. **Create Pattern Library entries systematically**
4. **Backfill cross-references** to units using each pattern

**Pattern entry location:** `/website/src/pages/{platform}/patterns/{category}/{pattern-name}.mdx`

**Combined approach:**
- Tag patterns during creation (lightweight, don't block)
- Systematic extraction after game (comprehensive coverage)

### Step 4.4: Cross-References

**Update unit with Vault links:**
```markdown
### From the Vault

- [VIC-II Chip](/vault/hardware/vic-ii) - Graphics chip register reference
- [Sprite System](/vault/hardware/sprites) - Hardware sprite capabilities
- [Impossible Mission](/vault/games/impossible-mission) - Pioneering platformer
```

**Update navigation if new unit:**

Edit `/website/src/pages/{platform}/game-NN-{slug}/index.astro`:
```javascript
const units = [
  // ... existing units ...
  {
    number: NN,
    slug: "unit-slug",
    title: "Unit Title",
    description: "Brief description for game overview",
    status: "published"
  }
];
```

---

## Phase 5: Publication (Detailed)

### Step 5.1: Final Verification Checklist

Before committing, verify ALL of these:

**Code:**
- [ ] All code examples validated (syntax + runtime)
- [ ] No crashes, no error messages in output
- [ ] PRG/executable files generated successfully
- [ ] Code follows platform conventions (no indentation for BASIC, etc.)

**Quality:**
- [ ] Three quality criteria met (It Works Fast, It's Real, It's Clear)
- [ ] Screenshots captured and verified with Read tool
- [ ] Audio captured and verified (for sound units)
- [ ] No error messages or blank screens in screenshots
- [ ] British English throughout (except "program" for code)

**Curriculum:**
- [ ] Matches curriculum specification exactly
- [ ] Prerequisites clearly stated
- [ ] Builds logically on previous units
- [ ] Objectives in frontmatter match content

**Integration:**
- [ ] Required Vault entries created (hardware, essential context)
- [ ] Nice-to-have Vault entries tracked in vault-todo.md
- [ ] Pattern candidates tagged for later extraction
- [ ] Vault links included in "From the Vault" section
- [ ] Navigation updated (game landing page)

### Step 5.2: Commit Workflow

**Stage all related files:**
```bash
git add website/src/pages/{platform}/game-NN-{slug}/unit-NN-{slug}.mdx
git add code-samples/{platform}/game-NN-{slug}/unit-NN/*.{bas,prg,asm,bin}
git add website/public/images/{platform}/game-NN-{slug}/unit-NN/*.png
git add website/public/media/{platform}/game-NN-{slug}/unit-NN/*.{wav,ogg}
git add website/src/pages/vault/{category}/*.mdx  # if created Vault entries
git add docs/vault-todo.md  # if tracked nice-to-have entries
git add website/src/pages/{platform}/game-NN-{slug}/index.astro  # if updated navigation
```

**Commit message format:**
```
<type>(<scope>): <brief description>

- Learning objective 1
- Learning objective 2
- Key concept introduced
- Hardware chips covered
- Historical connection (if relevant)

Game: N ({game-name}), Unit: NN/total

Vault entries created: [list if any]
Pattern candidates tagged: [list if any]
```

**Types:**
- `feat` - New unit
- `fix` - Bug fix in existing unit
- `docs` - Documentation updates
- `refactor` - Restructure without changing content

**Scopes:** `{platform}-game{NN}` (e.g., `c64-game01`, `spectrum-game03`, `nes-game09`)

**Example:**
```
feat(c64-game02): Add unit 18 - Player-controlled sprites

- Read joystick port at $DC00 for hardware input
- Update sprite X/Y positions based on directional input
- Create real-time interactive control loop
- VIC-II sprite positioning, CIA joystick port

Game: 2 (Starfield), Unit: 18/64

Vault entries created: hardware/cia (joystick registers)
Pattern candidates tagged: joystick-polling-loop
```

### Step 5.3: Mark as Published

Update unit status in game landing page (if not already done in Step 4.4):

```javascript
{
  number: NN,
  slug: "unit-slug",
  title: "Unit Title",
  description: "Brief description",
  status: "published"  // was "draft" or "wip"
}
```

### Step 5.4: Push to Repository

```bash
git push origin <branch-name>
```

**Note:** Follow project git workflow for branching/merging (see CLAUDE.md or project README)

### Step 5.5: Update Landing Pages

**Update as appropriate based on milestone:**

**Game Landing Page (every unit):**
- Location: `/website/src/pages/{platform}/game-NN-{slug}/index.astro`
- Update unit list with new/updated unit
- Mark status as "published"

**Platform Landing Page (when completing game):**
- Location: `/website/src/pages/{platform}/index.astro`
- Update game completion status
- Update unit count
- Add game summary/accomplishments if game complete

**Homepage (major milestones):**
- Location: `/website/src/pages/index.astro`
- Update when:
  - First game complete (first playable curriculum)
  - Platform fully complete (all games)
  - New platform launched
  - Major milestone (100 units, 500 units, etc.)

**What constitutes "appropriate":**
- Single unit → Game landing only
- Game complete → Game + Platform landing
- Major milestone → All levels including Homepage

---

## Platform-Specific Details

**Universal workflow applies to all platforms. Platform skills provide technical execution details.**

**⚠️ IMPORTANT: Use platform skills during Phase 3 (Validation) for compilation, screenshot capture, and platform-specific checks.**

### Commodore 64
- **BASIC V2:** `/docs/platforms/commodore-64/skills/basic-lesson-creation/SKILL.md`
- **6510 Assembly:** `/docs/platforms/commodore-64/skills/6510-lesson-creation/SKILL.md`

### Sinclair ZX Spectrum
- **Sinclair BASIC:** `/docs/platforms/sinclair-zx-spectrum/skills/basic-lesson-creation/SKILL.md`
- **Z80 Assembly:** `/docs/platforms/sinclair-zx-spectrum/skills/z80-lesson-creation/SKILL.md`

### Commodore Amiga
- **AMOS BASIC:** `/docs/platforms/commodore-amiga/skills/amos-lesson-creation/SKILL.md`
- **68000 Assembly:** `/docs/platforms/commodore-amiga/skills/68k-lesson-creation/SKILL.md`

### Nintendo Entertainment System
- **No BASIC** (assembly only)
- **6502 Assembly:** `/docs/platforms/nintendo-entertainment-system/skills/6502-lesson-creation/SKILL.md`

**Each platform skill provides:**
- Compilation/assembly commands
- Semantic validation (where available)
- Emulator configuration for screenshots
- Platform-specific pitfalls and anti-patterns
- Memory map validation
- File naming conventions

**Relationship: Workflow = Strategy, Skills = Tactics**
- This workflow defines WHAT to do and WHEN
- Platform skills define HOW to execute technical steps

---

## Language-Specific Considerations

### BASIC Gateway Games (Optional Track)

**Focus:**
- Game-first approach for novices/children
- Proving concepts before assembly
- Honest about speed limitations
- Foundation for assembly understanding

**Key Requirements:**
- NO indentation (line numbers flush left on most platforms)
- British English (colour, learnt) BUT "program" for code
- Acknowledge BASIC is slower, assembly is faster
- Show hardware addresses and chip names
- Create impressive results within BASIC constraints
- **C64 BASIC variable names:** Only first TWO characters are significant
  - `f1x` and `f1y` are BOTH read as `f1` (collision!)
  - Use distinct first-two-char names: `fx`/`fy`, `gx`/`gy`, `px`/`py`
  - Good: `fx`, `fy`, `gx`, `gy`, `px`, `py`, `sc`, `hp`
  - Bad: `f1x`, `f1y` (both become `f1`), `score1`, `score2` (both become `sc`)

**Typical Unit Structure:**
- Simple example (5-15 lines)
- More complex example (20-40 lines)
- Experimentation suggestions
- "Assembly games will show full-speed techniques" where relevant

### Assembly Games (Main Curriculum)

**Focus:**
- Professional-level techniques
- Direct hardware control
- Cycle-accurate timing
- Real-time game development

**Key Requirements:**
- Cycle counting for timing-critical sections
- Register usage documentation
- Memory-efficient techniques
- Comment WHY, not WHAT

**Typical Unit Structure:**
- Concept explanation with hardware details
- Assembly implementation
- Optimization discussion
- Complete working example with cycle counts

**Differences in Validation:**
- **BASIC:** Syntax validation + runtime test
- **Assembly:** Assembly + linking + runtime test + timing verification

**Differences in Quality Criteria:**
- **BASIC:** "It Works Fast" = within 10 seconds (BASIC speed)
- **Assembly:** "It Works Fast" = instant/real-time (assembly speed)

---

## Emergency Procedures

**What to do when things go wrong:**

### Emergency 1: Edited Wrong Unit (Doesn't Match Curriculum)

**You accidentally edited a unit that doesn't match the specification.**

**If uncommitted:**
```bash
git status  # Check what changed
git restore unit-NN-*.mdx  # Discard changes
```

**If committed but not pushed:**
```bash
git log -1  # Verify it's your commit
git revert HEAD  # Create revert commit
# OR
git reset --soft HEAD^  # Undo commit, keep changes in staging
```

**If pushed:**
1. Create new commit that fixes the issue
2. Follow proper alignment procedure from Phase 1
3. Document in commit message: "fix: Align unit-NN with curriculum specification"

**Then:** Return to Phase 1, Step 1.1 (Curriculum Alignment Verification)

### Emergency 2: Discovered Curriculum Drift Mid-Session

**You realize partway through that unit doesn't match curriculum.**

**Steps:**
1. **STOP immediately**
2. Document changes: `git diff unit-NN-*.mdx > /tmp/changes.diff`
3. Revert changes: `git restore unit-NN-*.mdx`
4. Review diff: Check `/tmp/changes.diff` for universally useful edits (typo fixes, clarity improvements)
5. Follow proper alignment procedure from Phase 1
6. Apply salvaged edits ONLY if they support curriculum-aligned version

### Emergency 3: Code Validation Fails After Writing Unit

**Validation errors after unit is written.**

**Steps:**
1. Read error messages carefully
2. Fix code issues
3. Re-run validation
4. Regenerate executables (PRG/binary files)
5. Re-test runtime
6. If screenshots were captured, recapture after fixes
7. **Do NOT proceed to publication until validation passes**

**Common fixes:**
- Syntax errors → Check BASIC/assembly syntax reference
- Runtime errors → Check memory addresses, value ranges
- Reserved variables → Rename (e.g., ST → GS, TI → CT)
- Missing line numbers → Add target for GOSUB/GOTO

### Emergency 4: Screenshot Shows Errors or Blank Screen

**Screenshot verification revealed problems.**

**Steps:**
1. Identify error type:
   - Syntax error → Code has bugs, validation missed it
   - Runtime error → POKE out of range, illegal quantity
   - Blank screen → Initialization bug or crash
2. Fix code
3. Re-validate completely (syntax + runtime)
4. Recapture screenshot
5. Re-verify with Read tool
6. Repeat until clean

**Do NOT:**
- Publish unit with error screenshots
- Assume error is "minor" and will be fixed later
- Skip re-verification after fixes

### Emergency 5: Committed Wrong Files or Broken Navigation

**Navigation broken, wrong files committed, etc.**

**Steps:**
```bash
git status  # See what's staged/committed
git log -3  # See recent commits

# If uncommitted:
git restore <file>  # Discard wrong changes
git add <correct-file>  # Stage correct files

# If committed but not pushed:
git reset --soft HEAD^  # Undo commit, keep changes
# Fix issues, re-stage correctly, commit again

# If pushed:
# Create fix commit with proper changes
```

### Emergency 6: Lost Work Due to Crash/Error

**Work lost, need to recover.**

**Prevention:**
- Commit frequently during creation
- Use git branches for experimentation
- Keep code samples in separate files (auto-saved by editor)

**Recovery:**
```bash
git reflog  # See all recent git actions
git checkout <commit-hash>  # Recover lost commits
git stash list  # Check for stashed changes
```

---

## Common Pitfalls and Troubleshooting

### Pitfall 1: Formulaic Writing

**Problem:** Every unit starts the same way: "You're controlling the same hardware as..." or "This is the technique that powered..."

**Solution:**
- Vary your openings completely
- Let concepts speak for themselves
- Historical connections only when genuinely illuminating
- Trust the hardware to be compelling

### Pitfall 2: Skipping Curriculum Alignment

**Problem:** "I know what this unit should teach" → write unit → doesn't match specification

**Solution:**
- **ALWAYS** read specification first (Phase 1, Step 1.1)
- Hard stop on mismatches
- Specifications exist for a reason

### Pitfall 3: Claiming Validation Passed Without Evidence

**Problem:** "Code validated ✅" but no screenshot verification, no Read tool check

**Solution:**
- **MUST** run validation commands
- **MUST** verify screenshots with Read tool
- **MUST** listen to audio for sound units
- **MUST** check exit codes
- Evidence before assertions, always

### Pitfall 4: Indentation in BASIC Code

**Problem:** Adding indentation for readability in .bas files breaks BASIC compatibility

**Solution:**
- Line numbers flush left, always (BASIC gateway games)
- No exceptions
- Validation will catch this (petcat will fail)

### Pitfall 5: Reserved Variables in C64 BASIC

**Problem:** Using ST, TI, TI$ causes crashes or unexpected behavior

**Solution:**
- Use GS (game state), CT (custom timer), SC (score), HP (health)
- Never use ST, TI, TI$ as variables
- Check with grep: `grep -iE '\<(st|ti|ti\$)\>' *.bas`

### Pitfall 6: Sprite MSB Not Handled

**Problem:** Sprite X > 255 wraps to left side of screen

**Solution:**
- Always handle $D010 (53264) MSB register
- Introduce in first sprite positioning unit
- All subsequent sprite units must handle correctly

### Pitfall 7: Pattern Library Forgotten

**Problem:** Finish game without extracting patterns, lose track of reusable techniques

**Solution:**
- Tag patterns during creation (lightweight)
- Systematic extraction after game completion
- Combined approach ensures comprehensive coverage

### Pitfall 8: Nice-to-Have Vault Entries Block Progress

**Problem:** Trying to write complete game/programmer bios before completing unit

**Solution:**
- Required entries (hardware) before completion
- Nice-to-have entries (games, people) tracked for later
- vault-todo.md is your friend

### Pitfall 9: Quality Criteria Ignored

**Problem:** Unit published without checking "It Works Fast, It's Real, It's Clear"

**Solution:**
- Apply three criteria in Phase 3 (Validation)
- At least 2/3 must be strongly met
- If not, revise unit before publication

### Pitfall 10: Screenshot Timing Issues

**Problem:** Screenshot captured too early (loading screen) or too late (after program ends)

**Solution:**
- Capture when impressive moment is visible
- Use emulator cycle limits or pause functionality
- Verify with Read tool that screenshot shows expected output

### Pitfall 11: Audio Frequency Errors

**Problem:** SID/AY/sound chip frequencies incorrect, sounds wrong

**Solution:**
- Verify frequency calculations in code
- Use frequency analyzer for precise tones
- Note PAL vs NTSC differences
- Listen to captured audio, don't assume it's correct

---

## Quick Reference Summary

### The Five Workflow Phases

1. **Planning** - Verify curriculum alignment, choose archetype, identify prerequisites
2. **Creation** - Write content and code, tag patterns
3. **Validation** - Code validation, quality criteria, screenshot/audio verification
4. **Integration** - Vault entries, pattern tagging, cross-references
5. **Publication** - Final checks, commit, update navigation

### Hard Stops (Must Complete Before Proceeding)

- ❌ No curriculum specification → STOP, cannot create unit
- ❌ Unit doesn't match specification → STOP, archive and rewrite
- ❌ Code validation fails → STOP, fix before proceeding
- ❌ Screenshot shows errors → STOP, fix and recapture
- ❌ Audio sounds wrong → STOP, fix and recapture
- ❌ Quality criteria not met → STOP, revise unit

### Three Quality Criteria

1. **It Works Fast** - Immediate feedback, impressive result
2. **It's Real** - Hardware visible, honest limitations
3. **It's Clear** - Focused concept, logical progression, invites experimentation

**Quality Bar:** At least 2/3 strongly met

### Six Unit Archetypes

- **Discovery** - Standard teaching (most common)
- **Challenge** - Problem-solving exercise
- **Synthesis** - Combining concepts
- **Deep Dive** - Hardware internals
- **Tutorial** - Step-by-step construction
- **Showcase** - Inspirational demonstration

### Required Before Completion

- [ ] Curriculum alignment verified
- [ ] Code validated (syntax + runtime)
- [ ] Screenshots verified with Read tool
- [ ] Audio verified (for sound units)
- [ ] Quality criteria met (2/3+)
- [ ] Required Vault entries created (hardware)
- [ ] Pattern candidates tagged
- [ ] British English checked
- [ ] Navigation updated

### Vault Categories (14 total)

hardware, games, people, companies, platforms, techniques, events, culture, publications, tools, peripherals, formats, concepts, terminology

### Platform Skills Location

Skills are in `/docs/platforms/{platform}/skills/{language}-lesson-creation/SKILL.md`

Examples:
- C64 BASIC: `/docs/platforms/commodore-64/skills/basic-lesson-creation/SKILL.md`
- ZX Z80: `/docs/platforms/sinclair-zx-spectrum/skills/z80-lesson-creation/SKILL.md`

### Commit Message Format

```
<type>(<scope>): <brief description>

- Learning objective 1
- Learning objective 2

Game: N ({game-name}), Unit: NN/total
```

Types: `feat`, `fix`, `docs`, `refactor`
Scopes: `{platform}-game{NN}`

---

## Version History

- **2.0 (2026-01-07):** Complete rewrite for games/units model. Replaced phases/tiers/lessons structure with games/units throughout.
- **1.0 (2025-11-15):** Original content creation workflow.

---

## End of Content Creation Workflow

**Remember:** Quality over speed. Curriculum alignment is mandatory. Evidence before assertions, always.
