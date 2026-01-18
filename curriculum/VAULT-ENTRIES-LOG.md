# Vault Entries Log

**Purpose:** Track all Vault entries to be created based on curriculum references.
**Last Updated:** 2026-01-18

Each entry includes:
- **Slug:** URL-friendly identifier
- **Category:** One of 7 Vault types
- **Referenced In:** Where this appears in curriculum
- **Priority:** High (core concept), Medium (enhances understanding), Low (nice to have)

---

## Systems (4 entries)

Core platform entries - highest priority, foundational to everything.

| Slug | Title | Priority | Notes |
|------|-------|----------|-------|
| `c64` | Commodore 64 | High | Primary platform, 1982, 6510 CPU |
| `spectrum` | Sinclair ZX Spectrum | High | Primary platform, 1982, Z80 CPU |
| `nes` | Nintendo Entertainment System | High | Primary platform, 1983/85, 6502 CPU |
| `amiga` | Commodore Amiga | High | Primary platform, 1985, 68000 CPU |

---

## Hardware (25+ entries)

### Commodore 64

| Slug | Title | Priority | Referenced In | Notes |
|------|-------|----------|---------------|-------|
| `vic-ii` | VIC-II Graphics Chip | High | Games 1-16 | 6569 (PAL), sprites, raster |
| `sid` | SID Sound Chip | High | Games 1-16, especially Game 6 | 6581/8580, 3 voices, filters |
| `6510` | 6510 CPU | High | All games | 6502 variant with I/O port |
| `cia` | CIA Interface Chips | Medium | Games 1+ | 6526, timers, joystick, keyboard |
| `1541` | 1541 Disk Drive | Medium | Game 11, 16 | Floppy drive with own CPU |

### ZX Spectrum

| Slug | Title | Priority | Referenced In | Notes |
|------|-------|----------|---------------|-------|
| `ula` | Spectrum ULA | High | Games 1-16 | Custom chip handling video/keyboard |
| `z80` | Zilog Z80 | High | All games | 8-bit CPU |
| `ay-3-8912` | AY-3-8912 Sound Chip | Medium | Games 9+ (128K) | 3-voice PSG |
| `spectrum-memory` | Spectrum Memory Map | Medium | Games 1+ | Contended RAM, screen layout |

### Nintendo Entertainment System

| Slug | Title | Priority | Referenced In | Notes |
|------|-------|----------|---------------|-------|
| `ppu` | NES PPU (Picture Processing Unit) | High | Games 1-16 | 2C02, sprites, nametables |
| `apu` | NES APU (Audio Processing Unit) | High | Games 1-16 | 5 channels, DMC |
| `6502` | 6502 CPU | High | All games | Ricoh 2A03 variant |
| `mmc1` | MMC1 Mapper | Medium | Game 11+ | First mapper taught |
| `mmc3` | MMC3 Mapper | Medium | Games 15-16 | Advanced mapper, IRQ |

### Commodore Amiga

| Slug | Title | Priority | Referenced In | Notes |
|------|-------|----------|---------------|-------|
| `agnus` | Agnus Chip | High | Games 1-16 | DMA controller, Blitter, Copper |
| `denise` | Denise Chip | High | Games 1-16 | Video output, sprites |
| `paula` | Paula Chip | High | Games 1-16 | 4-channel audio, disk I/O |
| `copper` | Copper Co-processor | High | Games 1-16 | Display list processor |
| `blitter` | Blitter | High | Games 1-16 | Hardware graphics accelerator |
| `68000` | Motorola 68000 | High | All games | 32-bit registers, 16-bit bus |

### Cross-Platform

| Slug | Title | Priority | Referenced In | Notes |
|------|-------|----------|---------------|-------|
| `joystick-de9` | DE-9 Joystick Standard | Low | All platforms | Atari-style connector |
| `ntsc-pal` | NTSC vs PAL | Medium | All platforms | Regional timing differences |

---

## Techniques (50+ entries)

### Beginner Techniques (Games 1-4)

| Slug | Title | Priority | Platforms | Notes |
|------|-------|----------|-----------|-------|
| `game-loop` | Game Loop Architecture | High | All | Frame-based update cycle |
| `state-machine` | Game State Machines | High | All | Menu/play/pause/gameover states |
| `fixed-point-math` | Fixed-Point Arithmetic | High | All | 8.8 and 16.16 formats |
| `sprite-animation` | Frame-Based Animation | Medium | All | Cycling through frames |
| `tile-collision` | Tile-Based Collision | High | All | Grid-based detection |
| `bounding-box` | Bounding Box Collision | High | All | Rectangle overlap |

