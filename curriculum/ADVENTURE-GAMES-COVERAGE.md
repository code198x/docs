# Adventure Games: The Missing Genre

**Purpose:** Address the major gap in curriculum coverage of text and graphical adventures - one of the most important genres of the 8-bit era.

**Last Updated:** 2026-01-18

---

## Why This Is Critical

Adventure games were:
1. **Dominant genre** - Infocom, Sierra, Level 9 were major players
2. **Narrative pioneers** - Where storytelling in games developed
3. **Technical innovators** - Compression, parsers, virtual machines
4. **Design laboratories** - Puzzle design, player communication
5. **Literary crossover** - Attracted writers, legitimised games

Missing adventures from a retro curriculum is like missing shooters or platformers.

---

## Part 1: Text Adventures

### The Technical Challenge

Text adventures are deceptively complex:

| Challenge | Techniques |
|-----------|------------|
| **Text compression** | Huffman coding, abbreviations, dictionary systems |
| **World state** | Object locations, flags, complex state machines |
| **Parser** | Tokenisation, grammar, disambiguation |
| **Virtual machines** | Z-Machine, A-Machine, custom interpreters |
| **Memory management** | Paging, overlays for large games |

### Key Companies

#### Infocom (USA, 1979-1989)

| Aspect | Notes |
|--------|-------|
| **Founded by** | MIT students, Zork creators |
| **Innovation** | Z-Machine virtual machine |
| **Quality** | "Implementors" - writer/programmer hybrids |
| **Output** | 35+ games, multiple genres |
| **Legacy** | Set the standard for parser games |

**Key games:**
- **Zork I, II, III** - Dungeon exploration
- **Hitchhiker's Guide** - Adams collaboration
- **Planetfall** - Floyd the robot, emotional AI
- **A Mind Forever Voyaging** - Political narrative
- **Trinity** - Nuclear allegory

**Key people:**
- **Marc Blank** - Zork co-creator
- **Dave Lebling** - Zork co-creator
- **Steve Meretzky** - Hitchhiker's, Planetfall
- **Brian Moriarty** - Trinity, Loom
- **Amy Briggs** - Plundered Hearts (romance adventure)

**Vault entries:** `infocom`, `z-machine`, `zork`, all key people

---

#### Level 9 (UK, 1981-1991)

| Aspect | Notes |
|--------|-------|
| **Founded by** | Austin brothers (Pete, Mike, Nick) |
| **Innovation** | A-CODE system, extreme compression |
| **Specialty** | Fitting complex games into 32-48KB |
| **Quality** | UK's Infocom equivalent |

**Key games:**
- **Colossal Adventure** - Improved Crowther/Woods port
- **Snowball** - Silicon Dreams trilogy
- **The Worm in Paradise** - Political SF
- **Knight Orc** - Humorous fantasy
- **Gnome Ranger** - Comedy adventure

**Technical achievement:** Level 9 fit games with 200+ rooms and sophisticated parsing into 32KB Spectrum tapes. Their compression was legendary.

**Vault entries:** `level-9`, `austin-brothers`, `a-code`, key games

---

#### Melbourne House (Australia/UK, 1980s)

| Aspect | Notes |
|--------|-------|
| **Key product** | The Hobbit (1982) |
| **Innovation** | Inglish parser, NPC behaviour |
| **Quality** | Revolutionary for its time |

**The Hobbit:**
- NPCs with independent behaviour
- Sophisticated parser ("Inglish")
- Time-passing world
- Multiple solutions
- Literary license (Tolkien estate)

**Vault entries:** `the-hobbit-game`, `inglish-parser`

---

#### Magnetic Scrolls (UK, 1985-1992)

| Aspect | Notes |
|--------|-------|
| **Founded by** | Anita Sinclair, Ken Gordon |
| **Innovation** | Beautiful graphics + sophisticated parser |
| **Quality** | Often called "British Infocom" |

**Key games:**
- **The Pawn** - First release, impressive graphics
- **Guild of Thieves** - Heist adventure
- **Jinxter** - Comedy fantasy
- **Fish!** - Surreal goldfish spy

**Key people:**
- **Anita Sinclair** - Founder, producer (notable woman in industry)
- **Ken Gordon** - Technical director

**Vault entries:** `magnetic-scrolls`, `anita-sinclair`, `the-pawn`

---

