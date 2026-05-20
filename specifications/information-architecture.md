# Information Architecture Specification

**Version:** 2.1
**Last Updated:** 2026-01-19

## Overview

This document defines how learners navigate and discover content across Code Like It's 198x. The IA connects four primary content types (Curriculum, Units, Vault, Pattern Library) into a coherent learning experience that supports both structured learning and exploratory discovery.

**Core Principles:**
- **Learning-first navigation** - Curriculum progression is primary path
- **Rich context available** - Vault/Patterns accessible but not required
- **Multiple discovery modes** - Browse by platform, genre, technique, era
- **No dead ends** - Every page links to related content
- **Progressive disclosure** - Complex information revealed as needed

---

## Site Structure

### Primary Content Areas

```
/
├── / (Homepage)
├── /platforms/ (Platform directory)
│   ├── /commodore-64/
│   ├── /sinclair-zx-spectrum/
│   ├── /commodore-amiga/
│   └── /nintendo-nes/
│
├── /curriculum/ (Curriculum overviews)
│   ├── /commodore-64/
│   ├── /sinclair-zx-spectrum/
│   ├── /commodore-amiga/
│   └── /nintendo-nes/
│
├── /learn/ (Units)
│   ├── /commodore-64/
│   │   ├── /game-01-sid-symphony/
│   │   │   ├── /unit-01-first-notes/
│   │   │   ├── /unit-02-adsr-envelopes/
│   │   │   └── ... (128 units)
│   │   ├── /game-02-starfield/
│   │   └── ... (16 games)
│   └── ... (all platforms)
│
├── /vault/ (Reference encyclopedia)
│   ├── /people/
│   ├── /companies/
│   ├── /games/
│   ├── /techniques/
│   ├── /hardware/
│   ├── /systems/
│   ├── /events/
│   ├── /movies/
│   ├── /music/
│   ├── /publications/
│   └── /demos/
│
├── /patterns/ (Pattern Library)
│   ├── /commodore-64/
│   │   ├── /rendering/
│   │   ├── /input/
│   │   ├── /audio/
│   │   ├── /physics/
│   │   ├── /ai/
│   │   ├── /framework/
│   │   ├── /optimization/
│   │   └── /data/
│   └── ... (all platforms)
│
├── /about/ (Project information)
├── /how-to-use/ (Site guide)
└── /browse/ (Discovery tools)
    ├── /by-platform/
    ├── /by-genre/
    ├── /by-technique/
    ├── /by-era/
    └── /by-difficulty/
```

---

## URL Patterns

### Units
**Pattern:** `/learn/{platform}/game-{NN}-{game-slug}/unit-{NN}-{unit-slug}/`

**Examples:**
- `/learn/commodore-64/game-01-sid-symphony/unit-01-first-notes/` - First unit
- `/learn/commodore-64/game-09-sprite-storm/unit-12-multiplexing/` - Advanced game
- `/learn/nintendo-nes/game-16-requiem-for-a-mapper/unit-128-final-polish/` - Final unit

**Why this structure:**
- Clear hierarchy: platform → game → unit
- Numbered AND slugged for sort order + readability
- Human-readable URLs (SEO-friendly)
- Supports breadcrumb navigation naturally

### Vault Entries
**Pattern:** `/vault/{category}/{slug}/`

**Examples:**
- `/vault/people/martin-galway/`
- `/vault/games/mayhem-in-monsterland/`
- `/vault/techniques/c64-sprite-multiplexing/`
- `/vault/hardware/sid-6581/`
- `/vault/events/fall-of-berlin-wall/`

**Why this structure:**
- Category-first organisation
- Shared namespace (one vault for all platforms)
- Descriptive slugs
- Supports browsing by category

### Pattern Library
**Pattern:** `/patterns/{platform}/{category}/{pattern-name}/`

**Examples:**
- `/patterns/commodore-64/rendering/sprite-multiplexing-basic/`
- `/patterns/sinclair-zx-spectrum/audio/beeper-sound-effects/`
- `/patterns/commodore-amiga/rendering/copper-palette-effects/`
- `/patterns/nintendo-nes/physics/tile-collision/`

