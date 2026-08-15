# Assignment 01 — Packet Analysis of TCP/IP & OSI using Wireshark

## 🎯 Objective

Create a practical demonstration showing how data flows through the different layers of the OSI and TCP/IP models — identifying which devices/protocols operate at each layer, and capturing real Wireshark packets as proof of how the Application, Transport, Internet/Network, and Physical layers interact during a single web request.

## 🛠️ Tools & Setup

| Tool | Interface | OS | Target |
|---|---|---|---|
| Wireshark | Wi-Fi | Windows | `http://example.com` |

## 📋 OSI vs TCP/IP Layer Mapping

| OSI Layer | TCP/IP Layer | Device / Protocol | Role in This Capture |
|---|---|---|---|
| Application | Application | Browser, DNS, HTTP, HTTPS | Browser builds request; DNS resolves `example.com` |
| Presentation | Application | TLS | Client Hello negotiates encryption |
| Transport | Transport | TCP (OS stack) | 3-way handshake on port 443 |
| Network | Internet | Router, IPv6 stack | IPv6 source/destination addressing |
| Data Link | Network Access | NIC, Access Point | Wi-Fi (802.11) MAC framing |
| Physical | Network Access | Wi-Fi | Raw radio signal transmission |

## ⚙️ Implementation Steps

1. **Started the capture** — Opened Wireshark as Administrator and began capturing on the Wi-Fi interface.
2. **Generated traffic** — Noted the machine's local IPv4 address via `ipconfig`, then browsed to `http://example.com`. Waited for the page to fully load before stopping the capture.
3. **Isolated the DNS query** — Applied filter `dns.qry.name == "example.com"` to isolate the DNS query/response — showing the Application layer resolving the domain name to an IP.
4. **Noticed IPv6-over-IPv4 behavior** — The DNS query went out over IPv6 even though an IPv4 address was noted earlier. This is normal on dual-stack Windows networks, which **prefer IPv6 by default (RFC 6724)** — decided by the OS network stack, not by any Wireshark filter.
5. **Read the resolved address** — From the DNS response (Answer RRs: 1), noted `example.com`'s resolved IPv6 address.
6. **Isolated the TCP handshake** — Applied `tcp.flags.syn==1 && ipv6.addr == <resolved IP>` to isolate the 3-way handshake specific to `example.com`, since the browser opened several parallel connections. Used the first SYN/SYN-ACK pair.
7. **Confirmed HTTPS upgrade** — Destination port was 443, confirming the browser auto-upgraded the connection to HTTPS. Switched to `tls.handshake.type == 1 && ipv6.addr == <resolved IP>` to capture the TLS Client Hello instead of a plain HTTP filter.
8. **Identified the Client Hello** — Found the Client Hello packet for `example.com` via the **Server Name Indication (SNI)** field, visible directly in the Info column as `"Client Hello (SNI=example.com)"`.
9. **Captured the Physical layer** — Captured the Frame-level view of a packet to represent the Physical layer — the raw bits/signal information before Wireshark parses any headers.

## 🔍 Filters Used

```
dns.qry.name == "example.com"
tcp.flags.syn==1 && ipv6.addr == <example.com's resolved IP>
tls.handshake.type == 1 && ipv6.addr == <example.com's resolved IP>
```

## 📸 Screenshots and Output Explanation

**Screenshot 1 — DNS Query**
![DNS Query](./screenshots/01-dns-query.png)
Shows the Application layer asking for `example.com`'s IP address using a UDP query on port 53, before any TCP connection is made.

**Screenshot 2 — TCP 3-Way Handshake**
![TCP handshake — IP header](./screenshots/02a-tcp-3way-handshake-ip-header.png)
![TCP handshake — SYN flag](./screenshots/02b-tcp-3way-handshake-syn-flag.png)
Shows the Transport layer setting up a reliable connection (SYN, SYN-ACK, ACK) before any data is sent. The destination port 443 confirms the connection used HTTPS.

**Screenshot 3 — TLS Client Hello**
![TLS Client Hello](./screenshots/03-tls-client-hello.png)
Captures the TLS handshake beginning — the Client Hello packet identified via the SNI field `(SNI=example.com)`, showing the Presentation-layer encryption negotiation.

**Screenshot 4 — Physical Layer (Frame)**
![Physical layer frame](./screenshots/04-physical-layer-frame.png)
Shows the raw "Frame: N bytes on wire" detail, representing the Physical layer — the actual signal captured by the Wi-Fi NIC before any header is read.

## 🔑 Key Observations

1. **Encapsulation** — Each layer adds its own header while going down the stack (Application → Physical) when sending, and removes it in reverse order when receiving.
2. **OS-level protocol choice vs. Wireshark filters** — On dual-stack systems, the OS may prefer IPv6 over IPv4 automatically. A Wireshark filter cannot change this — it only controls what is *displayed* after capture, not what protocol the OS actually sends.

## ✅ Conclusion

The capture successfully showed how a single web request passes through the Application, Transport, Network, Data Link, and Physical layers, matching both the OSI and TCP/IP models. All screenshots and filters confirm the layers work together correctly, and the assignment requirements are fully satisfied.
