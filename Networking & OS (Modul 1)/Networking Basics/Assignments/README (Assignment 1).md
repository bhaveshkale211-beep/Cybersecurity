# Assignment 01 — Design and Implement LAN & WAN Network

## 🎯 Objective

Design and set up two separate Local Area Networks (LAN) — a Head Office and a Branch Office — and connect them using a Wide Area Network (WAN) serial link with proper routing, so that all devices across both sites can communicate (ping each other).

## 🛠️ Tools Used

- Cisco Packet Tracer

## 🗺️ Network Topology

- **Star Topology (LAN):** Used inside both offices — all PCs connect to a single central switch. If one cable fails, only that PC drops; the rest of the office stays online.
- **Point-to-Point Topology (WAN):** Used to directly connect Router R1 and Router R2 over a single serial cable for a fast, dedicated link between branches.

## 📋 IP & MAC Addressing

**Branch Office (BO) — `192.168.1.0/24`**

| Device | Interface | IP Address | Subnet Mask | MAC Address |
|---|---|---|---|---|
| R1 Router | G0/0 | 192.168.1.1 | 255.255.255.0 | Auto |
| R1 Router | S0/0/0 | 10.0.0.1 | 255.255.255.252 | N/A |
| PC 1 | FastEthernet0 | 192.168.1.2 | 255.255.255.0 | 0006.2A8D.326C |
| PC 2 | FastEthernet0 | 192.168.1.3 | 255.255.255.0 | 0060.2FA9.152C |
| PC 3 | FastEthernet0 | 192.168.1.4 | 255.255.255.0 | 0002.4AC8.5774 |

**Head Office (HO) — `192.168.2.0/24`**

| Device | Interface | IP Address | Subnet Mask | MAC Address |
|---|---|---|---|---|
| R2 Router | G0/0 | 192.168.2.1 | 255.255.255.0 | Auto |
| R2 Router | S0/0/0 | 10.0.0.2 | 255.255.255.252 | N/A |
| PC 4 | FastEthernet0 | 192.168.2.2 | 255.255.255.0 | 00E0.F7CB.2719 |
| PC 5 | FastEthernet0 | 192.168.2.3 | 255.255.255.0 | 0090.2B31.74C6 |
| PC 6 | FastEthernet0 | 192.168.2.4 | 255.255.255.0 | 0060.70EE.71CE |

## ⚙️ Implementation Steps

1. **Built the topology** — Placed two 1941 Routers (R1, R2) and two 2960 Switches, plus six PCs. Powered off each router to insert an HWIC-2T serial module, then powered back on. Connected PCs → switches → routers with copper straight-through cables, and R1 → R2 with a Serial DCE cable.
2. **Configured the PCs** — Set static IP addresses, subnet masks, and default gateways on each PC via Desktop → IP Configuration, per the address tables above.
3. **Configured router interfaces** — Assigned IPs to GigabitEthernet0/0 (LAN gateway) and Serial0/0/0 (WAN interface) via CLI on both routers. Set clock rate `64000` on R1 (the DCE end of the serial link).
4. **Configured static routing** — Added a route on R1 to reach `192.168.2.0` via R2's serial IP (`10.0.0.2`), and a route on R2 to reach `192.168.1.0` via R1's serial IP (`10.0.0.1`).
5. **Saved and tested** — Saved configs with `copy running-config startup-config`, then verified end-to-end connectivity using `ping` from the PCs' command prompt.

## 💻 Router Configuration Commands

**Router 1 (Branch Office)**
```
Router> enable
Router# configure terminal
Router(config)# hostname R1
R1(config)# interface GigabitEthernet0/0
R1(config-if)# ip address 192.168.1.1 255.255.255.0
R1(config-if)# no shutdown
R1(config-if)# exit
R1(config)# interface Serial0/0/0
R1(config-if)# ip address 10.0.0.1 255.255.255.252
R1(config-if)# clock rate 64000
R1(config-if)# no shutdown
R1(config-if)# exit
R1(config)# ip route 192.168.2.0 255.255.255.0 10.0.0.2
R1(config)# exit
R1# copy running-config startup-config
```

**Router 2 (Head Office)**
```
Router> enable
Router# configure terminal
Router(config)# hostname R2
R2(config)# interface GigabitEthernet0/0
R2(config-if)# ip address 192.168.2.1 255.255.255.0
R2(config-if)# no shutdown
R2(config-if)# exit
R2(config)# interface Serial0/0/0
R2(config-if)# ip address 10.0.0.2 255.255.255.252
R2(config-if)# no shutdown
R2(config-if)# exit
R2(config)# ip route 192.168.1.0 255.255.255.0 10.0.0.1
R2(config)# exit
R2# copy running-config startup-config
```

## ✅ Verification & Conclusion

Connectivity was verified using `ping` inside the Packet Tracer terminal — PCs in the Branch Office successfully communicated with PCs in the Head Office. All configurations were saved on both routers, fully satisfying the assignment requirements.

## 🔑 Key Takeaways

- How LAN (star) and WAN (point-to-point) topologies serve different purposes and fault-tolerance needs
- Manually assigning and tracking IP/MAC addresses across two separate subnets
- Configuring router interfaces and static routing to connect two independent LANs over a WAN link
- Verifying end-to-end network connectivity using `ping`

> 📌 No screenshots for this assignment — the report is text/config-based only.
