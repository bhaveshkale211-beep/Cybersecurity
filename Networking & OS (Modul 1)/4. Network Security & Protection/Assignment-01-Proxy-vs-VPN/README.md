# Assignment 01 — Proxy Server vs VPN in Cybersecurity

## 🎯 Objective

Analyze and demonstrate the functional and structural differences between Proxy Servers and Virtual Private Networks (VPNs) — their implementation for security, privacy, encryption, and organizational remote access — using practical network configurations and real-world scenarios.

## 🛠️ Tools & Setup

- Windows built-in Proxy settings
- Command Prompt (`ipconfig`, `netstat`)
- Network Connections control panel
- Proton VPN (Windows Tunnel adapter — "ProTUN")

## 🌐 Browser & System Proxy Configuration (Layer 7 Proxy Proof)

Unlike VPNs, a Proxy Server typically operates at the **Application Layer (Layer 7)**. It requires application-specific or system-wide manual configuration to redirect HTTP/SOCKS traffic.

![Proxy server configuration](./screenshots/01-proxy-server-configuration.png)
*Windows proxy settings — manually configuring a proxy IP address and port to route traffic locally.*

This configuration effectively delegates web request handling to the specified proxy server — useful for content filtering, caching, or web application shielding, without encrypting the entire machine's underlying network stack.

## 🔌 Active IP & Network Adapter Verification (Layer 3 Baseline)

To verify the network configuration before and after establishing a secure tunnel, network interfaces were inspected via the command line. A VPN operates at the **Network Layer (Layer 3)** and creates a virtual adapter to route traffic securely.

![ipconfig showing ProTUN adapter](./screenshots/02-ipconfig-vpn-adapter.png)
*`ipconfig` output showing the ProTUN adapter initialized with IP `10.2.0.2`, alongside the regular Wi-Fi and Ethernet adapters.*

The output shows the ProTUN adapter successfully initialized, indicating the system is ready to encapsulate and encrypt all outbound OS traffic through the VPN gateway.

## 🔐 Encrypted VPN Tunnel Connection State

A VPN establishes a secure, encrypted tunnel to a remote server. The active connection state and adapter status can be verified through the Network Connections control panel.

![VPN connection state](./screenshots/03-vpn-connection-state.png)
*Network Connections panel — the ProTUN adapter shows "Connected to 146.70.246.98@2" and is identified as the "Proton VPN Windows Tunnel," alongside Wi-Fi, Ethernet, and Bluetooth adapters.*

The active "Connected" status of the ProTUN interface confirms an encrypted tunnel is established. In this state, local ISPs can only observe encrypted ciphertext, preserving the anonymity and privacy of user payloads.

## 📡 Packet Inspection and Traffic Verification

To confirm traffic is securely routed and to analyze active connection endpoints, network statistics were captured during an active browsing session.

![netstat active connections](./screenshots/04-netstat-active-connections.png)
*`netstat -ano` output — multiple `ESTABLISHED` TCP connections shown originating from local address `10.2.0.2` (the VPN tunnel's IP, matching Screenshot 2) rather than the machine's real Wi-Fi/Ethernet address.*

The command output displays the local address `10.2.0.2` establishing multiple secure TCP connections, verifying that data transmission successfully bypasses the default unencrypted gateway and flows exclusively over the secured VPN tunnel.

## 🔑 Key Takeaways

- **Proxy = Application Layer (L7):** redirects traffic for specific apps/protocols (HTTP/SOCKS), requires manual per-app or system-wide config, doesn't encrypt the whole OS network stack.
- **VPN = Network Layer (L3):** creates a virtual network adapter and encrypts *all* outbound OS traffic, not just browser traffic — visible directly in `ipconfig` as a distinct virtual interface.
- `netstat` is a practical way to *prove* a VPN is active — connections show the tunnel's internal IP as the local address, not the machine's real network IP.
- **Real-world roles are complementary, not competing:**
  - VPNs → secure remote workforce access to internal enterprise networks (e.g., SMB file shares, SQL databases off-site)
  - Proxy Servers → web content filtering, enterprise traffic monitoring (Forward Proxies), and load-balancing (Reverse Proxies)

## ✅ Conclusion

VPNs and Proxy Servers serve different but complementary cybersecurity purposes. VPNs provide comprehensive OS-level encryption essential for secure remote access, while Proxy Servers provide application-level gateway control effective for content filtering and traffic management. Implementing both technologies concurrently is a foundational strategy for defense-in-depth and Zero Trust network architecture.
