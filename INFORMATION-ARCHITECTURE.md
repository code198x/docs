# Information Architecture Specification

## Overview

This document defines how learners navigate and discover content across Code Like It's 198x. The IA connects four primary content types (Curriculum, Lessons, Vault, Pattern Library) into a coherent learning experience that supports both structured learning and exploratory discovery.

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
├── /learn/ (Lessons)
│   ├── /commodore-64/
│   │   ├── /phase-1/
│   │   │   ├── /tier-01/ (Space Shooter)
│   │   │   │   ├── /lesson-001/
│   │   │   │   ├── /lesson-002/
│   │   │   │   └── ... (32 lessons)
│   │   │   ├── /tier-02/ (Maze Chase)
│   │   │   └── ... (16 tiers)
│   │   ├── /phase-2/
│   │   └── ... (8 phases)
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

### Lessons
**Pattern:** `/learn/{platform}/phase-{N}/tier-{NN}/lesson-{NNN}/`

**Examples:**
- `/learn/commodore-64/phase-1/tier-01/lesson-001/` - First lesson
- `/learn/commodore-64/phase-2/tier-05/lesson-150/` - Horizontal Shooter, Lesson 150
- `/learn/nintendo-nes/phase-8/tier-16/lesson-512/` - Final lesson

**Why this structure:**
- Clear hierarchy: platform → phase → tier → lesson
- Predictable URLs (easy to guess next lesson)
- Human-readable
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
- Category-first organization
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
- Category organization (find all rendering patterns)
- Descriptive pattern names
- Supports evolution chains (sprite-multiplexing-basic → -sorted → -advanced)

### Curriculum Pages
**Pattern:** `/curriculum/{platform}/`

**Examples:**
- `/curriculum/commodore-64/`
- `/curriculum/sinclair-zx-spectrum/`

**Why this structure:**
- One overview page per platform
- Shows all phases, tiers, genre progression
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
- Recent additions (vault entries, new lessons)
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

**Content:**
- 8 phases with descriptions
- 16 tiers per phase (expandable/collapsible)
- Genre progression visualization
- Learning path guidance
- "Start Phase 1" CTA

**Navigation:**
- Breadcrumb: Home → Platform → Curriculum
- Phase navigation (jump to phase)
- Link to first lesson in each tier
- Related: Platform page, Vault system entry

**Example Layout:**
```
# Commodore 64 Curriculum

## Phase 1: Foundation (1982-1983)
Target quality: Early C64 games - simple graphics, basic scrolling...

[Tier 1: Space Shooter] → Lesson 1
[Tier 2: Maze Chase] → Lesson 33
[Tier 3: Platform Game] → Lesson 65
... (expand to show all 16)

## Phase 2: Enhancement (1983-1984)
Target quality: Improved C64 games - smooth scrolling...

[Show/Hide Tiers]
```

### 4. Lesson Page (`/learn/{platform}/phase-{N}/tier-{NN}/lesson-{NNN}/`)

**Purpose:** Primary learning content - teach one concept

**Required Sections:**
1. **Header:**
   - Lesson number and title
   - Tier/genre context
   - Estimated time
   - Difficulty indicator

2. **Learning Objectives:**
   - What you'll learn in this lesson
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
   - Related lessons

**Navigation:**
- Breadcrumb: Home → Platform → Curriculum → Phase N → Tier NN → Lesson NNN
- Lesson navigation: ← Previous | Next →
- Tier overview: All lessons in this tier
- Jump to: [Lesson select dropdown]

**Sidebar (contextual):**
- Tier progress: Lesson X of 32
- Phase progress: Tier X of 16
- Quick links to Vault mentions
- Related patterns
- Download code samples

**Example Layout:**
```
┌─────────────────────────────────────────────────┐
│ Breadcrumb: C64 > Phase 1 > Tier 1 > Lesson 8  │
├─────────────────────────────────────────────────┤
│ LESSON 8: Displaying More Sprites               │
│ Space Shooter • 30 mins • Intermediate          │
├──────────────────────────┬──────────────────────┤
│ MAIN CONTENT             │ SIDEBAR              │
│                          │                      │
│ ## Learning Objectives   │ Tier Progress:       │
│ - Sprite multiplexing    │ [████████░░] 8/32    │
│ - Raster interrupts      │                      │
│                          │ Related Vault:       │
│ ## Introduction          │ • VIC-II Chip        │
│ The VIC-II supports...   │ • Raster Interrupts  │
│                          │                      │
│ [Code example]           │ Related Patterns:    │
│                          │ • Sprite Mux Basic   │
│ [Screenshot]             │                      │
│                          │ Download:            │
│ ## Further Reading       │ • lesson-008.asm     │
│ **Patterns:**            │ • lesson-008.prg     │
│ - Sprite Multiplexing    │                      │
│                          │                      │
├──────────────────────────┴──────────────────────┤
│ ← Lesson 7  |  Tier Overview  |  Lesson 9 →     │
└─────────────────────────────────────────────────┘
```

