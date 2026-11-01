# TryHackMe — DNS in Detail

## Lab Completion Proof

![TryHackMe DNS in Detail Completion](screenshot/room-completed.png)

This section displays the TryHackMe room completion screenshot as proof that the lab has been completed.

## Overview

In this lab, I learned about the Domain Name System (DNS), why it is needed, and how it translates human-readable domain names into IP addresses. I explored domain hierarchy, different types of DNS records, and the complete process that takes place when a DNS request is made. I also learned about DNS servers, local DNS caching, and Time to Live (TTL).

## What I Learned

### 1. What Is DNS?

- DNS stands for **Domain Name System**.
- It is a system that translates human-readable domain names into IP addresses.
- Computers use IP addresses to communicate with other devices over a network.
- DNS makes it easier for users to access websites and online services using domain names instead of remembering IP addresses.

**Example:**

When you enter `tryhackme.com` into your browser, DNS helps find the IP address associated with that domain name so your device can communicate with the correct server.

### 2. Why Do We Need DNS?

- Computers communicate with each other using IP addresses.
- Remembering the IP addresses of every website would be difficult for users.
- DNS allows users to access websites using easy-to-remember domain names.
- It automatically helps resolve domain names into their corresponding IP addresses.
- It makes accessing websites and online services easier.

### 3. What Is Domain Hierarchy?

- Domain hierarchy is the structure used to organize domain names.
- A domain name is divided into different levels.
- Each level represents a different part of the domain name.
- DNS uses this hierarchical structure to organize and manage domain names.

**Example:**

```text
www.tryhackme.com
```

The domain hierarchy can be understood as:

- `.com` — Top-Level Domain (TLD).
- `tryhackme` — Second-Level Domain.
- `www` — Subdomain.

### 4. TLD (Top-Level Domain)

- TLD stands for Top-Level Domain.
- It is the last part of a domain name.
- It appears after the final dot in a domain name.

**Examples:**

```text
google.com
amazon.com
tryhackme.com
```

In these examples, `.com` is the TLD.

### 5. gTLD (Generic Top-Level Domain)

- gTLD stands for Generic Top-Level Domain.
- These are TLDs that are generally used for different categories or purposes.
- They are not restricted to a particular country.

**Examples:**

- `.com` — Commonly used for commercial websites.
- `.org` — Commonly associated with organizations.
- `.net` — Originally associated with network-related services.
- `.edu` — Used by eligible educational institutions.

### 6. ccTLD (Country Code Top-Level Domain)

- ccTLD stands for Country Code Top-Level Domain.
- These TLDs are associated with specific countries or territories.
- They usually contain two letters.

**Examples:**

- `.in` — India.
- `.uk` — United Kingdom.
- `.us` — United States.
- `.au` — Australia.

### 7. Second-Level Domain

- The second-level domain is the part of the domain name directly before the TLD.
- It identifies the registered domain name.

**Example:**

```text
tryhackme.com
```

In this example:
- `tryhackme` — Second-Level Domain.
- `.com` — Top-Level Domain.

### 8. Subdomain

- A subdomain is an additional part placed before the main domain name.
- It is used to organize different sections or services of a website.
- A domain can have multiple subdomains.

**Examples:**

```text
www.tryhackme.com
admin.tryhackme.com
blog.tryhackme.com
```

Here, `www`, `admin`, and `blog` are subdomains of `tryhackme.com`.

### 9. Multiple Domains

- An organization or company can own multiple domain names.
- Different domains can be used for different websites, services, or purposes.
- Each domain can also have its own subdomains.

For example:

```text
example.com
example.net
example.org
```

These are separate domain names, even though they use the same second-level name.

### 10. DNS Records

- DNS records are entries stored in DNS servers.
- They contain information about a domain name and its associated services or network addresses.
- Different DNS record types provide different kinds of information.
- When a DNS query is made, the DNS server returns the relevant record.

### 11. A Record

- An A record maps a domain name to an IPv4 address.
- It helps a device find the IPv4 address associated with a domain.

**Example:**

```text
tryhackme.com → 104.26.10.229
```

Here, the A record provides the IPv4 address for `tryhackme.com`.

### 12. AAAA Record

- An AAAA record maps a domain name to an IPv6 address.
- It performs a similar function to an A record, but it returns an IPv6 address.

**Example:**

```text
example.com → 2001:db8::1
```

Here, the AAAA record provides an IPv6 address.

### 13. CNAME Record

- CNAME stands for Canonical Name.
- A CNAME record points one domain name or subdomain to another domain name.
- It acts as an alias for another domain name.

**Example:**

```text
www.example.com → example.com
```

Here, `www.example.com` is an alias for `example.com`.

### 14. MX Record

- MX stands for Mail Exchange.
- An MX record specifies the mail server responsible for receiving emails for a domain.
- It helps email systems determine where emails should be delivered.
- MX records can contain priority values to determine which mail server should be preferred.

### 15. TXT Record

- A TXT record stores text-based information associated with a domain.
- It is commonly used for domain verification and email security configurations.
- It can contain information used by services to verify domain ownership or validate email-sending sources.

