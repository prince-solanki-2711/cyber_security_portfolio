# IOC Extraction Tool 🔎

A simple Python-based IOC (Indicator of Compromise) Extraction Tool.

I built this project while learning Python and preparing for a career in **Cybersecurity and SOC (Security Operations Center)**.

The main purpose of this project is to practice using Python to extract useful information from security log files.

---

## What is an IOC?

IOC stands for **Indicator of Compromise**.

It is a piece of information that can help identify possible malicious or suspicious activity.

Some common examples are:

* IP addresses
* URLs
* Email addresses
* File hashes

---

## What This Tool Does

This tool reads a security log file and searches for different types of IOCs.

It currently extracts:

* IP Addresses
* URLs
* Email Addresses
* File Hashes

The extracted information is then saved into a separate text file.

---

## Features

### 1. IP Address Extraction

The tool searches the log file for IPv4 addresses.

Example:

```text
192.168.1.10
10.10.10.25
172.16.0.5
```

### 2. URL Extraction

The tool searches for HTTP and HTTPS URLs.

Example:

```text
http://example.com
https://malicious-site.com/login
```

### 3. Email Extraction

The tool searches for email addresses.

Example:

```text
attacker@example.com
admin@example.com
```

### 4. File Hash Extraction

The tool searches for possible file hashes and identifies them based on their length.

It supports:

* MD5
* SHA1
* SHA256

Example:

```text
MD5    -> 5d41402abc4b2a76b9719d911017c592
SHA1   -> 7f83b1657ff1fc53b92dc18148a1d65dfa1350c6
SHA256 -> 3a7bd3e2360a3d29eea436fcfb7e44c7...
```

---

## Technologies Used

* Python
* Regular Expressions (`re`)
* File Handling
* Sets
* Dictionaries

No external Python libraries are required.

---

## Project Structure

```text
IOC-Extractor/
│
├── ioc_extractor.py
├── security_logs.txt
├── ioc_report.txt
└── README.md
```

### Files

**`ioc_extractor.py`**

Main Python program that extracts the IOCs.

**`security_logs.txt`**

Sample security log file used as input.

**`ioc_report.txt`**

Output file containing the extracted IOCs.

**`README.md`**

Project documentation.

---

## How to Run

### Step 1: Clone the repository

```bash
git clone <your-github-repository-link>
```

### Step 2: Open the project folder

```bash
cd IOC-Extractor
```

### Step 3: Run the Python script

```bash
python ioc_extractor.py
```

---

## Output

After running the program, the extracted IOCs will be saved in:

```text
ioc_report.txt
```

The report contains sections for:

```text
IP Addresses
URL Addresses
Email Addresses
File Hashes
```

The terminal also shows a completion message when the extraction is finished.

---

## What I Learned

While building this project, I learned and practiced:

* How to read data from a text file
* How to use Regular Expressions
* How to search for patterns in security logs
* How to use sets to remove duplicate IOCs
* How to use dictionaries
* How to write output into a text file
* How to use `sys.stdout` to redirect output
* Basic security log analysis using Python

---

## Disclaimer

This project is created for **learning and educational purposes**.

The log data used in this project is sample data and should not contain real sensitive information.

---

## Author

**Prince Solanki**

Currently learning Python and Cybersecurity with a focus on **SOC Analyst / Blue Team** skills.

This is one of my beginner projects as I continue learning and building practical cybersecurity projects.
