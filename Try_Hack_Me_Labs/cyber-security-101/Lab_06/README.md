# TryHackMe – Windows Fundamentals Part 2

## Lab Completion Proof

![Room Completion Screenshot](screenshot/room-completed.png)

*Screenshot showing the successful completion of the Windows Fundamentals Part 2 room on TryHackMe.*

## Overview

In this room, I continued learning about Windows system administration tools and utilities.

I explored System Configuration, Advanced System Settings, User Account Control (UAC) settings, Computer Management, System Information, Resource Monitor, Command Prompt, and Registry Editor.

These tools help users manage Windows settings, monitor system resources, troubleshoot problems, and understand how the operating system is configured.

## What I Learned

### 1. System Configuration and Advanced System Settings

System Configuration is a Windows utility used to troubleshoot and manage different startup and system settings.

It can be opened by running:

```cmd
msconfig
```

System Configuration contains different tabs:

- **General:** Allows users to select how Windows starts.
- **Boot:** Provides options related to the Windows boot process.
- **Services:** Displays services configured on the system.
- **Startup:** Provides access to startup application management through Task Manager.
- **Tools:** Provides shortcuts to different Windows utilities.

#### Advanced System Settings

Advanced System Settings provides access to additional Windows configuration options.

It includes settings related to:

- Performance.
- User Profiles.
- Startup and Recovery.
- System Protection.
- Environment Variables.

These settings help users manage advanced operating system behaviour.

### 2. Change UAC Setting

UAC stands for **User Account Control**. It is a Windows security feature that helps prevent unauthorised changes to the system.

Windows allows users to change the UAC notification level.

To access these settings, search for **Change User Account Control settings** in the Windows Start Menu.

The UAC settings include different notification levels:

- **Always notify:** Notifies the user whenever an application or user attempts to make changes that require administrator permissions.
- **Notify when apps try to make changes:** Notifies the user when applications attempt to make changes, but not when the user changes Windows settings.
- **Notify when apps try to make changes (without dimming the desktop):** Provides notifications without dimming the desktop.
- **Never notify:** Does not notify the user about these changes.

UAC helps users control applications that request elevated permissions. Lowering its notification level can reduce the security warnings shown by Windows.

### 3. Computer Management

Computer Management is a Windows utility that provides access to different system administration tools.

It can be opened by running:

```cmd
compmgmt.msc
```

Computer Management has three primary sections:

#### System Tools

This section contains tools used to manage and monitor the Windows system.

Some important tools include:

- **Task Scheduler:** Allows users to schedule tasks to run automatically at specific times or events.
- **Event Viewer:** Displays system, security, and application logs.
- **Shared Folders:** Shows shared folders and resources on the computer.
- **Local Users and Groups:** Allows administrators to manage local user accounts and groups.
- **Performance:** Provides access to system performance monitoring tools.
- **Device Manager:** Displays hardware devices installed on the system and their status.

#### Storage

This section contains tools related to storage management.

- **Disk Management:** Allows users to view and manage disks, partitions, and volumes.

#### Services and Applications

This section provides access to services and other application management options.

- **Services:** Displays services running on the Windows system and allows administrators to manage them.

### 4. System Information

System Information is a Windows utility that displays detailed information about the computer's hardware and software environment.

It can be opened by running:

```cmd
msinfo32
```

It provides information such as:

- Operating system details.
- System manufacturer and model.
- Processor information.
- BIOS information.
- Installed memory (RAM).
- Hardware resources.
- Software environment.

System Information is useful when checking the configuration and specifications of a Windows computer.

### 5. Resource Monitor

Resource Monitor is a Windows utility used to monitor how system resources are being used.

It can be opened by running:

```cmd
resmon
```

It provides information about different system resources through five main tabs:

- **Overview:** Displays a general summary of resource usage.
- **CPU:** Shows processes and services using the processor.
- **Memory:** Displays memory usage by processes.
- **Disk:** Shows disk activity and processes accessing storage.
- **Network:** Displays network activity and processes using network connections.

Resource Monitor helps users identify which processes are consuming system resources and investigate performance-related issues.

### 6. Command Prompt

Command Prompt is a command-line interface in Windows that allows users to interact with the operating system by entering commands.

