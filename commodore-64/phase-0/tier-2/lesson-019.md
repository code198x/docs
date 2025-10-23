# Lesson 019: Shooting Gallery

**Arc:** Space Shooter Evolution
**Position:** Lesson 3 of 7 in arc
**Type:** Standard
**Estimated Completion:** 50 lines of code

## Learning Objectives

- Implement bullet system using sprites
- Detect hardware sprite collision
- Add fire button handling
- Create shooting gameplay mechanics

## Prerequisites

**From Previous Lessons:**
- Sprite creation (L17)
- Joystick input (L18)
- Arrays for multiple objects (L13)
- Collision detection concepts (L14)

**BASIC Knowledge:**
- Sprite positioning
- Joystick reading
- Arrays for bullet tracking
- PEEK for collision registers

## Key Concepts Introduced

### Bullet Management
Use arrays to track active bullets: BX(), BY(), BA() (active flag). Update all active bullets each frame.

### Hardware Collision Detection
VIC-II automatically detects sprite-sprite and sprite-background collisions. Read collision registers instead of manual position checking.

### Fire Rate Control
Prevent continuous firing by checking time since last shot or using cooldown counter.

### Multiple Sprites
Player=sprite 0, bullets=sprites 1-4, targets=sprites 5-7. Manage sprite allocation carefully.

## Code Pattern

```basic
10 DIM BX(4),BY(4),BA(4):REM Bullet arrays
20 DIM TX(3),TY(3):REM Target positions
30 SC=0:REM Score
40 REM Initialize targets
50 FOR I=1 TO 3:TX(I)=INT(RND(1)*280)+20:TY(I)=50:NEXT I
60 REM Game loop
70 J=PEEK(56320)
80 REM Move player (sprite 0)
90 REM Fire button check
100 IF (J AND 16)=0 AND FC=0 THEN GOSUB 1000:FC=10
110 IF FC>0 THEN FC=FC-1
120 REM Update bullets
130 FOR I=1 TO 4
140 IF BA(I)=1 THEN BY(I)=BY(I)-4:POKE 53250+I*2,BX(I):POKE 53251+I*2,BY(I)
150 IF BY(I)<50 THEN BA(I)=0:POKE 53269,PEEK(53269) AND (255-2^I)
160 NEXT I
170 REM Check collisions
180 C=PEEK(53279):IF C>0 THEN GOSUB 2000
190 GOTO 70
1000 REM Fire bullet
1010 FOR I=1 TO 4:IF BA(I)=0 THEN BA(I)=1:BX(I)=SX:BY(I)=SY:RETURN
1020 NEXT I:RETURN
2000 REM Collision handler
2010 SC=SC+10:POKE 53279,0:REM Clear collision register
2020 RETURN
```

## Hardware Interaction

**Chips Involved:**
- **VIC-II** - Sprite positioning and collision detection

**Memory Addresses:**
- `53279` ($D01F) - Sprite-sprite collision register
- `53278` ($D01E) - Sprite-background collision register
- `53269` ($D015) - Sprite enable register
- `53248-53264` - Sprite position registers

## Common Pitfalls

1. **Collision register not cleared:** Must POKE 0 to collision register after reading
2. **Running out of bullets:** Need to check bullet availability before firing
3. **Sprite enable confusion:** Must enable/disable sprites as bullets activate/deactivate
4. **Fire rate too fast:** Need cooldown or will spawn bullets every frame
5. **Array bounds:** Only 8 sprites total, allocate wisely

## Extension Ideas

- Add multiple bullet types (rapid fire, spread shot)
- Add bullet lifetime (auto-deactivate after distance)
- Add moving targets
- Add sound effects for shooting and hits
- Add bullet-target collision scoring
- Add ammo limit system

## Builds Toward

**In This Tier:**
- L20: Enemy bullets (reverse direction)
- L21: Animated sprites for bullets and effects
- L23: Complete shooter with all weapon systems

## Quick Reference

**Sprite-Sprite Collision:**
```basic
10 C=PEEK(53279)      :REM Read collision register
20 IF C>0 THEN [collision occurred]
30 POKE 53279,0       :REM Clear register
```

**Sprite Enable/Disable:**
```basic
REM Enable sprite N
POKE 53269,PEEK(53269) OR 2^N

REM Disable sprite N
POKE 53269,PEEK(53269) AND (255-2^N)
```

**Bullet Pool Pattern:**
```basic
10 DIM BX(N),BY(N),BA(N)  :REM Position + active
20 REM Find inactive bullet
30 FOR I=1 TO N
40 IF BA(I)=0 THEN [use this slot]:RETURN
50 NEXT I
```

**Fire Rate Control:**
```basic
10 IF FIRE AND FC=0 THEN GOSUB [shoot]:FC=10
20 IF FC>0 THEN FC=FC-1
REM FC=cooldown counter, prevents rapid fire
```

**Sprite Allocation Example:**
```
Sprite 0: Player
Sprites 1-4: Player bullets
Sprites 5-7: Enemies
```

**Collision Bit Decoding:**
```
Bit 0 = Sprite 0 collided
Bit 1 = Sprite 1 collided
...decode which sprites involved
```

See `/docs/VIC-II-QUICK-REFERENCE.md` for complete collision documentation
