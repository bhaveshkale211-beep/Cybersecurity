# Assignment 02 — File Operations

Following on from the navigation assignment, this one was about actually doing things to files — creating one, copying it, renaming it, and deleting the original. Basically the four commands you'll use every single day: `touch`, `cp`, `mv`, `rm`.

## What I was trying to do

Create a file inside `module1`, copy it over to `module2`, rename the copy, then delete the original — checking after each step that things actually ended up where I expected.

## What I actually ran

Working from inside `~/Training` (the folder I made in the last assignment):

```
touch module1/assignment.txt
ls
ls module1
pwd
cp module1/assignment.txt module2/assignment.txt
ls
ls -l module2
mv module2/assignment.txt module2/assignment_backup.txt
ls -l module2
rm module1/assignment.txt
ls -l module1
ls -l module2
```

![Terminal — touch, cp, mv, rm](./screenshots/01-touch-cp-mv-rm-file-operations.png)

Going through it in order:

- **`touch module1/assignment.txt`** — creates a new, empty file. (`touch` is technically meant for updating timestamps, but if the file doesn't exist it just creates it, which is why everyone uses it for that.)
- **`ls`, `ls module1`, `pwd`** — quick sanity checks. `ls module1` showed `assignment.txt` was there, and `pwd` confirmed I was still in `/home/kali/Training`.
- **`cp module1/assignment.txt module2/assignment.txt`** — copies the file into `module2`. The original stays put — `cp` duplicates, it doesn't move.
- **`ls -l module2`** — confirmed the copy landed: `-rw-rw-r-- 1 kali kali 0 Aug 17 05:04 assignment.txt`. Size is 0 because I never wrote anything into the file, it's just empty.
- **`mv module2/assignment.txt module2/assignment_backup.txt`** — this is how you rename a file in Linux. There's no separate "rename" command; `mv` with the same directory and a new name does it.
- **`ls -l module2`** again — the file now shows up as `assignment_backup.txt`, with the same timestamp, so it really is the same file just under a new name.
- **`rm module1/assignment.txt`** — deleted the original from `module1`.
- **`ls -l module1`** — `total 0` and nothing listed, so it's empty now.
- **`ls -l module2`** — `assignment_backup.txt` still there, untouched.

So the end state is exactly what it should be: `module1` empty, `module2` holding just `assignment_backup.txt`.

## Little things I noticed

- `rm` has no undo. There's no recycle bin in the terminal — once it's gone, it's gone. Fine on an empty test file, but it's a habit worth being careful about early, especially once you're working as a user with more permissions.
- `mv` doing double duty (move *and* rename) confused me a bit at first, but it makes sense: renaming is really just "move this to a new name."
- The timestamp on the backup file matched the timestamp on the copy — `mv` doesn't change the modified time, it just changes the name.
- I ran a couple of extra `ls` and `pwd` checks that weren't strictly part of the task. That ended up being a good habit though — verifying after each step instead of assuming it worked.

## What I took away from this

| Command | What it does |
|---|---|
| `touch` | Creates an empty file (or updates the timestamp on an existing one) |
| `cp` | Copies a file — original stays where it is |
| `mv` | Moves a file, or renames it if the destination is in the same folder |
| `rm` | Deletes a file permanently, no undo |
| `ls -l` | Lists contents with details, handy for verifying each step |

## Wrapping up

Small assignment, but these four commands cover most of what day-to-day file handling in Linux looks like. The main habit I'm taking from it is checking with `ls -l` after each operation instead of trusting that it worked.
