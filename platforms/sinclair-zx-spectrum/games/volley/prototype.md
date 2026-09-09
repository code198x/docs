# Volley prototype and teaching review

**Status:** Six runnable checkpoint sources implemented; execution findings are recorded below. This is a prototype, not published curriculum or final approval of the course order.

The [brief](brief.md) owns the proposed game and scope. Sources live in `code-samples/sinclair-zx-spectrum/basic/volley/prototype/`; each `steps/step-NN.bas` is a complete program. Verification scripts, source hashes and results belong beside the sources.

## Implemented choices

One three-cell paddle moves vertically at the left of a character court. A one-cell ball travels diagonally in fixed steps. Top, bottom and right boundaries reflect it. Paddle contact adds one return; missing ends the rally. A/Z move, S serves, R returns to the serve screen after a miss, and Q exits. Serving and retry require release before advancing.

The prototype is silent. It uses existing characters and a provisional `PAUSE 2`; this is not a fixed wall-clock update guarantee. The first review can concentrate on input, motion and contact without sound or custom graphics introducing extra work.

Candidate contact resolves the vertical boundary before testing the paddle's inclusive three-row interval. The ball reflects into the court rather than occupying the paddle cell. A miss returns a flag to the main loop before the result screen: retry must not accumulate unfinished `GO SUB` calls.

## Teaching progression

| Checkpoint | New demand | Review finding |
|---|---|---|
| Horizontal movement | Position changes and erase/redraw | Small enough to trace several updates by hand |
| Horizontal reflection | A signed direction value | Explain the sign through visible motion before introducing a second axis |
| Diagonal court | Two independently changing coordinates | Use corner traces; no speed magnitude, acceleration or angles are needed |
| Paddle demonstration | Poll input without stopping movement; constrain the entire paddle | The ball still returns automatically at the left boundary in this intermediate demonstration; explain that paddle contact is not implemented yet |
| Rally collision | Candidate position, overlap and update order | Largest conceptual step; split into multiple lesson checkpoints if traces and source edits become crowded |
| Complete game | Serve, score, miss, retry and exit | Mainly recalls counters, input hand-off and reset behaviour from Bright Spark; still explain each locally |

The transition into collision restructures direct position updates into candidate coordinates. Teach the reason before the change: contact must be decided before drawing, including the row after a wall reflection. The miss flag is communication from a routine, not a new game engine.

This supports the proposed bridge: Volley establishes position/direction, continuous input and simple contact; Touchdown can concentrate on changing speed, fuel and landscape. It does not yet establish an appropriate lesson count or prove the finished rally is enjoyable to human players.

## Verification and remaining review

The initial run checked all six checkpoints, upper/lower paddle limits, misses, retry, six contact boundaries and a fresh-process tape load. A subsequent screen-observed rally exposed a score-column error (the first return displayed as 10); the source now aligns score updates with the initial counter. The corrected final game passed a fresh-process tape load, serve, miss, retry and exit, plus centre/edge/miss/corner contact checks. A screen-observed automated player completed eight returns, with the score advancing exactly from 1 through 8. Results and source/tape hashes are maintained with the samples. Use those results and hashes for exact execution coverage. ROM editing, MCP-driven keyboard events and screen observations are configuration-specific evidence; they are not native host-keyboard or original-hardware acceptance.

The automated rally observed roughly eight to nine PAL frames between drawn ball positions on average; this is an observation of this run, not a fixed timing guarantee. Drawing includes an erase interval, so inspect flicker as well as speed. The intentionally simple visuals and silence leave those questions visible.

Before confirming the order and writing lessons, review the playable tape for readable motion, responsiveness under held and tapped keys, fair recovery time and whether repeated trajectories sustain interest. Check whether keeping the paddle stationary can exploit the geometry. Automated interception alone cannot answer enjoyment or learner comprehension.

If human play exposes a need for richer return rules, assess their teaching cost before extending the game. A smaller game is useful here only if its implementation and explanations stay smaller too.
