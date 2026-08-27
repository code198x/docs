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

### Structure follows the material

There is no required set of sections and no required order. An entry is shaped by
what its sources support, not by a template.

**What an entry must do:**

- **Open on its subject.** The first thing a reader meets is the subject, not a
  heading that names a slot. `## Overview` above a fifty-word paragraph tells the
  reader nothing they did not get from the title.
- **Ground every claim a reader could check**, and name the source in the prose
  where it carries weight — the magazine, the issue, the date.
- **Mark contested evidence, never editing.** See *Corrections are edits, not
  content* below.
- **End with links that resolve.** `## See also`, lowercase, pointing at entries
  that exist. `npm run check:links` enforces this.

**What an entry may do**, when the material calls for it and not otherwise:

- Carry a **fast-facts block** of `**Label:** value` pairs. Worth it where an
  entry has hard data a reader will want to grab — founding dates, addresses,
  prices, scores, personnel. Not worth it where the "facts" are restatements of
  the prose.
- Use **any headings the material suggests**. Good headings are claims, not
  categories: "CRASH declined to score it" earns its place; "Reception" does not.
  Where two entries cover the same kind of subject, their headings will often
  differ, and that is correct.

**⚠ belongs in prose, never in a facts block.** A warning needs room to say what the
evidence is and why it is thin; a bullet does not have that room, so a ⚠ in a facts block is
almost always one of two things wearing a warning sign:

- **an attribution** — put the provenance in the label. Not
  `- **Author of:** *Hunchback*.` followed by `⚠ these credits come from advertising`, but
  `- **Credited in publishers' advertising, not in review boxes:** *Hunchback*.`
- **a scope** — put the limit in the label. Not `⚠ that is the whole list for this title`,
  but `- **Releases of this title, in full:**`.

Method disclosure is a third case and simply goes. "Read by eye from the index, which is
scanned badly" tells the reader about our reading. Either the figure is right and it is
stated, or it is uncertain and it says so.

Where a caveat genuinely needs to argue — sources that disagree, a claim resting on one
source, a name confused with another — it goes in the prose, where there is room to give the
evidence. The four corrections moved out of fast facts in `code198x/website#287` are the
worked examples.

**Casing:** sentence case throughout — `## Fast facts`, not `## Fast Facts`.
Proper nouns keep their capitals.

**Length:** whatever the evidence supports. A subject with one attested fact gets
a short entry; padding it to a standard shape produces the filler this section
exists to prevent.

### Corrections are edits, not content

Everything in the Vault is published. An entry is written for a reader who has
arrived to learn about the subject, not to learn how the entry came to be written.

**Incorporate the corrected information seamlessly into the entry. Remove
superseded claims. Do not add correction notes, revision summaries, editorial
commentary, "what changed" sections, or descriptions of the editing process
unless explicitly requested.**

The record of what changed belongs in the commit message and, where it matters,
in `tracker/`. It does not belong on the page.

The test: would a reader who had never seen an earlier version understand why
this sentence is here? If it only makes sense as an apology to someone who read
the old one, cut it. The same test catches the quieter form — an entry that
discusses its own fast facts, or announces what it exists to demonstrate, is
talking about itself rather than its subject.

**One thing this does not ban: warning the reader about the evidence.** A
correction note is about us. An evidence note is about the sources, and a reader
weighing a fact needs it:

- a date that contemporary and retrospective sources disagree on
- a figure that is a period estimate rather than a verified total
- a claim resting on a single source, or on one that is not in English
- a name that is confused with another person's

Those stay. The distinction is who the ⚠ is about — write "sources disagree on
this date", never "this entry had this date wrong".

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

⚠⚠ **State the period an entry describes, and check for a change of owner.**
A company that changes *name* leaves a visible seam and gets written up. A
company that changes *owner* while keeping its name, logo and staff leaves no
seam at all — every source before and after says the same word and means
something different by it. Entries written without checking read as confidently
wrong:

| Company | Change | Missed because |
|---|---|---|
| Team17 | 1995, exclusive distribution by Ocean, dual-branded | name unchanged |
| Palace | 1991, bought by Leisure Holding (French, owns Titus) | name unchanged |
| Quicksilva | 1984, bought by Argus Press Software (later Grandslam) | name unchanged |

Run `python3 ops/scripts/ownership_check.py <Company>` in the `198x` umbrella
before publishing. It prints the magazine windows for a human to read; it does
not decide. Where a change is found, say which years the entry's description
covers.

### Games

**Sections:** Overview, Fast Facts (developer, year, platform, genre), Technical Achievements (if notable), See Also

### Techniques

**Sections:** Overview, How It Works, Trade-offs, See Also

Link to Pattern Library for actual code: "See [Pattern: Sprite Multiplexing](/patterns/commodore-64/assembly/rendering/sprite-multiplexing) for implementation."

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
- [ ] **Every `/vault/...` link resolves** — the site build does NOT catch dead
      Vault links, so check them directly
- [ ] Technical details verified (dates, specs)
- [ ] **Companies and studios: ownership checked** (`ownership_check.py`), and
      the period the entry describes stated where it changed hands
- [ ] Claims sourced — and where a claim comes from advertising or from one
      side of a dispute, said so in the entry
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