### 16. What Happens When You Make a DNS Request?

When you enter a domain name into your browser, several steps take place to find the IP address associated with that domain.

The DNS lookup process involves the following components:

1. Local DNS Cache.
2. Recursive DNS Server.
3. Root DNS Server.
4. TLD DNS Server.
5. Authoritative DNS Server.

### 17. Local DNS Cache

- When you request a domain name, your computer first checks its local DNS cache.
- The cache stores previously resolved domain names and their IP addresses.
- If the required record is available and has not expired, the computer can use the cached result.
- This avoids making unnecessary DNS requests to external DNS servers.

### 18. Recursive DNS Server

- If the required DNS record is not available in the local cache, the request is sent to a recursive DNS server.
- The recursive DNS server is responsible for finding the IP address associated with the requested domain.
- It contacts other DNS servers when necessary to find the required information.
- It returns the result to the requesting device and can cache the response for future requests.
- Recursive DNS servers are often provided by ISPs or public DNS providers.

### 19. Root DNS Server

- Root DNS servers are at the top of the DNS hierarchy.
- They help direct DNS queries to the appropriate TLD DNS servers.
- They do not normally provide the final IP address of the requested domain.
- Instead, they return information about which TLD DNS server should be contacted next.

### 20. TLD DNS Server

- TLD stands for Top-Level Domain.
- TLD DNS servers manage information about domains belonging to a particular TLD, such as `.com`, `.org`, or `.in`.
- They direct the recursive DNS server toward the authoritative DNS server responsible for the requested domain.

### 21. Authoritative DNS Server

- An authoritative DNS server stores the actual DNS records for a domain.
- It provides the final DNS answer for the requested record.
- For example, when an A record is requested, it can return the IPv4 address associated with the domain.
- It is the source of authoritative DNS information for that domain.

### 22. Complete DNS Request Process

Let's understand the complete process using an example:

Suppose you enter:

```text
www.tryhackme.com
```

The following steps take place:

1. Your computer first checks its local DNS cache for the IP address of `www.tryhackme.com`.
2. If the record is not available in the cache, your computer sends the DNS query to a recursive DNS server.
3. The recursive DNS server contacts a Root DNS server to find the appropriate TLD server.
4. The Root DNS server directs the recursive resolver to the `.com` TLD DNS server.
5. The `.com` TLD DNS server directs the resolver to the authoritative DNS server responsible for `tryhackme.com`.
6. The authoritative DNS server returns the requested DNS record.
7. The recursive DNS server sends the result back to your computer and may cache it.
8. Your computer can now use the returned IP address to communicate with the destination server.

### 23. What Is TTL?

- TTL stands for Time to Live.
- It specifies how long a DNS record can remain in a cache before it expires.
- TTL is measured in seconds.
- When the TTL expires, the cached DNS record should no longer be treated as valid, and a new DNS lookup may be required.

**Example:**

```text
TTL: 3600 seconds
```

This means the DNS record can remain in the cache for 3600 seconds (1 hour) before it expires.

**Why Is TTL Important?**

- It controls how long DNS records are cached.
- It helps reduce repeated DNS queries.
- It can improve DNS lookup performance.
- It determines how long cached DNS information may remain available before a fresh lookup is needed.

## Practical Experience

During this lab, I learned how DNS translates domain names into IP addresses. I explored domain hierarchy, different DNS record types, and the roles of local DNS caches, recursive DNS servers, root servers, TLD servers, and authoritative DNS servers. I also understood the step-by-step process of a DNS lookup and how TTL controls DNS caching.

## SOC Analyst Relevance

Understanding DNS is important for a SOC Analyst because:

- **DNS traffic analysis:** Helps understand domain name resolution activity on a network.
- **Suspicious domain investigation:** Helps investigate unusual or potentially malicious domain names.
- **DNS record analysis:** Helps understand how domains are associated with IP addresses and other services.
- **DNS monitoring:** Helps identify unusual DNS requests and potentially suspicious domain lookups.
- **DNS tunnelling awareness:** Provides foundational knowledge for understanding how DNS can potentially be misused to transfer data.
- **Incident investigation:** Helps connect domain names, IP addresses, and network communication during security investigations.

## Key Takeaways

- DNS translates human-readable domain names into IP addresses.
- Domain hierarchy includes TLDs, second-level domains, and subdomains.
- gTLDs are generic top-level domains, while ccTLDs are associated with countries or territories.
- A records map domains to IPv4 addresses.
- AAAA records map domains to IPv6 addresses.
- CNAME records create aliases for other domain names.
- MX records identify mail servers.
- TXT records store text-based domain information.
- DNS lookups can involve local caches, recursive resolvers, root servers, TLD servers, and authoritative servers.
- TTL determines how long DNS records can remain in a cache.

## Lab Details

- **Platform:** TryHackMe
- **Learning Path:** Pre-Security
- **Room:** DNS in Detail
- **Status:** Completed

## Disclaimer

These notes summarize the concepts learned during the TryHackMe Pre-Security lab. They are intended for educational purposes and personal revision.