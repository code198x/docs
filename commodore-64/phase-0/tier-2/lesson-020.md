# Lesson 020: Enemy Movement

**Arc:** Space Shooter Evolution
**Position:** Lesson 4 of 7 in arc
**Type:** Standard
**Estimated Completion:** 60 lines of code

## Learning Objectives

- Implement AI movement patterns for enemies
- Create enemy bullets moving opposite direction
- Add enemy-player collision detection
- Design engaging enemy behaviors (patterns, formations)

## Prerequisites

**From Previous Lessons:**
- Sprite management (L17-19)
- Collision detection (L19)
- Arrays for multiple objects (L13, L19)

**BASIC Knowledge:**
- Sprite positioning
- Collision registers
- Pattern-based movement

## Key Concepts Introduced

### AI Movement Patterns
Simple patterns create interesting enemies: sine wave (side-to-side), dive attack (toward player), circle formation, zigzag descent.

### Enemy State Machine
Each enemy has state: moving, attacking, destroyed. State determines behavior each frame.

### Enemy Bullets
Similar to player bullets but move downward. Require separate sprite allocation and tracking arrays.

### Formation Management
Position enemies relative to each other (formations) or independently (random swarms).

## Code Pattern

```basic
10 DIM EX(3),EY(3),EP(3):REM Enemy position + pattern
20 DIM EBX(4),EBY(4),EBA(4):REM Enemy bullets
30 REM Initialize enemies
40 FOR I=1 TO 3:EX(I)=I*80:EY(I)=60:EP(I)=I:NEXT I
50 REM Game loop
60 REM Update enemies
70 FOR I=1 TO 3
80 IF EP(I)=1 THEN EX(I)=EX(I)+SIN(T/10)*2:REM Sine wave
90 IF EP(I)=2 THEN EY(I)=EY(I)+1:REM Descend
100 IF EP(I)=3 THEN EX(I)=EX(I)-1:REM Drift left
110 POKE 53250+I*2,EX(I):POKE 53251+I*2,EY(I)
120 IF RND(1)<0.02 THEN GOSUB 1000:REM Enemy fires
130 NEXT I
140 T=T+1:REM Time for patterns
150 REM Update enemy bullets (move down)
160 FOR I=1 TO 4
170 IF EBA(I)=1 THEN EBY(I)=EBY(I)+3
180 IF EBY(I)>229 THEN EBA(I)=0
190 NEXT I
200 GOTO 60
1000 REM Enemy fire bullet
1010 FOR J=1 TO 4:IF EBA(J)=0 THEN EBA(J)=1:EBX(J)=EX(I):EBY(J)=EY(I):RETURN
1020 NEXT J:RETURN
```

## Hardware Interaction

**Chips Involved:**
- **VIC-II** - Sprite positioning and collision

**Memory Addresses:**
- Sprite positions: `53248-53264`
- Collision registers: `53278-53279`

## Common Pitfalls

1. **Running out of sprites:** Player + player bullets + enemies + enemy bullets = all 8 sprites quickly
2. **Pattern timing:** Need counter/timer for smooth patterns (not just frame count)
3. **Overlapping enemies:** Multiple enemies same position looks wrong
4. **Fire rate too high:** Random firing needs low probability (< 0.05)
5. **No enemy removal:** Destroyed enemies should be deactivated or respawned

## Extension Ideas

- Add different enemy types (behaviors)
- Add enemy health (multiple hits to destroy)
- Add boss enemies (larger, complex patterns)
- Add enemy formations (V-shape, waves)
- Enemies drop power-ups when destroyed
- Add enemy animation (preview L21)

## Builds Toward

**In This Tier:**
- L21: Animated enemy sprites
- L22: Power-ups and advanced mechanics
- L23: Complete shooter synthesis

## Quick Reference

**Simple AI Patterns:**
```basic
REM Sine wave (side-to-side)
EX=EX+SIN(T/10)*2

REM Dive toward player
IF EX<PX THEN EX=EX+1 ELSE EX=EX-1
EY=EY+2

REM Circle pattern
EX=CX+COS(T/20)*50
EY=CY+SIN(T/20)*50

REM Zigzag
EY=EY+1
IF T MOD 30<15 THEN EX=EX+1 ELSE EX=EX-1
```

**Enemy State Machine:**
```basic
10 ES=0  :REM 0=inactive, 1=moving, 2=attacking, 3=destroyed
20 IF ES=1 THEN [movement pattern]
30 IF ES=2 THEN [attack pattern]
40 IF ES=3 THEN [explosion animation]
```

**Random Firing:**
```basic
10 IF RND(1)<0.02 THEN GOSUB [fire]
REM 2% chance per frame = ~1 shot/second at 60fps
```

See `/docs/VIC-II-QUICK-REFERENCE.md` for sprite management
