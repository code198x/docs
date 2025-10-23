# Lesson 040: Room Navigation

**Arc:** Adventure/RPG
**Position:** Lesson 1 of 6 in arc
**Type:** Standard
**Estimated Completion:** 70 lines of code

## Learning Objectives

- Build multi-room world with NSEW navigation
- Implement room-to-room transitions
- Create data-driven room descriptions
- Design interconnected game world structure

## Prerequisites

**From Previous Lessons:**
- Data-driven design (L6, L35)
- Screen memory manipulation (L8)
- Text-based navigation concepts (L16)

**BASIC Knowledge:**
- String arrays for descriptions
- Room adjacency data structures
- Direction parsing

## Key Concepts Introduced

### Room-Based World
Game world divided into discrete rooms. Each room has description, exits (N/S/E/W), and contents. Player navigates between rooms.

### Adjacency Data
Store room connections in arrays: RN(room)=north exit room number, RS(room)=south, etc. 0 means no exit in that direction.

### Room Descriptions
Use string arrays or DATA statements for room text. Display description on entry, allow commands to move or interact.

### Navigation Commands
Parse player input for N/S/E/W commands. Validate exit exists, then transition to new room.

## Code Pattern

```basic
10 REM Room navigation system
20 MAXROOMS=10:CR=1:REM Max rooms, current room
30 REM Room connections (N/S/E/W exits for each room)
40 DIM RN(10),RS(10),RE(10),RW(10)
50 REM Room descriptions
60 DIM RD$(10)
70 REM Initialize world
80 GOSUB 1000:REM Load room data
90 REM Main game loop
100 GOSUB 2000:REM Display room
110 PRINT:PRINT "COMMAND (N/S/E/W/LOOK/QUIT)";
120 INPUT C$
130 REM Parse command
140 IF C$="N" THEN GOSUB 3000:REM Go north
150 IF C$="S" THEN GOSUB 3100:REM Go south
160 IF C$="E" THEN GOSUB 3200:REM Go east
170 IF C$="W" THEN GOSUB 3300:REM Go west
180 IF C$="LOOK" THEN GOSUB 2000
190 IF C$="QUIT" THEN PRINT "THANKS FOR PLAYING!":END
200 GOTO 100
1000 REM Load room data
1010 REM Room 1: Entrance Hall
1020 RN(1)=2:RS(1)=0:RE(1)=3:RW(1)=0
1030 RD$(1)="YOU STAND IN THE ENTRANCE HALL. A GRAND"
1040 RD$(1)=RD$(1)+" STAIRCASE LEADS NORTH. A DOOR IS EAST."
1050 REM Room 2: Upper Landing
1060 RN(2)=4:RS(2)=1:RE(2)=5:RW(2)=0
1070 RD$(2)="THE UPPER LANDING. STAIRS SOUTH. HALLWAY"
1080 RD$(2)=RD$(2)+" NORTH. BEDROOM DOOR EAST."
1090 REM Room 3: Library
1100 RN(3)=0:RS(3)=0:RE(3)=0:RW(3)=1
1110 RD$(3)="A DUSTY LIBRARY. BOOKS LINE THE WALLS."
1120 RD$(3)=RD$(3)+" EXIT WEST."
1130 REM Room 4: Tower
1140 RN(4)=0:RS(4)=2:RE(4)=0:RW(4)=0
1150 RD$(4)="THE TOWER TOP. WIND HOWLS. STAIRS DOWN"
1160 RD$(4)=RD$(4)+" SOUTH."
1170 REM Room 5: Bedroom
1180 RN(5)=6:RS(5)=0:RE(5)=0:RW(5)=2
1190 RD$(5)="A SIMPLE BEDROOM. DOOR WEST. CLOSET"
1200 RD$(5)=RD$(5)+" NORTH."
1210 REM Room 6: Closet
1220 RN(6)=0:RS(6)=5:RE(6)=0:RW(6)=0
1230 RD$(6)="A DARK CLOSET. SOMETHING GLINTS IN THE"
1240 RD$(6)=RD$(6)+" CORNER. EXIT SOUTH."
1250 REM Room 7-10: Additional rooms
1260 RN(7)=0:RS(7)=0:RE(7)=8:RW(7)=0
1270 RD$(7)="THE CELLAR. DAMP AND COLD. DOOR EAST."
1280 RN(8)=0:RS(8)=0:RE(8)=9:RW(8)=7
1290 RD$(8)="UNDERGROUND PASSAGE. DOORS EAST AND WEST."
1300 RN(9)=10:RS(9)=0:RE(9)=0:RW(9)=8
1310 RD$(9)="TREASURE VAULT. STAIRS UP NORTH. DOOR WEST."
1320 RN(10)=0:RS(10)=9:RE(10)=0:RW(10)=0
1330 RD$(10)="SECRET CHAMBER. ANCIENT ARTIFACTS HERE."
1340 RD$(10)=RD$(10)+" STAIRS DOWN SOUTH."
1350 RETURN
2000 REM Display room description
2010 PRINT CHR$(147):REM Clear screen
2020 PRINT "ROOM ";CR
2030 PRINT STRING$(40,"-")
2040 PRINT RD$(CR)
2050 PRINT STRING$(40,"-")
2060 PRINT
2070 REM Show available exits
2080 PRINT "EXITS: ";
2090 IF RN(CR)>0 THEN PRINT "NORTH ";
2100 IF RS(CR)>0 THEN PRINT "SOUTH ";
2110 IF RE(CR)>0 THEN PRINT "EAST ";
2120 IF RW(CR)>0 THEN PRINT "WEST ";
2130 PRINT
2140 RETURN
3000 REM Go north
3010 IF RN(CR)=0 THEN PRINT "YOU CAN'T GO THAT WAY.":RETURN
3020 PRINT "YOU GO NORTH..."
3030 CR=RN(CR):FOR I=1 TO 50:NEXT I:REM Brief pause
3040 RETURN
3100 REM Go south
3110 IF RS(CR)=0 THEN PRINT "YOU CAN'T GO THAT WAY.":RETURN
3120 PRINT "YOU GO SOUTH..."
3130 CR=RS(CR):FOR I=1 TO 50:NEXT I
3140 RETURN
3200 REM Go east
3210 IF RE(CR)=0 THEN PRINT "YOU CAN'T GO THAT WAY.":RETURN
3220 PRINT "YOU GO EAST..."
3230 CR=RE(CR):FOR I=1 TO 50:NEXT I
3240 RETURN
3300 REM Go west
3310 IF RW(CR)=0 THEN PRINT "YOU CAN'T GO THAT WAY.":RETURN
3320 PRINT "YOU GO WEST..."
3330 CR=RW(CR):FOR I=1 TO 50:NEXT I
3340 RETURN
```

