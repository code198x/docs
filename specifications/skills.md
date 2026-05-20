# Skills Inventory: Code Like It's 198x

**Version:** 1.0
**Last Updated:** 2026-01-18

This document catalogues all skills taught across the curriculum, organised by:
- **Cross-Platform Skills** (applicable to all platforms)
- **Platform-Specific Skills** (unique to each system)

Each skill is tagged with:
- **Level:** Beginner (Games 1-4), Intermediate (Games 5-8), Advanced (Games 9-12), Expert (Games 13-16)
- **Category:** The technical domain

---

## Part 1: Cross-Platform Skills

These skills apply universally across C64, ZX Spectrum, NES, and Amiga.

---

### Category: Game Architecture

| Skill | Level | First Introduced | Description |
|-------|-------|------------------|-------------|
| Game loop structure | Beginner | Game 1 | Title → Game → Game Over → Restart cycle |
| State machines | Beginner | Game 1 | Managing game states (menu, playing, paused, game over) |
| Lives system | Beginner | Game 1 | Tracking and displaying player lives |
| Score system | Beginner | Game 1 | Accumulating and displaying points |
| Wave-based spawning | Beginner | Game 1 | Spawning enemies in structured waves |
| Difficulty progression | Beginner | Game 2 | Increasing challenge over time |
| Level data format | Beginner | Game 2 | Storing level layouts in data structures |
| Checkpoint systems | Intermediate | Game 5 | Saving progress mid-level |
| Password systems | Intermediate | Game 5 | Encoding progress as text codes |
| Save/load systems | Advanced | Game 11 | Persisting game state to storage |
| Multiple endings | Expert | Game 15 | Branching narrative based on completion |
| New Game+ mode | Expert | Game 16 | Enhanced replay with carried progress |

---

### Category: Player Movement

| Skill | Level | First Introduced | Description |
|-------|-------|------------------|-------------|
| 4-way movement | Beginner | Game 1 | Cardinal direction movement |
| 8-way movement | Beginner | Game 1 | Diagonal movement included |
| Screen boundary clamping | Beginner | Game 1 | Preventing player from leaving play area |
| Grid-based movement | Beginner | Game 3 | Snapping to tile positions |
| Smooth interpolation | Beginner | Game 3 | Animating between grid positions |
| Gravity simulation | Beginner | Game 2 | Constant downward acceleration |
| Jump mechanics | Beginner | Game 2 | Impulse-based vertical movement |
| Variable jump height | Beginner | Game 2 | Button release affects jump arc |
| Terminal velocity | Beginner | Game 2 | Maximum fall speed cap |
| Coyote time | Intermediate | Game 7 | Grace period for jumping after leaving platform |
| Jump buffering | Intermediate | Game 7 | Queuing jump input before landing |
| Wall sliding | Advanced | Game 14 | Slowed descent against walls |
| Wall jumping | Advanced | Game 14 | Bouncing off walls |
| Dash mechanics | Advanced | Game 15 | Quick directional burst movement |
| Grappling hook | Expert | Game 15 | Swing physics and attachment |

---

### Category: Physics & Mathematics

| Skill | Level | First Introduced | Description |
|-------|-------|------------------|-------------|
| Fixed-point arithmetic | Beginner | Game 3 | Sub-pixel precision (8.8 or 16.16 format) |
| Velocity and acceleration | Beginner | Game 2 | Speed changes over time |
| Ball physics | Beginner | Game 3 | Reflection angles and momentum |
| Angle-based collision response | Beginner | Game 3 | Hit position affects bounce direction |
| Slope physics | Intermediate | Game 7 | Walking on angled surfaces |
| Momentum transfer | Intermediate | Game 2 | Riding moving platforms |
| Curve mathematics | Advanced | Game 10 | Calculating road curves for racing |
| Perspective projection | Advanced | Game 10 | Pseudo-3D depth calculations |
| Isometric projection | Advanced | Game 14 | Diamond-grid coordinate conversion |

---

### Category: Collision Detection

