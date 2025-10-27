# Lesson 026: Parallax Scrolling

**Arc:** Arcade Action
**Position:** Lesson 5 of 6 in arc
**Type:** Standard
**Estimated Completion:** 100 lines of code

## Learning Objectives

- Create scrolling backgrounds for depth
- Implement parallax layers (multiple speeds)
- Use Screen Offset for smooth scrolling
- Optimize background rendering

## Prerequisites

**From Previous Lessons:**
- Fast BOB movement (L22)
- Blitter concepts (L23)

**AMOS Knowledge:**
- Screen Open dual-playfield mode
- Screen Offset command
- Screen Copy for wrapping

## Key Concepts Introduced

### Parallax Effect
Multiple background layers scroll at different speeds to create illusion of depth. Far layer (stars) scrolls slowly, near layer (clouds) scrolls faster.

### Screen Offset
`Screen Offset playfield,x,y` shifts entire screen hardware register. CPU cost: ~1μs. Blitter cost: zero! Hardware just changes display start address.

### Wrapping
When background scrolls past edge, copy it to other side seamlessly. Use Screen Copy or draw repeating tiles.

### Dual Playfield
Amiga can display two independent screens simultaneously. Background on playfield 0, sprites on playfield 1. Each has own palette and scroll offset.

## Code Pattern

```amos
' Dual-playfield mode: 2 screens, 8 colours each
Screen Open 0,320,256,8,Lowres : Curs Off: Flash Off
Screen Open 1,320,256,8,Lowres

' Screen 0: Far background (stars)
Screen 0
Screen Display 0,,320,256,0,0  ' Back playfield
Cls 0
' Draw starfield
For I=1 To 100
  Ink 1+Rnd(3)
  Plot Rnd(640),Rnd(256)  ' 2× width for wrapping
Next I

' Screen 1: Near background + sprites
Screen 1
Screen Display 1,,320,256,0,0  ' Front playfield
Cls 0
' Draw clouds (repeating pattern)
For I=0 To 1  ' Draw twice for wrapping
  Ink 7
  For C=0 To 5
    Circle I*320+Rnd(320),Rnd(128),Rnd(20)+10
  Next C
Next I

' Get player sprite
Ink 2: Bar 0,0 To 15,15: Get Bob 1,0,0 To 16,16: Cls 0

' Player
px=100: py=128
Bob 1,px,py,1

' Scroll positions (fixed-point for smooth sub-pixel)
farScroll#=0
nearScroll#=0

Do
  ' Player movement
  If Jleft(1) Then Dec px,3
  If Jright(1) Then Add px,3
  If Jup(1) Then Dec py,3
  If Jdown(1) Then Add py,3

  ' Auto-scroll (or player-driven)
  scrollSpeed#=64  ' 0.25 pixels/frame
  Add farScroll#,scrollSpeed#*4/10   ' Far layer: 40% speed
  Add nearScroll#,scrollSpeed#        ' Near layer: 100% speed

  ' Wrap scroll positions
  If farScroll#>=320*256 Then farScroll#=0
  If nearScroll#>=320*256 Then nearScroll#=0

  ' Apply hardware scroll
  Screen Offset 0,farScroll#/256,0   ' Stars
  Screen Offset 1,nearScroll#/256,0  ' Clouds

  ' Update sprites
  Bob 1,px,py,1

  Wait Vbl
  Bob Update
Loop Until Inkey$<>""
```

## Hardware Interaction

**Chips Involved:**
- **Denise** - Dual playfield compositor, hardware scroll registers
- **Copper** - Sets BPLCON1 (scroll fine), BPL1MOD/BPL2MOD (scroll coarse)
- **Blitter** - Draws initial backgrounds (not used during scroll)
- **CPU** - Minimal: just updates scroll registers

**Hardware Scroll:**
- Screen Offset writes to Copper list
- No pixel copying! Just changes start address
- Sub-pixel precision: 15 positions (hardware limit)
- AMOS handles wrapping automatically when using Screen Copy

