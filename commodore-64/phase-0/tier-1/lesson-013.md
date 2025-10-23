# Lesson 013: Falling Stars

**Arc:** Dodge & Catch
**Position:** Lesson 2 of 3 in arc
**Type:** Standard
**Estimated Completion:** 40 lines of code

## Learning Objectives

- Create moving objects with independent behaviour
- Use arrays to track multiple objects
- Implement simple gravity/falling mechanics
- Add randomization for variety

## Prerequisites

**From Previous Lessons:**
- Character movement (L12)
- Arrays (L5)
- Random numbers (L3)
- Screen memory (L8)

**BASIC Knowledge:**
- Arrays with DIM
- RND for randomization
- Screen position calculations
- Erase-move-draw pattern

## Key Concepts Introduced

### Object Arrays
Track multiple objects using parallel arrays: FX() for X position, FY() for Y position. Each array index represents one object.

### Automatic Movement
Unlike player (controlled by input), falling objects update position automatically each frame. This creates dynamic environments.

### Object Spawning
Generate new objects at top of screen with random X positions. When object reaches bottom, respawn it at top.

## Code Pattern

```basic
10 DIM FX(5),FY(5)
20 FOR I=1 TO 5
30 FX(I)=INT(RND(1)*40):FY(I)=0
40 NEXT I
50 REM Game loop
60 FOR I=1 TO 5
70 REM Erase old position
80 POKE 1024+(FY(I)*40)+FX(I),32
90 REM Move down
100 FY(I)=FY(I)+1
110 REM Respawn at top if hit bottom
120 IF FY(I)>24 THEN FY(I)=0:FX(I)=INT(RND(1)*40)
130 REM Draw new position
140 POKE 1024+(FY(I)*40)+FX(I),42
150 NEXT I
160 GOTO 60
```

## Hardware Interaction

**Chips Involved:**
- **VIC-II** - Screen display

**Memory Addresses:**
- `1024-2023` - Screen memory for objects and player

## Common Pitfalls

1. **Array size mismatch:** DIM FX(5) but loop to 6 = crash
2. **Not erasing before moving:** Objects leave trails
3. **Respawn without randomization:** All objects in same column
4. **Speed too fast:** Need delay in main loop or objects blur
5. **Forgetting bounds check:** FY can exceed 24 causing wrong screen positions

## Extension Ideas

- Vary falling speeds (some objects faster than others)
- Add different object types (stars, asteroids, coins)
- Add horizontal movement (objects drift left/right while falling)
- Increase difficulty over time (add more objects, increase speed)
- Add object colours using colour memory

## Builds Toward

**In This Tier:**
- L14: Add player collision detection with falling objects
- L14: Add scoring for catching vs dodging objects

**In Next Tier:**
- Sprite-based falling objects (smoother animation)
- Bullet systems (rising objects)
- Enemy movement patterns

## Quick Reference

**Object Array Pattern:**
```basic
10 DIM OX(N),OY(N)  :REM Position arrays
20 FOR I=1 TO N     :REM Initialize
30 OX(I)=...:OY(I)=...
40 NEXT I
```

**Update Loop:**
```basic
100 FOR I=1 TO N
110 POKE 1024+(OY(I)*40)+OX(I),32  :REM Erase
120 REM Update position
130 IF [out of bounds] THEN [respawn]
140 POKE 1024+(OY(I)*40)+OX(I),C   :REM Draw
150 NEXT I
```

**Respawn Pattern:**
```basic
100 IF Y>24 THEN Y=0:X=INT(RND(1)*40)
```

**Multiple Object Management:**
- Use parallel arrays (one index = one object)
- Loop through all objects each frame
- Erase-update-draw for each object
- Handle respawning when out of bounds

**Typical Object Counts:**
- 3-5 objects: Easy to track, good for beginners
- 8-10 objects: Busier screen, more challenge
- 15+ objects: Starts to slow down in BASIC
