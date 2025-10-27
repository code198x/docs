# Lesson 023: Blitter Optimization

**Arc:** Arcade Action
**Position:** Lesson 2 of 6 in arc
**Type:** Deep Dive
**Estimated Completion:** 60 lines of code (but heavy concept focus)

## Learning Objectives

- Understand Blitter bandwidth and limits
- Optimize BOB usage for performance
- Reduce overdraw with priority and clipping
- Manage sprite pools efficiently

## Prerequisites

**From Previous Lessons:**
- Fast BOB movement (L22)
- BOB fundamentals (L7-9, L12)

**AMOS Knowledge:**
- Bob command variations
- Bob Update synchronization
- Bob priority system

## Key Concepts Introduced

### Blitter Bandwidth
The Blitter can copy ~800KB/second. A 32×32×4-bitplane BOB = 512 bytes. Moving 12 such BOBs = ~6KB × 50fps = 300KB/s. More BOBs or larger sprites exceed bandwidth.

### Overdraw
When multiple BOBs overlap, the Blitter copies all layers. Priority and Bob Off reduce wasted copies. A 4-BOB pile = 4× the work vs. single BOB.

### Sprite Pooling
Pre-allocate maximum BOBs needed (e.g., 50 bullets). Reuse inactive BOBs instead of creating/destroying. Faster and prevents fragmentation.

### Bob Priority
Higher priority BOBs render on top. Use priority to control Z-order without sorting. Background layer = 0, player = 10, effects = 20.

## Code Pattern

```amos
Screen Open 0,320,256,32,Lowres
Curs Off: Flash Off: Cls 0

' Create sprite
Ink 2
Bar 0,0 To 7,7  ' Small 8×8 sprite (4× less data than 16×16)
Get Bob 1,0,0 To 8,8
Cls 0

' Sprite pool: 50 bullets
Dim active(50)      ' 0=inactive, 1=active
Dim bx#(50),by#(50) ' Fixed-point positions
Dim bvx#(50),bvy#(50) ' Velocities

' Initialize all BOBs (pre-allocate)
For I=1 To 50
  Bob I,-100,-100,1  ' Off-screen
  Bob Priority I,5   ' Mid-priority
  active(I)=0
Next I

' Player
px=160: py=128
Bob 51,px,py,1
Bob Priority 51,10  ' Player higher priority

bulletCount=0

Do
  ' Player movement
  If Jleft(1) Then Dec px,3
  If Jright(1) Then Add px,3
  If Jup(1) Then Dec py,3
  If Jdown(1) Then Add py,3

  ' Fire bullet
  If Fire(1)
    ' Find inactive bullet in pool
    For I=1 To 50
      If active(I)=0
        active(I)=1
        bx#(I)=px*256
        by#(I)=py*256
        bvx#(I)=0
        bvy#(I)=-512  ' Move up (2 pixels/frame)
        Inc bulletCount
        Exit  ' Found one, stop searching
      End If
    Next I
  End If

  ' Update active bullets
  For I=1 To 50
    If active(I)=1
      ' Move
      Add bx#(I),bvx#(I)
      Add by#(I),bvy#(I)

      ' Off-screen check
      If by#(I)<0 or by#(I)>256*256
        active(I)=0  ' Deactivate
        Bob Off I    ' Hide (saves Blitter time!)
        Dec bulletCount
      Else
        ' On-screen: update position
        Bob I,bx#(I)/256,by#(I)/256,1
        Bob On I
      End If
    End If
  Next I

  ' Display stats
  Locate 0,0: Print "Active bullets: ";bulletCount;" "

  Bob 51,px,py,1
  Wait Vbl
  Bob Update
Loop Until Inkey$<>""
```

## Hardware Interaction

**Blitter Operation:**
1. Wait Vbl signals start of frame
2. Bob Update triggers Blitter operations
3. Blitter copies each active BOB:
   - Read source bitmap from Chip RAM
   - Apply transparency mask
   - Write to screen buffer
