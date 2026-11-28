# TryHackMe – Tcpdump: The Basics

## Lab Completion Proof

![Tcpdump The Basics Lab Completion](screenshot/room-completed.png)

*Screenshot showing successful completion of the Tcpdump: The Basics room.*

## Overview

In this room, I learned the basics of Tcpdump, a command-line packet analyzer used to capture and inspect network traffic.

I explored how to capture packets on network interfaces, save and read packet capture files, and filter traffic based on IP addresses, ports, and protocols.

I also learned advanced packet filtering techniques, including filtering based on packet size and TCP flags. Finally, I practiced controlling how captured packets are displayed using different command-line options.

## What I Learned

### 1. Tcpdump Introduction

Tcpdump is a command-line network protocol analyzer used to capture and inspect packets travelling through a network.

It helps us monitor network traffic and investigate communication between devices.

Unlike Wireshark, which provides a graphical interface, Tcpdump works directly from the command line.

**Why Tcpdump is useful:**

- Captures network packets in real time.
- Helps monitor network communication.
- Filters traffic based on IP addresses, ports, and protocols.
- Saves captured traffic for later analysis.
- Helps troubleshoot network connectivity issues.
- Supports security investigations by allowing analysts to inspect network traffic.

### 2. Tcpdump Basics – Command-Line Options

Tcpdump provides different command-line options to control packet capturing and viewing.

**Common command-line options:**

| Command | Purpose |
|---|---|
| `tcpdump -i INTERFACE` | Captures packets on a specific network interface. |
| `tcpdump -i any` | Captures packets on all available interfaces. |
| `tcpdump -w FILE` | Saves captured packets to a file. |
| `tcpdump -r FILE` | Reads captured packets from a file. |
| `tcpdump -c COUNT` | Captures a specific number of packets. |
| `tcpdump -n` | Disables IP address resolution. |
| `tcpdump -nn` | Disables IP address and port number resolution. |
| `tcpdump -v` | Displays more packet details. |
| `tcpdump -vv` | Displays even more packet details. |
| `tcpdump -vvv` | Displays the highest verbosity level of these three options. |

**Examples:**

Capture packets on a specific interface:

```bash
sudo tcpdump -i eth0
```

Capture packets on all available interfaces:

```bash
sudo tcpdump -i any
```

Capture only 10 packets:

```bash
sudo tcpdump -i eth0 -c 10
```

Save captured packets to a file:

```bash
sudo tcpdump -i eth0 -w capture.pcap
```

Read packets from a saved file:

```bash
tcpdump -r capture.pcap
```

Display IP addresses and port numbers without resolving them into names:

```bash
sudo tcpdump -nn
```

Display more packet details:

```bash
sudo tcpdump -vv
```

**Important point:**

The `-w` option saves packets in a capture file, while the `-r` option reads packets from an existing capture file. The saved file can also be opened in Wireshark for further analysis.

### 3. Tcpdump Basic Packet Filtering

Packet filtering allows us to capture or display only the traffic we are interested in.

Tcpdump supports filters based on hosts, ports, and network protocols.

#### Host Filtering

| Filter | Purpose |
|---|---|
| `host IP` | Filters packets to or from a particular IP address. |
| `host HOSTNAME` | Filters packets to or from a hostname. |
| `src host IP` | Filters packets from a specific source host. |
| `dst host IP` | Filters packets going to a specific destination host. |

**Examples:**

Capture traffic to or from a particular IP:

```bash
sudo tcpdump host 192.168.1.10
```

Capture traffic from a specific source IP:

```bash
sudo tcpdump src host 192.168.1.10
```

Capture traffic going to a specific destination IP:

```bash
sudo tcpdump dst host 192.168.1.20
```

#### Port Filtering

| Filter | Purpose |
|---|---|
| `port 53` | Filters packets to or from port 53. |
| `src port 53` | Filters packets with source port 53. |
| `dst port 53` | Filters packets with destination port 53. |

