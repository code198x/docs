# AMOS and Blitz: selected opening objectives

The source inventory counts 17 authored AMOS units and 15 Blitz units, plus one
setup page and one module overview per track. We read the two setups, two
overviews and first three units of each track. Later-unit counts/hashes are an
inventory only. Both tracks are peers of assembly; neither is a prerequisite for
the other. These observations are editorial, not learner validation.

| Selected unit | Observable objective from the actual lesson | Knowledge used and local support | Maintained example |
| --- | --- | --- | --- |
| AMOS 1: Type and Run | Edit, run and change quoted output; explain why the result stays visible | Editor and key use; Print, quotes, Hide and Wait Key explained locally | `amos/meet-amos/unit-01/hello.amos` |
| AMOS 2: Print and the Screen | Place text using column/row and distinguish cursor placement from drawing; explain why clearing after printing removes output | Unit 1 output; Cls, Locate, zero-based cells, axis directions and command order explained locally | `amos/meet-amos/unit-02/screen.amos` |
| AMOS 3: Variables and Types | Distinguish literal names from stored values, update a score and join a label/value | Assignment and arithmetic; number/string distinction, dollar suffix, semicolon and a score update explained locally | `amos/meet-amos/unit-03/variables.amos` |
| Blitz 1: Type, Compile, Run | Distinguish source, compile and execution; change quoted output and compare text with arithmetic | Editor/compiler controls, NPrint, MouseWait and End explained locally; timing claims need qualification | `blitz/meet-blitz/unit-01/hello.bb2` |
| Blitz 2: Amiga Mode and Blitz Mode | Trace bitmap creation, drawing and display; explain which mode supplies OS services | Unit 1 compile loop; bitmap, slice, bitplanes and display order introduced locally; multiple ideas enter together | `blitz/meet-blitz/unit-02/blitzmode.bb2` |
| Blitz 3: Variables and Blitz's Types | Predict the stated byte wrap, choose a wider representation and distinguish numeric/text storage | Variables assumed in the opening; suffixes and the −128..127 byte interval explained locally, but comparative AMOS safety/speed claims are unsupported here | `blitz/meet-blitz/unit-03/types.bb2` |

Paths above are relative to `code-samples/commodore-amiga/`. Each public lesson
uses CodeFromFile. All six capture drivers' typed payloads exactly match their
included files. That is source consistency, not a successful compiler or runtime
result. The preserved screenshot for Blitz 3 visibly shows −106; we have not
freshly reproduced it or qualified another compiler's behaviour.

## Entry and transfer

Both module overviews direct complete beginners to Foundations and assume
variables, loops and decisions; the first units then reintroduce several of
those ideas. That is an entry-contract choice worth reviewing with a learner,
not proof that the track is inaccessible or a reason to force the Spectrum
lesson structure onto it. Blitz explicitly says AMOS attendance is unnecessary.

Useful distinguishing probes after the setup/runtime route is qualified:

- In AMOS 3, predict a quoted `"SCORE"` versus a read of `SCORE`, then move the
  update below the Print. Explain which shown value changes and why.
- In Blitz 3, predict the stated byte/word difference, then verify the actual
  compiled result and representation contract on the named version. A host-side
  two's-complement calculation cannot alone qualify the compiler.
- In Blitz 2, identify where the image exists before Show, and explain a changed
  draw/display order. Do not infer OS behaviour or speed from a still image.

These are candidate probes, not executed learner tasks or new course requirements.
Use the established separate learner/assessor method when developing the selected
trial. The first priority is a reproducible unit-1 route for each language.
