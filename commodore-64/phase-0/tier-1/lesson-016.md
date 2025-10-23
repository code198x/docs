# Lesson 016: Crystal Caverns

**Arc:** Mini Adventure
**Position:** Lesson 2 of 2 in arc
**Type:** Synthesis
**Estimated Completion:** 60 lines of code

## Learning Objectives

- Create complete text adventure with room navigation
- Implement inventory system basics
- Combine timer pressure with exploration gameplay
- Synthesize ALL Tier 1 concepts into one complete game
- Experience complete game design (story, goals, challenge, feedback)

## Prerequisites

**From Previous Lessons:**
- String handling and input (L4-6)
- Data structures (arrays, DATA) (L5-6)
- Countdown timer (L15)
- Sound effects (L11)
- Game state management (L14)

**BASIC Knowledge:**
- All Tier 1 fundamentals
- DATA/READ for room descriptions
- Arrays for inventory
- Conditionals for game logic

## Key Concepts Introduced

### Room-Based Navigation
Each room is a number (1-5). Player input (N/S/E/W) changes room number. Different descriptions and items per room.

### Simple Inventory
Array stores collected items. Check array before allowing certain actions (need key to unlock door).

### Goal-Oriented Gameplay
Player has clear objective: find crystal, return to entrance before time expires. Not just exploration.

### State Management
Track current room, inventory, timer, game phase (exploring vs escaping). Multiple systems interact.

## Code Pattern

```basic
10 DIM I$(5):II=0:R=1:TL=120:T1=TI
20 REM Room descriptions
30 READ R$:PRINT R$
40 PRINT "N/S/E/W TO MOVE, GET ITEM"
50 INPUT C$
60 IF C$="N" OR C$="S" OR C$="E" OR C$="W" THEN GOSUB 1000
70 IF C$="GET" THEN GOSUB 2000
80 REM Timer check
90 E=INT((TI-T1)/60):RE=TL-E
100 IF RE<=0 THEN PRINT "COLLAPSED!":END
110 PRINT "TIME:";RE
120 REM Win condition
130 IF R=1 AND II=1 THEN PRINT "ESCAPED!":END
140 GOTO 30
1000 REM Movement handler
1010 IF C$="N" AND R=1 THEN R=2
1020 IF C$="S" AND R=2 THEN R=1
1030 REM [more room connections]
1040 RETURN
2000 REM Item pickup
2010 IF R=5 THEN II=1:I$(II)="CRYSTAL"
2020 PRINT "GOT:";I$(II)
2030 GOSUB 3000:REM Pickup sound
2040 RETURN
3000 REM Pickup sound effect
3010 POKE 54296,15:POKE 54272,100:POKE 54273,30
3020 POKE 54276,65:FOR D=1 TO 100:NEXT D
3030 POKE 54276,64:RETURN
5000 DATA "ENTRANCE. PASSAGES N AND E."
5010 DATA "DARK TUNNEL. EXITS S AND N."
5020 DATA "CRYSTAL ROOM! GET THE CRYSTAL!"
```

## Hardware Interaction

**Chips Involved:**
- **SID** - Sound effects for pickups and events
- **CIA** - Timer for countdown pressure

**Memory Addresses:**
- SID registers for sound
- TI variable for timing

## Common Pitfalls

1. **Complex room connections:** Easy to create impossible navigation (room 2 goes to room 3 but not back)
2. **Inventory overflow:** Array size limits number of items
3. **Missing win condition:** Player can get crystal but never escape
4. **No item checking:** Door opens without key (breaks puzzle logic)
5. **Timer too short/long:** Balance is critical for fun

## Extension Ideas

- Add more rooms (10-15 room dungeon)
- Add multiple items (key, torch, map)
- Add room hazards (need torch for dark rooms)
- Add enemies (random encounters with combat)
- Add multiple endings (different escape routes)
- Add room-specific sounds (dripping water, wind)
- Save/load game state (preview of L44)

## Builds Toward

**In Next Tier:**
- More complex adventures with graphics
- Room-based games with sprite characters

**In Tier 3:**
- L40-45: Complete RPG with advanced room navigation
- L42: Branching dialogue systems
- L43: Turn-based combat
- L44: Save/load systems

## Quick Reference

**Room Navigation Pattern:**
```basic
10 R=1  :REM Current room
20 INPUT C$
30 IF C$="N" THEN R=[north room number]
40 IF C$="S" THEN R=[south room number]
50 [etc for E/W]
```

**Simple Inventory:**
```basic
10 DIM I$(10)  :REM Item array
20 II=0        :REM Item index
30 REM On pickup:
40 II=II+1:I$(II)="ITEM NAME"
50 REM Check if has item:
60 FOR I=1 TO II:IF I$(I)="KEY" THEN HK=1:NEXT I
```

**Room Data Pattern:**
```basic
1000 REM Room descriptions
1100 IF R=1 THEN PRINT "ENTRANCE. EXITS N,E"
1110 IF R=2 THEN PRINT "TUNNEL. EXITS S,W"
1120 REM etc...
```

**Or DATA-driven:**
```basic
10 DIM RD$(10)  :REM Room descriptions
20 FOR I=1 TO 5:READ RD$(I):NEXT I
30 PRINT RD$(R)  :REM Display current room
5000 DATA "ENTRANCE. EXITS N,E"
5010 DATA "TUNNEL. EXITS S,W"
```

**Win/Lose Conditions:**
```basic
100 IF R=1 AND [has crystal] THEN PRINT "WIN!":END
200 IF RE<=0 THEN PRINT "LOSE!":END
```

**Tier 1 Synthesis Checklist:**
This game demonstrates:
- ✓ Variables and conditionals (L1-3)
- ✓ String input and comparison (L4)
- ✓ Arrays for data (L5)
- ✓ DATA for content (L6)
- ✓ Sound effects (L11)
- ✓ Timer system (L15)
- ✓ Game state management (L14)
- ✓ Complete game structure

**Congratulations - you've completed Tier 1!**
