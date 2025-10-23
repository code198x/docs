# Lesson 026: Background Music Player

**Arc:** Sound & Music Mastery
**Position:** Lesson 3 of 5 in arc
**Type:** Standard
**Estimated Completion:** 50 lines of code

## Learning Objectives

- Create non-blocking music playback
- Play music while game continues running
- Implement music state machine
- Understand timing trade-offs

## Prerequisites

**From Previous Lessons:**
- Melody sequencer (L25)
- Game loop structure (L23)
- State management (L20-23)

**BASIC Knowledge:**
- Music data format
- Game loop integration
- State variables

## Key Concepts Introduced

### Non-Blocking Playback
Instead of FOR loop that freezes game, advance one note per game loop iteration. Game continues while music plays.

### Music State Variables
Track current note index (MI), note start time, note duration. Check each frame if time to advance.

### Frame Budget
Playing music takes time each frame. Complex music + complex game = slowdown. Trade-off awareness begins.

### Music Loop
When reaching end of song, reset to beginning for continuous background music.

## Code Pattern

```basic
10 DIM N(32),D(32):MI=1:MT=0:REM Music arrays, index, timer
20 REM Load music data
30 FOR I=1 TO 16:READ N(I),D(I):NEXT I
40 POKE 54296,15
50 REM Main game loop
60 REM [Game logic here]
70 GOSUB 1000:REM Update music
80 GOTO 60
1000 REM Music update (non-blocking)
1010 MT=MT+1
1020 IF MT<D(MI)*5 THEN RETURN:REM Not time to change yet
1030 REM Change to next note
1040 POKE 54276,16:REM Stop current note
1050 MI=MI+1:IF MI>16 THEN MI=1:REM Loop music
1060 IF N(MI)=0 THEN MT=0:RETURN:REM Rest
1070 POKE 54272,N(MI) AND 255
1080 POKE 54273,INT(N(MI)/256)
1090 POKE 54277,0:POKE 54278,240
1100 POKE 54276,17:REM Start new note
1110 MT=0:REM Reset timer
1120 RETURN
```

## Hardware Interaction

**Chips Involved:**
- **SID** - Voice for music (typically voice 3 for background)

**Memory Addresses:**
- SID voice registers

## Common Pitfalls

1. **Music slows game:** Each music update takes time; complex music = slower game
2. **Timing drift:** Frame rate variations affect music tempo
3. **Note overlap:** Not stopping previous note before starting new
4. **Index overflow:** MI exceeds array size if not looped/checked
5. **Duration scaling:** Need to adjust duration multiplier for game speed

## Extension Ideas

- Use voice 3 for music, voices 1-2 for effects
- Add music on/off toggle
- Add multiple songs (select by level/mood)
- Adjust tempo based on game state (faster when danger)
- Fade music in/out
- Add music pause/resume

## Builds Toward

**In This Tier:**
- L27: Sound effects with music playing
- L28: Full 3-voice composition

## Quick Reference

**Non-Blocking Pattern:**
```basic
1000 REM Called each game loop
1010 [check if time to advance]
1020 IF NOT_TIME THEN RETURN
1030 [advance to next note]
1040 [update SID]
1050 RETURN
```

**Music State Variables:**
```basic
10 MI=1    :REM Music index (current note)
20 MT=0    :REM Music timer
30 ML=16   :REM Music length (# notes)
```

**Music Loop:**
```basic
10 MI=MI+1
20 IF MI>ML THEN MI=1  :REM Restart from beginning
```

**Performance Note:**
"Music playback adds ~1-2ms per frame. Combined with game logic (sprites, collisions), total frame time increases. At 60fps target (16.7ms/frame), music takes ~10% of budget."

**Recommended Voice Allocation:**
- Voice 1: Player sound effects (shots, hits)
- Voice 2: Enemy/world sound effects
- Voice 3: Background music
