# Curriculum Planning Agent

**Type:** Autonomous multi-step execution agent
**Invoked via:** Task tool with `subagent_type: general-purpose`
**Priority:** P1 (High - needed for NES/Amiga expansion)
**Complexity:** High (pattern recognition, adaptation)

---

## Purpose

Autonomously expands phase curricula for new platforms by analyzing existing curricula and adapting patterns while respecting platform-specific strengths and constraints.

Creates complete phase curriculum documents that maintain conceptual consistency across platforms while selecting appropriate games for each platform's hardware capabilities.

---

## What It Does

The agent generates platform-specific phase curricula:

1. **Reads reference curricula** from established platforms (C64, ZX Spectrum)
2. **Identifies universal concepts** taught across platforms (physics, AI, collision detection)
3. **Analyzes platform strengths** (PPU tiles vs sprites, hardware scrolling capabilities)
4. **Selects appropriate games** matching platform's signature genres
5. **Adapts lesson counts** based on platform complexity (powers of 2)
6. **Generates curriculum document** with complete structure
7. **Validates against** MASTER-CURRICULUM-PLAN.md and strategic principles
8. **Reports completion** with curriculum breakdown and rationale

---

## Input Required

**Target Platform Specification:**
- Platform name (e.g., "nintendo-entertainment-system", "commodore-amiga")
- Phase number (e.g., 1, 2)
- Total lesson budget (power of 2, from MASTER-CURRICULUM-PLAN.md)
- Hardware capabilities summary (sprites/tiles, sound, scrolling, memory)

**Reference Platforms:**
- Primary reference (usually C64 or ZX Spectrum with completed phase)
- Secondary reference (for comparison)

**Example:**
```
Target Platform: nintendo-entertainment-system
Phase: 1
Lesson Budget: 512 (from 4096 total assembly lessons)
Hardware: PPU (tiles, 64 sprites), APU (5 channels), hardware scrolling
References: C64 Phase 1, ZX Spectrum Phase 1
```

---

## Decisions Agent Makes Autonomously

The agent makes these high-level curriculum decisions:

1. **Game selections** - Chooses games matching platform's strengths and historical library
2. **Lesson distribution** - Allocates lessons across tiers (16/32/64/128/256 per tier)
3. **Concept introduction order** - Sequences concepts building on hardware capabilities
4. **Arc structure** - Groups lessons into coherent arcs (2-4 lessons per game)
5. **Tier progression** - Determines when to introduce advanced concepts
6. **Game revisit strategy** - Plans when games return with new techniques

---

## Decisions Agent Does NOT Make

These require human approval:

1. **Platform lesson budget** - Must come from MASTER-CURRICULUM-PLAN.md (user-defined)
2. **Phase structure** - Follows universal model (Tier 1: Discovery, Tier 2: Building, etc.)
3. **Strategic principles** - Cannot violate project non-goals (no reproductions, no modern engines)
4. **Lesson archetypes** - Must use established types (Discovery, Challenge, Synthesis, Deep Dive)

---

## Agent Behavior

### Step 1: Analyze Reference Curricula

**Reads:**
- `/docs/commodore-64/PHASE-{N}-CURRICULUM.md`
- `/docs/sinclair-zx-spectrum/PHASE-{N}-CURRICULUM.md`

**Extracts:**
- Universal concepts taught (collision detection, sprite movement, scoring, AI patterns)
- Lesson count distribution across tiers
- Game selection rationale
- Concept introduction timing
- Arc structures (how many lessons per game)

**Example output:**
```
UNIVERSAL CONCEPTS (Phase 1):
- Sprite/character movement (Tier 1)
- Collision detection (Tier 1-2)
- Scoring systems (Tier 1)
- Basic AI (Tier 2)
- Physics (velocity, acceleration) (Tier 2-3)
- Sound effects (throughout)
- Level progression (Tier 3+)

LESSON DISTRIBUTION PATTERN:
- Tier 1: 16 lessons (foundation)
- Tier 2: 32 lessons (building)
- Tier 3: 64 lessons (complexity)
- Tier 4+: Scale up (128, 256...)

ARC STRUCTURE:
- Simple games: 2-3 lessons
- Medium games: 4-6 lessons
- Complex games: 8-12 lessons
```

