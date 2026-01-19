# Graphics and Audio Coverage

**Purpose:** Ensure the curriculum adequately covers graphics and audio creation, not just programming.

**Last Updated:** 2026-01-18

---

## The Challenge

Many bedroom coders of the 1980s weren't trained artists or musicians. They:
1. Learned the basics themselves
2. Used tools that made it accessible
3. Worked within severe constraints (which paradoxically helped)
4. Collaborated when they could

Our curriculum should acknowledge this and provide practical guidance.

---

## Part 1: Graphics Coverage

### What Learners Need

| Skill | Level | Why It Matters |
|-------|-------|----------------|
| Pixel art fundamentals | Beginner | Every game needs sprites and tiles |
| Platform colour constraints | Beginner | Working within limits |
| Sprite readability | Beginner | Gameplay clarity |
| Tile design | Beginner | Building worlds efficiently |
| Animation basics | Intermediate | Bringing sprites to life |
| Attribute-aware design | Intermediate | Spectrum/C64 colour clash |
| Character design (small) | Intermediate | Personality in 16×16 pixels |
| UI/HUD design | Intermediate | Communicating game state |
| Advanced techniques | Advanced | Dithering, anti-aliasing |

### Platform-Specific Graphics Constraints

#### Commodore 64
- **Sprites:** 24×21 pixels, 3 colours + transparent (or 12×21 multicolour)
- **Characters:** 8×8 pixels, 4 colours in multicolour mode
- **Screen:** 40×25 characters, 16 colours total
- **Challenge:** Limited sprite colours, but flexible character graphics

#### ZX Spectrum
- **No hardware sprites** - everything is software rendered
- **Attribute clash:** 8×8 pixel cells, 2 colours per cell (ink + paper)
- **Screen:** 256×192 pixels, 32×24 attribute cells
- **Challenge:** Designing around colour clash is THE skill

#### NES
- **Sprites:** 8×8 or 8×16, 3 colours + transparent per sprite
- **Background:** 8×8 tiles, 4 palettes (3 colours each + shared background)
- **Attribute table:** 16×16 pixel regions share palette
- **Challenge:** Very limited palettes, careful colour planning

#### Amiga
- **Hardware sprites:** 16 pixels wide, 3 colours + transparent
- **BOBs:** Any size via Blitter, but cost CPU/Blitter time
- **Screen:** Up to 32 colours (5 bitplanes), or 64/4096 in special modes
- **Challenge:** Most flexible, but BOB rendering costs performance

### Graphics Techniques to Teach

#### Beginner (Games 1-4)

| Technique | Description | Curriculum Integration |
|-----------|-------------|----------------------|
| **Silhouette design** | Readable shapes at small sizes | Game 1: Player/enemy must be instantly recognisable |
| **Colour coding** | Using colour for gameplay meaning | Game 1: Enemy types by colour |
| **Grid-based design** | Working in 8×8 or 16×16 units | Game 2: Platform tiles |
| **Minimal animation** | 2-4 frame cycles | Game 2: Walk cycle basics |
| **Contrast** | Foreground vs background readability | All games: Player must stand out |

#### Intermediate (Games 5-8)

| Technique | Description | Curriculum Integration |
|-----------|-------------|----------------------|
| **Tile variety** | Many tiles from few base designs | Game 5: Dungeon theming |
| **Animation principles** | Anticipation, follow-through | Game 6: Musical feedback |
| **Dithering basics** | Creating apparent colours/gradients | Game 7: Background depth |
| **Character personality** | Expression in limited pixels | Game 8: Piece design |
| **UI clarity** | Score, lives, status communication | All games: HUD design |

#### Advanced (Games 9-16)

| Technique | Description | Curriculum Integration |
|-----------|-------------|----------------------|
| **Anti-aliasing** | Smoothing edges manually | Game 9: Large sprites |
| **Sub-pixel animation** | Movement smaller than pixels | Game 10: Smooth racing |
| **Attribute-aware layout** | Designing for colour constraints | Game 14: Isometric |
| **Palette tricks** | Cycling, swapping for effects | Game 16: Demo effects |

### Graphics Tools to Document

#### Historical Tools

