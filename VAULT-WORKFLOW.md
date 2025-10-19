# The Vault: Historical Context & Reference Guide

**Last Updated:** 2025-01-17
**Purpose:** Create a living timeline showing when, where, and by whom the retro computing era happened.

---

## The Vision

The Vault is more than a reference collection. It's the historical context that makes lessons come alive.

**Not:** Dry encyclopedia entries
**But:** The story of real people solving real problems in a specific moment in time

When a lesson mentions "Andrew Braybrook's *Uridium*", learners can explore:
- Who Andrew Braybrook was (person)
- When *Uridium* was released (1986)
- What hardware it targeted (C64, VIC-II chip)
- What company published it (Hewson Consultants)
- What technique it pioneered (sprite multiplexing)
- What else was happening that year (timeline context)

**The goal:** Help learners understand they're learning techniques from a REAL era, not abstract "retro times."

---

## Entry Categories

### **1. Hardware**
Chips, systems, peripherals

**Examples:**
- VIC-II chip
- SID chip
- Commodore 64
- 1541 disk drive

**Include:**
- Designer (if known)
- Release date
- Technical specifications
- What it enabled creatively
- Complete register reference (where applicable)

---

### **2. Games**
Specific titles that pioneered techniques or defined genres

**Examples:**
- *Uridium*
- *Paradroid*
- *Impossible Mission*

**Include:**
- Release year
- Programmer(s)
- Publisher
- Systems (C64, Spectrum, etc.)
- What technique it pioneered
- Which lessons reference it

---

### **3. People**
Programmers, designers, chip designers, publishers

**Examples:**
- Andrew Braybrook
- Jeff Minter
- Bob Yannes (SID designer)

**Include:**
- Birth year (death year if applicable)
- Key works
- Companies worked for
- Technical innovations
- Timeline of career

---

### **4. Companies**
Publishers, studios, hardware manufacturers

**Examples:**
- Llamasoft
- Hewson Consultants
- Commodore International

**Include:**
- Founded date (closed date if applicable)
- Key people
- Notable releases
- Market position
- What they enabled

---

### **5. Events**
Product launches, company milestones, market shifts

**Examples:**
- "Commodore 64 UK Release (1982)"
- "Commodore Bankruptcy (1994)"
- "First C64 Demo Scene Party (1986)"

**Include:**
- Precise date (or month/year)
- Who was involved
- Why it mattered
- What changed afterward

---

### **6. Publications**
Magazines, fanzines that shaped the scene

**Examples:**
- Zzap!64
- Crash
- Your Sinclair

**Include:**
- Publication dates (first issue, last issue)
- Key writers/editors
- Influence on the scene
- Notable features/columns

---

### **7. Concepts**
Techniques, cultural movements, industry practices

**Examples:**
- Sprite Multiplexing
- The Demo Scene
- Bedroom Coding

**Include:**
- When it emerged
- Who pioneered it
- How it spread
- Modern equivalents

---

## Frontmatter Structure

### **All Entries**

```yaml
---
layout: ../../layouts/VaultLayout.astro
title: "Entry Name"
subtitle: "One-line characterization"
summary: "One-sentence hook that avoids dry encyclopedia style"
category: "hardware|game|person|company|event|publication|concept"
years: [start_year, end_year]  # Or single year for events
system_tags: [C64, Spectrum, NES]  # Applicable systems
---
```

### **Category-Specific Fields**

**Hardware:**
```yaml
tech_tags: ["Video", "Sound", "I/O"]
designer: "Bob Yannes"
release_date: "1982-08"
```

**Games:**
```yaml
tech_tags: ["Platformer", "Sprite multiplexing"]
programmer: "Andrew Braybrook"
publisher: "Hewson Consultants"
release_date: "1986"
platforms: [C64, Spectrum]
```

**People:**
```yaml
people_tags: ["Programmers", "Chip designers"]
born: "1962"
died: null  # Or year if applicable
companies: ["Commodore", "Ensoniq"]
notable_works: ["SID chip", "Ensoniq soundcards"]
```

**Companies:**
```yaml
founded: "1982"
closed: "1994"  # null if still operating
founders: ["Jeff Minter"]
notable_releases: ["Attack of the Mutant Camels", "Gridrunner"]
```

**Events:**
```yaml
event_date: "1982-09"  # YYYY-MM or YYYY-MM-DD
location: "United Kingdom"
participants: ["Commodore International"]
```

**Publications:**
```yaml
first_issue: "1985-05"
last_issue: "1992-12"  # null if still publishing
publisher: "Newsfield Publications"
editors: ["Roger Kean", "Julian Rignall"]
```

**Concepts:**
```yaml
tech_tags: ["Graphics techniques", "Demo scene"]
emerged: "1984"
pioneers: ["Andrew Braybrook"]
```

---

## Content Structure

### **Overview** (Required)
2-3 sentences establishing who/what this is and why it matters.

**Tone:** Energetic, personal, not dry.

