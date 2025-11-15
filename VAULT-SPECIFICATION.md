# The Vault: Specification

## Overview

The Vault is a comprehensive reference encyclopedia providing historical, technical, and cultural context for everything referenced in the Code Like It's 198x curriculum. When a lesson mentions a person, game, technique, or cultural event, learners can follow links to Vault entries to explore deeper context, understand significance, and discover related concepts.

**Key Principles:**
- **Comprehensive where practical** - Provide thorough context, not just definitions
- **Heavily cross-linked** - Connect related entries throughout the Vault
- **Platform-agnostic** - One shared Vault across all platforms
- **Cultural context** - Link technical history with broader cultural/geopolitical events
- **Standalone utility** - Useful independently of curriculum, enhanced when used together

---

## Entry Types

### 1. People

**Purpose:** Document programmers, artists, musicians, designers, and other individuals who shaped retro gaming.

**Required Fields:**
- **Name:** Full name with common aliases/pseudonyms
- **Role(s):** Primary roles (Programmer, Musician, Artist, Designer, etc.)
- **Active Years:** Time period of main activity
- **Notable Works:** Key games/demos/music they created
- **Platforms:** Primary platforms they worked on
- **Biography:** Comprehensive background, career highlights, innovations, influence
- **Signature Techniques:** Distinctive approaches or innovations they pioneered
- **Cultural Impact:** How they influenced the industry/scene
- **Related Entries:** Links to Companies, Games, Techniques, other People

**Optional Fields:**
- Birthdate/location (if publicly known)
- Awards and recognition
- Post-retro era career
- Interviews/quotes
- External links (official sites, interviews)

**Example:**
```markdown
# Martin Galway

**Role:** Musician, Sound Designer
**Active Years:** 1983-1988
**Platforms:** Commodore 64, ZX Spectrum
**Notable Works:** Times of Lore, Parallax, Arkanoid, Comic Bakery

## Biography
Martin Galway revolutionized SID chip music composition in the mid-1980s...

## Signature Techniques
- Multi-speed music routines allowing complex arrangements
- Creative use of filter sweeps and envelope manipulation
- Integration of sound effects with music without channel conflicts

## Cultural Impact
Galway's work demonstrated that 8-bit computer music could be...

## Related Entries
- [SID Chip](/vault/hardware/sid-6581)
- [Comic Bakery](/vault/games/comic-bakery)
- [Imagine Software](/vault/companies/imagine-software)
```

---

### 2. Companies

**Purpose:** Document game studios, publishers, hardware manufacturers, and other organizations.

**Required Fields:**
- **Name:** Full company name with common abbreviations
- **Type:** Studio, Publisher, Hardware Manufacturer, etc.
- **Founded/Dissolved:** Date range of operation
- **Location:** Headquarters location(s)
- **Key People:** Founders, notable employees
- **Notable Products:** Major games/hardware/software
- **Platforms:** Primary platforms supported
- **History:** Formation, evolution, achievements, closure (if applicable)
- **Legacy:** Impact on industry and lasting influence
- **Related Entries:** Links to People, Games, Systems, other Companies

**Optional Fields:**
- Parent company/acquisitions
- Development philosophy
- Technical innovations
- Business model

**Example:**
```markdown
# Psygnosis

**Type:** Game Studio & Publisher
**Founded:** 1984
**Dissolved:** 2012 (absorbed into Sony)
**Location:** Liverpool, UK
**Key People:** Ian Hetherington, Jonathan Ellis

## History
Founded in Liverpool by Ian Hetherington and Jonathan Ellis, Psygnosis became known for...

## Notable Products
- Lemmings (1991)
- Shadow of the Beast series (1989-1992)
- Wipeout series (1995+)

## Technical Innovation
Psygnosis pushed hardware limits on Amiga, particularly with Shadow of the Beast's multi-layer parallax scrolling...

## Related Entries
- [Shadow of the Beast](/vault/games/shadow-of-the-beast)
- [Roger Dean](/vault/people/roger-dean) (Cover Artist)
- [Commodore Amiga](/vault/systems/commodore-amiga)
```

---

### 3. Games

**Purpose:** Document specific games referenced in lessons as examples, inspirations, or technical achievements.

