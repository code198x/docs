# Lesson 046: Sokoban Clone

**Arc:** Strategy/Puzzle
**Position:** Lesson 1 of 3 in arc
**Type:** Standard
**Estimated Completion:** 110 lines of code

## Learning Objectives

- Implement grid-based puzzle mechanics
- Create push/pull box movement system
- Build level validation (win condition checking)
- Design progressive puzzle difficulty
- Master grid coordinate systems

## Prerequisites

**From Previous Lessons:**
- Grid-based navigation concepts (L40)
- Array management for level data
- Win condition logic

**BASIC Knowledge:**
- 2D array manipulation
- Collision detection in grids
- Level design with DATA statements

## Key Concepts Introduced

### Grid Representation
Use 2D array to represent playfield: 0=empty, 1=wall, 2=box, 3=goal, 4=player. Each cell is one grid square.

### Push Mechanics
When player moves into box, check if space beyond box is empty. If yes, move box and player. If no, movement blocked.

### Win Condition
Level complete when all boxes are on goal squares. Check after each move: count boxes on goals vs total goals.

### Level Progression
8 levels increasing in difficulty. Simple tutorials (2-3 boxes) to complex puzzles (5-6 boxes, tight spaces).

## Code Pattern

```basic
10 REM Sokoban clone
20 REM Grid-based puzzle game
30 DIM GRID(12,12):REM 12×12 playfield
40 DIM LVL$(8,144):REM 8 levels, 144 cells each (12×12)
50 PX=0:PY=0:REM Player position
60 LEVEL=1:MOVES=0:MAXLEVEL=8
70 REM Initialize
80 GOSUB 1000:REM Load level data
90 GOSUB 2000:REM Setup level
100 REM Main loop
110 GOSUB 3000:REM Display grid
120 GOSUB 4000:REM Get input
130 GOSUB 5000:REM Check win
140 IF WIN=1 THEN GOSUB 6000:REM Next level
150 GOTO 110
1000 REM Load level data
1010 REM Level 1: Tutorial (2 boxes)
1020 DATA "############"
1030 DATA "#.......#..#"
1040 DATA "#..B....G..#"
1050 DATA "#..........#"
1060 DATA "#..P...B.G.#"
1070 DATA "#..........#"
1080 DATA "############"
1090 REM (8 more DATA lines for 12×12 grid)
1100 REM Legend: # = wall, . = empty, B = box, G = goal, P = player
1110 REM [Additional 7 levels...]
1120 RETURN
2000 REM Setup level
2010 PRINT CHR$(147)
2020 PRINT "LOADING LEVEL ";LEVEL;"..."
2030 REM Clear grid
2040 FOR Y=1 TO 12:FOR X=1 TO 12
2050 GRID(X,Y)=0
2060 NEXT X:NEXT Y
2070 REM Read level data
2080 FOR Y=1 TO 12
2090 READ ROW$
2100 FOR X=1 TO 12
2110 C$=MID$(ROW$,X,1)
2120 IF C$="#" THEN GRID(X,Y)=1:REM Wall
2130 IF C$="B" THEN GRID(X,Y)=2:REM Box
2140 IF C$="G" THEN GRID(X,Y)=3:REM Goal
2150 IF C$="P" THEN PX=X:PY=Y:REM Player position
2160 NEXT X
2170 NEXT Y
2180 MOVES=0:WIN=0
2190 RESTORE:REM Reset DATA pointer for next level
2200 FOR I=1 TO (LEVEL-1)*12:READ DUMMY$:NEXT I:REM Skip to current level
2210 RETURN
3000 REM Display grid
3020 PRINT CHR$(19):REM Home cursor
3030 PRINT "LEVEL ";LEVEL;" MOVES: ";MOVES
3040 PRINT STRING$(40,"-")
3050 FOR Y=1 TO 12
3060 FOR X=1 TO 12
3070 REM Draw player
3080 IF X=PX AND Y=PY THEN PRINT "@";:GOTO 3150
3090 REM Draw grid cell
3100 IF GRID(X,Y)=0 THEN PRINT " ";:REM Empty
3110 IF GRID(X,Y)=1 THEN PRINT CHR$(160);:REM Wall (solid block)
3120 IF GRID(X,Y)=2 THEN PRINT "O";:REM Box
3130 IF GRID(X,Y)=3 THEN PRINT ".";:REM Goal
3140 IF GRID(X,Y)=4 THEN PRINT "*";:REM Box on goal
3150 NEXT X:PRINT
3160 NEXT Y
3170 PRINT STRING$(40,"-")
3180 PRINT "WASD=MOVE, R=RESTART, Q=QUIT"
3190 RETURN
4000 REM Get input and move
4010 GET K$:IF K$="" THEN RETURN
4020 DX=0:DY=0
4030 IF K$="W" THEN DY=-1:REM Up
4040 IF K$="S" THEN DY=1:REM Down
4050 IF K$="A" THEN DX=-1:REM Left
4060 IF K$="D" THEN DX=1:REM Right
4070 IF K$="R" THEN GOSUB 2000:RETURN:REM Restart level
4080 IF K$="Q" THEN PRINT "QUIT":END
4090 IF DX=0 AND DY=0 THEN RETURN:REM No movement
4100 REM Calculate new position
4110 NX=PX+DX:NY=PY+DY
4120 REM Check if move is valid
4130 IF GRID(NX,NY)=1 THEN RETURN:REM Wall blocks
4140 IF GRID(NX,NY)=0 OR GRID(NX,NY)=3 THEN GOSUB 4500:RETURN:REM Move to empty/goal
4150 IF GRID(NX,NY)=2 OR GRID(NX,NY)=4 THEN GOSUB 4600:RETURN:REM Push box
4160 RETURN
4500 REM Move to empty space or goal
4510 PX=NX:PY=NY:MOVES=MOVES+1
4520 RETURN
4600 REM Push box
4610 REM Check space beyond box
4620 BX=NX+DX:BY=NY+DY
4630 IF GRID(BX,BY)=1 OR GRID(BX,BY)=2 OR GRID(BX,BY)=4 THEN RETURN:REM Blocked
4640 REM Move box
4650 GRID(NX,NY)=0:REM Clear old box position
4660 IF GRID(BX,BY)=3 THEN GRID(BX,BY)=4:REM Box on goal
4670 IF GRID(BX,BY)=0 THEN GRID(BX,BY)=2:REM Box on empty
4680 REM Move player
4690 PX=NX:PY=NY:MOVES=MOVES+1
4700 RETURN
5000 REM Check win condition
5010 WIN=1:REM Assume win
5020 FOR Y=1 TO 12:FOR X=1 TO 12
5030 IF GRID(X,Y)=3 THEN WIN=0:REM Goal without box
5040 NEXT X:NEXT Y
5050 RETURN
6000 REM Next level
6010 PRINT CHR$(147)
6020 PRINT:PRINT:PRINT
6030 PRINT "LEVEL ";LEVEL;" COMPLETE!"
6040 PRINT "MOVES: ";MOVES
6050 FOR I=1 TO 150:NEXT I:REM Pause
6060 LEVEL=LEVEL+1
6070 IF LEVEL>MAXLEVEL THEN GOSUB 7000:END:REM All levels done
6080 GOSUB 2000:REM Load next level
6090 RETURN
7000 REM Game complete
7010 PRINT CHR$(147)
7020 PRINT:PRINT:PRINT:PRINT
7030 PRINT TAB(8);"CONGRATULATIONS!"
7040 PRINT:PRINT
7050 PRINT TAB(6);"ALL LEVELS COMPLETED!"
7060 PRINT:PRINT
7070 PRINT TAB(8);"TOTAL MOVES: ";MOVES
7080 RETURN
```

