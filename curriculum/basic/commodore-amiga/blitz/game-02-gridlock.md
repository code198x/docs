# Blitz Game 02: Gridlock

**Track:** Blitz Basic 2
**Genre:** Tower defence / tactical strategy
**Units:** 64 (4 phases × 16 units)
**Language:** Blitz Basic 2
**Max lines:** ~500

---

## Premise

Enemies march along a path through a grid. You place towers on empty cells to stop them. Towers fire automatically at enemies within range. Killing enemies earns currency to buy more towers. If enemies reach the exit, you lose lives.

Tower defence is the perfect vehicle for Blitz's NEWTYPE system: towers are structured data (position, type, range, damage, fire rate, cooldown). Enemies are structured data (position, speed, health, path index). The game is a system of interacting entities — exactly what custom types are designed for.

Mouse-driven: click to select tower type, click to place. The Amiga mouse is the natural interface.

---

## Core Mechanics

### The Grid

A grid (12×8) with a predefined path from entry to exit. Enemies follow the path. Empty cells adjacent to the path are buildable. The player places towers on buildable cells.

### Tower Types

| Tower | Cost | Range | Damage | Fire Rate | Special |
|-------|------|-------|--------|-----------|---------|
| Arrow | 10 | Medium | Low | Fast | Cheap, reliable |
| Cannon | 25 | Short | High | Slow | Splash damage (hits adjacent enemies) |
| Frost | 30 | Medium | None | Medium | Slows enemies for 3 seconds |
| Sniper | 50 | Long | Very high | Very slow | Targets strongest enemy in range |

### Enemies

| Type | Health | Speed | Worth | Special |
|------|--------|-------|-------|---------|
| Scout | 10 | Fast | 5 | Weak but quick |
| Soldier | 25 | Medium | 10 | Standard |
| Armoured | 50 | Slow | 20 | High health |
| Runner | 15 | Very fast | 15 | Hard to hit |
| Boss | 200 | Very slow | 100 | Appears wave 10, 20 |

### Waves

20 waves of enemies marching along the path. Each wave defines enemy types and counts. Later waves mix types. The player earns currency from kills and spends it between waves.

### Economy

- Start with 50 currency
- Enemies drop currency on death
- Towers can be sold for 50% cost
- Between waves: build phase (unlimited time)

---

## Phase Breakdown

### Phase 1: Grid and Towers (Units 1-16)

| Unit | Title | What the learner builds | Code concepts |
|------|-------|------------------------|---------------|
| 1 | The Grid | Draw a 12×8 grid. Path marked with different colour. Buildable cells highlighted. | Grid rendering, cell states |
| 2 | NEWTYPE Introduction | `NEWTYPE .Tower` with fields: x, y, ttype, range, damage, cooldown, timer. | NEWTYPE, structured data |
| 3 | Mouse Selection | Mouse cursor moves over grid. Hover highlights cell. Click selects. | MouseX, MouseY, grid mapping |
| 4 | Tower Placement | Click a buildable cell → tower appears (drawn as a shape). NEWTYPE instance stored in array. | Array of NEWTYPE, placement logic |
| 5 | Tower Types | Tower selection panel: click arrow/cannon/frost/sniper, then click grid cell. Different shapes per type. | Type selection UI, parameterised placement |
| 6 | Range Circles | Hovering a tower shows its range as a circle. Helps placement decisions. | Range visualisation, Circle command |
| 7 | Currency | Display currency. Towers cost currency. Can't build if insufficient. | Resource management, validation |
| 8 | Selling Towers | Right-click a placed tower to sell for 50%. Frees the cell. | Tower removal, refund |
| 9 | The Path | Path defined as array of grid coordinates. Enemies will follow this path. | Path data structure |
| 10 | One Enemy | NEWTYPE .Enemy: x, y, health, speed, path_index. Enemy follows the path, cell by cell. | Enemy NEWTYPE, path following |
| 11 | Enemy Movement | Enemy moves smoothly between path cells (interpolate position). Reaches the end = lose a life. | Interpolation, smooth movement |
| 12 | Tower Firing | Each frame: tower checks if any enemy is within range (distance calculation). If yes and cooldown ready: fire. | Range check, cooldown timer |
| 13 | Projectile | Tower fires a projectile (small shape) that travels toward the target enemy. On arrival: damage. | Projectile system, target tracking |
| 14 | Enemy Death | Health reaches 0 → explosion, currency awarded. Enemy removed from array. | Death handling, reward |
| 15 | Wave Structure | Wave 1: 10 scouts. They march, towers fire, scouts die or reach the exit. Functional game loop. | Wave management |
| 16 | Build Phase | Between waves: unlimited time to build. "NEXT WAVE" button starts the action. | Phase switching, build/action modes |

