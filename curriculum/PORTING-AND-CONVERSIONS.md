# Porting & Conversions: The Art of Translation

**Purpose:** Document how games were adapted between platforms - the challenges, techniques, successes, and disasters.

**Last Updated:** 2026-01-18

---

## Why Porting Matters

Porting was fundamental to the industry:
1. **Business necessity** - Maximise revenue from one design
2. **Technical challenge** - Different hardware, same experience
3. **Learning opportunity** - Understand what makes games work
4. **Historical record** - Same game, different interpretations

Understanding ports means understanding platform differences deeply.

---

## Part 1: The Porting Challenge

### What Made Porting Hard

| Challenge | Examples |
|-----------|----------|
| **CPU architecture** | 6502 vs Z80 vs 68000 |
| **Memory** | 48KB Spectrum vs 64KB C64 vs 512KB Amiga |
| **Graphics** | Attribute clash vs sprites vs bitplanes |
| **Sound** | Beeper vs SID vs Paula |
| **Controls** | Joystick buttons, keyboard layouts |
| **Storage** | Tape vs disk vs cartridge |
| **Screen resolution** | 256×192 vs 320×200 vs 256×240 |

### The Spectrum Problem

The Spectrum's attribute system made arcade ports particularly difficult:

| Arcade Feature | Spectrum Challenge |
|----------------|-------------------|
| **Colourful sprites** | 2 colours per 8×8 cell |
| **Smooth scrolling** | No hardware support |
| **Many enemies** | Colour clash chaos |
| **Detailed backgrounds** | Attributes limit detail |

**Solutions:**
- Monochrome graphics (avoid clash entirely)
- Careful colour placement
- Smaller play areas
- Different visual style

### The C64 Advantage (and Limits)

| Strength | Limitation |
|----------|------------|
| Hardware sprites | Only 8 sprites |
| Smooth scrolling | Slower CPU than Spectrum |
| SID audio | Memory same as Spectrum |
| Colour per character | Less flexible than bitplanes |

### The NES Constraint

| Feature | Limit |
|---------|-------|
| Sprites | 64 total, 8 per scanline |
| Colours | 25 on screen (with tricks) |
| Scrolling | Excellent hardware support |
| Audio | 5 channels, distinctive |

---

## Part 2: Legendary Good Ports

### Arcade to Home Excellence

| Game | Original | Port | Why It Worked |
|------|----------|------|---------------|
| **R-Type** | Arcade | PC Engine | Near-perfect, HuCard magic |
| **Galaga** | Arcade | NES | Excellent adaptation |
| **Street Fighter II** | Arcade | SNES | "Arcade perfect" marketing |
| **Bubble Bobble** | Arcade | Multiple | Faithful across platforms |
| **Rainbow Islands** | Arcade | Multiple | Ocean's excellent work |
| **Turrican** | Amiga | C64 | Manfred Trenz miracle |

### Cross-Platform Excellence

| Game | Platforms | Notes |
|------|-----------|-------|
| **Elite** | BBC → Everything | Braben/Bell adapted to each |
| **Lemmings** | Amiga → Everything | DMA's careful ports |
| **Prince of Persia** | Apple II → Everything | Mechner supervised |
| **Flashback** | Amiga → Everything | Delphine's care |
| **Another World** | Amiga → Everything | Chahi's vision preserved |

### The Turrican C64 Miracle

| Aspect | Achievement |
|--------|-------------|
| **Original** | Amiga (1990) |
| **C64 port** | Same year, same developer |
| **Challenge** | 512KB Amiga → 64KB C64 |
| **Result** | Arguably better than original |
| **How** | Manfred Trenz rewrote from scratch |

Trenz didn't "port" - he reimagined for C64's strengths.

### Elite: The Universal Game

