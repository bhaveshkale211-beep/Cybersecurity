# Assignment 02 — DNS Resolution Analysis

## 🎯 Scenario & Objective

**Scenario:** An organization's IT team noticed strange delays and loading lag while employees browse websites, with concerns that network traffic might be exposed to security vulnerabilities.

**Objective:** As a Security Analyst, investigate exactly how domain names translate into IP addresses, check the DNS records running behind the scenes, and explain why HTTPS must be used instead of HTTP to keep company data safe.

## 🛠️ Tools Used

- Conceptual/analytical (no simulation tool — protocol-level walkthrough)

## 🔎 How DNS Resolution Works (Step-by-Step)

Using `www.wikipedia.org` as the example:

1. **Browser Cache Check** — The computer checks its local browser/OS cache first. If the IP is already known from a recent visit, it connects instantly.
2. **Ask the Local DNS Resolver** — If not cached locally, the request goes to the Local DNS Resolver. If *it* has the answer cached, it replies immediately.
3. **Query the Root Name Server** — If not, the resolver asks a global Root Name Server (`.`). The root doesn't know the exact site, but reads the extension (`.org`) and points to the `.org` TLD server.
4. **Query the TLD Name Server** — The `.org` TLD server looks up `wikipedia.org` and returns the IP of Wikipedia's Authoritative Name Server.
5. **Query the Authoritative Name Server** — This server holds the master record for the domain, and returns the final IP: `198.35.26.96`.
6. **Load the Page** — The resolver passes the IP back to the browser, which contacts the web server directly and loads the page.

## 📋 Common DNS Record Types

| Record Type | Role | Example Purpose |
|---|---|---|
| **A Record** | Maps a domain name to an IPv4 address | Points `www.wikipedia.org` to `198.35.26.96` |
| **AAAA Record** | Maps a domain name to an IPv6 address | Used for modern IPv6-based networks |
| **MX Record** | Specifies mail servers for the domain | Routes employee emails to the correct mail server, not the web server |
| **CNAME Record** | Creates an alias pointing one domain to another | Points `blog.example.com` to `example.com` |
| **TXT Record** | Holds arbitrary text for external verification | Verifies domain ownership, helps prevent spam/email spoofing |

**Why multiple records exist for one domain:** A single business runs multiple services at once — e.g. an A Record for the public website, an MX Record for internal email routing, and multiple TXT Records for security/certificate verification. A domain can even have multiple A Records pointing to different server IPs (load distribution).

## 🔐 HTTP vs HTTPS

- **HTTP (non-secure):** Sends all data in plain text. Anyone sharing the same Wi-Fi/network can use sniffing tools to read passwords, personal data, and sensitive company information in transit.
- **HTTPS (secure):** Uses an SSL/TLS certificate to encrypt data before it leaves the device. Even if intercepted, an attacker only sees scrambled text. HTTPS also authenticates the site — confirming the user is connected to the real website, not a hacker's fake copy.

## 📈 Findings & Recommendations

- **Delays:** Likely caused by a slow/unoptimized Local DNS Resolver taking too long through the Root → TLD → Authoritative chain. **Fix:** switch to fast public DNS resolvers like Google DNS (`8.8.8.8`) or Cloudflare DNS (`1.1.1.1`).
- **Security:** To prevent data leaks and interception, enforce a policy blocking non-secure HTTP connections — all company browsing and transactions should be restricted to HTTPS.

## 🔑 Key Takeaways

- The full DNS resolution chain: cache → resolver → root → TLD → authoritative server
- What each major DNS record type does and why domains need several of them
- Why HTTPS is non-negotiable for protecting data in transit, and how it differs technically from HTTP
- Practical, real-world fixes for both DNS performance and web traffic security

> 📌 No screenshots for this assignment — the report is analytical/text-based only.