### 5. Vault Entry (`/vault/{category}/{slug}/`)

**Purpose:** Provide context and background for referenced topics

**Content Structure:**
- Entry type badge (Person, Game, Technique, etc.)
- Key facts (frontmatter data displayed)
- Main content (comprehensive article)
- Cross-references (related entries)
- Curriculum integration (which lessons reference this)

**Navigation:**
- Breadcrumb: Home → Vault → Category → Entry
- Related entries (same category)
- Category browser
- Referenced in lessons (backlinks)

**Example Layout (Person):**
```
┌─────────────────────────────────────────────────┐
│ Breadcrumb: Vault > People > Martin Galway     │
├─────────────────────────────────────────────────┤
│ [PERSON] Martin Galway                          │
│                                                 │
│ Role: Musician, Sound Designer                 │
│ Platforms: Commodore 64, ZX Spectrum           │
│ Active: 1983-1988                               │
├─────────────────────────────────────────────────┤
│ [Photo if available]                            │
│                                                 │
│ ## Biography                                    │
│ Martin Galway revolutionized...                 │
│                                                 │
│ ## Notable Works                                │
│ • Comic Bakery (link to game vault)            │
│ • Times of Lore                                 │
│                                                 │
│ ## Signature Techniques                         │
│ • Multi-speed music routines                    │
│   (link to technique vault)                     │
│                                                 │
│ ## Related Entries                              │
│ People: Rob Hubbard, Ben Daglish               │
│ Hardware: SID Chip                              │
│ Companies: Ocean Software                       │
│                                                 │
│ ## Referenced In Curriculum                     │
│ • C64 Phase 2, Tier 3, Lesson 45               │
│ • C64 Phase 4, Tier 8, Lesson 230              │
└─────────────────────────────────────────────────┘
```

### 6. Pattern Entry (`/patterns/{platform}/{category}/{pattern}/`)

**Purpose:** Provide production-ready reference implementation

**Content Structure:**
- Pattern metadata (difficulty, phase, prerequisites)
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
- Referenced in lessons (backlinks)

**Example Layout:**
```
┌─────────────────────────────────────────────────┐
│ Breadcrumb: Patterns > C64 > Rendering >       │
│             Sprite Multiplexing (Basic)         │
├─────────────────────────────────────────────────┤
│ Sprite Multiplexing (Basic)                     │
│ Intermediate • Phase 2 • C64                    │
├──────────────────────────┬──────────────────────┤
│ ## Overview              │ METADATA             │
│ Displays more than 8...  │                      │
│                          │ Difficulty: ●●●○○    │
│ ## When to Use           │ Phase: 2             │
│ Use when: 9-40 sprites   │ First taught:        │
│                          │   Phase 2, Tier 1,   │
│ ## How It Works          │   Lesson 8           │
│ 1. Sort sprites by Y     │                      │
│ 2. Set up IRQ chain...   │ Prerequisites:       │
│                          │ • Raster IRQs        │
│ ## Code Implementation   │ • Sprite Basics      │
│ ```asm                   │                      │
│ ; Complete code here     │ Evolution:           │
│ ```                      │ ← (none)             │
│                          │ → Sorted (Phase 3)   │
│ ## Performance           │ → Advanced (Phase 5) │
│ CPU: ~900 cycles/frame   │                      │
│                          │ Related:             │
│ ## Variations            │ • Sprite Animation   │
│ • Sorted (Phase 3)       │ • Raster Interrupts  │
│ • Advanced (Phase 5)     │                      │
│                          │ Used in lessons:     │
│ ## Genre Applications    │ • Phase 2, Tier 1,   │
│ Essential for:           │   Lesson 8           │
│ • Shoot 'em ups          │ • Phase 3, Tier 2,   │
│ • Beat 'em ups           │   Lessons 12-14      │
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
- Lesson: `Home → C64 → Curriculum → Phase 1 → Tier 1 → Lesson 8`
- Vault: `Home → Vault → People → Martin Galway`
- Pattern: `Home → Patterns → C64 → Rendering → Sprite Multiplexing`

**Behavior:**
- Each segment is clickable (navigates up hierarchy)
- Current page not clickable
- Collapses on mobile to `... → Parent → Current`

### Contextual Navigation

**In Lessons:**
- Sequential: ← Previous Lesson | Next Lesson →
- Tier overview: "View all 32 lessons in Tier 1: Space Shooter"
- Phase overview: "View Phase 1 overview"
- Lesson jump: Dropdown to jump to any lesson in tier

**In Vault:**
- Category browser: "View all People"
- Related entries: Horizontal cards of related vault entries
- Backlinks: "Referenced in 12 lessons"

**In Patterns:**
- Evolution chain: ← Basic | Sorted | Advanced →
- Category browser: "View all Rendering patterns"
- Platform patterns: "View all C64 patterns"

### Footer Navigation

**Consistent site footer:**

```
┌─────────────────────────────────────────────────┐
│ PLATFORMS         LEARN            RESOURCES     │
│ • Commodore 64    • How to Use     • Vault       │
│ • ZX Spectrum     • Browse         • Patterns    │
│ • Amiga           • By Genre                     │
│ • NES             • By Era         ABOUT         │
│                                    • About       │
│                   COMMUNITY        • Contact     │
│                   • GitHub         • Legal       │
│                   • Discord                      │
│                                                  │
│ Code Like It's 198x © 2025                       │
└─────────────────────────────────────────────────┘
```

---

## Cross-Linking Strategy

### Inline Links in Lessons

**When to link to Vault:**
- First mention of person/company/game/technique in lesson
- Natural reading flow (don't over-link)
- Provide context without disrupting lesson

**Format:**
```markdown
...similar to [Martin Galway](/vault/people/martin-galway/)'s approach
in [Comic Bakery](/vault/games/comic-bakery/)...
```

**Visual treatment:**
- Vault links: Subtle color/underline, icon indicator
- Hover: Preview card with key facts
- Click: Navigate to full vault entry

**When to link to Patterns:**
- End of lesson in "Further Practice" section
- When referencing a technique the learner should know
- Don't link to patterns not yet taught

**Format:**
```markdown
## Further Practice

