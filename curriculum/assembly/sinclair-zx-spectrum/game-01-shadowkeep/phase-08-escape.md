# Phase 8: Escape

**Game:** Shadowkeep (ZX Spectrum Game 1)
**Units:** 113–128
**Theme:** Commercial release quality — the complete game
**Z80 Focus:** Keyboard matrix, code optimisation, TAP/TZX file formats, memory audit
**Hardware:** Full keyboard scanning, 128K features, tape I/O
**Status:** Planned

---

## Overview

Phase 8 adds everything a commercial 1984 Spectrum game would ship with: high scores, difficulty selection, an ending sequence, and proper tape distribution files. No new gameplay mechanics — instead, every system from Phases 1–7 is polished, balanced, and integrated into a release-quality product.

The game's conclusion is literal: the player escapes the keep. A final room sequence leads to daylight, a victory screen, and credits. The journey from a coloured block on screen (Unit 1) to a complete, atmospheric dungeon crawler (Unit 128) mirrors the learner's journey from zero Z80 knowledge to genuine Spectrum programming competence.

---

## Prerequisites from Phase 7

- Complete game with all mechanics — Phase 8 polishes, doesn't add
- 128K memory paging — extra content, high score persistence
- Interrupt mode 2 — stable timing for menus and attract mode
- Full audio system — music for title, menus, ending

---

## Unit Progression

| Unit | Title | New Z80 Concept | Game Addition |
|------|-------|----------------|---------------|
| 113 | High Score Table | Multi-byte comparison, sorted insertion | Top 5 scores |
| 114 | Name Entry | Full keyboard matrix scanning ($FE rows) | 3-letter initials |
| 115 | High Scores on Title | Display integration, 128K persistence via paged RAM | Bragging rights |
| 116 | Difficulty Select | Menu system, key-driven cursor | Easy / Normal / Hard |
| 117 | Difficulty Affects Gameplay | Parameter tables: enemy speed, light radius, health | Real difference |
| 118 | Continue System | Resume from save point, limited continues | Forgiveness |
| 119 | Ending Sequence | Final room, escape to daylight, victory screen | **Narrative reward** |
| 120 | Credits Screen | Scrolling or paged text with colour effects | Attribution |
| 121 | Attract Mode | Recorded input playback, game plays itself | Demo mode |
| 122 | Attract on Title Timeout | Timer-triggered transition from title to demo | Shop display |
| 123 | Loading Screen | Character art displayed before game loads | Presentation |
| 124 | Two-Player Alternating | Turn-based play, separate scores | Social play |
| 125 | 48K Memory Audit | Fit everything in ~42KB, remove waste | Runs on all Spectrums |
| 126 | Final Testing | Edge cases, balance, difficulty curve | Release quality |
| 127 | TAP/TZX File Creation | Tape file formats, turbo loading (TZX) | Distribution |
| 128 | **Complete Game** | Final build, documentation, retrospective | **Ship it** |

---

## Key Teaching Moments

### Keyboard Matrix (Unit 114)

The Spectrum keyboard is a matrix of 8 rows × 5 columns. Port $FE reads a row selected by the high byte of the address. Each row maps to 5 keys. Scanning the full keyboard means reading 8 addresses:

```z80
    ld a,$fe            ; Row: CAPS-V
    in a,($fe)
    bit 0,a             ; CAPS SHIFT
    ; ...
    ld a,$fd            ; Row: A-G
    in a,($fe)
    ; etc.
```

For name entry, the code scans all rows each frame, maps the pressed key to a character, and handles debouncing (ignore if the key is still held from last frame). This is more involved than the simple directional checks in Phase 1 — full keyboard input for the first time.

### The Ending as Reward (Unit 119)

The final room sequence uses every trick from the game: a path through darkness, a last boss encounter, a locked door requiring the final key, then a room where the ceiling opens to show sky (attributes transition from dark to bright). A simple animation — the player walks upward off screen — and a victory message. The ending doesn't need to be elaborate; it needs to be earned.

### TAP and TZX Formats (Unit 127)

