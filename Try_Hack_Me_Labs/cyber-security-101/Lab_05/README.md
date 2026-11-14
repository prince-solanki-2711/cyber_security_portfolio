# TryHackMe – Windows Fundamentals Part 1

## Lab Completion Proof

![Room Completion Screenshot](screenshot/room-completed.png)

*Screenshot showing the successful completion of the Windows Fundamentals Part 1 room on TryHackMe.*

## Overview

In this room, I learned about the basic features of the Windows operating system and how to use its graphical user interface (GUI).

I explored the Windows desktop, file system, NTFS, important system folders, user accounts, and User Account Control (UAC).

I also learned about Windows Settings, Control Panel, and Task Manager. These topics helped me understand how Windows systems are organised and how users can manage different system settings and processes.

## What I Learned

### 1. Windows Desktop and GUI

The Windows desktop is the main screen that appears after logging into a Windows system.

GUI stands for **Graphical User Interface**. It allows users to interact with the operating system through visual elements instead of entering commands in a terminal.

Some common elements of the Windows desktop include:

- **Desktop:** The main workspace where shortcuts and files can be placed.
- **Start Menu:** Provides access to applications, settings, and other system options.
- **Taskbar:** Displays running applications and pinned programs.
- **File Explorer:** Allows users to browse and manage files and folders.
- **System Tray:** Displays background applications, notifications, and system information.

### 2. Windows File System (NTFS) and Older File System Technology

Windows uses file systems to organise and store data on storage devices.

**NTFS (New Technology File System)** is the primary file system used by modern Windows systems.

Some important features of NTFS include:

- Supports large files and storage volumes.
- Provides file and folder permissions.
- Supports file compression.
- Supports encryption.
- Provides features that help maintain file system reliability.

Windows also has older file system technologies, such as:

- **FAT16:** An older file system used in early storage devices.
- **FAT32:** A widely supported file system, but it has a maximum individual file size of 4 GB.
- **exFAT:** Designed mainly for flash storage devices and supports large files.

### 3. Windows Folder and System32

Windows contains different folders that store system files, applications, and user data.

One important folder is:

```text
C:\Windows
```

This directory contains important files required by the Windows operating system.

Inside it, there is another important folder called:

```text
C:\Windows\System32
```

The System32 folder contains important Windows system files, including executable files, libraries, and utilities required for the operating system to function.

It is an important system directory, so deleting or modifying its files without understanding their purpose can cause problems with Windows.

### 4. User Accounts and Profiles

Windows allows multiple users to have separate accounts on the same computer.

Each user account can have its own settings, files, and permissions.

Common types of Windows user accounts include:

- **Administrator Account:** Has elevated permissions and can perform system-level tasks, install software, and change important settings.
- **Standard User Account:** Has limited permissions and can perform normal tasks without making certain system-level changes.

Windows also creates a user profile for each account.

User profiles store personal settings and information, such as desktop preferences, documents, and other user-specific data.

User profile folders are commonly located at:

```text
C:\Users
```

### 5. User Account Control (UAC)

UAC stands for **User Account Control**.

It is a Windows security feature that helps prevent unauthorised changes to the system.

When an application or user action requires administrator-level permissions, UAC displays a confirmation prompt.

For example, when installing software or changing important system settings, Windows may ask for permission before allowing the action.

UAC helps users understand when an application is requesting elevated permissions.

### 6. Settings and Control Panel

Windows provides two main interfaces for managing system configuration: Settings and Control Panel.

#### Windows Settings

Settings is the modern interface used to manage different Windows features and configurations.

It provides options for:

- System configuration.
- Network and internet settings.
- Personalisation.
- Applications.
- User accounts.
- Privacy and security.

#### Control Panel

Control Panel is an older Windows interface that provides access to different system configuration options.

It includes settings related to:

- Hardware and devices.
- User accounts.
- Network configuration.
- Programs.
- System and security.

Both Settings and Control Panel allow users to manage and configure the Windows operating system.

### 7. Task Manager

Task Manager provides information about applications and processes currently running on the Windows system.

It also displays information about system resource usage.

Some important sections of Task Manager include:

- **Processes:** Displays running applications and background processes.
- **Performance:** Shows resource usage, including CPU, RAM, disk, and network activity.
- **App History:** Displays resource usage information for applications.
- **Startup Apps:** Shows applications configured to start when Windows starts.
- **Users:** Displays users currently signed in to the system.
- **Details:** Provides detailed information about running processes.
- **Services:** Displays services running on the Windows system.

Task Manager can be opened by right-clicking the taskbar and selecting Task Manager. It can also be opened using the keyboard shortcut:

```text
Ctrl + Shift + Esc
```

It is useful for checking running applications, monitoring system performance, and managing processes.

## Practical Experience

During this room, I explored the Windows operating system and learned about its different features through the graphical user interface.

I explored:

- The Windows desktop and its GUI components.
- The Windows file system and NTFS.
- Older file system technologies such as FAT16, FAT32, and exFAT.
- Important Windows directories, including System32.
- User accounts and user profiles.
- User Account Control (UAC).
- Windows Settings and Control Panel.
- Task Manager and its different sections.

## SOC Analyst Relevance

Understanding Windows is important for a SOC Analyst because many organisations use Windows computers and servers.

The topics covered in this room help build a foundation for investigating and monitoring Windows systems.

- **Windows File System:** Helps understand where files and system information are stored.
- **System32:** Helps identify important Windows system files and directories.
- **User Accounts:** Helps understand user access and permissions during investigations.
- **UAC:** Helps understand how Windows handles requests for elevated permissions.
- **Settings and Control Panel:** Help understand how Windows system configurations are managed.
- **Task Manager:** Helps identify running processes, monitor resource usage, and investigate unusual application activity.

These concepts are useful when investigating suspicious processes, unusual system behaviour, and possible unauthorised activity on Windows machines.

## Key Takeaways

- Windows provides a graphical user interface to interact with the operating system.
- NTFS is the primary file system used by modern Windows systems.
- FAT16, FAT32, and exFAT are other file system technologies.
- `C:\Windows` contains important operating system files.
- `C:\Windows\System32` stores important Windows system files and utilities.
- Windows supports Administrator and Standard User accounts.
- User profiles store individual user settings and files.
- UAC helps prevent unauthorised system-level changes.
- Settings and Control Panel are used to manage Windows configurations.
- Task Manager displays running processes and system resource usage.

## Lab Details

- **Platform:** TryHackMe
- **Learning Path:** Cyber Security 101
- **Room:** Windows Fundamentals Part 1
- **Status:** Completed

## Disclaimer

These notes document my learning from an authorized TryHackMe lab environment and are intended for educational purposes.