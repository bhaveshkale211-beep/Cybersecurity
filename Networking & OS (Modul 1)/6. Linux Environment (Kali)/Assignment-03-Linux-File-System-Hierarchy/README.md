# Assignment 03 — Linux File System Hierarchy in Kali Linux

This one was about actually walking through Kali's folder structure instead of just reading a diagram of it — going into a few key directories myself and seeing what's actually there.

## What I was trying to do

Explore the Linux filesystem hierarchy, move through the important directories (`/home`, `/etc`, `/var`, `/usr`, `/tmp` and a couple others), figure out what each one is actually for, and understand why any of this matters for someone doing system admin or security work.

## Starting at the root

Everything in Linux branches off from a single directory: `/`. I moved there and listed what's inside.

```
cd /
pwd
ls
```

![Root directory — terminal listing](./screenshots/01-root-directory-terminal-listing.png)

`pwd` confirmed I was at `/`, and `ls` showed the standard set of top-level folders: `bin`, `boot`, `dev`, `etc`, `home`, `lib`, `lib32`, `lib64`, `lost+found`, `media`, `mnt`, `opt`, `proc`, `root`, `run`, `sbin`, `srv`, `swap`, `sys`, `tmp`, `usr`, `var` — plus a few boot-related files (`initrd.img`, `vmlinuz`, and their `.old` versions).

I also pulled up the same root directory in the **Thunar** file manager (the GUI side) just to see it laid out visually instead of as plain text:

![Root directory — file manager view](./screenshots/02-root-directory-file-manager-view.png)

Same folders, just easier to scan visually — 21 folders, 5 files, 1.3 GiB used, 58.8 GiB free on that disk.

## Moving through the important folders

Instead of jumping straight to each folder from `/`, I actually navigated relative to wherever I already was — using `cd ..` to go back up and then into the next folder. Here's the actual path I took:

```
cd /              →  pwd: /
ls                →  (full root listing)
cd home           →  pwd: /home
cd ../etc         →  pwd: /etc
cd ../bin         →  pwd: /bin
cd ../tmp         →  pwd: /tmp
cd ../var         →  pwd: /var
ls                →  backups, cache, lib, local, lock, log, mail, opt, run, spool, tmp, www
```

![Terminal navigation through directories](./screenshots/03-terminal-directory-navigation.png)

So the actual route was `/ → /home → /etc → /bin → /tmp → /var`. I ended up in `/bin` along the way too, even though it wasn't one of the folders I originally set out to check — and I didn't get to `/usr` in this particular run. Worth being upfront about since it's easy to just write "checked all five folders" when in reality the terminal history shows exactly what happened.

## What each directory is actually for

| Directory | What it's for |
|---|---|
| `/` | The root — top of the entire filesystem, everything else branches from here |
| `/home` | Where regular users' personal files live |
| `/etc` | System-wide config files — settings for pretty much everything |
| `/var` | Data that changes over time — logs, caches, mail, spool files |
| `/usr` | User-space programs, libraries, shared resources (most installed software lives here) |
| `/tmp` | Temporary files, usually cleared on reboot |
| `/root` | Home directory for the root (admin) user — separate from `/home` |
| `/boot` | Files needed to actually boot the system |
| `/dev` | Device files — how Linux represents hardware and virtual devices as files |
| `/proc` | A virtual filesystem — not real files on disk, but a live window into running processes and kernel info |
| `/opt` | Optional or third-party software that doesn't fit the standard package structure |
| `/bin` | Essential command binaries — the core programs the system needs even in a minimal environment |

## Why this actually matters for security work

This isn't just trivia — knowing where things live is genuinely useful once you're doing real admin or investigation work:

- `/etc` is where most configuration lives, so it's often the first place to check if something's been tampered with
- `/var/log` holds system and application logs — usually the first stop when investigating an incident
- `/home` is where user-specific files and activity show up
- `/tmp` gets used a lot by malware for temporary staging, since it's writable by default

Basically, if you don't know where things are *supposed* to be, you won't notice when something's *not* where it should be — and that's often how suspicious activity gets spotted.

## Takeaways

- The Linux filesystem is one single tree starting at `/`, not separate drives like `C:` and `D:` — everything, including other physical drives, gets mounted somewhere inside that same tree.
- Using `cd ..` and relative paths instead of retyping the full path each time is a small thing, but it's genuinely how people actually move around in the terminal day to day.
- `/proc` is a bit of a mind-bender at first — it looks like a normal folder but it's not backed by real files on disk, it's the kernel exposing live system state as if it were a filesystem.
- Documenting the *actual* commands run (not just what I meant to do) matters — my real path skipped `/usr` and included `/bin`, which wasn't the original plan, but that's what the terminal history actually shows.

## Wrapping up

This gave me a much more concrete sense of how Kali (and Linux generally) is organized, compared to just seeing a filesystem diagram somewhere. Actually `cd`-ing into these folders and matching them up with what I already knew they were "supposed" to do made it stick a lot better than memorizing a table would have.
