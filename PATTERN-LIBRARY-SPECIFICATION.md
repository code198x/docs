# Pattern Library: Specification

## Overview

The Pattern Library is a collection of reusable code patterns taught throughout the Code Like It's 198x curriculum. Each pattern provides production-ready code that learners can copy and adapt for their own projects.

**Key Principles:**
- **Production-ready** - Complete, working code you can copy-paste-adapt
- **Concise** - Just enough explanation to use it effectively
- **Cross-platform** - Same concept shown across different platforms where applicable
- **Evolution tracked** - Simple → complex versions linked together

---

## Organisation

### URL Structure

```
/patterns/                           # Index: browse by platform or category
/patterns/commodore-64/              # All C64 patterns
/patterns/commodore-64/rendering/    # C64 rendering patterns
/patterns/commodore-64/rendering/sprite-multiplexing-basic/
```

### Categories

- **Rendering:** Sprites, scrolling, screen effects
- **Input:** Joystick, keyboard, mouse
- **Audio:** Music playback, sound effects
- **Physics:** Collision, movement, gravity
- **AI:** Enemy behaviour, pathfinding
- **Framework:** Game loops, state machines, interrupts

---

## Pattern Entry Format

Each pattern has **5 sections** (not 12):

### 1. Frontmatter

```yaml
---
title: "Sprite Multiplexing (Basic)"
platform: "Commodore 64"
category: "Rendering"
difficulty: "Intermediate"  # Beginner | Intermediate | Advanced
taught_in: "Game 9, Unit 8"
tags: ["sprites", "raster", "vic-ii"]
evolution:
  previous: null
  next: "sprite-multiplexing-sorted"
related:
  patterns: ["raster-interrupts", "sprite-animation"]
  vault: ["vic-ii", "raster-tricks-101"]
---
```

### 2. Overview

One paragraph: what it does, why you'd use it, key trade-off.

```markdown
## Overview

Display more than 8 hardware sprites by reusing them at different vertical positions. A raster interrupt repositions sprites after the beam passes. Use when you need 9-40 sprites; accept occasional flicker when sprites cluster on the same scanline.
```

### 3. Code

The actual pattern - complete, commented, ready to use.

```markdown
## Code

` ``asm
; SPRITE MULTIPLEXING - BASIC (8-24 sprites)
; Taught: Game 9 (Sprite Storm), Unit 8
; CPU: ~900 cycles/frame | Memory: ~400 bytes

MAX_SPRITES = 24

; [Complete working code here...]
` ``

**Usage:**
` ``asm
jsr init_multiplexing
; [Minimal usage example]
` ``
```

### 4. Trade-offs

Brief, scannable costs and benefits.

```markdown
## Trade-offs

| Aspect | Cost |
|--------|------|
| CPU | ~900 cycles/frame (3 IRQs) |
| Memory | 4 bytes/sprite + 300 bytes code |
| Limitation | Flickers when >8 sprites share Y position |

**When to use:** 9-40 sprites, vertically distributed.
**When to avoid:** All sprites clustered at same Y, or ≤8 sprites needed.
```

### 5. Related

Links only - no prose.

```markdown
## Related

**Patterns:** [Raster Interrupts](/patterns/commodore-64/framework/raster-interrupts) | [Sprite Animation](/patterns/commodore-64/rendering/sprite-animation)

**Vault:** [VIC-II Chip](/vault/vic-ii) | [Raster Tricks 101](/vault/raster-tricks-101)

**Evolution:** Basic → [Sorted](/patterns/commodore-64/rendering/sprite-multiplexing-sorted) → [Advanced](/patterns/commodore-64/rendering/sprite-multiplexing-advanced)
```

---

## Cross-Platform Patterns

When the same concept exists across platforms, create a **comparison page**:

```
/patterns/cross-platform/sprite-collision/
```

Shows side-by-side implementations:
- C64: Hardware sprite collision registers
- Spectrum: Software bounding box (no hardware sprites)
- Amiga: Blitter-based collision
- NES: OAM sprite collision flags

This is one of the most valuable features - learners see how the same problem is solved differently based on hardware.

---

## What NOT to Include

Patterns are **not** tutorials. They assume you've done the curriculum or have equivalent knowledge.

**Don't include:**
- Step-by-step explanations of how the code works
- Historical context (that's what the Vault is for)
- Multiple pages of prose
- "Prerequisites" sections (the difficulty tag suffices)
- Genre applications (obvious from the pattern name)

**Do include:**
- Working code
- Enough comments to understand it
- Clear trade-offs
- Links to related content

---

## Code Standards

### Comments

```asm
; =============================================================================
; PATTERN NAME - VARIATION
; Brief description
; Taught: Game X, Unit Y
; CPU: ~N cycles/frame | Memory: ~N bytes
; =============================================================================
```

### Style

- Platform-appropriate assembler (ACME for C64, pasmonext for ZX Spectrum, vasm for Amiga, ca65 for NES)
- Labels flush left, instructions indented
- Named constants, not magic numbers
- Comments on non-obvious lines only

---

## File Structure

```
/website/src/pages/patterns/
  index.astro                              # Main index
  commodore-64/
    index.astro                            # C64 patterns index
    rendering/
      sprite-multiplexing-basic.mdx
      sprite-multiplexing-sorted.mdx
      scrolling-character.mdx
    input/
      joystick-reading.mdx
    audio/
      sid-music-playback.mdx
    framework/
      raster-interrupts.mdx
      game-loop.mdx
  sinclair-zx-spectrum/
    index.astro
    rendering/
      software-sprites.mdx
      attribute-clash.mdx
    input/
      keyboard-reading.mdx
    framework/
      interrupt-mode-2.mdx
  commodore-amiga/
    index.astro
    ...
  nintendo-nes/
    index.astro
    ...
  cross-platform/
    sprite-collision.mdx                   # Comparison pages
    game-loop.mdx
    scrolling.mdx
```

---

## Integration

### From Units
Units link to patterns at the end:
```markdown
For a production-ready version, see [Pattern: Sprite Multiplexing](/patterns/commodore-64/rendering/sprite-multiplexing-basic).
```

### From Vault
Vault articles link to implementations:
```markdown
See the [Pattern Library](/patterns/commodore-64/rendering/sprite-multiplexing-basic) for working code.
```

### Relationship Summary
- **Curriculum Units** = "How to build this step-by-step"
- **Pattern Library** = "Here's production code to copy"
- **Vault** = "Why this matters and how it came to be"

---

## Quality Checklist

Before publishing:
- [ ] Code compiles and runs
- [ ] Comments on non-obvious lines
- [ ] Trade-offs table complete
- [ ] At least 2 related links
- [ ] Difficulty tag accurate

---

## Version History

- **3.0 (2026-01-08):** Simplified from 12 sections to 5. Added cross-platform comparison pages. Removed redundant sections.
- **2.0 (2026-01-07):** Updated for games/units model.
- **1.0 (2025-11-15):** Original specification.