**Required Fields:**
- **Title:** Full game title with regional variants
- **Developer:** Studio/individuals who created it
- **Publisher:** Company that published it
- **Release Date:** Year (and month if significant)
- **Platform(s):** Systems it was released on
- **Genre:** Primary genre classification
- **Overview:** What the game is and why it matters
- **Technical Achievements:** Notable programming/artistic techniques used
- **Cultural Impact:** Influence on gaming and broader culture
- **Curriculum Relevance:** Why this game is referenced in lessons
- **Related Entries:** Links to People, Companies, Techniques, other Games

**Optional Fields:**
- Developer team credits
- Sales figures/awards
- Ports and conversions
- Legacy (sequels, spiritual successors, remakes)
- Source material (for licensed games)

**Example:**
```markdown
# Mayhem in Monsterland

**Developer:** Apex Computer Productions (Rowlands Brothers)
**Publisher:** Apex Computer Productions
**Release Date:** 1993
**Platform:** Commodore 64
**Genre:** Platform Game

## Overview
Widely considered one of the most technically accomplished C64 games ever made, Mayhem in Monsterland pushed the aging hardware to its absolute limits...

## Technical Achievements
- Full-screen multi-directional scrolling at 50fps
- 50+ sprite multiplexing with minimal flicker
- Advanced raster effects (FLD, VSP)
- Sophisticated parallax backgrounds
- 4×4 char sprite system for huge animated characters

## Cultural Impact
Released in 1993 when the C64 was commercially dead, Mayhem proved that dedicated programmers could still extract previously impossible performance...

## Curriculum Relevance
Referenced in Phase 7-8 lessons as the gold standard for:
- Advanced sprite multiplexing (Lesson 7-01)
- Full-screen scrolling optimization (Lesson 7-02)
- Character-based sprite systems (Lesson 8-05)

## Related Entries
- [John and Steve Rowlands](/vault/people/rowlands-brothers)
- [Full Screen Scrolling](/vault/techniques/c64-full-screen-scrolling)
- [FLD (Flexible Line Distance)](/vault/techniques/c64-fld)
```

---

### 4. Techniques

**Purpose:** Document programming techniques, design patterns, algorithms, and optimization approaches.

**Required Fields:**
- **Name:** Common name for the technique
- **Platform(s):** Which systems use this technique (or "Universal" if applicable)
- **Category:** Rendering, Audio, Input, Optimization, etc.
- **Overview:** What the technique does and why it's used
- **How It Works:** Technical explanation of the approach
- **Variations:** Different implementations or related techniques
- **Trade-offs:** Performance, memory, complexity considerations
- **Historical Context:** When it emerged, who pioneered it
- **Curriculum Integration:** Which lessons teach/use this technique
- **Related Entries:** Links to Games, People, Pattern Library entries

**Optional Fields:**
- Code examples (link to Pattern Library for full implementations)
- Visual diagrams
- Difficulty level
- Prerequisites

**Example:**
```markdown
# Sprite Multiplexing (C64)

**Platform:** Commodore 64
**Category:** Rendering
**Difficulty:** Intermediate to Advanced

## Overview
The C64 hardware supports only 8 sprites, but sprite multiplexing allows displaying many more by reusing the same hardware sprites multiple times per frame via raster interrupts.

## How It Works
By triggering a raster interrupt when the screen beam passes the bottom of the first set of sprites, you can reposition and redefine those same 8 hardware sprites to appear further down the screen. With careful timing, 40-60+ sprites can be displayed.

## Variations
- **Simple Multiplexing:** Fixed sprite positions per zone
- **Sorted Multiplexing:** Dynamic Y-sorting for variable sprite counts
- **Zone-Based:** Screen divided into multiplexing zones
- **8-per-scanline Limit Handling:** Strategies when >8 sprites share Y coordinates

## Trade-offs
- **Performance:** Requires precise raster timing, consumes CPU cycles
- **Flickering:** Can occur when >8 sprites share scanlines
- **Complexity:** Significantly more complex than static sprites

## Historical Context
First extensively used in commercial games around 1985-1986. Games like *Parallax* and *Uridium* demonstrated sophisticated multiplexing that became standard by the late 1980s.

## Curriculum Integration
- **First Introduced:** Phase 2, Tier 1, Lesson 8
- **Intermediate:** Phase 3, Tier 2, Lessons 12-14
- **Advanced:** Phase 5, Tier 1, Lessons 18-20
- **Mastery:** Phase 7, Tier 2, Lesson 10

## Related Entries
- [VIC-II Chip](/vault/hardware/vic-ii)
- [Raster Interrupts](/vault/techniques/c64-raster-interrupts)
- [Sprite Multiplexing Pattern](/patterns/c64/rendering/sprite-multiplexing)
- [Mayhem in Monsterland](/vault/games/mayhem-in-monsterland)
```

