# Counted loops: ranges and body placement

Repeating unit 1's counted ranges are correct under the shared notation. This
slice makes their contract explicit and gives readers a way to distinguish
empty, one-visit and inclusive ranges, then diagnose a line moved across END.
[Website #756](https://github.com/code198x/website/issues/756) tracks the bounded
explanation gap. The existing numeric examples remain intact.

Five host models and **11 fresh Spectrum ROM program runs** agree on the selected
visit order, output placement and totals. The proposed lesson adds two closed
predictions, local variable/output recall and an optional existing BASIC link.
The [learner tasks](LEARNER-TASKS.md) and [assessor notes](ASSESSOR.md) prepare an
independent trial. No learner is available: effectiveness, retention and unaided
transfer remain unknown. Umbrella #114/#115/#124 stay open.

## Scope and evidence layers

The [plan](../../plans/2026-10-16-counted-loop-pilot.md) bounds this slice.
Website baseline is `6360218ff5095dd352679fdffa265e8b09297bb5`, after approved
website #755 merged. Docs baseline is
`e68cf6d9b03c98ae2bb20936a947d810d73246dc`, after approved docs #85 merged.
[Identities](identities.json) retain source, specification, verifier and earlier
report hashes. Existing packages, the pinned UI kit and generated assets were
reused in isolated checkouts. No dependency was added or installed.

The earlier [repetition pilot](../2026-10-repetition-pilot/REPORT.md) already
observed Spectrum FOR 1-to-0, 1-to-1 and 1-to-3. Those results remain **earlier
execution evidence**, not fresh runs from this slice. Its randomness and
pre/post-test investigations are not repeated here.

The new [model](model-counted.json) covers 1-to-0, 1-to-1, 1-to-3, 0-to-3 and
-2-to-1. It enumerates visits and independently checks count, endpoints and
arithmetic-series total. It traces a message after the loop and the same message
inside the body. This is a host model of the stated rules, not a new pseudocode
interpreter or a proof of every possible loop.

[Fresh native results](native-counted.json) retain complete output for both
placements at all five ranges, plus a misplaced accumulator reset. Source
fixtures are keyboard-entered numbered BASIC programs using the existing ROM
transport. No source/result memory injection or ROM patch is used. NEW must
return to its positive ready state before entering the next program. Normal
completion and the complete expected output are required; missing or extra output
fails. Each ROM identity read has its length checked. The process is closed and
its exit verified after success or failure.

## Contract and source review

[Curriculum design](../../specifications/curriculum.md),
[unit guidance](../../specifications/unit.md) and
[pseudocode](../../specifications/pseudocode.md) preserve independent entry and
separate teaching notation from target syntax. The notation guide already gives
inclusive ranges; the unit's troubleshooting already gives a zero-pass example.
We clarify that introductory examples use fixed whole-number endpoints, ascend
by one and leave the bounds/counter unchanged in the body. This records the
existing convention rather than adding STEP syntax or prescribing a target's
post-loop counter value.

The original trace caption referred to two repeated lines although its body has
one SHOW line. That caption now describes the repeated SHOW. The empty-range
code span is kept together so its source line break does not obscure the range.
The broad statement about an outside line running once is tied to the concrete
straight-line example; it is not a promise about a line inside another outer loop
or an execution interrupted before reaching it.

Sinclair Research's *ZX Spectrum BASIC Programming*,
[chapter 4, Looping](https://worldofspectrum.org/ZXBasicManual/zxmanchap4.html),
pp. 31–34, explains the counter, NEXT, steps, proper nesting and the empty-range
search for a matching NEXT. This supports the Spectrum comparison. It does not
establish another dialect's entry rule. Only the installed Spectrum native
emulator was available; other BASIC dialect execution is **skipped**. Original
hardware, STEP variants, fractional bounds and counter mutation are untested.

The optional [Give the answer a rhythm](https://code198x.com/systems/sinclair-zx-spectrum/basic/meet-basic/unit-10-give-the-answer-a-rhythm/)
explains its own FOR/NEXT counter and a sound after the loop. Reading its local
explanations does not require playing the earlier game. Sound is supplementary;
this slice checks the navigation and explanation, not new audio delivery or
whole-game execution. BASIC and assembly remain independent entry points.

All-state counted/FOR/range searches found existing randomness, termination and
unrelated range findings, not a matching unit-1 placement/explanation finding.
The [full objective map](../2026-10-foundations-objectives/MAP.md) keeps its
immutable baseline. This report adds direct unit-1 evidence rather than silently
rewriting that inventory or certifying every objective it lists.

## Results

| Check | Outcome | Boundary |
| --- | --- | --- |
| Exact ascending models | Passed five ranges | Zero/one/three/four visits; exact order, endpoints, totals and message placement |
| Fresh ROM programs | Passed 11 runs | Ten range/placement combinations plus one reset contrast; actual output and normal completion retained |
| Exclusive-end wrong variant | Rejected with nonzero exit | [Known-red record](known-red/rejection.json): shortened end omits the intended third visit and changes its total; complete observed output retained |
| Production and browser checks | See retained record | [Website results](website-results.json) and [browser results](browser-counted.json) identify the actual build, test and keyboard outcomes |
| Learner understanding | Unknown | Prompts prepared; no learner trial or measured improvement |

For 1-to-0, the outside-message version displays BEFORE, TOTAL 0 and AFTER.
The body has no visits; continuation still runs. The
[empty-range capture](outside-1-0.png) shows that actual output and normal ROM
completion. For 1-to-3 with AFTER inside, it alternates 1/AFTER, 2/AFTER,
3/AFTER, then displays TOTAL 6. The [placement capture](inside-1-3.png) records
that result. Both captures were visually inspected.

The reset variant displays 1, 2, 3 but totals only 3: resetting before each
addition erases the earlier partial sum. The correct version totals 6. This is
a deliberately changed program whose observed effect is checked, not a new
claim that any reset inside any loop is wrong. Initialization belongs where
the intended lifetime requires it.

[verify-counted.py](verify-counted.py) runs the model and, with `--samples` and
`--emulator`, the native program checks. The `--wrong-only` mode must fail against
the intended three-visit output. The audit fixtures are test tooling, not new
learner samples. Target syntax/number rules and host model evidence stay separate.

The final production build and all 237 tests pass. Chrome 155.0.8059.80 checks
at 1440×900 and 390×900 pass six keyboard groups. Neither closed nor revealed
answers produced a scoped axe violation or incomplete result; no document
overflow or page errors were observed. Readable wide/narrow answer captures were
visually inspected. These selected checks do not establish whole-site access,
assistive-technology usability or physical-touch behaviour.

The [first browser attempt](browser-context-failure.json) failed before page
results with `Error: Please use browser.newContext()`. The harness had used
Playwright’s shortcut `browser.newPage()`; axe requires an explicitly created
context. We corrected that setup and retained the failed attempt. It is not a
lesson failure or a passing page observation.

[Evidence validation](validation.json) checks source identities, exact fixture
hashes, complete native/model correspondence and local links. A changed source
hash and a missing transcript are deliberately rejected. Run
[verify-evidence.py](verify-evidence.py) with `--website PATH_TO_WEBSITE_REPO`;
the [SHA-256 manifest](SHA256SUMS) retains all evidence identities.

## Next bounded work

Observe the independent prompts when a learner is available. Meanwhile, inspect
Basics unit 3's output-joining contract: quotation marks, values, comma-inserted
spacing and target-language separator differences. Start from the stored-value
and sequence/input pilots and the current pseudocode specification; do not assume
an untested teaching gap is an incorrect example or require a new runtime.