### Intermediate Techniques (Games 5-8)

| Slug | Title | Priority | Platforms | Notes |
|------|-------|----------|-----------|-------|
| `ring-buffer` | Ring Buffer Data Structure | Medium | All | Snake body, position history |
| `wall-kicks` | Tetris Wall Kicks | Low | All | Rotation adjustment |
| `ghost-ai` | Pac-Man Ghost AI | Medium | All | Personality-based behaviour |
| `hardware-scroll` | Hardware Scrolling | High | C64, NES, Amiga | Register-based scrolling |
| `software-scroll` | Software Scrolling | High | Spectrum | Bit-shifting techniques |

### Advanced Techniques (Games 9-12)

| Slug | Title | Priority | Platforms | Notes |
|------|-------|----------|-----------|-------|
| `sprite-multiplexing` | Sprite Multiplexing | High | C64 | Displaying 24+ sprites |
| `raster-interrupts` | Raster Interrupts | High | C64 | Mid-frame code execution |
| `stable-raster` | Stable Raster Timing | High | C64 | Double-IRQ technique |
| `y-depth-sorting` | Y-Depth Sprite Sorting | High | All | Beat 'em up ordering |
| `parallax-scrolling` | Multi-Layer Parallax | High | All | Depth through speed |
| `dual-playfield` | Dual Playfield Mode | Medium | Amiga | Two independent layers |
| `pseudo-3d-road` | Pseudo-3D Road Rendering | Medium | All | Outrun-style perspective |
| `pixel-scroll-spectrum` | Pixel Scrolling (Spectrum) | High | Spectrum | ROL/RR bit shifting |
| `self-modifying-code` | Self-Modifying Code | Medium | C64, Spectrum | Runtime code changes |

### Expert Techniques (Games 13-16)

| Slug | Title | Priority | Platforms | Notes |
|------|-------|----------|-----------|-------|
| `isometric-projection` | Isometric Projection | High | All | Diamond grid maths |
| `bullet-patterns` | Bullet Pattern Systems | Medium | All | Shmup attack design |
| `fld` | FLD (Flexible Line Distance) | Medium | C64 | Screen warp effect |
| `dycp` | DYCP Scrolling | Medium | C64 | Dynamic Y-coordinate positioning |
| `agsp` | AGSP Effects | Low | C64 | Sprite stretching |
| `fast-loader` | Fast Loader Creation | Medium | C64 | Custom disk routines |
| `dmc-samples` | DMC Sample Playback | Medium | NES | Delta modulation audio |
| `mmc3-irq` | MMC3 Scanline IRQ | Medium | NES | Mid-frame interrupts |
| `dual-48k-128k` | 48K/128K Dual Support | Medium | Spectrum | Multi-version games |
| `aga-support` | AGA Enhanced Graphics | Low | Amiga | A1200 256-colour mode |
| `ability-gating` | Metroidvania Ability Gating | Medium | All | Progress-blocking design |
| `combo-systems` | Fighting Game Combos | Medium | All | Input chains, frame data |

---

## Games (40+ entries)

Reference games mentioned in curriculum comparisons.

### Shooters

| Slug | Title | Priority | Platform(s) | Referenced In |
|------|-------|----------|-------------|---------------|
| `galaga` | Galaga | Medium | Arcade | Game 1 comparisons |
| `phoenix` | Phoenix | Low | Arcade | Game 1 comparisons |
| `gyruss` | Gyruss | Low | Arcade | Game 1 comparisons |
| `r-type` | R-Type | Medium | Multiple | Game 13 comparisons |
| `gradius` | Gradius | Medium | Multiple | Game 9 (NES) comparisons |
| `1942` | 1942 | Medium | Arcade/NES | Vertical shmup reference |
| `turrican` | Turrican | High | C64/Amiga | Game 15 (C64) inspiration |
| `shadow-of-the-beast` | Shadow of the Beast | High | Amiga | Game 9 (Amiga) parallax reference |

### Platformers

| Slug | Title | Priority | Platform(s) | Referenced In |
|------|-------|----------|-------------|---------------|
| `super-mario-bros` | Super Mario Bros. | High | NES | Platformer reference |
| `manic-miner` | Manic Miner | Medium | Spectrum | Single-screen platformer |
| `jet-set-willy` | Jet Set Willy | Medium | Spectrum | Multi-room exploration |
| `metroid` | Metroid | High | NES | Game 15 (NES) inspiration |
| `castlevania` | Castlevania | Medium | NES | Action platformer reference |

### Maze/Puzzle

