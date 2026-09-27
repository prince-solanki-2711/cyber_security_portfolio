# Failed Login Analyzer

This is a simple Python project that I made after completing my Python basics.

The main purpose of this project is to analyze authentication log data and find failed login attempts.

I made this project to get some practical experience with Python and also to understand how Python can be used for a simple cybersecurity-related task.

## What this project does

The script reads a mock authentication log file and checks for failed password attempts.

It then:

* Finds failed login attempts
* Extracts the IP address from the log
* Counts how many times each IP address appears
* Shows IP addresses with more than 5 failed attempts
* Finds the usernames that are being targeted
* Displays the results in the terminal

## Python concepts I used

While making this project, I used:

* File handling
* `for` loops
* `if` conditions
* Dictionaries
* Regular expressions
* String searching
* Reading and processing log files

## How it works

The script reads the authentication log line by line.

First, it looks for:

```text
Failed password
```

When it finds a failed login entry, it uses a regular expression to extract the IP address.

The IP address is then stored in a dictionary and its count is increased whenever the same IP appears again.

I set the suspicious limit to:

```python
suspicious_limit = 5
```

If an IP has more than 5 failed attempts, the script displays it as a suspicious attempt.

The script also checks the username from the failed login entry and counts how many times each username was targeted.

## Example

The script can produce output similar to:

```text
===================================================================================
Failed Login Attempts
===================================================================================
192.168.1.10 → 3
192.168.1.15 → 7
192.168.1.20 → 2

Sucpicous Attempts
192.168.1.15 -> 7 Failed Attempts More Than Five Times

Targeted Username
===================================================================================
admin -> 7
test -> 3
```

The actual output depends on the data inside the log file.

## Files in this project

```text
failed_login_analyzer.py
```

The main Python script that analyzes the log file.

```text
mock_auth_data.txt
```

A sample authentication log file used for testing the script.

```text
README.md
```

This file contains information about the project.

## How to run the project

First, make sure Python is installed on your computer.

Clone the repository or download this project.

Then open the project folder in the terminal.

Run:

```bash
python failed_login_analyzer.py
```

Make sure the path to the log file in the Python script matches the location of your `mock_auth_data.txt` file.

## What I learned

This was one of my first practical Python projects.

While making it, I learned how to work with log files, search through log data, use regular expressions, store data in dictionaries, and generate a simple security-related report.

I also got a better idea of how Python can be useful in cybersecurity.

## Future improvements

There are still many things I can improve in this project.

Some of the things I would like to add later are:

* Take the log file path from the user instead of using a fixed path
* Add better error handling
* Improve the output format
* Add command-line arguments
* Generate a report automatically
* Add more log analysis features

## Project Status

This is a beginner-level project and is part of my Python and cybersecurity learning journey.

I will continue improving it as I learn more about Python, Linux, networking, and SOC operations.

## Author

Prince Solanki

Learning Python and Cybersecurity with the goal of building my skills towards the SOC / Blue Team field.
