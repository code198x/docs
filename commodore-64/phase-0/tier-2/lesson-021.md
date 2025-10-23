# Lesson 021: Sprite Animation

**Arc:** Space Shooter Evolution
**Position:** Lesson 5 of 7 in arc
**Type:** Standard
**Estimated Completion:** 45 lines of code

## Learning Objectives

- Create multi-frame sprite animation
- Implement animation timing and frame switching
- Store multiple sprite frames in memory
- Apply animation to enemies and effects

## Prerequisites

**From Previous Lessons:**
- Sprite creation and display (L17-20)
- Multiple sprite shapes (L17)
- Timer/counter concepts (L15, L20)

**BASIC Knowledge:**
- Sprite pointers (2040-2047)
- Sprite data storage
- Frame timing

## Key Concepts Introduced

### Animation Frames
Store 2-4 different sprite shapes for each animated object. Switch between them over time to create animation.

### Frame Timing
Don't change frame every loop (too fast). Use counter: change frame every N loops for visible animation.

### Sprite Pointer Switching
Change sprite pointer (POKE 2040-2047) to switch which sprite shape displays. Shape data stays in memory, pointer changes.

### Animation State
Track current frame for each animated sprite: AF(sprite#) holds current frame number (0-3).

## Code Pattern

```basic
10 REM Store 3 enemy frames at blocks 13,14,15
20 FOR F=0 TO 2
30 FOR I=0 TO 62
40 READ B:POKE 832+(F*64)+I,B
50 NEXT I:NEXT F
60 DIM AF(3),AC(3):REM Anim frame, anim counter
70 REM Game loop
80 FOR I=1 TO 3
90 AC(I)=AC(I)+1
100 IF AC(I)>5 THEN AC(I)=0:AF(I)=AF(I)+1
110 IF AF(I)>2 THEN AF(I)=0
120 POKE 2040+I,13+AF(I):REM Switch sprite pointer
130 NEXT I
140 GOTO 80
1000 DATA [frame 0 sprite data - 63 bytes]
1100 DATA [frame 1 sprite data - 63 bytes]
1200 DATA [frame 2 sprite data - 63 bytes]
```

## Hardware Interaction

**Chips Involved:**
- **VIC-II** - Sprite display and pointers

**Memory Addresses:**
- `832-1087` (example) - Multiple sprite frames stored consecutively
- `2040-2047` ($07F8-$07FF) - Sprite pointers (switch these for animation)

## Common Pitfalls

1. **Animation too fast:** Changing every frame = blur; need timing counter
2. **Frame memory overlap:** Each frame needs 64 bytes (63 data + 1 padding)
3. **Pointer calculation wrong:** Block 13 = 832, block 14 = 896 (832+64)
4. **Not resetting frame:** AF goes beyond max frame, shows wrong sprite
5. **Memory conflicts:** Sprite data can't overlap with BASIC program or screen memory

## Extension Ideas

- Add explosion animation (4-frame burst)
- Animate player sprite (exhaust flames)
- Add idle vs moving animation states
- Create animated power-ups (rotating, pulsing)
- Add damage animation (flash different colours)
- Synchronize animation with sound

## Builds Toward

**In This Tier:**
- L22: Animated power-ups
- L23: Complete shooter with all animations

**In Next Tier:**
- Multi-state animation (idle/walk/jump) in L34
- 6-frame character animation in platformer

## Quick Reference

**Animation Frame Storage:**
```basic
REM Frame 0 at block 13 (832)
REM Frame 1 at block 14 (896)
REM Frame 2 at block 15 (960)
REM Frame 3 at block 16 (1024) - DANGER: screen memory!
```

**Frame Switching Pattern:**
```basic
10 AC=AC+1             :REM Animation counter
20 IF AC>5 THEN AC=0:AF=AF+1  :REM Change frame every 6 loops
30 IF AF>3 THEN AF=0   :REM Loop back to first frame
40 POKE 2040,13+AF     :REM Update sprite pointer
```

**Animation Speeds:**
- Every 2 frames: Very fast (30fps)
- Every 4-6 frames: Normal (10-15fps)
- Every 8-10 frames: Slow/smooth
- Every 15+ frames: Very slow

**Memory-Safe Sprite Blocks:**
```
Blocks 13-15: 832-1023 (safe, 3 frames)
Blocks 192-255: 12288+ (safe area, after BASIC)
```

See `/docs/VIC-II-QUICK-REFERENCE.md` for sprite memory map
