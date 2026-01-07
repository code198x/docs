# Maze Raider: 64-Unit Outline

**Game:** C64 Game 3: Maze Raider
**Units:** 64
**Prerequisites:** SID Symphony (Game 1), Starfield (Game 2)
**Concept:** Pac-Man style maze chase. Navigate corridors, collect pellets, avoid ghosts, use power-ups to turn the tables.

**Commercial Quality Target:** A game comparable to Pac-Man, Ms. Pac-Man, or Lady Bug. Multiple mazes, smart enemy AI, power-ups, bonus items, smooth character movement. Something that would have competed with maze games in 1983-85.

---

## Skill Progression

### Skills Applied from Previous Games

| Skill | Origin | Application in Maze Raider |
|-------|--------|---------------------------|
| Program structure, BASIC stub | SID Symphony 1-2 | Assumed |
| Screen memory, colour RAM | SID Symphony 5 | Maze display, pellets |
| Custom character sets | SID Symphony 6 | **Deep expansion** - maze graphics |
| Game loop, raster sync | SID Symphony 7 | Applied |
| Data structures | SID Symphony 8, Starfield 6 | Maze data, enemy arrays |
| Score display | SID Symphony 13 | Applied directly |
| Lives system | SID Symphony 15, Starfield 10 | Applied with maze context |
| State machines | SID Symphony 16-17 | Game states, ghost modes |
| Menus, title screens | SID Symphony 33-34 | Applied |
| SID sound effects | SID Symphony 41-43 | Pellet sounds, power-up, death |
| SID music | Starfield 40-41 | Maze music, ghost chase music |
| High scores | SID Symphony 45 | Applied |
| Sprite basics | Starfield 1-5 | Player and ghost sprites |
| Sprite animation | Starfield 35-36 | Character animations |
| Enemy AI concepts | Starfield 13, 19-20 | **Deep expansion** - chase AI |
| Collision concepts | Starfield 8 | Adapted for tile collision |
| Polish methodology | Both games | Applied |
| Optimisation | Both games | Applied |

### New Skills Introduced

| New Skill | Description |
|-----------|-------------|
| Tile-based maps | Maze as grid of tiles |
| Tile collision | Wall detection via map data |
| Character graphics (deep) | Full custom charset for maze |
| Grid-based movement | Snap-to-grid movement |
| Smooth tile transitions | Pixel movement between tiles |
| Pathfinding basics | Ghost chase algorithms |
| Scatter/chase modes | Ghost behaviour states |
| Power-up state changes | Enemies become vulnerable |
| Collectible systems | Pellets, power pellets, fruit |
| Level progression | Multiple maze layouts |
| Map data format | Efficient maze storage |
| Intersection detection | Decision points for AI |
| Target tile selection | Ghost targeting strategies |

---

## The Finished Game

### Core Gameplay
- Player navigates maze corridors
- Collect all pellets to complete level
- Avoid four ghosts with distinct personalities
- Power pellets make ghosts vulnerable
- Eat vulnerable ghosts for bonus points
- Bonus fruit appears periodically

### Characters
- **Player:** Animated character (mouth opening/closing or similar)
- **Blinky (Red):** Aggressive, targets player directly
- **Pinky (Pink):** Ambusher, targets ahead of player
- **Inky (Cyan):** Unpredictable, complex targeting
- **Clyde (Orange):** Shy, retreats when close

### Mazes
- 8 distinct maze layouts
- Increasing complexity
- Different pellet patterns
- Varying ghost house positions
- Progressive difficulty

### Features
- Power pellets (4 per maze)
- Bonus fruit (cherry, strawberry, orange, etc.)
- Ghost house with release timing
- Scatter mode (ghosts retreat to corners)
- Chase mode (ghosts pursue player)
- Frightened mode (after power pellet)
- Wraparound tunnels
- Intermission screens between mazes

### Audio
- Waka-waka eating sound
- Power pellet dramatic sound
- Ghost eaten sound
- Death melody
- Level complete jingle
- Background music (optional, or silence like original)

---

## Phase 1: Foundation (Units 1-16)

*Goal: Core maze gameplay. Player moves through maze, collects pellets, one ghost chases. Collision with walls and ghost works.*

---

### Unit 1: Maze Character Set Design

**Prerequisites:** Custom characters (SID Symphony 6)

**Learning Objectives:**
- Design complete maze character set
- Understand tile-based graphics
- Plan maze visual style
- Create cohesive visual language

**Concepts Introduced:**
- Tile set design (walls, corners, intersections)
- Character reuse patterns
- Visual consistency
- Maze aesthetics

**Code Written:**
```
- Design maze wall characters (horizontal, vertical, corners)
- Design pellet character
- Design power pellet character
- Design empty corridor character
- Load custom charset
```

**What the Learner Sees:**
Custom characters ready for maze construction. Walls, pellets, corridors all designed. Foundation for maze display.

**Reference to SID Symphony:**
"We built custom characters in Unit 6. Now we're creating a complete tile set for a different purpose - maze construction rather than game UI."

---

### Unit 2: Maze Data Format

**Prerequisites:** Data structures (SID Symphony 8, Starfield 6)

**Learning Objectives:**
- Design efficient maze storage
- Understand tile map concepts
- Create first maze layout
- Plan for multiple mazes

**Concepts Introduced:**
- Tile map data format
- Tile types (wall, pellet, power, empty, tunnel)
- 40x25 or subset grid
- Maze as data

**Code Written:**
```
- Define tile type constants
- Create maze data array (40x21 visible area)
- First maze layout
- Maze header (dimensions, pellet count)
```

