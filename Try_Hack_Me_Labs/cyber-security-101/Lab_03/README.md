# TryHackMe – Linux Fundamentals Part 2

## Lab Completion Proof

![Room Completion Screenshot](screenshot/room-completed.png)

*Screenshot showing the successful completion of the Linux Fundamentals Part 2 room on TryHackMe.*

## Overview

In this room, I continued learning about Linux and explored more commands and features used in the Linux terminal.

I learned about SSH, command arguments, hidden files and folders, Linux help options, and manual pages. I also explored how to create, move, copy, and delete files and directories.

Along with this, I learned about the Linux file system structure, important directories, file permissions, users and groups, and how to switch between users using the `su` command.

## What I Learned

### 1. What Is SSH?

SSH stands for **Secure Shell**. It is a network protocol used to connect securely to another computer over a network.

It allows users to access and manage a remote system through a command-line interface.

### 2. Why Is SSH Used?

SSH is used when we need to access or manage a remote Linux machine.

It provides a secure connection between the local machine and the remote machine.

Some common uses of SSH include:

- Remotely accessing Linux servers.
- Executing commands on remote systems.
- Managing servers without physical access.
- Transferring files securely.

**Example:**

```bash
ssh username@ip_address
```

This command attempts to connect to a remote machine using the specified username and IP address.

### 3. What Are Command Arguments?

Command arguments are additional values provided with a command to control what it does or specify the target on which it should operate.

**Example:**

```bash
ls -l
```

Here:
- `ls` is the command.
- `-l` is an argument that displays files in a detailed list format.

Arguments help us use commands in different ways and perform specific tasks.

### 4. What Are Hidden Files and Folders?

In Linux, files and directories whose names begin with a dot (`.`) are treated as hidden files or directories.

They are not displayed by the normal `ls` command.

To display hidden files and directories, we can use:

```bash
ls -a
```

**Example:**

```text
.bashrc
.profile
.config
```

Hidden files are commonly used to store configuration settings and other information.

### 5. The `--help` Argument

Many Linux commands provide a `--help` argument that displays information about how to use the command.

It shows available options and arguments.

**Example:**

```bash
ls --help
```

This displays the help information for the `ls` command.

It is useful when we want to understand the available features of a command.

### 6. Introduction to Linux Manual Pages (MAN Pages)

Linux provides manual pages, commonly called MAN pages, to explain commands and their usage.

The `man` command is used to open the manual page of a particular command.

**Example:**

```bash
man ls
```

This displays the manual page for the `ls` command.

MAN pages provide information such as:

- Command descriptions.
- Available options.
- Command usage.
- Additional details about the command.

They are useful when we want to learn more about a Linux command.

### 7. Linux File System: Creating, Moving, Copying and Deleting Files

Linux provides different commands to manage files and directories.

#### Creating Files – `touch`

The `touch` command is used to create an empty file.

```bash
touch file.txt
```

#### Creating Directories – `mkdir`

The `mkdir` command is used to create a new directory.

```bash
mkdir myfolder
```

#### Moving Files – `mv`

The `mv` command is used to move a file or directory from one location to another.

```bash
mv file.txt /home/user/Documents/
```

#### Copying Files – `cp`

The `cp` command is used to create a copy of a file.

```bash
cp file.txt copy.txt
```

#### Deleting Files – `rm`

The `rm` command is used to delete files.

```bash
rm file.txt
```

#### Deleting Directories

The `rmdir` command can be used to remove an empty directory.

```bash
rmdir myfolder
```

These commands help us manage files and directories through the Linux terminal.

### 8. Linux File System Structure – Important Directories

Linux uses a hierarchical file system structure. It contains different directories, and each directory has a specific purpose.

Some important Linux directories include:

| Directory | Purpose |
|---|---|
| `/` | The root directory and starting point of the Linux file system. |
| `/home` | Contains personal directories of regular users. |
| `/root` | Home directory of the root user. |
| `/etc` | Contains system configuration files. |
| `/var` | Stores variable data such as logs. |
| `/tmp` | Used for temporary files. |
| `/bin` | Contains essential user command binaries. |
| `/sbin` | Contains system administration commands. |
| `/usr` | Contains user applications, utilities, and related files. |

Understanding these directories helps us know where different types of files and information are stored in Linux.

### 9. What Does Root Mean?

In Linux, the term `root` can refer to two different things:

- **Root directory (`/`):** The starting point of the entire Linux file system.
- **Root user:** The administrator account that has the highest level of permissions on the system.

The root user has permission to perform administrative tasks and access or modify protected system files.

### 10. Understanding the File System Like a Tree

