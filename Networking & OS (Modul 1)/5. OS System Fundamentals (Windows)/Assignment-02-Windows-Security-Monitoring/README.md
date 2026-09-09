# Assignment 02 — Windows Security Monitoring and Advanced System Management

## 🎯 Objective

Explore Windows security monitoring and advanced system management using built-in administrative tools. The practical focuses on monitoring security events, managing system services, scheduled tasks, and analyzing system resource usage.

> 📌 **Scope note:** The assignment brief mentions Task Scheduler, but only the Services (`services.msc`) view was captured with a screenshot — this README documents that practical work only.

## 🛠️ Tools & Setup

- Event Viewer
- Windows Security (Virus & Threat Protection)
- Services (`services.msc`)
- Resource Monitor

## 📋 Event Viewer

Opened Event Viewer and navigated to **Windows Logs → System**, filtering by **Critical** level events to identify serious system problems.

![Event Viewer critical events](./screenshots/01-event-viewer-critical-events.png)
*System log filtered to Critical events — repeated Event ID 41 ("Kernel-Power": the system rebooted without cleanly shutting down first) alongside one WinREAgent event, out of 32,430 total logged events.*

**Findings:** The repeated **Kernel-Power Event ID 41** entries indicate the system experienced multiple unclean shutdowns — meaning it stopped responding, crashed, or lost power unexpectedly on several dates. This is exactly the kind of pattern Event Viewer is built to surface: a single Critical event might be a one-off, but a *recurring* Critical event points to a real underlying issue (hardware, power, or driver-related) worth investigating.

## 🛡️ Windows Defender

Opened Windows Security and checked the **Virus & Threat Protection** section, which provides real-time protection against malware and other security threats.

![Windows Defender scan status](./screenshots/02-windows-defender-scan.png)
*Virus & Threat Protection dashboard — last quick scan found 0 threats across 14,244 files scanned in 58 seconds, with security intelligence (definitions) confirmed up to date.*

**Findings:** A clean scan result combined with up-to-date security intelligence confirms Windows Defender's real-time protection is both active and current — the two things that matter most for baseline endpoint protection on a Windows machine.

## ⚙️ Services

Opened `services.msc` to observe the full list of Windows background services, their current status, startup type, and the account they run under.

![Services (services.msc)](./screenshots/03-services-msc.png)
*Services console — showing a mix of `Running`, `Automatic`, and `Manual` services (system services like BitLocker, Base Filtering Engine, and Bluetooth support, alongside third-party services like AnyDesk, Brave Update Service, and ASUS utilities), each tagged with its Log On As account (mostly Local System / Local Service).*

**Findings:** The Services console is a key place to spot unexpected entries — a service with a suspicious name, an unfamiliar publisher, or one set to "Automatic" that shouldn't be running at startup can be an early indicator of unwanted or malicious software persisting on a system.

## 📊 Resource Monitor

Opened Resource Monitor from Task Manager to observe detailed CPU, Memory, Disk, and Network usage beyond what Task Manager's basic view shows.

![Resource Monitor overview](./screenshots/04-resource-monitor.png)
*Resource Monitor's Overview tab — 6% CPU usage, 1 MB/sec disk I/O (3% highest active time), 91 Kbps network I/O (0% utilization), and 80% physical memory used, with live per-process breakdowns and graphs for each resource.*

**Findings:** Resource Monitor gives a more granular, per-process view than Task Manager — useful for pinpointing exactly *which* process is responsible for a spike in CPU, disk, network, or memory usage, rather than just seeing the aggregate number.

## 🔑 Key Takeaways

- **Event Viewer's Critical filter** turns a noisy 32,000+ event log into a short, actionable list — recurring Critical events (like repeated Kernel-Power Event 41) reveal patterns a single glance wouldn't catch.
- Windows Defender's health depends on two things together: a **clean scan result** and **up-to-date definitions** — either one alone doesn't guarantee protection.
- The **Services console** is a practical place to audit what's running persistently on a machine, including third-party software that installs its own background services (seen here: AnyDesk, Brave, ASUS tools).
- **Resource Monitor vs Task Manager:** Resource Monitor trades Task Manager's simplicity for deeper per-process, per-resource detail — useful once you already suspect *something* is consuming resources and need to find exactly what.

## ✅ Conclusion

This practical assignment explored Windows security monitoring and system management using built-in administrative tools. Event Viewer surfaced a real recurring issue (unclean shutdowns), Windows Defender confirmed active and current malware protection, the Services console provided visibility into background processes, and Resource Monitor offered a detailed breakdown of live system resource usage — together giving a well-rounded picture of the system's health and security posture.