It can be opened by searching for `cmd` in the Start Menu or by using the Run dialog.

Some common Command Prompt commands include:

| Command | Purpose |
|---|---|
| `whoami` | Displays the current logged-in username. |
| `hostname` | Displays the computer's hostname. |
| `ipconfig` | Displays network configuration information. |
| `dir` | Lists files and directories. |
| `cd` | Changes the current directory. |
| `systeminfo` | Displays detailed system information. |
| `tasklist` | Displays currently running processes. |
| `cls` | Clears the Command Prompt screen. |

Command Prompt is useful for performing administrative tasks and gathering system information.

### 7. Registry Editor

The Windows Registry is a central hierarchical database used to store configuration information for Windows, applications, users, and hardware devices.

Windows continuously refers to the Registry during system operation.

It stores information such as:

- User profiles.
- Installed applications.
- Hardware configuration.
- System settings.
- Application settings.
- File and folder-related settings.

Registry Editor is the Windows utility used to view and modify Registry entries.

It can be opened by running:

```cmd
regedit
```

The Registry is organised into different keys and subkeys.

Some important Registry root keys include:

- **HKEY_CLASSES_ROOT (HKCR):** Contains information about file associations and registered object classes.
- **HKEY_CURRENT_USER (HKCU):** Contains configuration settings for the currently logged-in user.
- **HKEY_LOCAL_MACHINE (HKLM):** Contains system-wide configuration information.
- **HKEY_USERS (HKU):** Contains information about user profiles loaded on the system.
- **HKEY_CURRENT_CONFIG (HKCC):** Contains information about the current hardware profile.

**Important point:** Changes to the Registry can affect how Windows operates. Incorrect modifications may cause system problems, so Registry entries should be changed carefully.

## Practical Experience

During this room, I explored different Windows utilities and learned how they help manage and monitor the operating system.

I practised:

- Opening System Configuration using `msconfig`.
- Exploring the General, Boot, Services, Startup, and Tools sections.
- Understanding Advanced System Settings.
- Exploring different UAC notification levels.
- Opening Computer Management using `compmgmt.msc`.
- Exploring System Tools, Storage, and Services and Applications.
- Viewing system details using `msinfo32`.
- Monitoring CPU, memory, disk, and network usage using Resource Monitor.
- Using basic commands in Command Prompt.
- Opening Registry Editor using `regedit`.
- Understanding the main Registry root keys.

## SOC Analyst Relevance

Understanding Windows administration tools is useful for a SOC Analyst because these utilities provide information about system configuration, user activity, running processes, and system behaviour.

- **System Configuration:** Helps understand startup settings and services configured on a Windows system.
- **UAC:** Helps understand permission requests and attempts to perform administrative actions.
- **Computer Management:** Provides access to tools such as Event Viewer, Task Scheduler, and Local Users and Groups.
- **System Information:** Helps identify operating system, hardware, and software details.
- **Resource Monitor:** Helps investigate unusual CPU, memory, disk, and network activity.
- **Command Prompt:** Helps gather system information and investigate running processes.
- **Registry Editor:** Helps understand Windows configuration and investigate changes to Registry entries.

These tools are useful during Windows security investigations, especially when checking suspicious processes, user accounts, startup configurations, and system changes.

## Key Takeaways

- System Configuration can be opened using `msconfig`.
- Advanced System Settings provides access to performance, user profile, startup, recovery, and environment variable settings.
- UAC helps control applications requesting administrator-level permissions.
- Computer Management can be opened using `compmgmt.msc`.
- Computer Management contains System Tools, Storage, and Services and Applications.
- System Information can be opened using `msinfo32`.
- Resource Monitor can be opened using `resmon`.
- Resource Monitor helps monitor CPU, memory, disk, and network usage.
- Command Prompt allows users to interact with Windows through commands.
- The Windows Registry stores important system and application configuration information.
- Registry Editor can be opened using `regedit`.
- Registry changes should be made carefully because incorrect changes can affect Windows functionality.

## Lab Details

- **Platform:** TryHackMe
- **Learning Path:** Cyber Security 101
- **Room:** Windows Fundamentals Part 2
- **Status:** Completed

## Disclaimer

These notes document my learning from an authorized TryHackMe lab environment and are intended for educational purposes.