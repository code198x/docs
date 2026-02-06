# Phase 8: Salvation

**Game:** Exodus (Amiga Game 1)
**Units:** 113-128
**Theme:** Commercial release quality -- the complete game
**68000 Focus:** System restoration (Exec), memory management, disk I/O optimisation, code optimisation
**Hardware:** Exec library calls, system state save/restore
**Status:** Planned

---

## Overview

Phase 8 adds everything a commercial 1990 Amiga game would ship with: high scores, difficulty selection, a level editor preview, attract mode, and proper system restoration on exit. No new gameplay mechanics -- instead, every system from Phases 1-7 is polished, balanced, and integrated into a release-quality product.

System restoration is an Amiga-specific requirement. Unlike cartridge consoles, the Amiga runs an operating system. Taking over the hardware (Copper, Blitter, DMA, interrupts) means saving the system state first and restoring it when the game exits. A clean exit returns the user to Workbench without a reboot. This is professional Amiga development.

The game's completion: 30 levels with a full difficulty curve, themed music, attract mode, and a game that boots from disk and runs cleanly. The journey from a coloured screen (Unit 1) to a complete puzzle game (Unit 128) mirrors the learner's journey from zero 68000 knowledge to genuine Amiga programming competence.

---

## Prerequisites from Phase 7

- Complete game with all mechanics -- Phase 8 polishes, doesn't add
- MOD music engine with themed tracks
- 20+ levels with difficulty curve
- Optimised Blitter performance

---

## Unit Progression

| Unit | Title | New 68000 Concept | Game Addition |
|------|-------|-------------------|---------------|
| 113 | High Score Table | Multi-byte comparison, sorted insertion | Top 5 scores |
| 114 | Name Entry | Keyboard input via `rawkey` events, character display | Ownership |
| 115 | High Scores on Title | Display integration | Bragging rights |
| 116 | Difficulty Select | Menu system, mouse cursor navigation | Easy / Normal / Hard |
| 117 | Difficulty Affects Gameplay | Fewer abilities, faster timer, higher threshold | Real difference |
| 118 | Level Editor Preview | Simple mouse terrain paint | Creative mode |
| 119 | Two-Player Mode | Alternating turns, separate levels | Social play |
| 120 | Attract Mode | Auto-play demo showing a solution | Professional |
| 121 | Demo on Title Timeout | Timer-triggered state change | Shop display |
| 122 | Credits Screen | Scrolling text with Copper effects | Attribution |
| 123 | System Restoration | Save/restore Exec state, DMA, interrupts | **Clean exit** |
| 124 | Memory Audit | Chip RAM usage map, optimisation pass | Fits in 512KB |
| 125 | Disk Loading Optimisation | Fast loader, progress bar | Quick loads |
| 126 | 30 Levels Final Set | Full level pack with difficulty curve | Complete content |
| 127 | Final Testing | Edge cases, ability interactions, solvability | Release quality |
| 128 | **Complete Game** | Bootable ADF, documentation | **Ship it** |

---

## Key Teaching Moments

### System Restoration (Unit 123)

The Amiga has an operating system. Taking over the hardware means saving the state first:

```asm
; Save system state before taking over
    move.l 4.w,a6           ; ExecBase
    jsr _LVOForbid(a6)     ; Stop multitasking
    lea gfx_name,a1
    jsr _LVOOpenLibrary(a6)
    move.l d0,gfx_base

    ; Save the system Copper list
    move.l gfx_base,a0
    move.l gb_copinit(a0),old_copper

    ; Save DMA and interrupt state
    move.w $DFF01C,old_intena  ; INTENAR
    move.w $DFF002,old_dmacon  ; DMACONR

    ; ... take over hardware, run game ...

; Restore system state on exit
    move.w #$7FFF,$DFF096  ; Disable all DMA
    move.w #$7FFF,$DFF09A  ; Disable all interrupts
    move.w old_dmacon,d0
    or.w #$8000,d0
    move.w d0,$DFF096      ; Restore DMA
    move.w old_intena,d0
    or.w #$8000,d0
    move.w d0,$DFF09A      ; Restore interrupts
    move.l old_copper,$DFF080 ; Restore system Copper
    move.w #$0000,$DFF088  ; Restart Copper

    move.l 4.w,a6
    jsr _LVOPermit(a6)    ; Resume multitasking
```

Without this, exiting the game crashes the system. Every professional Amiga game saves and restores. Every demo that doesn't forces a reboot.

### Attract Mode (Unit 120)