| Tool | Platform | Notes | Vault Entry |
|------|----------|-------|-------------|
| **Deluxe Paint** | Amiga | Industry standard, Lucasfilm used it | `deluxe-paint` |
| **OCP Art Studio** | C64/Spectrum | Popular all-in-one package | `ocp-art-studio` |
| **Koala Painter** | C64 | Bitmap art creation | `koala-painter` |
| **The Graphics Machine** | Spectrum | Sprite designer | `graphics-machine` |
| **NES Screen Tool** | NES (modern) | Tile/nametable editor | `nes-screen-tool` |

#### Modern Tools (for creating vintage-style art)

| Tool | Use | Notes |
|------|-----|-------|
| **Aseprite** | Pixel art, animation | Industry standard for indie/retro |
| **Pro Motion NG** | Pixel art | Deluxe Paint spiritual successor |
| **GIMP/Photoshop** | With indexed palette | Constrain to platform colours |
| **Multipaint** | C64/Spectrum-specific | Handles attribute constraints |
| **YY-CHR** | NES tile editing | Direct CHR manipulation |
| **Charpad/Spritepad** | C64 specific | Character/sprite editors |

### Graphics Vault Entries Needed

#### People (Artists)

| Slug | Name | Platform | Known For |
|------|------|----------|-----------|
| `bernie-drummond` | Bernie Drummond | Spectrum | Knight Lore, Head Over Heels |
| `oliver-frey` | Oliver Frey | Magazines | Zzap!64 and Crash covers |
| `bob-wakelin` | Bob Wakelin | C64/Spectrum | Ocean box art |
| `mark-ferrari` | Mark Ferrari | Amiga/PC | Lucasfilm palette cycling |
| `henk-nieborg` | Henk Nieborg | Multiple | Lionheart, Flink |
| `paul-robertson` | Paul Robertson | Modern | Mercenary Kings, Scott Pilgrim |

#### Techniques

| Slug | Technique | Description |
|------|-----------|-------------|
| `dithering` | Dithering | Creating gradients with limited colours |
| `attribute-aware-design` | Attribute-Aware Design | Designing for Spectrum/NES constraints |
| `palette-cycling` | Palette Cycling | Animation via colour rotation |
| `pixel-clusters` | Pixel Clusters | Grouping pixels for readability |
| `tile-variation` | Tile Variation | Many tiles from few bases |

---

## Part 2: Audio Coverage

### What Learners Need

| Skill | Level | Why It Matters |
|-------|-------|----------------|
| Sound chip basics | Beginner | Understanding the hardware |
| Sound effect design | Beginner | Feedback and feel |
| When to use sound | Beginner | Audio as communication |
| Basic music theory | Intermediate | Composing simple tunes |
| Tracker software | Intermediate | Creating music efficiently |
| Chip-specific techniques | Advanced | Exploiting hardware |
| Music direction | Advanced | Mood and pacing |

### Platform-Specific Audio

#### Commodore 64 (SID)
- **3 voices** - Each with independent waveform, ADSR, frequency
- **Waveforms:** Triangle, sawtooth, pulse (variable width), noise
- **Filter:** Low-pass, high-pass, band-pass (one filter shared)
- **Strengths:** Rich sound, filter for expression, ring mod/sync
- **Challenge:** Only 3 voices for music + SFX

#### ZX Spectrum
- **48K:** Single-channel beeper (1-bit output)
- **128K:** AY-3-8912 - 3 voices + noise
- **Strengths:** AY has crisp, clear sound
- **Challenge:** Beeper requires CPU time, very limited

#### NES (APU)
- **2 Pulse channels** - Square waves with duty cycle
- **1 Triangle channel** - Bass/melody
- **1 Noise channel** - Percussion
- **1 DMC channel** - 1-bit samples
- **Strengths:** Punchy, recognisable sound
- **Challenge:** Limited voices, DMC is tricky

#### Amiga (Paula)
- **4 channels** of 8-bit sampled audio
- **Stereo:** Channels 1&4 left, 2&3 right
- **Strengths:** Real samples, no synthesis limits
- **Challenge:** Sample memory, mixing for balance

### Audio Techniques to Teach

#### Beginner (Games 1-4)