A `.tap` file is the simplest tape format: a header block (filename, type, length) followed by the data block. Each block has a flag byte and a checksum. The `.tzx` format supports turbo loading — faster baud rates that reduce load times from minutes to seconds. Most emulators support both. The learner creates a proper distribution file, not just a raw memory dump.

### 48K Memory Audit (Unit 125)

The 48K Spectrum has approximately 42KB of user RAM ($5B00–$FFFF). The game must fit: code, room data (compressed), UDG definitions, sound data, enemy tables, high score table, and working buffers. Auditing memory means listing every allocation, measuring its size, and ensuring nothing overlaps. If it doesn't fit, compression ratios improve or content is reduced. The 128K version has no such pressure — paged RAM provides ample space.

---

## Z80 Concepts Introduced

1. Full keyboard matrix scanning — 8 rows via port $FE high byte (Unit 114)
2. Key debouncing — track previous state to detect new presses (Unit 114)
3. Multi-byte comparison — cascading compare for score ranking (Unit 113)
4. Sorted insertion — shuffle table entries to maintain order (Unit 113)
5. Input abstraction — game reads from joystick or recording (Unit 121)
6. Tape block format — flag byte, data, XOR checksum (Unit 127)
7. Memory map audit — systematic allocation review (Unit 125)

---

## Hardware

### New in Phase 8

| Resource | Purpose | Introduced |
|----------|---------|-----------|
| Keyboard matrix (8 rows via $FE) | Full character input for name entry | Unit 114 |
| TAP/TZX file structure | Distribution format for tape/emulator | Unit 127 |

---

## Game State at Phase End

After Unit 128 — the complete game:

- **High scores** — top 5 with initials, sorted, displayed on title
- **Difficulty** — Easy/Normal/Hard with menu selection
- **Two-player** — alternating turns, separate scores
- **Attract mode** — auto-play demo after title timeout
- **Ending sequence** — escape the keep, victory screen, credits
- **Loading screen** — character art during tape load
- **48K compatible** — fits in memory, beeper audio
- **128K enhanced** — extra rooms, AY music, score persistence
- **TAP/TZX files** — ready for distribution
- **Full audio** — 48K beeper effects + 128K AY music
- **Full visuals** — UDG characters, animated, themed zones, fog of war
- **Boss encounters** — multi-phase fights with health bars
- **16+ rooms** — compressed, themed, connected, with secret passages

A game you could put on tape and sell through Crash magazine's mail-order pages in 1984.

---

## Quality Comparison Across All Phases

| Aspect | Phase 1 | Phase 4 | Phase 8 |
|--------|---------|---------|---------|
| Graphics | Attribute blocks, ROM font | + room themes, fast transitions | UDGs, animation, fog of war |
| World | 1 room | 16+ rooms, map, themes | + secret rooms, 128K extras |
| Enemies | None | + multiple types, patrol AI | + bosses, dark room enemies |
| Puzzles | Collect treasures | + keys, doors, one-way passages | + item combinations, traps |
| Audio | Single beeper tone | + beeper library, 128K AY detection | Full music, interrupt-driven |
| Features | Walk + collect + exit | + inventory, map, save points | High scores, attract, 2-player |
| Z80 Skill | LD, CP, JR | + LDIR, 16-bit, RLE | Full instruction set, IM 2 |

---

## What This Game Teaches

By completing Shadowkeep, learners are ready for:

- **Game 2 (Shatter, 128 units)** — attribute skills transfer to breakout physics. The ball uses pixel movement (learned in Phase 5), collision uses attribute reading
- **Game 3 (Cavern, 128 units)** — platformer physics build on character-cell movement. Gravity and jumping layer on top of the movement system
- **Game 5 (Ink War, 256 units)** — the attribute system becomes the core gameplay mechanic at a strategic level. Everything Shadowkeep teaches about attributes is foundation
- **Every future Spectrum game** — attribute-based collision, UDG graphics, beeper/AY audio, 48K/128K detection, and the screen memory layout are reused throughout

Shadowkeep isn't just Game 1. It's the foundation for the entire Spectrum curriculum.

---

**Version:** 1.0
**Last Updated:** 2026-02-06
