# BASIC Curricula: Pattern Library Entries

**Purpose:** Document reusable game programming patterns from the BASIC curriculum that apply across platforms and languages.

**Last Updated:** 2026-01-18

---

## Overview

These patterns emerged from the BASIC game specifications and represent fundamental game programming techniques that transfer to any language.

---

## Pattern 1: Number Guessing Loop

**Games:** Psychic Computer, Think of a Number
**Complexity:** Beginner

### Problem
Create a simple game loop where the computer picks a number and the player guesses until correct.

### Pattern

```
1. Generate random target
2. Loop:
   a. Get player guess
   b. Compare to target
   c. Give feedback (higher/lower)
   d. If correct, exit loop
3. Display results
```

### Implementation (Generic BASIC)

```basic
target = INT(RND * 100) + 1
attempts = 0
DO
  INPUT "Guess"; guess
  attempts = attempts + 1
  IF guess > target THEN PRINT "Too high!"
  IF guess < target THEN PRINT "Too low!"
LOOP UNTIL guess = target
PRINT "Correct in"; attempts; "tries!"
```

### Applications
- Binary search teaching
- Hot/cold games
- Code-breaking games

---

## Pattern 2: Text Adventure Parser

**Games:** The Forgotten Key, The Cursed Manor
**Complexity:** Intermediate

### Problem
Parse player input into verb and noun for adventure game commands.

### Pattern

```
1. Get input string
2. Find space position
3. Extract verb (before space)
4. Extract noun (after space)
5. Route to handler based on verb
```

### Implementation

```basic
INPUT "> "; cmd$
sp = INSTR(cmd$, " ")
IF sp > 0 THEN
  verb$ = LEFT$(cmd$, sp-1)
  noun$ = MID$(cmd$, sp+1)
ELSE
  verb$ = cmd$
  noun$ = ""
END IF

SELECT CASE verb$
  CASE "GO", "WALK": GOSUB MoveHandler
  CASE "GET", "TAKE": GOSUB GetHandler
  CASE "DROP": GOSUB DropHandler
  CASE "LOOK", "EXAMINE": GOSUB LookHandler
END SELECT
```

### Applications
- Text adventures
- Command-line interfaces
- Chat bots

---

## Pattern 3: Snake Body Queue

**Games:** Pixel Serpent, Spectrum Serpent, Venom
**Complexity:** Intermediate

### Problem
Manage a snake that grows and moves, with the tail following the head.

### Pattern

```
1. Store body segments in circular array
2. Add new head position to front
3. Remove tail position from back
4. On growth, skip tail removal
```

### Implementation

```basic
DIM bodyX(100), bodyY(100)
head = 0 : tail = 0 : length = 3

SUB MoveSnake(newX, newY)
  ' Add new head
  head = (head + 1) MOD 100
  bodyX(head) = newX
  bodyY(head) = newY

  ' Remove tail (unless growing)
  IF NOT growing THEN
    tail = (tail + 1) MOD 100
  END IF
END SUB
```

### Key Insight
Circular buffer avoids shifting array elements - O(1) instead of O(n).

### Applications
- Snake games
- Trail effects
- History buffers

---

## Pattern 4: Ball Physics (Breakout)

**Games:** Wall Smasher, Block Breaker, Barrier Bash
**Complexity:** Intermediate

### Problem
Implement bouncing ball with angle reflection.

### Pattern

```
1. Store position (x, y) and velocity (dx, dy)
2. Each frame: add velocity to position
3. On wall collision: negate appropriate velocity component
4. On paddle collision: adjust angle based on hit position
```

### Implementation

```basic
' Movement
x = x + dx : y = y + dy

' Wall bounce
IF x < 0 OR x > screenWidth THEN dx = -dx
IF y < 0 THEN dy = -dy

' Paddle bounce with angle
IF y > paddleY AND x > paddleX AND x < paddleX + paddleWidth THEN
  dy = -dy
  ' Angle based on hit position
  hitPos = (x - paddleX) / paddleWidth  ' 0 to 1
  dx = (hitPos - 0.5) * maxAngle
END IF
```

### Applications
- Breakout clones
- Pong variants
- Pinball