**Why this structure:**
- Platform-first (code is platform-specific)
- Category organisation (find all rendering patterns)
- Descriptive pattern names
- Supports evolution chains (sprite-multiplexing-basic → -sorted → -advanced)

### Curriculum Pages
**Pattern:** `/curriculum/{platform}/`

**Examples:**
- `/curriculum/commodore-64/`
- `/curriculum/sinclair-zx-spectrum/`

**Why this structure:**
- One overview page per platform
- Shows all games, unit counts, skill progression
- Entry point for structured learning

### Platform Landing Pages
**Pattern:** `/platforms/{platform}/`

**Examples:**
- `/platforms/commodore-64/`
- `/platforms/nintendo-nes/`

**Content:**
- Platform overview and history
- Links to curriculum, vault entries, patterns
- Technical specifications
- Notable games/developers
- Getting started guide

---

## Page Types & Templates

### 1. Homepage (`/`)

**Purpose:** Entry point to the site, orient new visitors

**Content:**
- Site tagline/mission
- Platform selector (4 primary platforms prominently)
- Quick links to popular content
- Recent additions (vault entries, new units)
- "Start Learning" CTA

**Navigation:**
- Primary: Links to platform landing pages
- Secondary: About, How to Use, Browse

### 2. Platform Landing Page (`/platforms/{platform}/`)

**Purpose:** Overview and entry point for a specific platform

**Content:**
- Platform name and era (e.g., "Commodore 64 (1982-1994)")
- Brief history and cultural significance
- Technical specs overview
- Quick links:
  - Start learning (→ `/curriculum/{platform}/`)
  - Browse patterns (→ `/patterns/{platform}/`)
  - Explore vault (→ `/vault/systems/{platform}/`)
- Featured games for this platform
- Notable developers/companies

**Navigation:**
- Breadcrumb: Home → Platform
- Global nav: Other platforms
- Related: Curriculum, Patterns, Vault entries

### 3. Curriculum Overview (`/curriculum/{platform}/`)

**Purpose:** Show complete curriculum structure for a platform

**Note:** Some platforms have multiple curricula:
- **BASIC Gateway (Optional):** 8 games teaching fundamentals through an accessible language
- **Assembly Main:** 16 games teaching professional-level hardware programming

Platforms with BASIC gateways: Commodore 64 (BASIC V2), ZX Spectrum (Sinclair BASIC), Amiga (AMOS BASIC)
Platforms without BASIC gateway: NES (assembly only)

**Content:**
- Curriculum selector (if platform has multiple)
- Game sequence with descriptions
- Unit counts per game
- Skill progression visualisation
- Learning path guidance
- "Start Game 1" CTA

**Navigation:**
- Breadcrumb: Home → Platform → Curriculum
- Curriculum tabs (if multiple: "BASIC Gateway" / "Assembly")
- Game navigation (jump to any game)
- Link to first unit in each game
- Related: Platform page, Vault system entry

**Example Layout (Platform with BASIC Gateway):**
```
# Commodore 64 Curriculum

[BASIC V2 Gateway] [6510 Assembly]  ← Curriculum tabs

## BASIC V2 Gateway (Optional - 8 Games, 512 Units)

Start here if you're new to programming or want a gentler introduction.

[Game 1: Number Hunter] → Unit 1
Number guessing with INPUT and IF/THEN

[Game 2: Cosmic Drift] → Unit 1
Animation with POKE to screen memory

... (8 games)

---

## 6510 Assembly (Main - 16 Games, 1,536 Units)

[Game 1: SID Symphony] → Unit 1
Rhythm game introducing the SID chip

[Game 2: Starfield] → Unit 1
Space shooter with hardware sprites

... (show all 16 games)

## Advanced Games (128 Units Each)

[Game 11: Dungeon Crawl] → Unit 1
Top-down adventure with save system

...

## Capstone (256 Units)

[Game 16: Symphony's End] → Unit 1
Commercial-quality action-adventure
```

### 4. Unit Page (`/learn/{platform}/game-{NN}-{slug}/unit-{NN}-{slug}/`)

**Purpose:** Primary learning content - teach concepts that produce a working result

**Required Sections:**
1. **Header:**
   - Unit number and title
   - Game context
   - Estimated time
   - Difficulty indicator

