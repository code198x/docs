# Put your first message on screen

In Bank or Risk, we will roll a die, keep points or risk another roll, and try
to reach 30 over five rounds. Our first program puts the game's name and an
invitation on screen. Then we will change what it says.

![The later Bank or Risk board: a six has been banked, six points are secured and one of five rounds is complete.](https://raw.githubusercontent.com/emu198x/docs/a35897e2b965b6ec20063d4e2749bce1d412b1cf/plans/2026-10-19-amiga-native-save-investigation/fix/captures/cold-native-bank.png)

This is where we are heading: a die, a score and a choice to make. We will
build those pieces in steps; today we need only the message.

We are using AMOS Professional 2.00. Start in its editor with an empty program:
a space where we can type instructions. You do not need to have used another
programming language. If you already recognise these commands, try the edit
and repair below, then continue to [keeping your work](02-keep-your-words.md).

## Type, check and run

Type these five lines, pressing Return after each one. Use ordinary double
quotes, `"`, around the words. Do not add numbers at the start of the lines.

```text
Cls 0
Print "BANK OR RISK"
Print "Bank points or risk another roll."
Wait Key
End
```

Press F2 to check the instructions. AMOS should report **No errors**. If it
points to a line, compare that line with the listing before continuing.

Press F1 to run. You should see:

```text
BANK OR RISK
Bank points or risk another roll.
```

The words remain on screen. Press Space to let the program finish. When AMOS
shows its end prompt, press Return to return to the editor. The end prompt
is not the place to edit your program.

If your computer uses its function keys for other jobs, use the emulator's
mapping for F1 and F2. The AMOS editor must receive those keys.

## What did each line do?

AMOS works through these instructions from top to bottom.

`Cls 0` clears the display using colour entry 0. A colour entry is a numbered
place in the screen's palette. We will choose our own palette when we draw
the die; this program uses the colours already present in AMOS.

`Print` displays the words inside the double quotes, then moves to the next
text line. The quotes tell AMOS where the text begins and ends. They are
not part of the message it displays.

`Wait Key` pauses until a key is pressed. Without a pause, the program would
reach `End` immediately after displaying its words. `End` finishes the program;
it does not save your instructions to disk.

## Change the invitation

Find the second `Print` instruction, on the third line of the program. Keep
the other four lines. Replace that one line with:

```text
Print "Can you secure 30 points?"
```

You can move there with the cursor arrows and edit the words. To replace the
whole line in the checked AMOS editor, put the cursor on it, hold **Control**
and press **Q**. This clears that line and leaves a blank line to type into.
Use Control here, rather than an Amiga key or your host's application-quit chord.

Before running, predict the two lines that will appear.

<details>
<summary>Check your prediction</summary>

```text
BANK OR RISK
Can you secure 30 points?
```

Only the invitation changes. The first `Print` still supplies the title.
Changing words inside quotes does not change what the `Print` instruction does.

</details>

Press F2, then F1. Compare what happens with your prediction. Press Space,
then Return at the end prompt, to return to editing. The complete changed
program is:

```text
Cls 0
Print "BANK OR RISK"
Print "Can you secure 30 points?"
Wait Key
End
```

## Repair one instruction

In the title line, change `Print` to `Prit`, leaving the quoted title alone.
Press F2. AMOS should point out an error instead of reporting No errors.
We have changed an instruction name, so AMOS cannot treat it as the same command.

Which part needs repairing: the name before the quotes, or the title inside them?

<details>
<summary>Show the repair</summary>

Restore the missing `n` so the line reads `Print "BANK OR RISK"`. The title
was already correct. Press F2 again; expect No errors before running.

</details>

Keep the repaired program with the changed invitation. In the
[next lesson](02-keep-your-words.md), we will save it, start a fresh session,
and find out whether our edit survived.