| Technique | Description | Curriculum Integration |
|-----------|-------------|----------------------|
| **Feedback sounds** | Sound confirms player action | Game 1: Shoot, hit, die |
| **Pitch variation** | Same sound, different pitch = variety | Game 1: Different enemy hits |
| **Sound priority** | Important sounds override others | Game 2: Jump vs ambient |
| **Simple melodies** | 4-8 note loops | Game 1: Title screen |

#### Intermediate (Games 5-8)

| Technique | Description | Curriculum Integration |
|-----------|-------------|----------------------|
| **ADSR shaping** | Attack/Decay/Sustain/Release | Game 6: SID deep dive |
| **Arpeggios** | Rapid note cycling for chords | Game 6: Chord simulation |
| **Tracker basics** | Pattern-based composition | Game 6: Music creation |
| **Audio pacing** | Music tempo matching gameplay | Game 7: Speed-based music |
| **Jingles** | Short musical phrases for events | All: Level complete, game over |

#### Advanced (Games 9-16)

| Technique | Description | Curriculum Integration |
|-----------|-------------|----------------------|
| **Filter sweeps** | Moving filter cutoff | Game 6+: SID expression |
| **PWM (Pulse Width Mod)** | Animated pulse width | Game 6+: Richer tones |
| **Dynamic music** | Music responding to game state | Game 10+: Tension building |
| **DMC samples** | NES sample playback | Game 16: NES capstone |
| **Ring modulation** | Voice interaction effects | Game 16: C64 capstone |

### Audio Tools to Document

#### Historical Tools

| Tool | Platform | Notes | Vault Entry |
|------|----------|-------|-------------|
| **SoundTracker** | Amiga | First tracker, started it all | `soundtracker` |
| **ProTracker** | Amiga | Industry standard | `protracker` |
| **SID Wizard** | C64 | Modern SID tracker | `sid-wizard` |
| **Sound Monitor** | C64 | Early SID tool | `sound-monitor` |
| **Wham! Music Box** | Spectrum | AY tracker | `wham-music-box` |

#### Modern Tools (for creating vintage-style audio)

| Tool | Use | Notes |
|------|-----|-------|
| **FamiTracker** | NES music | Exports to NSF, very capable |
| **DefleMask** | Multi-platform | C64, Spectrum, Genesis, NES |
| **SID Wizard** | C64 | Cross-platform SID tracker |
| **Vortex Tracker II** | Spectrum AY | Standard for AY music |
| **OpenMPT** | MOD/tracker | Modern tracker, exports to Amiga formats |
| **BFXR/SFXR** | Sound effects | Quick retro SFX generation |

### Audio Vault Entries Needed

#### People (Composers) - Many already listed, adding:

| Slug | Name | Platform | Known For |
|------|------|----------|-----------|
| `jeroen-tel` | Jeroen Tel | C64 | Cybernoid, Turbo Outrun |
| `fred-gray` | Fred Gray | C64 | Mutants, Hysteria |
| `jonathan-dunn` | Jonathan Dunn | Multiple | Ocean games |
| `matt-furniss` | Matt Furniss | Multiple | Sega ports |
| `neil-baldwin` | Neil Baldwin | NES | Magician, James Bond Jr |
| `manami-matsumae` | Manami Matsumae | NES | Mega Man |
| `hip-tanaka` | Hirokazu Tanaka | NES | Metroid, Kid Icarus |
| `yuzo-koshiro` | Yuzo Koshiro | Multiple | Streets of Rage, ActRaiser |

#### Techniques

| Slug | Technique | Description |
|------|-----------|-------------|
| `arpeggio` | Arpeggio | Rapid note cycling for chord illusion |
| `pwm` | Pulse Width Modulation | Animating pulse width for movement |
| `filter-sweep` | Filter Sweep | Moving cutoff for expression |
| `vibrato` | Vibrato | Pitch wobble for warmth |
| `echo-delay` | Echo/Delay | Using voices for delay effect |
| `digi-drum` | Digi-Drums | Sample playback for percussion |

#### Tools

| Slug | Tool | Description |
|------|------|-------------|
| `protracker` | ProTracker | Amiga tracker software |
| `famitracker` | FamiTracker | NES music creation |
| `sid-wizard` | SID Wizard | Modern C64 tracker |
| `deflemask` | DefleMask | Multi-platform chiptune tracker |
| `deluxe-paint` | Deluxe Paint | Amiga graphics standard |

---