**What the Learner Sees:**
Maze exists as data. Not yet displayed, but structure defined.

**Data Format:**
```
; Tile types
TILE_WALL   = 0
TILE_PELLET = 1
TILE_POWER  = 2
TILE_EMPTY  = 3
TILE_TUNNEL = 4

maze_1:
    !byte 0,0,0,0,0,0,0,0,0,0...  ; Top wall
    !byte 0,1,1,1,1,1,1,1,1,0...  ; Pellet row
    ; etc.
```

---

### Unit 3: Maze Rendering

**Prerequisites:** Screen memory (SID Symphony 5)

**Learning Objectives:**
- Render maze from data
- Map tiles to characters
- Set up maze colours
- Efficient rendering

**Concepts Introduced:**
- Tile-to-character mapping
- Row-by-row rendering
- Colour RAM for maze
- Render optimisation

**Code Written:**
```
- render_maze: draw entire maze from data
- Tile type to character lookup
- Set wall colours
- Set pellet colours
- HUD area reserved
```

**What the Learner Sees:**
Complete maze displayed on screen. Walls, pellets, power pellets all visible. Looks like a maze game.

**Reference to SID Symphony:**
"Screen memory manipulation from Unit 5. Now we're writing a whole screen's worth of custom characters."

---

### Unit 4: Player Sprite

**Prerequisites:** Sprites (Starfield 1-5)

**Learning Objectives:**
- Create player sprite
- Position over maze
- Sprite-over-character display
- Player visual design

**Concepts Introduced:**
- Sprite priority over characters
- Character grid alignment
- Player animation frames
- Maze-appropriate sprite

**Code Written:**
```
- Player sprite design (Pac-Man style or unique)
- Animation frames (mouth open/closed or movement)
- Position at maze start position
- Sprite colour and settings
```

**What the Learner Sees:**
Player character appears in the maze. Sprite overlays the character graphics cleanly. Ready to move.

**Reference to Starfield:**
"Same sprite setup from Units 1-2, but positioned over character graphics instead of empty space."

---

### Unit 5: Grid-Based Input

**Prerequisites:** Joystick input (Starfield 3)

**Learning Objectives:**
- Read joystick for 4 directions
- Queue next direction
- Grid-aligned movement concept
- Direction state management

**Concepts Introduced:**
- Direction queueing
- Current vs desired direction
- 4-way movement (no diagonals)
- Movement intent vs movement action

**Code Written:**
```
- Read joystick (applied from Starfield)
- Store desired_direction
- Ignore diagonals (pick one axis)
- Direction constants (UP, DOWN, LEFT, RIGHT)
```

**What the Learner Sees:**
Input detected and direction queued. Player doesn't move yet but direction is tracked.

**Reference to Starfield:**
"Joystick reading from Unit 3. We're restricting to 4-way and queueing direction rather than immediate movement."

---

### Unit 6: Tile Collision Detection

**Learning Objectives:**
- Check if tile is passable
- Read maze data at position
- Convert pixel to tile coordinates
- Foundation for movement

**Concepts Introduced:**
- Pixel to tile conversion
- Tile lookup from coordinates
- Passable vs impassable tiles
- Collision before movement

**Code Written:**
```
- pixel_to_tile: convert X,Y to tile coords
- get_tile: read maze data at tile position
- is_passable: check if tile allows movement
- Wall = not passable, all else = passable
```

**What the Learner Sees:**
No visible change yet. Collision system ready for movement.

**New Technique:**
Unlike Starfield's sprite-sprite collision (hardware), this is data-driven collision - checking the map data directly.

---

### Unit 7: Player Movement - Grid Aligned

**Learning Objectives:**
- Move player between tiles
- Smooth animation between positions
- Snap to grid
- Basic maze navigation

**Concepts Introduced:**
- Tile-to-tile movement
- Movement speed
- Position interpolation
- Grid snapping

**Code Written:**
```
- Player tile position (grid coords)
- Player pixel offset (within tile)
- Move toward next tile
- Snap when reaching tile centre
- Check collision before moving
```

**What the Learner Sees:**
Player moves through maze! Smooth movement between tiles. Stops at walls. Core navigation works.

---

### Unit 8: Direction Changes at Intersections

**Learning Objectives:**
- Detect intersections
- Allow direction change at valid points
- Pre-turn queueing
- Smooth corner navigation

**Concepts Introduced:**
- Intersection detection
- Valid turn checking
- Direction change timing
- Turn queueing window

**Code Written:**
```
- At tile centre: check if desired_direction is valid
- If valid: change current_direction
- If invalid: continue current direction until wall
- Pre-turn: queue turns slightly before intersection
```

**What the Learner Sees:**
Player can turn at intersections. Can queue turns before reaching them. Smooth navigation through corridors.

---

### Unit 9: Pellet Collection

**Prerequisites:** Collectibles concept (new), score (SID Symphony 13)

**Learning Objectives:**
- Detect pellet tiles
- Remove pellet on collection
- Add score
- Track pellets remaining

**Concepts Introduced:**
- Tile modification during play
- Collection detection
- Pellet counter
- Level completion condition

**Code Written:**
```
- On tile centre: check for pellet
- If pellet: increment score, play sound
- Change tile from PELLET to EMPTY
- Update screen character
- Decrement pellets_remaining
```

**What the Learner Sees:**
Collecting pellets! Score increases. Pellets disappear. Satisfying collection loop.

**Reference to SID Symphony:**
"Scoring from Unit 13. Sound effects from Units 41-43. Now triggered by tile collection."

