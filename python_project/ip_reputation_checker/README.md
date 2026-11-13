# IP Reputation Checker

A simple Python-based **IP Reputation Checker** that uses the **VirusTotal API** to check an IP address and display useful threat intelligence information.

This project is part of my learning journey toward becoming a **SOC Analyst**. I built this project to practice Python concepts that can be useful in security automation and SOC-related tasks.

## What does this project do?

The tool takes one or multiple IP addresses from the user and checks their reputation using the VirusTotal API.

It displays:

### Network Information

* IP Address
* Country
* Organization
* ASN
* Reputation Score

### Threat Intelligence

* Malicious detections
* Suspicious detections
* Harmless detections
* Undetected results

Finally, the tool gives an overall result:

* Malicious
* Suspicious
* Good reputation

## Project Workflow

The basic workflow is:

```text
User enters IP address
        ↓
Validate IP address
        ↓
Send request to VirusTotal API
        ↓
Receive JSON response
        ↓
Extract required information
        ↓
Display network information
        ↓
Display threat intelligence
        ↓
Give overall reputation result
```

## Connecting This Project With My IOC Extractor

I also wanted to connect this project with my previous **IOC Extraction Tool**.

My IOC Extractor reads a security log file and extracts different types of Indicators of Compromise (IOCs), such as:

* IP addresses
* URLs
* Email addresses
* File hashes

The IP addresses extracted by the IOC Extractor can then be checked using this IP Reputation Checker.

The combined workflow looks like this:

```text
Security Log
     ↓
IOC Extractor
     ↓
Extract IP Address
     ↓
IP Reputation Checker
     ↓
VirusTotal API
     ↓
Threat Intelligence Information
     ↓
Malicious / Suspicious / Good Reputation
```

For example, if the IOC Extractor finds:

```text
185.XXX.XXX.XXX
```

I can take that IP address and provide it to the IP Reputation Checker. The tool then sends the IP to VirusTotal and displays the available reputation and threat intelligence information.

This makes the two projects more connected to a real SOC-style workflow instead of being completely separate scripts.

## Technologies Used

* Python
* Requests
* VirusTotal API
* JSON
* Regular Expressions
* Environment Variables

## Python Concepts Practiced

While building this project, I practiced:

* Making API requests using `requests`
* Working with JSON responses
* Using environment variables
* Validating IP addresses with `ipaddress`
* Using dictionaries
* Using loops
* Handling user input
* Basic exception handling
* Extracting nested data from JSON

## Requirements

Make sure Python is installed on your system.

Install the required library:

```bash
pip install requests
```

## VirusTotal API Key

This project requires a VirusTotal API key.

The API key is stored as an environment variable instead of directly writing it inside the Python code.

The variable used in the project is:

```text
VT_API_KEY
```

### Windows PowerShell

Set the environment variable:

```powershell
$env:VT_API_KEY="YOUR_API_KEY"
```

You can check whether it is available with:

```powershell
$env:VT_API_KEY
```

**Do not upload your API key to GitHub.**

## How to Run

Clone the repository and move into the project directory.

Then run:

```bash
python ip_reputation_checker.py
```

The program will ask:

```text
Enter IP addresses separated by commas:
```

You can enter one IP:

```text
8.8.8.8
```

Or multiple IP addresses:

```text
8.8.8.8, 1.1.1.1, 192.168.1.1
```

The program will check each IP address one by one.

## Example Output

```text
==========================================
           IP Reputation Checker
==========================================

 IP Address : x.x.x.x

------------Network Information------------

 Country : XX
 Organization : Example Organization
 ASN : XXXXX
 Reputation Score : XX

------------Threat Intelligence------------

 Malicious : X
 Suspicious : X
 Harmless : X
 Undetected : X

------------Reputation------------

This IP address is flagged as malicious.

----------------------------------
```

The exact information will depend on the IP address and the data returned by VirusTotal.

## Project Purpose

The main purpose of this project is not just to create an IP checker.

I built it to understand how Python can be used for **security automation and threat intelligence**.

As someone preparing for a **SOC Analyst** role, I want to become comfortable with tasks such as:

* Working with security logs
* Extracting IOCs
* Investigating IP addresses
* Using threat intelligence sources
* Understanding API responses
* Automating repetitive security tasks

## My Previous Projects

This project is part of a small collection of SOC-focused Python projects I am building while learning Python.

### 1. Failed Login Analyzer

Analyzes failed login attempts from security logs and helps identify suspicious login activity.

### 2. IOC Extractor

Extracts different IOCs from security logs, including:

* IP addresses
* URLs
* Email addresses
* File hashes

### 3. IP Reputation Checker

Takes an IP address and checks its reputation using the VirusTotal API.

The projects can also be connected together:

```text
Failed Login Analyzer
          ↓
    Security Logs
          ↓
     IOC Extractor
          ↓
      IP Address
          ↓
 IP Reputation Checker
          ↓
   VirusTotal API
          ↓
 Threat Intelligence
```

## What I Learned

This project helped me understand that Python can be very useful in cybersecurity.

Instead of only learning Python syntax, I am trying to use Python to solve small security-related problems.

My next goal is to continue building more practical projects and improve my skills in:

* Python
* Linux
* Networking
* SIEM
* Threat Intelligence
* Log Analysis
* SOC Operations

This project is one more step in my journey toward becoming a **SOC Analyst**.

Disclaimer

The information returned by VirusTotal is based on its available threat intelligence and security analysis. It may not always be completely accurate or up to date.

A malicious or suspicious result does not always mean that an IP address is harmful, and a clean result does not guarantee that an IP address is completely safe.

This project is created for learning and security analysis purposes only. The results should be treated as an additional source of information and should be verified with other security sources before making any security decision.