**Performance:**
- Screen Offset: ~1μs (instant)
- Drawing background: only once at startup
- Wrapping: ~5ms when edge reached (Screen Copy)
- BOBs render same speed regardless of scroll

## Common Pitfalls

1. **Single background only:** No depth, looks flat
2. **Same scroll speed for all layers:** Breaks parallax illusion
3. **No wrapping:** Background ends abruptly at edge
4. **Forgetting Screen Display mode:** Screens don't composite without it
5. **Drawing background every frame:** Wastes Blitter time (draw once!)

## Extension Ideas

- Three+ parallax layers (far, mid, near)
- Vertical parallax (clouds move up/down too)
- Player-driven scroll (world moves, not player)
- Starfield with depth (dimmer = farther)
- Animated background elements (waterfalls, lava)

## Builds Toward

**In This Arc:**
- L27: Complete space shooter with scrolling starfield

**In Next Arc:**
- Platform game scrolling (camera following player)

## Quick Reference

### Dual Playfield Setup
```amos
' Create two screens
Screen Open 0,320,256,8,Lowres  ' Back layer
Screen Open 1,320,256,8,Lowres  ' Front layer

' Set display modes
Screen Display 0,,320,256,0,0   ' Back
Screen Display 1,,320,256,0,0   ' Front

' Draw on screen 0 (back)
Screen 0
' ... draw background ...

' Draw on screen 1 (front) + BOBs
Screen 1
' ... draw foreground ...
' Bob commands work on current screen
```

### Parallax Scroll Rates
```amos
' Far background: 30% of scroll speed
farScroll# = farScroll# + scrollSpeed# * 3/10

' Mid background: 70% of scroll speed
midScroll# = midScroll# + scrollSpeed# * 7/10

' Near/foreground: 100% of scroll speed
nearScroll# = nearScroll# + scrollSpeed#

' Apply
Screen Offset 0, farScroll#/256, 0
Screen Offset 1, midScroll#/256, 0
Screen Offset 2, nearScroll#/256, 0
```

### Wrapping (Manual)
```amos
' When scroll reaches edge, wrap
If scroll# >= wrapPoint*256
  scroll# = 0
  ' Optional: Screen Copy to seamlessly loop
  Screen Copy 0,320,0 To 0,0,320,256
End If
```

### Repeating Background Pattern
```amos
' Draw pattern twice for seamless wrap
For I=0 To 1
  ' Draw at x=0 and x=320
  xOffset = I*320
  ' ... draw pattern at xOffset ...
Next I

' Scroll will wrap seamlessly
```

### Player-Driven Scroll
```amos
' World scrolls, player appears stationary
If Jright(1)
  ' Don't move player sprite
  ' Instead, scroll world left
  Add worldScroll#, -playerSpeed#
End If

' Far layer moves slower
Screen Offset 0, worldScroll#*3/10/256, 0
Screen Offset 1, worldScroll#/256, 0
```

### Vertical Parallax
```amos
' Horizontal AND vertical scroll
Add farScrollX#, scrollSpeedX# * 3/10
Add farScrollY#, scrollSpeedY# * 3/10

Screen Offset 0, farScrollX#/256, farScrollY#/256
```

### Starfield Depth
```amos
' Create 3 star layers with different brightness
Screen 0
For layer=1 To 3
  Ink layer  ' Dimmer colour = farther
  For I=1 To 50
    Plot Rnd(640), Rnd(256)
  Next I
Next layer

' Scroll at different speeds
' (Only works if stars drawn on separate playfields)
```

### Performance: Static vs Dynamic Background
```amos
' GOOD: Draw once, scroll with hardware
Screen 0
' ... draw background once ...
' In loop: Screen Offset 0, x, y

' BAD: Redraw every frame
Screen 0
Repeat
  Cls 0  ' Wastes Blitter time!
  ' ... redraw background ...
  Screen Offset 0, x, y
Until False
```

---

**Version:** 1.0
**Created:** 2025-10-27