| Skill | Level | First Introduced | Description |
|-------|-------|------------------|-------------|
| Bounding box collision | Beginner | Game 1 | Rectangle overlap testing |
| Point-in-rectangle | Beginner | Game 1 | Testing if position is inside area |
| Tile-based collision | Beginner | Game 2 | Checking tile type at position |
| Pixel-perfect collision | Intermediate | Game 4 | Checking actual pixel overlap |
| Multi-entity collision | Intermediate | Game 1 | Checking many objects efficiently |
| Hitbox/hurtbox separation | Advanced | Game 12 | Separate attack and damage areas |
| Swept collision | Advanced | Game 10 | Detecting fast-moving object intersections |
| Spatial partitioning | Expert | Game 9 | Grid or bucket-based collision optimisation |

---

### Category: Animation

| Skill | Level | First Introduced | Description |
|-------|-------|------------------|-------------|
| Frame-based animation | Beginner | Game 1 | Cycling through sprite frames |
| Direction-aware sprites | Beginner | Game 2 | Different frames for facing direction |
| Animation state machines | Beginner | Game 2 | Idle, walk, jump, fall states |
| Interpolated animation | Intermediate | Game 3 | Smooth transitions between positions |
| Anticipation frames | Intermediate | Game 2 | Visual preparation before action |
| Squash and stretch | Intermediate | Game 4 | Deformation for impact feel |
| Particle effects | Advanced | Game 7 | Small animated elements (sparks, dust) |
| Death animations | Beginner | Game 1 | Visual feedback for defeat |
| Screen shake | Intermediate | Game 5 | Camera movement for impact |
| Screen flash | Beginner | Game 1 | Colour change for emphasis |

---

### Category: Enemy AI

| Skill | Level | First Introduced | Description |
|-------|-------|------------------|-------------|
| Static enemies | Beginner | Game 1 | Non-moving threats |
| Patrol patterns | Beginner | Game 2 | Back-and-forth movement |
| Edge detection | Beginner | Game 2 | Turning at platform edges |
| Chase AI (direct) | Beginner | Game 3 | Moving toward player position |
| Predictive AI | Intermediate | Game 3 | Targeting where player will be |
| State-based AI | Intermediate | Game 3 | Chase/scatter mode switching |
| Personality-based AI | Intermediate | Game 3 | Different behaviours per enemy (Pac-Man ghosts) |
| Pathfinding | Intermediate | Game 5 | Finding routes around obstacles |
| Group coordination | Advanced | Game 11 | Enemies working together |
| Attack slots | Advanced | Game 11 | Limiting simultaneous attackers |
| Difficulty-based AI | Advanced | Game 5 | Adjusting AI based on settings |
| Rubber banding | Advanced | Game 11 | Dynamic difficulty adjustment |

---

### Category: Combat Systems

| Skill | Level | First Introduced | Description |
|-------|-------|------------------|-------------|
| Projectile spawning | Beginner | Game 1 | Creating bullets at player position |
| Bullet pooling | Beginner | Game 1 | Reusing bullet objects |
| Fire rate limiting | Beginner | Game 1 | Cooldown between shots |
| Multi-directional shooting | Intermediate | Game 8 | Aiming in 8 directions |
| Spread shot patterns | Intermediate | Game 1 | Multiple bullets in fan |
| Melee attacks | Intermediate | Game 5 | Close-range combat |
| Attack hitboxes | Intermediate | Game 5 | Defining damage areas |
| Combo systems | Advanced | Game 12 | Chained attack sequences |
| Frame data | Advanced | Game 12 | Startup, active, recovery frames |
| Juggle mechanics | Advanced | Game 11 | Air combo systems |
| Special moves | Advanced | Game 12 | Input sequences for abilities |
| Invincibility frames | Beginner | Game 2 | Brief immunity after damage |
| Knockback | Intermediate | Game 5 | Pushing back on hit |

---

### Category: Power-Up Systems

| Skill | Level | First Introduced | Description |
|-------|-------|------------------|-------------|
| Item drops | Beginner | Game 1 | Enemies dropping collectibles |
| Collection detection | Beginner | Game 1 | Player touching items |
| Temporary effects | Beginner | Game 1 | Time-limited power-ups |
| Timer display | Beginner | Game 1 | Showing remaining duration |
| Weapon upgrades | Intermediate | Game 1 | Enhanced firepower |
| Stacking upgrades | Intermediate | Game 9 | Cumulative improvements |
| Equipment systems | Advanced | Game 11 | Permanent gear with stats |
| Ability gating | Expert | Game 15 | Progress blocked until ability acquired |

---

### Category: Inventory & Items

