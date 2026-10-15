# Assessor notes: sequence and submitted text

All actual learner outcomes remain **not observed**. Do not enter these expected
answers as learner evidence.

1. SHOW displays the words; it does not dress anyone. A valid Goodbye when Hello
   was intended shows a wrong intention without an instruction error.
2. Go outside remains third. Check the intended running version and completion
   state, and inspect earlier output; absence from the current screen alone is
   not proof that an instruction never ran.
3. Before Enter the example waits. Enter submits the text, stores it and lets
   the following SHOW use it. Waiting is not the same as submitted empty text.
4. Ada has length 3 and gives Hello, Ada on both runs. Empty has length 0 and
   gives "Hello, ". Three spaces has length 3 and gives four spaces after the
   comma. Padded Ada has length 5 and gives two spaces before Ada and one after.
   Text 42 has length 2 and gives Hello, 42; there is no numeric conversion.
5. The greeting literal needs its own space after the comma. Spaces in the input
   are separate. This example accepts text without checking a name.
6. SHOW "Hello, ", name, "!" gives Hello, Ada! or "Hello, !" for empty text.
7. Accept any conversation with a stated consistent input contract and correctly
   traced normal, repeated and boundary values. A deliberate rejection rule is
   extra behaviour to describe, not something ASK silently supplies.

The optional target contrast uses Spectrum string INPUT with its supplied
quotation marks and PRINT semicolons for immediate joining. Pseudocode SHOW's
comma does not imply Sinclair BASIC PRINT's comma spacing. No other target's
input policy or numeric parsing follows from this pilot.
