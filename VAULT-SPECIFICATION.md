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

Eighteen categories, each with a nested URL structure:

| Type | URL Pattern | Purpose |
|------|-------------|---------|
| People | `/vault/people/{slug}` | Programmers, artists, musicians, designers |
| Companies | `/vault/companies/{slug}` | Studios, publishers, hardware manufacturers |
| Groups | `/vault/groups/{slug}` | Scene collectives, demo groups, informal organisations |
| Games | `/vault/games/{slug}` | Notable games referenced in curriculum |
| Demos | `/vault/demos/{slug}` | Demo scene productions and digital art showcases |
| Genres | `/vault/genres/{slug}` | Game genres, subgenres, and design movements |
| Techniques | `/vault/techniques/{slug}` | Programming techniques and approaches |
| Tools | `/vault/tools/{slug}` | Development tools, trackers, databases, archives |
| Emulators | `/vault/emulators/{slug}` | Emulation software preserving vintage platforms |
| Hardware | `/vault/hardware/{slug}` | Chips and components (SID, VIC-II, PPU) |
| Systems | `/vault/systems/{slug}` | Platforms (C64, Spectrum, Amiga, NES) |
| Culture | `/vault/culture/{slug}` | Movements and cultural context |
| Events | `/vault/events/{slug}` | Demo parties, LAN events, conferences |
| Magazines | `/vault/magazines/{slug}` | Gaming press, computing magazines, fanzines |
| Books | `/vault/books/{slug}` | Books about gaming, programming, computing history |
| Phenomena | `/vault/phenomena/{slug}` | Cultural phenomena, industry events, defining moments |
| Distribution | `/vault/distribution/{slug}` | Software distribution methods (shareware, cover tapes) |
| Communities | `/vault/communities/{slug}` | Subcultures and communities (demo scene, modding) |

---

## Entry Format

### Frontmatter

Required fields for all entries:

```yaml
---
title: "Entry Title"
subtitle: "Short tagline"
summary: "One-sentence description for cards and SEO."
category: "people"  # people, companies, groups, games, demos, genres, techniques, tools, emulators, hardware, systems, culture, events, magazines, books, phenomena, distribution, communities
platforms: ['c64', 'amiga']  # Optional, any platform strings
tags: ['tag1', 'tag2']
---
```

### Category-Specific Date Fields

Each category has semantic date fields. Use `null` or omit the end field if still active/alive/ongoing.

| Category | Start Field | End Field | Display Label | Example |
|----------|-------------|-----------|---------------|---------|
| People | `born` | `died` | Lived | `born: 1960` (alive) |
| Companies | `founded` | `dissolved` | Active | `founded: 1987`, `dissolved: 2001` |
| Groups | `founded` | `dissolved` | Active | `founded: 1987` (still active) |
| Games | `released` | — | Released | `released: 1993` |
| Demos | `released` | — | Released | `released: 1993` |
| Genres | `emerged` | `ended` | Era | `emerged: 1980` (ongoing) |
| Techniques | `originated` | `deprecated` | Used | `originated: 1980` (still used) |
| Tools | `released` | — | Released | `released: 1987` |
| Emulators | `released` | — | Released | `released: 1997` |
| Culture | `emerged` | `ended` | Period | `emerged: 1985`, `ended: 1995` |
| Events | `emerged` | `ended` | Held | `emerged: 1992` (ongoing) |
| Magazines | `founded` | `dissolved` | Published | `founded: 1984`, `dissolved: 1992` |
| Books | `released` | — | Published | `released: 2003` |
| Phenomena | `emerged` | `ended` | Period | `emerged: 1983`, `ended: 1985` |
| Distribution | `emerged` | `ended` | Era | `emerged: 1980` (ongoing) |
| Communities | `emerged` | `ended` | Active | `emerged: 1985` (ongoing) |
| Hardware/Systems | `introduced` | `discontinued` | Produced | `introduced: 1982`, `discontinued: 1994` |

**Example (Person):**
```yaml
---
title: "Rob Hubbard"
subtitle: "Composer of the Commodore"
summary: "One-sentence description for cards and SEO."
category: "people"
platforms: ['c64']
tags: ['composers', 'sid']
born: 1955
---
```

