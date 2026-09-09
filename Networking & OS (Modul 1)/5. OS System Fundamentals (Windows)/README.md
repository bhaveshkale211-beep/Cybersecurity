# Topic 5 — OS System Fundamentals (Windows)

## 📖 Overview

This topic shifts focus from networking into the operating system itself — exploring how Windows organizes its core system files, how basic file management and system monitoring work, and how built-in administrative tools are used to check security posture, manage background services, and analyze live resource usage. These fundamentals are essential groundwork for later OS-level security topics (process analysis, malware behavior, system hardening).

## 🛠️ Tools Used

- File Explorer
- Command Prompt (`ipconfig`, `systeminfo`)
- Task Manager
- Event Viewer
- Windows Security (Virus & Threat Protection)
- Services (`services.msc`)
- Resource Monitor

## 📂 Assignments

### Assignment 01 — Explore Windows OS Core Functions and System Operations

Explored the core functions of Windows by navigating system directories, managing files, and monitoring system resources using built-in utilities.

- Navigated `C:\Windows\System32` — the core repository of OS binaries, DLLs, and drivers Windows depends on
- Practiced basic file management: created a folder, added a text file, renamed it to `MyNotes.txt`
- Used `ipconfig` to inspect network adapter configuration
- Used `systeminfo` for a full static system report (OS version, hardware, memory, installed hotfixes, network cards)
- Used Task Manager's Performance tab to observe live CPU, memory, disk, and GPU usage

**Key takeaway:** `ipconfig` is network-focused and quick, `systeminfo` gives a full static snapshot, and Task Manager shows real-time usage — three complementary views of the same machine.

📁 [Full assignment README](./Assignment-01-Windows-OS-Core-Functions/)

### Assignment 02 — Windows Security Monitoring and Advanced System Management

Explored Windows security monitoring and system management using built-in administrative tools — monitoring security events, managing services, and analyzing resource usage.

- Used **Event Viewer**, filtered to Critical events, and found recurring **Kernel-Power Event ID 41** entries — indicating multiple unclean shutdowns
- Checked **Windows Defender** (Virus & Threat Protection) — confirmed a clean scan (0 threats, 14,244 files) and up-to-date security intelligence
- Opened **Services** (`services.msc`) to audit running/manual background services, including third-party ones (AnyDesk, Brave Update Service, ASUS utilities)
- Used **Resource Monitor** for a granular, per-process breakdown of CPU, Memory, Disk, and Network usage

**Key takeaway:** Event Viewer's Critical filter turns a 32,000+ event log into an actionable short list, and Resource Monitor trades Task Manager's simplicity for the per-process detail needed to pinpoint *exactly* what's consuming a resource.

📁 [Full assignment README](./Assignment-02-Windows-Security-Monitoring/)

## ✅ Topic Conclusion

Together, these two assignments cover both the **basics of Windows system navigation** (directories, files, core monitoring commands) and **practical security administration** (event logs, malware protection status, service auditing, live resource analysis) — the essential OS-layer toolkit before moving into deeper OS security topics.