### Step 2: Assess Platform Strengths

**Analyzes target platform:**
- Graphics capabilities (sprites/tiles, colors, resolution)
- Sound capabilities (channels, sample vs synthesis)
- Scrolling (hardware smooth, hardware tile, software only)
- Memory architecture (flat, banked, mappers)
- Signature genres (what games are this platform known for?)

**Example for NES:**
```
STRENGTHS:
- Hardware tile scrolling (excellent for side-scrollers)
- 64 hardware sprites (good for action games)
- Mappers expand capabilities (progression path)
- PPU tile system (efficient backgrounds)

CONSTRAINTS:
- Fixed palettes (52 colors, 4 per tile)
- No individual pixel control (tile-based)
- Sprite flicker if too many (8 per scanline limit)

SIGNATURE GENRES:
- Platformers (Mario, Mega Man style)
- Side-scrolling shooters (Gradius style)
- Top-down adventures (Zelda style)
- Action games with scrolling
```

### Step 3: Select Platform-Appropriate Games

**Criteria:**
1. **Matches platform strengths** (scrolling platformers for NES, not flip-screen)
2. **Historically appropriate** (genres popular on this platform)
3. **Teaches universal concepts** (not platform-specific gimmicks)
4. **Progressive complexity** (Pong → Snake → Breakout → Platformer → Shooter)
5. **Revisitable** (can return to same game with new techniques)

**Avoids:**
- Games requiring unavailable hardware (C64 sprite multiplexing on NES)
- Genres mismatched to platform (complex strategy on console)
- Copyrighted games (respects strategic principle)

**Example for NES Phase 1:**
```
TIER 1 (16 lessons - Discovery):
- Arc 1: Pong variant (paddle movement, collision)
- Arc 2: Snake (grid movement, self-collision)
- Arc 3: Breakout (ball physics, brick breaking)
- Arc 4: Simple platformer (jumping, gravity)

TIER 2 (32 lessons - Building):
- Arc 1: Expanded platformer (enemies, hazards)
- Arc 2: Scrolling shooter basics (scrolling, projectiles)
- Arc 3: Maze chase game (AI, pathfinding)

TIER 3 (64 lessons - Complexity):
- Arc 1: Advanced platformer (Mario-style mechanics)
- Arc 2: Scrolling shooter advanced (power-ups, bosses)
- Arc 3: Adventure game basics (Zelda-style)
```

### Step 4: Map Universal Concepts to Platform Implementation

**Universal concept:** Sprite movement
- **C64 implementation:** VIC-II sprite registers, 8 hardware sprites
- **ZX implementation:** Software sprites, character-based movement
- **NES implementation:** PPU OAM, 64 hardware sprites, 8-per-scanline limit

**Agent documents HOW concept is taught on this platform:**
```
COLLISION DETECTION:
- C64: SPRITE-SPRITE collision register, SPRITE-BACKGROUND register
- ZX: SCREEN$ character checking, software collision
- NES: PPU sprite 0 hit, software bounding boxes
→ NES lessons use bounding box approach (universal technique)
```

### Step 5: Generate Curriculum Document

**Creates:**
```
/docs/{platform}/PHASE-{N}-CURRICULUM.md
```

**Structure:**
```markdown
# Phase {N} Curriculum: {Platform}

## Platform Overview
[Hardware capabilities, constraints, signature genres]

## Lesson Budget
- Total lessons this phase: {N} (power of 2)
- Tier distribution: [breakdown]
- Rationale: [why this count for this platform]

## Universal Concepts Covered
[List with platform-specific implementations]

## Game Selections
[List with rationale for each]

## Tier Structure

### Tier 1: Discovery (X lessons)
**Goals:** [learning objectives]
**Games:** [list]
**Concepts:** [list]
**Arcs:**
- Arc 1: [game] (L1-3)
  - L1: [title] - [concept]
  - L2: [title] - [concept]
  - L3: [title] - [concept]
...

[Repeat for all tiers]

## Revisit Strategy
[Which games return, when, with what new techniques]

## Cross-Platform Learning
[How this compares to C64/ZX implementations]
```

