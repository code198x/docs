# The Caverns — source review

The user selected this game next after Three in a Row. The existing twenty-room BASIC program and retained brief were read together. `verification/review.py` pins the source and checks its graph; this is source inspection, not a fresh native playtest of that older game.

## Useful structure

The existing game stores north/south/east/west links in numeric arrays and uses one adjacency routine for pits, a creature and treasure. All twenty rooms are reachable without hazards. Treasure flags and creature position are separate from the static connections, which is a useful foundation for teaching a persistent world.

## Gaps that affect the trial

The initial placement excludes room 1 but not its neighbours, rooms 2 and 5. The brief's safe-neighbourhood promise is not implemented. Room identity is numeric in the source; the promised individual descriptions are absent.

More importantly, movement can create a lethal encounter before the player receives a fresh warning. Put the creature in room 6 and the player at the starting room 1. There is no creature-adjacency clue at room 1. Move south to room 5. The creature can then move west from 6 to 5, triggering capture immediately. This follows the source's legal links and update order; no emulator timing assumption is needed.

The last treasure wins immediately and the message says the player escaped, although the program never requires returning to the entrance. That may be an acceptable rule, but a return journey would make the learnt geography useful again.

## First-trial choices

The [prototype brief](brief.md) uses twelve named rooms, a fixed pit, three treasures and an actual return objective. Directional warnings replace undirected danger messages. A fixed patrol replaces the random walk, and a creature arrival gives one action to escape. The first cave is repeatable so these decisions can be judged without random placement obscuring the result.

These are implementation choices for the authorised prototype direction. Native acceptance remains outstanding. They do not approve a new course group, lesson count, larger cave, inventory system or random generation.
