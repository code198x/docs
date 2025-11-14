# Master Curriculum Plan

**Version:** 1.0
**Date:** 2025-11-04
**Status:** Initial framework

---

## Purpose

This document defines curriculum scope, depth, and structure across all platforms. It answers:
- What gets covered on each platform, and why
- How concepts map across platforms
- How lessons get created and validated
- Why lesson counts differ by platform

**Not a learning path.** Students choose any lesson, any platform, any order. This guides content creators.

---

## Platform Complexity & Rationale

**Assembly lesson counts (Phase 0 excluded, powers of 2):**

| Platform | Assembly Lessons | Phases | Phase 0 (Gateway) | Total | Rationale |
|----------|-----------------|---------|-------------------|-------|-----------|
| **C64** | 8,192 | 16 | +64 (BASIC V2) | 8,256 | Deep VIC-II, sprite multiplexing, SID mastery. |
| **ZX Spectrum** | 4,096 | 8 | +64 (Sinclair BASIC) | 4,160 | Simpler hardware. Attribute system, spiral learning. |
| **NES** | 4,096 | TBD | None (console) | 4,096 | PPU tiles, mapper variety. No BASIC interpreter. |
| **Amiga** | 8,192 | TBD | +64 (AMOS BASIC) | 8,256 | Blitter, copper, Paula. Professional output. |

**Phase 0 exists only for home computers with BASIC/gateway languages. Consoles skip directly to assembly.**

**Key principle**: Lesson counts reflect genuine hardware complexity, not arbitrary targets.

**Powers of 2**: All assembly lesson counts must be 2048, 4096, 8192, or 16384.

---

## Universal vs Platform-Specific Concepts

**Universal Concepts** (taught on all platforms, implementation differs):
- Game loops (input → update → draw)
- Collision detection (AABB, pixel-perfect)
- Physics (velocity, acceleration, gravity)
- AI patterns (chase, predict, pathfind)
- Score/lives/HUD systems
- Level progression
- Save/load systems
- Sound effects and music sequencing
- Input handling
- Memory management

**Platform-Specific Techniques:**

| Concept | C64 | ZX Spectrum | NES | Amiga |
|---------|-----|-------------|-----|-------|
| **Graphics** | VIC-II sprites, bitmap modes | Attribute system, software sprites | PPU tiles, nametables | Blitter, bitplanes, copper |
| **Scrolling** | Hardware smooth scroll | Software character/pixel scroll | Hardware tile scroll | Hardware smooth scroll |
| **Sprites** | 8 hardware (multiplexing for 100+) | None (software only) | 64 hardware sprites | 8 hardware sprites + blitter |
| **Sound** | SID chip (3 voices, filters) | BEEP (1-bit) / AY (128K, 3 voices) | APU (5 channels) | Paula (4 channels, samples) |
| **Memory** | 64K flat, bank switching | 48K/128K paging | Mappers (expand ROM/RAM) | Chip/Fast RAM, DMA |
| **Colors** | 16 colors, multi-color modes | 8/16 colors, attribute clash | 52 colors, 4 per tile | 4096 colors, HAM mode |

**Teaching Strategy**: Introduce universal concept first, then show platform-specific implementation.

---

## Platform-Specific Game Selections

**Principle**: Choose games that suit each platform's strengths and match its historical library.

### C64 - Sprite Excellence
- Sprite multiplexing showcases (shooters: 1942, R-Type)
- SID music showcases (rich audio)
- Colorful arcade conversions
- Hardware scrolling techniques

### ZX Spectrum - Flip-Screen Adventures
- Attribute-aware design (color clash as constraint)
- Character-based games (Manic Miner, Jet Set Willy style)
- Isometric games (Knight Lore, Head Over Heels)
- Maze/puzzle games (minimal sprite needs)
- 128K AY music showcases in later phases

### NES - Scrolling Action
- Platformers (Mario, Mega Man style)
- Tile-based adventures (Zelda style)
- Side-scrolling shooters
- Mapper progression (NROM → MMC1 → MMC3)
- Emphasis on smooth scrolling

### Amiga - Graphical Showcases
- 16-bit graphical quality
- Smooth animation (Turrican, Shadow of the Beast)
- Complex simulations
- Sample-based audio (speech, realistic SFX)
- Professional polish

**Key Point**: Same concept (e.g., "platformer physics") taught via different games showcasing each platform's character.

---

## Cross-Platform Learning Paths

**No Prerequisites**: Students start with any platform, do lessons in any order.

**But... Knowledge Transfers**:
- Complete C64 Phase 1 → ZX Spectrum Phase 1 goes faster (Z80 vs 6502, but concepts same)
- Master scrolling on one platform → understand scrolling everywhere (implementation differs)
- Build platformer on NES → easier on C64 (physics knowledge transfers)

### Concept Cross-Reference

The curriculum includes concept glossary showing where each concept appears:

**Example entries:**
- **Collision Detection**: C64 (Phase 1, Lesson 32: Breakout), ZX (Phase 1, Lesson 16: Snake), NES (Phase 1, TBD), Amiga (Phase 1, TBD)
- **Sprite Multiplexing**: C64 (Phase 6, essential), ZX (N/A - software sprites), NES (different approach), Amiga (blitter approach)
- **Scrolling**: C64 (Phase 1, hardware), ZX (Phase 2, software), NES (Phase 1, hardware tiles), Amiga (Phase 1, hardware smooth)

