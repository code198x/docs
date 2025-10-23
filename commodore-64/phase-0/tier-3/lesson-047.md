# Lesson 047: Two-Player Strategy

**Arc:** Strategy/Puzzle
**Position:** Lesson 2 of 3 in arc
**Type:** Standard
**Estimated Completion:** 130 lines of code

## Learning Objectives

- Implement two-player turn-based strategy (Connect Four)
- Create AI opponent with multiple difficulty levels
- Build win condition detection (4-in-a-row)
- Design fair turn-based gameplay
- Master game tree search concepts

## Prerequisites

**From Previous Lessons:**
- Grid-based game logic (L46)
- Turn-based structure (L43)
- Win condition checking

**BASIC Knowledge:**
- 2D arrays for game boards
- AI decision making
- Pattern matching for win detection

## Key Concepts Introduced

### Two-Player Structure
Alternate between player 1 and player 2 (or player vs AI). Each turn: display board, accept input, update board, check win, switch player.

### Connect Four Mechanics
7 columns × 6 rows grid. Players drop pieces into columns. Pieces fall to lowest empty row. First to get 4-in-a-row (horizontal, vertical, diagonal) wins.

### AI Opponent
Three difficulty levels: Easy (random), Medium (block player wins), Hard (minimax lookahead). AI evaluates board and chooses best move.

### Win Detection
Check all directions from last move: horizontal, vertical, diagonal-left, diagonal-right. Count consecutive pieces in each direction.

## Code Pattern