#### Adventure International (USA, 1978-1985)

| Aspect | Notes |
|--------|-------|
| **Founded by** | Scott Adams (no relation to Dilbert) |
| **Innovation** | First commercial text adventures |
| **Platforms** | TRS-80, then everywhere |

**Key games:**
- **Adventureland** - First commercial adventure
- **Pirate Adventure**
- **The Count** - Dracula themed
- **Ghost Town**

**Vault entries:** `adventure-international`, `scott-adams-developer`

---

### Parser Technology

The parser is where much innovation happened:

| Level | Capability | Examples |
|-------|------------|----------|
| **Two-word** | VERB NOUN | Scott Adams games |
| **Simple sentence** | VERB NOUN with prepositions | Early Infocom |
| **Complex sentence** | Multiple objects, pronouns | Later Infocom |
| **Natural language** | Sophisticated disambiguation | The Hobbit, Magnetic Scrolls |

**Vault entries:**
- `text-parser` - Technique entry
- `tokenisation` - Technique entry
- `disambiguation` - Technique entry

---

### Virtual Machines

Adventures pioneered portable virtual machines:

| VM | Company | Notes |
|----|---------|-------|
| **Z-Machine** | Infocom | Ran on 25+ platforms |
| **A-CODE** | Level 9 | Efficient for small systems |
| **QUILL** | Gilsoft | Made adventures accessible |
| **PAW** | Gilsoft | Professional Adventure Writer |
| **TADS** | Modern | Text Adventure Development System |
| **Inform** | Modern | Graham Nelson's system, Z-Machine target |

**Vault entries:** `z-machine`, `quill`, `paw`, `inform`

---

## Part 2: Graphical Adventures

### Point-and-Click Revolution

#### Sierra On-Line (USA, 1979-1999)

| Aspect | Notes |
|--------|-------|
| **Founded by** | Ken and Roberta Williams |
| **Innovation** | AGI then SCI engines, graphical + parser |
| **Output** | King's Quest, Space Quest, Police Quest, Leisure Suit Larry |
| **Cultural impact** | Defined graphical adventures |

**Key series:**
- **King's Quest** (8 games) - Fantasy adventure
- **Space Quest** (6 games) - Sci-fi comedy (Two Guys from Andromeda)
- **Police Quest** (4 games) - Procedural police sim
- **Leisure Suit Larry** (7+ games) - Adult comedy
- **Gabriel Knight** (3 games) - Supernatural mystery

**Key people:**
- **Roberta Williams** - King's Quest creator, design pioneer
- **Ken Williams** - Technical, business
- **Al Lowe** - Leisure Suit Larry
- **Mark Crowe & Scott Murphy** - Space Quest ("Two Guys")
- **Jane Jensen** - Gabriel Knight
- **Lori Ann Cole** - Quest for Glory (with Corey Cole)

**Vault entries:** `sierra`, `roberta-williams`, `ken-williams`, `agi-engine`, `sci-engine`, all series, all key people

---

#### LucasArts/Lucasfilm Games (USA, 1982-2013)

| Aspect | Notes |
|--------|-------|
| **Innovation** | SCUMM engine, no dead ends, no deaths |
| **Design philosophy** | Player shouldn't get stuck unfairly |
| **Output** | Maniac Mansion, Monkey Island, Day of the Tentacle, etc. |

**Key games:**
- **Maniac Mansion** (1987) - First SCUMM game
- **Zak McKracken** (1988) - Alien conspiracy
- **Indiana Jones** series - Licensed adventures
- **Loom** (1990) - Musical interface
- **The Secret of Monkey Island** (1990) - Pirate comedy masterpiece
- **Day of the Tentacle** (1993) - Time travel sequel
- **Sam & Max Hit the Road** (1993) - Freelance police
- **Full Throttle** (1995) - Biker adventure
- **The Dig** (1995) - Sci-fi
- **Grim Fandango** (1998) - Day of the Dead noir

**Key people:**
- **Ron Gilbert** - SCUMM creator, Maniac Mansion, Monkey Island
- **Tim Schafer** - Monkey Island, Day of the Tentacle, Grim Fandango
- **Dave Grossman** - Monkey Island, Day of the Tentacle
- **Gary Winnick** - Maniac Mansion co-designer
- **Brian Moriarty** - Loom (from Infocom)