Attract mode records mouse and keyboard input during a sample solution: each frame's input state stored in a buffer. During playback, the buffer replaces live input -- the game solves a level automatically. The recording is compressed (delta encoding: only store frames where input changes). The demo shows the game's mechanics to spectators -- important for shop displays and trade shows.

### Memory Audit (Unit 124)

The base Amiga 500 has 512KB of Chip RAM. All graphics, audio samples, Copper lists, and Blitter data must live here. Code can go in Fast RAM if available, but data cannot. The audit:

1. List every allocation: bitplanes (40KB for a 320x256 2-bitplane display), samples (~100KB for MOD instruments), Copper list (2KB), creature sprites (4KB), level data (20KB per level)
2. Total must fit in 512KB minus system overhead (~50KB)
3. If tight: compress samples, reduce level size, share instrument data between MODs

---

## 68000 Concepts Introduced

1. Exec library calls -- `OpenLibrary`, `Forbid`/`Permit` (Unit 123)
2. System state save/restore -- DMA, interrupts, Copper list (Unit 123)
3. Keyboard input via raw key codes -- character mapping (Unit 114)
4. Delta-encoded input recording -- compressed attract mode data (Unit 120)
5. Chip RAM allocation tracking -- systematic memory audit (Unit 124)
6. Disk loading optimisation -- batch reads, DMA-aware scheduling (Unit 125)

---

## Hardware

### New in Phase 8

| Resource | Purpose | Introduced |
|----------|---------|------------|
| Exec library (4.w) | Operating system calls for clean startup/shutdown | Unit 123 |
| INTENAR ($DFF01C) | Read current interrupt enable state | Unit 123 |
| DMACONR ($DFF002) | Read current DMA enable state | Unit 123 |

---

## Game State at Phase End

After Unit 128 -- the complete game:

- **High scores** -- top 5 with names, sorted, displayed on title
- **Difficulty** -- Easy/Normal/Hard with menu selection
- **Two-player** -- alternating turns with separate levels
- **Attract mode** -- auto-solve demo after title timeout
- **Level editor** -- simple terrain paint for experimentation
- **Credits screen** -- scrolling text with Copper effects
- **System restoration** -- clean exit to Workbench
- **30 levels** -- full difficulty curve across grass, snow, cave, desert themes
- **7 abilities** -- Dig, Build, Redirect, Pause, Climb, Float, Explode
- **Terrain types** -- dirt, rock, steel, water, conveyors, teleporters
- **Chain reactions** -- cascading ability combinations
- **Full audio** -- 4-channel MOD music, themed tracks, crafted SFX
- **Full visuals** -- Copper gradient skies, parallax, themed palettes, animations
- **Password system** -- level progress persistence
- **Bootable ADF** -- runs from disk, no installation needed

A game worthy of an Amiga Power review. Bootable, polished, and professional.

---

## Quality Comparison Across All Phases

| Aspect | Phase 1 | Phase 4 | Phase 8 |
|--------|---------|---------|---------|
| Graphics | 1-bitplane terrain, hardware sprites | + multi-bitplane types | Gradient skies, parallax, themed art |
| World | 1 level | 8+ levels, terrain types | 30 levels, full difficulty curve |
| Creatures | Walk + fall | + crowd AI, step-up | 30+ per level, animation, pathfinding |
| Abilities | None | Dig + Build + Redirect + 4 more | All abilities, chain reactions, combos |
| Audio | One sample | + effect library | Full MOD music, themed tracks, SFX |
| Features | Walk to exit | + passwords, timer, types | High scores, attract, 2-player, editor |
| 68000 Skill | MOVE, BSR, branches | + Blitter, LEA, disk I/O | Full chipset, Exec, system restoration |

---

## What This Game Teaches

By completing Exodus, learners are ready for:

- **Signal (Game 2)** -- Blitter BOB rendering transfers to lane-crossing objects. Copper screen split reused for HUD
- **Shatter Point (Game 3)** -- Blitter fills become brick rendering. Ball physics builds on creature position tracking
- **Ascent (Game 4)** -- cookie-cut masking becomes platformer rendering. Gravity builds on creature fall physics
- **Parallax (Game 9)** -- Copper display list skills enable multi-layer parallax. Blitter performance awareness enables smooth scrolling
- **Every future game** -- the Copper list framework, Blitter operation patterns, Paula audio engine, and system restoration from Exodus are reused throughout

Exodus isn't just Game 1. It's the foundation for the entire Amiga curriculum.

---

**Version:** 1.0
**Last Updated:** 2026-02-06
