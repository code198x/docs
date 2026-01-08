# The Vault: Specification

## Overview

The Vault is a reference encyclopedia providing historical, technical, and cultural context for the Code Like It's 198x curriculum. When a unit mentions a person, game, technique, or hardware component, learners can follow links to explore deeper.

**Key Principles:**
- **Concise but comprehensive** - Enough context to understand significance, not exhaustive Wikipedia articles
- **Cross-linked** - Connect related entries throughout
- **Platform-agnostic** - One shared Vault across all platforms
- **Standalone utility** - Useful independently of curriculum

---

## Entry Types

Six categories, each with a nested URL structure:

| Type | URL Pattern | Purpose |
|------|-------------|---------|
| People | `/vault/people/{slug}` | Programmers, artists, musicians, designers |
| Companies | `/vault/companies/{slug}` | Studios, publishers, hardware manufacturers |
| Games | `/vault/games/{slug}` | Notable games referenced in curriculum |
| Techniques | `/vault/techniques/{slug}` | Programming techniques and approaches |
| Hardware | `/vault/hardware/{slug}` | Chips and components (SID, VIC-II, PPU) |
| Systems | `/vault/systems/{slug}` | Platforms (C64, Spectrum, Amiga, NES) |
| Culture | `/vault/culture/{slug}` | Magazines, demos, events, music, films, movements |

**Note:** Current implementation uses flat URLs (`/vault/{slug}`). Migration to nested structure is planned.

---

## Entry Format

### Frontmatter

Keep it simple:

```yaml
---
layout: ../../layouts/VaultLayout.astro
title: "Rob Hubbard"
subtitle: "Composer of the Commodore"
summary: "One-sentence description for cards and SEO."
tags: ["c64", "sid", "composers"]
years: [1985, 1990]  # Active period or release years
---
```

### Content Structure

Every entry follows this pattern:

```markdown
## Overview
2-3 paragraphs covering what this is and why it matters.

## Fast Facts
- **Key detail:** Value
- **Another detail:** Value
- **Relevant stat:** Value

## [Topic-specific section]
Optional deeper content relevant to this entry type.

## See Also
- [Related Entry 1](/vault/category/slug)
- [Related Entry 2](/vault/category/slug)
```

---

## Entry Type Guidelines

### People

```yaml
tags: ["c64", "composers"] or ["spectrum", "programmers"]
```

**Sections:** Overview, Fast Facts (background, notable works, techniques), See Also

**Example:**
```markdown
## Overview
Rob Hubbard's C64 soundtracks pushed the SID chip to its limits. A classically trained musician turned programmer, he composed and coded his own playback routines.

## Fast Facts
- **Background:** Studied music, worked as teacher before games
- **Notable works:** Monty on the Run, Commando, International Karate
- **Technique:** Custom drivers squeezing extra channels from SID

## See Also
- [SID Chip](/vault/hardware/sid)
- [Commodore 64](/vault/systems/c64)
```

### Companies

**Sections:** Overview, Fast Facts (founded, location, key people, notable products), See Also

### Games

**Sections:** Overview, Fast Facts (developer, year, platform, genre), Technical Achievements (if notable), See Also

### Techniques

**Sections:** Overview, How It Works, Trade-offs, See Also

Link to Pattern Library for actual code: "See [Pattern: Sprite Multiplexing](/patterns/commodore-64/rendering/sprite-multiplexing) for implementation."

### Hardware

**Sections:** Overview, Specifications (as bullet list), Key Registers (if relevant), Quirks/Limitations, See Also

### Systems

**Sections:** Overview, Specifications, Historical Context, See Also

### Culture

Covers magazines, demos, events, films, music, and movements that provide era context.

**Sections:** Overview, Significance, See Also

---

## Cross-Linking

Every entry should link to 2-5 related entries:

- **People** → Companies, Games, Hardware they worked with
- **Games** → People who made them, Techniques used, Systems
- **Techniques** → Hardware exploited, Games exemplifying it, Pattern Library
- **Hardware** → Systems using it, Techniques exploiting it
- **Culture** → Contemporary people, games, events

**Link format:** `[Display Text](/vault/category/slug)`

---

## Writing Style

- **British English** - colour, organised (but "program" for software)
- **Concise** - 25-75 lines per entry, not 200
- **Informative** - Explain significance, not just facts
- **No nostalgia tourism** - Focus on what's interesting/useful

---

## Quality Checklist

Before publishing:
- [ ] Title, subtitle, summary filled in
- [ ] 2-5 cross-links to related entries
- [ ] Technical details verified (dates, specs)
- [ ] Explains why this matters
- [ ] Under 100 lines

---

## Integration

### From Units
Units link inline: "...similar to [Rob Hubbard's](/vault/people/rob-hubbard) approach..."

### From Pattern Library
Patterns link for context: "See [VIC-II](/vault/hardware/vic-ii) for hardware details."

### Relationship Summary
- **Vault** = "What it is and why it matters"
- **Pattern Library** = "Here's working code"
- **Curriculum** = "How to build it step-by-step"

---

## File Structure

```
/website/src/pages/vault/
  index.astro                    # Main vault index
  people/
    rob-hubbard.mdx
    jeff-minter.mdx
  companies/
    llamasoft.mdx
    hewson.mdx
  games/
    paradroid.mdx
    uridium.mdx
  techniques/
    raster-tricks.mdx
    sprite-multiplexing.mdx
  hardware/
    sid.mdx
    vic-ii.mdx
  systems/
    c64.mdx
    spectrum.mdx
  culture/
    zzap64.mdx
    bedroom-coder.mdx
    demo-scene.mdx
```

---

## Migration Notes

**Current state:** All entries at `/vault/{slug}` (flat)
**Target state:** Entries at `/vault/{category}/{slug}` (nested)

Migration will require:
1. Moving files to category subdirectories
2. Updating all internal links
3. Setting up redirects from old URLs

---

## Version History

- **3.0 (2026-01-08):** Simplified from 11 entry types to 7. Reduced required fields. Shortened examples. Documented migration path.
- **2.0 (2026-01-07):** Updated for games/units model.
- **1.0 (2025-11-15):** Original specification.