---

### Unit 10: First Ghost

**Prerequisites:** Enemy sprites (Starfield 7)

**Learning Objectives:**
- Add ghost sprite
- Ghost starting position
- Basic ghost movement
- Ghost animation

**Concepts Introduced:**
- Ghost as sprite
- Ghost position tracking
- Ghost direction
- Ghost visual design

**Code Written:**
```
- Ghost sprite design (classic ghost shape)
- Ghost position (tile + pixel)
- Ghost colour (red for Blinky)
- Ghost animation frames
- Position in maze
```

**What the Learner Sees:**
A ghost in the maze! Red ghost visible. Doesn't move intelligently yet but is present.

**Reference to Starfield:**
"Enemy sprites from Unit 7. Same concept, different visual, different behaviour system."

---

### Unit 11: Ghost Movement - Random

**Learning Objectives:**
- Ghost moves through maze
- Random direction at intersections
- Ghost respects walls
- Movement pacing

**Concepts Introduced:**
- Simple ghost AI
- Random decision making
- Same tile collision as player
- Ghost speed

**Code Written:**
```
- Ghost uses same movement system as player
- At intersection: pick random valid direction
- Never reverse direction (ghost rule)
- Move continuously
```

**What the Learner Sees:**
Ghost wanders the maze. Moves randomly at intersections. Feels alive but dumb.

---

### Unit 12: Player-Ghost Collision

**Prerequisites:** Collision (Starfield 8)

**Learning Objectives:**
- Detect player-ghost overlap
- Handle player death
- Death animation
- Respawn

**Concepts Introduced:**
- Sprite-sprite collision for death
- Tile proximity collision (alternative)
- Death state
- Respawn position

**Code Written:**
```
- Check player-ghost distance each frame
- If overlapping: trigger death
- Death animation (player sprite sequence)
- Death sound
- Respawn at start position
- Lose life
```

**What the Learner Sees:**
Ghost kills player on contact. Death animation plays. Life lost. Player respawns. Stakes are real.

**Reference to Starfield:**
"Collision detection concept from Unit 8. Death handling from Unit 10. Applied to maze context."

---

### Unit 13: Ghost AI - Chase Behaviour

**Prerequisites:** Enemy AI (Starfield 13)

**Learning Objectives:**
- Ghost targets player
- Simple pathfinding
- Chase behaviour
- Threat increases

**Concepts Introduced:**
- Target tile concept
- Direction toward target
- Manhattan distance
- Chase mode

**Code Written:**
```
- Ghost target = player tile
- At intersection: pick direction that reduces distance to target
- Manhattan distance calculation
- Ghost now actively chases
```

**What the Learner Sees:**
Ghost chases player intelligently! Follows through maze. Much more threatening. Real tension.

**Reference to Starfield:**
"Enemy AI from Unit 13 expanded. Instead of simple patterns, ghost makes decisions based on player position."

---

### Unit 14: Level Complete

**Learning Objectives:**
- Detect all pellets collected
- Level complete sequence
- Advance to next level
- Reset maze

**Concepts Introduced:**
- Win condition
- Level transition
- Maze reset
- Difficulty progression

**Code Written:**
```
- Check pellets_remaining == 0
- Level complete animation (flash maze)
- Increment level counter
- Reset maze data
- Rerender maze
- Faster ghost (difficulty)
```

**What the Learner Sees:**
Clear all pellets = level complete! Maze flashes. Next level starts. Ghost is slightly faster. Progression.

---

### Unit 15: Power Pellets

**Learning Objectives:**
- Special pellet type
- Ghost state change
- Frightened mode
- Eat ghosts for points

**Concepts Introduced:**
- Power-up state
- Ghost frightened mode
- Role reversal
- Time-limited power

**Code Written:**
```
- Detect power pellet collection
- Set frightened_timer
- Ghost changes colour (blue)
- Ghost reverses direction
- Ghost moves randomly (flee)
- If player touches ghost: ghost eaten, bonus points
```

**What the Learner Sees:**
Power pellet turns the tables! Ghost turns blue and flees. Can eat ghost for big points. Iconic mechanic.

---

### Unit 16: Phase 1 Complete - Core Playtest

**Learning Objectives:**
- Playtest core maze gameplay
- Balance chase difficulty
- Tune power pellet duration
- Document improvements

**Concepts Introduced:**
- Maze game balance
- Chase vs escape balance
- Power timing
- Applied playtesting

**Code Written:**
```
- Playtest session
- Adjust ghost speed
- Tune power pellet duration
- Balance pellet point values
- Document Phase 2 needs
```

**What the Learner Sees:**
Complete core maze game. One ghost, one maze, power pellets. Playable and challenging. Ready for expansion.

**Phase 1 Checkpoint:**
Core Pac-Man gameplay working. Player moves through maze, collects pellets, avoids/eats ghost. One intelligent ghost, one maze layout. Foundation complete.

---

## Phase 2: Expansion (Units 17-32)

*Goal: Full ghost cast, multiple mazes, bonus items, ghost house, scatter/chase modes. Complete maze game content.*

---

### Unit 17: Ghost Personalities - Blinky

**Learning Objectives:**
- Refine Blinky (red) behaviour
- Direct chase targeting
- Aggressive personality
- Speed increases with pellets

**Concepts Introduced:**
- Personality as targeting algorithm
- Cruise Elroy mode (speed up)
- Individual ghost tuning
- Character through behaviour