| Skill | Level | First Introduced | Description |
|-------|-------|------------------|-------------|
| Item collection | Beginner | Game 2 | Picking up objects |
| Inventory data structure | Intermediate | Game 5 | Storing collected items |
| Key-door systems | Intermediate | Game 5 | Coloured keys unlock matching doors |
| Consumable items | Intermediate | Game 5 | One-use items (potions) |
| Equipment slots | Advanced | Game 11 | Weapon/armour assignment |
| Quest items | Advanced | Game 11 | Story-critical collectibles |
| Shop systems | Expert | Game 16 | Buying/selling with currency |

---

### Category: Level Design

| Skill | Level | First Introduced | Description |
|-------|-------|------------------|-------------|
| Static level layout | Beginner | Game 1 | Hard-coded level design |
| Data-driven levels | Beginner | Game 2 | Levels loaded from data |
| Metatile systems | Intermediate | Game 7 | 2×2 or larger tile groupings |
| Level streaming | Intermediate | Game 7 | Loading level data as needed |
| RLE compression | Intermediate | Game 7 | Run-length encoded level data |
| Multi-room architecture | Intermediate | Game 5 | Connected room transitions |
| Hub world design | Advanced | Game 11 | Central area connecting regions |
| Ability-gated progression | Expert | Game 15 | Metroidvania-style backtracking |
| Secret areas | Intermediate | Game 5 | Hidden bonus content |
| Boss arenas | Intermediate | Game 1 | Dedicated boss battle rooms |

---

### Category: User Interface

| Skill | Level | First Introduced | Description |
|-------|-------|------------------|-------------|
| Score display | Beginner | Game 1 | Showing current points |
| Lives display | Beginner | Game 1 | Showing remaining lives |
| Health bar | Intermediate | Game 5 | Visual health representation |
| Title screen | Beginner | Game 1 | Game introduction screen |
| Game over screen | Beginner | Game 1 | End state display |
| High score table | Beginner | Game 1 | Persistent best scores |
| Name entry | Beginner | Game 1 | Initials input for high scores |
| Pause menu | Intermediate | Game 3 | In-game pause functionality |
| Inventory screen | Intermediate | Game 5 | Viewing collected items |
| Map display | Advanced | Game 5 | Showing world layout |
| Dialogue system | Advanced | Game 11 | Text conversations with NPCs |
| Cutscene engine | Expert | Game 16 | Scripted story sequences |

---

### Category: Audio Design

| Skill | Level | First Introduced | Description |
|-------|-------|------------------|-------------|
| Sound effect triggering | Beginner | Game 1 | Playing sounds on events |
| Sound variety | Beginner | Game 1 | Different sounds for different actions |
| Music playback | Beginner | Game 1 | Background music loop |
| Music transitions | Intermediate | Game 6 | Fading between tracks |
| Sound priority | Intermediate | Game 6 | Important sounds override others |
| Dynamic audio | Advanced | Game 6 | Music responding to gameplay |
| Positional audio | Advanced | Game 3 | Pitch/volume based on position |

---

### Category: Visual Effects

| Skill | Level | First Introduced | Description |
|-------|-------|------------------|-------------|
| Colour cycling | Beginner | Game 1 | Animating palette colours |
| Explosion animations | Beginner | Game 1 | Multi-frame destruction |
| Trail effects | Intermediate | Game 3 | Afterimages following objects |
| Parallax backgrounds | Intermediate | Game 1 | Multi-speed background layers |
| Weather effects | Advanced | Game 10 | Rain, snow, fog rendering |
| Lighting effects | Expert | Game 14 | Dynamic light and shadow |

---

### Category: Data Structures

| Skill | Level | First Introduced | Description |
|-------|-------|------------------|-------------|
| Arrays | Beginner | Game 1 | Sequential data storage |
| Lookup tables | Beginner | Game 1 | Pre-computed value tables |
| Ring buffers | Intermediate | Game 7 | Circular data structure (snake body) |
| Entity pools | Intermediate | Game 1 | Reusable object collections |
| Linked structures | Advanced | Game 9 | Connected data nodes |
| Compression/decompression | Intermediate | Game 7 | Reducing data size |

---

### Category: Game Modes