**Examples:**

Capture traffic using port 53:

```bash
sudo tcpdump port 53
```

Capture packets with source port 53:

```bash
sudo tcpdump src port 53
```

Capture packets with destination port 53:

```bash
sudo tcpdump dst port 53
```

Port 53 is commonly used by DNS.

#### Protocol Filtering

| Filter | Purpose |
|---|---|
| `tcp` | Filters TCP packets. |
| `udp` | Filters UDP packets. |
| `icmp` | Filters ICMP packets. |
| `arp` | Filters ARP packets. |
| `ip` | Filters IPv4 packets. |
| `ip6` | Filters IPv6 packets. |

**Examples:**

Capture only TCP packets:

```bash
sudo tcpdump tcp
```

Capture only UDP packets:

```bash
sudo tcpdump udp
```

Capture only ICMP packets:

```bash
sudo tcpdump icmp
```

Capture only ARP packets:

```bash
sudo tcpdump arp
```

Capture only IPv4 packets:

```bash
sudo tcpdump ip
```

Capture only IPv6 packets:

```bash
sudo tcpdump ip6
```

**Important point:**

Basic packet filters help reduce unnecessary traffic and make it easier to focus on specific network communication.

### 4. Tcpdump Advanced Packet Filtering

Tcpdump also supports advanced filtering expressions that allow us to inspect packets based on their size, header fields, and TCP flags.

#### Packet Size Filtering

We can filter packets based on their length.

| Filter | Purpose |
|---|---|
| `greater LENGTH` | Matches packets larger than the specified length. |
| `less LENGTH` | Matches packets smaller than the specified length. |

**Examples:**

Capture packets larger than 1000 bytes:

```bash
sudo tcpdump greater 1000
```

Capture packets smaller than 100 bytes:

```bash
sudo tcpdump less 100
```

#### Logical and Binary Operators

Tcpdump supports operators that help combine or modify filter conditions.

| Operator | Purpose |
|---|---|
| `&` | Binary AND. |
| `\|` | Binary OR. |
| `!` | Binary NOT / negation in filter expressions. |

These operators help create more specific filters.

#### Header Byte Access

Tcpdump allows us to inspect specific bytes in a packet header using the following syntax:

```text
proto[expr:size]
```

- `proto`: Protocol or header to inspect.
- `expr`: Byte offset or expression identifying the position.
- `size`: Number of bytes to examine.

This feature is useful when filtering packets based on specific header fields.

#### TCP Flags Filtering

TCP uses flags to control and manage connections between devices.

Common TCP flags include:

| TCP Flag | Purpose |
|---|---|
| SYN | Starts a TCP connection. |
| ACK | Acknowledges received data or connection information. |
| FIN | Indicates that a device wants to close a TCP connection. |
| RST | Resets a TCP connection. |
| PSH | Requests that received data be pushed to the application promptly. |

Tcpdump allows us to filter packets based on these flags.

**Common TCP flag filters:**

| Filter | Purpose |
|---|---|
| `tcp[tcpflags]` | Accesses the TCP flags field. |
| `tcp-syn` | Matches packets with the SYN flag set. |
| `tcp-ack` | Matches packets with the ACK flag set. |
| `tcp-fin` | Matches packets with the FIN flag set. |
| `tcp-rst` | Matches packets with the RST flag set. |
| `tcp-push` | Matches packets with the PSH flag set. |

**Only SYN flag is set:**

```bash
sudo tcpdump 'tcp[tcpflags] == tcp-syn'
```

This matches TCP packets where SYN is set and the other TCP flags are not set.

**SYN flag is set:**

```bash
sudo tcpdump 'tcp[tcpflags] & tcp-syn != 0'
```

This matches TCP packets where the SYN flag is set, even if other flags are also set.

**SYN or ACK flag is set:**