## Hardware Interaction

**Chips Involved:**
- None (text-based, minimal hardware interaction)

**Memory Addresses:**
- Screen memory for text display
- Keyboard buffer for INPUT

## Common Pitfalls

1. **Cyclic references:** Room A north to B, but B south to C (not A)—broken navigation
2. **String too long:** Room descriptions over 255 chars cause errors
3. **Unconnected rooms:** Room exists but no path from starting room
4. **Exit confusion:** Showing exits that don't exist (RN>0 but points to undefined room)
5. **No LOOK command:** Can't re-read room description after commands

## Extension Ideas

- Add room visited tracking (mark rooms explored)
- Add mini-map (ASCII grid showing visited rooms)
- Add "GO BACK" command (undo last move)
- Add locked doors (require keys)
- Add one-way passages (secret doors)
- Add random encounters in certain rooms
- Add room-specific events (triggers on entry)

## Builds Toward

**In This Tier:**
- L41: Inventory system (items found in rooms)
- L42: NPCs in rooms with dialogue
- L43: Combat encounters in specific rooms
- L44: Save/load (preserve room state and position)
- L45: Complete RPG with interconnected world

## Quick Reference

**Room Data Structure:**
```basic
RN(room) = North exit room number (0=no exit)
RS(room) = South exit
RE(room) = East exit
RW(room) = West exit
RD$(room) = Room description text
```

**Navigation Pattern:**
```basic
10 IF EXIT_ARRAY(CURRENT_ROOM)=0 THEN [no exit message]
20 PRINT "YOU GO [DIRECTION]..."
30 CURRENT_ROOM=EXIT_ARRAY(CURRENT_ROOM)
40 GOSUB [display room]
```

**Room Design Tips:**
- **Start simple:** 5-10 rooms initially
- **Loop paths:** Allow multiple routes between areas
- **Dead ends:** Some rooms have only one exit (tension)
- **Central hub:** One room connects to many areas
- **Logical layout:** North/south and east/west should feel consistent

**Command Parsing:**
```basic
10 INPUT C$
20 IF C$="N" OR C$="NORTH" THEN GOSUB [north]
30 IF C$="S" OR C$="SOUTH" THEN GOSUB [south]
40 REM Accept abbreviations and full words
```

**String Management:**
- **Concatenation:** Build long descriptions with RD$=RD$+" MORE TEXT"
- **Line breaks:** Use PRINT statements, not CHR$(13) in strings
- **Max length:** Keep descriptions under 200 chars

**World Design Patterns:**
- **Linear:** Room 1→2→3→4 (tutorial)
- **Hub-and-spoke:** Central room connects to 4-5 areas
- **Grid:** Rooms in rectangular grid
- **Maze:** Complex interconnections (advanced)

**Performance Note:**
"Room navigation is instant (no graphics, minimal processing). Text-based games have zero speed pressure—BASIC's interpreter overhead is irrelevant when player reads descriptions and types commands. Turn-based interaction is BASIC's strength."