---

### 5. Hardware Components

**Purpose:** Document chips, subsystems, and hardware components that programmers interact with.

**Required Fields:**
- **Name:** Component name with part number
- **Type:** CPU, Graphics Chip, Sound Chip, I/O, etc.
- **Used In:** Which systems featured this component
- **Manufacturer:** Who produced it
- **Specifications:** Key technical specs (clock speed, memory, channels, etc.)
- **Capabilities:** What it can do
- **Programming Model:** How software interacts with it
- **Limitations:** Notable constraints programmers had to work around
- **Historical Context:** When introduced, why it was significant
- **Related Entries:** Links to Systems, Techniques, People, Games

**Optional Fields:**
- Die photos/block diagrams
- Register maps (link to full documentation)
- Cost/availability
- Variants and revisions

**Example:**
```markdown
# SID 6581 (Sound Interface Device)

**Type:** Sound Synthesis Chip
**Manufacturer:** MOS Technology
**Used In:** Commodore 64, Commodore 128
**Release Date:** 1982

## Specifications
- **Voices:** 3 independent channels
- **Waveforms:** Sawtooth, Triangle, Pulse (variable width), Noise
- **Filter:** Multi-mode resonant filter (low-pass, high-pass, band-pass)
- **ADSR:** Independent Attack/Decay/Sustain/Release envelopes per voice
- **Frequency Range:** ~16 Hz to 4 kHz
- **Output:** Analog audio output

## Capabilities
The SID was revolutionary for home computers, offering:
- Programmable waveforms with multiple modes
- Ring modulation between voices for metallic sounds
- Hard sync for complex timbres
- Resonant filter allowing subtractive synthesis

## Programming Model
Programmed via 29 memory-mapped registers at $D400-$D41C:
- Frequency control (16-bit per voice)
- Waveform selection
- Envelope parameters
- Filter cutoff and resonance

## Limitations
- Only 3 voices (limiting polyphony)
- Filter could distort at high resonance
- Some registers write-only, making state management tricky
- Temperature-dependent filter characteristics

## Historical Context
Designed by Bob Yannes (who later founded Ensoniq), the SID elevated computer music from beeps to actual synthesis. Martin Galway, Rob Hubbard, and others demonstrated its musical potential.

## Techniques Enabled
- Multi-speed music routines
- Arpeggio simulation for chords
- Sample playback via pulse-width modulation
- Drum synthesis using noise channel

## Related Entries
- [Bob Yannes](/vault/people/bob-yannes)
- [Martin Galway](/vault/people/martin-galway)
- [SID Music Composition](/vault/techniques/c64-sid-music)
- [Commodore 64](/vault/systems/commodore-64)
```

---

### 6. Systems / Platforms

**Purpose:** Document computer systems and game consoles covered in the curriculum.

**Required Fields:**
- **Name:** Full system name with model variants
- **Manufacturer:** Company that produced it
- **Type:** Home Computer, Game Console, etc.
- **Release Date:** Launch date(s) by region
- **Discontinued:** End of production
- **CPU:** Processor used
- **Memory:** RAM, ROM, video memory
- **Graphics:** Display capabilities and chips
- **Sound:** Audio capabilities and chips
- **Storage:** Media types (cartridge, tape, disk)
- **Historical Context:** Market position, cultural impact
- **Library Highlights:** Notable games and software
- **Programming Environment:** Languages, tools, development process
- **Related Entries:** Links to Hardware Components, Companies, People, Games

**Optional Fields:**
- Sales figures
- Regional variants
- Peripherals
- Technical innovations
- Demoscene activity