## Hardware Interaction

**Chips Involved:**
- None (text-based, keyboard only)

**Memory Addresses:**
- Screen memory for grid display
- Keyboard buffer for GET

## Common Pitfalls

1. **Box pushed into wall:** Not checking space beyond box
2. **Player walks through boxes:** Not detecting box collision
3. **Wrong win condition:** Checking boxes instead of goals
4. **Can't undo moves:** No move history for undo feature
5. **Level data errors:** Mismatched grid sizes, missing player start

## Extension Ideas

- Add undo system (store move history)
- Add move counter optimization (track best solution)
- Add time limit per level
- Add animated sprites instead of characters
- Add level editor (create custom puzzles)
- Add hints system (show solution path)
- Add box counter (show boxes remaining)

## Builds Toward

**In This Tier:**
- L47: Two-player strategy game with AI opponent
- L48: Package multiple puzzle games together

## Quick Reference

**Grid Codes:**
```
0 = Empty space
1 = Wall (impassable)
2 = Box (can be pushed)
3 = Goal (target location)
4 = Box on goal (win condition)
5 = Player
```

**Movement Pattern:**
```basic
10 NEW_X = PLAYER_X + DX
20 NEW_Y = PLAYER_Y + DY
30 IF GRID(NEW_X, NEW_Y) = WALL THEN RETURN
40 IF GRID(NEW_X, NEW_Y) = EMPTY THEN [move player]
50 IF GRID(NEW_X, NEW_Y) = BOX THEN [try push box]
```

**Box Push Pattern:**
```basic
10 BOX_NEW_X = NEW_X + DX
20 BOX_NEW_Y = NEW_Y + DY
30 IF GRID(BOX_NEW_X, BOX_NEW_Y) <> EMPTY THEN RETURN (blocked)
40 GRID(BOX_NEW_X, BOX_NEW_Y) = BOX
50 GRID(NEW_X, NEW_Y) = EMPTY
60 PLAYER_X = NEW_X: PLAYER_Y = NEW_Y
```

**Win Condition:**
```basic
10 WIN = TRUE
20 FOR each GOAL in grid
30 IF GOAL does not have BOX THEN WIN = FALSE
40 NEXT
50 IF WIN THEN [level complete]
```

**Level Design Tips:**
- **Level 1:** 2 boxes, obvious solution (tutorial)
- **Level 2-3:** 3-4 boxes, introduce corners
- **Level 4-5:** 5 boxes, tight spaces, multiple paths
- **Level 6-7:** 6 boxes, box ordering matters
- **Level 8:** 6-7 boxes, complex multi-step solution

**Common Puzzle Patterns:**
- **Corner trap:** Box pushed to corner can't be moved
- **Chain push:** Push box A to reach box B
- **Goal blocking:** Box on wrong goal blocks access
- **Path creation:** Use boxes to create walkable path

**Display Characters:**
```
@ = Player
O = Box
. = Goal
* = Box on goal
█ = Wall (CHR$(160))
  = Empty space
```

**Performance Note:**
"Grid-based puzzle game has zero performance issues in BASIC. Grid updates are instant. Player input is responsive. No animation or real-time movement—pure turn-based logic. 12×12 grid with box pushing calculations completes instantly. BASIC excels at this genre."