**Use Case**: Student wants sprite multiplexing → Plan shows "C64 Phase 6 covers extensively, NES has different hardware approach, ZX doesn't apply, Amiga uses blitter instead"

**Documentation**: `docs/CONCEPT-CROSS-REFERENCE.md` (to be created)

---

## Production Workflow

**How lessons get created, validated, and published:**

### Step 1: Lesson Planning
- Reference phase curriculum document (e.g., `docs/commodore-64/PHASE-1-CURRICULUM.md`)
- Identify game, tier, lesson arc
- Define learning objectives

### Step 2: Code Development
- Write assembly code in platform-specific toolchain
- Follow platform skill guidelines (e.g., `/docs/skills/c64-6510-lesson-creation/SKILL.md`)
- Compile and test in emulator
- Verify on real hardware (optional but recommended)

### Step 3: Validation (MANDATORY)
- **Code compilation**: Must assemble without errors
- **Semantic validation**: Platform-specific validators check common mistakes
- **Screenshot capture**: Automated or manual screenshot of working program
- **Screenshot verification**: READ tool confirms screenshot shows expected output
- **British English check**: Grep for American spellings

### Step 4: Lesson Writing
- Create MDX file with lesson content
- Include code samples (proper formatting)
- Reference screenshots
- Follow lesson archetype (Discovery, Challenge, Synthesis, Deep Dive)
- Apply voice & tone guidelines (British English, playful but rigorous)

### Step 5: File Organization
- Code: `/code-samples/{platform}/phase-{N}/tier-{N}/lesson-{NNN}/`
- Screenshots: `/website/public/images/{platform}/phase-{N}/tier-{N}/lesson-{NNN}/`
- Lesson: `/website/src/pages/{platform}/phase-{N}/tier-{N}/lesson-{NNN}.mdx`

### Step 6: Update Navigation/Overview Files
- **Tier overview**: `/website/src/pages/{platform}/phase-{N}/tier-{N}/index.mdx`
- **Phase overview**: `/website/src/pages/{platform}/phase-{N}/index.mdx`
- **Platform overview**: `/website/src/pages/{platform}/index.mdx` (if new phase/tier)
- **Homepage**: `/website/src/pages/index.mdx` (if significant milestone)

### Step 7: Quality Verification
- Run full preflight checklist (`/docs/LESSON-PREFLIGHT-CHECKLIST.md`)
- Verify all files present in all locations
- Ensure curriculum alignment
- Test navigation links work

**Cascading Updates**: Adding one lesson may require updating 4+ files. Maintains navigation consistency.

---

## Platform Documentation Structure

**Platform-Specific Curriculum Documents:**
- `docs/commodore-64/PHASE-{N}-CURRICULUM.md` - Complete C64 phase details
- `docs/sinclair-zx-spectrum/PHASE-{N}-CURRICULUM.md` - Complete ZX Spectrum phase details
- `docs/nintendo-entertainment-system/PHASE-{N}-CURRICULUM.md` - Complete NES phase details
- `docs/commodore-amiga/PHASE-{N}-CURRICULUM.md` - Complete Amiga phase details

**Each platform document contains:**
1. Platform overview (hardware capabilities, constraints, signature genres)
2. Total lesson budget (power of 2, with rationale)
3. Phase structure (adapted from universal model, scaled to platform)
4. Game selections (which games, why they suit this platform)
5. Concept coverage (universal concepts + platform-specific techniques)
6. Revisit strategy (when/how games return with new techniques)

**Cross-Reference Documents:**
- `docs/MASTER-CURRICULUM-PLAN.md` (this document)
- `docs/CONCEPT-CROSS-REFERENCE.md` (to be created)
- `docs/CURRICULUM-OVERVIEW.md` (existing C64 overview, to be generalized)

---

## Games as Concept Vehicles

**Key Principle**: Games serve concept discovery. Games get revisited as students master new techniques.

**Example: Pong**
- **Phase 1**: Basic sprites, collision, score (32 lessons)
- **Phase 4**: Advanced physics, particle effects (revisit)
- **Phase 6**: Ultimate polish, competitive AI (final revisit)

**Example: Snake (ZX Spectrum)**
- **Phase 1**: Basic grid movement (16 lessons)
- **Phase 2**: Optimized rendering, power-ups (32 lessons)
- **Phase 3**: AI opponents, professional polish (64 lessons)
- **Phase 4**: 128K AY music, enhanced graphics (64 lessons)
- **Phase 6**: 20+ simultaneous AI snakes (128 lessons)

**Students see direct evolution**: "This is your Phase 1 Snake. Now make it professional."

---

## Revision History

- **1.0 (2025-11-04)**: Initial framework established

---

## Next Steps

1. Create `docs/CONCEPT-CROSS-REFERENCE.md`
2. Complete NES phase structure and lesson counts
3. Complete Amiga phase structure and lesson counts
4. Map universal concepts to specific lessons across platforms
5. Define production workflow automation tools