**Code Written:**
```
- Blinky target = player tile exactly
- Cruise Elroy: speed up when few pellets remain
- Most aggressive ghost
- Always in pursuit
```

**What the Learner Sees:**
Blinky refined. Directly chases. Gets faster as maze empties. Relentless.

---

### Unit 18: Ghost Personalities - Pinky

**Learning Objectives:**
- Add Pinky (pink) ghost
- Ambush targeting
- Target ahead of player
- Complementary to Blinky

**Concepts Introduced:**
- Predictive targeting
- Tiles ahead calculation
- Ambush behaviour
- Ghost cooperation (emergent)

**Code Written:**
```
- Pinky sprite (pink colour)
- Target = 4 tiles ahead of player direction
- Ambush positioning
- Second ghost in maze
```

**What the Learner Sees:**
Two ghosts! Pinky tries to ambush. Works with Blinky to trap player. Tactical challenge.

---

### Unit 19: Ghost Personalities - Inky

**Learning Objectives:**
- Add Inky (cyan) ghost
- Complex targeting
- Unpredictable behaviour
- Three-ghost dynamics

**Concepts Introduced:**
- Vector-based targeting
- Uses Blinky's position
- Unpredictability value
- Complex AI

**Code Written:**
```
- Inky sprite (cyan colour)
- Target = vector from Blinky through point ahead of player, doubled
- Strange, unpredictable paths
- Third ghost in maze
```

**What the Learner Sees:**
Three ghosts with Inky's erratic behaviour. Harder to predict. Increased chaos.

---

### Unit 20: Ghost Personalities - Clyde

**Learning Objectives:**
- Add Clyde (orange) ghost
- Shy/retreat behaviour
- Distance-based mode switch
- Four-ghost complete

**Concepts Introduced:**
- Distance threshold behaviour
- Chase vs scatter per-ghost
- Shy personality
- Full cast

**Code Written:**
```
- Clyde sprite (orange colour)
- If far from player: chase like Blinky
- If close to player: retreat to corner
- Fourth ghost completes cast
```

**What the Learner Sees:**
Four ghosts! Clyde runs away when close. Full ghost cast with distinct personalities.

---

### Unit 21: Ghost House

**Learning Objectives:**
- Central ghost pen
- Ghost release timing
- Exit sequence
- Regeneration point

**Concepts Introduced:**
- Ghost house tiles
- Release timing per ghost
- Exit animation
- Return after eaten

**Code Written:**
```
- Ghost house area in maze
- Ghosts start in house
- Release timer per ghost
- Exit through door
- Return to house when eaten
```

**What the Learner Sees:**
Ghosts emerge from central house. Staggered release. Eaten ghosts return to house. Classic mechanic.

---

### Unit 22: Scatter Mode

**Learning Objectives:**
- Ghosts retreat to corners
- Scatter/chase cycle
- Timer-based mode switching
- Strategic breathing room

**Concepts Introduced:**
- Scatter targets (corners)
- Mode timer
- Global mode state
- Predictable patterns

**Code Written:**
```
- Scatter mode: each ghost targets home corner
- Scatter duration timer
- Switch to chase after timer
- Cycle: scatter → chase → scatter → chase
```

**What the Learner Sees:**
Ghosts periodically retreat to corners. Breathing room for player. Predictable cycles create strategy.

---

### Unit 23: Frightened Mode Polish

**Learning Objectives:**
- Refine frightened behaviour
- Flashing before end
- Speed reduction
- Point escalation

**Concepts Introduced:**
- Frightened flash warning
- Slowed movement
- Escalating points (200, 400, 800, 1600)
- Mode transition

**Code Written:**
```
- Frightened mode slows ghosts
- Flash white/blue when nearly over
- Points: 200 → 400 → 800 → 1600 for consecutive ghosts
- Display point popup
```

**What the Learner Sees:**
Frightened mode polished. Ghost flashes when power ending. Eating multiple ghosts = big points. Strategic depth.

---

### Unit 24: Maze 2 Design

**Learning Objectives:**
- Create second maze layout
- Different challenge
- Visual variety
- Test maze loading

**Concepts Introduced:**
- Multiple maze data
- Maze selection
- Level-to-maze mapping
- Variety through design

**Code Written:**
```
- maze_2 data array
- Different layout, same rules
- Different ghost house position
- Load maze by level number
```

**What the Learner Sees:**
Level 2 has different maze! New layout to learn. Variety in gameplay.

---

### Unit 25: Mazes 3-4 Design

**Learning Objectives:**
- More maze variety
- Increasing complexity
- Tunnel variations
- Ghost house variations

**Concepts Introduced:**
- Maze difficulty curve
- Layout design principles
- Tunnel strategies
- Applied design

**Code Written:**
```
- maze_3: more complex, more dead ends
- maze_4: trickier ghost house access
- Different tunnel positions
- Progressive challenge
```

**What the Learner Sees:**
Four different mazes. Each presents new challenges. Game has depth.

---

### Unit 26: Bonus Fruit

**Learning Objectives:**
- Bonus item spawning
- Different fruit per level
- Collection timing
- Score bonus

**Concepts Introduced:**
- Timed spawns
- Level-based items
- Bonus point values
- Fruit as sprite or character

**Code Written:**
```
- Fruit spawns after N pellets eaten
- Disappears after timer
- Cherry (100), Strawberry (300), Orange (500)...
- Fruit sprite near ghost house
```

**What the Learner Sees:**
Bonus fruit appears mid-level. Grab for extra points. Different fruit each level. Classic mechanic.

---

### Unit 27: Tunnel Wraparound