```bash
sudo tcpdump 'tcp[tcpflags] & (tcp-syn|tcp-ack) != 0'
```

This matches packets where either SYN or ACK is set.

**Why TCP flag filtering is useful:**

- Helps analyze TCP connection establishment.
- Helps identify connection attempts.
- Helps investigate connection resets.
- Helps examine unusual TCP traffic patterns.

### 5. Tcpdump – Controlling How Packets Are Displayed

Tcpdump provides different options to control how packet information is displayed.

These options help us inspect packet headers and data in different formats.

| Option | Purpose | Use |
|---|---|---|
| `-q` | Displays brief packet information. | Quick inspection. |
| `-e` | Displays the link-level header, including MAC addresses. | Data Link Layer analysis. |
| `-A` | Displays packet data in ASCII format. | Reading text-based data. |
| `-xx` | Displays packet data in hexadecimal, including the link-level header. | Inspecting raw packet bytes. |
| `-X` | Displays packet headers and data in hexadecimal and ASCII. | Detailed packet inspection. |

**Examples:**

Quick packet output:

```bash
sudo tcpdump -q -i eth0
```

Display link-level headers:

```bash
sudo tcpdump -e -i eth0
```

Display packet data in ASCII:

```bash
sudo tcpdump -A -i eth0
```

Display packet data in hexadecimal:

```bash
sudo tcpdump -xx -i eth0
```

Display packet headers and data in hexadecimal and ASCII:

```bash
sudo tcpdump -X -i eth0
```

**Important point:**

These options change how packet information is displayed. They do not change the actual packet contents.

## Practical Experience

During this room, I got hands-on experience using Tcpdump from the command line.

I practiced capturing network traffic, applying different filters, and controlling how packet information is displayed.

My practical activities included:

- Understanding how Tcpdump works.
- Capturing packets on specific network interfaces.
- Saving captured packets into PCAP files.
- Reading previously saved capture files.
- Limiting packet capture using the `-c` option.
- Filtering traffic using IP addresses, hostnames, ports, and protocols.
- Applying advanced filters based on packet size and TCP flags.
- Inspecting TCP SYN, ACK, FIN, RST, and PSH flags.
- Displaying packet information in brief, ASCII, hexadecimal, and combined formats.

These activities helped me understand how to inspect network traffic using a command-line tool.

## SOC Analyst Relevance

Tcpdump is a useful tool for SOC Analysts because it helps capture and investigate network traffic, especially when working on systems without a graphical interface.

- **Traffic Capture:** Helps collect network packets for security investigations.
- **Host Filtering:** Helps investigate communication involving suspicious IP addresses.
- **Port Filtering:** Helps monitor traffic related to specific services such as DNS and HTTP.
- **Protocol Filtering:** Helps identify communication using TCP, UDP, ICMP, and other protocols.
- **Advanced Filtering:** Helps investigate unusual packet sizes and specific TCP flag combinations.
- **PCAP Analysis:** Helps save traffic for later investigation using tools such as Wireshark.
- **Packet Inspection:** Helps examine packet headers and data to understand network communication.

## Key Takeaways

- Tcpdump is a command-line tool used to capture and analyze network traffic.
- The `-i` option selects the network interface.
- The `-w` option saves packets, while `-r` reads saved capture files.
- Basic filters help identify traffic based on hosts, ports, and protocols.
- Advanced filters allow us to inspect packet sizes, header bytes, and TCP flags.
- TCP flags help us understand connection establishment and termination.
- The `-q`, `-e`, `-A`, `-xx`, and `-X` options control how packet information is displayed.
- Tcpdump is useful for network troubleshooting and SOC investigations.

## Lab Details

- **Platform:** TryHackMe
- **Learning Path:** Cyber Security 101
- **Room:** Tcpdump: The Basics
- **Status:** Completed

## Disclaimer

These notes document my learning from an authorized TryHackMe lab environment and are intended for educational purposes.