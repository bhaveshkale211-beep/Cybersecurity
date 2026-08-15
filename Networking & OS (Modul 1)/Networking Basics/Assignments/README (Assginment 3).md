# Assignment 03 — Web Security in Practice

## 🎯 Objective

Study how web security protocols work in real-world environments by inspecting `www.wikipedia.org`'s live security configuration, analyzing how modern browsers handle insecure connections, and understanding the role of CDNs like Cloudflare in boosting security and performance.

## 🛠️ Tools Used

- Web browser (built-in security/certificate inspector)

## 🔐 HTTPS Certificate Inspection

Loading `www.wikipedia.org` shows a lock icon next to the URL, confirming a secure HTTPS connection. Clicking the lock displays the site's official SSL/TLS digital certificate.

![HTTPS secure connection indicator](./screenshots/01-https-secure-connection.png)
*Browser confirming the connection to Wikipedia is secure*

![TLS certificate details](./screenshots/02-tls-certificate-details.png)
*Certificate viewer — issued to `*.wikipedia.org`, issued by Let's Encrypt, with SHA-256 fingerprint and validity period*

**Findings:** The certificate confirms all data between the browser and Wikipedia is fully encrypted — passwords, search terms, and other inputs can't be read or stolen by anyone sniffing the local network.

## ⚠️ How Browsers Handle HTTPS Warnings

When a site doesn't use HTTPS, or has an expired/invalid certificate, modern browsers block the page and show a full "Not secure" / "Your connection is not private" warning.

![HTTP not secure warning](./screenshots/03-http-not-secure-warning.png)
*Browser flagging a non-HTTPS site as "Not secure"*

**How this protects users:**
- **Active protection:** Prevents the browser from silently downloading harmful cookies or fake login scripts.
- **Human alert:** Forces the user to manually click through an "Advanced"/"Proceed anyway" link — ensuring they understand the risk before continuing.

## 🌐 How Cloudflare Improves HTTPS Security & Performance

Many sites route traffic through a CDN like Cloudflare instead of connecting users directly to their origin server:

1. **Enhanced Security** — Cloudflare acts as a proxy firewall, scanning incoming traffic and blocking malicious bots, brute-force attempts, and DDoS attacks before they reach the real backend server. It also automates SSL/TLS certificate management.
2. **Performance Optimization** — Rather than loading every file from one distant server, Cloudflare caches static pages, images, and scripts across thousands of global servers, serving users from the closest location for faster load times.

## ✅ Conclusion

Strict browser security controls and mandatory HTTPS are critical for real-world internet use. Without encryption, everyday tasks like banking, email, or filling out forms would be exposed to identity theft. HTTPS confirms site identity, protects privacy through encryption, and ensures data integrity — and combined with protections like Cloudflare, it keeps the internet safe, fast, and reliable.

## 🔑 Key Takeaways

- How to read and interpret a live TLS/SSL certificate in-browser
- What actually happens (technically and visually) when a browser blocks an insecure site
- The dual role of a CDN like Cloudflare: security (WAF/DDoS protection) *and* performance (edge caching)
- Why HTTPS is fundamental to protecting real-world web traffic
