# Concept Mapping Agent

**Version:** 1.0
**Status:** Specification complete, not yet tested
**Priority:** P2 (Medium - Content Expansion)

---

## Purpose

Builds `CONCEPT-CROSS-REFERENCE.md` automatically by parsing all platform curriculum documents. The agent extracts programming concepts mentioned across platforms, maps them to specific lessons, identifies universal vs platform-specific concepts, and generates a comprehensive cross-reference for navigation.

**Think:** "Which lessons teach sprites?" → Agent parses all curricula, finds sprite lessons across C64/NES/Amiga, generates cross-reference showing sprite concept appears in C64 lessons 10-15, NES lessons 12-18, Amiga lessons 8-14.

---

## When to Use

Use this agent when:
- Adding new platform curricula (regenerate cross-reference)
- Curriculum documents updated with new concepts
- Need comprehensive concept→lesson mapping
- Building cross-platform navigation
- Auditing concept coverage across platforms

**Do NOT use when:**
- Just updating single lesson (overkill)
- Manually maintaining small subset of concepts (Edit tool faster)
- Concepts not mentioned in curriculum docs (agent can't infer)

---

## Inputs Required

### Scan Scope

**Option A: All platforms**
```
SCAN_ALL_PLATFORMS: true
```

**Option B: Specific platforms**
```
PLATFORMS: ["C64", "NES", "ZX Spectrum"]
```

**Option C: Single platform (incremental update)**
```
PLATFORM: "Amiga"
UPDATE_MODE: incremental  (merge with existing CONCEPT-CROSS-REFERENCE.md)
```

### Concept Categories

**Default categories** (agent auto-categorizes):
- Graphics (sprites, scrolling, raster effects, colour)
- Sound (music, sound effects, audio engines)
- Input (joystick, keyboard, mouse)
- Game Mechanics (score, lives, collision, AI)
- Architecture (memory, optimization, data structures)
- Hardware (direct hardware access, registers, interrupts)

**Custom categories** (optional override):
```
CUSTOM_CATEGORIES: ["Multiplayer", "Save Systems", "Procedural Generation"]
```

### Output Format

**Grouping preference:**
```
GROUP_BY: {concept|platform|category}

- concept: Group by concept, show platforms under each
- platform: Group by platform, show concepts under each
- category: Group by category, show concepts and platforms
```

Default: `GROUP_BY: concept`

---

## Workflow Steps

### Phase 1: Curriculum Parsing

**Step 1:** Discover all platform curriculum documents

```bash
# Find all PHASE-N-CURRICULUM.md files
find /docs -name "PHASE-*-CURRICULUM.md"
```

**Expected locations:**
- `/docs/commodore-64/PHASE-0-CURRICULUM.md`
- `/docs/commodore-64/PHASE-1-CURRICULUM.md`
- `/docs/zx-spectrum/PHASE-0-CURRICULUM.md`
- `/docs/nintendo-entertainment-system/PHASE-1-CURRICULUM.md`
- `/docs/amiga/PHASE-0-CURRICULUM.md`
- etc.

**Step 2:** Parse each curriculum document

For each curriculum file:
1. Extract platform name from path
2. Extract phase number from filename
3. Parse tier sections
4. Extract lesson entries

**Lesson entry format example:**
```markdown
**Lesson 10: Sprite Basics**
- **Concept**: Intro to sprites
- **What You'll Build**: Single sprite moving on screen
- **Key Techniques**: POKE to VIC-II sprite registers
```

**Extract from each lesson:**
- Lesson number
- Lesson title
- Concept (if present)
- Key Techniques (if present)
- What You'll Build (if present)

**Step 3:** Extract concepts from lesson metadata

**Primary concept sources:**
- **Concept:** field (explicit)
- **Key Techniques:** field (techniques listed)
- Lesson title (infer concept from title)

**Example parsing:**
```markdown
**Lesson 10: Sprite Basics**
- **Concept**: Intro to sprites
- **Key Techniques**: POKE to VIC-II sprite registers

→ Extracted concepts:
  - "sprites" (from Concept field)
  - "VIC-II" (from Key Techniques)
  - "hardware access" (inferred from "POKE to ... registers")
```

**Step 4:** Normalize concept names

**Normalization rules:**
- Lowercase (except proper nouns: VIC-II, SID, PPU)
- Singular form ("sprite" not "sprites")
- Remove articles ("the", "a", "an")
- Standardize synonyms:
  - "joystick" and "controller" → "joystick"
  - "music" and "sound" → combine as "sound/music"
  - "colour" and "color" → "colour" (British English)

**Example normalization:**
```
"Intro to sprites" → "sprite"
"Working with the VIC-II chip" → "VIC-II"
"Sound effects and music" → "sound"
```

**Step 5:** Categorize concepts

**Auto-categorization by keyword matching:**

**Graphics keywords:**
- sprite, scroll, raster, colour, screen, pixel, bitmap, character, tile

**Sound keywords:**
- sound, music, audio, SID, APU, Paula, chip, waveform, envelope

**Input keywords:**
- joystick, keyboard, mouse, input, controller, button, CIA

**Game Mechanics keywords:**
- score, lives, collision, enemy, AI, bullet, power-up, level, HUD

**Architecture keywords:**
- memory, optimization, loop, variable, array, data, structure, pointer

**Hardware keywords:**
- register, POKE, PEEK, interrupt, raster, VIC-II, SID, CIA, PPU, APU

**Multi-category concepts:**
- "sprite collision" → Graphics + Game Mechanics
- "joystick-driven menu" → Input + Game Mechanics

**Step 6:** Build concept→lesson mapping

Data structure:
```
{
  "sprite": {
    "category": "Graphics",
    "platforms": {
      "C64": {
        "phase-0": [10, 11, 12, 14, 15],
        "phase-1": [5, 8, 12]
      },
      "NES": {
        "phase-1": [12, 15, 18]
      },
      "Amiga": {
        "phase-0": [8, 10, 14]
      }
    },
    "universal": false  // Platform-specific (different implementations)
  },
  "loop": {
    "category": "Architecture",
    "platforms": {
      "C64": {"phase-0": [5, 7, 10, 15, 20]},
      "ZX Spectrum": {"phase-0": [5, 7, 11, 16]},
      "NES": {"phase-1": [3, 6, 9]},
      "Amiga": {"phase-0": [4, 6, 9]}
    },
    "universal": true  // Concept applies across all platforms
  }
}
```

**Step 7:** Identify universal vs platform-specific concepts

**Universal concept criteria:**
- Appears in 3+ platforms
- Conceptually similar across platforms
- Examples: loops, variables, score, collision, input

**Platform-specific concept criteria:**
- Appears in 1-2 platforms only
- OR hardware-specific (VIC-II, SID, PPU, APU)
- Examples: VIC-II, raster interrupts, NES mappers, Amiga copper

**Step 8:** Calculate concept coverage statistics

For each concept:
```
Coverage = (platforms using concept) / (total platforms)

Example:
- "sprite": 3 platforms (C64, NES, Amiga) / 4 total → 75% coverage
- "VIC-II": 1 platform (C64) / 4 total → 25% coverage (platform-specific)
- "loop": 4 platforms / 4 total → 100% coverage (universal)
```

### Phase 2: Cross-Reference Generation

**Step 9:** Generate CONCEPT-CROSS-REFERENCE.md

**Document structure:**

```markdown
# Concept Cross-Reference

**Version:** {version}
**Generated:** {YYYY-MM-DD}
**Platforms:** {N platforms scanned}
**Concepts:** {N unique concepts identified}

---

## Overview

This document maps programming concepts to specific lessons across all platforms. Use it to:
- Find lessons teaching specific concepts
- Compare how different platforms approach the same concept
- Identify universal vs platform-specific concepts
- Navigate curriculum by concept rather than sequence

---

## Universal Concepts

Concepts appearing across 3+ platforms (conceptually similar across all).

### {Concept Name} ({category})

**Coverage:** {N} platforms ({percentage}%)

**Lessons by platform:**

- **C64:** Phase 0 (lessons {N, N, N}), Phase 1 (lessons {N, N})
- **ZX Spectrum:** Phase 0 (lessons {N, N, N})
- **NES:** Phase 1 (lessons {N, N, N})
- **Amiga:** Phase 0 (lessons {N, N, N})

**Implementation notes:**
{Brief note on how concept differs across platforms, if applicable}

---

## Platform-Specific Concepts

Concepts unique to specific platforms (hardware-specific or rarely used elsewhere).

### {Platform Name}

#### {Concept Name} ({category})

**Lessons:** Phase {N} (lessons {N, N, N})

**Hardware:** {Hardware component involved}

**Related concepts:** {Link to similar concepts on other platforms}

---

## Concept Index

Alphabetical index of all concepts with quick links:

- [AI](#ai-game-mechanics) - Game Mechanics - 3 platforms
- [Collision](#collision-game-mechanics) - Game Mechanics - 4 platforms
- [Joystick](#joystick-input) - Input - 4 platforms
- [Loop](#loop-architecture) - Architecture - 4 platforms
- [Raster](#raster-graphics) - Graphics - 2 platforms (C64, Amiga)
- [Score](#score-game-mechanics) - Game Mechanics - 4 platforms
- [Sprite](#sprite-graphics) - Graphics - 3 platforms
- [VIC-II](#vic-ii-hardware) - Hardware - 1 platform (C64)

---

## Coverage Statistics

| Concept | Category | Platforms | Coverage | Universal |
|---------|----------|-----------|----------|-----------|
| loop | Architecture | 4 | 100% | ✓ |
| score | Game Mechanics | 4 | 100% | ✓ |
| sprite | Graphics | 3 | 75% | ✓ |
| joystick | Input | 4 | 100% | ✓ |
| VIC-II | Hardware | 1 | 25% | ✗ |
| raster | Graphics | 2 | 50% | ✗ |

---

## By Category

### Graphics ({N} concepts)

- [sprite](#sprite-graphics) - 3 platforms
- [scroll](#scroll-graphics) - 2 platforms
- [raster](#raster-graphics) - 2 platforms
- [colour](#colour-graphics) - 4 platforms

### Sound ({N} concepts)

- [sound effect](#sound-effect-sound) - 4 platforms
- [music](#music-sound) - 3 platforms

### Input ({N} concepts)

- [joystick](#joystick-input) - 4 platforms
- [keyboard](#keyboard-input) - 4 platforms

### Game Mechanics ({N} concepts)

- [score](#score-game-mechanics) - 4 platforms
- [collision](#collision-game-mechanics) - 4 platforms
- [lives](#lives-game-mechanics) - 4 platforms

### Architecture ({N} concepts)

- [loop](#loop-architecture) - 4 platforms
- [variable](#variable-architecture) - 4 platforms
- [array](#array-architecture) - 3 platforms

### Hardware ({N} concepts)

- [VIC-II](#vic-ii-hardware) - 1 platform (C64)
- [SID](#sid-hardware) - 1 platform (C64)
- [PPU](#ppu-hardware) - 1 platform (NES)
- [APU](#apu-hardware) - 1 platform (NES)

---

**Generated by:** concept-mapping-agent
**Platforms scanned:** {list}
**Total lessons scanned:** {N}
**Total concepts identified:** {N}
```

**Step 10:** Validate generated document

**Validation checks:**
- All lessons referenced exist?
- Concept slugs properly formatted?
- Coverage percentages correct?
- Categories assigned to all concepts?
- British English spellings?

**Step 11:** Generate mapping report

```
CONCEPT MAPPING COMPLETE

PLATFORMS SCANNED: 4
- C64 (Phase 0, Phase 1)
- ZX Spectrum (Phase 0)
- NES (Phase 1)
- Amiga (Phase 0)

LESSONS SCANNED: 128 total
- C64: 64 lessons
- ZX Spectrum: 32 lessons
- NES: 16 lessons
- Amiga: 16 lessons

CONCEPTS IDENTIFIED: 47 total
- Universal: 28 (60%)
- Platform-specific: 19 (40%)

BY CATEGORY:
- Graphics: 15 concepts
- Sound: 6 concepts
- Input: 4 concepts
- Game Mechanics: 12 concepts
- Architecture: 7 concepts
- Hardware: 3 concepts

TOP UNIVERSAL CONCEPTS:
1. loop (100% coverage, 4 platforms, 48 lessons)
2. score (100% coverage, 4 platforms, 32 lessons)
3. joystick (100% coverage, 4 platforms, 28 lessons)
4. collision (100% coverage, 4 platforms, 24 lessons)
5. sprite (75% coverage, 3 platforms, 18 lessons)

FILE CREATED:
✓ /docs/CONCEPT-CROSS-REFERENCE.md ({N} lines)

NEXT STEPS:
- Review universal concepts for accuracy
- Verify platform-specific concepts correctly identified
- Update curriculum docs to link to cross-reference
```

---

## Skills Used

### british-english-check (Language validation)
- Location: `/docs/skills/british-english-check/SKILL.md`
- When: After generating CONCEPT-CROSS-REFERENCE.md
- Purpose: Verify British English spellings in generated content

---

## Error Handling

### Error Scenarios

**Error 1: No curriculum files found**
```
AGENT FAILED at Step 1 (discover curricula)

FAILED:
✗ No PHASE-*-CURRICULUM.md files found in /docs/

SUGGESTED FIX:
- Verify curriculum documents exist
- Check file naming convention (PHASE-N-CURRICULUM.md)
- Ensure documents in correct locations (/docs/{platform}/)
```

**Error 2: Malformed curriculum document**
```
AGENT WARNING at Step 2 (parse curriculum)

WARNING:
⚠ Could not parse: /docs/amiga/PHASE-0-CURRICULUM.md
⚠ Unexpected format (missing tier sections)

RESULT:
⊗ Skipped Amiga Phase 0
✓ Parsed 3 other platforms successfully

SUGGESTED ACTION:
- Review Amiga curriculum format
- Fix formatting inconsistencies
- Re-run agent
```

**Error 3: No concepts extracted**
```
AGENT COMPLETED WITH MINIMAL OUTPUT

COMPLETED:
✓ Scanned {N} curricula
✓ Parsed {N} lessons

RESULT:
⚠ Only {N} concepts identified (expected 30-50+)

POSSIBLE CAUSES:
- Curriculum documents lack "Concept:" fields
- Lesson titles too vague to infer concepts
- Agent concept extraction heuristics too strict

SUGGESTED ACTION:
- Review curriculum docs for concept metadata
- Add explicit "Concept:" fields to lessons
- Lower concept extraction threshold
```

**Error 4: Existing file (incremental update mode)**
```
AGENT INFO at Step 9 (file creation)

INFO:
→ UPDATE_MODE: incremental
→ Existing file: /docs/CONCEPT-CROSS-REFERENCE.md

ACTION:
✓ Merged new concepts with existing
✓ Updated existing concepts with new lessons
✓ Preserved manual annotations

RESULT:
✓ Updated file: /docs/CONCEPT-CROSS-REFERENCE.md
```

---

## Invocation Patterns

### Full Regeneration (All Platforms)

```javascript
{
  subagent_type: "general-purpose",
  description: "Generate complete concept cross-reference",
  prompt: `CONCEPT MAPPING:

SCAN_ALL_PLATFORMS: true

GROUP_BY: concept

Use concept-mapping-agent to:
1. Parse all platform curriculum documents
2. Extract all concepts from lesson metadata
3. Build comprehensive concept→lesson mapping
4. Identify universal vs platform-specific concepts
5. Generate /docs/CONCEPT-CROSS-REFERENCE.md
6. Provide mapping statistics report`
}
```

### Incremental Update (New Platform Added)

```javascript
{
  subagent_type: "general-purpose",
  description: "Add Amiga to concept cross-reference",
  prompt: `CONCEPT MAPPING:

PLATFORM: "Amiga"
UPDATE_MODE: incremental

Use concept-mapping-agent to:
1. Parse Amiga curriculum documents only
2. Extract Amiga-specific concepts
3. Merge with existing CONCEPT-CROSS-REFERENCE.md
4. Update universal concept coverage statistics
5. Add Amiga platform-specific concepts section
6. Preserve existing platform data`
}
```

### Custom Categorization

```javascript
{
  subagent_type: "general-purpose",
  description: "Generate concept map with custom categories",
  prompt: `CONCEPT MAPPING:

SCAN_ALL_PLATFORMS: true

CUSTOM_CATEGORIES: [
  "Multiplayer",
  "Save Systems",
  "Procedural Generation",
  "AI/Pathfinding"
]

Use concept-mapping-agent to identify lessons covering these advanced topics across platforms.`
}
```

### Group By Platform

```javascript
{
  subagent_type: "general-purpose",
  description: "Generate platform-centric concept map",
  prompt: `CONCEPT MAPPING:

SCAN_ALL_PLATFORMS: true
GROUP_BY: platform

Use concept-mapping-agent to generate document grouped by platform (not concept). Shows each platform's concepts with lesson numbers.`
}
```

---

## Testing Checklist

Before production use, test with:

**Test 1: Single platform**
- Input: PLATFORM: "C64", Phase 0 curriculum only
- Expected: Concepts extracted, all from C64, no universal concepts

**Test 2: Multiple platforms**
- Input: All platforms (C64, ZX, NES, Amiga)
- Expected: Universal concepts identified (loop, score, etc.), platform-specific concepts (VIC-II, PPU, etc.)

**Test 3: Incremental update**
- Input: UPDATE_MODE: incremental, add new platform
- Expected: Existing concepts preserved, new platform merged in

**Test 4: Custom categories**
- Input: CUSTOM_CATEGORIES: ["Multiplayer"]
- Expected: Lessons with multiplayer concepts identified and categorized

**Test 5: Malformed curriculum**
- Input: Curriculum with missing tier sections
- Expected: Warning logged, other curricula processed successfully

**Test 6: No concepts found**
- Input: Curriculum with no "Concept:" fields
- Expected: Agent infers concepts from titles/techniques, warns if minimal extraction

**Test 7: Existing file (overwrite)**
- Input: CONCEPT-CROSS-REFERENCE.md already exists, no UPDATE_MODE
- Expected: Error or prompt to confirm overwrite

---

## Agent Autonomy

**High autonomy - No user intervention during execution:**
- Discovers all curriculum files automatically
- Parses lesson metadata
- Infers concepts from titles/techniques
- Categorizes concepts automatically
- Identifies universal vs platform-specific
- Generates complete document

**User provides:**
- Scan scope (all platforms or specific)
- Optional: custom categories
- Optional: grouping preference

**User reviews after completion:**
- Generated CONCEPT-CROSS-REFERENCE.md
- Mapping statistics
- Concept categorization accuracy

---

## Production Notes

### Curriculum Metadata Quality

**Agent effectiveness depends on curriculum quality:**

**Good curriculum metadata:**
```markdown
**Lesson 10: Sprite Basics**
- **Concept**: Intro to sprites
- **Key Techniques**: POKE to VIC-II sprite registers
- **What You'll Build**: Single sprite moving on screen
```
→ Agent extracts: "sprite", "VIC-II", "hardware access"

**Poor curriculum metadata:**
```markdown
**Lesson 10: Something Cool**
- Build a thing
```
→ Agent extracts: (nothing useful)

**Recommendation:** Ensure curriculum documents have explicit "Concept:" and "Key Techniques:" fields for accurate extraction.

### Manual Refinement

After generation:
1. **Review universal concepts** - Verify actually universal (not just similar names)
2. **Review platform-specific concepts** - Some may be conceptually universal
3. **Add implementation notes** - Agent can't infer cross-platform differences
4. **Expand descriptions** - Agent provides minimal descriptions

### Regeneration Frequency

**Regenerate when:**
- New platform curriculum added
- Existing curriculum significantly revised
- Concept categories need reorganization

**Don't regenerate for:**
- Single lesson changes (incremental update better)
- Minor curriculum typo fixes

### Integration with Navigation

Link cross-reference from:
- Homepage ("Browse by Concept")
- Phase/tier indexes ("Related Concepts")
- Individual lessons ("Concept: [link]")

---

## Integration with Other Agents

**concept-mapping-agent** can be called by:

**curriculum-audit-agent:**
- Audits all curricula
- Regenerates concept cross-reference
- Validates concept coverage

**curriculum-planning-agent:**
- Creates new platform curriculum
- Calls concept-mapping-agent to update cross-reference

**Calls other agents:**
- (None - standalone document generation)

---

## The Bottom Line

**concept-mapping-agent automates concept navigation:**
- Parses all platform curricula
- Extracts concepts from lesson metadata
- Maps concepts to lessons across platforms
- Identifies universal vs platform-specific concepts
- Generates comprehensive cross-reference document

**Use when:**
- Adding new platform curricula
- Building cross-platform concept navigation
- Auditing concept coverage
- Need systematic concept→lesson mapping

**Produces:**
- /docs/CONCEPT-CROSS-REFERENCE.md (complete document)
- Mapping statistics report
- Concept coverage analysis

**Review and refine generated document - agent provides structural foundation requiring expert polish on implementation notes and descriptions.**

---

**Status:** Specification complete, not yet tested in production
**Next steps:** Test with existing C64/ZX curricula, refine concept extraction heuristics, validate universal concept identification