**Good:**
```markdown
Jeff Minter founded Llamasoft in 1982 and promptly filled British shelves
with neon shooters starring ungulates and particle storms. His work combined
tight arcade mechanics with humour that felt unmistakably personal.
```

**Dry (avoid this):**
```markdown
Jeff Minter (born 1962) is a British video game programmer who founded
Llamasoft Ltd. He is known for his work on the Commodore 64 and other
platforms.
```

### **Fast Facts** (Required)
Bullet points with key dates, people, technical details.

**Format:** Short, scannable, chronological where possible.

```markdown
## Fast facts
- **Founded:** 1982 by Jeff Minter
- **First release:** *Gridrunner* on VIC-20
- **Peak period:** 1982-1987 (C64/Spectrum era)
- **Still active:** Light synthesizer performances, indie releases
```

### **Lesson Connections** (Required)
Which lessons reference this? How does it connect to what learners are building?

**Format:** Phase/Tier/Lesson references with brief explanation.

```markdown
## Lesson connections
- Phase 0, Tier 2, Lesson 18: Sprite positioning uses VIC-II registers
- Phase 0, Tier 4, Lesson 45: Sprite multiplexing explained
- Phase 3, Tier 1, Lesson 201: Assembly sprite routines

See [VIC-II](/vault/vic-ii) for complete register reference.
```

### **Technical Details** (For Hardware/Concepts)
Register tables, memory maps, specifications.

**This is where reference material lives** - not in lessons.

```markdown
## VIC-II Sprite Registers

| Address | Decimal | Purpose |
|---------|---------|---------|
| $D000 | 53248 | Sprite 0 X position |
| $D001 | 53249 | Sprite 0 Y position |
| $D015 | 53269 | Sprite enable |
...
```

### **Timeline** (For People/Companies/Events)
Key dates showing career/company progression or event sequence.

```markdown
## Timeline

**1982:** Founded Llamasoft from bedroom in Reading
**1982:** *Gridrunner* released for VIC-20 (£5.95 cassette)
**1983:** *Attack of the Mutant Camels* - first major hit
**1984-87:** Peak output - dozens of C64/Spectrum titles
**1994:** *Tempest 2000* on Atari Jaguar - critical acclaim
**2000s:** Light synthesizer development
**2023:** *Akka Arrh* released
```

### **Influence/Legacy** (Optional)
How this person/game/concept shaped what came after.

**Focus on:** Concrete connections, not vague claims.

```markdown
## Influence

Braybrook's sprite multiplexing technique became standard in C64 games
after *Uridium*. Programmers studying his work discovered you could
reposition sprites mid-screen during raster interrupts.

(Assembly lessons in Phase 3 teach this technique.)
```

### **See Also** (Required)
Cross-links to related Vault entries.

**Strategy:**
- People → their companies, games, contemporaries
- Games → programmers, publishers, hardware
- Hardware → designers, games that used it
- Concepts → pioneers, example games

```markdown
## See also
- [Andrew Braybrook](/vault/andrew-braybrook) - Programmer
- [Hewson Consultants](/vault/hewson-consultants) - Publisher
- [VIC-II](/vault/vic-ii) - Hardware used
- [Sprite Multiplexing](/vault/sprite-multiplexing) - Technique pioneered
- [Paradroid](/vault/paradroid) - Another Braybrook classic
```

---

## When to Create Vault Entries

### **During Lesson Authoring**

1. **Extract references** to vault-todo.md (as covered in LESSON-WORKFLOW.md)
2. **Don't stop to write full entries** - stay focused on lesson
3. **Note what needs documenting:**
   ```markdown
   ## Vault TODO from Lesson 23

   - [ ] *Impossible Mission* (1984, Dennis Caswell, Epyx)
   - [ ] Dennis Caswell (programmer)
   - [ ] Epyx (publisher)
   - [ ] Joystick input technique
   ```

### **Batch Creation Later**

After completing a tier or when you have 10+ references accumulated:

1. **Group by category** (games, people, companies, etc.)
2. **Research dates** (release years, birth/death dates, company founding)
3. **Write entries** in batches (easier to maintain consistent tone)
4. **Cross-link** as you go
5. **Update timeline** (see below)

### **Priority Order**

1. **Hardware** - Learners need register references immediately
2. **Concepts** - Techniques referenced across multiple lessons
3. **Games/People** - Historical context enriches but isn't blocking
4. **Companies/Publications** - Background context, lowest priority

---

## Timeline Construction

### **The Global Timeline View**

Eventually, create `/vault/timeline` showing all events chronologically:

```markdown
## 1982

**January:** Commodore 64 released in US ($595)
**September:** Commodore 64 released in UK (£399)
**October:** Jeff Minter founds Llamasoft
**November:** *Gridrunner* released (VIC-20)

## 1983

**March:** *Attack of the Mutant Camels* released
**May:** Zzap!64 magazine launches
**November:** Matthew Smith's *Jet Set Willy* released

## 1984

**February:** *Impossible Mission* released (Epyx)
**June:** Bob Yannes leaves Commodore
...
```