2. **Opening:**
   - What this unit teaches
   - What you'll build
   - Prerequisites (with links)

3. **Main Content:**
   - Concept introduction
   - Step-by-step implementation
   - Code examples (syntax highlighted)
   - Screenshots/diagrams
   - Common pitfalls
   - Testing/verification

4. **Further Practice:**
   - Exercises to reinforce learning
   - Variations to try

5. **Further Reading:**
   - Pattern Library references
   - Vault contextual links
   - Related units

6. **What You've Learnt:**
   - Bullet summary of capabilities

**Navigation:**
- Breadcrumb: Home → Platform → Game → Unit
- Unit navigation: ← Previous | Next →
- Game overview: All units in this game
- Jump to: [Unit select dropdown]

**Sidebar (contextual):**
- Game progress: Unit X of N (varies by game: 8, 16, 32, 64, or 128)
- Quick links to Vault mentions
- Related patterns
- Download code samples

**Example Layout:**
```
┌─────────────────────────────────────────────────┐
│ Breadcrumb: C64 > SID Symphony > Unit 3         │
├─────────────────────────────────────────────────┤
│ UNIT 3: Reading the Keyboard                    │
│ SID Symphony • 45 mins • Foundation             │
├──────────────────────────┬──────────────────────┤
│ MAIN CONTENT             │ SIDEBAR              │
│                          │                      │
│ ## What You'll Build     │ Game Progress:       │
│ A keyboard scanner that  │ [██░░░░░░] 3/128     │
│ detects which key is...  │                      │
│                          │ Related Vault:       │
│ ## Introduction          │ • CIA Chip           │
│ The C64 keyboard is a    │ • Keyboard Matrix    │
│ matrix scanned by...     │                      │
│                          │ Related Patterns:    │
│ [Code example]           │ • Key Debounce       │
│                          │                      │
│ [Screenshot]             │ Download:            │
│                          │ • unit-03.bas        │
│ ## What You've Learnt    │                      │
│ - Keyboard matrix        │                      │
│ - CIA register reading   │                      │
│                          │                      │
├──────────────────────────┴──────────────────────┤
│ ← Unit 2  |  Game Overview  |  Unit 4 →         │
└─────────────────────────────────────────────────┘
```

### 5. Vault Entry (`/vault/{category}/{slug}/`)

**Purpose:** Provide context and background for referenced topics

**Content Structure:**
- Entry type badge (Person, Game, Technique, etc.)
- Key facts (frontmatter data displayed)
- Main content (comprehensive article)
- Cross-references (related entries)
- Curriculum integration (which units reference this)

**Navigation:**
- Breadcrumb: Home → Vault → Category → Entry
- Related entries (same category)
- Category browser
- Referenced in units (backlinks)

**Example Layout (Person):**
```
┌─────────────────────────────────────────────────┐
│ Breadcrumb: Vault > People > Rob Hubbard        │
├─────────────────────────────────────────────────┤
│ [PERSON] Rob Hubbard                            │
│                                                 │
│ Role: Musician, Sound Designer                  │
│ Platforms: Commodore 64, Amiga                  │
│ Active: 1985-1989                               │
├─────────────────────────────────────────────────┤
│ [Photo if available]                            │
│                                                 │
│ ## Biography                                    │
│ Rob Hubbard defined the sound of the C64...     │
│                                                 │
│ ## Notable Works                                │
│ • Commando (link to game vault)                 │
│ • Monty on the Run                              │
│                                                 │
│ ## Signature Techniques                         │
│ • Multi-speed playback routines                 │
│   (link to technique vault)                     │
│                                                 │
│ ## Related Entries                              │
│ People: Martin Galway, Ben Daglish              │
│ Hardware: SID Chip                              │
│ Companies: Ocean Software                       │
│                                                 │
│ ## Referenced In Curriculum                     │
│ • C64 Game 1: SID Symphony, Units 8-12          │
│ • C64 Game 11: Dungeon Crawl, Unit 45           │
└─────────────────────────────────────────────────┘
```

### 6. Pattern Entry (`/patterns/{platform}/{category}/{pattern}/`)