| Skill | Level | First Introduced | Description |
|-------|-------|------------------|-------------|
| Single-player campaign | Beginner | Game 1 | Main game progression |
| Two-player alternating | Beginner | Game 1 | Taking turns |
| Two-player simultaneous | Intermediate | Game 9 | Both players active |
| Cooperative mode | Advanced | Game 11 | Players working together |
| Versus mode | Advanced | Game 8 | Players competing |
| Time attack | Intermediate | Game 8 | Speed-focused mode |
| Endless/survival | Intermediate | Game 7 | Play until failure |
| Boss rush | Expert | Game 15 | Sequential boss battles |
| Attract mode | Beginner | Game 1 | Demo playback |

---

## Part 2: Platform-Specific Skills

---

## Commodore 64

### Category: VIC-II Graphics

| Skill | Level | First Introduced | Description |
|-------|-------|------------------|-------------|
| Hardware sprite setup | Beginner | Game 1 | Enabling sprites via $D015 |
| Sprite positioning | Beginner | Game 1 | X/Y registers $D000-$D010 |
| Sprite colours | Beginner | Game 1 | Individual and shared colours |
| Multicolour sprites | Intermediate | Game 1 | 4-colour mode sprites |
| Sprite expansion | Intermediate | Game 5 | X/Y stretching |
| Sprite priority | Intermediate | Game 7 | Behind/in-front control ($D01B) |
| Sprite-sprite collision | Beginner | Game 1 | Hardware collision register $D01E |
| Sprite-background collision | Intermediate | Game 7 | Hardware collision register $D01F |
| Character set redefinition | Beginner | Game 3 | Custom characters via $D018 |
| Multicolour characters | Intermediate | Game 3 | 4-colour character mode |
| Screen memory layout | Beginner | Game 1 | 40×25 character display |
| Colour RAM | Beginner | Game 3 | Per-character colour at $D800 |
| Hardware scrolling | Intermediate | Game 7 | $D016 fine scroll (0-7 pixels) |
| Bitmap mode | Advanced | Game 16 | High-resolution graphics |

### Category: VIC-II Raster

| Skill | Level | First Introduced | Description |
|-------|-------|------------------|-------------|
| Raster interrupt basics | Intermediate | Game 7 | Triggering code at scanline |
| Raster register $D012 | Intermediate | Game 7 | Reading/setting raster position |
| Stable raster | Advanced | Game 9 | Eliminating timing jitter |
| Double IRQ technique | Advanced | Game 9 | Achieving cycle-exact timing |
| Badline awareness | Advanced | Game 9 | VIC-II stealing cycles |
| Multiple raster splits | Advanced | Game 9 | Several effects per frame |
| Border effects | Advanced | Game 7 | Opening side borders |
| FLD (Flexible Line Distance) | Expert | Game 16 | Screen warp effects |
| DYCP | Expert | Game 16 | Dynamic Y-coordinate characters |
| AGSP | Expert | Game 16 | Sprite geometry effects |
| Tech-tech | Expert | Game 16 | Character rotation effects |

### Category: Sprite Multiplexing

| Skill | Level | First Introduced | Description |
|-------|-------|------------------|-------------|
| Virtual sprite table | Advanced | Game 9 | Managing more than 8 sprites |
| Y-position sorting | Advanced | Game 9 | Ordering sprites for reuse |
| IRQ-based reuse | Advanced | Game 9 | Repositioning sprites mid-frame |
| Flicker management | Advanced | Game 9 | Distributing visible sprites |
| Priority allocation | Advanced | Game 9 | Important sprites always visible |

### Category: SID Audio

| Skill | Level | First Introduced | Description |
|-------|-------|------------------|-------------|
| SID register access | Beginner | Game 1 | Writing to $D400-$D418 |
| Frequency control | Beginner | Game 1 | Setting note pitch |
| ADSR envelope | Beginner | Game 1 | Attack/Decay/Sustain/Release |
| Waveform selection | Beginner | Game 1 | Triangle, saw, pulse, noise |
| Gate control | Beginner | Game 1 | Starting/stopping notes |
| Pulse width modulation | Intermediate | Game 6 | Animating pulse width |
| Filter basics | Intermediate | Game 6 | Low/high/band-pass filtering |
| Filter sweeps | Advanced | Game 6 | Animated filter cutoff |
| Ring modulation | Advanced | Game 6 | Voice interaction effects |
| Hard sync | Advanced | Game 6 | Voice synchronisation |
| Combined waveforms | Advanced | Game 16 | Multiple waveforms simultaneously |
| Digi-drums | Expert | Game 16 | Sample playback via volume |
| Dual SID detection | Expert | Game 16 | Supporting two SID chips |