**Milestone:** A working tower defence with one tower type, one enemy type, and the build/action phase cycle. NEWTYPE for towers and enemies.

### Phase 2: Strategy (Units 17-32)

All tower types, all enemy types, 20 waves.

| Unit | Title | What the learner builds | Code concepts |
|------|-------|------------------------|---------------|
| 17 | Arrow Tower | Fast fire, low damage. Good for scouts. | Tower parameterisation |
| 18 | Cannon Tower | Slow fire, high damage, splash (damages enemies within 1 cell of target). | Area damage, splash radius |
| 19 | Frost Tower | No damage, but slows enemy speed by 50% for 3 seconds. Strategy: place before cannon. | Debuff effect, enemy speed modification |
| 20 | Sniper Tower | Long range, high damage, targets the enemy with most health in range (not nearest). | Target priority, sorting |
| 21 | Multiple Enemies | 10+ enemies on screen simultaneously. All following the path, all targetable. | Mass entity management |
| 22 | Enemy Variety | Scouts, soldiers, armoured, runners. Different health, speed, rewards. Visual distinction. | Enemy types, NEWTYPE fields |
| 23 | Waves 1-10 | Design 10 waves with escalating difficulty. Pure scouts → mixed types → first boss. | Level design |
| 24 | Boss Enemy | Wave 10 boss: very high health, slow, worth lots of currency. Requires focused fire. | Boss entity, high-value target |
| 25 | Tower Upgrades | Click an existing tower twice → upgrade (costs currency). More range, more damage. | Upgrade system, tower levels |
| 26 | Waves 11-20 | Harder waves. Armoured + runner combos. Second boss at wave 20. | End-game design |
| 27 | Lives System | Enemies reaching the exit cost 1 life. 20 lives. Zero = game over. | Life counter, fail state |
| 28 | Speed Controls | Fast-forward button (2× speed). Pause button. Quality of life. | Game speed control |
| 29 | Wave Preview | Before each wave: show enemy types and counts. "WAVE 5: 8 Soldiers, 4 Runners." | Pre-wave information |
| 30 | Score | Based on waves survived, enemies killed, currency remaining, lives remaining. | Scoring formula |
| 31 | Sound | Tower firing sounds (per type), enemy death, wave start horn, boss warning. | Audio per event |
| 32 | Twenty Waves | Complete progression. Strategic tower placement matters. Upgrades are essential in late waves. | Content-complete |

### Phase 3-4: Polish and Production (Units 33-64)

Linked lists for dynamic enemy spawning (instead of fixed arrays). Multiple maps (3 different path layouts). Difficulty select. High score table. MOD music. Title screen with animated tower demo. Visual effects (projectile trails, frost aura around slowed enemies, explosion particles). Statistics screen (damage per tower, kills per tower). Final production: bootable ADF, system-friendly startup/shutdown, testing across Amiga models.

Key technical highlights:
- Linked lists via Blitz's dynamic allocation (alternative to fixed arrays)
- NEWTYPE inheritance patterns (base entity → tower/enemy subtypes)
- Efficient range checking (skip distant towers, only check nearby)
- Frame rate maintains 50fps with 20+ enemies and 15+ towers

---

## Design Notes

### Why Tower Defence

Tower defence is inherently about data structures. Every tower is a struct with properties. Every enemy is a struct on a path. The game loop iterates collections, checks ranges, updates timers. This is exactly what NEWTYPE teaches — and it's a genre that rewards strategic thinking over reflexes, suiting the Blitz track's "structured programming" focus.

### AMOS vs Blitz Comparison

Gridlock and Conduit are both mouse-driven grid games. But Conduit (AMOS) is a puzzle with no real-time pressure. Gridlock (Blitz) runs 20+ entities with pathfinding and projectiles at 50fps. Same input device, same grid concept, very different computational demands. The comparison demonstrates why compiled code matters.

---

## Changelog

- **v1.0 (2026-03-09):** Initial game outline. Replaces old Blitz Game 2 (Venom) with a tower defence teaching NEWTYPE and structured data.
