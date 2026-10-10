#!/usr/bin/env bash
set -euo pipefail

workspace=$(mktemp -d "${TMPDIR:-/tmp}/bcps-lab-01-02.XXXXXX")
cd "$workspace"
mkdir Notes Archive Empty
cd Notes
echo 'BCPS file management practice' > notes.txt
cat notes.txt
cp notes.txt backup.txt
mv backup.txt ../Archive/revision.txt
cd ..
ls
rmdir Empty
test -f Notes/notes.txt
cmp Notes/notes.txt Archive/revision.txt
test ! -e Notes/backup.txt
test ! -d Empty
printf 'All file-management checks passed. Workspace: %s\n' "$workspace"