For a production-ready implementation, see
[Pattern: Sprite Multiplexing (Basic)](/patterns/c64/rendering/sprite-multiplexing-basic/).
```

### Backlinks

**Every Vault entry and Pattern shows:**
- Which lessons reference it
- Automatic bidirectional linking
- Helps learners find related content

**Display:**
```
## Referenced In Curriculum

C64:
• Phase 2, Tier 1, Lesson 8 - "Displaying More Sprites"
• Phase 3, Tier 2, Lesson 40 - "Advanced Sprite Management"
• Phase 5, Tier 1, Lesson 160 - "Sprite Multiplexing Mastery"
```

### Related Content

**Algorithmic suggestions:**
- Same platform, same phase
- Same genre, different platform
- Same technique, different implementation
- Prerequisite/follow-up lessons

**Manual curation:**
- Frontmatter in vault/pattern entries
- Editor-specified related content
- Curated learning paths

---

## Search & Discovery

### Global Search

**Search box in header, searches:**
- Lesson titles and content
- Vault entry names and content
- Pattern names and descriptions

**Results grouped by type:**
```
Search: "sprite multiplexing"

LESSONS (8)
• C64 Phase 2, Tier 1, Lesson 8 - Displaying More Sprites
• C64 Phase 3, Tier 2, Lesson 40 - Advanced Sprite Management
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
- Filter by phase, tier, category

**By Genre:** `/browse/by-genre/`
- All "Shoot 'em Up" tiers across platforms
- All "Platformer" tiers across platforms
- See how genre evolved across phases

**By Technique:** `/browse/by-technique/`
- All "sprite multiplexing" content (lessons, vault, patterns)
- All "scrolling" content across platforms
- Compare techniques between platforms

**By Era:** `/browse/by-era/`
- Group content by year/period
- "What games were released in 1989?"
- "What techniques emerged in 1985-1987?"

**By Difficulty:** `/browse/by-difficulty/`
- Beginner (Phase 1-2)
- Intermediate (Phase 3-5)
- Advanced (Phase 6-8)

**Example Browse Page:**
```
# Browse by Genre: Shoot 'em Up

## Horizontal Shooters

Commodore 64:
• Phase 1, Tier 1: Space Shooter (Lessons 1-32)
• Phase 2, Tier 5: Horizontal Shooter Enhanced (Lessons 129-160)
• Phase 3, Tier 1: Horizontal Shooter Advanced (Lessons 1-32)
...

ZX Spectrum:
• Phase 1, Tier 5: Horizontal Shooter (Lessons 129-160)
...

[Filter: Platform | Phase | Difficulty]
```

---

## User Flows

### Flow 1: New Learner Starting C64

**Path:**
1. Homepage → "Choose Platform" → Commodore 64
2. Platform page → "Start Learning" → Curriculum overview
3. Curriculum → "Phase 1" → Tier 1 → Lesson 1
4. In lesson: Read content, follow inline Vault links for context
5. End of lesson: Click "Next Lesson →"
6. After Lesson 32: "Tier complete! → Start Tier 2"

**Navigation support:**
- Clear CTAs at each step
- Progress indicators (Lesson X of 32)
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
7. Check "Referenced in lessons" to learn context

**Navigation support:**
- Fast access from global nav
- Category organization
- Search shortcut
- Clear code examples
- Evolution chain visible

