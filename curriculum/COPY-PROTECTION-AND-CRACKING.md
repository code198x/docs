# Copy Protection & Cracking: The Eternal Arms Race

**Purpose:** Document how publishers protected software, how crackers broke it, and the technical and cultural implications of both sides.

**Last Updated:** 2026-01-18

---

## Why This Matters

Copy protection and cracking were:
1. **Technical education** - Taught deep system knowledge
2. **Arms race** - Drove innovation on both sides
3. **Demo scene origin** - Crackers became demo coders
4. **Industry concern** - Shaped business models
5. **Preservation challenge** - Protected disks harder to archive

---

## Part 1: Why Protection Existed

### The Piracy Problem

| Platform | Piracy Rate (estimated) |
|----------|------------------------|
| **8-bit computers** | Very high (80%+?) |
| **Amiga/ST** | High (70%+?) |
| **Consoles** | Lower (cartridge harder to copy) |
| **PC** | High, grew with CD burners |

### Publisher Perspective

| Concern | Response |
|---------|----------|
| **Lost sales** | Protection schemes |
| **Distribution control** | Retail relationships |
| **Development funding** | Higher prices |
| **Market size** | Volume vs margin |

### The Debate

| Position | Argument |
|----------|----------|
| **"Piracy is theft"** | Direct revenue loss |
| **"Try before buy"** | Piracy as marketing |
| **"Can't afford"** | Price too high anyway |
| **"Not lost sale"** | Would never have bought |

This debate continues today.

---

## Part 2: Tape Protection Schemes

### Basic Tape Tricks

| Technique | How It Worked |
|-----------|---------------|
| **Non-standard timing** | Different baud rate |
| **Header tricks** | Modified tape headers |
| **Multi-stage loaders** | Loading in chunks |
| **Encrypted blocks** | Decrypted during load |

### Speedlock (UK)

| Aspect | Notes |
|--------|-------|
| **Developer** | Speedlock Associates |
| **Used by** | Ocean, US Gold, many |
| **Technique** | Custom loader, encrypted data |
| **Versions** | Multiple iterations |

Speedlock was the most common UK tape protection.

### Custom Loaders

Publishers created distinctive loaders:
- Unique loading screens
- Brand recognition
- Protection and marketing combined

**Vault entries:**
- `speedlock` - Technique entry
- `tape-protection` - Technique entry
- `custom-loaders` - Technique entry

---

## Part 3: Disk Protection Schemes

### Floppy Disk Tricks

| Technique | How It Worked |
|-----------|---------------|
| **Extra tracks** | Data beyond track 40/80 |
| **Non-standard sectors** | Unusual sector sizes |
| **Weak bits** | Deliberately bad sectors |
| **Timing checks** | Measure disk rotation |
| **Track alignment** | Half-tracks |
| **Fat tracks** | Wider than normal |

### Platform-Specific Protections

#### C64 Disk Protection

| Scheme | Technique |
|--------|-----------|
| **Rapidlok** | Custom GCR encoding |
| **V-Max** | Non-standard tracks |
| **Vorpal** | Fast loader + protection |
| **Many others** | Constant innovation |

#### Amiga Disk Protection

| Scheme | Technique |
|--------|-----------|
| **Rob Northen Copylock** | Most common Amiga protection |
| **Timelord** | Timing-based |
| **Custom MFM** | Non-standard encoding |

**Rob Northen's Copylock** dominated Amiga protection.

#### Atari ST

| Scheme | Technique |
|--------|-----------|
| **Copylock** | Rob Northen here too |
| **Various** | Similar to Amiga |

### The Copylock Dynasty

Rob Northen's Copylock was used on:
- Hundreds of Amiga games
- Many Atari ST games
- Evolved through multiple versions
- Cat-and-mouse with crackers

**Vault entries:**
- `rob-northen` - People entry
- `copylock` - Technique entry
- `rapidlok` - Technique entry
- `disk-protection` - Technique entry

---

## Part 4: Manual-Based Protection

### Off-Disk Protection

| Type | Example |
|------|---------|
| **Code wheels** | Monkey Island, Starflight |
| **Manual lookups** | "Word 3, line 5, page 12" |
| **Map references** | "What city is at coordinate X?" |
| **Lenslock** | Physical decoder device |
| **Dongles** | Hardware keys |

### Lenslock

| Aspect | Notes |
|--------|-------|
| **Device** | Plastic prism held to screen |
| **Usage** | Decode two-letter code |
| **Problems** | Easily lost, annoying, different TVs |
| **Games** | Elite, others |

Lenslock was universally hated by players.

