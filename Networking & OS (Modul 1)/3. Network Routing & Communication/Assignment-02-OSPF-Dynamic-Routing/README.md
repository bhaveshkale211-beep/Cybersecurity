# Assignment 02 — Configure OSPF for Dynamic Routing

## 🎯 Objective

Design a multi-router network topology in Cisco Packet Tracer, assign proper IP addressing, and configure Open Shortest Path First (OSPF) to enable dynamic routing. The implementation is verified by inspecting routing tables, confirming OSPF neighbor adjacencies, and testing end-to-end communication across the network.

## 🛠️ Tools & Setup

| Tool | Devices |
|---|---|
| Cisco Packet Tracer | 3 Routers (2911), 3 Switches (2960), PCs/Laptop/Printer as end devices |

## 🗺️ Network Topology & IP Addressing Scheme

A **3-Router, 3-LAN topology** was implemented to demonstrate multi-hop routing capabilities — Router0 (Left) and Router3 (Right) each connect to Router2 (Middle), which sits between them as the central hop.

| Device / Network | Interface | IP Address | Subnet Mask |
|---|---|---|---|
| Router0 (Left) | Gig0/0 (LAN) | 192.168.10.1 | 255.255.255.0 |
| Router0 (Left) | Gig0/1 (WAN) | 10.1.1.1 | 255.255.255.0 |
| Router2 (Middle) | Gig0/0 (LAN) | 192.168.20.1 | 255.255.255.0 |
| Router2 (Middle) | Gig0/1 (WAN) | 10.1.1.2 | 255.255.255.0 |
| Router2 (Middle) | Gig0/2 (WAN) | 10.2.2.1 | 255.255.255.0 |
| Router3 (Right) | Gig0/0 (LAN) | 192.168.30.1 | 255.255.255.0 |
| Router3 (Right) | Gig0/1 (WAN) | 10.2.2.2 | 255.255.255.0 |

The initial physical topology was constructed by connecting the routers, switches, and end devices using the appropriate straight-through and cross-over cables.

## ⚙️ Configuration Steps (Interface & OSPF)

1. **Interface activation** — Interfaces on all three routers were configured with their respective IP addresses and activated using the `no shutdown` command. This established active physical link states, indicated by green connection lights across the network.
2. **OSPF configuration** — OSPF Process ID 1 and Area 0 (**Single Area OSPF**) were configured globally on each router. Every router was configured to advertise its directly connected networks using wildcard masks (`0.0.0.255` for /24 networks), allowing devices to dynamically exchange routing information.

## ✅ Verification & Testing

**A. OSPF Neighbor Adjacency**
To verify that routers successfully exchanged Hello packets and formed neighbor relationships, `show ip ospf neighbor` was executed on the central router (Router2). The output confirms a **FULL state adjacency** with both Router0 and Router3.

**B. Routing Table Population**
To verify dynamic route learning was successful, `show ip route` was executed on Router0. The routing table displays routes marked with an `O` (OSPF), confirming the remote `192.168.20.0/24` and `192.168.30.0/24` networks were successfully learned via OSPF — not manually configured.

**C. End-to-End Communication**
A final connectivity test was conducted using ICMP echo requests (`ping`) from a device on the far-left network (PC0) to a device on the far-right network (PC3). After an initial ARP request timeout, continuous communication was established with a **0% packet loss rate**, confirming fully functional dynamic routing across the full 3-router path.

## 📸 Screenshots and Output Explanation

**Screenshot 1 — Network Topology**
![Network topology](./screenshots/01-network-topology.png)
The initial 3-router, 3-LAN topology — Router0 and Router3 connected through central Router2, with switches and end devices on each LAN.

**Screenshot 2 — Interfaces Activated**
![Interfaces activated](./screenshots/02-interfaces-activated.png)
All physical links show green connection lights, confirming every interface was correctly IP-addressed and brought up with `no shutdown`.

**Screenshot 3 — OSPF Neighbor Adjacency**
![OSPF neighbor adjacency](./screenshots/03-ospf-neighbor-adjacency.png)
Output of `show ip ospf neighbor` on Router2, showing FULL state adjacency with both Router0 (`192.168.10.1`) and Router3 (`192.168.30.1`) — confirming OSPF Hello packets were exchanged successfully.

**Screenshot 4 — Routing Table Population**
![Routing table population](./screenshots/04-routing-table-population.png)
Output of `show ip route` on Router0. Routes marked `O` show `192.168.20.0/24` and `192.168.30.0/24` were learned dynamically via OSPF, not entered as static routes.

**Screenshot 5 — End-to-End Ping Test**
![End-to-end ping test](./screenshots/05-end-to-end-ping-test.png)
Ping from PC0 (`192.168.10.x`) to PC3 (`192.168.30.2`) — after an initial timeout, replies succeed with 0% packet loss, proving full end-to-end connectivity across the OSPF-routed network.

## 🔑 Key Takeaways

- How to configure **Single Area OSPF (Area 0)** across multiple routers using process IDs and wildcard masks
- The difference between statically configured routes and dynamically learned OSPF routes (`O` flag in the routing table)
- How to verify OSPF neighbor relationships using `show ip ospf neighbor` and interpret **FULL** adjacency state
- Why a central "hub" router (Router2) can bridge two separate networks without needing full-mesh connections between every router

## ✅ Conclusion

The implementation of Single Area OSPF across a multi-router topology was successful. The configuration allowed all routers to dynamically build their routing tables, resulting in full end-to-end communication across disparate, remote networks — without the need for manual static route entries.
