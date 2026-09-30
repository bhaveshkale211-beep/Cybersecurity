# Assignment 03 — File Permissions and Ownership

This one moves from just handling files to actually controlling who can touch them — the whole point of Linux permissions. Made a file, checked its default permissions, then locked it down so only I could read or write it.

## What I was trying to do

Create a file meant to hold "sensitive" info, check what permissions it gets by default, then restrict it so only the owner has access — nobody else on the system can read or touch it.

## What I actually ran

Still inside `~/Training`:

```
pwd
touch confidential.txt
ls -l confidential.txt
chmod 600 confidential.txt
ls -l confidential.txt
```

![Terminal — checking and changing permissions with chmod](./screenshots/01-chmod-file-permissions.png)

- **`pwd`** — just confirming I was in `/home/kali/Training` before starting.
- **`touch confidential.txt`** — created the file.
- **`ls -l confidential.txt`** (first check) — showed `-rw-rw-r--`. That's the default: owner can read/write, group can read/write, everyone else can only read. Not great for something meant to be private.
- **`chmod 600 confidential.txt`** — changed the permissions.
- **`ls -l confidential.txt`** (second check) — now shows `-rw-------`. Owner still has read/write, but group and others have nothing at all.

## Making sense of the permission string

The output looks cryptic at first (`-rw-------`), but it breaks down into clear chunks:

| Position | Who it's for | Before (`rw-rw-r--`) | After (`rw-------`) |
|---|---|---|---|
| 1st char | File type (`-` = regular file) | `-` | `-` |
| Chars 2–4 | Owner | `rw-` (read, write) | `rw-` (read, write) |
| Chars 5–7 | Group | `rw-` (read, write) | `---` (nothing) |
| Chars 8–10 | Others | `r--` (read only) | `---` (nothing) |

## How `chmod 600` actually maps to that

The numeric form is just each permission set (owner/group/others) written as a single digit, where read = 4, write = 2, execute = 1, added together:

- **6** = 4 (read) + 2 (write) → owner gets read + write
- **0** = nothing → group gets nothing
- **0** = nothing → others get nothing

So `600` is really just shorthand for "owner: read+write, everyone else: nothing" — once you know the read/write/execute = 4/2/1 pattern, the three-digit numbers stop looking random.

## Why this actually matters

Every file in Linux has an owner and a group attached to it, and the permission bits decide what each of those (plus everyone else) can do. That default `rw-rw-r--` might be totally fine for a normal file you don't mind others reading — but for something like a config file with credentials in it, or notes containing anything sensitive, leaving group/others with read access means any other user account on that machine could open it. `chmod 600` is the standard way to shut that down completely.

## What I took away from this

- The default permissions a new file gets aren't automatically "safe" — group and others can often still read it unless you explicitly restrict it.
- `chmod 600` is the go-to permission for a private file: owner read/write, nobody else gets anything.
- The numeric permission system (4/2/1 for read/write/execute) is worth actually learning rather than memorizing common combos like `600` or `644` — once the math clicks, any three-digit permission becomes readable at a glance.
- `ls -l` isn't just for confirming a file exists — the permission string itself is genuinely useful security information every time you look at it.

## Wrapping up

Short assignment, but this is one of those things that matters a lot more in practice than it looks on paper — permission mistakes (files left too open) are a real, common way sensitive data ends up exposed on a system.