**Learning Objectives:**
- Screen edge wraparound
- Ghost slowdown in tunnel
- Strategic tunnel use
- Classic escape mechanic

**Concepts Introduced:**
- Wraparound logic
- Position wrapping
- Ghost speed zones
- Escape routes

**Code Written:**
```
- Detect tunnel tile entry
- Wrap position to other side
- Ghosts slow in tunnel
- Player same speed in tunnel
```

**What the Learner Sees:**
Side tunnels wrap around screen. Ghosts slow in tunnels. Strategic escape route.

---

### Unit 28: Intermission Screens

**Learning Objectives:**
- Between-maze cutscenes
- Simple animations
- Story/humour
- Pacing break

**Concepts Introduced:**
- Cutscene state
- Scripted animation
- Non-interactive sequence
- Reward for progress

**Code Written:**
```
- Intermission after every 2 mazes
- Simple animation (ghost chases player, then reverses)
- Humorous moment
- Auto-advance after sequence
```

**What the Learner Sees:**
Little animated scenes between mazes. Charming break. Reward for progress.

---

### Unit 29: Mazes 5-8 Design

**Learning Objectives:**
- Complete maze set
- Advanced layouts
- Expert challenge
- Maze variety complete

**Concepts Introduced:**
- Expert-level design
- Multiple paths emphasis
- Ghost strategies
- Full content

**Code Written:**
```
- maze_5 through maze_8
- Increasingly complex
- Different strategies required
- Full 8-maze rotation
```

**What the Learner Sees:**
Eight complete mazes. Full variety. Game loops after maze 8 with increased difficulty.

---

### Unit 30: Difficulty Progression

**Learning Objectives:**
- Speed increases per level
- Frightened duration decreases
- Scatter/chase timing changes
- Long-term challenge

**Concepts Introduced:**
- Difficulty curves
- Per-level parameters
- Expert loop
- Challenge retention

**Code Written:**
```
- Speed table per level
- Frightened duration table (shorter each level)
- Scatter/chase timing changes
- After level 21: max difficulty
```

**What the Learner Sees:**
Game gets progressively harder. Early levels learnable. Later levels punishing. Infinite skill ceiling.

---

### Unit 31: Extra Life

**Learning Objectives:**
- Bonus life at score threshold
- One-up sound
- Life display
- Reward for skill

**Concepts Introduced:**
- Score threshold bonus
- One-up convention
- Life cap (optional)
- Progress reward

**Code Written:**
```
- Extra life at 10,000 points
- One-up sound effect
- Life counter increases
- Display indicates bonus
```

**What the Learner Sees:**
Hit 10,000 points = extra life! Rewarding sound. Skill rewarded with more chances.

---

### Unit 32: Content Complete Playtest

**Learning Objectives:**
- Full content playtest
- Balance all mazes
- Ghost AI verification
- Document polish needs

**Concepts Introduced:**
- Complete game testing
- Maze balance
- AI verification
- Applied playtesting

**Code Written:**
```
- Playtest all 8 mazes
- Verify all ghost behaviours
- Balance difficulty curve
- Document issues
```

**What the Learner Sees:**
Complete maze game. 4 ghosts, 8 mazes, full features. Ready for polish.

**Phase 2 Checkpoint:**
Full maze game content. Four unique ghosts with personalities. Eight mazes. Scatter/chase modes. Bonus fruit. Tunnels. Intermissions. Feature-complete.

---

## Phase 3: Polish (Units 33-48)

*Goal: Visual and audio polish. Animations, sound design, menus, presentation. Commercial quality.*

---

### Unit 33: Title Screen

**Prerequisites:** Title screen (SID Symphony 33-34)

**Learning Objectives:**
- Apply title screen techniques
- Maze game presentation
- Character showcase
- Menu system

**Concepts Introduced:**
- Maze game title style
- Ghost parade animation
- Applied techniques

**Code Written:**
```
- "MAZE RAIDER" logo
- Ghost parade animation
- Menu: Start, Options, High Scores
- Apply SID Symphony techniques
```

**What the Learner Sees:**
Professional title with ghost characters displayed. Animated parade. Clear menu.

**Reference to SID Symphony:**
"Title screen from Units 33-34. Customised for maze game aesthetic."

---

### Unit 34: Attract Mode

**Prerequisites:** Attract mode (SID Symphony 35, Starfield 44)

**Learning Objectives:**
- Demo gameplay
- Showcase mechanics
- Power pellet demonstration
- Ghost personalities shown

**Concepts Introduced:**
- Scripted demo
- Feature showcase
- Applied attract mode

**Code Written:**
```
- Demo plays maze 1
- Shows power pellet use
- Ghost chase visible
- Any key returns to title
```

**What the Learner Sees:**
Game demonstrates itself. Shows pellet collection, power-up, ghost eating. Commercial quality.

**Reference to Previous Games:**
"Attract mode from SID Symphony Unit 35 and Starfield Unit 44. Applied to maze context."

---

### Unit 35: Player Animation Polish

**Prerequisites:** Animation (Starfield 35)

**Learning Objectives:**
- Smooth player animation
- Direction-based frames
- Eating animation
- Death animation polish

**Concepts Introduced:**
- Directional sprites
- Mouth animation timing
- Death sequence frames
- Character animation

**Code Written:**
```
- 4 directions × 2 animation frames
- Mouth open/close synced to movement
- Death animation sequence
- Smooth transitions
```

**What the Learner Sees:**
Player character fully animated. Mouth opens and closes. Death animation dramatic.

---

