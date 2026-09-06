# Assignment 01 — Explore Windows OS Core Functions and System Operations

## 🎯 Objective

Explore the core functions of Microsoft Windows by navigating system directories, managing files, monitoring system resources, and using built-in Windows utilities.

## 🛠️ Tools & Setup

- File Explorer
- Command Prompt (`ipconfig`, `systeminfo`)
- Task Manager (Performance tab)

## 📂 Windows System Directory Exploration

Navigated to `C:\Windows\System32` in File Explorer to observe important system files used by Windows.

![System32 directory](./screenshots/01-system32-directory.png)
*`C:\Windows\System32` — 4,725 items, containing core OS binaries, DLLs, and localized resource folders.*

**Findings:** `System32` is the central repository for critical Windows system files, drivers, and executables that the OS depends on to function — a folder users are generally warned not to modify directly.

## 🗂️ File Management

Created a new folder, added a text file inside it, and renamed the file to `MyNotes.txt` to practice basic file management operations.

![File management](./screenshots/02-file-management-mynotes.png)
*The renamed `MyNotes.txt` file inside a new folder, shown with its file details (Text Document, 0 bytes, creation date/time, and full file path).*

**Findings:** Demonstrates the basic file lifecycle in Windows — create, rename, and inspect file properties (type, size, location, modified date) via File Explorer's Details pane.

## 🖥️ System Monitoring and Commands

Used Command Prompt to run `ipconfig` and `systeminfo`, and opened Task Manager's Performance tab to monitor live CPU and memory usage.

**`ipconfig` — Network Configuration**
![ipconfig output](./screenshots/03-ipconfig-output.png)
*Lists all network adapters and their IP configuration — including active Wi-Fi (`192.168.1.14`) and Ethernet adapters, plus several disconnected wireless adapters.*

**`systeminfo` — Full System Details**
![systeminfo output](./screenshots/04-systeminfo-output.png)
*Full OS and hardware report — OS version/build, manufacturer, install date, boot time, system model, processor, memory (total/available/virtual), installed hotfixes, and all network cards with their IPs.*

**Task Manager — Performance Tab**
![Task Manager Performance tab](./screenshots/05-task-manager-performance.png)
*Live CPU utilization graph (Intel Core i5-10300H, 4% usage, 2.83 GHz), alongside Memory, Disk, network adapters, and both integrated and dedicated GPUs.*

**Findings:** These three tools give complementary views of the same machine — `ipconfig` for network-layer configuration, `systeminfo` for a full static snapshot of OS/hardware details, and Task Manager for real-time resource usage.

## 🧩 Important Windows System Files

| File | Role |
|---|---|
| `explorer.exe` | File Explorer |
| `cmd.exe` | Command Prompt |
| `taskmgr.exe` | Task Manager |
| `svchost.exe` | Hosts and runs Windows services |

## 🔑 Key Takeaways

- `System32` holds the core executables and DLLs Windows depends on — a common target for malware to disguise itself in, since legitimate system processes also live there.
- `ipconfig` vs `systeminfo`: `ipconfig` is network-focused and quick; `systeminfo` is a full static system report covering OS, hardware, memory, and security features in one command.
- Task Manager's Performance tab gives real-time (not static) resource usage — useful for spotting abnormal CPU/memory/network spikes that could indicate a running process worth investigating.
- Recognizing core system processes (`explorer.exe`, `cmd.exe`, `taskmgr.exe`, `svchost.exe`) by name is a foundational skill for later spotting *fake* or malicious processes impersonating them.

## ✅ Conclusion

This practical assignment successfully explored core Windows OS functions — navigating critical system directories, performing basic file management, and using built-in utilities (`ipconfig`, `systeminfo`, Task Manager) to inspect network configuration, system specifications, and live resource usage.