### Category: C64 Disk I/O

| Skill | Level | First Introduced | Description |
|-------|-------|------------------|-------------|
| Kernal file routines | Advanced | Game 11 | $FFBD, $FFBA, $FFD8 etc. |
| File open/read/write | Advanced | Game 11 | Sequential file access |
| D64 disk image creation | Advanced | Game 11 | Building disk images |
| Save game implementation | Advanced | Game 11 | Persisting game state |
| Error handling | Advanced | Game 11 | Checking disk status |
| 1541 drive architecture | Expert | Game 16 | Understanding drive internals |
| Fast loader creation | Expert | Game 16 | Custom loading routines |
| Direct drive programming | Expert | Game 16 | Uploading code to drive |
| GCR decoding | Expert | Game 16 | Reading raw disk data |

---

## ZX Spectrum

### Category: Spectrum Graphics

| Skill | Level | First Introduced | Description |
|-------|-------|------------------|-------------|
| Attribute system | Beginner | Game 1 | 8×8 colour cells |
| Colour clash management | Beginner | Game 1 | Working within attribute limits |
| BRIGHT attribute | Beginner | Game 1 | High-intensity colours |
| FLASH attribute | Intermediate | Game 3 | Automatic colour cycling |
| UDG (User Defined Graphics) | Beginner | Game 2 | Custom 8×8 characters |
| Pixel plotting | Beginner | Game 1 | Individual pixel manipulation |
| Screen memory layout | Beginner | Game 1 | Understanding interleaved lines |
| Attribute RAM | Beginner | Game 1 | $5800-$5AFF colour area |
| Sprite rendering | Beginner | Game 1 | Software sprite drawing |
| Sprite masking | Intermediate | Game 4 | Transparent backgrounds |
| Pre-shifted sprites | Intermediate | Game 9 | Multiple pixel offsets stored |
| Dirty rectangle rendering | Intermediate | Game 7 | Only redrawing changed areas |

### Category: Spectrum Scrolling

| Skill | Level | First Introduced | Description |
|-------|-------|------------------|-------------|
| Character-level scroll | Intermediate | Game 9 | 8-pixel increments |
| Pixel-level scroll | Advanced | Game 9 | Smooth sub-character scroll |
| ROL/RR bit shifting | Advanced | Game 9 | Rotating screen data |
| Unrolled scroll loops | Advanced | Game 9 | Speed-optimised scrolling |
| Self-modifying scroll code | Advanced | Game 9 | Runtime code modification |
| Stack-based scrolling | Advanced | Game 9 | Using stack for speed |
| Attribute synchronisation | Advanced | Game 9 | Keeping colours aligned |
| Contended memory awareness | Advanced | Game 9 | Avoiding ULA conflicts |

### Category: Spectrum Audio

| Skill | Level | First Introduced | Description |
|-------|-------|------------------|-------------|
| Beeper basics | Beginner | Game 1 | Single-bit sound output |
| Frequency generation | Beginner | Game 1 | Timing loops for pitch |
| Multi-voice beeper tricks | Intermediate | Game 1 | Interleaved tones |
| Beeper music | Intermediate | Game 1 | Melody playback |
| AY-3-8912 basics (128K) | Intermediate | Game 9 | Three-voice chip access |
| AY tone control | Intermediate | Game 9 | Frequency and volume |
| AY noise channel | Intermediate | Game 9 | Percussion and effects |
| AY envelope | Intermediate | Game 9 | Hardware volume shapes |
| AY music player | Advanced | Game 10 | Pattern-based playback |

### Category: Spectrum System

| Skill | Level | First Introduced | Description |
|-------|-------|------------------|-------------|
| 48K memory layout | Beginner | Game 1 | Understanding RAM areas |
| 128K bank switching | Advanced | Game 9 | Accessing extra RAM |
| 128K detection | Advanced | Game 9 | Identifying machine type |
| Interrupt mode 2 | Intermediate | Game 5 | Custom interrupt handling |
| Tape loading basics | Advanced | Game 11 | Standard loader routines |
| TAP file format | Advanced | Game 11 | Tape archive structure |
| Multi-load structure | Advanced | Game 11 | Loading in sections |
| TZX turbo loading | Advanced | Game 11 | Faster tape formats |
| +3 disk access | Expert | Game 16 | Floppy disk I/O |