### Code Wheels

| Game | Implementation |
|------|----------------|
| **Monkey Island** | "Dial-a-Pirate" faces |
| **Pool of Radiance** | Translation wheel |
| **Starflight** | Star coordinates |

Code wheels were creative but photocopiable.

### Clever Manual Protection

Some games integrated protection creatively:
- **Police Quest** - Manual was police procedures
- **Falcon** - Manual was flight operations
- **Various** - Manual needed to play

**Vault entries:**
- `lenslock` - Technique entry
- `code-wheels` - Technique entry
- `manual-protection` - Technique entry

---

## Part 5: The Cracking Scene

### Who Were Crackers?

| Type | Motivation |
|------|------------|
| **Technical challenge** | Puzzle solving |
| **Scene status** | Reputation, "first release" |
| **Distribution** | Getting games to friends |
| **Anti-corporate** | Ideological |

### Scene Structure

| Role | Function |
|------|----------|
| **Cracker** | Removed protection |
| **Supplier** | Obtained original disks |
| **Sysop** | Ran BBSes |
| **Courier** | Distributed releases |
| **Swapper** | Traded via mail |

### Famous Cracking Groups

#### C64 Scene

| Group | Notes |
|-------|-------|
| **Fairlight** | Legendary, still active |
| **Ikari + Talent** | Collaboration |
| **Triad** | Long-running |
| **Cosmos** | Notable |

#### Amiga Scene

| Group | Notes |
|-------|-------|
| **Fairlight** | Multi-platform |
| **Skid Row** | Prolific |
| **Paradox** | Major group |
| **Razor 1911** | Multi-platform |
| **Class** | Notable |

#### PC Scene

| Group | Notes |
|-------|-------|
| **Razor 1911** | Pioneering |
| **Fairlight** | Continued |
| **Deviance** | Later era |
| **RELOADED** | Modern |

### The Crack Process

1. **Obtain original** - Buy or receive
2. **Analyse protection** - Disassemble, trace
3. **Find check** - Locate protection code
4. **Patch** - NOP out checks or fake responses
5. **Test** - Ensure game works
6. **Add intro** - Group branding (became demos)
7. **Distribute** - BBSes, mail, courier

### Crack Intros

**Crack intros** (cracktros) were splash screens:
- Group logo
- Scroller with greets
- Music
- Evolved into **demo scene**

**Vault entries:**
- `cracking-scene` - Culture entry
- `fairlight` - Culture entry (group)
- `razor-1911` - Culture entry
- `crack-intros` - Culture entry

---

## Part 6: Trainers & Cheats

### What Trainers Were

**Trainers** added cheats to cracked games:

| Feature | Implementation |
|---------|----------------|
| **Infinite lives** | Patch life counter |
| **Invincibility** | Skip collision check |
| **Level skip** | Jump to later levels |
| **All weapons** | Enable everything |

### Trainer Menus

Trainers often had menus:
```
PRESS 1 FOR INFINITE LIVES
PRESS 2 FOR INFINITE ENERGY
PRESS 3 FOR LEVEL SKIP
PRESS SPACE TO START GAME
```

### POKE Culture (Spectrum)

Spectrum magazines published POKEs:
```
POKE 35678,0    ; Infinite lives
```

Players typed these before running games.

### Multiface

| Device | Function |
|--------|----------|
| **Multiface One/128** | Spectrum hardware device |
| **Action Replay** | C64/Amiga equivalent |

These devices could:
- Freeze running games
- Search for values
- Create POKEs/trainers
- Save memory to tape/disk

### Game Genie

| Aspect | Notes |
|--------|-------|
| **Platform** | NES, Genesis, SNES, Game Boy |
| **Function** | Intercept memory reads |
| **Codes** | Published in books/magazines |
| **Legal battle** | Nintendo sued (and lost) |

**Vault entries:**
- `trainers` - Culture entry
- `poke-culture` - Culture entry
- `multiface` - Hardware entry
- `action-replay` - Hardware entry
- `game-genie` - Hardware entry
- `galoob` - Company entry

---

## Part 7: Technical Deep Dive

### Protection Techniques (Advanced)

| Technique | Platform | How Defeated |
|-----------|----------|--------------|
| **Decryption loops** | All | Dump after decrypt |
| **Timing checks** | Disk | Fake timing responses |
| **Hardware checks** | Various | Patch check code |
| **Checksum verification** | All | Recalculate or patch |
| **Self-modifying code** | All | Careful tracing |

### Anti-Debugging Tricks

