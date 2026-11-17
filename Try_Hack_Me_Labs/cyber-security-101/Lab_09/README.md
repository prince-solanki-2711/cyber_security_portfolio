# TryHackMe – Windows Command Line

## Lab Completion Proof

![Room Completed](screenshot/room-completed.png)

*Screenshot showing successful completion of the Windows Command Line room on TryHackMe.*

## Overview

In this room, I learned how to use the Windows Command Line (CLI) to interact with the Windows operating system. I explored the difference between a Graphical User Interface (GUI) and a Command Line Interface (CLI).

I also practised basic system commands, networking commands, file and directory management, and commands for viewing and managing running processes.

## What I Learned

### 1. Introduction – GUI and CLI

Windows provides two common ways to interact with the operating system:

- **Graphical User Interface (GUI):** Allows users to interact with the system using windows, icons, menus, and buttons.
- **Command Line Interface (CLI):** Allows users to interact with the system by entering text-based commands in a terminal.

The Windows Command Prompt is an example of a CLI.

The CLI is useful because it allows users to perform tasks quickly, automate operations, and manage the system using commands.

### 2. Basic System Commands

I learned some basic commands used to view system information and work with the Command Prompt.

| Command | Purpose |
|---|---|
| `set` | Displays or changes environment variables. |
| `ver` | Displays the Windows version. |
| `systeminfo` | Displays detailed information about the computer and operating system. |
| `more` | Displays output one screen at a time. |
| `driverquery` | Lists installed device drivers. |
| `help` | Displays help information about available commands. |
| `cls` | Clears the Command Prompt screen. |

These commands help users understand the Windows environment and check basic system information.

### 3. Networking Commands

I learned how to use Windows networking commands to check network configuration, test connectivity, and view network activity.

| Command | Purpose |
|---|---|
| `ipconfig` | Displays basic IP configuration information. |
| `ipconfig /all` | Displays detailed network configuration information. |
| `ping` | Tests connectivity to another device or host. |
| `tracert` | Shows the route taken by packets to reach a destination. |
| `nslookup` | Queries DNS to find information about domain names and IP addresses. |
| `netstat` | Displays network connections, listening ports, and network statistics. |

These commands are useful for basic network troubleshooting and understanding network communication.

### 4. Working with Directories and Files

I learned how to navigate directories and manage files using the Windows Command Prompt.

| Command | Purpose |
|---|---|
| `cd` | Changes the current directory. |
| `dir` | Lists files and folders in the current directory. |
| `tree` | Displays the directory structure in a tree format. |
| `mkdir` | Creates a new directory. |
| `rmdir` | Removes a directory. |
| `type` | Displays the contents of a text file. |
| `more` | Displays file contents one screen at a time. |
| `copy` | Copies files from one location to another. |
| `move` | Moves files or directories to another location. |
| `del` | Deletes one or more files. |
| `erase` | Deletes one or more files; it works like `del`. |

These commands make it possible to manage files and folders without using File Explorer.

### 5. Managing Processes

A process is a running instance of a program or application.

Windows provides commands to view and manage running processes through the Command Prompt.

**Tasklist**

The `tasklist` command displays a list of currently running processes.

Example:

```cmd
tasklist
```

It displays information such as:

- Image Name – Name of the running process.
- PID – Process ID assigned to the process.
- Session Name – Name of the session in which the process is running.
- Mem Usage – Memory currently used by the process.

**Other Tasklist Variants**

I also learned that `tasklist` supports additional options to filter and display process information.

| Command | Purpose |
|---|---|
| `tasklist /?` | Displays help and available options for tasklist. |
| `tasklist /FI "IMAGENAME eq notepad.exe"` | Displays processes matching the specified image name. |
| `tasklist /FI "PID eq 1234"` | Displays the process with the specified PID. |
| `tasklist /SVC` | Displays services hosted by each process. |
| `tasklist /V` | Displays detailed information about running processes. |

These commands help users identify running applications and inspect processes on a Windows system.

## Practical Experience

During this lab, I practised using Windows Command Prompt and explored different commands.

I used system commands to check Windows information, networking commands to inspect network configuration and connectivity, and file management commands to work with directories and files.

I also learned how to list running processes using `tasklist` and view additional process information with its options.

## SOC Analyst Relevance

Understanding Windows Command Line commands is useful for a SOC Analyst because many investigations involve checking system activity and network information.

- **System Commands:** Help collect basic information about a Windows system.
- **Networking Commands:** Help investigate network connectivity, DNS queries, routes, and active connections.
- **File and Directory Commands:** Help navigate the system and inspect files during investigations.
- **Process Management:** Helps identify running processes and investigate suspicious applications.
- **Tasklist:** Helps identify processes that may require further investigation.

These commands are useful during initial investigation, system analysis, and incident response.

## Key Takeaways

- GUI and CLI are two different ways to interact with Windows.
- Windows Command Prompt provides commands for managing and inspecting the system.
- System commands help collect operating system and hardware information.
- Networking commands help troubleshoot and investigate network activity.
- File and directory commands help manage files and folders.
- The `tasklist` command helps identify running processes and their details.
- Learning CLI commands makes Windows system administration and security investigation easier.

## Lab Details

- **Platform:** TryHackMe
- **Learning Path:** Cyber Security 101
- **Room:** Windows Command Line
- **Status:** Completed

## Disclaimer

These notes document my learning from an authorized TryHackMe lab environment and are intended for educational purposes.