**Example:**
```markdown
# Commodore 64

**Manufacturer:** Commodore International
**Type:** Home Computer
**Release Date:** August 1982
**Discontinued:** April 1994
**Units Sold:** ~12.5-17 million (best-selling single computer model)

## Specifications
- **CPU:** MOS 6510 @ 1.023 MHz (NTSC), 0.985 MHz (PAL)
- **RAM:** 64 KB
- **Graphics:** VIC-II chip, 320×200 / 160×200, 16 colors, 8 hardware sprites
- **Sound:** SID 6581/8580, 3 voices with synthesis capabilities
- **Storage:** Cassette tape, 5.25" floppy disk (1541 drive)
- **Ports:** Cartridge, 2× joystick, serial, user port

## Historical Context
The C64 dominated home computing through the 1980s, particularly strong in Europe and North America. Its combination of capable graphics, revolutionary sound chip, and affordability ($595 at launch, later $199) made it the platform for a generation of gamers and bedroom coders...

## Library Highlights
- Hundreds of commercial games across all genres
- Vibrant demoscene pushing hardware to extremes
- Educational software and productivity tools

## Programming Environment
- **BASIC:** Built-in Commodore BASIC V2 (limited graphics commands)
- **Assembly:** 6510 assembly for serious games and demos
- **Tools:** Cross-assemblers, sprite editors, music trackers
- **Development:** Hobbyist bedroom coding to small studio teams

## Cultural Impact
The C64 created a generation of programmers who learned by necessity (slow BASIC forced learning assembly). The demoscene, crack intros, and magazine type-in listings created a unique programming culture...

## Related Entries
- [VIC-II](/vault/hardware/vic-ii)
- [SID 6581](/vault/hardware/sid-6581)
- [6510 CPU](/vault/hardware/6510-cpu)
- [Commodore International](/vault/companies/commodore-international)
```

---

### 7. Events

**Purpose:** Document significant events - both computer/gaming industry events AND broader geopolitical/cultural events that provide historical context.

**Required Fields:**
- **Name:** Event name
- **Date:** When it occurred (day/month/year as appropriate)
- **Type:** Industry (conference, release, announcement) or Cultural/Geopolitical
- **Overview:** What happened and why it matters
- **Impact:** Significance for gaming industry or cultural context
- **Related Entries:** Links to Companies, People, Games, Systems, other Events

**Optional Fields:**
- Location
- Key participants
- Media coverage
- Long-term consequences

**Computer/Gaming Event Example:**
```markdown
# Crash of 1983 (Video Game Crash)

**Date:** 1983-1984
**Type:** Industry Crisis
**Location:** Primarily North America

## Overview
The video game crash of 1983 saw the North American console market collapse, with industry revenues dropping from $3.2 billion in 1983 to $100 million in 1985. Thousands of arcades and video game companies went bankrupt.

## Causes
- Market saturation with low-quality games
- Lack of quality control (particularly Atari 2600)
- Consumer confusion from too many incompatible systems
- Competition from home computers
- E.T. and Pac-Man disasters

## Impact on Retro Gaming Era
- Shifted gaming dominance to Europe (C64, ZX Spectrum thrived)
- Created opportunity for Nintendo's carefully controlled NES launch (1985)
- Established importance of quality control and first-party standards
- Europe's bedroom coder culture flourished while US industry struggled

## Recovery
Nintendo Entertainment System (1985 US launch) revitalized the console market with:
- Strict licensing and quality control
- "Entertainment System" rebranding (avoiding "video game")
- Pack-in titles demonstrating quality

## Related Entries
- [Atari 2600](/vault/systems/atari-2600)
- [Nintendo Entertainment System](/vault/systems/nes)
- [European Home Computer Market](/vault/events/european-home-computer-boom)
```

**Cultural/Geopolitical Event Example:**
```markdown
# Fall of the Berlin Wall

**Date:** 9 November 1989
**Type:** Geopolitical / Cultural
**Location:** Berlin, Germany

## Overview
The Berlin Wall, separating East and West Berlin since 1961, was opened on 9 November 1989, leading to German reunification and symbolizing the end of the Cold War.

## Cultural Context for Gaming
This event marks a pivotal moment in the era when many classic games were being developed:

**Contemporary Releases (1989):**
- *Prince of Persia* (US)
- *Shadow of the Beast* (Amiga)
- *Populous* (Amiga, PC)
- *SimCity* (PC)

## Impact on European Gaming Industry
- Reunified Germany became a significant gaming market
- Eastern European developers gained access to Western platforms
- Cultural exchange influenced game themes and settings

## Related Entries
- [1989 Gaming Timeline](/vault/events/1989-gaming)
- [European Game Development](/vault/culture/european-dev-scene)
- [Cold War in Games](/vault/culture/cold-war-themes)
```

