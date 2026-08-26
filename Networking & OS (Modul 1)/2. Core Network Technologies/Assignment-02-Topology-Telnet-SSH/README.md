# Assignment 02 — Network Topology, Telnet & SSH Remote Access Configuration

## 🎯 Objective

Design and build a routed network topology in Cisco Packet Tracer using 2 routers, 2 switches, and 4 PCs, then configure and test two remote access methods:

- **Telnet** remote access, using username and password authentication
- **SSH** remote access, using username and password authentication with RSA key generation

Connectivity between the two networks was verified using `ping`, and remote logins were verified from PCs using the `telnet` and `ssh` commands.

## 🛠️ Tools & Setup

| Tool | Devices | OS |
|---|---|---|
| Cisco Packet Tracer | 2 Routers (1941), 2 Switches (2960), 4 PCs | Windows |

## 🗺️ Network Topology

Two LANs, each connected to its own router, with the two routers linked over a point-to-point WAN connection:

- **LAN A:** PC0, PC1 → Switch0 → Router0 (R1)
- **LAN B:** PC2, PC3 → Switch1 → Router1 (R2)
- **Router0 ↔ Router1** connected over WAN

Router0 (R1) was configured for **Telnet** access, and Router1 (R2) was configured for **SSH** access. Remote logins were tested from the PC on the *opposite* LAN in each case, so login traffic had to cross the routed WAN link — proving both remote access and inter-network routing were working correctly.

## 📋 IP Addressing Plan

| Segment | Network | Device | Interface | IP Address | Subnet Mask |
|---|---|---|---|---|---|
| LAN A | 192.168.10.0/24 | Router0 (R1) | GigabitEthernet0/0 | 192.168.10.1 | 255.255.255.0 |
| LAN A | 192.168.10.0/24 | PC0 | NIC | 192.168.10.10 | 255.255.255.0 |
| LAN A | 192.168.10.0/24 | PC1 | NIC | 192.168.10.11 | 255.255.255.0 |
| WAN | 192.168.100.0/30 | Router0 (R1) | GigabitEthernet0/1 | 192.168.100.1 | 255.255.255.252 |
| WAN | 192.168.100.0/30 | Router1 (R2) | GigabitEthernet0/1 | 192.168.100.2 | 255.255.255.252 |
| LAN B | 192.168.20.0/24 | Router1 (R2) | GigabitEthernet0/0 | 192.168.20.1 | 255.255.255.0 |
| LAN B | 192.168.20.0/24 | PC2 | NIC | 192.168.20.10 | 255.255.255.0 |
| LAN B | 192.168.20.0/24 | PC3 | NIC | 192.168.20.11 | 255.255.255.0 |

## ⚙️ Implementation Steps

**Step 1 — Topology and cabling**
Placed 2 routers, 2 switches, and 4 PCs in Packet Tracer and cabled them per the topology above, confirming all links showed a green (up) status.

**Step 2 — IP addressing and routing**
```
! On Router0 (R1)
ip route 192.168.20.0 255.255.255.0 192.168.100.2

! On Router1 (R2)
ip route 192.168.10.0 255.255.255.0 192.168.100.1
```

**Step 3(a) — Telnet configuration on Router0 (R1)**
```
hostname R1
enable secret class123
username admin privilege 15 secret Admin@123
line vty 0 4
 login local
 transport input telnet
```
Tested from a PC on the opposite LAN using: `telnet 192.168.10.1`, logging in with the admin account.

**Step 3(b) — SSH configuration on Router1 (R2)**
```
hostname R2
ip domain-name sunnylab.local
crypto key generate rsa   (1024 bits)
username admin privilege 15 secret Admin@123
ip ssh version 2
line vty 0 4
 login local
 transport input ssh
```
Tested from PC0 using: `ssh -l admin 192.168.20.1`, logging in with the admin account.

## 📸 Screenshots and Output Explanation

**Screenshot 1 — Network Topology**
![Network topology](./screenshots/01-network-topology.png)
Shows the complete topology with all devices connected and links up.

**Screenshot 2 — IP Configuration and Connectivity**
![Router0 Telnet config & IP interface brief](./screenshots/02a-router0-telnet-config-ip.png)
![Router1 SSH config & IP interface brief](./screenshots/02b-router1-ssh-config-ip.png)
Shows `show ip interface brief` output on both routers, confirming interfaces are correctly addressed and up, alongside the Telnet/SSH configuration commands as applied.

**Screenshot 3 — Telnet Practical**
![Telnet session](./screenshots/03-telnet-practical.png)
Shows the Telnet session to Router0, including username/password login (with a few invalid-login attempts first) and the resulting privileged router prompt.

**Screenshot 4 — SSH Practical**
![SSH session](./screenshots/04-ssh-practical.png)
Shows the SSH session from PC0 to Router1, including successful pings across the network followed by username/password login and the resulting privileged router prompt.

**Screenshot 5 — Successful Remote Login and Verification**
![Remote login verification](./screenshots/05-remote-login-verification.png)
Shows a final ping test confirming end-to-end connectivity across the routed network, alongside the remote access session.

## 🔑 Key Observations

- **Telnet transmits the username and password in plain text**, making it unsuitable for use over untrusted networks.
- **SSH encrypts the session using an RSA key pair**, which requires a hostname and domain name to be configured before the key can be generated.
- A router hostname must be changed from the default `"Router"` before `crypto key generate rsa` will run, since the key identity is derived from hostname + domain name.
- **Static routes were required on both routers** because each router only knows about its own directly connected networks by default.
- Testing remote access from the *opposite* LAN (rather than the same LAN as the router) verifies both the remote-access configuration and the inter-network routing at the same time.

## ✅ Conclusion

The topology was successfully built with two routers, two switches, and four PCs, with full IP connectivity established between both LANs. Telnet was configured and verified on Router0, and SSH was configured and verified on Router1, both using username and password authentication. All screenshots confirm that remote access and routing worked as required, and the assignment requirements are fully satisfied.