| Platform | Year | Notes |
|----------|------|-------|
| **BBC Micro** | 1984 | Original |
| **Acorn Electron** | 1984 | Reduced but playable |
| **C64** | 1985 | Excellent adaptation |
| **ZX Spectrum** | 1985 | Monochrome but complete |
| **Amstrad CPC** | 1985 | Good conversion |
| **NES** | 1991 | Late but solid |
| **Amiga** | 1991 | Enhanced |

**Why Elite ported well:** Core gameplay was mathematical (vectors, trading), not dependent on specific hardware features.

**Vault entries:**
- `elite-ports` - Culture entry
- `turrican-c64` - Game entry
- `cross-platform-development` - Technique entry

---

## Part 3: Notorious Bad Ports

### The Pac-Man 2600 Disaster

| Aspect | Details |
|--------|---------|
| **Original** | Arcade (1980) |
| **Port** | Atari 2600 (1982) |
| **Developer** | Tod Frye (solo, 5 weeks) |
| **Problems** | Flickering ghosts, wrong maze, poor graphics |
| **Impact** | 7 million sold, millions returned |
| **Legacy** | Contributed to 1983 crash |

**Why it failed:**
- Impossible deadline
- Single developer
- 2600 couldn't handle 5 moving objects
- No time for iteration

### OutRun Spectrum

| Aspect | Details |
|--------|---------|
| **Original** | Arcade (1986), scaling sprites, 60fps |
| **Port** | Spectrum (1987) |
| **Problems** | Jerky scrolling, tiny view, unplayable speed |
| **Lesson** | Some games don't translate |

The Spectrum simply couldn't do sprite scaling - the core mechanic.

### Street Fighter II on 8-bit

| Platform | Quality | Notes |
|----------|---------|-------|
| **C64** | Poor | US Gold, barely playable |
| **Spectrum** | Poor | Missing frames, slow |
| **Master System** | Acceptable | 8-bit but designed for it |
| **Game Boy** | Acceptable | Designed for limitations |

**Lesson:** Fighting games need responsive controls and smooth animation.

### Double Dragon on Various

| Platform | Quality | Developer |
|----------|---------|-----------|
| **Arcade** | Original | Technos |
| **NES** | Different | Single-screen, no co-op |
| **Master System** | Poor | Flickery, slow |
| **Spectrum** | Poor | Attribute clash chaos |
| **C64** | Mediocre | Better than Spectrum |
| **Amiga** | Mediocre | Should have been better |

**The NES version** was actually a different game - and arguably better for the platform.

### R-Type on Spectrum/C64

| Platform | Approach | Result |
|----------|----------|--------|
| **Spectrum** | Split into 2 loads | Monochrome, actually decent |
| **C64** | Split into 2 loads | More colourful, good |
| **Problem** | Each was only half a game |

**Lesson:** Sometimes honesty about limitations works better than pretending.

**Vault entries:**
- `pac-man-2600` - Game entry (cautionary tale)
- `bad-ports` - Culture entry
- `outrun-spectrum` - Game entry

---

## Part 4: Porting Houses

### US Gold

| Aspect | Notes |
|--------|-------|
| **Role** | UK publisher, licensed arcade games |
| **Method** | Farmed out to various developers |
| **Quality** | Highly variable |
| **Notable** | Street Fighter II ports, various arcade |

US Gold's ports ranged from excellent to terrible depending on developer.

### Ocean Software

| Aspect | Notes |
|--------|-------|
| **Role** | UK publisher and developer |
| **Method** | In-house and contracted |
| **Quality** | Generally better than US Gold |
| **Notable** | Rainbow Islands, various licenses |

Ocean put more care into platform-specific versions.

### Tiertex

| Aspect | Notes |
|--------|-------|
| **Role** | UK developer, US Gold contractor |
| **Reputation** | Consistently poor quality |
| **Notable** | Strider (home versions), various |

Tiertex became synonymous with rushed, poor ports.

### Elite Systems

| Aspect | Notes |
|--------|-------|
| **Role** | UK publisher |
| **Notable ports** | Paperboy, Ghosts 'n Goblins |
| **Quality** | Variable |