**Design innovations:**
- **No deaths** (mostly) - Player could experiment
- **No dead ends** - Couldn't make game unwinnable
- **Verb-object interface** - Click verbs, click objects
- **Dialogue trees** - Multiple choice conversations

**Vault entries:** `lucasarts-adventures`, `scumm`, `ron-gilbert`, `tim-schafer`, all major games

---

#### Other Important Companies

| Company | Key Games | Notes |
|---------|-----------|-------|
| **Revolution Software** | Lure of the Temptress, Beneath a Steel Sky, Broken Sword | UK developer, Charles Cecil |
| **Delphine Software** | Future Wars, Operation Stealth, Cruise for a Corpse | French, cinematic style |
| **Westwood** | Legend of Kyrandia series | Before Command & Conquer |
| **Cyan** | Myst | Changed everything (for better or worse) |
| **Access Software** | Tex Murphy series | FMV integration |

**Vault entries:** `revolution-software`, `charles-cecil`, `delphine-software`, `myst`

---

## Part 3: Technical Innovations

### Compression Techniques

Adventures pushed compression harder than almost any genre:

| Technique | Used By | Notes |
|-----------|---------|-------|
| **Dictionary compression** | Infocom | Common words stored once |
| **Huffman coding** | Various | Variable-length encoding |
| **Abbreviations** | Level 9 | "the" = 1 byte |
| **Token threading** | Various | Bytecode for story logic |
| **Image compression** | Sierra, LucasArts | Vector + fill graphics |

**Vault entries:**
- `text-compression` - Technique entry
- `adventure-game-compression` - Technique entry

---

### Graphics Technology

| Technique | Era | Examples |
|-----------|-----|----------|
| **Vector graphics** | Early | AGI games |
| **Dithered bitmaps** | Mid | SCI games |
| **Room-based** | Throughout | Pre-rendered backgrounds |
| **Rotoscoping** | 1990s | Prince of Persia, Another World |

---

### State Management

Adventures needed complex state tracking:

| Concept | Notes |
|---------|-------|
| **Object trees** | Items in containers in rooms |
| **Flag systems** | Thousands of boolean states |
| **Event triggers** | When X happens, do Y |
| **NPC schedules** | Characters with routines (The Hobbit) |
| **Time passage** | World changes over turns |

**Vault entry:**
- `adventure-state-management` - Technique entry

---

## Part 4: Design Principles

### What Adventures Taught

| Principle | Adventure Origin | Modern Application |
|-----------|------------------|-------------------|
| **Environmental storytelling** | Room descriptions | Every walking simulator |
| **Puzzle design** | Lock-and-key logic | Metroidvania, Zelda |
| **Dialogue systems** | Conversation trees | Every RPG |
| **Narrative branching** | Multiple solutions | Choice-based games |
| **Player agency** | Parser freedom | Open world design |
| **Fair play** | Infocom/LucasArts rules | Modern game design ethics |

### Infocom's Design Rules

1. Be fair - don't kill player without warning
2. Provide hints - not walkthrough, but nudges
3. Multiple solutions when possible
4. Reward exploration
5. Writing quality matters

### LucasArts' Design Rules

1. **No deaths** (or instant restore)
2. **No dead ends** - can't make game unwinnable
3. **Puzzles must be logical** - solutions make sense
4. **Comedy is valid** - games can be funny

**Vault entry:**
- `adventure-design-principles` - Technique entry

---

## Part 5: People to Add

### Women in Adventures (significant!)

| Person | Role | Contribution |
|--------|------|--------------|
| **Roberta Williams** | Designer | King's Quest, Phantasmagoria |
| **Anita Sinclair** | Founder/Producer | Magnetic Scrolls |
| **Jane Jensen** | Designer | Gabriel Knight series |
| **Lori Ann Cole** | Designer | Quest for Glory (with Corey Cole) |
| **Amy Briggs** | Designer | Plundered Hearts (Infocom) |

### Key Designers

| Person | Role | Contribution |
|--------|------|--------------|
| **Will Crowther** | Original creator | Colossal Cave Adventure |
| **Don Woods** | Expander | Colossal Cave (expanded version) |
| **Scott Adams** | Pioneer | First commercial adventures |
| **Marc Blank** | Infocom | Zork co-creator |
| **Dave Lebling** | Infocom | Zork co-creator |
| **Steve Meretzky** | Infocom | Hitchhiker's, Planetfall |
| **Ron Gilbert** | LucasArts | SCUMM, Monkey Island |
| **Tim Schafer** | LucasArts | Day of the Tentacle, Grim Fandango |
| **Charles Cecil** | Revolution | Broken Sword |
| **Pete Austin** | Level 9 | A-CODE, numerous games |

