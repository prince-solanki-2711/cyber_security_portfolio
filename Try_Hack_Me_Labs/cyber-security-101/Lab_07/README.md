# TryHackMe – Windows Fundamentals Part 3

## Lab Completion Proof

![Room Completed](screenshot/room-completed.png)

*Screenshot showing successful completion of the Windows Fundamentals Part 3 room on TryHackMe.*

## Overview

In this room, I learned about important Windows security features and how Windows protects a system from different threats. I explored Windows Update, Windows Security, Virus and Threat Protection, Firewall and Network Protection, App and Browser Control, and Device Security.

I also learned about BitLocker and Volume Shadow Copy Service (VSS), which help protect data and support recovery.

## What I Learned

### 1. Windows Update

Windows Update helps keep the Windows operating system up to date.

- It provides security updates to fix vulnerabilities.
- It provides bug fixes and improvements.
- It helps protect the system from known security threats.
- Regular updates help maintain system security and stability.

### 2. Windows Security

Windows Security is a built-in security application in Windows. It provides different security features to protect the computer.

It includes several sections, such as:

- Virus and Threat Protection
- Firewall and Network Protection
- App and Browser Control
- Device Security

These features help protect the system from malware, unsafe applications, network threats, and other security risks.

### 3. Virus and Threat Protection

Virus and Threat Protection helps protect the computer from viruses, malware, and other security threats.

It provides features to:

- Scan the computer for threats.
- Check protection history.
- Manage antivirus settings.
- Detect and remove malicious files.

Microsoft Defender Antivirus is included in Windows and helps detect and protect against malware.

### 4. Firewall and Network Protection

Windows Firewall helps protect a computer from unwanted network connections.

It monitors incoming and outgoing network traffic based on configured rules.

It provides different network profiles:

- **Domain Network:** Used when the computer is connected to a domain network.
- **Private Network:** Used for trusted private networks, such as a home network.
- **Public Network:** Used for public networks, such as Wi-Fi in cafes or airports.

A firewall helps control network communication and blocks connections that are not allowed by its rules.

### 5. App and Browser Control

App and Browser Control helps protect the system from potentially unsafe applications, files, and websites.

It includes security features that help:

- Protect against malicious or suspicious applications.
- Warn users about unsafe files and websites.
- Reduce the risk of running potentially harmful content.

These protections help prevent users from accidentally opening or installing unsafe content.

### 6. Device Security

Device Security provides security features that help protect the computer at the hardware and system level.

It includes security options such as:

- **Core Isolation:** Helps protect important system processes from malicious code.
- **Memory Integrity:** Helps prevent malicious code from accessing high-security processes.

These features add another layer of protection to the Windows system.

### 7. BitLocker

BitLocker is a Windows feature used to encrypt drives.

- It protects data by encrypting the contents of a drive.
- It helps prevent unauthorized access to data if a device or drive is lost or stolen.
- A recovery key can be used to regain access when required.

BitLocker is useful for protecting sensitive information stored on a computer.

### 8. Volume Shadow Copy Service (VSS)

Volume Shadow Copy Service (VSS) is a Windows service that helps create consistent copies of data for backup purposes.

These copies are also called **shadow copies**, **snapshots**, or **point-in-time copies**.

- VSS coordinates the actions needed to create a consistent shadow copy.
- Shadow copies are stored in the `System Volume Information` folder on drives where protection is enabled.
- When System Protection is turned on, Windows can create restore points that use this functionality.

VSS helps users recover previous versions of data and supports system recovery.

## Practical Experience

During this lab, I explored different Windows security settings and learned how they help protect a system.

I explored Windows Update and Windows Security, checked the different protection sections, and learned about drive encryption using BitLocker and data recovery using Volume Shadow Copy Service.

## SOC Analyst Relevance

Understanding Windows security features is useful for a SOC Analyst because:

- **Windows Update:** Helps understand the importance of security patches and system updates.
- **Virus and Threat Protection:** Helps understand how antivirus tools detect and protect against malware.
- **Firewall and Network Protection:** Helps understand how network traffic is controlled.
- **App and Browser Control:** Helps understand protection against unsafe applications and websites.
- **Device Security:** Helps understand hardware-level and system-level security protections.
- **BitLocker:** Helps understand how encryption protects sensitive data.
- **Volume Shadow Copy Service:** Helps understand Windows backup and recovery features.

These concepts help a SOC Analyst understand the security controls available on Windows systems.

## Key Takeaways

- Windows Update helps keep the operating system secure and up to date.
- Windows Security provides built-in protection features.
- Microsoft Defender Antivirus helps detect and protect against malware.
- Windows Firewall controls network connections.
- App and Browser Control helps protect against unsafe applications and websites.
- Device Security provides additional system-level protection.
- BitLocker encrypts drives to protect stored data.
- VSS creates shadow copies that support backup and recovery.

## Lab Details

- **Platform:** TryHackMe
- **Learning Path:** Cyber Security 101
- **Room:** Windows Fundamentals Part 3
- **Status:** Completed

## Disclaimer

These notes document my learning from an authorized TryHackMe lab environment and are intended for educational purposes.