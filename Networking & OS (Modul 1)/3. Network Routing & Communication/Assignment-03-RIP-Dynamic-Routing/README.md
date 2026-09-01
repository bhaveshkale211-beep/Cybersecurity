# Assignment 03 — Explore RIP Routing Protocol Practically

## 🎯 Objective

Configure RIP in Cisco Packet Tracer, verify dynamic routing using CLI commands, and observe its routing behavior, scalability, and convergence.

> 📌 **Scope note:** The original assignment brief also asked to demonstrate BGP for comparison. Only RIP was practically configured and verified with screenshots/CLI output — this README documents that practical work only. BGP is a theoretical topic Sunny will demonstrate practically in a separate future assignment.

## 🛠️ Tools & Setup

| Tool | Devices |
|---|---|
| Cisco Packet Tracer | 2 Routers (Cisco 2901), 1 PC on each side |

## 🗺️ Topology

Two Cisco 2901 routers connected directly to each other, with one PC connected to each router. **RIP Version 2** was configured to exchange routes dynamically between the two routers.

## ⚙️ Configuration & Verification Steps

1. Connected the two routers and their respective PCs, and configured IP addressing across the topology.
2. Enabled **RIP Version 2** on both routers so they would exchange routing information automatically, without manual static routes.
3. Verified the RIP configuration using `show ip protocols` — confirming RIP was active, sending updates every 30 seconds, and using version 2 send/receive on both interfaces.
4. Verified learned routes using `show ip rip database` — confirming the router had dynamically learned the remote `192.168.3.0/24` network via its RIP neighbor.
5. Tested end-to-end connectivity from PC0 using `ping` and `tracert` to a device on the far side of the topology.

## 📸 Screenshots and Output Explanation

**Figure 1 — RIP Topology**
![RIP topology](./screenshots/01-rip-topology.png)
The two-router topology used for this demonstration — Router0 and Router1 connected directly, with one PC on each side.

**Figure 2 — RIP CLI Verification**
![RIP CLI verification](./screenshots/02-rip-cli-verification.png)
Output of `show ip protocols` and `show ip rip database` on Router0 — confirming RIP v2 is active and that the remote `192.168.3.0/24` network was learned dynamically via RIP (not statically configured), with a hop-count metric of `[1]`.

**Figure 3 — Successful Ping and Traceroute**
![Ping and traceroute](./screenshots/03-ping-traceroute.png)
`ping` and `tracert` from PC0 to `192.168.3.2` — the initial ping shows one timeout (typical first-packet ARP delay) followed by successful replies with 0% loss on the retry. The `tracert` output confirms the path crosses **three hops** (`192.168.1.1 → 192.168.2.2 → 192.168.3.2`), verifying multi-hop connectivity across the RIP-routed network.

## 🔑 Observations

- RIP v2 exchanged routes automatically between routers, with no manual static routing required.
- `show ip protocols` and `show ip rip database` are the key commands for confirming RIP is running and which routes it has learned.
- Ping and traceroute confirmed successful communication across the routed network, including the expected first-packet delay from ARP resolution.

## 🔑 Key Takeaways

- How to enable and verify **RIP v2** as a dynamic routing protocol in Cisco IOS
- The difference between a route being "directly connected" vs. learned dynamically via RIP (visible in the RIP database output)
- RIP's simplicity makes it easy to configure for small networks, but it relies on hop count as its only metric — a limitation compared to more scalable protocols
- Using `tracert` to visually confirm the actual path packets take hop-by-hop across a network, not just whether the destination is reachable

## ✅ Conclusion

The RIP practical successfully demonstrated automatic route exchange and end-to-end communication across a multi-hop routed network. RIP proved simple to configure and reliable for this small topology, consistent with its real-world use in small LAN environments.