---

## Part 6: Games for Vault

### Text Adventures

| Game | Company | Notes |
|------|---------|-------|
| **Colossal Cave Adventure** | Crowther/Woods | The original |
| **Zork I** | Infocom | Defined the genre |
| **The Hitchhiker's Guide** | Infocom | Adams collaboration |
| **Planetfall** | Infocom | Floyd the robot - emotional AI |
| **Trinity** | Infocom | Nuclear allegory masterpiece |
| **The Hobbit** | Melbourne House | Revolutionary parser and NPC |
| **Snowball** | Level 9 | Silicon Dreams trilogy |
| **The Pawn** | Magnetic Scrolls | Beautiful graphics + parser |

### Graphical Adventures

| Game | Company | Notes |
|------|---------|-------|
| **Mystery House** | Sierra | First graphical adventure (1980) |
| **King's Quest** | Sierra | Defined graphical adventure |
| **Maniac Mansion** | LucasArts | First SCUMM game |
| **The Secret of Monkey Island** | LucasArts | Comedy masterpiece |
| **Day of the Tentacle** | LucasArts | Time travel sequel |
| **Loom** | LucasArts | Musical interface |
| **Beneath a Steel Sky** | Revolution | Cyberpunk, free on GOG |
| **Myst** | Cyan | Changed everything |
| **Grim Fandango** | LucasArts | 3D adventure masterpiece |

---

## Part 7: Curriculum Integration

### Should We Teach Adventures?

**Arguments for:**
- Major genre of the era
- Technically interesting (parsers, compression, VMs)
- Design principles still relevant
- Different from action games - expands scope

**Arguments against:**
- Less "game programming" in traditional sense
- Writing-heavy (not our strength either)
- Complex to implement fully
- Parser games are niche now

### Possible Integration Points

| Option | Approach |
|--------|----------|
| **Vault only** | Document history and techniques, don't teach |
| **One game** | Add adventure as Game 17+ optional track |
| **Techniques** | Teach compression, parsers as standalone skills |
| **Design lessons** | Reference adventure design in other games |

### If We Teach (Recommended: Optional Track)

A text adventure could teach:
- String handling and parsing
- State management
- Compression techniques
- Data-driven design
- Narrative structure

**Platform suitability:**
- **Spectrum/C64:** Natural fit, strong adventure tradition
- **NES:** Less tradition, but doable
- **Amiga:** Graphical adventures more natural

---

## Part 8: Modern Relevance

### Adventures → Modern Games

| Adventure Element | Modern Equivalent |
|-------------------|-------------------|
| Text parser | Voice commands, chatbots |
| Dialogue trees | Every RPG, visual novel |
| Environmental storytelling | Walking simulators |
| Puzzle design | Escape rooms, puzzle games |
| Point-and-click | Touch interfaces |
| Virtual machines | Unity, Unreal, Godot |

### Revival Scene

- **Wadjet Eye Games** - Modern pixel art adventures
- **Thimbleweed Park** - Gilbert/Winnick reunion
- **Disco Elysium** - Text-heavy RPG
- **Return to Monkey Island** - Gilbert returns!
- **Interactive Fiction** - Inform, Twine, modern tools

---

## Summary: New Vault Entries

| Category | Entries |
|----------|---------|
| **Companies** | Infocom, Level 9, Sierra, LucasArts, Magnetic Scrolls, Revolution, Adventure International | 7 |
| **People** | ~25 (Williams, Gilbert, Schafer, Meretzky, Austin brothers, etc.) | 25 |
| **Games** | ~20 (Zork, Monkey Island, King's Quest, The Hobbit, etc.) | 20 |
| **Techniques** | Parser, compression, Z-Machine, SCUMM, state management | 8 |
| **Culture** | Adventure game design principles, text adventure history | 3 |

**Total new entries: ~63**

---

## Running Vault Total

| Previous | This Document | Non-Western | New Total |
|----------|---------------|-------------|-----------|
| ~535 | +63 | +43 | **~641 entries** |