### Flow 3: Exploring Cultural Context

**Path:**
1. Reading Lesson 45 (C64, Phase 2)
2. Click inline link → Vault: Martin Galway
3. From vault entry → Related: SID Chip
4. From SID Chip → Related: Bob Yannes (designer)
5. From Bob Yannes → Related: Ensoniq (company he founded)
6. Backlink → "Referenced in 8 lessons" → Discover more content

**Navigation support:**
- Rich cross-linking
- Related entries visible
- Backlinks to curriculum
- Breadcrumbs to navigate back

### Flow 4: Comparing Platforms

**Path:**
1. Browse → "By Genre" → "Platformers"
2. See all platformer tiers across all platforms
3. Compare: C64 Phase 1, Tier 3 vs. NES Phase 1, Tier 3
4. Open both lessons in tabs
5. Compare techniques, constraints, approaches
6. Check Vault → Compare VIC-II vs. PPU hardware

**Navigation support:**
- Side-by-side comparison view (future enhancement)
- Genre/technique browse pages
- Platform comparison tables in Vault

---

## Progressive Disclosure

### Lesson Complexity

**Phase 1 Lessons:**
- Simpler layout
- More explanation, less assumed knowledge
- Fewer sidebar elements
- Clear step-by-step

**Phase 8 Lessons:**
- Denser technical content
- Assumes prerequisite knowledge
- More sidebar cross-references
- Advanced patterns prominent

### Sidebar Content

**Contextual visibility:**
- Phase 1: Show minimal sidebar (progress, next lesson)
- Phase 3+: Add related patterns, vault links
- Phase 5+: Add performance notes, optimization links
- Phase 8: Full sidebar with advanced cross-references

### Content Density

**Progressive information:**
- Lessons link to Vault for "deep dive" info
- Patterns link to Vault for historical context
- Vault entries link to lessons for practical application
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

**Sticky lesson navigation:**
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
- `Lesson 8: Displaying More Sprites | C64 Phase 1 | Code Like It's 198x`
- `Martin Galway | People | The Vault | Code Like It's 198x`
- `Sprite Multiplexing (Basic) | C64 Patterns | Code Like It's 198x`

### Meta Descriptions

**Lessons:**
```
Learn sprite multiplexing on the Commodore 64. Display more than 8 sprites
using raster interrupts. Phase 1, Tier 1, Lesson 8 of our C64 game
development curriculum.
```

**Vault:**
```
Martin Galway - Pioneering C64 musician who revolutionized SID chip
composition. Known for Comic Bakery, Times of Lore, and innovative
multi-speed music routines.
```

**Patterns:**
```
Production-ready sprite multiplexing code for Commodore 64. Handles 8-24
sprites using zone-based raster interrupts. Includes performance notes
and usage examples.
```

### Structured Data

**Lessons:**
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
│  OVERVIEW   │   │   (Galway)  │   │   ENTRY    │
└──────┬──────┘   └──────┬──────┘   └─────┬──────┘
       │                 │                 │
┌──────▼──────┐          │                 │
│   LESSON    │◄─────────┴─────────────────┘
│    PAGE     │   (inline links & backlinks)
└─────────────┘
```

**Relationship types:**
- **Hierarchical:** Homepage → Platform → Curriculum → Lesson
- **Cross-reference:** Lessons ↔ Vault (inline links)
- **Cross-reference:** Lessons ↔ Patterns (further reading)
- **Cross-reference:** Patterns ↔ Vault (context links)
- **Backlinks:** All content types ↔ Lessons

---

## Implementation Priorities

### Phase 1: Core Learning Path
**Must have for launch:**
- Homepage
- Platform landing pages
- Curriculum overviews
- Lesson pages (all structure, Phase 1 content)
- Basic global nav
- Breadcrumbs
- Prev/Next lesson navigation

### Phase 2: Reference Systems
**Add after core path works:**
- Vault directory and entries
- Pattern Library directory and entries
- Inline linking from lessons
- Backlinks (automated)
- Search (basic)

### Phase 3: Discovery & Enhancement
**Nice to have:**
- Browse pages (by genre, technique, era)
- Advanced search (filters)
- Related content algorithms
- User progress tracking
- Mobile optimizations

---

## Success Metrics

**Good IA = Learners can:**
1. **Start easily** - New user to first lesson in <2 clicks
2. **Progress smoothly** - Never uncertain what to do next
3. **Find context** - Vault/patterns accessible but not required
4. **Explore freely** - Browse by interest without getting lost
5. **Return confidently** - Remember where they were, pick up easily

**Measure:**
- Click depth to first lesson
- Lesson completion rate
- Vault/pattern engagement
- Search success rate
- Browse page usage

---

*This IA creates a learning-first experience where structured curriculum progression is primary, but rich contextual exploration is always one click away.*
