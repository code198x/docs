# Phase 1 Curriculum: 6507 Assembly + TIA Programming (Lessons 1-64) - Showcase

> **⚠️ SHOWCASE PLATFORM:** This curriculum focuses on Atari 2600's extreme constraints and "racing the beam" technique. 64 lessons across 2 games teach the most challenging retro programming.

## Primary Documentation

**Start here:** [`phase-1/overview.md`](phase-1/overview.md)

This provides the Phase 1 overview with philosophy, structure, and learning outcomes for Atari 2600 kernel programming.

## Detailed Documentation

| What you need | Where to find it |
|---------------|------------------|
| **Tier 1 details** (Wall Breaker, L1-32) | [`phase-1/tier-1/README.md`](phase-1/tier-1/README.md) |
| **Tier 2 details** (Alien Defense, L33-64) | [`phase-1/tier-2/README.md`](phase-1/tier-2/README.md) |
| **Individual lesson specs** | [`phase-1/tier-{1-2}/lesson-NNN.md`](phase-1/) |

## Why This Structure?

**Organised by tier and lesson**

**Benefits:**
- **60-70% less context** when working on specific lessons
- **Better organisation** with clear hierarchy (phase → tier → lesson)
- **Easier navigation** to find specific game or concept
- **Scalable** for future expansion

## Atari 2600-Specific Features

This curriculum showcases the most constrained retro gaming platform:

- **6507 CPU @ 1.19MHz** - Cost-reduced 6502 with 13 address lines (8KB space)
- **128 BYTES of RAM** - Not kilobytes. Bytes. Total system RAM.
- **TIA chip** - Television Interface Adapter, generates video in real-time
- **No framebuffer** - You write to TIA registers as electron beam scans
- **"Racing the beam"** - Code executes scanline-by-scanline in sync with TV
- **Kernel programming** - Per-scanline code defining what appears on screen
- **Player/Missile graphics** - 2 players, 2 missiles, 1 ball, 1 playfield
- **Sprite reuse** - Change register mid-frame to show same sprite multiple times
- **Cartridge-based** - 2KB-4KB ROM typical, banking for larger games

## Showcase Philosophy

This is a **showcase curriculum** teaching the most extreme programming constraints in retro gaming:

Students learn:
- **What makes 2600 unique** - Kernel programming, racing the beam
- **Extreme resource management** - 128 bytes RAM, per-scanline code
- **Historical significance** - First successful home console, launched industry
- **Transfer from C64/NES** - Same CPU family, completely different approach

This is not comprehensive 6502 instruction (see C64/NES/BBC for that). This teaches 2600's unique kernel programming model.

## Curriculum Structure

### Phase 1: 6507 Assembly + TIA Programming (64 lessons, 2 games)

**Total:** 64 lessons across 2 tiers
**Outcome:** 2 complete original games showcasing 2600 constraints and techniques

### Tier Breakdown

**Tier 1 (L1-32):** Beam Breaker - Race the TV scan!
- 6507 fundamentals (6502 subset)
- 2600 memory map (TIA, RIOT, ROM)
- TV frame structure (VSYNC, VBLANK, visible, overscan)
- WSYNC - Sync with TV electron beam!
- Player graphics (paddle)
- Ball graphics
- Playfield (wall at top)
- Joystick input
- **Simple kernel** - Basic scanline routine, feel the beam racing
- **Playable:** Lesson 5 (paddle moves, ball bounces, see WSYNC in action)
- **Complete:** Lesson 9 (wall breaks, score, 128-byte RAM management)
- **Pattern focus:** Racing the beam fundamentals, per-scanline programming
- **2600 showcase:** Introduction to kernel programming - code runs in sync with TV!