The Linux file system follows a hierarchical structure that can be understood like a tree.

The root directory (`/`) is at the top, and other directories and files exist under it.

For example:

```text
/
├── home
│   ├── user
│   │   ├── Documents
│   │   └── Downloads
├── etc
├── var
├── tmp
└── root
```

This structure helps us understand how directories are organised and how files are located in Linux.

### 11. Linux Fundamentals – File Permissions and Switching Between Users

Linux supports multiple users, and each user can have different permissions.

File permissions control who can read, modify, or execute a file or directory.

Understanding permissions and user access is important when working with Linux systems.

### 12. Introduction to File Permissions

Linux uses file permissions to control access to files and directories.

We can view file permissions using:

```bash
ls -l
```

The output displays information about files, including their permissions.

For example:

```text
-rwxr-xr--
```

This permission string describes which users can read, write, or execute the file.

### 13. Types of File Permissions

Linux has three main types of file permissions:

| Permission | Symbol | Meaning |
|---|---|---|
| Read | `r` | Allows reading a file or listing directory contents. |
| Write | `w` | Allows modifying a file or changing directory contents. |
| Execute | `x` | Allows executing a file or accessing a directory. |

These permissions are assigned to three categories:

- **User (u):** The owner of the file.
- **Group (g):** Users who belong to the file's group.
- **Others (o):** Everyone else.

For example, in `-rwxr-xr--`:

- Owner: `rwx` – read, write, and execute.
- Group: `r-x` – read and execute.
- Others: `r--` – read only.

### 14. Difference Between Users and Groups

Linux uses users and groups to manage access to files and directories.

**Users:**

A user represents an individual account on a Linux system. Each user can have their own permissions and access.

**Groups:**

A group is a collection of users. Groups make it easier to manage permissions for multiple users.

For example, instead of giving the same permission to each user separately, permissions can be assigned to a group.

### 15. Switching Between Users in Linux

Linux allows users to switch from one user account to another.

This is useful when we need to perform tasks using a different account or check how permissions work for different users.

The `su` command is commonly used for switching between users.

### 16. Using the `su` Command

The `su` command stands for **Switch User**. It allows us to switch to another user account.

**Example:**

```bash
su username
```

This attempts to switch to the specified user.

To switch to the root user:

```bash
su root
```

After switching users, the commands we execute will run under the new user's account and permissions.

## Practical Experience

During this room, I got hands-on experience with different Linux commands and learned how to manage files, directories, users, and permissions.

I practised:

- Connecting to remote systems using SSH.
- Using command arguments and `--help`.
- Viewing hidden files and directories using `ls -a`.
- Reading command documentation using `man`.
- Creating files using `touch`.
- Creating directories using `mkdir`.
- Moving files using `mv`.
- Copying files using `cp`.
- Deleting files using `rm`.
- Understanding important Linux directories.
- Checking file permissions using `ls -l`.
- Understanding read, write, and execute permissions.
- Learning the difference between users and groups.
- Switching between users using `su`.

## SOC Analyst Relevance

Linux knowledge is important for a SOC Analyst because many servers, security tools, and systems use Linux.

The topics covered in this room are useful during security investigations.

- **SSH:** Helps understand remote access to Linux systems.
- **Command arguments and MAN pages:** Help SOC Analysts understand and use Linux commands.
- **File management:** Helps locate and manage files during investigations.
- **Linux directories:** Helps identify where system configuration files and logs may be stored.
- **File permissions:** Helps understand access control and identify potentially incorrect permissions.
- **Users and groups:** Helps investigate user accounts and understand access privileges.
- **Switching users:** Helps understand how different user accounts and permissions work.

These concepts provide a stronger foundation for working with Linux systems during SOC operations.

## Key Takeaways

- SSH is used to securely access remote systems.
- Command arguments provide additional options and functionality to commands.
- Hidden files and directories start with a dot (`.`).
- `--help` displays information about command usage.
- `man` opens Linux manual pages.
- `touch` creates files.
- `mkdir` creates directories.
- `mv` moves files and directories.
- `cp` copies files.
- `rm` deletes files.
- Linux uses a hierarchical file system structure.
- The root directory (`/`) is the starting point of the file system.
- The root user has administrative privileges.
- Linux permissions include read (`r`), write (`w`), and execute (`x`).
- Users and groups help manage access to files and directories.
- `su` is used to switch between user accounts.

## Lab Details

- **Platform:** TryHackMe
- **Learning Path:** Cyber Security 101
- **Room:** Linux Fundamentals Part 2
- **Status:** Completed

## Disclaimer

These notes document my learning from an authorized TryHackMe lab environment and are intended for educational purposes.