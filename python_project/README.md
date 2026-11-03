# Python Cybersecurity Projects

This folder contains small Python projects that I built while learning Python and exploring how it can be used for cybersecurity tasks.

I am an MCA student specialising in Cyber Security, and I am working towards becoming a SOC Analyst. These projects help me practise Python by working with sample security logs, extracting useful information, and checking indicators with a threat-intelligence service.

Each project has its own folder with a README file, source code, and sample input or output files where applicable. Open a project folder to read its documentation and learn how to run it.

## Projects

### 1. Failed Login Analyzer

**Folder:** [`failed_login_analyzer/`](failed_login_analyzer/)

This script reads sample authentication logs and looks for failed password attempts. It extracts source IP addresses, counts repeated failed attempts, highlights IPs that pass the configured threshold, and counts the usernames being targeted.

**What I practised:**
- Reading and processing text log files
- Searching for patterns in log entries
- Using regular expressions
- Working with loops, conditions, and dictionaries
- Counting failed attempts by IP address and username

### 2. IOC Extraction Tool

**Folder:** [`IOC_Extraction_Tool/`](IOC_Extraction_Tool/)

This tool scans a security log file and extracts common Indicators of Compromise (IOCs), including IP addresses, URLs, email addresses, and file hashes. It saves the extracted information in a report file.

**What I practised:**
- Understanding common types of IOCs
- Using regular expressions to find patterns
- Reading input files and writing report files
- Using sets to avoid duplicate results
- Organising extracted information

### 3. IP Reputation Checker

**Folder:** [`IP_repuatation checker/`](IP_repuatation%20checker/)

This tool accepts one or more IP addresses and checks them using the VirusTotal API. It displays available network information and threat-intelligence results, such as malicious, suspicious, harmless, and undetected counts.

This project can also be used after the IOC Extraction Tool: IP addresses found in a log file can be checked separately with the reputation checker.

**What I practised:**
- Making API requests with Python's `requests` library
- Working with JSON responses
- Reading values from nested JSON data
- Validating IP addresses
- Using environment variables to store an API key
- Handling user input and basic errors

**Note:** A VirusTotal result is one source of threat-intelligence information. It should be reviewed with other context and should not be treated as a final verdict on its own. Keep your API key private and do not upload it to GitHub.

### 4. Brute Force Detection

**Folder:** [`Brute_Force_Detection/`](Brute_Force_Detection/)

This script analyses sample SSH login events and looks for patterns that may indicate brute-force attempts or password spraying. It counts failed attempts, applies simple time-based detection rules, displays a summary, and saves detected alerts in a JSON file.

**What I practised:**
- Reading and validating log entries
- Working with timestamps
- Grouping login events by source IP and username
- Detecting repeated activity using simple rules
- Creating and saving JSON output

The detection rules are basic learning examples. An alert means that the activity may need further review; it does not prove that an attack has occurred.

## How the Projects Connect

The IOC Extraction Tool and IP Reputation Checker can be used together as a simple investigation workflow:

```text
Security Log File
       |
       v
IOC Extraction Tool
       |
       v
Extracted IP Addresses
       |
       v
IP Reputation Checker
       |
       v
VirusTotal Threat-Intelligence Results
       |
       v
Review the results with additional context
```

The Failed Login Analyzer and Brute Force Detection projects focus on different ways to review authentication activity and identify patterns that may deserve investigation.

## Tools and Technologies

- **Language:** Python
- **Python modules and libraries:** `re`, `json`, `ipaddress`, `requests`, and other Python standard-library features used in the scripts
- **External service:** VirusTotal API (for the IP Reputation Checker)
- **Input and output:** Sample text log files, text reports, and JSON files

## How to Use This Folder

1. Open the folder of the project you want to explore.
2. Read that project's `README.md` for its requirements and instructions.
3. Keep the script and its required sample input files together, as described in the project README.
4. Install any required dependency before running the script. The IP Reputation Checker requires `requests` and a VirusTotal API key.
5. Run the command shown in that project's README from its project folder.

## What I Learned

Building these projects helped me practise using Python for basic cybersecurity tasks. I gained experience working with log files, searching for patterns, extracting IOCs, checking IP reputation through an API, analysing login activity, and saving results in report formats.

These are beginner-level projects created for learning and practice. They use sample data and simple detection logic; they are not connected to a live SOC or intended to replace professional security tools.

## What's Next

I plan to keep improving these projects and build more practical tools as I learn. My goal is to strengthen my Python skills and develop a better understanding of the tasks involved in SOC operations, such as log analysis, threat-intelligence checks, security monitoring, and incident investigation.

---

*Created and maintained as part of my Python and cybersecurity learning journey.*