### Step 6: Validate Against Strategic Principles

**Checks:**
- No copyrighted game reproductions (strategic principle)
- Games teach concepts, not nostalgia (strategic principle)
- Platform-appropriate depth (not shallow coverage)
- Progressive difficulty (follows mastery through repetition)
- Self-directed learning possible (no instructor dependency)

**If violations found:** Agent reports and stops

### Step 7: Report Completion

**Report includes:**
- Curriculum file created
- Lesson count breakdown
- Game selections with rationale
- Concept coverage summary
- Platform-specific implementation notes
- Recommendations for user review

---

## Example Output

```
CURRICULUM PLANNING COMPLETE

FILE CREATED:
/docs/nintendo-entertainment-system/PHASE-1-CURRICULUM.md

LESSON BREAKDOWN:
- Tier 1 (Discovery): 16 lessons
- Tier 2 (Building): 32 lessons
- Tier 3 (Complexity): 64 lessons
- Tier 4 (Deep Dive): 128 lessons
- Tier 5 (Mastery): 256 lessons
Total: 496 lessons (16 reserved for tier expansion)

GAME SELECTIONS:
Tier 1:
- Pong variant (hardware sprites introduction)
- Snake (grid-based movement, OAM basics)
- Breakout (ball physics, PPU scrolling)
- Simple platformer (jumping, gravity, collision)

Tier 2:
- Expanded platformer (enemies, hazards, lives)
- Scrolling shooter (background scrolling, projectiles)
- Maze chase (AI algorithms, pathfinding)

Tier 3:
- Advanced platformer (Mario-style mechanics, power-ups)
- Scrolling shooter advanced (bosses, patterns, polish)
- Adventure game (Zelda-style, top-down, screens)

PLATFORM-SPECIFIC ADAPTATIONS:
- Using PPU tile scrolling (NES strength vs C64 character scroll)
- Hardware sprite advantages (64 vs C64's 8)
- Mapper progression (NROM → MMC1 → MMC3 in higher tiers)
- 8-per-scanline sprite limit addressed in Tier 2

UNIVERSAL CONCEPTS:
✓ Collision detection (bounding boxes, PPU sprite 0 hit)
✓ Physics (velocity, acceleration, gravity)
✓ AI patterns (chase, predict, pathfind)
✓ Scoring systems
✓ Lives/health systems
✓ Sound effects (APU channels)
✓ Level progression
✓ Save systems (battery-backed RAM, passwords)

RECOMMENDATIONS:
1. Review game selections for platform appropriateness
2. Verify lesson count aligns with platform complexity
3. Check arc structure maintains progressive difficulty
4. Confirm no copyrighted reproductions
5. Validate against MASTER-CURRICULUM-PLAN.md
```

---

## Invocation Pattern

```javascript
Task tool invocation:
{
  subagent_type: "general-purpose",
  description: "Generate phase curriculum for platform",
  prompt: `You are creating a phase curriculum for the Code Like It's 198x project.

TARGET PLATFORM:
- Platform: {platform-name}
- Phase: {N}
- Lesson Budget: {X} (power of 2, from MASTER-CURRICULUM-PLAN.md)
- Hardware Summary: {brief capabilities description}

REFERENCE CURRICULA:
- Primary: /docs/commodore-64/PHASE-{N}-CURRICULUM.md
- Secondary: /docs/sinclair-zx-spectrum/PHASE-{N}-CURRICULUM.md

YOUR TASK:
1. Analyze reference curricula
   - Extract universal concepts taught
   - Identify lesson distribution patterns
   - Note arc structures and game progressions

2. Assess target platform
   - Graphics capabilities (sprites/tiles, colors)
   - Sound capabilities (channels, synthesis)
   - Scrolling (hardware/software)
   - Memory architecture
   - Signature genres

