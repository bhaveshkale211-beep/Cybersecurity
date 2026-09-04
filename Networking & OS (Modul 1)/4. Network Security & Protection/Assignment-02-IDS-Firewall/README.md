# Assignment 02 — IDS and Firewall Security Analysis

## 🎯 Objective

Study and analyze core network security controls — specifically Firewalls and Intrusion Detection Systems (IDS) — in a simulated Security Operations Center (SOC) environment. This practical report demonstrates how these technologies monitor, filter, and detect unauthorized or suspicious traffic to protect network infrastructure.

> 📌 **Scope note:** The original report title also references IPS, but only Firewall and IDS (Snort) were practically demonstrated with screenshots/output — this README documents that practical work only.

## 🛠️ Tools & Setup

- Windows Defender Firewall with Advanced Security
- Snort IDS (command-line, Windows build)

## 🧱 Firewall Security Analysis

To understand perimeter defense, the Windows Defender Firewall with Advanced Security interface was examined — the gatekeeper for network traffic. Firewalls operate at **Layers 3 and 4** of the OSI model, using predefined security rules (Access Control Lists) to allow or block inbound and outbound connections.

![Windows Firewall dashboard](./screenshots/01-windows-firewall-dashboard.png)
*Windows Defender Firewall dashboard — Domain, Private, and Public profiles all active, with inbound connections that don't match a rule blocked by default and outbound connections allowed by default.*

**Findings:** The firewall dashboard confirms that inbound connections without matching rules are blocked across all three network profiles. This ensures unauthorized external entities cannot establish unauthorized access to local ports or services.

## 🕵️ Intrusion Detection System (IDS) — Snort Implementation

Unlike firewalls that actively block traffic, an Intrusion Detection System acts as a **passive watchdog**. Snort IDS was deployed and executed via the command prompt to monitor network packet flows and inspect traffic headers.

![Snort IDS packet capture](./screenshots/02-snort-ids-packet-capture.png)
*Snort initializing on Windows — listing all available network interfaces (including the same Proton VPN "ProTUN" adapter seen in Assignment 1), then binding to the active interface and entering packet dump mode.*

**Findings:** The terminal output shows Snort initializing output plugins, successfully binding to the active network interface adapter, and running in packet dump mode. This proves the IDS is operational — tracking live network traffic and ready to trigger alerts upon encountering suspicious signatures.

## ⚖️ Comparative Role in a SOC Environment

In a real-world SOC setup, Firewalls and IDS complement each other rather than duplicate each other's job:

| Control | Role | Behavior |
|---|---|---|
| **Firewall** | Perimeter enforcement | Actively blocks unauthorized ports and filters direct malicious connection requests at the entry point |
| **IDS** | Threat visibility | Passively logs anomalies, packet behaviors, and attack signatures without disrupting live performance |

## 🔑 Key Takeaways

- Firewalls operate at **Layer 3/4** and make active allow/block decisions based on rule sets (ACLs) — they are a *preventive* control.
- IDS tools like Snort are **passive** — they observe and alert but don't block traffic themselves, making them a *detective* control.
- A real SOC environment layers both: the firewall stops known-bad connections at the door, while the IDS watches everything that gets through for suspicious patterns the firewall's static rules wouldn't catch.
- Snort must bind to a specific network interface to capture traffic — on a multi-adapter system (Wi-Fi, Ethernet, VPN tunnel, virtual adapters), choosing the *correct* interface matters for what traffic actually gets inspected.

## ✅ Conclusion

This practical assignment successfully demonstrated the implementation and role of network security controls. By examining firewall rules and running the Snort IDS, hands-on understanding was gained of how organizations protect networks against unauthorized access, malware propagation, and suspicious traffic — using prevention (firewall) and detection (IDS) as complementary layers of defense.