## Part 3: Curriculum Integration

### Approach: Learn By Doing

Rather than separate "art" and "music" courses, integrate into game creation:

| Game | Graphics Focus | Audio Focus |
|------|----------------|-------------|
| 1 | Sprite basics, silhouettes | Feedback sounds, simple melody |
| 2 | Tile design, animation | Jump/land sounds, jingles |
| 3 | Character design, colour coding | AI sounds, tension audio |
| 4 | Polish, juice, effects | Impact sounds, rhythm |
| 5 | Themed environments | Ambient, zone music |
| 6 | Musical visualisation | **DEEP DIVE: Chip audio mastery** |
| 7 | Scrolling backgrounds | Dynamic tempo |
| 8 | UI/HUD design | Combo sounds, escalation |
| 9+ | Platform-specific advanced | Platform-specific advanced |

### Game 6: The Audio Deep Dive

Each platform's Game 6 should be a rhythm/music game that forces deep audio understanding:

- **C64 (SID Symphony):** Full SID mastery - all waveforms, filter, ring mod
- **Spectrum:** AY tracker use, beeper techniques for 48K
- **NES:** APU channels, duty cycles, basic DMC
- **Amiga:** Sample-based composition, MOD format

### Supplementary Materials Needed

#### Graphics Guides

| Guide | Content |
|-------|---------|
| **Sprite Design Basics** | Silhouettes, readability, animation |
| **Tile Design** | Seamless tiling, variation from limited sets |
| **Platform Colour Guides** | Each platform's palette and constraints |
| **Attribute Clash Survival** | Spectrum-specific design strategies |

#### Audio Guides

| Guide | Content |
|-------|---------|
| **Sound Effect Design** | What makes good feedback sounds |
| **Chip Music Basics** | Waveforms, ADSR, composition |
| **Tracker Tutorial** | Platform-appropriate tracker |
| **When to Use Sound** | Audio as game design |

### Asset Provision Options

For learners who struggle with art/audio, we could:

1. **Provide base assets** - Starter sprites/sounds they can modify
2. **Asset packs** - Optional downloads for those who want to focus on code
3. **Collaboration encouragement** - Point to communities for asset sharing
4. **Tool tutorials** - Step-by-step guides for creating assets

---

## Part 4: New Vault Entries Summary

### Graphics

| Category | New Entries |
|----------|-------------|
| People | ~10 (artists) |
| Techniques | ~10 (pixel art, design) |
| Tools | ~10 (art software) |

### Audio

| Category | New Entries |
|----------|-------------|
| People | ~15 (composers) |
| Techniques | ~10 (chip music) |
| Tools | ~10 (trackers, editors) |

### Total New Entries: ~65

**Running Vault Total: ~465 entries**

---

## Part 5: The Honest Truth

### What We Can Teach
- Technical constraints (must understand to create anything)
- Basic principles (readability, feedback, communication)
- Tools and workflows (trackers, pixel editors)
- Historical context (what worked and why)
- Platform-specific techniques (dithering, arpeggios)

### What's Harder to Teach
- Artistic talent (but constraints help everyone)
- Musical ear (but understanding helps)
- Visual creativity (but rules provide structure)

### The Good News
- **Constraints breed creativity** - Limited palettes force good design
- **Tools have improved** - Modern pixel editors are very capable
- **Communities exist** - Asset sharing, collaboration
- **Many coders weren't artists** - They learned enough, or collaborated
- **"Programmer art" is a genre** - Some games embrace it

### The Historical Precedent

Many legendary games had "programmer art" that worked:
- **Tetris** - Functional blocks, iconic anyway
- **Elite** - Wireframe, became an aesthetic
- **Rogue** - ASCII characters, spawned a genre
- **Dwarf Fortress** - ASCII, beloved

And many bedroom coders learned enough to be competent:
- Matthew Smith (Manic Miner) - Distinctive, readable
- Jeff Minter - Unique style, personality over polish

---

## Action Items

1. [ ] Create graphics constraint guides per platform
2. [ ] Create audio basics guides per platform
3. [ ] Document recommended tools with tutorials
4. [ ] Integrate art/audio learning into game phases
5. [ ] Consider asset packs for struggling learners
6. [ ] Add artist/composer Vault entries
7. [ ] Add tool Vault entries
