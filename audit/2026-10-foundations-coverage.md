# Foundations umbrella coverage

Continue the original audit while learner trials remain pending. The pause on
expanding the public first-session pack does not pause #114/#115/#124.

This is an inventory and evidence map, not a claim that every authored lesson
has been audited. At website baseline
`b1ddbdfc5f72e79e2a97bd6ed42ae8402e25c883`, Foundations has ten modules and 39
unit files. Module catalogue `complete` status describes authored content; it
does not certify conceptual accuracy or educational effectiveness.

## Objectives and knowledge used

These objectives come from the authored unit titles/headings and the module
catalogue. Knowledge used is distinct from compulsory course attendance. System
BASIC and assembly entry remain independent; shared subjects offer support.

| Module | Units | Objectives and knowledge used | Evidence in this umbrella run | Remaining bounded work |
| --- | --- | --- | --- | --- |
| Basics | 5 | Instructions/order, output, variables, input; ordinary text and numbers | [Stored-value pilot](2026-10-spectrum-learner-journey/stored-value-pilot/REPORT.md), principally units 3–4 | Complete objective coverage of units 1–2/5; input contracts and ordering transfer |
| Working It Out | 3 | Arithmetic/precedence, updating a value, division/remainder/rounding; variables and number order | [Arithmetic pilot](2026-10-arithmetic-pilot/REPORT.md) covers the overview and three units | Real learner outcomes and further target-language mappings remain unobserved |
| Decisions | 4 | IF/ELSE, chains, stored flags, compound conditions; values and comparisons | [Decisions/boundary pilot](2026-10-decisions-boundary-pilot/REPORT.md) samples unit 1; current Boolean slice reads units 3–4 as context | Chains, flag lifetime and fractional/range boundaries remain incompletely covered |
| Truth Tables | 3 | Boolean combinations, NOT/AND/OR/XOR, De Morgan equivalence; conditions and stable input values | [Current Boolean pilot](2026-10-boolean-logic-pilot/REPORT.md) | Learner understanding and unaided transfer remain unobserved |
| Repeating | 3 | Counted, pre/post-test loops and repeated work; conditions and updates | [Repetition pilot](2026-10-repetition-pilot/REPORT.md) | Broader termination/state-invariant coverage; current checks do not exhaust every loop example |
| Structure | 4 | Lists, named jobs, parameters/results, diagnosis; loops and changing values | [Structure pilot](2026-10-structure-pilot/REPORT.md): all four units read, selected outputs/traces and target contrasts checked | Actual learner outcomes, real-language list aliasing and further target contracts remain unverified |
| Counting in Twos | 4 | Bases, bytes/words, signed representation; place value and arithmetic | [Numbers pilot](2026-10-numbers-pilot/REPORT.md), principally units 3–4; [binary/hex pilot](2026-10-binary-hex-pilot/REPORT.md) samples units 1–2 | Actual learner outcomes, further target representations and signed-boundary cases |
| Working the Bits | 5 | Masks/shifts, codes, floating/fixed point; representation and conditions | [Bits/shifts](2026-10-bits-shifts-pilot/REPORT.md), [characters](2026-10-character-codes-pilot/REPORT.md), [fractions](2026-10-fractions-pilot/REPORT.md); [decimal investigation](2026-10-decimal-investigation/REPORT.md) | Broadest sampled module; not a learner validation or every-target proof |
| Gates and the Adder | 3 | Gate models, half/full adders, carry; Boolean tables and binary place value | [Gates/adder pilot](2026-10-gates-adder-pilot/REPORT.md): all three units, selected circuit/table cases and native arithmetic contrasts | Physical specimen/timing measurements and actual learner outcomes remain unobserved |
| From Source to Silicon | 5 | Source/bytes, interpretation/translation, interfaces and measurement; code/data and execution | Existing publication is source context, not a full audit in this run | Complete objective/assumption map and reproducible execution/performance comparisons |

The catalogue, module openings and unit headings supply this inventory. The
[retained heading list](2026-10-boolean-logic-pilot/foundations-inventory.json)
identifies all 39 unit files. This is not a full text or execution review of them. Source-level findings may exist in other project reviews; “not
linked in this run” does not assert that no earlier work exists.

## Game maths and other boundaries

Game maths is a separate responsibility under The Craft, not another Foundations
module. The main `craft/maths-for-games` directory has eleven unit files at this
baseline; the separate dice experiment also belongs to Maths for Games. A
probability experiment or the representation pilots do not establish full maths
coverage. Inspect the authored paths and objectives before selecting a later
maths slice. No claim of mathematical prerequisites for every game is made here.

The Boolean and gate pilots do not qualify a physical specimen's electrical/timing
behaviour, all target-language truth representations or short-circuit rules. Native results
name their machine and inputs. Browser checks name their page set and viewports.
Actual learner outcomes remain pending across these pilots.

## Next work and stopping points

The Boolean, Working It Out and Structure slices now have linked source, native
and browser evidence. Real learner outcomes remain pending.

The binary/hex pilot adds selected evidence for Counting in Twos units 1–2.
The gate/adder pilot adds settled Boolean model and carry evidence. Next inspect
all five From Source to Silicon units: map their source/bytes, interpretation,
translation and performance claims before selecting a bounded execution example.
Continue source and technical work while learner observations wait.

Keep the public [first-session pack](https://code198x.com/try/) small and ready to
share. New learner observations may reorder the audit queue or require a repair;
absence of learners is not a reason to stop unrelated source/technical work.
Do not close the parent issues from this inventory or from green automated checks.
