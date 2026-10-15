# Stored values: learner tasks

These are draft trial prompts, not a published lesson or an examination. Choose
one starting route. You do not need to complete the other routes first. Say what
you think will happen before checking an answer or running a program. It is fine
to say that a term or instruction is unclear.

## Finding your way

Begin at [Start Here](https://code198x.com/start-here/). Find either the shared
explanation of variables, the Spectrum BASIC introduction or the Spectrum
assembly introduction. Tell the observer which you chose and why. Find the
lesson named below through the site's navigation. If you need help, ask; the
observer will record what helped.

## Route F: reasoning with pseudocode

Read [A Place to Remember](https://code198x.com/foundations/basics/unit-04/).
This is notation to reason about, not code to enter into the Spectrum.

1. Before opening “Check your prediction”, write down the three output lines
   and the value left in `score`. Explain what each `SHOW` does to that value.
2. Without looking at the worked result, trace this new example:

   ```text
   LET lives = 3
   SHOW lives
   SHOW lives
   LET lives = 1
   SHOW lives
   ```

   What appears, and what remains in `lives`? Does the final assignment change
   the output already shown? Explain why.
3. Someone changes only the second `SHOW lives` to `SHOW life`. What would you
   check first? Has the earlier `SHOW` used up the value?
4. Write your own short example that shows a stored value twice, replaces it,
   then shows the replacement. Choose your own variable name and values. Explain
   which instruction changes the stored value.

## Route B: Sinclair BASIC

Read [Remember a name; keep the program](https://code198x.com/systems/sinclair-zx-spectrum/basic/meet-basic/unit-02-remember-and-save/).
Use the opening lesson if you need help with numbered lines or keyboard entry.
You may edit the listing using your device's normal keyboard instead of typing
Spectrum keyword combinations. Keep a copy of any work you want to retain.

1. In the editable listing, enter this complete program. Before choosing
   **Run this code**, predict its output and explain what each `PRINT` reads.

   ```sinclair-basic
   10 LET n$="ONE"
   20 PRINT n$
   30 PRINT n$
   40 LET n$="TWO"
   50 PRINT n$
   ```

2. Run it and compare. Explain why changing the variable does or does not change
   the words already displayed.
3. Change line 30 to `30 PRINT m$`. Predict the result, then run. Explain the
   report and repair the program by changing that line alone.
4. Create a new program with a different text variable, values and greeting.
   Show the first stored value twice and its replacement once. Predict before
   running. Download the current source or tape using the available controls.

The `$` belongs to Sinclair BASIC's text-variable name. Its `PRINT` punctuation
is not the punctuation used by Foundations' `SHOW`.

## Route A: Z80 assembly

Read [A byte becomes pixels](https://code198x.com/systems/sinclair-zx-spectrum/assembly/meet-assembly/unit-02/).
The previous lesson explains registers, addresses, assembling and running; use
it if those terms are new. You do not need BASIC.

1. Complete the lesson's three experiments, making a prediction before each
   run. Explain the difference between the pattern byte, register A and the
   copy in screen memory. What does the label `pattern` name?
2. Change `%10101010` to `%11110000` but do not assemble yet. Predict whether
   the running screen and its memory reading change. Check, then assemble and
   run and explain the difference.
3. Immediately after the existing `ld ($4000),a`, insert:

   ```z80
   ld a,%00001111
   ld ($4000),a
   ```

   Before running, predict the final eight pixels. Does the new write combine
   with the old one or replace it? Is the byte stored at `pattern` changed by
   those two instructions? Explain from the source and the observed bitmap.
4. Change only the second destination to `$4001`. This is the next bitmap byte,
   controlling the next eight pixels to the right. Predict the two groups of
   pixels and test. If you meant to replace the first group, identify the
   instruction that sends the value somewhere else and repair it.
5. Choose a different pattern of your own. Make the first eight pixels show it,
   then replace those pixels with a different pattern in the same run. Download
   your edited source and explain which write determines the final result.

## Optional depth

If you want to know how a BASIC implementation stores variables, explore
[Variables and Memory](https://code198x.com/vault/techniques/variables-memory/).
It compares specific machines and uses more advanced terms; it is optional.
Find one statement about the Spectrum's storage and say how it differs from
Foundations' named-box explanation. You do not need to understand the whole
article to complete these tasks.

The observer keeps expected answers separately. Predictions, requests for help
and unexpected results are useful evidence; there is no score to maximise.
