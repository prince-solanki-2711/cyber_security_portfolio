# TryHackMe – Networking Essentials

## Lab Completion Proof

![Networking Essentials Lab Completion](screenshot/room-completed.png)

*Screenshot showing successful completion of the Networking Essentials room.*

## Overview

In this room, I learned about some important networking protocols and concepts used for communication between devices. I explored how devices receive IP addresses, how they find each other on a local network, how network connectivity is tested, and how data travels between different networks.

I also learned how NAT allows devices with private IP addresses to communicate with the internet.

## What I Learned

### 1. DHCP (Dynamic Host Configuration Protocol)

DHCP is a network protocol that automatically assigns IP configuration to devices when they connect to a network.

Without DHCP, we would need to manually configure the IP address and other network settings on every device.

DHCP can provide the following information:

- **IP Address:** Identifies the device on the network.
- **Subnet Mask:** Defines the network and host portions of an IP address.
- **Default Gateway:** Allows the device to communicate with other networks.
- **DNS Server:** Helps resolve domain names into IP addresses.

**How DHCP works:**

DHCP commonly follows a four-step process known as DORA:

1. **Discover:** The client broadcasts a request to find a DHCP server.
2. **Offer:** The DHCP server offers an available IP address.
3. **Request:** The client requests the offered IP address.
4. **Acknowledge:** The server confirms the IP address assignment.

DHCP commonly uses UDP ports 67 and 68.

### 2. ARP (Address Resolution Protocol)

ARP is used to find the MAC address associated with an IPv4 address on a local network.

When a device wants to communicate with another device on the same local network, it needs the destination device's MAC address to send an Ethernet frame.

**How ARP works:**

1. A device checks its ARP cache to see whether it already knows the MAC address.
2. If the MAC address is not available, it broadcasts an ARP request.
3. The device with the matching IP address sends an ARP reply containing its MAC address.
4. The sender stores this information in its ARP cache.

**Important points:**

- IP addresses identify devices at the network layer.
- MAC addresses identify network interfaces on the local network.
- ARP helps map IPv4 addresses to MAC addresses.
- ARP requests are broadcast on the local network.

### 3. ICMP (Internet Control Message Protocol)

ICMP is a network-layer protocol used to send error messages and diagnostic information about network communication.

It helps us check whether a destination is reachable and understand possible network problems.

#### Ping

Ping uses ICMP Echo Request and Echo Reply messages to check connectivity between two devices.

Example:

```bash
ping 8.8.8.8
```

This command sends ICMP requests to Google's public DNS server and displays the replies if they are received.

Ping can help us understand:

- Whether a destination is reachable.
- How much time a packet takes to travel to the destination and back.
- Whether packets are being lost.

#### Traceroute

Traceroute helps identify the routers (hops) that packets pass through while travelling towards a destination.

Example on Linux:

```bash
traceroute google.com
```

On Windows:

```cmd
tracert google.com
```

It works by sending packets with increasing TTL (Time To Live) values. When a packet's TTL reaches zero, a router may return an ICMP Time Exceeded message.

This helps identify the network path and can show where delays or connectivity problems occur.

### 4. Routing

Routing is the process of forwarding network packets from one network to another so they can reach their destination.

Routers are networking devices responsible for connecting different networks and selecting suitable paths for packets.

**How routing works:**

1. A router receives a packet.
2. It checks the destination IP address.
3. It looks for a matching route in its routing table.
4. It forwards the packet through the appropriate interface or next-hop router.

**Routing Table:**

A routing table contains information that helps a router decide where to forward packets.

It generally includes:

- Destination network
- Subnet mask or prefix length
- Next-hop address
- Network interface
- Route metric

If no specific route matches the destination, the router may use a default route if one is configured.

**Important points:**

- Routing allows communication between different networks.
- Routers use destination IP addresses to make forwarding decisions.
- The default gateway is the router a device usually uses to reach destinations outside its local network.

### 5. NAT (Network Address Translation)

NAT is a networking technique that translates IP addresses as packets pass through a router or another network device.

It is commonly used to allow multiple devices with private IP addresses to access the internet using a public IP address.

For example, devices in a home network may have private IP addresses such as:

- 192.168.1.10
- 192.168.1.11
- 192.168.1.12

The router can translate their outgoing traffic so it uses the same public IP address when communicating with the internet.

**Types of NAT:**

- **Static NAT:** Maps one private IP address to one public IP address.
- **Dynamic NAT:** Maps private IP addresses to available public IP addresses from a pool.
- **PAT (Port Address Translation):** Allows multiple private devices to share one public IP address by using different port numbers. It is also commonly called NAT overload.

**Why NAT is important:**

- Helps conserve public IPv4 addresses.
- Allows private network devices to access the internet.
- Hides internal private IP addressing from external networks.

## Practical Experience

During this room, I learned how different networking protocols and devices work together to provide communication between systems.

I understood how DHCP automatically assigns network configurations, how ARP resolves IP addresses to MAC addresses, and how ICMP tools like ping and traceroute help troubleshoot network connectivity.

I also learned how routers forward packets between networks and how NAT allows multiple private devices to communicate with the internet.

## SOC Analyst Relevance

These networking concepts are useful for a SOC Analyst because network-related alerts and incidents often involve IP addresses, communication failures, and suspicious network traffic.

- **DHCP:** Helps investigate which device was assigned a particular IP address at a specific time.
- **ARP:** Helps identify unusual IP-to-MAC address mappings and possible ARP spoofing attacks.
- **ICMP:** Helps investigate connectivity issues and unusual ICMP traffic.
- **Routing:** Helps understand how traffic moves between networks and identify unexpected network paths.
- **NAT:** Helps understand how multiple internal devices can share a public IP address when investigating network logs.

## Key Takeaways

- DHCP automatically assigns IP addresses and other network settings to devices.
- ARP finds the MAC address associated with an IPv4 address on a local network.
- ICMP is used for network diagnostics and error reporting.
- Ping checks connectivity, while traceroute helps identify the path packets take.
- Routing forwards packets between different networks.
- NAT translates IP addresses and helps private devices access the internet.

## Lab Details

- **Platform:** TryHackMe
- **Learning Path:** Cyber Security 101
- **Room:** Networking Essentials
- **Status:** Completed

## Disclaimer

These notes document my learning from an authorized TryHackMe lab environment and are intended for educational purposes.