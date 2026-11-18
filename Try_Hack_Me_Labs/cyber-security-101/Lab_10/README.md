# TryHackMe – Windows PowerShell

## Lab Completion Proof

![Room Completed](screenshot/room-completed.png)

*Screenshot showing successful completion of the Windows PowerShell room on TryHackMe.*

## Overview

In this room, I learned about Windows PowerShell and how it is used to manage and interact with the Windows operating system.

I explored PowerShell cmdlets, working with files and directories, piping, filtering, searching, and important comparison operators. I also learned how to collect system and network information, check running processes and services, view network connections, and calculate file hashes.

Finally, I learned the basics of PowerShell scripting, its benefits in cybersecurity, and how to execute commands remotely.

## What I Learned

### 1. Introduction to PowerShell

PowerShell is a command-line shell and scripting language developed by Microsoft. It is mainly used for system administration, automation, and managing Windows systems.

Unlike the traditional Command Prompt, PowerShell works with objects instead of only plain text.

It allows users to:
- Manage files and directories.
- Collect system information.
- Manage processes and services.
- Check network configurations.
- Automate repetitive tasks using scripts.
- Execute commands remotely.

### 2. A Brief History of PowerShell

PowerShell was introduced by Microsoft in 2006.

It was developed to provide a more powerful command-line environment for Windows administrators. Over time, PowerShell became available on multiple operating systems through PowerShell Core and the newer cross-platform PowerShell versions.

Today, PowerShell is widely used for system administration, automation, and security-related tasks.

### 3. The Power in PowerShell – Objects and Properties

One important feature of PowerShell is that it works with objects instead of just plain text.

An object contains information about something, such as a process, service, or computer.

Objects can have:

- **Properties:** Describe information about an object.
- **Methods:** Define actions that can be performed on an object.

For example, a process object can contain properties such as its name, ID, CPU usage, and memory usage.

This makes it easier to filter, sort, and select specific information.

### 4. Windows PowerShell Basic Cmdlets

A cmdlet is a lightweight command used in PowerShell to perform a specific task.

Most PowerShell cmdlets follow the naming format:

```powershell
Verb-Noun
```

For example, `Get-Process` uses `Get` as the verb and `Process` as the noun.

I learned the following basic cmdlets:

| Cmdlet | Purpose |
|---|---|
| `Get-Command` | Lists available commands in PowerShell. |
| `Get-Command -CommandType "Function"` | Lists commands that are functions. |
| `Get-Help` | Displays help information about cmdlets and commands. |
| `Get-Alias` | Displays available aliases for PowerShell commands. |
| `Find-Module` | Searches for modules in online repositories such as PowerShell Gallery. |
| `Install-Module` | Installs a PowerShell module. |

These cmdlets help users discover commands, understand how they work, and install additional functionality.

### 5. Windows PowerShell – Working with Files and Directories

PowerShell provides cmdlets to create, view, copy, move, and delete files and directories.

| Cmdlet | Purpose |
|---|---|
| `Get-ChildItem` | Lists files and directories in a location. |
| `Set-Location` | Changes the current working directory. |
| `New-Item` | Creates a new file or directory. |
| `Remove-Item` | Deletes files or directories. |
| `Copy-Item` | Copies files or directories. |
| `Move-Item` | Moves files or directories. |
| `Get-Content` | Reads and displays the contents of a file. |

These commands make file and directory management easier through the PowerShell terminal.

### 6. Windows PowerShell – Piping, Filtering and Searching

PowerShell supports piping, which allows the output of one cmdlet to be passed as input to another cmdlet using the pipe symbol `|`.

This is useful when working with large amounts of information because we can filter and select only the data we need.

I learned the following cmdlets:

| Cmdlet | Purpose |
|---|---|
| `Get-ChildItem` | Gets files and directories from a location. |
| `Sort-Object` | Sorts objects based on their properties. |
| `Where-Object` | Filters objects based on specified conditions. |
| `Select-Object` | Selects specific properties or objects. |
| `Select-String` | Searches for text or patterns inside files and input. |

**Example of piping:**

```powershell
Get-Process | Sort-Object CPU
```

This command gets running processes and sorts them based on CPU usage.

**Example of filtering:**

```powershell
Get-Process | Where-Object {$_.CPU -gt 100}
```

This command displays processes whose CPU value is greater than 100.

**Example of selecting properties:**

```powershell
Get-Process | Select-Object Name, Id, CPU
```

This command displays only the process name, ID, and CPU properties.

### 7. Important PowerShell Comparison Operators

PowerShell uses comparison operators to compare values and filter information.

| Operator | Meaning |
|---|---|
| `-eq` | Equal to |
| `-ne` | Not equal to |
| `-gt` | Greater than |
| `-ge` | Greater than or equal to |
| `-lt` | Less than |
| `-le` | Less than or equal to |
| `-like` | Matches a wildcard pattern |

**Example:**

```powershell
Get-Process | Where-Object {$_.Name -eq "notepad"}
```

This command displays the process named `notepad`.

Another example:

```powershell
Get-Process | Where-Object {$_.CPU -gt 50}
```

This command filters processes whose CPU value is greater than 50.

These operators are useful when searching for specific information or filtering command output.

### 8. Windows PowerShell – System and Network Information

PowerShell provides cmdlets to collect information about the computer, local users, and network configuration.

| Cmdlet | Purpose |
|---|---|
| `Get-ComputerInfo` | Displays detailed information about the computer and operating system. |
| `Get-LocalUser` | Lists local user accounts on the computer. |
| `Get-NetIPConfiguration` | Displays network interface configuration information. |
| `Get-NetIPAddress` | Displays IP address information for network interfaces. |

These commands help administrators understand the system configuration and identify network-related information.