### Probe Software

| Aspect | Notes |
|--------|-------|
| **Role** | UK developer |
| **Quality** | Generally competent |
| **Notable** | Various 16-bit ports |

**Vault entries:**
- `us-gold` - Company entry
- `tiertex` - Company entry
- `probe-software` - Company entry

---

## Part 5: Porting Techniques

### Graphics Adaptation

| Technique | When Used |
|-----------|-----------|
| **Monochrome** | Avoid colour clash (Spectrum) |
| **Smaller sprites** | Fit memory/sprite limits |
| **Reduced animation** | Save memory |
| **Different art style** | Play to platform strengths |
| **Background simplification** | Reduce memory/drawing time |

### Audio Adaptation

| Source | Target | Approach |
|--------|--------|----------|
| **FM synthesis** | SID | Recompose for SID strengths |
| **FM synthesis** | AY-3-8910 | Simplified arrangements |
| **Samples** | Chip | Convert to synthesis |
| **Beeper** | Skip | Sometimes better silent |

### Gameplay Adaptation

| Change | Reason |
|--------|--------|
| **Fewer enemies** | Sprite limits |
| **Smaller levels** | Memory limits |
| **Simplified patterns** | CPU limits |
| **Different level order** | Fit available memory |
| **Removed features** | Time/capability limits |

### "Speccy Port" Problem

When C64 versions were ported FROM Spectrum:
- Didn't use hardware sprites
- No smooth scrolling
- Wasted C64's capabilities

**Examples:** Many UK-developed multiformat games.

**The reverse:** C64-first games ported to Spectrum often had unusable colour clash.

**Vault entries:**
- `speccy-port` - Culture entry (derogatory term)
- `platform-specific-development` - Technique entry

---

## Part 6: Same Game, Different Versions

### Aladdin (1993)

| Platform | Developer | Style |
|----------|-----------|-------|
| **Genesis** | Virgin | Animation by Disney, fluid |
| **SNES** | Capcom | Tighter platforming |
| **Game Boy** | Virgin | Simplified |
| **Master System** | Sega | Different entirely |

**Both 16-bit versions are excellent** - different interpretations of same source.

### Prince of Persia

| Platform | Notes |
|----------|-------|
| **Apple II** | Original (Mechner) |
| **DOS** | Enhanced graphics |
| **SNES** | New levels, graphical upgrade |
| **Mega CD** | Full voice acting |
| **Game Boy** | Impressive portable |
| **Master System** | Domark, decent |

### Lemmings

| Platform | Quality | Notes |
|----------|---------|-------|
| **Amiga** | Original | DMA Design |
| **DOS** | Excellent | Near-identical |
| **SNES** | Excellent | Sunsoft |
| **Mega Drive** | Excellent | |
| **NES** | Simplified | Fewer lemmings |
| **Game Boy** | Impressive | Tiny but works |
| **Spectrum** | Remarkable | Shouldn't work, does |
| **C64** | Remarkable | Same |

**DMA Design** took pride in platform-appropriate versions.

### Flashback

| Platform | Notes |
|----------|-------|
| **Amiga** | Original |
| **DOS** | CD version with voice |
| **SNES** | Excellent port |
| **Mega Drive** | Excellent port |
| **CD-i** | Actually good |
| **3DO** | Enhanced |

Delphine maintained quality across platforms.

**Vault entries:**
- `aladdin-versions` - Culture entry
- `lemmings-ports` - Culture entry
- `multi-platform-releases` - Culture entry

---

## Part 7: The "Enhanced Port"

### When Ports Exceeded Originals

| Game | Original | Enhanced Port |
|------|----------|---------------|
| **Turrican** | Amiga | C64 (different but equal) |
| **Speedball 2** | Amiga | Mega Drive (better audio) |
| **Sensible Soccer** | Amiga | Mega Drive (more teams) |
| **Syndicate** | Amiga | DOS (SVGA) |
| **Wing Commander** | DOS | SNES (different but excellent) |

