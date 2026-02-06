# Phase 3: Firepower

**Game:** Starfield (C64 Game 1)
**Units:** 33–48
**Theme:** Power-ups make the player stronger
**6510 Focus:** Bit manipulation (AND/ORA/EOR), 16-bit arithmetic (ADC/SBC with carry), stack operations (PHA/PLA)
**Hardware:** Sprite slot allocation strategy, expanded SID usage
**Status:** Planned

---

## Overview

Phase 2 filled all 8 sprite slots with enemies. Phase 3 asks: what happens when you need another sprite for a power-up item? The answer is allocation — reuse a dead enemy's slot for the falling power-up, then reclaim it. The 8-sprite limit stops being a technical constraint and becomes a design challenge.

The 6510 focus moves to bit manipulation and 16-bit arithmetic. Power-up state is tracked with bit flags (AND/ORA to set and test). Timers use 16-bit subtraction (SBC with borrow across two bytes). Stack operations (PHA/PLA) preserve registers during state transitions.

By Unit 48, the player has meaningful choices: speed boost, rapid fire, spread shot, shield. Each power-up feels rewarding. The sprite budget is managed, not exceeded.

---

## Prerequisites from Phase 2

- All 8 sprite slots in active use — allocation thinking is now essential
- Data-driven design — power-up types follow the same table pattern as enemy types
- Wave system — power-up drop rates vary per wave
- Score system — power-ups interact with scoring

---

## Unit Progression

| Unit | Title | New 6510 Concept | Game Addition |
|------|-------|-----------------|---------------|
| 33 | Sprite Allocation Plan | Bit flags with `AND`/`ORA` for slot tracking | System design document |
| 34 | Power-Up Drops | Reuse dead enemy's sprite slot for collectible | Items appear on kill |
| 35 | Collect Power-Up | `PHA`/`PLA` for register preservation during transitions | System works |
| 36 | Speed Boost | Temporary state with frame countdown in zero page | Faster movement |
| 37 | Rapid Fire | Fire rate as variable, `DEC` timer per frame | Faster shooting |
| 38 | Power-Up Sound | SID voice 2, distinct waveform from laser/explosion | Satisfying pickup |
| 39 | Power-Up HUD | Character display update routine | Know what you have |
| 40 | Temporary Timer | 16-bit countdown with `SBC` and borrow | Power-ups expire |
| 41 | Timer Warning | Frame counter `AND` mask for blink rate | Know when it ends |
| 42 | Double Shot | Bullet pool expanded, shared update routine | Two bullets at once |
| 43 | Spread Shot | Velocity tables for angle offsets | Three-direction fire |
| 44 | Shield | State flag in zero page, absorbs one hit | Defensive option |
| 45 | Shield Visual | `$D027` colour change (no extra sprite needed) | See the protection |
| 46 | Shield Break | Combined SID + colour register feedback | Dramatic feedback |
| 47 | Drop Frequency Tuning | Probability per kill, wave-dependent rates | Balanced spawning |
| 48 | Integration + Balance | Sprite allocation audit, power-up playtesting | Rewarding loop |

---

## Key Teaching Moments

### Sprite Allocation (Unit 33)

With 8 sprite slots and more than 8 on-screen entities, allocation becomes a real problem. The solution: when an enemy dies, its sprite slot is temporarily repurposed for the falling power-up item. When the power-up is collected or falls off screen, the slot returns to the enemy pool. Bit flags track which slots are available — `AND` to test, `ORA` to claim, `EOR` or `AND #~bit` to release. This is resource management in 8 bits.

### Stack Operations (Unit 35)

Collecting a power-up triggers a state transition mid-frame: the enemy dies, the power-up activates, the score updates, a sound plays. Several routines need to run in sequence, each expecting different values in A, X, and Y. `PHA`/`PLA` (push/pull accumulator) preserve values across these calls. The stack has been implicitly used by `JSR`/`RTS` since Phase 1 — now it's explicitly managed.

### 16-Bit Arithmetic (Unit 40)

Power-up timers count down from values larger than 255 (e.g., 300 frames = 5 seconds at 60fps). This requires two bytes: a low byte and a high byte. `SBC` on the low byte may borrow from the high byte via the carry flag. The carry flag, previously just "something `SEC` sets before subtraction," becomes meaningful across multi-byte operations. This is the 6502's answer to 16-bit numbers on an 8-bit processor.

### Bit Masking for Blink (Unit 41)

`AND #$08` on a frame counter creates a 16-frame on/off cycle — the counter's bit 3 alternates every 8 frames. This is cheaper than any comparison-based blink timer: one instruction, no branches. The technique generalises to any power-of-two blink rate by changing the mask value.

---

## 6510 Concepts Introduced

1. `PHA` / `PLA` — push/pull accumulator to/from stack (Unit 35)
2. `TXA` / `TAX` / `TYA` / `TAY` — register transfers for stack save/restore (Unit 35)
3. Bit flags — `AND` to test, `ORA` to set, `EOR` to toggle (Unit 33)
4. 16-bit subtraction — `SBC` with borrow across two bytes (Unit 40)
5. Frame counter masking — `AND #mask` for power-of-two blink rates (Unit 41)
6. Velocity tables — pre-computed X/Y deltas for diagonal movement (Unit 43)

---

## Hardware Registers

### New in Phase 3

No new hardware registers — Phase 3 uses existing VIC-II and SID registers in more sophisticated ways. The key advance is *allocation strategy* for the 8 sprite slots, not new register access.

### Design Constraint

- Ship: sprite 0 (permanent)
- Bullet(s): sprite 1, optionally sprite 7 for double shot
- Enemies: sprites 2–6 (5 slots, down from 6 to free one for power-ups)
- Power-up item: borrows a killed enemy's slot temporarily

Shield uses sprite 0's colour change (no additional slot). Spread shot shares the bullet slot(s) with rapid cycling.

---

## Game State at Phase End

After Unit 48:

- **Power-ups** — speed boost, rapid fire, double shot, spread shot, shield
- **Temporary effects** — power-ups expire after ~5 seconds with visual warning
- **HUD** — shows active power-up type and remaining time
- **Sound** — distinct collect sound, shield break sound
- **Sprite budget** — managed dynamically: enemy slots borrowed for power-up items
- **Player agency** — meaningful choices about which power-ups to pursue

The game has depth beyond shooting. Players make decisions, manage timing, and feel rewarded.

---

## What Carries to Phase 4

- **Stack operations** — essential for interrupt handlers (must save/restore all registers)
- **Bit manipulation** — interrupt enable/acknowledge uses the same AND/ORA patterns
- **16-bit arithmetic** — timer calculations for raster interrupt timing
- **Sprite allocation** — Phase 4 adds enemy bullets, requiring further allocation discipline

---

**Version:** 1.0
**Last Updated:** 2026-02-06