### Category: Spectrum 48K/128K Support

| Skill | Level | First Introduced | Description |
|-------|-------|------------------|-------------|
| Dual version development | Expert | Game 16 | Supporting both machines |
| AY/beeper fallback | Expert | Game 16 | Audio that works on both |
| Feature toggling | Expert | Game 16 | Enabling 128K extras |
| Memory-conditional code | Expert | Game 16 | Different paths per machine |

---

## Nintendo Entertainment System

### Category: NES PPU

| Skill | Level | First Introduced | Description |
|-------|-------|------------------|-------------|
| OAM (Object Attribute Memory) | Beginner | Game 1 | Sprite data structure |
| Sprite positioning | Beginner | Game 1 | X/Y coordinates in OAM |
| Sprite tile selection | Beginner | Game 1 | CHR ROM tile indices |
| Sprite attributes | Beginner | Game 1 | Palette, flip, priority |
| Sprite flipping | Beginner | Game 2 | Horizontal/vertical mirror |
| 8×16 sprite mode | Intermediate | Game 8 | Taller sprites |
| Metasprite assembly | Intermediate | Game 1 | Multiple sprites as one |
| Nametable rendering | Beginner | Game 1 | Background tile display |
| Attribute table | Beginner | Game 3 | 2×2 tile colour areas |
| Palette management | Beginner | Game 1 | 4 background + 4 sprite palettes |
| CHR tile design | Beginner | Game 1 | Creating graphics tiles |
| PPUSCROLL | Intermediate | Game 8 | Hardware scrolling |
| Split-screen techniques | Advanced | Game 9 | Fixed HUD with scrolling |
| Sprite 0 hit | Advanced | Game 8 | Timing via sprite collision |

### Category: NES Sprite Management

| Skill | Level | First Introduced | Description |
|-------|-------|------------------|-------------|
| 8-sprite per scanline limit | Intermediate | Game 1 | Understanding hardware limit |
| Sprite flickering | Intermediate | Game 1 | Rotating priority to show all |
| OAM cycling | Intermediate | Game 9 | Distributing flicker fairly |
| Y-depth sprite ordering | Advanced | Game 13 | Sorting for correct overlap |
| Sprite budget management | Advanced | Game 9 | Limiting on-screen sprites |

### Category: NES APU

| Skill | Level | First Introduced | Description |
|-------|-------|------------------|-------------|
| Pulse channel basics | Beginner | Game 1 | Square wave voices |
| Pulse duty cycle | Beginner | Game 1 | 12.5%, 25%, 50% waveforms |
| Triangle channel | Beginner | Game 1 | Bass and melody |
| Noise channel | Beginner | Game 1 | Percussion and effects |
| Length counter | Intermediate | Game 1 | Automatic note cutoff |
| Envelope | Intermediate | Game 1 | Volume changes over time |
| Sweep unit | Intermediate | Game 6 | Automatic pitch bend |
| DMC sample playback | Expert | Game 16 | Delta modulation samples |
| Music driver architecture | Intermediate | Game 6 | Pattern-based playback |

### Category: NES Mappers

| Skill | Level | First Introduced | Description |
|-------|-------|------------------|-------------|
| NROM (no mapper) | Beginner | Game 1-8 | 32K PRG + 8K CHR |
| MMC1 basics | Advanced | Game 11 | First mapper introduction |
| MMC1 serial register | Advanced | Game 11 | Bit-by-bit writing |
| MMC1 CHR banking | Advanced | Game 11 | Swapping graphics |
| MMC1 PRG banking | Advanced | Game 11 | Swapping code/data |
| MMC3 setup | Expert | Game 15 | Advanced mapper |
| MMC3 IRQ scanline | Expert | Game 16 | Mid-frame interrupts |
| MMC3 CHR banking | Expert | Game 15 | Fine-grained tile swaps |
| SRAM battery backup | Expert | Game 15 | Persistent save data |

### Category: NES System

| Skill | Level | First Introduced | Description |
|-------|-------|------------------|-------------|
| 6502 assembly basics | Beginner | Game 1 | CPU instructions |
| NMI handling | Beginner | Game 1 | Vertical blank interrupt |
| Controller reading | Beginner | Game 1 | Polling $4016/$4017 |
| Two-controller support | Intermediate | Game 8 | Player 2 input |
| iNES ROM format | Beginner | Game 1 | ROM header structure |
| NTSC/PAL timing | Intermediate | Game 1 | Regional differences |

