# Labs 1–2: Command-line file management

## Aim

Create directories and files, navigate folders, list contents, copy and rename files, and remove an empty directory.

## Commands

| Action | Linux Bash | Windows Command Prompt |
| --- | --- | --- |
| Current directory | `pwd` | `cd` |
| Create a directory | `mkdir Notes` | `mkdir Notes` |
| Change directory | `cd Notes` | `cd Notes` |
| List files | `ls` | `dir` |
| Create a text file | `echo Hello > notes.txt` | `echo Hello > notes.txt` |
| Read a file | `cat notes.txt` | `type notes.txt` |
| Copy | `cp notes.txt backup.txt` | `copy notes.txt backup.txt` |
| Rename | `mv backup.txt revision.txt` | `ren backup.txt revision.txt` |
| Remove one file | `rm revision.txt` | `del revision.txt` |
| Remove an empty directory | `rmdir Empty` | `rmdir Empty` |

`>` replaces the target file's contents; `>>` appends. `rmdir` only removes empty directories. Run the practice in its own new folder.

## Linux procedure

From the repository root, run `bash lab-01-02/file-management.sh`.
The script creates a fresh temporary workspace, performs the commands, checks their results and prints its location. Open the printed folder to inspect `Notes/notes.txt` and `Archive/revision.txt`.

## Windows procedure

Run these commands one at a time in **Command Prompt**, starting in a practice location where `BCPS_Practice` does not already exist:

```bat
mkdir BCPS_Practice
cd BCPS_Practice
mkdir Notes Archive Empty
cd Notes
echo BCPS file management practice>notes.txt
type notes.txt
copy notes.txt backup.txt
move backup.txt ..\Archive\revision.txt
cd ..
dir
rmdir Empty
type Archive\revision.txt
```

## Expected result

```text
Notes/notes.txt       BCPS file management practice
Archive/revision.txt BCPS file management practice
```

The empty folder and the temporary copied file are gone. The original is preserved.

## Viva

- `cd ..` moves to the parent directory.
- Copying preserves the source; moving changes its location or name.
- Relative paths start from the working directory; absolute paths identify a location from the filesystem root or drive.

Reference: [GNU file operations](https://www.gnu.org/software/coreutils/manual/html_node/Basic-operations.html).
