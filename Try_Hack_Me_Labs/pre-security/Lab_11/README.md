# TryHackMe – Windows CLI

## Lab Completion Proof

![TryHackMe Windows CLI Completion](screenshot/room-completed.png)

*Screenshot showing completion of the Windows CLI room on TryHackMe.*

## Overview

I completed the **Windows CLI** room in the Pre Security learning path on TryHackMe.

This lab introduced me to Windows, the Windows command line, basic commands for navigating directories and searching for files, and commands used to retrieve system and network information.

## What I Learned

### 1. Introduction to Windows
- Learned about Microsoft Windows and its role as an operating system.
- Understood how Windows provides an environment for running applications, managing files, and interacting with computer hardware.

### 2. What Is the Windows Command Line?
- Learned that the Windows command line allows users to interact with the operating system by entering text-based commands.
- Understood that commands can be used to navigate directories, search for files, and retrieve system information.
- Learned that the command line is useful for performing tasks without relying entirely on a graphical interface.

### 3. Navigating and Searching for Files

Learned and practiced the following Windows command-line commands:

| Command | Purpose |
|---|---|
| `cd` | Displays the current directory path when entered without a directory argument in Command Prompt. |
| `dir` | Lists files and directories in the current directory. |
| `dir /a` | Displays files and directories, including hidden and system items. |
| `cd directory_name` | Changes the current directory to the specified directory. |
| `cd ..` | Moves to the parent directory. |
| `dir /s` | Lists files and directories in the current directory and its subdirectories. |
| `type filename.txt` | Displays the contents of a text file in the command prompt. |

### 4. System Information

Learned how to use Windows commands to identify the current user, inspect the computer, and view network configuration.

| Command | Purpose |
|---|---|
| `whoami` | Displays the current user's account name. |
| `hostname` | Displays the computer's hostname. |
| `systeminfo` | Displays detailed information about the Windows system and its configuration. |
| `ipconfig` | Displays network adapter IP configuration information. |

I also learned the importance of checking system information before troubleshooting or investigating a computer.

## Practical Experience

During the lab, I gained hands-on experience using the **Windows command line** and executing commands directly.

I practiced navigating directories, listing files and directories, viewing file contents, searching through directory structures, identifying the current user, checking the computer's hostname, viewing Windows system information, and inspecting network configuration.

## SOC Analyst Relevance

Windows command-line knowledge is useful for a SOC Analyst because many organizations use Windows workstations and servers.

This knowledge provides a foundation for:
- Identifying the current user and computer during an investigation.
- Navigating directories and locating files.
- Examining text-file contents during basic investigations.
- Gathering Windows operating system and configuration information.
- Checking IP configuration when investigating network-related issues.
- Building the command-line skills needed for further Windows security monitoring and incident investigation.

As I continue preparing for a SOC Analyst Level 1 role, I will build on these fundamentals by learning Windows logs, Event Viewer, process inspection, and security investigation techniques.

## Key Takeaways

- The Windows command line allows users to interact with Windows through text-based commands.
- Commands such as `cd`, `dir`, and `dir /s` help with directory navigation and file discovery.
- The `type` command displays the contents of a text file.
- Commands such as `whoami`, `hostname`, and `systeminfo` provide useful system information.
- The `ipconfig` command helps inspect network configuration.
- Hands-on command-line practice builds a foundation for Windows administration and security investigations.

## Lab Details

- **Platform:** TryHackMe
- **Learning Path:** Pre Security
- **Room:** Windows CLI
- **Practical Work:** Windows command-line commands and system information gathering
- **Status:** Completed

## Disclaimer

These notes document my learning from an authorized TryHackMe lab environment and are intended for educational purposes.