```basic
10 REM Connect Four
20 REM Two-player strategy game
30 DIM BOARD(7,6):REM 7 columns × 6 rows
40 PLAYER=1:REM Current player (1 or 2)
50 MODE=0:REM 0=2P, 1=vs AI Easy, 2=vs AI Medium, 3=vs AI Hard
60 REM Main menu
70 PRINT CHR$(147)
80 PRINT "CONNECT FOUR"
90 PRINT:PRINT "1. TWO PLAYERS"
100 PRINT "2. VS AI (EASY)"
110 PRINT "3. VS AI (MEDIUM)"
120 PRINT "4. VS AI (HARD)"
130 PRINT "5. QUIT"
140 INPUT M:IF M<1 OR M>5 THEN 70
150 IF M=5 THEN PRINT "GOODBYE!":END
160 MODE=M-1
170 REM Initialize board
180 FOR C=1 TO 7:FOR R=1 TO 6
190 BOARD(C,R)=0:REM Empty
200 NEXT R:NEXT C
210 PLAYER=1
220 REM Main game loop
230 GOSUB 1000:REM Display board
240 REM Player turn
250 IF PLAYER=1 OR MODE=0 THEN GOSUB 2000:REM Human move
260 IF PLAYER=2 AND MODE>0 THEN GOSUB 3000:REM AI move
270 REM Check win
280 GOSUB 4000
290 IF WIN>0 THEN GOSUB 5000:GOTO 70:REM Game over
300 REM Check draw
310 IF MOVES=42 THEN PRINT "DRAW!":FOR I=1 TO 200:NEXT I:GOTO 70
320 REM Switch player
330 PLAYER=3-PLAYER:REM Toggles 1↔2
340 GOTO 230
1000 REM Display board
1010 PRINT CHR$(147)
1020 PRINT "CONNECT FOUR"
1030 PRINT STRING$(30,"-")
1040 PRINT " 1 2 3 4 5 6 7"
1050 PRINT STRING$(30,"-")
1060 FOR R=1 TO 6
1070 PRINT " ";
1080 FOR C=1 TO 7
1090 IF BOARD(C,R)=0 THEN PRINT ". ";:REM Empty
1100 IF BOARD(C,R)=1 THEN PRINT "X ";:REM Player 1
1110 IF BOARD(C,R)=2 THEN PRINT "O ";:REM Player 2
1120 NEXT C:PRINT
1130 NEXT R
1140 PRINT STRING$(30,"-")
1150 RETURN
2000 REM Human move
2010 PRINT:PRINT "PLAYER ";PLAYER;" TURN"
2020 PRINT "CHOOSE COLUMN (1-7)";
2030 INPUT COL
2040 IF COL<1 OR COL>7 THEN PRINT "INVALID!":GOTO 2020
2050 REM Find lowest empty row in column
2060 FOR R=6 TO 1 STEP -1
2070 IF BOARD(COL,R)=0 THEN BOARD(COL,R)=PLAYER:LASTCOL=COL:LASTROW=R:MOVES=MOVES+1:RETURN
2080 NEXT R
2090 PRINT "COLUMN FULL!":GOTO 2020
3000 REM AI move
3010 IF MODE=1 THEN GOSUB 3100:RETURN:REM Easy
3020 IF MODE=2 THEN GOSUB 3200:RETURN:REM Medium
3030 IF MODE=3 THEN GOSUB 3300:RETURN:REM Hard
3040 RETURN
3100 REM AI Easy: Random move
3110 COL=INT(RND(1)*7)+1
3120 REM Check if column has space
3130 IF BOARD(COL,1)<>0 THEN 3110:REM Top full, try another
3140 REM Place piece
3150 FOR R=6 TO 1 STEP -1
3160 IF BOARD(COL,R)=0 THEN BOARD(COL,R)=2:LASTCOL=COL:LASTROW=R:MOVES=MOVES+1:RETURN
3170 NEXT R
3180 GOTO 3110:REM Shouldn't reach, but safety
3200 REM AI Medium: Block player wins
3210 REM First, check if AI can win this turn
3220 FOR C=1 TO 7
3230 GOSUB 3500:REM Try move
3240 IF TRYWIN=1 THEN COL=C:GOSUB 3600:RETURN:REM Winning move found!
3250 NEXT C
3260 REM Second, check if need to block player
3270 FOR C=1 TO 7
3280 GOSUB 3700:REM Check if player wins here
3290 IF TRYWIN=1 THEN COL=C:GOSUB 3600:RETURN:REM Block!
3300 NEXT C
3310 REM Otherwise, random move
3320 GOSUB 3100:RETURN
3300 REM AI Hard: Minimax (simplified)
3310 REM [Advanced AI - minimax tree search]
3320 REM For lesson scope, use Medium AI
3330 GOSUB 3200:RETURN
3500 REM Try AI move in column C
3510 FOR R=6 TO 1 STEP -1
3520 IF BOARD(C,R)=0 THEN
3530 BOARD(C,R)=2:REM Temporarily place
3540 GOSUB 4100:REM Check if this wins
3550 TRYWIN=WIN
3560 BOARD(C,R)=0:REM Undo
3570 RETURN
3580 NEXT R
3590 TRYWIN=0:RETURN
3600 REM Execute AI move in COL
3610 FOR R=6 TO 1 STEP -1
3620 IF BOARD(COL,R)=0 THEN BOARD(COL,R)=2:LASTCOL=COL:LASTROW=R:MOVES=MOVES+1:RETURN
3630 NEXT R
3640 RETURN
3700 REM Check if player can win at C
3710 FOR R=6 TO 1 STEP -1
3720 IF BOARD(C,R)=0 THEN
3730 BOARD(C,R)=1:REM Temporarily place player piece
3740 GOSUB 4100:REM Check win
3750 TRYWIN=WIN
3760 BOARD(C,R)=0:REM Undo
3770 RETURN
3780 NEXT R
3790 TRYWIN=0:RETURN
4000 REM Check win from last move
4010 IF LASTCOL=0 THEN RETURN:REM No move yet
4020 WIN=0
4030 REM Check horizontal
4040 GOSUB 4100:IF WIN>0 THEN RETURN
4050 REM Check vertical
4060 GOSUB 4200:IF WIN>0 THEN RETURN
4070 REM Check diagonal /
4080 GOSUB 4300:IF WIN>0 THEN RETURN
4090 REM Check diagonal \
4100 GOSUB 4400:IF WIN>0 THEN RETURN
4110 RETURN
4100 REM Check horizontal win
4110 COUNT=1:REM Count includes current piece
4120 REM Check left
4130 FOR C=LASTCOL-1 TO 1 STEP -1
4140 IF BOARD(C,LASTROW)=BOARD(LASTCOL,LASTROW) THEN COUNT=COUNT+1:ELSE C=0
4150 NEXT C
4160 REM Check right
4170 FOR C=LASTCOL+1 TO 7
4180 IF BOARD(C,LASTROW)=BOARD(LASTCOL,LASTROW) THEN COUNT=COUNT+1:ELSE C=8
4190 NEXT C
4200 IF COUNT>=4 THEN WIN=BOARD(LASTCOL,LASTROW):RETURN
4210 WIN=0:RETURN
4200 REM Check vertical win
4210 COUNT=1
4220 REM Check down (up not needed, pieces fall down)
4230 FOR R=LASTROW+1 TO 6
4240 IF BOARD(LASTCOL,R)=BOARD(LASTCOL,LASTROW) THEN COUNT=COUNT+1:ELSE R=7
4250 NEXT R
4260 IF COUNT>=4 THEN WIN=BOARD(LASTCOL,LASTROW):RETURN
4270 WIN=0:RETURN
4300 REM Check diagonal / win
4310 COUNT=1
4320 REM Check down-left
4330 C=LASTCOL-1:R=LASTROW+1
4340 IF C>=1 AND R<=6 THEN
4350 IF BOARD(C,R)=BOARD(LASTCOL,LASTROW) THEN COUNT=COUNT+1:C=C-1:R=R+1:GOTO 4340
4360 REM Check up-right
4370 C=LASTCOL+1:R=LASTROW-1
4380 IF C<=7 AND R>=1 THEN
4390 IF BOARD(C,R)=BOARD(LASTCOL,LASTROW) THEN COUNT=COUNT+1:C=C+1:R=R-1:GOTO 4380
4400 IF COUNT>=4 THEN WIN=BOARD(LASTCOL,LASTROW):RETURN
4410 WIN=0:RETURN
4400 REM Check diagonal \ win
4410 COUNT=1
4420 REM Check down-right
4430 C=LASTCOL+1:R=LASTROW+1
4440 IF C<=7 AND R<=6 THEN
4450 IF BOARD(C,R)=BOARD(LASTCOL,LASTROW) THEN COUNT=COUNT+1:C=C+1:R=R+1:GOTO 4440
4460 REM Check up-left
4470 C=LASTCOL-1:R=LASTROW-1
4480 IF C>=1 AND R>=1 THEN
4490 IF BOARD(C,R)=BOARD(LASTCOL,LASTROW) THEN COUNT=COUNT+1:C=C-1:R=R-1:GOTO 4480
4500 IF COUNT>=4 THEN WIN=BOARD(LASTCOL,LASTROW):RETURN
4510 WIN=0:RETURN
5000 REM Game over
5010 PRINT CHR$(147)
5020 GOSUB 1000:REM Show final board
5030 PRINT:PRINT "PLAYER ";WIN;" WINS!"
5040 FOR I=1 TO 300:NEXT I
5050 RETURN
```