---

## Pattern 5: Gravity and Jumping

**Games:** Jump Quest, Miner Mick, Hop Island
**Complexity:** Intermediate

### Problem
Implement realistic jumping with gravity.

### Pattern

```
1. Apply gravity to vertical velocity each frame
2. Add velocity to position
3. Check for ground collision
4. On jump input (if grounded): set upward velocity
```

### Implementation

```basic
GRAVITY = 0.5
JUMP_POWER = -8

' Apply gravity
vy = vy + GRAVITY
y = y + vy

' Ground collision
IF y > groundY THEN
  y = groundY
  vy = 0
  grounded = TRUE
ELSE
  grounded = FALSE
END IF

' Jump
IF jumpPressed AND grounded THEN
  vy = JUMP_POWER
END IF
```

### Key Values
- Gravity: 0.3-0.8 per frame (affects fall speed)
- Jump power: -6 to -12 (affects jump height)
- Ratio determines "feel"

### Applications
- Platformers
- Any jumping mechanic

---

## Pattern 6: Match-3 Detection

**Games:** Match Gems
**Complexity:** Intermediate

### Problem
Detect and remove matching gems in a grid.

### Pattern

```
1. Scan all rows for 3+ horizontal matches
2. Scan all columns for 3+ vertical matches
3. Mark matched cells
4. Remove marked cells
5. Drop remaining cells down
6. Fill empty top cells
7. Repeat until no matches
```

### Implementation

```basic
SUB CheckMatches
  ' Horizontal check
  FOR y = 0 TO gridHeight-1
    FOR x = 0 TO gridWidth-3
      IF grid(x,y) = grid(x+1,y) AND grid(x,y) = grid(x+2,y) THEN
        marked(x,y) = TRUE
        marked(x+1,y) = TRUE
        marked(x+2,y) = TRUE
      END IF
    NEXT x
  NEXT y

  ' Vertical check (similar)
  ' ...
END SUB

SUB DropGems
  FOR x = 0 TO gridWidth-1
    writeY = gridHeight-1
    FOR y = gridHeight-1 TO 0 STEP -1
      IF NOT marked(x,y) THEN
        grid(x,writeY) = grid(x,y)
        writeY = writeY - 1
      END IF
    NEXT y
    ' Fill top with new gems
    FOR y = writeY TO 0 STEP -1
      grid(x,y) = RandomGem()
    NEXT y
  NEXT x
END SUB
```

### Applications
- Puzzle games
- Pattern matching
- Tile-based games

---

## Pattern 7: Top-Down Car Physics

**Games:** Speed Circuit, Speed Demon, Road Rage
**Complexity:** Advanced

### Problem
Implement car movement with steering, acceleration, and drift.

### Pattern

```
1. Store angle, speed, velocity vector
2. Steering changes angle (reduced at high speed)
3. Acceleration adds to speed
4. Calculate target velocity from angle and speed
5. Lerp actual velocity toward target (grip factor)
6. Apply friction
```

### Implementation

```basic
' Steering (less effective at speed)
IF leftPressed THEN angle = angle - turnRate * (1 - speed/maxSpeed * 0.5)
IF rightPressed THEN angle = angle + turnRate * (1 - speed/maxSpeed * 0.5)

' Acceleration
IF upPressed THEN speed = speed + acceleration
IF downPressed THEN speed = speed - braking

' Target velocity from angle
targetVX = COS(angle) * speed
targetVY = SIN(angle) * speed

' Lerp toward target (grip)
vx = vx + (targetVX - vx) * grip
vy = vy + (targetVY - vy) * grip

' Move
x = x + vx : y = y + vy

' Friction
speed = speed * friction
```

### Grip Factor
- High grip (0.8-1.0): Tight handling
- Low grip (0.2-0.5): Drifty, slidey
- Surface-dependent: Tarmac vs grass

### Applications
- Racing games
- Driving sections
- Vehicle combat

---

## Pattern 8: Destructible Terrain

**Games:** Artillery Duel
**Complexity:** Advanced

### Problem
Create terrain that can be destroyed by explosions (Worms-style).

### Pattern

