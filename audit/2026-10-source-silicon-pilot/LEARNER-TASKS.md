# Learner tasks: source, codes and failed translation

Use the From Source to Silicon overview and five units. No machine setup is
required. Work on paper in the teaching notation; a helper should record what
happened without coaching. Keep the assessor sheet separate.

1. Predict `INC, INC, DOUBLE, SHOW` from a starting box of zero. Write its codes
   and the displayed result. Explain why character codes for the letters INC
   are not the same thing as our invented instruction code.
2. Trace the revised translator for `INC, MYSTERY, DOUBLE, SHOW`. Record found,
   valid and pending after each word, and distinguish diagnostic text from
   emitted program codes. Does the final recognised word repair the error?
3. Try an unknown word at the beginning, at the end, and twice. Then try an
   empty program. Explain which cases are rejected and why no emitted codes
   can mean two different things.
4. Change the source to `INC, DOUBLE, INC, SHOW`. Predict the codes and answer.
   Explain what happens if we edit the source but hand the model machine the
   old output. Describe the steps needed to make the edit take effect.
5. Design a short program that shows two different values. Give its source,
   encoded version and expected outputs, then trace both routes independently.
6. In unit 2, distinguish the processor executing the interpreter from that
   interpreter reading a BASIC token. What could a memory snapshot show, and
   what would it fail to prove about the full execution path?
7. For unit 5's invented four-update table, calculate both averages and count
   missed 12ms deadlines. Explain why this does not prove a worst-case bound or
   establish which language every game should use.

Optional: follow unit 4's diagnosis link and identify an observation that could
separate a wrong board rule from a drawing error. The longer Meteor Storm
experiment remains optional; its controls and workload need separate records.

Record the learner's own answers, revisions, requested hints and anything they
could not interpret. Leave timing, independence, retention and transfer unknown
until observed; do not fill in expected answers as learner evidence.
