# Lesson 015: Countdown Timer

**Arc:** Mini Adventure
**Position:** Lesson 1 of 2 in arc
**Type:** Standard
**Estimated Completion:** 20 lines of code

## Learning Objectives

- Use the TI system timer variable
- Create countdown timers for time-based challenges
- Understand jiffies (1/60th second timing unit)
- Add time pressure to games

## Prerequisites

**From Previous Lessons:**
- Variables and conditionals (L1-3)
- Game loop structure (L12-14)
- Screen display techniques (L7-9)

**BASIC Knowledge:**
- Variables
- IF/THEN conditionals
- Basic arithmetic

## Key Concepts Introduced

### The TI Variable
TI is a special system variable counting jiffies (1/60th second) since power-on. It automatically increments in background.

### Jiffy Timing
PAL C64: 50 jiffies/second, NTSC: 60 jiffies/second. For simplicity, use 60 for calculations (close enough for games).

### Countdown Logic
Store start time, calculate elapsed time (TI - start), convert to seconds, display remaining time. When time reaches zero, trigger event.

### Timer Pressure
Timers create urgency. Players must act before time expires. Essential for challenges, puzzles, and action sequences.

## Code Pattern

```basic
10 TL=30:REM Time limit in seconds
20 T1=TI:REM Store start time
30 REM Game loop
40 E=INT((TI-T1)/60):REM Elapsed seconds
50 R=TL-E:REM Remaining time
60 PRINT CHR$(19):REM Clear screen
70 PRINT "TIME LEFT:";R
80 IF R<=0 THEN PRINT "TIME UP!":END
90 REM Game logic here
100 GOTO 40
```

## Hardware Interaction

**Chips Involved:**
- **CIA** - Hardware timer that updates TI

**Memory Addresses:**
- TI is a BASIC variable, not direct memory address
- Underlying hardware: CIA timer at $DC04-$DC05

## Common Pitfalls

1. **TI overflows:** TI resets to 0 after 24 hours (rare in games but possible)
2. **Wrong jiffy count:** Using 50 vs 60 affects accuracy slightly
3. **Not storing start time:** Must save TI at game start, then compare
4. **Integer division:** INT() prevents decimal seconds display
5. **Blocking during timer:** Long delays stop timer display updates

## Extension Ideas

- Add timer bonus (finish fast = more points)
- Add timer penalty (time pressure increases difficulty)
- Add time pickups (collect items to extend time)
- Add timer warnings (colour change when <10 seconds)
- Add lap timer (racing games, speedruns)
- Display minutes:seconds format

## Builds Toward

**In This Tier:**
- L16: Crystal Caverns uses timer for dungeon escape

**In Next Tier:**
- Animation timing (frame rate control)
- Enemy spawn timing
- Power-up duration timers

**In Later Tiers:**
- Precise frame timing for smooth animation
- Music synchronization
- Performance measurement (fps calculation)

## Quick Reference

**TI System Variable:**
- `TI` - Jiffy counter (1/60 second)
- Automatically increments
- Resets to 0 after 24 hours or with `TI=0`

**Timing Formulas:**
```basic
Seconds elapsed: INT((TI-T1)/60)
Milliseconds: (TI-T1)*16.67  (approximate)
Minutes: INT((TI-T1)/3600)
```

**Countdown Timer Pattern:**
```basic
10 TL=30           :REM Time limit (seconds)
20 T1=TI           :REM Store start time
30 E=INT((TI-T1)/60) :REM Elapsed
40 R=TL-E          :REM Remaining
50 IF R<=0 THEN [time up action]
```

**Count-Up Timer Pattern:**
```basic
10 T1=TI           :REM Store start time
20 E=INT((TI-T1)/60) :REM Elapsed seconds
30 PRINT "TIME:";E
```

**Minutes:Seconds Display:**
```basic
10 E=INT((TI-T1)/60)  :REM Total seconds
20 M=INT(E/60)        :REM Minutes
30 S=E-(M*60)         :REM Remaining seconds
40 PRINT M;":";S
```

**Timer Warning Pattern:**
```basic
10 IF R<=10 THEN POKE 53280,2:REM Red border warning
20 IF R<=5 THEN [play warning sound]
```

**Common Timer Durations:**
- 30 seconds: Quick challenge
- 60 seconds: Standard level
- 120 seconds: Long level
- 300 seconds: Episode/chapter
