# Volley prototype and teaching review

**Status:** Eight runnable checkpoint sources implemented; execution findings are recorded below. The prototype and plan are approved as the basis for the agreed course order; eight lessons and an overview are drafted but not yet published.

The [brief](brief.md) owns the proposed game and scope. Sources live in `code-samples/sinclair-zx-spectrum/basic/volley/prototype/`; each `steps/step-NN.bas` is a complete program. Verification scripts, source hashes and results belong beside the sources.

## Implemented choices

One three-cell paddle moves vertically at the left of a character court. A one-cell ball travels diagonally in fixed steps. Top, bottom and right boundaries reflect it. Paddle contact adds one return; missing ends the rally. A/Z move, S serves, R returns to the serve screen after a miss, and Q exits. Serving and retry require release before advancing.

The prototype is silent. Checkpoints 7–8 add a blue PAPER playfield, cyan walls, a yellow PAPER paddle and a white ball. They retain a provisional `PAUSE 2`; this is not a fixed wall-clock update guarantee. The first review can concentrate on input, motion and contact without sound or custom graphics introducing extra work.

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
| Colour the court | PAPER-coloured spaces, temporary PRINT colours and restoring the background | Recall colour from Bright Spark; keep the original drawing order for comparison |
| Keep the ball visible | Calculate before erasing; draw old/new cells consecutively; update only paddle endpoints | Compare the actual versions and explain both visibility and any change in cadence |

The transition into collision restructures direct position updates into candidate coordinates. Teach the reason before the change: contact must be decided before drawing, including the row after a wall reflection. The miss flag is communication from a routine, not a new game engine.

This supports the proposed bridge: Volley establishes position/direction, continuous input and simple contact; Touchdown can concentrate on changing speed, fuel and landscape. It does not yet establish an appropriate lesson count or prove the finished rally is enjoyable to human players.

## Verification and remaining review

The baseline run checked the original six checkpoints, upper/lower paddle limits, misses, retry, six contact boundaries and a fresh-process tape load. A subsequent screen-observed rally exposed a score-column error (the first return displayed as 10); the source now aligns score updates with the initial counter. The corrected final game passed a fresh-process tape load, serve, miss, retry and exit, plus centre/edge/miss/corner contact checks. A screen-observed automated player completed eight returns, with the score advancing exactly from 1 through 8. Results and source/tape hashes are maintained with the samples. Use those results and hashes for exact execution coverage. ROM editing, MCP-driven keyboard events and screen observations are configuration-specific evidence; they are not native host-keyboard or original-hardware acceptance.

The drawing comparison executed the same no-input path in checkpoints 7 and 8:

| Checkpoint | Sampled frames | Frames with no decoded ball | Longest absent run |
|---|---:|---:|---:|
| 7: colour, erase first | 328 | 206 (63%) | 6 frames |
| 8: calculate first, consecutive erase/draw | 204 | 0 | 0 frames |

With X held, the respective counts were 208 absent frames out of 291, and zero out of 204. These figures were refreshed using ROM entry without redundant token spaces before writing the lesson. These are frame-by-frame samples of decoded screen memory, not emitted-video measurements or a claim that no raster artefact is possible. The shorter run shows that reduced drawing work also increases cadence with the same PAUSE setting.

Both coloured checkpoints passed checks for cyan walls, black score background, upper/lower yellow paddle limits and restoring every visited ball/paddle cell to blue. Checkpoint 8 passed centre, both paddle edges, both adjacent misses and a wall–paddle corner; its exported tape passed fresh-process play, held retry and quit. An automated player sustained eight returns on that tape, with the score advancing from 1 to 8. The coloured rally averaged about 5.35 PAL frames between observed positions, including startup in the measured intervals.

The inspected court capture holds the initial ball with a declared test-only PAUSE 0. The distributed tape restores PAUSE 2. Source/tape hashes, measurements and the capture manifest live with the samples. Native review of the new cadence and flashing remains distinct from these checks.

During lesson review, revisit the playable tape for readable motion, responsiveness under held and tapped keys, fair recovery time and whether repeated trajectories sustain interest. Check whether keeping the paddle stationary can exploit the geometry. Automated interception alone cannot answer enjoyment or learner comprehension.

If human play exposes a need for richer return rules, assess their teaching cost before extending the game. A smaller game is useful here only if its implementation and explanations stay smaller too.

## Teaching the drawing improvement

Use checkpoints 7 and 8 side by side. Ask the reader to locate the erase, calculation and draw operations before changing them. Trace one update with the ball already visible: input and contact calculation do not require removing its image.

Checkpoint 8 removes the early erase and the unconditional paddle redraw. Once contact is resolved, line 248 restores the old ball cell and draws the new one consecutively. The loop returns to input, so it does not perform a duplicate draw at its beginning. Paddle movement clears only the trailing cell and paints only the leading cell.

Useful authored questions and explanatory feedback:

- **What can the player see while the collision code runs?** The current ball remains visible. The next position can be calculated without changing the displayed position.
- **Why does clearing with a space sometimes leave a patch?** A space still has a PAPER colour. Restore the court's blue rather than the paddle's yellow or the score strip's black.
- **Which cells change when a three-cell paddle moves one row?** One trailing cell clears and one leading cell appears; the other two stay occupied.
- **Will fewer PRINT operations leave the speed unchanged?** Not necessarily. This loop's work contributes to its cadence; compare the result before adjusting pacing.

Explain this as a reusable drawing technique, not a promise of smooth pixel motion or an introduction to double buffering. The current character-cell movement is still deliberately discrete.

## Keyword entry

Maintained Volley sources and website listings retain readable keyword spacing. The local entry helper suppresses redundant spaces only when converting source lines or verification edits into ROM keystrokes, preserving strings and compound token names. `verification/spacing.py` checks the stored tokenised program, including numeric payloads and string contents. `spacing-source-map.json` maps readable source hashes to the verified normalised entry hashes. Restoring readable sources produces exactly the same normalised input and does not require changing the corrected tape.

## Approved lessons

The website holds a module overview and eight descriptive lesson files in `src/drafts/volley/`, following the checkpoint titles above. Development-only review routes use the existing module and unit layouts and show Volley as Game 2. The production catalogue remains unchanged until publication.

Each lesson states its starting program, exact edits, locally explained syntax, expected observations and a question with explanatory feedback. Short opening programs are shown in full; longer changes use maintained snippets plus complete-program disclosures. The last two lessons preserve the colour-only/erase-first version and then explain consecutive erase/draw and selective paddle updates. The final lesson includes tape save/load and a fresh-session play/retry/quit check.

`verification/lessons.py` checks the website roster's eight edit sets and the five change snippets against the complete checkpoints. The drawing verifier re-enters the baseline as well, ensuring its timing evidence matches current keyword spacing. Earlier runtime checks still establish the original stages; the source-spacing map and token-stream equivalence check connect them to the readable listings and their normalised ROM input.

The publication change adds the unit catalogue, places Volley after Bright Spark, reconciles module numbers and links, and redirects the review bookmarks. `website/scripts/volley-roster.json` retains the edit sets used by the sample verifier. Deployment remains a separate check.

Draft validation passed the eight edit-set checks and all 36 browser combinations (overview plus eight lessons, two widths and two themes), including source availability, links, keyboard question reveals, image loading, overflow and serious/critical Axe checks. The website production build passed with 69 tests passing and nine existing skips; a final static build confirmed that the review routes are excluded. The maintained website review checker can repeat the browser checks.