4. If Blitter work exceeds 20ms (50Hz frame), frame drops

**Bandwidth Math:**
- 32×32 BOB, 4 bitplanes = 512 bytes
- 50fps × 512 bytes = 25KB/s per BOB
- 12 BOBs = 300KB/s (still comfortable)
- 30 BOBs = 750KB/s (approaching limit!)

**Optimization Impact:**
- Bob Off: Skips Blitter copy entirely (saves full BOB time)
- Smaller sprites: 8×8 = 64 bytes (8× more bullets possible)
- Priority: Reduces overdraw (multiple layers at same pixel)

## Common Pitfalls

1. **Creating BOBs in game loop:** Get Bob is slow, do it once at startup
2. **No Bob Off for inactive sprites:** Blitter wastes time copying off-screen BOBs
3. **Sorting instead of priority:** Manual Z-sorting is slower than Bob Priority
4. **Large sprites for small objects:** 32×32 bullet wastes bandwidth
5. **Unbounded sprite count:** No pool = performance dies when many active

## Extension Ideas

- Multi-size sprite pools (small bullets, large enemies)
- Priority layers (background, entities, effects, UI)
- Frustum culling (don't update BOBs far off-screen)
- LOD system (simpler sprites when many on-screen)
- Blitter usage meter (visual performance gauge)

## Builds Toward

**In This Arc:**
- L24: Bullet management with pools
- L25: Enemy waves (many sprites)
- L27: Complete shooter with optimized rendering

## Quick Reference

### Sprite Pool Pattern
```amos
' Setup
Dim active(maxSprites)
For I=1 To maxSprites
  Bob I,-100,-100,imageNum
  Bob Off I
  active(I)=0
Next I

' Spawn sprite
For I=1 To maxSprites
  If active(I)=0
    active(I)=1
    ' Set position/velocity
    Exit
  End If
Next I

' Update active
For I=1 To maxSprites
  If active(I)=1
    ' Update logic
    If should_deactivate Then
      active(I)=0
      Bob Off I  ' CRITICAL: hide it!
    End If
  End If
Next I
```

### Bob Priority
```amos
' Setup (once)
Bob Priority bobNum,level

' Levels
'  0-5   Background elements
'  6-10  Enemies
' 11-15  Player
' 16-20  Particles/effects
' 21-25  UI elements
```

### Size Optimization
```amos
' Large sprite for main character
Get Bob 1,0,0 To 32,32  ' 512 bytes

' Tiny sprite for bullets
Get Bob 2,0,0 To 4,4    ' 8 bytes (64× smaller!)

' Medium sprite for enemies
Get Bob 3,0,0 To 16,16  ' 128 bytes
```

### Performance Measurement
```amos
' Start timing
t1=Timer

' Do Bob Update
Bob Update

' End timing
t2=Timer
blitterTime=t2-t1

Locate 0,0: Print "Blitter: ";blitterTime;" ticks"
' 1 tick = 0.02s @50Hz
' >10 ticks = frame drop warning!
```

### Frustum Culling
```amos
' Only update BOBs near screen
screenMargin=32  ' 32 pixels off-screen is okay

For I=1 To maxSprites
  If active(I)=1
    ' Check if in frustum
    If x(I)>-screenMargin and x(I)<320+screenMargin
      If y(I)>-screenMargin and y(I)<256+screenMargin
        ' On or near screen: update and show
        Bob I,x(I),y(I),img(I)
        Bob On I
      Else
        Bob Off I  ' Off-screen: hide
      End If
    Else
      Bob Off I
    End If
  End If
Next I
```

### Blitter Budget
```
Available time per frame @50Hz: 20ms
Bob Update overhead: ~2ms
Per-BOB cost (16×16, 4 bitplanes): ~0.5ms
Safe budget: 30-40 BOBs active simultaneously
Danger zone: >50 BOBs (frame drops likely)
```

---

**Version:** 1.0
**Created:** 2025-10-27
