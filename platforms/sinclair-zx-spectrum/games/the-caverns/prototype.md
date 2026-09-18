# The Caverns — prototype record

**Status:** The selected BASIC exploration trial is implemented and verified, ready for native play. The user has not yet accepted this game or its difficulty. Existing website lessons remain unchanged.

## Implemented trial

Twelve named rooms, one fixed pit, three treasures and a return to the entrance.
A creature follows an eight-room circuit after each valid action. Directional
clues identify danger and treasure at the neighbouring exits. A creature arrival
grants one valid action to leave; waiting then loses. Invalid input and blocked
exits cost no turn. S starts, N/S/E/W move, Space waits, R restarts the fixed
expedition and Q quits. The game is silent and has no real-time deadline.

The map and starting state are deliberately repeatable for this trial. There is
no full-map display, random generation or pursuit algorithm. The creature's
patrol is independent of the player's position. The final room and outcome
remain visible until replay or quit.

## Evidence

The source is maintained at
`code-samples/sinclair-zx-spectrum/basic/the-caverns/prototype/caverns.bas`.
Verification scripts and original captures are beside it. The complete source
was entered through the 48K ROM with keyword keys, saved to tape and loaded in a
fresh emulator process. A later result-control colour/cleanup edit was also
entered through the ROM after fresh loading; all other stored lines were
compared byte-for-byte before re-saving.

Nineteen execution check groups pass, with 32 observed actions checked against
the independent host transition model. They include fresh tape/source identity,
safe start, ignored keys, walls, held input, legal pit/capture/win paths,
arrival and escape, waiting after arrival, clue freshness, stable results,
uppercase controls, replay and quit from title/play/result. All memory access
used for observation is read-only; there are no game-state setup writes.

The host model explores 534 reachable nonterminal states. All 50 reachable
states where the creature has arrived in the player's room offer a nonlethal
exit. It also checks reciprocal connections, patrol adjacency and the safe
opening. These are model properties, not claims about human decision-making.
The shortest winning route found by that model is ten actions; this is not a
suggested first-play duration.

The audit binds source, saved tokens, self-starting tape, executable identity,
results and captures. Configuration is stock 48K PAL using the local Emu198x
build at `e1f49c7e8e20ff8cf1cab8453955f2b212dab4e3`, reporting 0.24.0. Original
entrance, arrival and ending images were inspected. No original-hardware timing,
independent learner testing or native acceptance is claimed.

## Native questions

Does each death follow a warning the player could understand? Do waiting and
escape feel like useful choices? Do room names help the return journey? Is a
fixed cave worth exploring, or exhausted too quickly? Judge those questions
before adding randomness, rooms, audio or a lesson sequence.
