# TryHackMe – Linux Shells

## Lab Completion Proof

![Room Completed](screenshot/room-completed.png)

*Screenshot showing successful completion of the Linux Shells room on TryHackMe.*

## Overview

In this room, I learned about Linux shells and how to interact with a Linux system using the Command Line Interface (CLI). I explored the difference between GUI and CLI, what a shell is, and how Bash works.

I also practised basic Linux commands, learned how to check and switch between different shells, and explored shell scripting. I covered variables, user input, loops, conditions, comments, and created a small locker authentication script to combine all these concepts.

## What I Learned

### 1. Introduction to CLI and GUI

There are two common ways to interact with a computer:

- **Graphical User Interface (GUI):** Allows users to interact with a computer using windows, icons, menus, and buttons.
- **Command Line Interface (CLI):** Allows users to interact with a computer by entering text-based commands in a terminal.

CLI is useful for system administration, automation, troubleshooting, and managing Linux systems.

### 2. What is a Shell?

A shell is a program that acts as an interface between the user and the operating system.

It accepts commands from the user, passes them to the operating system for execution, and displays the results.

For example, when we enter a command such as `ls`, the shell executes it and displays the files and directories in the current location.

### 3. Introduction to Bash

Bash stands for **Bourne Again Shell**.

It is one of the most commonly used shells in Linux systems. Bash allows users to execute commands, manage files, and write scripts to automate tasks.

It supports:
- Variables
- User input
- Loops
- Conditional statements
- Functions
- Command execution and automation

### 4. Basic Linux Commands

I revised some important Linux commands used to navigate directories, view files, and search for information.

| Command | Purpose |
|---|---|
| `pwd` | Displays the current working directory. |
| `cd` | Changes the current directory. |
| `ls` | Lists files and directories. |
| `cat` | Displays the contents of a file. |
| `grep` | Searches for specific text or patterns inside files or command output. |

These commands are useful for navigating the Linux filesystem and working with files through the terminal.

### 5. Introduction to Linux Shells

Linux supports different types of shells. Each shell provides a command-line environment where users can interact with the operating system.

Some commonly available shells include:

- **Bash:** Bourne Again Shell, commonly used in Linux.
- **Sh:** Bourne Shell, an older Unix shell.
- **Zsh:** Z Shell, an extended shell with additional features.
- **Fish:** Friendly Interactive Shell, designed to be user-friendly.
- **Ksh:** KornShell, another Unix shell.

Different shells provide different features, but they all allow users to execute commands.

**Checking the Current Shell**

The following command displays the current shell configured for the user:

```bash
echo $SHELL
```

**Listing Available Shells**

The following command displays the shells available on the system:

```bash
cat /etc/shells
```

**Switching Between Shells**

We can switch to another installed shell by entering its name.

For example:

```bash
bash
```

This starts a Bash shell.

To return to the previous shell, we can use:

```bash
exit
```

**Permanently Changing the Default Shell**

The `chsh` command is used to change the default login shell of a user.

Example:

```bash
chsh -s /bin/bash
```

This sets Bash as the default login shell, provided the shell is installed and the user has permission to make the change.

### 6. What is Shell Scripting?

Shell scripting is the process of writing multiple shell commands in a file so they can be executed together.

A shell script helps automate tasks that would otherwise require entering commands manually.

Shell scripts commonly use the `.sh` file extension.

**Benefits of Shell Scripting**

- Automates repetitive tasks.
- Saves time and effort.
- Reduces manual work.
- Helps execute multiple commands in sequence.
- Makes system administration easier.

### 7. Creating Your First Shell Script

To create a shell script, we can use a text editor such as Nano.

Example:

```bash
nano first_script.sh
```

After writing the script, save the file and give it execute permission:

```bash
chmod +x first_script.sh
```

We can execute it using:

```bash
./first_script.sh
```

### 8. Shebang

The shebang is the first line of a shell script. It tells the operating system which interpreter should be used to execute the script.

For a Bash script, we use:

```bash
#!/bin/bash
```

This tells the system to execute the script using Bash.

### 9. Variables

Variables are used to store information that can be accessed and modified during script execution.

Example:

```bash
#!/bin/bash

name="John"
age=25

echo "My name is $name"
echo "My age is $age"
```

In this example:
- `name` stores the value `John`.
- `age` stores the value `25`.
- `$name` and `$age` are used to access the stored values.

### 10. Taking Input from the User

The `read` command is used to take input from the user and store it in a variable.

Example:

```bash
#!/bin/bash

echo "Enter your name:"
read name

echo "Welcome, $name!"
```

Here, the script asks the user to enter their name and stores the input in the `name` variable.

### 11. Loops

Loops are used to execute a set of commands repeatedly.