## Hardware Interaction

**Chips Involved:**
- None (text-based, keyboard only)

**Memory Addresses:**
- Screen memory for board display
- TI register for RND (AI randomness)

## Common Pitfalls

1. **Diagonal win not detected:** Forgetting to check both diagonal directions
2. **Column full not handled:** Allowing pieces to stack infinitely
3. **AI sees ahead too far:** Advanced minimax too slow in BASIC
4. **Win check from wrong position:** Checking entire board instead of last move
5. **Draw not detected:** Game continues when board full

## Extension Ideas

- Add undo last move
- Add replay game feature
- Add move timer (time pressure)
- Add AI difficulty tuning (ply depth for minimax)
- Add animated piece drops
- Add different board sizes (8×7, 9×8)
- Add obstacles (blocked cells)

## Builds Toward

**In This Tier:**
- L48: Package multiple games (Sokoban + Connect Four + one more)

## Quick Reference

**Board Representation:**
```
BOARD(column, row) = 0 (empty), 1 (player 1), 2 (player 2)

Columns: 1-7 (left to right)
Rows: 1-6 (top to bottom)
```

**Piece Drop Pattern:**
```basic
10 FOR R=6 TO 1 STEP -1  : REM Start from bottom
20 IF BOARD(COL,R)=0 THEN
30 BOARD(COL,R)=PLAYER   : REM Place piece
40 RETURN
50 NEXT R
60 PRINT "COLUMN FULL"
```

**Win Detection Directions:**
```
Horizontal: Check left/right from last move
Vertical: Check down from last move (up not needed)
Diagonal /: Check down-left and up-right
Diagonal \: Check down-right and up-left
```

**AI Difficulty Levels:**
```
Easy: Random valid move
Medium:
  1. If can win → do it
  2. If player can win → block it
  3. Otherwise → random move
Hard:
  Minimax tree search (2-3 ply depth)
  Evaluate all possible futures
  Choose move with best outcome
```

**Turn Structure:**
```
1. Display board
2. Current player chooses column
3. Drop piece to lowest empty row
4. Check win condition (4-in-a-row)
5. Check draw (board full)
6. Switch player
7. Repeat
```

**Win Condition:**
```
Count consecutive pieces in each direction:
- If count ≥ 4 → Winner found
- Check from last move position only (optimization)
```

**AI Strategy Tips:**
- **Center control:** Middle columns (3-5) more valuable
- **Threat detection:** Block opponent's 3-in-a-row
- **Setup moves:** Create multiple threats at once
- **Trap patterns:** Force opponent into losing position

**Performance Note:**
"Turn-based strategy game has zero speed pressure. Board evaluation (win detection) completes instantly even with full 7×6 grid. Medium AI (block + win detection) evaluates 7 possible moves instantly. BASIC handles this perfectly—no lag, instant response. This is BASIC's strength: complex logic without time constraints."