| Trick | Purpose |
|-------|---------|
| **Watchdog timers** | Detect debugger delays |
| **Stack tricks** | Detect tracer |
| **Interrupt manipulation** | Confuse debuggers |
| **Code encryption** | Hide real code |

### Arms Race Examples

| Protection | Crack Response | Counter |
|------------|----------------|---------|
| Simple check | Patch NOP | Multiple checks |
| Multiple checks | Patch all | Encrypted checks |
| Encrypted | Dump after decrypt | Rolling encryption |
| Rolling encryption | Better analysis | More complexity |

---

## Part 8: Industry Responses

### Publisher Strategies

| Response | Effectiveness |
|----------|---------------|
| **Better protection** | Temporary delay |
| **Lower prices** | Budget games |
| **Add value** | Manuals, maps, boxes |
| **Online activation** | Modern DRM |
| **Accept some piracy** | Focus on genuine buyers |

### The Budget Games Connection

When Mastertronic proved £1.99 games sold:
- Some piracy converted to sales
- Impulse purchase price point
- Copying less worthwhile

### Positive Relationships

Some publishers tacitly accepted:
- Scene spread awareness
- Piracy as marketing
- Converting pirates later
- International markets reached

---

## Part 9: Preservation Implications

### Why Cracked Versions Matter Now

| Reason | Notes |
|--------|-------|
| **Originals degrading** | Magnetic media fails |
| **Protection prevents archiving** | Special hardware needed |
| **Cracked versions preserved** | Widely distributed |
| **Documentation lost** | Manual lookups impossible |

### Preservation Challenges

| Challenge | Status |
|-----------|--------|
| **Disk imaging** | Tools like Kryoflux help |
| **Dongle-protected** | Hardware recreation |
| **Online activation** | Servers shut down |
| **Manual lookups** | Scan and include |

### The Cracker as Preservationist

Crackers inadvertently preserved:
- Thousands of games still playable
- Protection schemes documented
- Game history accessible

**Vault entry:**
- `preservation-and-cracking` - Culture entry

---

## Part 10: Legal Aspects

### The Law

| Jurisdiction | Status |
|--------------|--------|
| **UK** | Computer Misuse Act (1990) |
| **US** | DMCA (1998) |
| **EU** | Various directives |

### Notable Legal Cases

| Case | Outcome |
|------|---------|
| **Nintendo vs Galoob (Game Genie)** | Galoob won |
| **Various scene busts** | Occasional prosecutions |
| **Abandonware** | Grey area |

### Modern Situation

| Aspect | Status |
|--------|--------|
| **Abandonware** | Legally grey, often tolerated |
| **Preservation exception** | Some legal provisions |
| **Scene prosecutions** | Occasional |
| **DRM circumvention** | Generally illegal |

---

## Part 11: Scene Culture

### Scene Values

| Value | Expression |
|-------|------------|
| **Speed** | "First release" prestige |
| **Quality** | Clean cracks, good trainers |
| **Honour** | Crediting, no re-releases |
| **Community** | Greets, collaborations |
| **Competition** | Group rivalries |

### Scene Communication

| Method | Era |
|--------|-----|
| **Crack intros** | Always |
| **Scrollers** | Message in intros |
| **NFO files** | Text file art |
| **BBSes** | Online gathering |
| **Demoparties** | Physical meetings |

### Evolution to Demo Scene

| Stage | Focus |
|-------|-------|
| **Cracking** | Remove protection |
| **Intros** | Show off skills |
| **Demos** | Art for its own sake |
| **Demoscene** | Separate culture |

---

## Part 12: Key People & Groups

### Protection Developers

| Person/Company | Contribution |
|----------------|--------------|
| **Rob Northen** | Copylock (Amiga/ST) |
| **Speedlock Associates** | Tape protection |
| **Various** | Custom schemes |

### Notable Crackers

| Handle | Group | Platform |
|--------|-------|----------|
| **Strider** | Fairlight | Multi |
| **The Karate Kid** | Various | C64 |
| **Many others** | Various | Various |

(Most crackers used handles, real names often unknown)

---

## Summary: New Vault Entries

| Category | Entries |
|----------|---------|
| **Techniques** | Protection schemes, cracking methods | 15 |
| **Culture** | Scene, trainers, POKEs | 10 |
| **Hardware** | Multiface, Action Replay, Game Genie | 5 |
| **People/Groups** | Northen, Fairlight, Razor 1911 | 8 |
| **Companies** | Galoob, Speedlock | 3 |

**Total new entries: ~41**

---

## Running Vault Total

| Previous | This Document | New Total |
|----------|---------------|-----------|
| ~1268 | +41 | **~1309 entries** |