---

## Commodore Amiga

### Category: Amiga Custom Chips

| Skill | Level | First Introduced | Description |
|-------|-------|------------------|-------------|
| Hardware sprite setup | Beginner | Game 1 | DMA sprite channels |
| Sprite positioning | Beginner | Game 1 | SPRPOS registers |
| Sprite colours | Beginner | Game 1 | Sprite palette entries |
| Sprite attachment | Intermediate | Game 5 | 15-colour sprites |
| BOB rendering | Beginner | Game 1 | Blitter Object basics |
| Blitter copy | Beginner | Game 1 | Fast memory transfers |
| Blitter fill | Beginner | Game 3 | Area filling |
| Blitter line draw | Intermediate | Game 3 | Hardware line drawing |
| Cookie-cut masking | Beginner | Game 4 | Transparent sprite backgrounds |
| Bitplane setup | Beginner | Game 1 | Configuring display |
| Display resolution | Beginner | Game 1 | Low-res, hi-res modes |
| Colour depth | Beginner | Game 1 | 2-64 colours |
| Dual playfield mode | Advanced | Game 9 | Two independent layers |
| HAM mode | Expert | Game 16 | Hold-And-Modify 4096 colours |

### Category: Copper Programming

| Skill | Level | First Introduced | Description |
|-------|-------|------------------|-------------|
| Copper list basics | Beginner | Game 1 | WAIT and MOVE commands |
| Copper colour changes | Beginner | Game 1 | Per-line palette |
| Copper gradient backgrounds | Intermediate | Game 1 | Smooth colour transitions |
| Copper split-screen | Intermediate | Game 9 | Fixed HUD areas |
| Copper palette cycling | Intermediate | Game 1 | Animated colours |
| Copper mid-screen effects | Advanced | Game 9 | Complex per-line changes |
| Copper raster bars | Advanced | Game 9 | Visual effects |

### Category: Blitter Operations

| Skill | Level | First Introduced | Description |
|-------|-------|------------------|-------------|
| Blitter channels (A/B/C/D) | Beginner | Game 1 | Source and destination |
| Blitter minterm logic | Intermediate | Game 4 | Boolean operations |
| Blitter shifting | Intermediate | Game 4 | Pixel alignment |
| Blitter modulo | Intermediate | Game 4 | Non-contiguous data |
| Blitter area fill | Intermediate | Game 3 | Flood fill technique |
| Blitter scroll | Advanced | Game 8 | Fast screen scrolling |
| Blitter queuing | Advanced | Game 1 | Multiple operations |
| Blitter/CPU coordination | Advanced | Game 9 | Avoiding conflicts |

### Category: Paula Audio

| Skill | Level | First Introduced | Description |
|-------|-------|------------------|-------------|
| Sample playback basics | Beginner | Game 1 | Playing sound effects |
| Sample loop | Beginner | Game 1 | Continuous sounds |
| Volume control | Beginner | Game 1 | Per-channel volume |
| Period (pitch) control | Beginner | Game 1 | Sample playback speed |
| 4-channel mixing | Intermediate | Game 2 | All channels active |
| MOD format playback | Intermediate | Game 2 | Tracker music support |
| Channel stealing | Intermediate | Game 1 | SFX over music |
| Stereo panning | Intermediate | Game 2 | Left/right placement |

### Category: Amiga System

| Skill | Level | First Introduced | Description |
|-------|-------|------------------|-------------|
| 68000 assembly basics | Beginner | Game 1 | CPU instructions |
| Bootable ADF creation | Beginner | Game 1 | Self-starting disks |
| xdftool usage | Beginner | Game 1 | Disk image manipulation |
| Startup-sequence | Beginner | Game 1 | Boot script |
| DMA timing | Intermediate | Game 9 | Chip bandwidth |
| DMACON register | Intermediate | Game 1 | Enabling DMA channels |
| Interrupt handling | Intermediate | Game 1 | Level 3 vertical blank |
| Vertical blank timing | Beginner | Game 1 | Frame synchronisation |
| OCS/ECS compatibility | Intermediate | Game 1 | Original chipset support |
| AGA enhancements | Expert | Game 15 | A1200 features |
| A500 memory constraints | Intermediate | Game 1 | 512K chip RAM limit |
| Disk-based streaming | Advanced | Game 11 | Loading during gameplay |