### Unit 36: Ghost Animation Polish

**Prerequisites:** Enemy animation (Starfield 36)

**Learning Objectives:**
- Ghost movement animation
- Frightened animation
- Eyes returning to house
- Character through animation

**Concepts Introduced:**
- Floating animation
- State-based animation
- Eyes-only sprite
- Animation character

**Code Written:**
```
- Ghost float animation (2 frames)
- Frightened blue animation
- Flashing frightened animation
- Eyes-only sprite for eaten ghost
```

**What the Learner Sees:**
Ghosts float smoothly. Frightened ghosts wobble. Eaten ghosts = just eyes returning. Full life.

---

### Unit 37: Sound Effects

**Prerequisites:** SID effects (SID Symphony 41-43)

**Learning Objectives:**
- Maze-appropriate sounds
- Waka-waka style eating
- Power pellet drama
- Ghost eaten sound

**Concepts Introduced:**
- Rhythmic eating sound
- State-change sounds
- Sound layering
- Applied sound design

**Code Written:**
```
- Eating sound: quick blip per pellet
- Power pellet: dramatic siren
- Ghost eaten: ascending tone
- Death: descending melody
- Level complete: victory jingle
```

**What the Learner Sees:**
Full sound design. Every action has feedback. Sounds match mood and action.

**Reference to SID Symphony:**
"Sound design techniques from Units 41-43. Applied to maze game actions."

---

### Unit 38: Background Music

**Learning Objectives:**
- Maze game music style
- Optional during gameplay
- Intermission music
- Applied composition

**Concepts Introduced:**
- Sparse vs full music
- Tension through absence
- Intermission themes
- Style matching

**Code Written:**
```
- Optional gameplay music (sparse, tense)
- Intermission music (playful)
- Power pellet music (urgent)
- Victory jingle
```

**What the Learner Sees:**
Music options. Spare tension during play. Playful intermissions. Cohesive audio.

---

### Unit 39: HUD Polish

**Prerequisites:** HUD (Starfield 43)

**Learning Objectives:**
- Maze game HUD
- Lives as icons
- Current level/maze
- Clean presentation

**Concepts Introduced:**
- Icon-based lives
- Level display
- Fruit collection shown
- Clean layout

**Code Written:**
```
- Score: top area
- Lives: player icons
- Level number
- Collected fruit display
- High score shown
```

**What the Learner Sees:**
Clean HUD showing all info. Lives as character icons. Current fruit progress.

---

### Unit 40: Ready Screen

**Learning Objectives:**
- Pre-game ready display
- Player orientation
- Brief pause
- Classic convention

**Concepts Introduced:**
- Ready message
- Starting positions shown
- Brief delay
- Tension building

**Code Written:**
```
- "READY!" text displayed
- All characters at start positions
- Brief pause (2 seconds)
- Then game starts
```

**What the Learner Sees:**
"READY!" appears before action. Player sees starting layout. Classic presentation.

---

### Unit 41: Game Over Screen

**Prerequisites:** Game over (Starfield 15)

**Learning Objectives:**
- Maze game over presentation
- Final score display
- Continue option (if applicable)
- Return to title

**Concepts Introduced:**
- Game over state
- Score summary
- Applied game over

**Code Written:**
```
- "GAME OVER" display
- Final score shown
- High score check
- Return to title after delay
```

**What the Learner Sees:**
Clean game over. Score displayed. Returns to title. Closure.

**Reference to Starfield:**
"Game over flow from Unit 15. Applied to maze game."

---

### Unit 42: High Score Entry

**Prerequisites:** High scores (SID Symphony 45)

**Learning Objectives:**
- Apply high score system
- Maze in name (optional)
- Initials entry
- Leaderboard

**Concepts Introduced:**
- Level reached tracking
- Applied high score

**Code Written:**
```
- Apply SID Symphony high score system
- Track highest level reached
- Name entry
- Top 10 display
```

**What the Learner Sees:**
High score entry if qualified. Shows score and level. Leaderboard visible.

**Reference to SID Symphony:**
"High score system from Unit 45. Applied directly."

---

### Unit 43: Options Screen

**Prerequisites:** Options (SID Symphony 46)

**Learning Objectives:**
- Maze game options
- Starting lives
- Music toggle
- Difficulty selection

**Concepts Introduced:**
- Maze-relevant options
- Applied options

**Code Written:**
```
- Starting lives: 3, 5
- Music: on/off
- Starting level: 1 (or unlocked)
- Sound test
```

**What the Learner Sees:**
Options screen with relevant choices. Music toggle. Lives selection.

**Reference to SID Symphony:**
"Options framework from Unit 46. Different options for maze game."

---

### Unit 44: Pause System

**Prerequisites:** Pause (SID Symphony 47)

**Learning Objectives:**
- Apply pause system
- Maze pause display
- Resume countdown
- Ghost visibility

**Concepts Introduced:**
- Pause in action game
- State preservation
- Applied pause

**Code Written:**
```
- Pause on key press
- Ghosts optionally hidden (prevent memorising)
- Resume options
- Countdown on resume
```

**What the Learner Sees:**
Pause works cleanly. Ghosts hidden during pause (fair). Resume countdown.

**Reference to SID Symphony:**
"Pause system from Unit 47. Ghost hiding is maze-specific."

---

### Unit 45: Visual Effects

**Prerequisites:** Effects (Starfield 38)

**Learning Objectives:**
- Maze flash on complete
- Power pellet screen effect
- Death flash
- Polish moments

**Concepts Introduced:**
- Maze-appropriate effects
- Victory celebration
- Applied effects