### **Temporal Data Requirements**

**Be as precise as possible:**
- **Year only:** If exact month unknown
- **Month/Year:** Most common (game releases, magazine issues)
- **Day/Month/Year:** For specific events if known

**Format:**
```yaml
release_date: "1986-03"  # March 1986
born: "1962"             # Year only
event_date: "1994-04-29" # Exact date (Commodore bankruptcy)
```

### **Birth/Death Dates for People**

**Include if publicly available:**
- Birth year (research Wikipedia, MobyGames, company sites)
- Death year if applicable
- Respect privacy for living people (year only, no day/month)

```yaml
born: "1962"
died: null  # Still alive, or unknown
```

**Tone for living people:**
```markdown
Jeff Minter (born 1962) still releases games and tours with light synth
performances.
```

**Tone for deceased:**
```markdown
Jack Tramiel (1928-2012) founded Commodore and drove the aggressive pricing
that made home computers affordable.
```

---

## Writing Tone Guidelines

### **Do:**
- Write like you're telling a story
- Use specific details (£399, September 1982)
- Show personality (Jeff Minter's llama obsession matters)
- Connect to modern context lightly
- Let the facts be interesting

### **Avoid:**
- Writing like Wikipedia
- Using passive voice excessively
- Burying dates in prose
- Over-explaining obvious things
- Forcing connections

### **Examples of Tone**

**Game entry:**
```markdown
*Uridium* arrived in 1986 and immediately raised questions: how was Andrew
Braybrook showing 20+ sprites when the VIC-II only had 8? The answer -
sprite multiplexing via raster interrupts - became a standard technique
after programmers studied his work.

(Assembly Phase 3 teaches this technique. BASIC is too slow for the
precise timing required.)
```

**Person entry:**
```markdown
Bob Yannes joined Commodore in 1981 with one mission: build a synthesizer
chip that didn't sound like a toy. The SID chip he designed became the
voice of a generation of games. He left Commodore in 1984, frustrated
that management didn't understand what they had.

He went on to co-found Ensoniq and design professional synthesizers.
```

**Event entry:**
```markdown
## Commodore Bankruptcy (April 29, 1994)

Commodore International filed for bankruptcy after years of mismanagement.
The company that made home computing affordable couldn't adapt to the PC era.

The brand spent the next three decades being passed between asset strippers,
each extracting value while contributing nothing. The Commodore 64 outlived
the company - user groups and demo scene kept it alive.
```

---

## Cross-Linking Strategy

### **Bidirectional Links**

Every link should work both ways:

- *Uridium* → Andrew Braybrook
- Andrew Braybrook → *Uridium*

- VIC-II → Bob Yannes (designer)
- Bob Yannes → VIC-II (designed this)

### **Link Types**

**People → Games:**
```markdown
## Notable works
- *Uridium* (1986)
- *Paradroid* (1985)
- *Morpheus* (1987)
```

**Games → People:**
```markdown
## Credits
**Programmer:** Andrew Braybrook
**Graphics:** Steve Turner
**Publisher:** Hewson Consultants
```

**Hardware → Games:**
```markdown
## Games that pushed the VIC-II
- *Uridium* - Sprite multiplexing
- *Mayhem in Monsterland* - Smooth scrolling
- *Last Ninja* - Isometric perspective
```

**Concepts → Examples:**
```markdown
## Notable implementations
- *Uridium* (1986) - First widespread use
- *Mayhem in Monsterland* (1993) - 24 sprites via multiplexing
- *Cybernoid* (1988) - Complex sprite patterns
```

---

## Workflow Summary

### **While Authoring Lessons:**
1. Mention games/people/techniques naturally where relevant
2. Extract references to `docs/vault-todo.md`
3. Continue with lesson (don't stop to write Vault entries)

### **Batch Vault Entry Creation:**
1. Accumulate 10-20 references in vault-todo.md
2. Research temporal data (dates, years, sequences)
3. Group by category
4. Write entries maintaining energetic tone
5. Cross-link bidirectionally
6. Update global timeline if exists

### **Long-term Vision:**
- Complete Vault coverage of referenced games/people/companies
- Global timeline view showing historical context
- Rich cross-linking creating knowledge graph
- Modern relevance mentioned lightly, not forced

---

## File Naming

Use slugified titles:

- `jeff-minter.mdx`
- `attack-of-the-mutant-camels.mdx`
- `vic-ii.mdx`
- `commodore-64.mdx`
- `sprite-multiplexing.mdx`

**Convention:** Lowercase, hyphens, no underscores.

---

## See Also

- [LESSON-WORKFLOW.md](LESSON-WORKFLOW.md) - How lessons extract Vault references
- [LESSON-ARCHETYPES.md](LESSON-ARCHETYPES.md) - When to link to Vault vs inline
- [README.md](../README.md) - Project philosophy

---

**Remember:** The Vault shows learners they're not just learning "old computer stuff" - they're learning techniques from REAL people who solved REAL problems in a specific moment in computing history. Make it come alive.
