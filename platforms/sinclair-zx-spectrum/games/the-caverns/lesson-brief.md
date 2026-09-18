# The Caverns — teaching progression

**Status:** The user accepted the native prototype and authorised lesson development. Ten lessons use eight independently runnable programs. The accepted endpoint is preserved; replacement lessons are prepared locally for review, not published.

**Endpoint:** `code-samples/sinclair-zx-spectrum/basic/the-caverns/prototype/caverns.bas` at samples commit `7c3fcfe`. The finished checkpoint must be byte-identical: twelve named rooms, a fixed pit, three treasures returned to the entrance, an eight-room patrol, directional clues, an escape turn after arrival, no real-time deadline and deliberate silence.

## Central idea

**The order of a turn determines whether a warning leaves a useful choice.** A static map, changing treasure flags, player position and an independently moving creature are distinct kinds of state. The display describes them; it does not decide their behaviour.

## Progression

| Lesson | Checkpoint | Result and explanation |
|---|---|---|
| 1. Name a room | `room` | New program with two strings, a room display and deliberate STOP. Explain character versus pixel coordinates and GO SUB/RETURN. |
| 2. Connect the rooms | `map` | Load twelve room records into numeric and fixed-length string arrays. Show the entrance's exits; STOP leaves it inspectable. Explain nested loops, DATA/READ/RESTORE and reciprocal links. |
| 3. Follow a tunnel | `walk` | N/S/E/W input, proposed destination, rejected walls, waiting, counted turns, release gate, R/Q and all twelve safe rooms. Room descriptions do not imply hazard rules. |
| 4. Leave a glint | `treasure` | Three flags, collection once and destination-based glint clues. All treasures can be found, but there is no winning rule yet. |
| 5. Warn about the pit | `pit` | Room 7 becomes lethal with a matching directional clue and stable result/replay loop. Check danger before collection. |
| 6. Give the creature a route | `patrol` | Cyclic route position versus actual room; move after player action; entering an occupied room versus receiving an arrival; combined clue text. |
| 7. Leave time to escape | Reuse `patrol` | Trace S/S/E/Space/W, explaining the creature arrival and retreat. Invalid keys and walls do not consume the escape action; another valid wait loses. No new BASIC. |
| 8. Bring the treasures home | `expedition` | Require both three treasures and room 1; winning check precedes creature update. A disclosed route verifies the complete objective. |
| 9. Invite the explorer | `finished` | Add the accepted title and S/Q entry loop while retaining the same expedition. Explain setup at 200 versus display at 270. |
| 10. Keep the expedition | Reuse `finished` | ROM SAVE with LINE 10, exported tape, fresh ROM load and a full play/replay/quit cycle. |

The first listing is a complete new program. Later changes have exact add/replace/delete instructions, ordinary changed-line listings and complete source disclosures. The source manifest records each transition; no diff notation is required.

## Temporary rules and worked examples

`walk` permits every room, including the shaft. `treasure` collects without ending; `pit` adds only the fixed danger; `patrol` can still return with all treasures without winning. `expedition` adds the return objective, and `finished` adds the invitation. These incomplete rules are named explicitly rather than mistaken for regressions.

The collection check uses S/E/W/E: the Old camp treasure scores only once. The pit check uses S/E/E. The encounter trace starts at room 1 with the creature at 4: S gives 5/8; S gives 9/12; E gives 10/11; Space gives 10/10; W gives 9/6. Choosing N instead of W reaches 6/6: the creature arrives again, granting another escape action. A valid escape need not finish away from the creature.

E/E/E/S/S/W/W/N/N/W reaches the entrance with all three treasures in ten actions from the fixed start. Hide this route in an optional explanation; it verifies the objective without giving away the whole first expedition in the main instructions.

## Verification and integration

Each source must be independently entered through a fresh stock 48K PAL ROM, saved to TAP and loaded in another process. Audit literal targets, exact editing reconstruction, token identity of unchanged lines, checksums/autostart and final-source identity. Run the prototype suite against the separately entered finished checkpoint.

Exercise all twelve safe rooms before hazards, ignored and held keys, walls, waiting, collection once and disappearing clues, pit/capture endings, arrival/escape/repeated arrival, result stability, reset and the exact point at which return becomes a win. No game-state writes or injected programs should be presented as ordinary play.

The local website draft places the accepted experience in a populated **Hidden worlds** group after the moving-world games. This is part of the lesson/navigation preview for review; it does not approve Yearfall or any further game. Preserve numeric identities and old lesson bookmarks with topic-based redirects. Native acceptance applies to the finished game; intermediate execution does not establish independent learner outcomes.

Language sources: Steven Vickers, edited by Robin Bradbeer, *ZX Spectrum BASIC Programming*, second edition (1983), chapters 4–6, 8, 12–13, 15–18 and 20. Lessons cite the public chapters and canonical Meet BASIC setup/save routes. Assembly and performance comparisons remain deferred.

Implementation and verification: [teaching implementation](lessons.md).