**Code Written:**
```
- Maze flash on level complete
- Screen pulse during power mode
- Death flash
- Ghost eaten flash
```

**What the Learner Sees:**
Visual feedback on key moments. Level complete celebration. Power mode feels powerful.

---

### Unit 46: Ghost Behaviour Tuning

**Learning Objectives:**
- Fine-tune all ghost AI
- Verify personalities distinct
- Balance challenge
- Fairness check

**Concepts Introduced:**
- AI tuning
- Personality verification
- Balance testing
- Applied tuning

**Code Written:**
```
- Verify each ghost behaves correctly
- Adjust targeting offsets if needed
- Test all maze configurations
- Document final parameters
```

**What the Learner Sees:**
Ghost behaviours feel right. Each personality distinct. Challenge fair.

---

### Unit 47: Intermission Polish

**Learning Objectives:**
- Polish cutscenes
- Smooth animation
- Timing refinement
- Charming presentation

**Concepts Introduced:**
- Cutscene polish
- Animation timing
- Applied polish

**Code Written:**
```
- Smooth intermission animations
- Timing adjustments
- Add variety between intermissions
- Polish transitions
```

**What the Learner Sees:**
Intermissions charming and smooth. Fun break between challenges.

---

### Unit 48: Polish Pass

**Learning Objectives:**
- Complete polish playtest
- Fix all issues
- Verify all states
- Release preparation

**Concepts Introduced:**
- Final polish
- State verification
- Applied methodology

**Code Written:**
```
- Full playtest
- Fix any issues found
- Verify all game states
- Document remaining tasks
```

**What the Learner Sees:**
Polished maze game. Everything feels right. Ready for mastery phase.

**Phase 3 Checkpoint:**
Fully polished maze game. Animations, sound, menus, effects all complete. Professional presentation.

---

## Phase 4: Mastery (Units 49-64)

*Goal: Advanced features and final release. Two-player, optimisation, packaging, expert features.*

---

### Unit 49: Code Review

**Prerequisites:** Code review (SID Symphony 49)

**Learning Objectives:**
- Review codebase
- Identify improvements
- Document architecture
- Plan optimisation

**Concepts Introduced:**
- Applied code review
- Maze-specific architecture

**Code Written:**
```
- Full code review
- Document memory map
- Identify hot paths
- Clean up code
```

**What the Learner Sees:**
No visible change. Clean codebase. Ready for optimisation.

---

### Unit 50: Optimisation

**Prerequisites:** Optimisation (SID Symphony 50-51)

**Learning Objectives:**
- Apply optimisation techniques
- Ghost AI performance
- Rendering optimisation
- Frame rate stability

**Concepts Introduced:**
- Maze-specific optimisation
- Applied techniques

**Code Written:**
```
- Optimise ghost AI calculations
- Optimise tile rendering
- Profile and improve
- Verify stable frame rate
```

**What the Learner Sees:**
Smooth performance. Handles busy screens. Professional quality.

---

### Unit 51: Two-Player Alternating

**Prerequisites:** Two-player (Starfield 55)

**Learning Objectives:**
- Two-player turns
- Separate scores
- Player indicator
- Competition

**Concepts Introduced:**
- Turn-based multiplayer
- Score tracking per player
- Applied two-player

**Code Written:**
```
- Two-player option
- Player 1 plays until death/level
- Player 2 turn
- Track scores separately
- Winner at end
```

**What the Learner Sees:**
Two players compete in turns. Each has own score. Competitive mode.

**Reference to Starfield:**
"Two-player from Unit 55. Applied to maze game with turn-based structure."

---

### Unit 52: Two-Player Simultaneous (Optional)

**Learning Objectives:**
- Both players in maze
- Cooperative play
- Shared maze
- Performance challenge

**Concepts Introduced:**
- Two sprites in maze
- Cooperative scoring
- Extra complexity
- Optional feature

**Code Written:**
```
- Two player sprites
- Both navigate same maze
- Cooperative: clear together
- Competitive: separate pellet scores
```

**What the Learner Sees:**
Two players in maze together! Cooperative chaos. Optional advanced mode.

---

### Unit 53: Ms. Pac-Man Style Features (Optional)

**Learning Objectives:**
- Wandering fruit
- Semi-random maze rotation
- Faster ghost release
- Variant gameplay

**Concepts Introduced:**
- Gameplay variants
- Moving fruit
- Random elements
- Game modes

**Code Written:**
```
- Option for wandering fruit
- Option for random maze order
- "Advanced" mode toggle
- Applied features
```

**What the Learner Sees:**
Optional advanced features. Moving fruit adds challenge. Variant mode for variety.

---

### Unit 54: Statistics

**Prerequisites:** Statistics (SID Symphony 31, Starfield 58)

**Learning Objectives:**
- Apply statistics tracking
- Maze-specific stats
- Lifetime progress
- Achievement tracking

**Concepts Introduced:**
- Total ghosts eaten
- Mazes completed
- Applied statistics

**Code Written:**
```
- Apply statistics system
- Ghosts eaten total
- Pellets collected total
- Perfect levels (no deaths)
```

**What the Learner Sees:**
Statistics screen with maze game stats. Lifetime progress visible.

---

### Unit 55: Speed Run Mode

**Learning Objectives:**
- Timer-based mode
- Best time per maze
- Speed running features
- Replay value

**Concepts Introduced:**
- Time attack mode
- Per-maze timing
- Leaderboard for time
- Speed run appeal

