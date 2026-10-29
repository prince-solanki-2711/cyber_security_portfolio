# TryHackMe — What Is Networking?

## Lab Completion Proof

![TryHackMe What Is Networking Completion](screenshot/room-completed.png)

This section displays the TryHackMe room completion screenshot as proof that the lab has been completed.

## Overview

In this lab, I learned the basics of computer networking, the importance of networks, and how the internet connects devices around the world. I also learned about network types, device identification using IP and MAC addresses, MAC address spoofing, and how the `ping` command is used to test network connectivity.

## What I Learned

### 1. What Is Networking?

- Networking is the process of connecting devices so they can communicate and share data.
- Networks allow computers, smartphones, servers, and other devices to exchange information.

### 2. Networks in Everyday Life

- Networks are used in everyday activities such as browsing websites, sending messages, streaming videos, and sharing files.
- Devices use networks to communicate with other devices and access online services.

### 3. Importance of Computer Networking

- Networking allows devices to share information and resources.
- It enables communication between users, computers, and servers.
- It provides access to services and information available over a network.

### 4. What Is the Internet?

- The internet is a global network of interconnected networks.
- It allows devices around the world to communicate and exchange information.
- Websites, online applications, and many digital services use the internet to communicate.

### 5. Understanding Networks Through an Example

- A network allows connected devices to exchange data.
- When a device requests information from another device, the information travels through the network.
- Communication depends on devices and networking systems working together to deliver data to its destination.

### 6. History of the Internet

- I learned about the history and development of the internet.
- The internet evolved from earlier computer networks into a global system connecting devices and networks around the world.

### 7. Types of Networks

- Networks can be classified according to their size, coverage, and purpose.
- Different types of networks are used to connect devices within a small area or across larger geographical areas.

### 8. Identifying Devices on a Network

- Devices on a network need identifiers so that network communication can reach the appropriate destination.
- IP addresses and MAC addresses are two important concepts used to identify devices in networking.

### 9. Device Identification

- Network devices use different types of addresses for identification and communication.
- IP addresses are used for logical addressing, while MAC addresses are associated with network interfaces.

### 10. IP Address

- An IP address is a logical address used to identify a device or network interface for communication over an IP network.
- IP addressing helps data reach the appropriate destination across networks.

### 11. IPv4 and IPv6

- **IPv4:** Uses a 32-bit address, commonly written in four decimal numbers separated by dots. Example: `192.168.1.10`.
- **IPv6:** Uses a 128-bit address, written in hexadecimal groups separated by colons. Example: `2001:db8::1`.
- IPv6 provides a much larger address space than IPv4.

### 12. MAC Address

- A MAC address is an address associated with a network interface.
- It is commonly represented as hexadecimal pairs, such as `00:1A:2B:3C:4D:5E`.
- MAC addresses are commonly used for communication within a local network segment.

### 13. MAC Address Spoofing

- MAC address spoofing involves changing or imitating the MAC address presented by a network interface.
- It can be used for legitimate testing and privacy-related purposes, but it can also be misused to impersonate another device.
- Changing a MAC address does not automatically change the device's IP address or guarantee anonymity.

### 14. What Is Ping?

- `ping` is a network utility used to test whether a destination can be reached over an IP network.
- It can also help measure the time taken for responses to return.
- It commonly uses ICMP Echo Request and Echo Reply messages.

### 15. How Does Ping Work?

- The source device sends an ICMP Echo Request to the destination.
- If the destination and network allow it, an ICMP Echo Reply is returned.
- The response time helps indicate the round-trip time between the devices.
- A missing reply does not always mean the destination is offline, because a firewall or network configuration may block ICMP traffic.

### 16. Ping Command

The `ping` command can be used from a command-line interface to test connectivity to an IP address or hostname.

Example:

```bash
ping 8.8.8.8
```

This command sends ping requests to the IP address `8.8.8.8` and displays the responses, if received.

Another example:

```bash
ping example.com
```

This tests connectivity to the hostname `example.com`. The hostname must first be resolved to an IP address.

## Practical Experience

During this lab, I explored the fundamentals of networking, device identification, IP addressing, and the purpose of MAC addresses. I also learned how the `ping` command uses ICMP messages to test network reachability and measure response times.

## SOC Analyst Relevance

Understanding networking is important for a SOC Analyst because:

- **Network troubleshooting:** Helps investigate connectivity problems.
- **IP address analysis:** Helps understand the source and destination of network traffic.
- **Device identification:** Helps interpret IP and MAC addresses during network investigations.
- **Ping and ICMP:** Helps recognize basic network diagnostic activity.
- **Network security:** Provides foundational knowledge for understanding network communication and investigating suspicious activity.

## Key Takeaways

- Networking allows devices to communicate and share information.
- The internet connects networks around the world.
- IPv4 and IPv6 are different versions of IP addressing.
- IP addresses and MAC addresses serve different purposes.
- MAC address spoofing changes the MAC address presented by a network interface.
- `ping` uses ICMP messages to test network reachability and measure response time.

## Lab Details

- **Platform:** TryHackMe
- **Learning Path:** Pre-Security
- **Room:** What Is Networking?
- **Status:** Completed

## Disclaimer

These notes summarize the concepts learned during the TryHackMe Pre-Security lab. They are intended for educational purposes and personal revision.