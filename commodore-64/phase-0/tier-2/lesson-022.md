# Lesson 022: Power-Up System

**Arc:** Space Shooter Evolution
**Position:** Lesson 6 of 7 in arc
**Type:** Standard
**Estimated Completion:** 55 lines of code

## Learning Objectives

- Implement collectible power-up system
- Add weapon upgrades and temporary effects
- Create visual feedback for power-up state
- Design balanced power-up mechanics

## Prerequisites

**From Previous Lessons:**
- Collision detection (L19)
- Sprite animation (L21)
- Multiple game systems integration (L20)

**BASIC Knowledge:**
- Sprite collision registers
- State variables
- Timer-based effects

## Key Concepts Introduced

### Collectible Items
Spawn power-ups on screen (sprites). Detect player collision, apply effect, remove sprite.

### Weapon Upgrades
Track weapon level (WL variable): 1=single shot, 2=double shot, 3=spread shot. Fire behavior changes based on level.

### Temporary Effects
Shield power-up: set timer (ST), while ST>0 player is invincible. Decrement each frame.

### Visual Power-Up States
Change player sprite colour or animation when powered up. Player needs visual feedback.

## Code Pattern

```basic
10 WL=1:ST=0:REM Weapon level, shield timer
20 DIM PX(3),PY(3),PT(3),PA(3):REM Powerup X,Y,type,active
30 REM Spawn power-up
40 IF RND(1)<0.005 THEN GOSUB 1000
50 REM Update power-ups
60 FOR I=1 TO 3
70 IF PA(I)=1 THEN PY(I)=PY(I)+1
80 IF PY(I)>229 THEN PA(I)=0
90 REM Check player collision
100 IF ABS(PX(I)-SX)<16 AND ABS(PY(I)-SY)<16 THEN GOSUB 2000
110 NEXT I
120 REM Shield timer
130 IF ST>0 THEN ST=ST-1:POKE 53287,3:REM Cyan when shielded
140 IF ST=0 THEN POKE 53287,1:REM White when normal
150 GOTO 50
1000 REM Spawn power-up
1010 FOR I=1 TO 3:IF PA(I)=0 THEN PA(I)=1:PX(I)=INT(RND(1)*280)+20:PY(I)=50:PT(I)=INT(RND(1)*3)+1:RETURN
1020 NEXT I:RETURN
2000 REM Collect power-up
2010 IF PT(I)=1 THEN WL=WL+1:IF WL>3 THEN WL=3
2020 IF PT(I)=2 THEN ST=300:REM 5 seconds shield
2030 IF PT(I)=3 THEN SC=SC+100:REM Score bonus
2040 PA(I)=0:GOSUB 3000:REM Sound effect
2050 RETURN
3000 REM Powerup sound
3010 [Sound effect from L11]
3020 RETURN
```

## Hardware Interaction

**Chips Involved:**
- **VIC-II** - Sprite collision and colour changes
- **SID** - Power-up sound effects

**Memory Addresses:**
- `53279` - Sprite-sprite collision
- `53287-53294` - Sprite colours for visual feedback

## Common Pitfalls

1. **Weapon level overflow:** WL can exceed max (cap at maximum)
2. **Shield never expires:** Must decrement timer each frame
3. **Collision too precise:** Use range check (ABS(PX-SX)<16) not exact match
4. **Power-up overload:** Too many power-ups = game too easy
5. **No visual feedback:** Player doesn't know shield is active

## Extension Ideas

- Add rapid-fire power-up (reduce fire cooldown)
- Add bomb/screen-clear power-up
- Add extra life power-up
- Display power-up duration (shield meter)
- Add power-up downgrade on hit
- Add power-up combos (collect 3 same type = mega upgrade)

## Builds Toward

**In This Tier:**
- L23: Complete shooter integrates all power-ups

**In Next Tier:**
- Complex upgrade systems in larger games

## Quick Reference

**Weapon Level System:**
```basic
10 WL=1  :REM Current weapon level
20 REM Fire pattern based on level
30 IF WL=1 THEN [single bullet]
40 IF WL=2 THEN [double bullet]
50 IF WL=3 THEN [triple spread]
```

**Temporary Effect Pattern:**
```basic
10 ST=300  :REM Shield timer (5 sec at 60fps)
20 IF ST>0 THEN ST=ST-1:REM Decrement
30 IF ST>0 THEN [apply shield effect]
```

**Power-Up Types:**
- Type 1: Weapon upgrade
- Type 2: Shield/invincibility
- Type 3: Score bonus
- Type 4: Speed boost
- Type 5: Extra life

**Collision Range Check:**
```basic
IF ABS(PX-SX)<16 AND ABS(PY-SY)<16 THEN COLLISION
REM 16 = sprite half-width, allows near-miss forgiveness
```

**Visual Feedback:**
```basic
REM Shield active
IF ST>0 THEN POKE 53287,3:REM Cyan player

REM Weapon level indicator
POKE 1024,WL+48:REM Show number on screen
```
