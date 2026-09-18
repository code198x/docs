# Spectrum BASIC — grouping and remaining-course review

The user agreed the four groups below. The website module catalogue owns their membership and order. This review recommends how to assess the remaining material; it does not approve a new lineup or retire existing lessons. Locksmith’s approved replacement lessons are now published. The user subsequently selected [Three in a Row’s opponent review](../games/three-in-a-row/review.md); its native prototype is accepted and the [teaching progression](../games/three-in-a-row/lesson-brief.md) is prepared locally.

## Agreed grouping

| Group | Published modules, in order | Connection |
|---|---|---|
| First programs | Meet BASIC, Bright Spark | Small responsive programs, then remembering and repeating a sequence |
| Movement and control | Volley, Touchdown | Continuous motion, contact, acceleration and braking |
| Boards and deduction | Sonar, Crates, Locksmith | Reading a grid, combining clues and changing board state safely |
| Worlds that keep moving | Tail Chase, Brick Bash, Drift, Quickstep | Ordered bodies, destructible worlds, independent velocity and multiple moving hazards |

These are navigation groups, not prerequisites or separate courses. All current game numbers, URLs and relative order remain unchanged. Five earlier games remain separately available, and the BASIC reference remains optional. Revised games can join the group that fits their activity; Locksmith now belongs to Boards and deduction.

## Review evidence and limits

Reviewed the website catalogue, the six existing game overviews and final-lesson structure, the final BASIC sources, relevant lesson explanations, retained briefs and the three retained specifications for Night Patrol, Blockstorm and Dorin. This is a source and scope review, not a fresh emulator execution or learner trial. The older briefs retain superseded sequence, line-budget and prerequisite assumptions; their feature lists do not establish implementation.