---

### 8. Movies

**Purpose:** Document films referenced in lessons, particularly for movie tie-in games, cultural context, and visual inspiration.

**Required Fields:**
- **Title:** Film title with year
- **Release Date:** Theatrical release
- **Director:** Primary director(s)
- **Studio:** Production company
- **Overview:** Brief synopsis and cultural significance
- **Related Games:** Video game adaptations or inspired titles
- **Cultural Impact:** Why this film matters for the era
- **Related Entries:** Links to Games, Events, Music

**Optional Fields:**
- Box office performance
- Awards
- Franchise information
- Visual style influence on games

**Example:**
```markdown
# Aliens (1986)

**Director:** James Cameron
**Studio:** 20th Century Fox
**Release Date:** 18 July 1986
**Genre:** Science Fiction / Action

## Overview
Sequel to *Alien* (1979), this film shifted from horror to action, following Ellen Ripley's return to the alien planet with Colonial Marines...

## Cultural Impact
*Aliens* defined the sci-fi action aesthetic of the late 1980s with its industrial military look, motion tracker beeps, and "game over man!" attitude that permeated gaming culture.

## Related Games
- *Aliens* (1986, multiple platforms)
- *Aliens: The Computer Game* (1986, C64, ZX Spectrum, Amstrad)
- *Alien Breed* series (1991+, Amiga) - spiritual successor

## Visual Influence on Games
The film's aesthetic heavily influenced:
- Corridor shooters (claustrophobic spaces, motion trackers)
- Run 'n' gun games (marines vs aliens theme)
- HUD design (iconic motion tracker interface)

## Related Entries
- [Alien Breed](/vault/games/alien-breed)
- [Team17](/vault/companies/team17)
- [Run 'n' Gun Genre](/vault/genres/run-n-gun)
```

---

### 9. Music

**Purpose:** Document albums, artists, and tracks that provide cultural context for the era or directly influenced game soundtracks.

**Required Fields:**
- **Title:** Album or track name
- **Artist:** Performer(s)
- **Release Date:** When released
- **Overview:** Musical style and significance
- **Cultural Context:** Why this matters for the gaming era
- **Related Entries:** Links to Events, Games, People

**Optional Fields:**
- Chart performance
- Genre classification
- Technical notes (synthesis, production techniques)
- Game soundtrack influences

**Example:**
```markdown
# Oxygène (Jean-Michel Jarre, 1976)

**Artist:** Jean-Michel Jarre
**Release Date:** December 1976
**Genre:** Electronic, Ambient, Synth

## Overview
Pioneering electronic music album that demonstrated the musical possibilities of synthesizers and sequencers to a mainstream audience.

## Cultural Context for Gaming
*Oxygène* arrived just as microcomputers emerged, proving that electronic instruments could create emotionally resonant music. This mindset influenced how early computer musicians approached limited sound chips.

## Influence on Game Music
- Demonstrated that synthesized music could be atmospheric, not just "computer beeps"
- Inspired C64 SID musicians like Martin Galway and Rob Hubbard
- Established sequencer-based composition approach used in tracker software

## Technical Parallels
Jarre's use of analog sequencers parallels game music tracker composition:
- Pattern-based sequencing
- Limited polyphony forcing creative arrangement
- Sound design as composition tool

## Related Entries
- [Martin Galway](/vault/people/martin-galway)
- [SID Chip](/vault/hardware/sid-6581)
- [Tracker Music](/vault/techniques/tracker-composition)
```

---

### 10. Publications

**Purpose:** Document magazines, books, and other publications that shaped retro gaming culture and education.

**Required Fields:**
- **Title:** Publication name
- **Publisher:** Company/organization
- **Publication Period:** When it was published (start-end dates)
- **Type:** Magazine, Book, Manual, Fanzine
- **Overview:** Content focus and significance
- **Cultural Impact:** Influence on developers and players
- **Related Entries:** Links to People, Companies, Games