3. Select platform-appropriate games
   - Match platform strengths (scrolling platformers for NES)
   - Historically appropriate (genres popular on platform)
   - Teach universal concepts
   - Progressive complexity
   - Revisitable with new techniques

4. Map universal concepts to platform implementations
   - Document HOW each concept is taught on this platform
   - Note platform-specific advantages/constraints

5. Generate curriculum document at:
   /docs/{platform}/PHASE-{N}-CURRICULUM.md

   Include:
   - Platform overview
   - Lesson budget breakdown
   - Universal concepts covered
   - Game selections with rationale
   - Complete tier structure
   - Revisit strategy
   - Cross-platform learning notes

6. Validate against strategic principles
   - No copyrighted reproductions
   - Concepts over nostalgia
   - Platform-appropriate depth
   - Self-directed learning

DECISIONS YOU MAKE:
- Which games to select
- How to distribute lessons across tiers
- When to introduce concepts
- Arc structures (lessons per game)
- Platform-specific implementations

CONSTRAINTS:
- Lesson budget from MASTER-CURRICULUM-PLAN.md (power of 2)
- Phase structure follows universal model
- Must respect strategic principles
- Use established lesson archetypes

REPORT:
"Curriculum planning complete.

FILE CREATED: [path]

LESSON BREAKDOWN:
[Tier-by-tier breakdown with totals]

GAME SELECTIONS:
[List by tier with rationale]

PLATFORM-SPECIFIC ADAPTATIONS:
[How this differs from reference platforms]

UNIVERSAL CONCEPTS:
[List with platform implementations]

RECOMMENDATIONS:
[What to review/verify]"

Execute curriculum planning now.`
}
```

---

## Dependencies

**Required:**
- MASTER-CURRICULUM-PLAN.md exists
- Reference platform curricula complete (C64, ZX Spectrum)
- Platform hardware capabilities documented
- Strategic principles defined (STRATEGIC-FOUNDATION.md)

**Curriculum documents:**
- At least one reference platform with completed phase curriculum

---

## Success Metrics

**Agent succeeds if:**
- Complete curriculum document generated
- Lesson count matches budget (power of 2)
- Games appropriate for platform strengths
- Universal concepts covered with platform implementations
- No strategic principle violations
- Progressive difficulty maintained
- Follows established phase structure

**Agent fails if:**
- Copyrighted reproductions suggested
- Wrong lesson count (not power of 2)
- Games mismatch platform capabilities
- Missing universal concepts
- Strategic violations
- Unclear implementation details

---

## Common Mistakes and Fixes

**Mistake 1: Directly copying reference curriculum**
- **Cause:** Not adapting to platform strengths
- **Fix:** Analyze platform capabilities, select appropriate games
- **Prevention:** Explicit platform assessment step

**Mistake 2: Wrong lesson count**
- **Cause:** Not following power-of-2 rule
- **Fix:** Read MASTER-CURRICULUM-PLAN.md for authoritative budget
- **Prevention:** Validate lesson count before generation

**Mistake 3: Suggesting copyrighted reproductions**
- **Cause:** Not checking against strategic principles
- **Fix:** Use genre names ("platformer", "shooter") not specific games
- **Prevention:** Strategic validation step

**Mistake 4: Missing platform-specific details**
- **Cause:** Generic curriculum without implementation notes
- **Fix:** Document HOW each concept works on this platform
- **Prevention:** Platform implementation mapping step

**Mistake 5: Shallow game selections**
- **Cause:** Not planning revisit strategy
- **Fix:** Specify when/how games return with new techniques
- **Prevention:** Revisit strategy section required

---

## The Bottom Line

**This agent creates platform-specific curricula by:**
1. Analyzing existing patterns from reference platforms
2. Adapting to target platform's strengths and constraints
3. Selecting appropriate games for platform's signature genres
4. Mapping universal concepts to platform-specific implementations
5. Validating against strategic principles

**Zero tolerance for:**
- Copyrighted reproductions
- Wrong lesson counts (must be power of 2)
- Platform-mismatched games
- Missing implementation details
- Strategic principle violations
