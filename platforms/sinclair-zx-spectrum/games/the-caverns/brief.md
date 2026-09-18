# The Caverns — BASIC prototype brief

**Status:** The user accepted the native game, reporting that it works quite well, and authorised lesson development. The [ten-lesson progression](lesson-brief.md) preserves this fixed cave and its rules. Replacement lessons are being prepared locally for review; the earlier published lessons remain live.

**Target:** Stock 48K PAL ZX Spectrum, Sinclair BASIC, keyboard and tape. No machine code or expansion. Sources belong in `code-samples/sinclair-zx-spectrum/basic/the-caverns/prototype/`; enter through the ROM and fresh-load a self-starting tape for verification.

## Experience

Explore twelve connected rooms, recover three lost treasures and bring them back to the entrance. Names and a short description make each room recognisable. Only the current room, its exits and signs from neighbouring rooms are shown. There is no full-map display in this first trial.

Use N/S/E/W to move and Space to wait. Each open exit has a directional clue when it leads to a pit, creature or uncollected treasure. A blocked exit and unrelated input cost no turn. R restarts the same expedition and Q quits. S starts at the title. A held key produces one action until released.

The cave, one pit, treasure positions and creature's initial phase are fixed. Repeatable content lets a player learn the geography and lets the trial isolate the turn rules. Random layouts, procedural generation and replay variation are deferred until native feedback establishes that the first expedition is interesting.

## Danger with an opportunity to respond

The pit is stationary. Its adjoining tunnels carry a cold-draught clue; entering it loses. The creature follows a fixed eight-room circuit, one step after each valid action. A footstep clue identifies the tunnel leading to its current room. Moving into that warned-about room loses.

If the creature moves into the player's room, show both “It arrives! Leave next turn!” and “IT IS HERE. MOVE NOW.” It does not kill on arrival. The next valid action must leave; waiting in the occupied room loses. Invalid keys or a wall do not consume that chance. Every reachable arrival must offer at least one legal, nonlethal exit.

Turn order is explicit: validate action; count the turn; resolve entering a pit or occupied creature room; move player; collect treasure; check escape at the entrance; move creature; report arrival and refresh clues. Winning at the entrance ends before another creature move. Collected treasure stays collected even when the creature enters that room.

This is a patrol to observe and evade, not a pursuing creature. Do not describe it as chasing the player. Directional warnings reduce blind guessing; the remaining decisions are route choice, timing, waiting and recognising safe escape routes.

## Presentation

A black screen, restrained blue separator, cyan room heading, short description and four aligned tunnel rows. Text and shape carry meaning; colour helps distinguish warnings and treasure. Keep the turn count, treasure count and controls in stable positions. Preserve the current room and result for inspection after either ending.

The first trial is silent. It must be possible to play from the text alone. Sound or a small graphic should be added only if native play identifies a useful role; the inherited ban on all graphics is not binding. Room descriptions and layout are original, not copied from an earlier commercial adventure.

## What it can teach

A world larger than the screen can be represented as room links. A two-dimensional numeric array holds four exits per room; string arrays hold names and descriptions; treasure flags change independently of the static map. A cyclic route separates autonomous state from player state. The order of updates determines whether a warning is actionable.

Possible teaching responsibilities are a readable room, linked rooms, hidden fixed state, clues, a moving patrol with fair encounters, objectives and return, then replay and tape. Do not fix a lesson count before the prototype is accepted. BASIC remains the present focus; assembly performance revisits are deferred.

## Verification and reasons to revise

Audit reciprocal links, connected safe routes, patrol adjacency, safe opening, reachable treasures and a return route. Use a source-pinned host exploration to examine arrival escapes. This supplements ROM execution; it does not establish human difficulty or enjoyment.

In fresh-ROM play, check each ending, invalid and held input, blocked exits, waiting, creature arrival and escape, directional clue freshness, combined footsteps/treasure clues, retained results, reset and quit from title/play/result. Check model predictions against observed BASIC state without game-state writes. Inspect original captures and ask the user to judge readability and tension.

If exact clues make the cave routine, investigate richer choices before merely adding rooms. If movement is confusing, improve room identity or navigation help. If a player cannot explain a death from the preceding warning, revise the rule or feedback. If the fixed patrol becomes trivial immediately, revisit its behaviour or controlled variation while preserving a chance to react.
