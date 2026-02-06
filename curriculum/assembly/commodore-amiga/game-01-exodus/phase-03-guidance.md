# Phase 3: Guidance

**Game:** Exodus (Amiga Game 1)
**Units:** 33-48
**Theme:** Player interaction -- selecting creatures, assigning abilities, UI panel
**68000 Focus:** MOVEM for register save/restore, BTST for input, subroutine parameter patterns, DBRA loops
**Hardware:** Mouse input (JOY0DAT $DFF00A, CIAA PRA), Copper screen split
**Status:** Planned

---

## Overview

Phase 3 gives the player control. A mouse cursor selects individual creatures. Clicking an ability icon in the UI panel, then clicking a creature, assigns that ability. The Copper splits the screen: gameplay area above, UI panel below -- different bitplane pointers, different colours, different scroll positions.

Four new abilities join the existing three: Pause (stop a creature, blocking others), Climb (ascend vertical surfaces), Float (reduced gravity for safe descent), and Explode (sacrifice a creature to blast terrain). The explode ability is the signature Lemmings-style mechanic: strategic sacrifice.

Release rate control lets the player speed up or slow down creature spawning. A countdown timer adds urgency. By the end of Phase 3, the puzzle game is fully interactive.

---

## Prerequisites from Phase 2

- Blitter terrain modification (dig, build, redirect)
- Cookie-cut BOB rendering
- Multiple creatures with ability state
- Paula sample playback

---

## Unit Progression

| Unit | Title | New 68000 Concept | Game Addition |
|------|-------|-------------------|---------------|
| 33 | Mouse Input | `JOY0DAT` ($DFF00A), button via CIAA PRA ($BFE001) | Cursor movement |
| 34 | Cursor Sprite | Hardware sprite follows mouse position | Visible cursor |
| 35 | Creature Selection | Click near creature, proximity check, highlight | **Direct interaction** |
| 36 | Ability Assignment | Click icon, then click creature | Dig/Build/Redirect |
| 37 | Copper Screen Split | WAIT at panel line, change colours/bitplanes | Gameplay + UI panel |
| 38 | UI Panel Layout | Ability icons, creature count, timer | Information display |
| 39 | Ability Icons (BOBs) | Blitter-drawn icons in panel area | Clickable buttons |
| 40 | Pause Ability | Creature stops, blocks others | Traffic jam control |
| 41 | Climb Ability | Creature ascends vertical surfaces | Vertical movement |
| 42 | Float Ability | Reduced gravity (slow fall) | Safe descent |
| 43 | Explode Ability | Creature destroys terrain in radius | **Sacrifice play** |
| 44 | Selection Highlight | Sprite flash or colour change on selected | Clear feedback |
| 45 | Release Rate Control | Speed up/slow down spawn rate | Timing control |
| 46 | Nuke Button | Explode all creatures (give up) | Reset option |
| 47 | Timer Display | Countdown, level fails when expired | Time pressure |
| 48 | Integration + UI Polish | Click accuracy, feedback, layout | Usable interface |

---

## Key Teaching Moments

### Mouse Input (Unit 33)

The Amiga mouse connects to joystick port 0. Position changes are read from `JOY0DAT` ($DFF00A) -- a register that encodes X and Y movement as 8-bit counters. The trick: read the difference from the previous frame's value, handling wrap-around:

```asm
; Read mouse X movement
    move.w $DFF00A,d0   ; JOY0DAT
    move.b d0,d1        ; X counter (low byte)
    sub.b old_mouse_x,d1 ; Delta since last frame
    ext.w d1            ; Sign-extend to word
    add.w d1,cursor_x   ; Move cursor
    move.b d0,old_mouse_x ; Save for next frame
```

Buttons are on CIAA PRA ($BFE001): bit 6 = left button (active low), bit 2 = right button (active low via joy port).

### Copper Screen Split (Unit 37)

The Copper WAITs for the panel's starting raster line, then changes the display:

```asm
; Copper list: split screen at line $C0
    ; ... gameplay bitplane pointers and colours above ...

    dc.w $C001,$FFFE    ; WAIT for line $C0
    dc.w $0100,$2200    ; BPLCON0: 2 bitplanes for panel
    dc.w $00E0,$0000    ; BPL1PTH: panel bitplane 1
    dc.w $00E2,$0000    ; BPL1PTL
    dc.w $0180,$0222    ; COLOR00: dark grey panel background
    dc.w $0182,$0FFF    ; COLOR01: white text
    dc.w $0184,$0F80    ; COLOR02: orange icons
    dc.w $0186,$00F0    ; COLOR03: green highlights
```

Above the split: terrain and creatures. Below: the UI panel with ability icons, counters, and timer. Two independent displays from one Copper list.

### Explode Ability (Unit 43)

The explode ability clears a circular area of terrain. A pre-calculated circular mask stored in memory is used with the Blitter to clear the matching pixels in the terrain bitplane. The Blitter's masked clear operation: where the mask is 1, clear the terrain (set to 0); where 0, leave terrain intact. The sacrificed creature is removed. Terrain vanishes, other creatures fall through.

---

## 68000 Concepts Introduced

1. `MOVEM` -- save/restore multiple registers on subroutine entry/exit (Unit 33)
2. Mouse delta calculation -- counter subtraction with sign extension (Unit 33)
3. CIAA PRA register -- button state via CIA chip at $BFE001 (Unit 33)
4. Copper WAIT instruction -- synchronise to raster line (Unit 37)
5. `DBRA` -- decrement and branch loop (replaces `DEX`/`BNE` from 6502) (Unit 38)
6. Proximity check -- `SUB.W` + `CMP.W` for click-near-creature (Unit 35)
7. `EXT.W` -- sign-extend byte to word for signed arithmetic (Unit 33)
8. Blitter masked operations -- combining mask with clear for circular destruction (Unit 43)

---

## Hardware

### New in Phase 3

| Register | Address | Purpose | Introduced |
|----------|---------|---------|------------|
| JOY0DAT | $DFF00A | Mouse/joystick port 0 position counters | Unit 33 |
| CIAA PRA | $BFE001 | Mouse buttons (active low) | Unit 33 |
| Copper WAIT | (list data) | Synchronise to raster position | Unit 37 |

---

## Game State at Phase End

After Unit 48:

- **Mouse cursor** -- hardware sprite tracks mouse movement
- **Creature selection** -- click near a creature to select it
- **7 abilities** -- Dig, Build, Redirect, Pause, Climb, Float, Explode
- **Ability assignment** -- click icon, then click creature
- **Copper screen split** -- gameplay above, UI panel below
- **UI panel** -- ability icons, creature counter, timer display
- **Ability limits** -- finite per level, displayed in panel
- **Release rate** -- adjustable creature spawn speed
- **Nuke** -- panic button to restart
- **Timer** -- countdown for level completion
- **Selection highlight** -- visual feedback on selected creature

The puzzle game is fully interactive. All abilities work, the UI is usable, time pressure creates urgency.

---

## What Carries to Phase 4

- **Mouse input** -- used for level select, menus, and editor
- **Copper screen split** -- permanent fixture for all game states
- **UI rendering** -- panel updated with level-specific information
- **Ability system** -- extended with terrain type interactions

---

**Version:** 1.0
**Last Updated:** 2026-02-06
