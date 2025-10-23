# Lesson 034: Advanced Animation

**Arc:** Platform Adventure
**Position:** Lesson 2 of 7 in arc
**Type:** Standard
**Estimated Completion:** 60 lines of code

## Learning Objectives

- Implement multi-state character animation (idle, walk, jump)
- Create smooth animation frame cycling
- Synchronize animation with character state
- Build animation system for platformer games

## Prerequisites

**From Previous Lessons:**
- Platform basics with gravity and jumping (L33)
- Sprite control and positioning (L17-23)
- Frame-based animation concepts (L21)

**BASIC Knowledge:**
- Sprite pointer manipulation
- State tracking with variables
- Frame counter management

## Key Concepts Introduced

### Animation State Machine
Track character state (ST): 0=idle, 1=walking, 2=jumping, 3=falling. Each state has its own animation frames.

### Frame Cycling
Use frame counter (FC) to cycle through animation frames at controlled speed. Increment FC each loop, change sprite when FC reaches threshold.

### State-Based Frame Selection
Different states use different sprite ranges. Idle uses frames 13-14, walking uses frames 15-18, jumping uses frame 19, falling uses frame 20.

### Animation Timing
Control animation speed independently from movement speed. FC threshold determines how many game loops per animation frame (FC MOD 5 = animation every 5 frames).

## Code Pattern

```basic
10 SX=160:SY=150:VX=0:VY=0:GR=0:ST=0:FC=0
20 GRAV=0.2:JMP=-3:SPWALK=15:SPJUMP=19:SPFALL=20
30 REM Platform setup
40 PX=100:PY=180:PW=80
50 POKE 53269,1:POKE 53287,1
60 REM Main loop
70 J=PEEK(56320):FC=FC+1
80 REM Movement input
90 VX=0
100 IF (J AND 4)=0 THEN VX=-2
110 IF (J AND 8)=0 THEN VX=2
120 REM Jump input
130 IF (J AND 16)=0 AND GR=1 THEN VY=JMP:GR=0
140 REM Apply gravity
150 VY=VY+GRAV
160 SX=SX+VX:SY=SY+VY
170 REM Platform collision
180 GR=0
190 IF SX>PX-12 AND SX<PX+PW+12 THEN
200 IF SY>PY-21 AND SY<PY AND VY>0 THEN SY=PY-21:VY=0:GR=1
210 IF SY>200 THEN SY=200:VY=0:GR=1
220 REM Determine animation state
230 IF GR=0 AND VY<0 THEN ST=2:REM Jumping
240 IF GR=0 AND VY>0 THEN ST=3:REM Falling
250 IF GR=1 AND VX<>0 THEN ST=1:REM Walking
260 IF GR=1 AND VX=0 THEN ST=0:REM Idle
270 REM Update animation frame
280 IF ST=0 THEN SP=13+(FC/10) AND 1:REM Idle (2 frames)
290 IF ST=1 THEN SP=SPWALK+(FC/5) AND 3:REM Walk (4 frames)
300 IF ST=2 THEN SP=SPJUMP:REM Jump (1 frame)
310 IF ST=3 THEN SP=SPFALL:REM Fall (1 frame)
320 POKE 2040,SP
330 REM Update sprite position
340 POKE 53248,SX:POKE 53249,SY
350 GOTO 70
```

## Hardware Interaction

**Chips Involved:**
- **VIC-II** - Sprite display, sprite pointer updates
- **CIA** - Joystick input reading

**Memory Addresses:**
- 2040 ($07F8) - Sprite 0 pointer (changes each frame)
- 53248-53249 ($D000-$D001) - Sprite X/Y position
- Multiple sprite data blocks (13-20) for animation frames

## Common Pitfalls

1. **Animation too fast:** FC incrementing too quickly makes animation jerky
2. **Wrong frame range:** Using AND 3 with only 2 frames shows garbage sprites
3. **State detection order:** Must check jumping before falling (VY<0 before VY>0)
4. **No idle animation:** Character freezes when stopped instead of subtle animation
5. **Sprite data not defined:** Using sprite pointers without designing sprite graphics

## Extension Ideas

- Add turning animation (left vs right facing)
- Add landing animation (brief squat when hitting ground)
- Add running animation (faster than walking, triggered by double-tap)
- Add crouching animation (down button when on ground)
- Add climbing animation (for ladder interaction)
- Add attack animation (fire button when grounded)

## Builds Toward

**In This Tier:**
- L35: Level design using data-driven approach
- L36: Enemy sprites with their own animation states
- L37: Collectible sprites with idle animations
- L39: Complete platformer with polished character animation

## Quick Reference

**Animation State Machine:**
```basic
10 ST=0:REM 0=idle, 1=walk, 2=jump, 3=fall
20 REM State detection priority:
30 IF NOT GR AND VY<0 THEN ST=2  : REM Jump first
40 IF NOT GR AND VY>0 THEN ST=3  : REM Fall second
50 IF GR AND VX<>0 THEN ST=1     : REM Walk third
60 IF GR AND VX=0 THEN ST=0      : REM Idle last
```

**Frame Cycling:**
```basic
10 FC=FC+1  : REM Increment every frame
20 FRAME=(FC/SPEED) AND (COUNT-1)
30 REM SPEED controls animation rate
40 REM COUNT must be power of 2 (2,4,8)
50 REM AND masks to frame range
```

**Sprite Pointer Layout:**
```
Block 13-14: Idle frames (2 frames)
Block 15-18: Walk cycle (4 frames)
Block 19: Jump frame (1 frame)
Block 20: Fall frame (1 frame)
Block 21-22: Turn frames (optional)

Total: 6-8 sprite blocks for full character
```

**Animation Speed Guidelines:**
- Idle: Slow (FC/10) - subtle breathing
- Walk: Medium (FC/5) - clear footsteps
- Jump/Fall: Static - no cycling needed
- Run: Fast (FC/3) - energetic motion

**Performance Note:**
"Multi-state animation adds minimal overhead (pointer changes only). Performance depends on total sprite count. With 8+ animated sprites, frame rate begins dropping (discovered in L36)."