**Code Written:**
```
- Timer display during game
- Best time per maze tracked
- Speed mode: infinite lives, timer only
- Time-based high score
```

**What the Learner Sees:**
Speed run mode with timer. Compete for fastest clear. Different skill challenge.

---

### Unit 56: Difficulty Modes

**Learning Objectives:**
- Easy/Normal/Hard
- Accessibility options
- Expert mode
- Skill range

**Concepts Introduced:**
- Difficulty parameters
- Ghost speed ranges
- Accessibility
- Applied difficulty

**Code Written:**
```
- Easy: slower ghosts, longer power
- Normal: balanced
- Hard: fast ghosts, short power
- "Original": classic parameters
```

**What the Learner Sees:**
Difficulty options for all skill levels. Easy mode accessible. Hard mode punishing.

---

### Unit 57: Credits Sequence

**Prerequisites:** Credits (SID Symphony 61, Starfield 60)

**Learning Objectives:**
- Apply credits sequence
- Maze-themed presentation
- Attribution
- Closure

**Concepts Introduced:**
- Applied credits

**Code Written:**
```
- Credits with ghost parade
- Learner attribution
- Return to title
- Applied from previous games
```

**What the Learner Sees:**
Credits with personality. Ghosts parade during credits. Satisfying closure.

---

### Unit 58: Maze Editor Concept (Design Only)

**Learning Objectives:**
- Consider tool creation
- Maze data format for editing
- Design document only
- Future tooling concept

**Concepts Introduced:**
- Tool design thinking
- Data-driven content
- User-generated content concept
- Design exercise

**Code Written:**
```
- Design document for maze editor
- Data format documentation
- No implementation (scope)
- Future possibility noted
```

**What the Learner Sees:**
Design document. Understanding of how tools could work. Seeds future learning.

---

### Unit 59: Easter Eggs

**Learning Objectives:**
- Hidden features
- Kill screen concept
- Secret modes
- Fan service

**Concepts Introduced:**
- Easter egg design
- Hidden content
- Classic references
- Player surprise

**Code Written:**
```
- Secret code for bonus lives
- Hidden message at level 256 (or special level)
- Classic reference (split maze at high level?)
- Fun surprises
```

**What the Learner Sees:**
Hidden features for dedicated players. Easter eggs reward exploration.

---

### Unit 60: Bug Hunt

**Prerequisites:** Bug hunt (SID Symphony 62, Starfield 62)

**Learning Objectives:**
- Apply bug hunt methodology
- Maze-specific edge cases
- Ghost AI edge cases
- Quality assurance

**Concepts Introduced:**
- Applied bug hunt
- Maze edge cases

**Code Written:**
```
- Systematic testing
- Ghost behaviour verification
- Collision edge cases
- Fix all issues
```

**What the Learner Sees:**
Solid, bug-free game. All states work. Professional quality.

---

### Unit 61: Final Balance

**Learning Objectives:**
- Final difficulty tuning
- All modes balanced
- Play all mazes
- Sign off on feel

**Concepts Introduced:**
- Final tuning
- Balance verification
- Sign off

**Code Written:**
```
- Final parameter adjustments
- All difficulty modes tested
- All mazes played through
- Parameters locked
```

**What the Learner Sees:**
Game feels right. Balanced for all skill levels. Final tuning complete.

---

### Unit 62: Final Playtest

**Prerequisites:** Final playtest (previous games)

**Learning Objectives:**
- Fresh eyes playtest
- Final issues
- Release candidate
- Sign off

**Concepts Introduced:**
- Applied final playtest

**Code Written:**
```
- External playtest if possible
- Final fixes
- Declare release candidate
- Documentation check
```

**What the Learner Sees:**
Final version ready. All issues resolved. Release candidate.

---

### Unit 63: Documentation

**Learning Objectives:**
- Write instructions
- Control reference
- Tips and tricks
- Complete documentation

**Concepts Introduced:**
- Game documentation
- Player guidance
- Applied documentation

**Code Written:**
```
- Instruction text
- Control reference
- Ghost personality descriptions
- Tips for new players
```

**What the Learner Sees:**
Complete documentation. Players can learn from instructions.

---

### Unit 64: Packaging and Distribution

**Prerequisites:** Packaging (previous games)

**Learning Objectives:**
- Apply packaging process
- Create distribution files
- Archive source
- Release

**Concepts Introduced:**
- Applied packaging

**Code Written:**
```
- D64/TAP images
- Documentation included
- Source archived
- Ready to distribute
```

**What the Learner Sees:**
Complete distribution package. Third commercial-quality game complete.

**Phase 4 Checkpoint:**
Complete maze game with advanced features. Two-player modes, difficulty options, statistics. Professional quality, fully packaged.

---

## Skills Progression Summary

### From Previous Games (Applied)
- All program fundamentals
- Sprite basics and animation
- Sound and music
- State machines and menus
- Polish methodology
- Distribution packaging

### New in Maze Raider
- Tile-based maps and collision
- Custom character sets (deep mastery)
- Grid-based movement with smooth animation
- Pathfinding and chase AI (four distinct algorithms)
- Ghost behaviour modes (scatter, chase, frightened)
- Power-up state that affects enemies
- Level-based content progression
- Wrap-around movement
- Cutscene/intermission implementation

### Prepared for Game 4 (Platform Panic)
- Character-based graphics mastery
- Tile collision deeply understood
- Smooth character movement
- Enemy behaviour patterns
- Level design principles
- State-based character behaviour

---

## Version History

- **1.0 (2025-01-07):** Initial 64-unit outline with game 1-2 integration