### 9. Windows PowerShell – Processes, Services, Network Connections and File Hashes

PowerShell provides useful cmdlets for monitoring running processes, services, network connections, and file information.

| Cmdlet | Purpose |
|---|---|
| `Get-Process` | Lists currently running processes. |
| `Get-Service` | Lists services and their current status. |
| `Get-NetTCPConnection` | Displays current TCP network connections. |
| `Get-FileHash` | Calculates a hash value for a file. |
| `Get-Item -Stream *` | Displays available alternate data streams for a file. |

**Get-Process**

This cmdlet helps identify running applications and processes.

```powershell
Get-Process
```

**Get-Service**

This cmdlet displays Windows services and their status, such as Running or Stopped.

```powershell
Get-Service
```

**Get-NetTCPConnection**

This cmdlet helps inspect TCP connections on the system.

```powershell
Get-NetTCPConnection
```

**Get-FileHash**

This cmdlet calculates a cryptographic hash of a file. Hashes can be used to check file integrity and compare files during security investigations.

```powershell
Get-FileHash .\sample.txt
```

**Get-Item -Stream \***

Windows supports Alternate Data Streams (ADS), which allow additional data to be associated with a file.

The following command helps display the streams associated with a file:

```powershell
Get-Item -Path .\sample.txt -Stream *
```

These commands are useful for system monitoring and security investigations.

### 10. Windows PowerShell – Scripting and Remote Command Execution

**Introduction to Scripting**

Scripting is the process of writing and executing a series of commands in a file to automate tasks that would normally be performed manually.

A PowerShell script usually uses the `.ps1` file extension.

For example, instead of entering the same commands every time, we can save them in a script and execute them when required.

**Benefits of Scripting**

- Saves time by automating repetitive tasks.
- Reduces manual work.
- Helps perform multiple tasks in sequence.
- Reduces the chances of errors caused by repeated manual operations.
- Makes system administration easier.

**Importance of PowerShell Scripting in Cybersecurity**

PowerShell scripting is useful in cybersecurity because it can help security professionals:

- Collect system and network information.
- Monitor running processes and services.
- Search files and logs.
- Automate security checks.
- Gather information during incident investigations.
- Perform administrative tasks across multiple systems.

**Invoke-Command**

`Invoke-Command` is a PowerShell cmdlet used to execute commands on local or remote computers.

It is useful when administrators need to run commands on multiple systems without manually accessing each computer.

**Difference Between -FilePath and -ScriptBlock**

Both parameters are used with `Invoke-Command`, but they work differently.

| Parameter | Purpose |
|---|---|
| `-FilePath` | Specifies a PowerShell script file that is executed on the remote computer. |
| `-ScriptBlock` | Specifies PowerShell commands directly inside the command. |

**Example using -FilePath:**

```powershell
Invoke-Command -ComputerName PC01 -FilePath C:\Scripts\check.ps1
```

This executes the specified script file on the remote computer.

**Example using -ScriptBlock:**

```powershell
Invoke-Command -ComputerName PC01 -ScriptBlock {Get-Process}
```

This executes the `Get-Process` command on the remote computer.

Remote execution requires appropriate permissions and a properly configured PowerShell remoting environment.

## Practical Experience

During this lab, I practised using different PowerShell cmdlets to manage Windows systems.

I learned how to work with files and directories, filter and sort command output, and collect system and network information. I also explored processes, services, TCP connections, file hashes, and Alternate Data Streams.

Finally, I learned the basics of PowerShell scripting and how `Invoke-Command` can be used to execute commands remotely.

## SOC Analyst Relevance

PowerShell is an important tool for a SOC Analyst because it is commonly available on Windows systems and can be used for both administration and malicious activities.

- **Basic Cmdlets:** Help understand PowerShell commands and investigate command execution.
- **Files and Directories:** Help inspect files and identify suspicious files or locations.
- **Piping and Filtering:** Help search and filter large amounts of system information.
- **Comparison Operators:** Help find specific processes, users, files, or other objects.
- **System Information:** Helps collect details about the operating system and local accounts.
- **Network Information:** Helps investigate IP configurations and active TCP connections.
- **Process and Service Monitoring:** Helps identify unusual processes or suspicious services.
- **File Hashes:** Help compare files and identify known malicious files using their hash values.
- **Alternate Data Streams:** Helps investigate hidden data associated with files.
- **PowerShell Scripting:** Helps automate repetitive investigation and system-monitoring tasks.
- **Remote Command Execution:** Helps understand how commands can be executed across multiple systems and why unauthorized remote execution can be a security risk.

These concepts are useful when investigating suspicious PowerShell activity, malware execution, unusual network connections, and possible system compromise.

## Key Takeaways

- PowerShell is a command-line shell and scripting language developed by Microsoft.
- PowerShell works with objects and their properties instead of only plain text.
- Cmdlets generally follow the `Verb-Noun` naming format.
- `Get-Command`, `Get-Help`, and `Get-Alias` help users work with PowerShell commands.
- File and directory cmdlets help manage files through the terminal.
- Piping, filtering, and searching help find specific information.
- Comparison operators are used to compare values and filter objects.
- PowerShell can collect system, user, and network information.
- Process, service, and network cmdlets help monitor system activity.
- `Get-FileHash` helps verify file integrity.
- PowerShell scripting helps automate repetitive tasks.
- `Invoke-Command` supports remote command execution using `-FilePath` or `-ScriptBlock`.

## Lab Details

- **Platform:** TryHackMe
- **Learning Path:** Cyber Security 101
- **Room:** Windows PowerShell
- **Status:** Completed

## Disclaimer

These notes document my learning from an authorized TryHackMe lab environment and are intended for educational purposes.