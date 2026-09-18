# Cipher — source and scope review

Inspected the published overview and final source at
`code-samples/sinclair-zx-spectrum/basic/cipher/unit-06/cipher.bas`, plus the
retained brief, before authoring the new trial. The source baseline is samples
commit `a2f5bdd`. This review is source evidence,
not fresh execution of the old game.

The old program already reveals all matching letters, stores tried letters and
tracks wins/losses. Its input at line 400 accepts a string without first requiring
one alphabetic character. Empty and multi-character input can reach the attempt
and miss logic; some lowercase multi-character strings are reduced to their
first letter by the normalisation expression. The tried-list display assumes
short input. The round cycle provides no explicit quit control.

The old brief equates word length with difficulty and assumes an eight-topic
progression with prior-volume attendance. Neither is retained as a design rule.
The overview's six lessons and final source are the implementation; the brief's
planned features do not establish what was built. The new bounded brief keeps
string mutation and content selection, replaces arbitrary string entry with
single key guesses, and makes the current choices and mistakes visible.