### SNES/Genesis Enhancements

16-bit consoles often received enhanced versions:
- More colours
- Better sound (sometimes)
- Additional content
- Mode 7 effects (SNES)

### CD-ROM Enhancements

CD versions often added:
- Voice acting
- Full motion video
- CD audio soundtrack
- Additional content

**Examples:** Monkey Island CD, Beneath a Steel Sky CD

---

## Part 8: Regional Differences

### Japan vs West

| Game | Japanese | Western |
|------|----------|---------|
| **Contra** | Japanese version | Renamed, sometimes censored |
| **Castlevania** | Akumajō Dracula | Different box art |
| **Final Fantasy** | Numbering | Different numbering in West |
| **Mega Man** | Rockman | Different character design |

### PAL vs NTSC

| Aspect | Impact |
|--------|--------|
| **Speed** | PAL games often 17% slower |
| **Resolution** | PAL has more lines (borders) |
| **Music** | Often wrong pitch in PAL |
| **Optimisation** | Some PAL versions properly adjusted |

**Properly optimised PAL:** Rare, required extra work.

**Vault entries:**
- `pal-vs-ntsc` - Culture entry
- `regional-differences` - Culture entry

---

## Part 9: Demakes

### Modern Games on Old Hardware

| Game | Original | Demake Platform |
|------|----------|-----------------|
| **Portal** | PC | Atari 2600, C64 |
| **Doom** | PC | Every platform imaginable |
| **Flappy Bird** | Mobile | Every retro platform |
| **Undertale** | PC | NES-style, but actual NES |

### Historical Demakes

| Game | Original | Demake |
|------|----------|--------|
| **Donkey Kong** | Arcade | Atari 2600 (Coleco sabotage?) |
| **Space Invaders** | Arcade | Atari 2600 (sold consoles) |
| **Pac-Man** | Arcade | Various (varying quality) |

### The Demake Scene

Modern hobbyists create demakes as:
- Technical challenges
- Nostalgia projects
- Learning exercises
- Scene competition entries

**Vault entries:**
- `demakes` - Culture entry
- `homebrew-ports` - Culture entry

---

## Part 10: Key People in Porting

| Person | Known For |
|--------|-----------|
| **Manfred Trenz** | Turrican C64 (not a port, a miracle) |
| **Jon Ritman** | Batman, Head Over Heels (Spectrum originals) |
| **David Braben** | Elite across platforms |
| **Eric Chahi** | Another World supervision |
| **Jordan Mechner** | Prince of Persia supervision |

### Anonymous Heroes

Many porters were uncredited:
- Contracted developers
- Work-for-hire arrangements
- Publisher-owned code
- Lost to history

---

## Part 11: Lessons for Curriculum

### What Porting Teaches

| Lesson | Application |
|--------|-------------|
| **Platform strengths** | Use hardware features appropriately |
| **Core gameplay** | What makes a game work isn't graphics |
| **Adaptation** | Same idea, different implementation |
| **Constraints** | Limitations force creativity |
| **Trade-offs** | Can't have everything |

### Curriculum Connection

Our multi-platform approach teaches porting mindset:
- Same concepts, different implementations
- C64 sprites vs Spectrum software sprites
- NES constraints vs Amiga freedom
- Understanding what transfers and what doesn't

---

## Summary: New Vault Entries

| Category | Entries |
|----------|---------|
| **Companies** | US Gold, Tiertex, Probe, Elite Systems | 5 |
| **Games** | Pac-Man 2600, Turrican C64, various ports | 15 |
| **People** | Porters and supervisors | 5 |
| **Techniques** | Porting methods, adaptation | 6 |
| **Culture** | Speccy port, PAL/NTSC, regional differences | 8 |

**Total new entries: ~39**

---

## Running Vault Total

| Previous | This Document | New Total |
|----------|---------------|-----------|
| ~953 | +39 | **~992 entries** |