**Tier 2 (L33-64):** Sprite Illusion - 3-5 enemies from 2 sprites!
- **Advanced kernel** - Different graphics per scanline
- Player ship (Player 0 sprite)
- Enemy formation (3-5 enemies from 2 player sprites!)
- **Sprite reuse magic** - Reposition sprites mid-frame
- Player shooting (missile)
- TIA hardware collision detection
- Wave progression (enemies move down)
- Score display (playfield digits)
- **128-byte RAM puzzle** - Every single byte accounted for
- **Playable:** Lesson 37 (shoot 3-5 enemies - all from 2 sprites!)
- **Complete:** Lesson 41 (waves, score, lives, full sprite reuse mastery)
- **Pattern focus:** Sprite reuse techniques, advanced kernel, extreme RAM management
- **2600 showcase:** Sprite reuse illusion - more objects than hardware allows!

## Original Games for Phase 1

All games are 100% original concepts designed to teach 2600 kernel programming progressively.

### 1. Beam Breaker (Tier 1, L1-32)
**Genre:** Ball-and-paddle game with TV beam synchronization
**Description:** Control paddle, break wall - but you're racing the TV electron beam! WSYNC makes it happen. Introduction to kernel programming.
**Technical focus:** WSYNC synchronization, basic kernel, TV frame structure, playfield, 128-byte RAM basics
**2600 showcase:** "Racing the beam" introduction - code runs in lockstep with TV scan, no framebuffer!
**Playable:** Lesson 5 | **Complete:** Lesson 9

### 2. Sprite Illusion (Tier 2, L33-64)
**Genre:** Fixed-screen shooter with sprite reuse magic
**Description:** Shoot 3-5 descending enemies - but there are only 2 player sprites! Sprite reuse creates the illusion. Ultimate 2600 challenge!
**Technical focus:** Advanced kernel (different every scanline), sprite reuse mid-frame, TIA collision hardware, extreme 128-byte RAM optimization
**2600 showcase:** Sprite reuse technique - show more objects than hardware allows, 128 bytes for EVERYTHING
**Playable:** Lesson 37 | **Complete:** Lesson 41

## What Students Master

### 6507 Assembly Essentials
- 6502 instruction set (6507 is subset)
- Register set (A, X, Y, SP, PC, P)
- Addressing modes (6507 supports same as 6502)
- Cycle counting (critical on 2600)
- Branch optimization
- Zero-page optimization

### Atari 2600 Hardware

**TIA (Television Interface Adapter):**
- VSYNC, VBLANK, WSYNC registers
- Player 0, Player 1 graphics
- Missile 0, Missile 1 graphics
- Ball graphics
- Playfield (20-bit asymmetric)
- Color registers (COLUP0, COLUP1, COLUPF, COLUBK)
- Collision detection (hardware registers)
- HMOVE (horizontal movement)

**RIOT (RAM-I/O-Timer):**
- 128 bytes RAM (all you get!)
- Joystick/paddle input
- Timer for intervals

**Memory Map:**
- $0000-$007F: TIA write registers
- $0080-$00FF: RAM (128 bytes)
- $0280-$0297: RIOT I/O and timer
- $F000-$FFFF: ROM (4KB typical, banked for larger)

### Racing the Beam

The defining 2600 technique:

**Frame Structure:**
```
VSYNC (3 scanlines) - Signal start of frame
VBLANK (37 scanlines) - Vertical blank, prepare data
Visible (192 scanlines) - RACE THE BEAM, draw graphics
Overscan (30 scanlines) - Bottom of frame
```

**Per-Scanline Code:**
- Each visible scanline: 76 cycles (NTSC)
- Must set TIA registers before electron beam draws that scanline
- WSYNC to wait for next scanline
- Code executes in lockstep with TV hardware

**Kernel Programming:**
- Write player graphics register before scanline draws
- Change colors per-scanline for multi-color sprites
- Reuse sprites by repositioning between scanlines
- No framebuffer - it's live video generation!

### Sprite Reuse

The 2600 has only 2 player sprites, but games show many objects:

**Technique:**
1. Draw sprite on scanline N
2. During scanline N's HBLANK, reposition sprite
3. Draw same sprite again on scanline N at new position
4. Can show 6-8 objects with careful timing

**Vertical Reuse:**
1. Draw alien row 1 on scanlines 10-20
2. Change player graphics register
3. Draw alien row 2 on scanlines 30-40
4. Show 10 aliens with 2 player sprites!

### Extreme RAM Management

128 bytes must hold:
- Player position, velocity
- Enemy positions (multiple enemies)
- Score, lives, level
- Temporary variables during kernel
- Stack space

**Techniques:**
- Bit packing (multiple flags in one byte)
- Reuse temporary variables
- Minimize stack usage
- Zero-page optimization
- Every byte carefully accounted for

### Playfield Techniques

20-bit playfield (40 bits with reflection):
- PF0 (4 bits, reversed)
- PF1 (8 bits, normal)
- PF2 (8 bits, reversed)
- Can be reflected or asymmetric

**Uses:**
- Maze walls
- Scrolling terrain
- Score display (playfield digits)
- Obstacles

### Cycle Counting

On 2600, cycles are everything:

- 76 cycles per scanline (NTSC)
- Must fit all register writes in that time
- WSYNC resets horizontal position
- Every instruction's cycle count matters
- Tables show instruction timing by addressing mode

Students learn to count cycles like second nature.

## The 2600 Challenge

This is the **hardest** retro platform:

**Why it's challenging:**
- No framebuffer to write to
- Code executes per-scanline in real-time
- 128 bytes RAM for everything
- Must understand TV timing intimately
- Cycle-perfect code required
- Every resource is precious

**Why it's rewarding:**
- Ultimate resource management
- Creative problem-solving required
- Historical significance (launched industry)
- Bragging rights (toughest retro platform)
- Deep understanding of how TVs work
- Appreciation for modern hardware

## Historical Significance

**Atari 2600 (1977-1992):**
- First successful home console
- 30 million units sold
- Launched video game industry
- "Golden age" classics: Pitfall, River Raid, Yars' Revenge
- Designed for simple games, programmers pushed it to limits
- Showcases raw ingenuity over hardware capability

**Design Constraints:**
- Designed for Pong-like games
- Never intended for complex games
- Programmers found creative ways around limits
- Racing the beam discovered by necessity
- Proved constraints drive innovation

## Transfer Knowledge

### From C64/NES/BBC Micro:
- 6502 instruction set knowledge transfers 100%
- But everything else is completely different
- Framebuffer-based thinking must be unlearned
- Per-scanline thinking replaces per-frame thinking

### To Other Platforms:
- Appreciate any platform with more than 128 bytes RAM!
- Scanline interrupt techniques (relevant on all platforms)
- Extreme optimization skills
- Creative problem-solving under constraints

## Comparison with Other Early Consoles

| Feature | Atari 2600 | Intellivision | ColecoVision |
|---------|------------|---------------|--------------|
| **Year** | 1977 | 1979 | 1982 |
| **CPU** | 6507 @ 1.19MHz | CP1610 @ 895kHz | Z80 @ 3.58MHz |
| **RAM** | 128 bytes | 1456 bytes | 1KB + 16KB VRAM |
| **Display** | Racing beam | 159×96 | 256×192 |
| **Sprites** | 5 max (with reuse) | 8 hardware | 32 hardware |
| **Difficulty** | Extreme | High | Moderate |
| **Innovation** | Kernel programming | Decent hardware | Near-arcade quality |

2600's legacy: proved programmers could overcome any constraint.

## Navigation

- **View all phases:** [`./`](./)
- **6502 references:** See C64/NES/BBC curriculum for comprehensive 6502 docs
- **Hardware references:** Coming soon (TIA, RIOT, memory map)
- **Documentation index:** [`../START-HERE.md`](../START-HERE.md)

---

**Last updated:** 2025-11-04
**Version:** 1.0
**Status:** Overview complete, tier details and individual lessons to be created
