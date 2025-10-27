# Lesson 017: AMAL Introduction

**Arc:** Animation System
**Position:** Lesson 1 of 5 in arc
**Type:** Standard
**Estimated Completion:** 60 lines of code

## Learning Objectives

- Introduction to AMAL (AMOS Animation Language)
- Create simple movement animations
- Understand animation channels
- Link AMAL programs to BOBs

## Prerequisites

**From Previous Lessons:**
- BOB creation and display (L7-9)
- BOB movement with joystick (L12)
- Bob command for positioning (all Tier 1)

**AMOS Knowledge:**
- Get Bob and Paste Bob
- Bob Update synchronization
- Wait Vbl timing

## Key Concepts Introduced

### AMAL (AMOS Animation Language)
AMAL is a mini-language for defining animations. Write movement scripts that run independently, freeing your main program from manual position updates.

### Animation Channels
AMAL supports multiple channels (0-15). Each BOB can have its own animation channel running simultaneously.

### Movement Commands
AMAL provides commands like `M` (move), `J` (jump), `L` (loop) to define sprite paths without frame-by-frame BASIC code.

### Amal and Amal On
`Amal channel,"script"` defines animation. `Amal On channel` activates it. Animations run automatically each frame.

## Code Pattern

```amos
Screen Open 0,320,256,32,Lowres
Curs Off: Flash Off: Cls 0

' Create sprite
Ink 2
Bar 0,0 To 15,15
Get Bob 1,0,0 To 16,16
Cls 0

' Position BOB
Bob 1,50,100,1

' Define AMAL animation on channel 0
' M = Move, first two numbers are X,Y distance, third is frames
Amal 0,"M 200,0,50; M 0,100,50; M -200,0,50; M 0,-100,50; L"

' Link channel 0 to BOB 1
Amal 0,1

' Activate animation
Amal On 0

' Main loop
Do
  Wait Vbl
  Bob Update
Loop Until Inkey$<>""

' Cleanup
Amal Off 0
```

## Hardware Interaction

**Chips Involved:**
- **Blitter** - BOB rendering (AMAL just updates positions)
- **CPU** - AMAL interpreter runs each frame

**AMAL Execution:**
- Parsed once when Amal command called
- Executed each frame automatically
- Updates BOB positions before Bob Update

## Common Pitfalls

1. **Forgetting Amal On:** Animation won't start without `Amal On channel`
2. **Wrong channel linking:** `Amal 0,1` links channel 0 to BOB 1 (not channel 0 to channel 1)
3. **Missing Loop:** Without `L` at end, animation runs once and stops
4. **No Bob Update:** AMAL updates positions but Bob Update needed to display
5. **Conflicting manual movement:** Don't Bob move same sprite you're AMAL animating

## Extension Ideas

- Create circular motion patterns
- Animate multiple BOBs with different channels
- Create figure-8 paths
- Bounce animations with wait commands
- Chain multiple movement sequences

## Builds Toward

**In This Tier:**
- L18: Multi-frame sprite animation
- L19: Animation synchronization
- L20: Collision during animation
- L21: Animated sprite showcase (deliverable)

**In Next Tier:**
- Advanced AMAL techniques
- Complex movement patterns

## Quick Reference

### AMAL Commands
```
M x,y,frames    Move relative by x,y over frames
J x,y           Jump absolute to x,y instantly
W frames        Wait for frames
L               Loop back to start
A channel       Auto-move (continue last direction)
```

### AMAL Setup
```amos
' 1. Define animation script
Amal channel,"script"

' 2. Link channel to BOB
Amal channel,bob_number

' 3. Activate
Amal On channel

' 4. (Later) Stop
Amal Off channel
```

### Channel Management
```amos
' Multiple channels for multiple BOBs
Amal 0,"M 100,0,25; L"  ' Channel 0 script
Amal 0,1                 ' Link channel 0 to BOB 1
Amal 1,"M 0,100,25; L"  ' Channel 1 script
Amal 1,2                 ' Link channel 1 to BOB 2
Amal On               ' Activate ALL channels
```

### Query Animation State
```amos
' Check if animation finished
If Amal(channel)=0 Then
  ' Animation complete or stopped
End If
```

---

**Version:** 1.0
**Created:** 2025-10-27