The source paths below are relative to the [samples repository](https://github.com/code198x/code-samples/tree/main/sinclair-zx-spectrum/basic). Existing lessons are under the same game slugs in the [BASIC track](https://code198x.com/systems/sinclair-zx-spectrum/basic/).

## Six existing games

| Game and inspected endpoint | Distinct activity and teaching value | Recommendation and bounded first scope |
|---|---|---|
| Dice Roller — `dice-roller/unit-05/dice-roller.bas` | Choose a sample size and compare random frequencies; accumulation, chart scaling and evidence | Keep as an optional probability experiment. Its source has no competing objective or win/loss rule. Validate the roll count and scale bars to the display before reusing it. It need not occupy a main-course game slot. |
| Cipher — `cipher/unit-06/cipher.bas` | Guess letters, reveal all matches, remember attempts; string mutation and content choices | Keep as an optional small word game within Boards and deduction. One word list, repeated-letter handling, validated single-letter input and clear replay are enough. DATA and arrays alone no longer justify a full progression after Crates. |
| Locksmith — `locksmith/unit-06/locksmith.bas` | Combine exact-position and wrong-position clues; counting repeated values without double-counting | Now revised and published in Boards and deduction: four digits, six symbols, repeats allowed and ten guesses with visible history. See its current brief and implementation record. |
| Three in a Row — `three-in-a-row/unit-06/three-in-a-row.bas` | Compete against rules that inspect the same board as the player; reusable evaluation, priority and counterexamples | Retain as an opponent-design game. Start with one board and a readable rule-based opponent. Decide whether the endpoint is deliberately fallible or unbeaten, then test that claim; an exhaustive host search can supplement native play. |
| The Caverns — `the-caverns/unit-06/caverns.bas` | Navigate connected rooms using local clues; graphs, adjacency and hidden moving state | Retain for a later Hidden worlds and lasting consequences group. Begin with one authored connected cave, one pit, one creature and a small treasure objective. Verify clue timing, safe starts and reachable objectives before enlarging it. |
| Yearfall — `yearfall/unit-06/yearfall.bas` | Allocate scarce resources and live with later consequences; constraints, turn resolution and a readable simulation model | Retain in the same later group. One settlement, grain/land/population and a finite run are enough. Reconcile the economy and attainable outcomes before adding events or systems. |

### Concrete findings to carry into the briefs

- **Dice Roller:** lines 270–320 print one block per occurrence, while the final lesson invites 10,000 rolls. The chart has no scaling; this does not remain one screen row per face. The rewrite should distinguish relative frequency from absolute count and avoid implying a finite sample proves fairness.
- **Cipher:** line 400 normalises input without first requiring one alphabetic character. The old brief also equates word length with difficulty; content selection needs a more careful account of letter frequency, repetition and familiarity. Review these as design questions, not established rules.
- **Locksmith:** line 150 generates each digit independently, and lines 320–410 count multiplicities. The source permits duplicates, whereas the retained brief initially excludes them. Preserve the actual repeated-digit algorithm as useful material, then settle one explicit rule set.
- **Three in a Row:** the strategy lesson claims a careful player cannot beat the opponent. The source tries win, block, centre, corners and edges; there is no explicit fork handling or search. The subsequent source-pinned host traversal finds a winning human sequence: 1, 8, 7, 4 against replies 5, 3, 9. See the dedicated review for evidence and native-execution limits. Line 330 does exist in the unit-05 source included by the strategy lesson; the final unit-06 moves that check to 320.
- **The Caverns:** hazard placement excludes room 1 but does not exclude its neighbours. The brief's safe-neighbourhood opening is therefore not enforced by the source. The actual map is numeric room links, without the promised individual room descriptions. Choose which experience the revised game should provide.
- **Yearfall:** the source starts at 100 people and adds at most six per year for ten years. Its 200-person “Wise Ruler” result is unreachable under that model, even with no deaths. The brief also differs from the source on workers per acre, yield and population growth. Reconcile the actual rules and make the reports explain them.

These findings establish rewrite work, not a new claim that the programs were executed in this review. No earlier lesson or sample was changed as part of grouping.

## Eleven proposals, seven families

The following are recommendations only. The catalogue entries stay proposals until their scope is agreed. The names in each paired row currently have separate entries; reviewing them as one family avoids assuming that each expansion needs another course-sized game.

| Catalogue entries | Distinct possibility | Recommendation and evidence needed |
|---|---|---|
| The Hungry Maze | Pursuit and a temporary reversal of danger | Keep as a candidate. Trial one maze, one pursuer and one power effect. It must add decisions beyond Tail Chase's avoidance; path choice and readable pursuit should justify it. Current evidence is catalogue-level. |
| Night Patrol | Retained specification: patrol routes and wall-blocked sightlines. Catalogue: multiple targets and limited interceptors | Resolve the identity before prototyping. Recommend investigating stealth: visibility and occlusion add something beyond Quickstep's cyclic hazards. Start with one guard and one room. Missile defence would need its own explicit brief if preferred. |
| Blockstorm | Retained specification: vertical shooter with enemies, bullets and waves | Re-scope to a small shooter trial. It is not a falling-block puzzle. One formation and one shot are enough to test the appeal; add objects only after measuring and playing. Reject the inherited requirement to make BASIC fail or imply that a particular wave demonstrates an absolute language limit. |
| Rooftops + Skyhold (`rooftops-pt1`, `rooftops-pt2`) | Jumping/platform contact, then connected screens | Review as one platform-game family. A single authored screen must feel good in BASIC before multi-screen exploration earns an extension. Existing evidence is catalogue-level; no timing or control quality is established. |
| Stonefall + Deepworks (`stonefall-pt1`, `stonefall-pt2`) | Falling objects, tile updates and authored puzzles | Review as one cave-puzzle family. A small board can expose update ordering, crushing and chain reactions. Distinguish it from Crates through autonomous changes; a later room set can extend the game without requiring a new title. |
| Dungeons of Dorin + Dungeons of Dorin II (`dorin-pt1`, `dorin-pt2`) | Generated spaces, turn-based encounters, inventory and persistent state | Review as one dungeon family. The retained specification already bundles generation, combat, equipment and tape persistence. Reduce the first trial to one generated, connected floor and one encounter type; prove reachability and meaningful choices before adding depth or persistence. |
| Thornwood Manor + Thornwood Manor II (`thornwood-pt1`, `thornwood-pt2`) | Verb/noun commands, objects and authored world responses; potentially autonomous inhabitants | Review as one adventure family. A few rooms and one object puzzle can establish parsing and world-state rules. Later inhabitants should create understandable consequences, not merely enlarge a “finale”. Current evidence is catalogue-level. |

This yields thirteen distinct concepts to review: six existing projects and seven proposed families. That is a comparison set, not a thirteen-game commitment. If Dice Roller and Cipher become optional routes, four existing main-course candidates remain, plus seven uncommitted families.

## Recommended sequence of decisions

1. Locksmith’s bounded prototype and replacement lessons are accepted and published. Retain its verified ten-guess baseline.
2. Three in a Row’s opponent review is complete; its native prototype is accepted and ten replacement lessons are prepared for review. The Caverns and Yearfall remain later candidates for contrasting forms of persistent state.
3. Keep Dice Roller and Cipher available while deciding how short optional projects should appear in navigation. No retirement or relocation is approved here.
4. Settle Night Patrol's identity and assess the seven proposal families individually. New groups should follow accepted experiences; do not publish empty groups or a promised finale sequence.

The current BASIC-first priority remains. Responsive action trials may expose constraints, but the later BASIC/assembly performance investigations remain deferred. No proposal is automatically moved to assembly because it might be demanding.

A candidate earns a place when its bounded prototype is enjoyable and its teaching adds a distinct relationship or decision. Merge or defer it when most of its progression repeats an existing game. Evidence that would change these recommendations includes a compelling small Cipher variant, a pursuit prototype with no decisions beyond existing avoidance games, or a platformer whose controls remain unsatisfying at the agreed BASIC scope.