### Category: Amiga Scrolling

| Skill | Level | First Introduced | Description |
|-------|-------|------------------|-------------|
| Hardware scroll registers | Intermediate | Game 9 | BPLCON1 fine scroll |
| Coarse scroll via BPLxPT | Intermediate | Game 9 | Bitplane pointer adjustment |
| Tile streaming | Intermediate | Game 9 | Loading new columns/rows |
| Multi-layer parallax | Advanced | Game 9 | Different scroll speeds |
| Dual playfield parallax | Advanced | Game 9 | Independent layer scrolling |

---

## Part 3: Skill Progression by Game

### Beginner Skills (Games 1-4, 128 units each)

**Introduced in Game 1:**
- Basic platform architecture (sprites, tiles, collision)
- Simple game loop
- Score and lives systems
- Basic audio playback
- Title/game over screens

**Introduced in Game 2:**
- Gravity and jump physics
- Platform collision
- Enemy patrol patterns
- Level data loading
- Animation systems

**Introduced in Game 3:**
- Fixed-point mathematics
- Ball/paddle physics
- Custom character sets
- AI personalities (Pac-Man ghosts)
- Grid-based movement

**Introduced in Game 4:**
- Platformer feel refinement
- Moving platforms
- Hazard variety
- Multi-room basics
- Power-up systems

### Intermediate Skills (Games 5-8, 128 units each)

**Introduced in Game 5:**
- Multi-room exploration
- Inventory systems
- Key-door mechanics
- Health bars
- Combat systems

**Introduced in Game 6:**
- Audio chip mastery (SID/AY/APU/Paula)
- Music composition
- Filter effects
- Dynamic audio

**Introduced in Game 7:**
- Hardware scrolling
- Tile streaming
- Ring buffer data structures
- Visual polish techniques

**Introduced in Game 8:**
- Rotation systems (Tetris)
- Wall kicks
- Scoring complexity
- Two-player modes
- Performance basics

### Advanced Skills (Games 9-12, 256 units each)

**Introduced in Game 9:**
- Sprite multiplexing (C64)
- Software pixel scrolling (Spectrum)
- Multi-layer parallax
- Dual playfield (Amiga)
- MMC1 mapper (NES)

**Introduced in Game 10:**
- Pseudo-3D racing
- Perspective mathematics
- Camera systems
- Large level management

**Introduced in Game 11:**
- Disk/tape I/O
- Save systems
- Y-depth sorting (beat 'em ups)
- Group AI coordination
- Quest systems

**Introduced in Game 12:**
- Fighting game architecture
- Frame data systems
- Input buffering
- Combo systems
- Complex state machines

### Expert Skills (Games 13-16, 256-512 units each)

**Introduced in Game 13:**
- Bullet pattern systems
- Rank-based difficulty
- Formation AI
- Vertical shooter mastery

**Introduced in Game 14:**
- Isometric projection
- Depth sorting algorithms
- Complex puzzle systems
- Multi-floor dungeons

**Introduced in Game 15:**
- Metroidvania design
- Ability gating
- Large world management
- Multiple endings
- 100% completion tracking

**Introduced in Game 16 (Capstone):**
- Demo-scene effects (C64: FLD, DYCP, AGSP)
- Fast loader creation (C64)
- 48K/128K dual support (Spectrum)
- DMC samples (NES)
- Physical cartridge production (NES)
- AGA support (Amiga)
- Commercial-quality polish

---

## Part 4: Skills by Pattern Library Category

These categories align with the planned Pattern Library structure:

### Input Handling
- Joystick/controller reading
- Keyboard scanning
- Input buffering
- Debouncing
- Two-player input

### Rendering
- Sprite systems
- Tile rendering
- Scrolling techniques
- Animation systems
- Visual effects

### Physics
- Gravity systems
- Collision detection
- Ball physics
- Slope handling
- Momentum

### Audio
- Sound effects
- Music playback
- Channel management
- Platform-specific audio chips

### Data Management
- Level compression
- Save/load systems
- Entity pooling
- State machines

### AI Systems
- Patrol patterns
- Chase behaviours
- Pathfinding
- Group coordination

### Game Systems
- Score tracking
- Power-ups
- Inventory
- Combat
- Progression

---

**Document Status:** Initial draft
**Next Steps:** Cross-reference with Pattern Library specification
