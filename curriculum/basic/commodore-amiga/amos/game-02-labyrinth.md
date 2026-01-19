# Game 02: Labyrinth

**Track:** AMOS
**Genre:** Maze Navigation
**Units:** 8
**BASIC Version:** AMOS Professional

---

## Overview

Navigate through mazes using Bobs (blitter objects). Introduction to tile-based collision.

### What You Build

- Tile-based maze
- Player bob movement
- Wall collision
- Exit detection
- Multiple mazes

---

## Unit Breakdown

### Unit 1: Bobs vs Sprites
**Concepts:** Bob, Paste Bob, differences

### Unit 2: Maze Drawing
**Concepts:** Tile array, drawing walls

### Unit 3: Player Movement
**Concepts:** Joy(), joystick input

### Unit 4: Collision Detection
**Concepts:** Tile checking, blocking

### Unit 5: The Exit
**Concepts:** Goal tile, level complete

### Unit 6: Multiple Mazes
**Concepts:** Level data, loading

### Unit 7: Timer Challenge
**Concepts:** Time pressure, scoring

### Unit 8: Polish
**Concepts:** Title screen, transitions

---

## Bobs vs Sprites

```basic
' SPRITES: Hardware, limited to 8
Sprite 1,100,100,1

' BOBS: Software blitter objects, unlimited
Bob 1,100,100,1
' Bobs need Double Buffer:
Double Buffer
Bob Clear : Bob Draw
```

---

## Skills Learned

- Bob graphics
- Double buffering
- Tile-based maps
- Joystick input (Joy)
- Collision detection