I learned how loops can be used to repeat tasks without writing the same commands multiple times.

**For Loop**

A `for` loop runs through a list of values.

Example:

```bash
#!/bin/bash

for i in 1 2 3 4 5
do
    echo "Number: $i"
done
```

**While Loop**

A `while` loop continues executing as long as the given condition is true.

Example:

```bash
#!/bin/bash

count=1

while [ $count -le 5 ]
do
    echo "Count: $count"
    count=$((count + 1))
done
```

### 12. Conditional Statements

Conditional statements allow a script to make decisions based on whether a condition is true or false.

The `if`, `else`, and `elif` statements are commonly used in Bash.

Example:

```bash
#!/bin/bash

echo "Enter your age:"
read age

if [ "$age" -ge 18 ]
then
    echo "You are an adult."
else
    echo "You are not an adult."
fi
```

In this example, the script checks the user's age and displays a different message depending on the result.

### 13. Comments

Comments are used to explain what a script or a particular command does.

Bash uses the `#` symbol for comments.

Example:

```bash
#!/bin/bash

# Store the user's name
name="John"

# Display the name
echo "$name"
```

Comments are ignored during script execution and help make scripts easier to understand.

### 14. Practical Project – Locker Authentication Script

To revise the shell scripting concepts, I created a small locker authentication script.

The idea was to create a simple bank locker system where a user must enter the correct name, company name, and PIN to access the locker.

The script combines:
- Shebang
- Variables
- User input
- Conditional statements
- Loops
- Comments

**Script:**

```bash
#!/bin/bash

# Store the correct login details
correct_name="John"
correct_company="TryHackMe"
correct_pin="1234"

# Ask the user for login details
echo "Enter your name:"
read name

echo "Enter your company name:"
read company

echo "Enter your PIN:"
read pin

# Check the entered details
if [ "$name" = "$correct_name" ] && [ "$company" = "$correct_company" ] && [ "$pin" = "$correct_pin" ]
then
    echo "Authentication successful!"
    echo "Welcome! Your locker is now open."

else
    echo "Authentication failed!"
    echo "Incorrect login details."
fi
```

**How the Script Works:**

1. First, the script stores the correct name, company name, and PIN in variables.
2. It asks the user to enter their name, company name, and PIN.
3. The `read` command stores the entered details in variables.
4. The `if` condition checks whether all three entered values match the stored values.
5. If all details are correct, the script displays an authentication success message.
6. Otherwise, it displays an authentication failure message.

This project helped me understand how different shell scripting concepts work together in a single script.

*Note: This is a basic learning project. The PIN is stored directly in the script, so it is not suitable for real authentication systems.*

## Practical Experience

During this lab, I practised using Linux commands and explored different types of shells.

I learned how to check the current shell, list available shells, switch between shells, and change the default login shell.

I also created and executed Bash scripts using variables, user input, loops, conditions, and comments. Finally, I built a small locker authentication script to combine and revise the concepts I learned.

## SOC Analyst Relevance

Understanding Linux shells and shell scripting is useful for a SOC Analyst because Linux systems are commonly used in servers, security tools, and network infrastructure.

- **CLI and Shell:** Helps interact with Linux systems during investigations.
- **Basic Linux Commands:** Helps navigate directories, inspect files, and search for information.
- **Bash:** Helps understand how commands are executed in Linux environments.
- **Shell Information:** Helps identify which shell is being used on a system.
- **Shell Scripting:** Helps automate repetitive security tasks.
- **Variables and User Input:** Helps understand how scripts collect and process information.
- **Loops and Conditions:** Helps create scripts that perform repeated checks and make decisions.
- **Locker Authentication Project:** Helps understand basic authentication logic and how user-provided information can be checked.

These concepts provide a foundation for writing simple automation scripts and understanding shell activity during security investigations.

## Key Takeaways

- GUI and CLI are two different ways to interact with a computer.
- A shell acts as an interface between the user and the operating system.
- Bash is one of the most commonly used Linux shells.
- Commands such as `pwd`, `cd`, `ls`, `cat`, and `grep` are useful for everyday Linux operations.
- Linux provides different shells, and users can check or change their default shell.
- Shell scripting helps automate repetitive tasks.
- The shebang specifies the interpreter used to execute a script.
- Variables store information, and `read` accepts input from users.
- Loops repeat commands, while conditions help scripts make decisions.
- Comments make scripts easier to understand.
- The locker authentication project helped me combine the main shell scripting concepts into one practical example.

## Lab Details

- **Platform:** TryHackMe
- **Learning Path:** Cyber Security 101
- **Room:** Linux Shells
- **Status:** Completed

## Disclaimer

These notes document my learning from an authorized TryHackMe lab environment and are intended for educational purposes.