# Lesson 018: Multi-Frame Animation

**Arc:** Animation System
**Position:** Lesson 2 of 5 in arc
**Type:** Standard
**Estimated Completion:** 80 lines of code

## Learning Objectives

- Create animated sprites with multiple frames
- Understand frame timing and playback
- Use Anim command for automatic frame cycling
- Combine movement and animation

## Prerequisites

**From Previous Lessons:**
- BOB creation and display (L7-9)
- AMAL movement scripts (L17)
- Bob Update synchronization (all Tier 1)

**AMOS Knowledge:**
- Get Bob and Paste Bob
- Amal movement commands
- Wait Vbl timing

## Key Concepts Introduced

### Animation Frames
Instead of single static images, sprites can cycle through multiple frames to create the illusion of motion. Each frame is a separate image stored sequentially in memory.

### Anim Command
`Anim bob_number,sequence,speed` automatically cycles through frames. The sequence defines frame order (e.g., "1,2,3,4,3,2" for smooth walk cycle). Speed sets frames per second.

### Frame Timing
Animation runs independently of movement. A sprite can move across screen while playing walk animation, or stand still while animating.

### Image Banking
Multiple frames stored together in image bank. Get Bob retrieves single frames; Anim cycles through them automatically.

## Code Pattern

```amos
Screen Open 0,320,256,32,Lowres
Curs Off: Flash Off: Cls 0

' Create 4-frame walk animation
Ink 2
For F=1 To 4
  Bar 0,0 To 15,15
  ' Draw frame F (different pose each frame)
  Get Bob F,0,0 To 16,16
  Cls 0
Next F

' Position BOB with frame 1
Bob 1,100,100,1

' Start animation: frames 1,2,3,4,3,2,1 at 8fps
Anim 1,"1,2,3,4,3,2",8

' Add AMAL movement
Amal 0,"M 200,0,100; M 0,100,100; M -200,0,100; M 0,-100,100; L"
Amal 0,1
Amal On 0

' Main loop
Do
  Wait Vbl
  Bob Update
Loop Until Inkey$<>""

' Cleanup
Amal Off 0
Anim Freeze 1
```

## Hardware Interaction

**Chips Involved:**
- **Blitter** - Copies each animation frame to screen
- **CPU** - Anim command updates which frame to display
- **Paula** - Could sync sound effects to animation frames

**Animation Execution:**
- Anim command sets up frame sequence in memory
- Each Wait Vbl, AMOS checks if it's time to change frame
- Blitter copies new frame data during Bob Update
- AMAL movement happens independently

**Performance:**
- Each frame is a separate 16x16 (or larger) bitmap
- More frames = more memory but smoother animation
- Blitter speed determines max sprites animating simultaneously

## Common Pitfalls

1. **Wrong frame numbers:** Anim sequence must reference existing Bob frames (1-N)
2. **Animation too fast:** Speed 50 = once per frame (too fast), 8-12 is typical
3. **Forgetting Anim Freeze:** Animation continues even after Bob hidden
4. **Frame size mismatch:** All frames in sequence must be same dimensions
5. **No Anim Off before Exit:** Animation keeps running in background

## Extension Ideas

- Create 8-direction walk animations (N, NE, E, SE, S, SW, W, NW)
- Sync animation to movement speed (faster = more fps)
- Different animations for different actions (walk, jump, attack)
- Pause animation when stationary (Anim Freeze/On)
- Frame-based collision boxes (different hitbox per frame)

## Builds Toward

**In This Tier:**
- L19: Synchronize multiple animations
- L20: Collision detection during animation
- L21: Complete animated sprite showcase

**In Next Tier:**
- Character state machines
- Enemy animation patterns

## Quick Reference

### Anim Commands
```
Anim bob,"sequence",speed   Set animation sequence
Anim Freeze bob             Pause animation
Anim On bob                 Resume animation
Anim Off                    Stop all animations
```

### Animation Setup
```amos
' 1. Create frames
For F=1 To 4
  ' Draw frame
  Get Bob F,0,0 To 16,16
Next F

' 2. Set animation
Anim 1,"1,2,3,4,3,2",8  ' Bob 1, sequence, 8fps

' 3. In main loop
Wait Vbl
Bob Update  ' Anim automatically updates frame
```

### Frame Sequences
```
"1,2,3,4"         Simple loop (1→2→3→4→1...)
"1,2,3,4,3,2"     Smooth reverse (1→2→3→4→3→2→1...)
"1,1,2,2,3,3"     Hold each frame (slower effect)
"1,2,1,2"         Two-frame toggle
```

### Speed Guidelines
```
1-4 fps     Very slow (idle breathing)
8-12 fps    Normal walk/run
15-20 fps   Fast action
30-50 fps   Special effects only
```

### Frame Management
```amos
' Check current frame
F=Bob Image(1)

' Manually set frame (bypasses Anim)
Bob 1,x,y,frame_number

' Stop animation, keep displaying current frame
Anim Freeze 1
```

---

**Version:** 1.0
**Created:** 2025-10-27