**Optional Fields:**
- Notable contributors
- Circulation figures
- Key columns/features
- Archive availability

**Example:**
```markdown
# Zzap!64

**Publisher:** Newsfield Publications (later Europress)
**Publication Period:** May 1985 - June 1992
**Type:** Magazine
**Focus:** Commodore 64 gaming

## Overview
Britain's premier C64 gaming magazine, *Zzap!64* combined comprehensive reviews, technical articles, and irreverent humor. Known for its "Sizzler" ratings and personality-driven criticism.

## Cultural Impact
- Made or broke C64 games with influential reviews
- Type-in program listings taught programming to thousands
- Detailed technical articles explained advanced techniques
- Fostered community through reader letters and competitions

## Notable Contributors
- Gary Penn (reviewer, later game designer)
- Julian "Jaz" Rignall (reviewer, later game designer)
- Gary Liddon (technical editor, assembly tutorials)

## Legacy
*Zzap!64* created a model for enthusiast gaming journalism that valued both entertainment and technical depth. Many readers became industry professionals.

## Related Entries
- [Newsfield Publications](/vault/companies/newsfield)
- [Gary Penn](/vault/people/gary-penn)
- [Type-in Programs](/vault/culture/type-in-programs)
```

---

### 11. Demos

**Purpose:** Document significant demos from the demoscene that showcased technical excellence or influenced game development.

**Required Fields:**
- **Title:** Demo name
- **Group:** Demo group that created it
- **Platform:** System it ran on
- **Release Date:** When released (event if applicable)
- **Overview:** What the demo does and why it's notable
- **Technical Achievements:** Specific techniques or effects demonstrated
- **Influence:** Impact on game development or demoscene
- **Related Entries:** Links to People, Techniques, Systems

**Optional Fields:**
- Competition results
- File size
- Download/watch links
- Source code availability

**Example:**
```markdown
# Edge of Disgrace (Booze Design, 2008)

**Group:** Booze Design
**Platform:** Commodore 64
**Release Date:** August 2008 (X'2008 Demo Party)
**Competition:** 1st Place, Demo Competition

## Overview
"Edge of Disgrace" demonstrated previously impossible feats on C64 hardware, including full-screen video playback at 50fps, pushing the 26-year-old platform far beyond its supposed limits.

## Technical Achievements
- Full-screen FLI (Flexible Line Interpretation) video
- Advanced sprite multiplexing (100+ sprites)
- Custom raster routines achieving near-50fps video
- Synchronized high-quality music

## Techniques
- FLD (Flexible Line Distance)
- VSP (Variable Screen Position)
- Advanced raster timing
- Optimized playback routines

## Influence on Game Development
While created in 2008, this demo proved techniques relevant to Phase 7-8 curriculum goals. Shows what's ultimately possible when combining all advanced techniques.

## Related Entries
- [FLD Technique](/vault/techniques/c64-fld)
- [VSP Technique](/vault/techniques/c64-vsp)
- [Booze Design](/vault/groups/booze-design)
- [Demoscene](/vault/culture/demoscene)
```

---

## Cross-Linking Strategy

**Every entry should link to related entries in multiple categories:**

- **People** → Companies they worked for, Games they created, Techniques they pioneered
- **Games** → Developer People, Publisher Companies, Techniques used, Systems released on
- **Techniques** → People who pioneered them, Games that exemplify them, Hardware they exploit
- **Hardware** → Systems using it, Techniques exploiting it, People who designed it
- **Events** → Contemporary Games/Movies/Music, People involved, Companies affected
- **Movies/Music** → Related Games, Cultural Events, Era context

**Cross-link format:**
- Use consistent linking: `[Link Text](/vault/category/entry-slug)`
- Categories: `people`, `companies`, `games`, `techniques`, `hardware`, `systems`, `events`, `movies`, `music`, `publications`, `demos`

---

## Writing Style and Tone

**Voice:**
- **Informative but engaging** - Encyclopedia-style with personality
- **British English** - Programme, colour, organised (but "program" for computer programs)
- **Respectful but honest** - Credit achievements, acknowledge limitations
- **Historical context** - Explain why things mattered at the time
- **Avoid nostalgia tourism** - Focus on what's interesting/useful, not just "remember this?"