```
1. Terrain stored as bitmap
2. Draw explosion as filled circle in background colour
3. Check collision by reading pixel colour
4. Projectiles fall through destroyed areas
```

### Implementation

```basic
' Check if point is solid terrain
FUNCTION IsTerrain(x, y)
  colour = GetPixel(terrainBitmap, x, y)
  RETURN colour <> backgroundColour
END FUNCTION

' Destroy terrain at explosion
SUB Explode(cx, cy, radius)
  ' Draw circle in background colour
  CircleFill terrainBitmap, cx, cy, radius, backgroundColour

  ' Apply damage to nearby units
  FOR each unit
    dist = Distance(unit.x, unit.y, cx, cy)
    IF dist < radius THEN
      damage = (radius - dist) / radius * maxDamage
      unit.health = unit.health - damage
    END IF
  NEXT
END SUB
```

### Applications
- Worms-style games
- Mining games
- Destructible environments

---

## Pattern 9: Turn-Based Game Loop

**Games:** Battle Grid, Artillery Duel
**Complexity:** Intermediate

### Problem
Structure a game where players take turns.

### Pattern

```
1. Game state machine: SELECT, MOVE, ATTACK, END_TURN
2. Current player variable
3. Each unit tracks: hasMoved, hasAttacked
4. End turn resets flags, switches player
```

### Implementation

```basic
currentPlayer = 1
gameState = STATE_SELECT

DO
  SELECT CASE gameState
    CASE STATE_SELECT
      HandleUnitSelection
    CASE STATE_MOVE
      HandleMovement
    CASE STATE_ATTACK
      HandleAttack
    CASE STATE_AI
      RunAITurn
  END SELECT

  IF endTurnPressed THEN
    EndTurn
  END IF
LOOP

SUB EndTurn
  ' Reset unit actions
  FOR each unit WHERE unit.team = currentPlayer
    unit.hasMoved = FALSE
    unit.hasAttacked = FALSE
  NEXT

  ' Switch player
  currentPlayer = 3 - currentPlayer  ' Toggle 1<->2
  IF currentPlayer = 2 AND isAI THEN
    gameState = STATE_AI
  ELSE
    gameState = STATE_SELECT
  END IF
END SUB
```

### Applications
- Strategy games
- Board game adaptations
- RPG combat

---

## Pattern 10: Projectile Arc (Artillery)

**Games:** Artillery Duel
**Complexity:** Intermediate

### Problem
Fire projectile with angle and power, affected by gravity and wind.

### Pattern

```
1. Convert angle/power to initial velocity
2. Each frame: apply gravity to vy, wind to vx
3. Move projectile
4. Check terrain collision
5. On hit: explode
```

### Implementation

```basic
' Fire projectile
vx = COS(angle * PI / 180) * power / 10
vy = -SIN(angle * PI / 180) * power / 10  ' Negative: up is negative y

' Projectile loop
DO
  ' Apply forces
  vy = vy + gravity
  vx = vx + wind / 100

  ' Move
  x = x + vx
  y = y + vy

  ' Check collision
  IF IsTerrain(x, y) THEN
    Explode x, y, blastRadius
    EXIT DO
  END IF

  ' Draw
  Plot x, y
  WaitFrame
LOOP WHILE InBounds(x, y)
```

### Applications
- Artillery games
- Sports (golf, basketball arc)
- Throwing mechanics

---

## Summary

| Pattern | Complexity | Key Technique |
|---------|------------|---------------|
| Number Guess Loop | Beginner | Basic game loop |
| Text Adventure Parser | Intermediate | String parsing |
| Snake Body Queue | Intermediate | Circular buffer |
| Ball Physics | Intermediate | Velocity reflection |
| Gravity/Jumping | Intermediate | Physics integration |
| Match-3 Detection | Intermediate | Grid scanning |
| Car Physics | Advanced | Velocity lerping |
| Destructible Terrain | Advanced | Bitmap manipulation |
| Turn-Based Loop | Intermediate | State machine |
| Projectile Arc | Intermediate | Physics simulation |

**Total new patterns: 10**

These patterns transcend BASIC - they apply to any game programming language.