**Purpose:** Provide production-ready reference implementation

**Content Structure:**
- Pattern metadata (difficulty, game introduced, prerequisites)
- Overview (what it does, when to use)
- How it works (technical explanation)
- Code implementation (complete, commented)
- Performance/trade-offs
- Variations (links to related patterns)
- Evolution chain (if applicable)
- Genre applications
- Curriculum integration (where taught)

**Navigation:**
- Breadcrumb: Home → Patterns → Platform → Category → Pattern
- Related patterns (same category)
- Evolution chain (previous/next versions)
- Platform pattern browser
- Referenced in units (backlinks)

**Example Layout:**
```
┌─────────────────────────────────────────────────┐
│ Breadcrumb: Patterns > C64 > Rendering >        │
│             Sprite Multiplexing (Basic)         │
├─────────────────────────────────────────────────┤
│ Sprite Multiplexing (Basic)                     │
│ Intermediate • Game 9 • C64                     │
├──────────────────────────┬──────────────────────┤
│ ## Overview              │ METADATA             │
│ Displays more than 8...  │                      │
│                          │ Difficulty: ●●●○○    │
│ ## When to Use           │ Introduced: Game 9   │
│ Use when: 9-40 sprites   │ First taught:        │
│                          │   Sprite Storm,      │
│ ## How It Works          │   Unit 12            │
│ 1. Sort sprites by Y     │                      │
│ 2. Set up IRQ chain...   │ Prerequisites:       │
│                          │ • Raster IRQs        │
│ ## Code Implementation   │ • Sprite Basics      │
│ ```asm                   │                      │
│ ; Complete code here     │ Evolution:           │
│ ```                      │ ← (none)             │
│                          │ → Sorted (Game 11)   │
│ ## Performance           │ → Advanced (Game 13) │
│ CPU: ~900 cycles/frame   │                      │
│                          │ Related:             │
│ ## Variations            │ • Sprite Animation   │
│ • Sorted (Game 11)       │ • Raster Interrupts  │
│ • Advanced (Game 13)     │                      │
│                          │ Used in units:       │
│ ## Genre Applications    │ • Game 9, Units 12-16│
│ Essential for:           │ • Game 11, Unit 8    │
│ • Shoot 'em ups          │ • Game 12, Units 4-8 │
│ • Beat 'em ups           │                      │
└──────────────────────────┴──────────────────────┘
```

---

## Navigation Systems

### Global Navigation (Site Header)

**Always visible, consistent across all pages:**

```
┌─────────────────────────────────────────────────────────┐
│ [LOGO] Code Like It's 198x                              │
│                                                         │
│ [Platforms ▼] [Vault] [Patterns] [About] [Search 🔍]   │
│                                                         │
│ Platform Dropdown:                                      │
│   • Commodore 64                                        │
│   • Sinclair ZX Spectrum                                │
│   • Commodore Amiga                                     │
│   • Nintendo NES                                        │
│   ─────────────                                         │
│   • Browse All Platforms                                │
└─────────────────────────────────────────────────────────┘
```

**Platform Dropdown Expanded:**
- Shows 4 primary platforms
- Each links to `/platforms/{platform}/`
- "Browse All" → `/platforms/` (directory of all current/future platforms)

### Breadcrumb Navigation

**Pattern:** `Home → Level 1 → Level 2 → Current Page`

**Examples:**
- Unit: `Home → C64 → SID Symphony → Unit 3: Reading the Keyboard`
- Vault: `Home → Vault → People → Rob Hubbard`
- Pattern: `Home → Patterns → C64 → Rendering → Sprite Multiplexing`

**Behaviour:**
- Each segment is clickable (navigates up hierarchy)
- Current page not clickable
- Collapses on mobile to `... → Parent → Current`

### Contextual Navigation

**In Units:**
- Sequential: ← Previous Unit | Next Unit →
- Game overview: "View all 64 units in SID Symphony"
- Curriculum overview: "View C64 Curriculum"
- Unit jump: Dropdown to jump to any unit in game

**In Vault:**
- Category browser: "View all People"
- Related entries: Horizontal cards of related vault entries
- Backlinks: "Referenced in 12 units"