**Structure:**
- Start with essential facts (quick reference)
- Expand with context and detail
- Include technical specifics where relevant
- Always explain significance ("Why does this matter?")
- End with related entries for further exploration

**Accuracy:**
- Verify dates, specifications, credits
- Cite sources where possible
- Note uncertainty when information conflicts
- Distinguish between documented facts and community knowledge

---

## Organization and Navigation

**File Structure:**
```
/vault/
  /people/
    martin-galway.md
    bob-yannes.md
  /companies/
    psygnosis.md
    imagine-software.md
  /games/
    mayhem-in-monsterland.md
    shadow-of-the-beast.md
  /techniques/
    c64-sprite-multiplexing.md
    amiga-copper-effects.md
  /hardware/
    sid-6581.md
    vic-ii.md
  /systems/
    commodore-64.md
    sinclair-zx-spectrum.md
  /events/
    crash-of-1983.md
    fall-of-berlin-wall.md
  /movies/
    aliens-1986.md
    robocop-1987.md
  /music/
    oxygene-jean-michel-jarre.md
  /publications/
    zzap64.md
  /demos/
    edge-of-disgrace.md
```

**URL Structure:**
- `/vault/people/martin-galway`
- `/vault/games/mayhem-in-monsterland`
- `/vault/techniques/c64-sprite-multiplexing`

---

## Frontmatter Metadata

Every Vault entry should include structured frontmatter for filtering, searching, and relationships:

```yaml
---
title: "Martin Galway"
type: "person"
role: ["Musician", "Sound Designer"]
platforms: ["Commodore 64", "ZX Spectrum"]
active_years: "1983-1988"
related_companies: ["Ocean Software", "Imagine Software"]
related_games: ["Comic Bakery", "Times of Lore", "Parallax"]
related_techniques: ["SID Music Composition", "Multi-speed Music"]
tags: ["sid-music", "c64-audio", "1980s"]
---
```

---

## Integration with Curriculum

**Lesson Linking:**
- Lessons include inline Vault links when mentioning people, games, techniques, etc.
- Links appear naturally in text: "...similar to Martin Galway's approach in *Comic Bakery*..."
- Links open Vault entries in new context (sidebar, modal, or new page)

**Vault-to-Lesson Reverse Links:**
- Vault entries include "Curriculum Integration" sections
- List which lessons reference or teach related concepts
- Example: "This technique is first introduced in Phase 3, Tier 2, Lesson 8"

**Pattern Library Integration:**
- Technique entries link to Pattern Library implementations
- Pattern Library entries link back to Vault for context
- Example: Vault's "Sprite Multiplexing" links to Pattern's "C64 Sprite Multiplexing Routine"

---

## Content Priorities

**Phase 1 Vault Needs (Immediate):**
- Core hardware components (SID, VIC-II, PPU, etc.)
- Fundamental techniques (sprites, scrolling, collision)
- Essential systems (C64, ZX Spectrum, Amiga, NES)
- Key companies (Commodore, Nintendo, Sinclair)

**Phase 2-4 Expansion:**
- Notable developers and musicians
- Classic games frequently referenced
- Intermediate techniques
- Cultural events of early-to-mid 1980s

**Phase 5-8 Completion:**
- Advanced techniques and optimizations
- Late-era developers and games
- Demoscene and technical showcases
- Cultural context through 1980s-early 1990s

---

## Quality Standards

**Before Publishing a Vault Entry:**
- [ ] All required fields completed
- [ ] At least 3 cross-links to related entries
- [ ] Technical accuracy verified (specs, dates, credits)
- [ ] British English spelling (except "program")
- [ ] No marketing speak or excessive hype
- [ ] Clear explanation of significance ("why it matters")
- [ ] Proper frontmatter metadata

---

## Future Enhancements

**Potential Additions:**
- **Interactive Elements:** Embedded playable games, audio players for SID music
- **Visual Media:** Screenshots, photos, diagrams, videos
- **Community Contributions:** Verified community additions with editorial review
- **Timelines:** Interactive timeline views of events, releases, technical evolution
- **Search/Filter:** Advanced search across all entry types, tag-based filtering

---

*The Vault provides the historical and technical context that transforms lessons from "how to code" into "how developers actually worked" - connecting learners to the real people, real constraints, and real innovations that defined the era.*
