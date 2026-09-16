# Assignment 01 — Kali Linux Installation Using VMware

## 🎯 Objective

Install Kali Linux using a VMware virtual machine, allocate appropriate hardware resources, verify the successful installation, and understand the advantages of virtualization for cybersecurity and penetration testing activities.

## 🛠️ Tools & Setup

- VMware Workstation
- Kali Linux ISO (`kali-linux-2026.2-vmware-amd64`)

## 💻 Virtual Machine Creation and Resource Allocation

Created a new virtual machine in VMware and selected the Kali Linux ISO image as the installation media. The VM was configured with the following resources:

| Resource | Allocation |
|---|---|
| Memory (RAM) | 4 GB |
| Processors | 4 |
| Hard Disk (SCSI) | 80.1 GB |
| Network Adapter | NAT |
| USB Controller | Present |

![VMware virtual machine configuration](./screenshots/01-vmware-vm-configuration.png)
*VMware Virtual Machine Settings — showing the Memory allocation of 4 GB against the recommended range (2 GB recommended, 6.1 GB max recommended, 1 GB guest OS minimum), alongside Processors, Hard Disk, and Network Adapter settings.*

## ⚙️ Kali Linux Installation

The virtual machine was started from the Kali Linux ISO and the **Graphical Install** option was selected. The language, location, keyboard, hostname, user account, and password were configured. Guided disk partitioning was selected for the virtual disk, the installation was completed, and the **GRUB bootloader** was installed. After installation, the virtual machine was restarted and Kali Linux was accessed through the login screen.

## ✅ Installation Verification

After logging into Kali Linux, the terminal was opened and the following commands were executed to verify the current user, hostname, and Linux system information:

```
whoami
hostname
uname --all
```

![Kali Linux login and terminal verification](./screenshots/02-kali-login-terminal-verification.png)
*Successful Kali Linux login and terminal output — `whoami` returns `kali`, `hostname` returns `kali`, and `uname --all` confirms the full kernel version: `Linux kali 6.19.14+kali-amd64 #1 SMP PREEMPT_DYNAMIC Kali 6.19.14-1+kali1 (2026-05-05) x86_64 GNU/Linux`.*

**Findings:** All three commands returned expected results, confirming the OS is correctly installed, the hostname was set as configured during setup, and the system is running the intended Kali Linux kernel build.

## 🔒 Advantages of Virtualization for Cybersecurity

Using a virtual machine provides an isolated environment for cybersecurity learning and penetration testing:

- Security tools and configurations can be tested **without directly modifying the host operating system**
- VMs can be **reset, cloned, or removed easily** — useful for controlled experiments, malware-analysis labs, and network testing
- **Multiple operating systems** can run on the same physical computer, enabling isolated test environments side by side
- Mistakes or infections inside the VM (e.g., while testing exploits or malware behavior) stay contained and don't risk the host machine

## 🔑 Key Takeaways

- How to allocate VM resources (RAM, CPU, disk, network mode) appropriately for running Kali Linux smoothly inside VMware
- The Kali Linux graphical installation flow — from ISO boot through guided partitioning to GRUB bootloader setup
- Using `whoami`, `hostname`, and `uname --all` as quick sanity checks to confirm a fresh Linux install is working correctly
- Why virtualization/isolation is foundational to safe cybersecurity practice — it's the reason penetration testing tools can be run and tested without risking the host system

## ✅ Conclusion

This practical assignment successfully demonstrated the creation and installation of Kali Linux in VMware. The allocated resources were sufficient for running the operating system, and the installation was verified through terminal commands. The practical also demonstrated why virtualization is useful for safe and controlled cybersecurity activities.