| Slug | Title | Priority | Platform(s) | Referenced In |
|------|-------|----------|-------------|---------------|
| `pac-man` | Pac-Man | High | Arcade | Game 3/6 AI reference |
| `tetris` | Tetris | High | Multiple | Game 8 reference |
| `boulder-dash` | Boulder Dash | Medium | C64 | Puzzle-action reference |

### Adventure/RPG

| Slug | Title | Priority | Platform(s) | Referenced In |
|------|-------|----------|-------------|---------------|
| `zelda` | The Legend of Zelda | High | NES | Game 11 (C64/NES) inspiration |
| `knight-lore` | Knight Lore | High | Spectrum | Game 14/15 isometric reference |
| `head-over-heels` | Head Over Heels | Medium | Spectrum | Isometric reference |

### Racing

| Slug | Title | Priority | Platform(s) | Referenced In |
|------|-------|----------|-------------|---------------|
| `outrun` | OutRun | High | Arcade | Game 10/12 racing reference |
| `pitstop-ii` | Pitstop II | Medium | C64 | Split-screen racing |

### Beat 'Em Up / Fighting

| Slug | Title | Priority | Platform(s) | Referenced In |
|------|-------|----------|-------------|---------------|
| `streets-of-rage` | Streets of Rage | Medium | Genesis | Game 11 (Amiga) reference |
| `final-fight` | Final Fight | Medium | Arcade | Beat 'em up reference |
| `street-fighter-ii` | Street Fighter II | High | Arcade | Game 12 (C64) reference |
| `international-karate` | International Karate+ | Medium | C64 | Fighting game reference |

### Run 'n' Gun

| Slug | Title | Priority | Platform(s) | Referenced In |
|------|-------|----------|-------------|---------------|
| `contra` | Contra | High | NES | Game 12 (NES/Spectrum) reference |

### Other

| Slug | Title | Priority | Platform(s) | Referenced In |
|------|-------|----------|-------------|---------------|
| `frogger` | Frogger | Medium | Arcade | Game 2 (Amiga) reference |
| `breakout` | Breakout | Medium | Arcade | Game 3/4 reference |
| `arkanoid` | Arkanoid | Medium | Multiple | Breakout evolution |
| `uridium` | Uridium | Medium | C64 | Horizontal shooter reference |
| `paradroid` | Paradroid | Medium | C64 | Top-down action reference |

---

## People (30+ entries)

Programmers, musicians, and designers whose work or techniques are referenced.

### Composers/Musicians

| Slug | Title | Priority | Platform | Notes |
|------|-------|----------|----------|-------|
| `rob-hubbard` | Rob Hubbard | High | C64 | SID mastery, custom drivers |
| `martin-galway` | Martin Galway | Medium | C64 | SID composer |
| `ben-daglish` | Ben Daglish | Medium | C64 | SID composer |
| `tim-follin` | Tim Follin | High | Multiple | Technical audio innovation |
| `david-whittaker` | David Whittaker | Medium | Multiple | Cross-platform composer |
| `koji-kondo` | Koji Kondo | Medium | NES | Mario/Zelda composer |
| `hip-tanaka` | Hirokazu Tanaka | Medium | NES | Metroid composer |

### Programmers

| Slug | Title | Priority | Platform | Notes |
|------|-------|----------|----------|-------|
| `andrew-braybrook` | Andrew Braybrook | Medium | C64 | Uridium, Paradroid |
| `jon-ritman` | Jon Ritman | High | Spectrum | Knight Lore, Head Over Heels |
| `bernie-drummond` | Bernie Drummond | Medium | Spectrum | Knight Lore artist |
| `matthew-smith` | Matthew Smith | Medium | Spectrum | Manic Miner, Jet Set Willy |
| `jeff-minter` | Jeff Minter | Medium | C64/Multiple | Llamasoft, visual style |
| `manfred-trenz` | Manfred Trenz | Medium | C64/Amiga | Turrican creator |
| `chris-huelsbeck` | Chris Hülsbeck | Medium | C64/Amiga | Turrican composer |
| `shigeru-miyamoto` | Shigeru Miyamoto | Medium | NES | Mario, Zelda designer |
| `gunpei-yokoi` | Gunpei Yokoi | Low | NES | Metroid producer |

### Demo Scene

| Slug | Title | Priority | Platform | Notes |
|------|-------|----------|----------|-------|
| `fairlight` | Fairlight (Group) | Low | C64 | Demo/crack group |
| `horizon` | Horizon (Group) | Low | C64 | Demo group |

---

## Companies (20+ entries)

### Publishers/Developers