**In Patterns:**
- Evolution chain: ← Basic | Sorted | Advanced →
- Category browser: "View all Rendering patterns"
- Platform patterns: "View all C64 patterns"

### Footer Navigation

**Consistent site footer:**

```
┌─────────────────────────────────────────────────┐
│ PLATFORMS         LEARN            RESOURCES    │
│ • Commodore 64    • How to Use     • Vault      │
│ • ZX Spectrum     • Browse         • Patterns   │
│ • Amiga           • By Genre                    │
│ • NES             • By Era         ABOUT        │
│                                    • About      │
│                   COMMUNITY        • Contact    │
│                   • GitHub         • Legal      │
│                   • Discord                     │
│                                                 │
│ Code Like It's 198x © 2026                      │
└─────────────────────────────────────────────────┘
```

---

## Cross-Linking Strategy

### Inline Links in Units

**When to link to Vault:**
- First mention of person/company/game/technique in unit
- Natural reading flow (don't over-link)
- Provide context without disrupting unit

**Format:**
```markdown
...similar to [Rob Hubbard](/vault/people/rob-hubbard/)'s approach
in [Commando](/vault/games/commando/)...
```

**Visual treatment:**
- Vault links: Subtle colour/underline, icon indicator
- Hover: Preview card with key facts
- Click: Navigate to full vault entry

**When to link to Patterns:**
- End of unit in "Further Reading" section
- When referencing a technique the learner should know
- Don't link to patterns not yet taught

**Format:**
```markdown
## Further Reading

For a production-ready implementation, see
[Pattern: Sprite Multiplexing (Basic)](/patterns/c64/rendering/sprite-multiplexing-basic/).
```

### Backlinks

**Every Vault entry and Pattern shows:**
- Which units reference it
- Automatic bidirectional linking
- Helps learners find related content

**Display:**
```
## Referenced In Curriculum

C64:
• Game 1: SID Symphony, Unit 8 - "Multi-voice Basics"
• Game 9: Sprite Storm, Unit 12 - "Multiplexing Introduction"
• Game 11: Dungeon Crawl, Unit 45 - "Background Music"
```

### Related Content

**Algorithmic suggestions:**
- Same platform, same game
- Same genre, different platform
- Same technique, different implementation
- Prerequisite/follow-up units

**Manual curation:**
- Frontmatter in vault/pattern entries
- Editor-specified related content
- Curated learning paths

---

## Search & Discovery

### Global Search

**Search box in header, searches:**
- Unit titles and content
- Vault entry names and content
- Pattern names and descriptions

**Results grouped by type:**
```
Search: "sprite multiplexing"

UNITS (8)
• C64 Game 9: Sprite Storm, Unit 12 - Multiplexing Introduction
• C64 Game 9: Sprite Storm, Unit 14 - Sorted Sprite Lists
...

VAULT (3)
• Sprite Multiplexing Technique
• VIC-II Chip
• Mayhem in Monsterland

PATTERNS (4)
• C64: Sprite Multiplexing (Basic)
• C64: Sprite Multiplexing (Sorted)
...
```

### Browse Pages (`/browse/`)

**Filter/discover content by:**

**By Platform:** `/browse/by-platform/`
- List all content for selected platform
- Filter by game, category

**By Genre:** `/browse/by-genre/`
- All "Shoot 'em Up" games across platforms
- All "Platformer" games across platforms
- See how genre evolved across platforms

**By Technique:** `/browse/by-technique/`
- All "sprite multiplexing" content (units, vault, patterns)
- All "scrolling" content across platforms
- Compare techniques between platforms

**By Era:** `/browse/by-era/`
- Group content by year/period
- "What games were released in 1989?"
- "What techniques emerged in 1985-1987?"

**By Difficulty:** `/browse/by-difficulty/`
- Foundation (Games 1-10)
- Advanced (Games 11-15)
- Capstone (Game 16)

---

## User Flows

### Flow 1: New Learner Starting C64

**Path:**
1. Homepage → "Choose Platform" → Commodore 64
2. Platform page → "Start Learning" → Curriculum overview
3. Curriculum → "Game 1: SID Symphony" → Unit 1
4. In unit: Read content, follow inline Vault links for context
5. End of unit: Click "Next Unit →"
6. After Unit 64: "Game complete! → Start Game 2"

**Navigation support:**
- Clear CTAs at each step
- Progress indicators (Unit X of 64)
- Option to skip ahead (but discouraged)
- Return to curriculum overview anytime

### Flow 2: Experienced Developer Looking for Specific Pattern

**Path:**
1. Homepage → Global nav "Patterns"
2. Patterns directory → Select platform (C64)
3. Category browser → "Rendering"
4. Scan list → "Sprite Multiplexing (Advanced)"
5. Read pattern, copy code
6. Related patterns sidebar → "Sprite Animation"
7. Check "Referenced in units" to learn context

**Navigation support:**
- Fast access from global nav
- Category organisation
- Search shortcut
- Clear code examples
- Evolution chain visible

### Flow 3: Exploring Cultural Context

**Path:**
1. Reading Unit 8 (C64, Game 1: SID Symphony)
2. Click inline link → Vault: Rob Hubbard
3. From vault entry → Related: SID Chip
4. From SID Chip → Related: Bob Yannes (designer)
5. From Bob Yannes → Related: Ensoniq (company he founded)
6. Backlink → "Referenced in 8 units" → Discover more content

**Navigation support:**
- Rich cross-linking
- Related entries visible
- Backlinks to curriculum
- Breadcrumbs to navigate back

### Flow 4: Comparing Platforms

**Path:**
1. Browse → "By Genre" → "Platformers"
2. See all platformer games across all platforms
3. Compare: C64 Game 4: Platform Panic vs. NES Game 2: Crate Escape
4. Open both games in tabs
5. Compare techniques, constraints, approaches
6. Check Vault → Compare VIC-II vs. PPU hardware

**Navigation support:**
- Side-by-side comparison view (future enhancement)
- Genre/technique browse pages
- Platform comparison tables in Vault

---

## Progressive Disclosure

### Unit Complexity

**Foundation Games (1-10):**
- Simpler layout
- More explanation, less assumed knowledge
- Fewer sidebar elements
- Clear step-by-step

**Advanced Games (11-15):**
- Denser technical content
- Assumes prerequisite knowledge
- More sidebar cross-references
- Advanced patterns prominent

**Capstone (Game 16):**
- Full technical depth
- Professional-level techniques
- Comprehensive cross-references

### Sidebar Content

**Contextual visibility:**
- Game 1-4: Show minimal sidebar (progress, next unit)
- Game 5-10: Add related patterns, vault links
- Game 11-15: Add performance notes, optimisation links
- Game 16: Full sidebar with advanced cross-references

### Content Density

**Progressive information:**
- Units link to Vault for "deep dive" info
- Patterns link to Vault for historical context
- Vault entries link to units for practical application
- Learner chooses depth based on interest

---

## Mobile Considerations

### Responsive Breakpoints

**Desktop (1024px+):**
- Full sidebar visible
- Wide code blocks
- Multi-column footer

**Tablet (768px - 1023px):**
- Collapsible sidebar
- Readable code blocks
- Two-column footer

**Mobile (<768px):**
- Hamburger menu
- No sidebar (move to bottom)
- Single-column layout
- Simplified breadcrumbs (... → Parent → Current)

### Mobile-Specific Features

**Sticky unit navigation:**
- Prev/Next always accessible
- Floating back-to-top button

**Code blocks:**
- Horizontal scroll
- Copy button prominent
- Syntax highlighting preserved

**Vault previews:**
- Inline expansion (no modal)
- Tap to expand, tap again to navigate

---

## Metadata & SEO

### Page Titles

**Format:** `{Specific} | {Context} | Code Like It's 198x`

**Examples:**
- `Unit 3: Reading the Keyboard | C64 SID Symphony | Code Like It's 198x`
- `Rob Hubbard | People | The Vault | Code Like It's 198x`
- `Sprite Multiplexing (Basic) | C64 Patterns | Code Like It's 198x`

### Meta Descriptions

**Units:**
```
Learn keyboard scanning on the Commodore 64. Read the CIA chip's keyboard
matrix to detect key presses for your rhythm game. Game 1: SID Symphony,
Unit 3 of our C64 game development curriculum.
```

**Vault:**
```
Rob Hubbard - Legendary C64 musician who defined the SID chip sound.
Known for Commando, Monty on the Run, and pioneering multi-speed
music routines.
```

**Patterns:**
```
Production-ready sprite multiplexing code for Commodore 64. Handles 8-24
sprites using zone-based raster interrupts. Includes performance notes
and usage examples.
```

### Structured Data

**Units:**
- Schema.org/LearningResource
- Course hierarchy
- Estimated time
- Skill level

**Vault:**
- Schema.org/Person (for people)
- Schema.org/VideoGame (for games)
- Schema.org/Article (for techniques)

---

## Content Relationship Diagram

```
┌─────────────┐
│  HOMEPAGE   │
└──────┬──────┘
       │
       ├─────────────────┬─────────────────┬─────────────
       │                 │                 │
┌──────▼──────┐   ┌──────▼──────┐   ┌─────▼──────┐
│  PLATFORMS  │   │    VAULT    │   │  PATTERNS  │
│  DIRECTORY  │   │  DIRECTORY  │   │ DIRECTORY  │
└──────┬──────┘   └──────┬──────┘   └─────┬──────┘
       │                 │                 │
┌──────▼──────┐   ┌──────▼──────┐   ┌─────▼──────┐
│  PLATFORM   │   │   CATEGORY  │   │  PLATFORM  │
│   LANDING   │   │   (People)  │   │ CATEGORIES │
└──────┬──────┘   └──────┬──────┘   └─────┬──────┘
       │                 │                 │
┌──────▼──────┐   ┌──────▼──────┐   ┌─────▼──────┐
│ CURRICULUM  │   │    ENTRY    │   │  PATTERN   │
│  OVERVIEW   │   │  (Hubbard)  │   │   ENTRY    │
└──────┬──────┘   └──────┬──────┘   └─────┬──────┘
       │                 │                 │
┌──────▼──────┐          │                 │
│    GAME     │          │                 │
│   LANDING   │          │                 │
└──────┬──────┘          │                 │
       │                 │                 │
┌──────▼──────┐          │                 │
│    UNIT     │◄─────────┴─────────────────┘
│    PAGE     │   (inline links & backlinks)
└─────────────┘
```

**Relationship types:**
- **Hierarchical:** Homepage → Platform → Curriculum → Game → Unit
- **Cross-reference:** Units ↔ Vault (inline links)
- **Cross-reference:** Units ↔ Patterns (further reading)
- **Cross-reference:** Patterns ↔ Vault (context links)
- **Backlinks:** All content types ↔ Units

---

## Implementation Priorities

### Phase 1: Core Learning Path
**Must have for launch:**
- Homepage
- Platform landing pages
- Curriculum overviews
- Game landing pages
- Unit pages (all structure, Game 1 content)
- Basic global nav
- Breadcrumbs
- Prev/Next unit navigation

### Phase 2: Reference Systems
**Add after core path works:**
- Vault directory and entries
- Pattern Library directory and entries
- Inline linking from units
- Backlinks (automated)
- Search (basic)

### Phase 3: Discovery & Enhancement
**Nice to have:**
- Browse pages (by genre, technique, era)
- Advanced search (filters)
- Related content algorithms
- User progress tracking
- Mobile optimisations

---

## Success Metrics

**Good IA = Learners can:**
1. **Start easily** - New user to first unit in <2 clicks
2. **Progress smoothly** - Never uncertain what to do next
3. **Find context** - Vault/patterns accessible but not required
4. **Explore freely** - Browse by interest without getting lost
5. **Return confidently** - Remember where they were, pick up easily

**Measure:**
- Click depth to first unit
- Unit completion rate
- Vault/pattern engagement
- Search success rate
- Browse page usage

---

## Version History

- **2.1 (2026-01-19):** Updated unit counts (SID Symphony has 128 units, not 64). Fixed variable unit counts in sidebar example.
- **2.0 (2026-01-07):** Complete rewrite for games/units model. Updated all URL patterns, page types, and navigation.
- **1.0 (2025-01-15):** Original specification using phases/tiers/lessons model.
