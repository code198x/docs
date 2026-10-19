# Keep your words

Our program now asks **Can you secure 30 points?** We want to see those changed
words after leaving AMOS and starting again. That will check whether we saved
our edit, rather than leaving it in the running editor.

You need AMOS Professional 2.00, the repaired program below, and a writable
Amiga work disk. A writable disk permits changes; a write-protected disk does
not. Keep the original runtime disk safe and use a separate work disk for your
programs. If you are using an emulator, establish how it exports modified disk
images before ending your session.

```text
Cls 0
Print "BANK OR RISK"
Print "Can you secure 30 points?"
Wait Key
End
```

If you entered here from another language, type that listing into an empty
AMOS editor project. F2 should report No errors; F1 should show the changed
question. Press Space, then Return at the end prompt, to return to the editor.

## Save an AMOS program

1. Insert your writable work disk before opening the save requester—the window
   in which we choose where to save and what to call the program.
2. In the editor, choose **Save As** with **Amiga+Shift+S**. Use the emulator's
   mapping for an Amiga key when running on another computer.
3. Check the directory field just above the filename field. If the requester
   says Device not available because the old runtime disk was removed, press
   a key to dismiss that message. Click the directory field and replace its
   contents with `DF0:*.AMOS`, then press Return to read that directory.
   `DF0:` names the internal drive; `*.AMOS` asks it to list program names
   ending in `.AMOS`. Remove the old path rather than adding text to its end.
4. Click in the filename field at the bottom and enter `welcome.amos`.
   Check that it is the filename, rather than text added to the directory path.
5. Choose **OK** or press Return while editing the filename. Allow disk activity
   to finish. Check that the requester closes without reporting an error.

The filename helps us find the program again. Saving writes AMOS's native
program format to the chosen disk. It does not create a screenshot of the
words, and the editor's No errors message does not mean a file has been saved.

If your emulator keeps disk changes in memory, export the updated work disk
using its host disk-export operation before closing the session. Keep that
exported image: an unchanged source image will not contain your new file.
Saving an emulator snapshot preserves the machine's session; we still need
the separate native file for the reopen check below.

## Reopen, rather than restore

Before leaving, predict what `welcome.amos` should display when we load it.

<details>
<summary>Check the expected result</summary>

It should display BANK OR RISK and **Can you secure 30 points?** The earlier
invitation—Bank points or risk another roll.—would identify the wrong version.

</details>

1. Keep the saved work disk, or the exported image containing it. End the old
   editor session and start AMOS again from its runtime disk.
2. Insert the saved work disk. Choose **Load** with **Amiga+L**.
3. Select the work disk's directory explicitly. If it still names the removed
   runtime volume, dismiss the message and replace the directory field with
   `DF0:*.AMOS`, as when saving. Press Return to read the directory. Finding
   the right drive is different from entering a name in the filename field.
4. Select `welcome.amos` from that disk. Check the listing: the question should
   be `Can you secure 30 points?`.
5. Press F2, then F1. Compare the displayed words with your prediction.
   Press Space and then Return at the end prompt to return to editing.

AMOS may ask you to reinsert its system disk when it needs a runtime file.
Return the disk it names and choose Retry. That request does not mean your
saved program should have been placed on the system disk.

## If the words or file are wrong

| What you observe | What to check before changing the code |
| --- | --- |
| The old invitation appears | Confirm which version you saved and which filename and disk you loaded. |
| File not found | Check the selected directory and the exact saved filename. |
| The disk is write protected | Use a writable work disk; keep your edited listing while correcting the disk choice. |
| The disk is full | Choose a work disk with enough free space. Waiting longer does not create space. |
| The file disappears after restarting the emulator | Check whether you retained the modified disk image or reopened its unchanged source. |

Seeing the changed question in a fresh session gives us evidence that the edit
survived saving and loading. Keep `welcome.amos` as a checkpoint we can return
to before we begin drawing the die.