| Slug | Title | Priority | Notes |
|------|-------|----------|-------|
| `ultimate` | Ultimate Play the Game | High | Knight Lore, Filmation |
| `ocean` | Ocean Software | Medium | Major UK publisher |
| `hewson` | Hewson Consultants | Medium | Uridium, Paradroid |
| `llamasoft` | Llamasoft | Medium | Jeff Minter's company |
| `factor-5` | Factor 5 | Medium | Turrican developers |
| `nintendo` | Nintendo | High | NES manufacturer |
| `konami` | Konami | Medium | Contra, Castlevania |
| `capcom` | Capcom | Medium | Street Fighter |
| `sega` | Sega | Low | Streets of Rage |
| `psygnosis` | Psygnosis | Medium | Shadow of the Beast |
| `team-17` | Team17 | Low | Amiga developers |

### Hardware Manufacturers

| Slug | Title | Priority | Notes |
|------|-------|----------|-------|
| `commodore` | Commodore | High | C64, Amiga manufacturer |
| `sinclair` | Sinclair Research | High | Spectrum manufacturer |
| `mos-technology` | MOS Technology | Medium | 6502, SID creators |
| `zilog` | Zilog | Low | Z80 manufacturer |
| `motorola` | Motorola | Low | 68000 manufacturer |
| `ricoh` | Ricoh | Low | NES CPU/PPU manufacturer |

---

## Culture (15+ entries)

### Magazines

| Slug | Title | Priority | Platform | Notes |
|------|-------|----------|----------|-------|
| `zzap64` | Zzap!64 | Medium | C64 | UK magazine, reviews |
| `crash` | CRASH | Medium | Spectrum | UK magazine |
| `your-sinclair` | Your Sinclair | Medium | Spectrum | UK magazine |
| `commodore-user` | Commodore User | Low | C64 | UK magazine |
| `amiga-format` | Amiga Format | Low | Amiga | UK magazine |
| `nintendo-power` | Nintendo Power | Low | NES | US magazine |

### Movements/Phenomena

| Slug | Title | Priority | Notes |
|------|-------|----------|-------|
| `bedroom-coder` | Bedroom Coder Era | High | Solo/small team development |
| `demo-scene` | Demo Scene | High | Technical art movement |
| `type-in-listings` | Type-In Listings | Medium | Magazine code listings |
| `crack-intros` | Crack Intros | Low | Piracy scene influence on demos |

### Events

| Slug | Title | Priority | Notes |
|------|-------|----------|-------|
| `assembly` | Assembly (Demo Party) | Low | Finnish demo event |
| `revision` | Revision (Demo Party) | Low | German demo event |

### Formats/Standards

| Slug | Title | Priority | Notes |
|------|-------|----------|-------|
| `mod-format` | MOD Music Format | Medium | Amiga tracker format |
| `sid-format` | SID File Format | Low | C64 music preservation |
| `tap-format` | TAP Tape Format | Low | Spectrum tape archive |
| `d64-format` | D64 Disk Format | Low | C64 disk image |
| `adf-format` | ADF Disk Format | Low | Amiga disk image |
| `ines-format` | iNES ROM Format | Low | NES ROM standard |

---

## Priority Summary

| Priority | Count | Description |
|----------|-------|-------------|
| **High** | ~40 | Core concepts essential to curriculum |
| **Medium** | ~50 | Enhances understanding, frequently referenced |
| **Low** | ~30 | Nice to have, occasional reference |

**Recommended creation order:**
1. Systems (4) - Foundation
2. Hardware - High priority (15)
3. Techniques - High/Medium (30)
4. Games - High priority (15)
5. People - High priority (10)
6. Culture - High priority (5)
7. Remaining entries by priority

---

## Cross-Reference Notes

### Techniques → Pattern Library

Every Technique entry should link to corresponding Pattern Library patterns:
- `sprite-multiplexing` → `/patterns/commodore-64/rendering/sprite-multiplexing`
- `raster-interrupts` → `/patterns/commodore-64/rendering/raster-interrupts`
- `y-depth-sorting` → `/patterns/common/rendering/y-depth-sorting`

### Games → Curriculum

Games are referenced in curriculum comparisons:
- "Commercial quality comparable to [Knight Lore](/vault/games/knight-lore)"
- "Inspired by [Turrican](/vault/games/turrican)'s exploration design"

### Hardware → Skills Inventory

Hardware entries directly support skills taught:
- VIC-II → Sprite skills, raster skills
- SID → Audio skills
- Copper → Amiga parallax, gradients

---

## Document Status

- [x] Initial inventory created
- [ ] Cross-reference with existing Vault entries
- [ ] Prioritise creation order
- [ ] Begin High priority entries
- [ ] Review for completeness after curriculum updates