**Example (Company):**
```yaml
---
title: "Bullfrog Productions"
subtitle: "God game inventors"
summary: "..."
category: "companies"
platforms: ['amiga', 'pc']
tags: ['developer', 'british']
founded: 1987
dissolved: 2001
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

Covers movements, communities, and cultural phenomena that provide era context.

**Sections:** Overview, Significance, See Also

### Groups

Scene collectives, demo groups, cracking groups, and informal organisations. Not commercial entities.

**Sections:** Overview, Fast Facts (founded, location, notable members), Key Releases, See Also

### Events

Demo parties, LAN events, gaming conferences, and recurring gatherings.

**Sections:** Overview, Fast Facts (first held, location, peak attendance), Notable Moments, See Also

### Demos

Demo scene productions - non-interactive audiovisual showcases.

**Sections:** Overview, Fast Facts (group, platform, year, competition placement), Technical Achievements, See Also

### Magazines

Gaming press, computing magazines, and fanzines.

**Sections:** Overview, Fast Facts (publisher, years active, circulation), Notable Coverage, See Also

### Books

Books about gaming, programming, computing history, and the games industry.

**Sections:** Overview, Fast Facts (author, publisher, year), Key Takeaways, See Also

### Phenomena

Cultural phenomena, industry events, and defining moments (e.g., video game crash of 1983, bedroom coding era).

**Sections:** Overview, Causes/Context, Impact, See Also

### Genres

Game genres, subgenres, and design movements (e.g., roguelike, immersive sim, JRPG).

**Sections:** Overview, Defining Characteristics, Key Games, Evolution, See Also

### Tools

Development tools, music trackers, databases, and archives (e.g., ProTracker, HVSC, World of Spectrum).

**Sections:** Overview, Fast Facts (platform, release year), Features, Significance, See Also

### Emulators

Emulation software preserving vintage platforms (e.g., VICE, MAME).

**Sections:** Overview, Fast Facts (platforms emulated, release year), Accuracy/Features, See Also

### Distribution

Software distribution methods and channels (e.g., shareware, budget games, cover tapes, type-in listings).

**Sections:** Overview, How It Worked, Impact on Gaming, See Also

### Communities

Subcultures and communities around gaming and computing (e.g., demo scene, modding, speedrunning, chiptune).

**Sections:** Overview, Origins, Culture and Practices, See Also

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
/website/src/content/vault/
  people/
    rob-hubbard.mdx
    jeff-minter.mdx
  companies/
    llamasoft.mdx
    hewson.mdx
  groups/
    fairlight.mdx
    future-crew.mdx
  games/
    paradroid.mdx
    uridium.mdx
  demos/
    second-reality.mdx
    state-of-the-art.mdx
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
    arcade-ports.mdx
    import-gaming.mdx
  events/
    assembly-party.mdx
    revision-party.mdx
  magazines/
    zzap64.mdx
    crash.mdx
  books/
    racing-the-beam.mdx
  phenomena/
    video-game-crash-1983.mdx
    bedroom-coder.mdx
  distribution/
    shareware.mdx
    cover-tapes.mdx
  communities/
    demo-scene.mdx
    modding.mdx
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

- **7.0 (2026-01-19):** Expanded from 16 to 18 categories. Added distribution (shareware, cover tapes, etc.) and communities (demo scene, modding, etc.). Moved bedroom-coder to phenomena.
- **6.0 (2026-01-19):** Expanded from 13 to 16 categories. Added tools (trackers, archives), genres (game genres), and emulators (emulation software).
- **5.0 (2026-01-19):** Expanded from 7 to 13 categories. Added groups (scene collectives), demos (demo productions), events (parties/conferences), magazines, books, and phenomena. Updated file structure and date field documentation.
- **4.0 (2026-01-19):** Replaced generic `years` field with category-specific date fields (born/died, founded/dissolved, released, etc.). Added semantic display labels.
- **3.0 (2026-01-08):** Simplified from 11 entry types to 7. Reduced required fields. Shortened examples. Documented migration path.
- **2.0 (2026-01-07):** Updated for games/units model.
- **1.0 (2025-11-15):** Original specification.
