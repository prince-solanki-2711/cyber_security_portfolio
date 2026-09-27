# ============================================================
# 1. IMPORT MODULES
# ============================================================

import re
import sys


# ============================================================
# 2. OPEN THE SECURITY LOG FILE
# ============================================================

# Open the security log file in read mode
file_handler = open("security_logs.txt", "rt")

# Read all the data from the log file
data = file_handler.read()


# ============================================================
# 3. CREATE OUTPUT FILE
# ============================================================

# Create a text file where the IOC report will be saved
output_file = open("ioc_report.txt", "w")

# Save the original terminal output
original_stdout = sys.stdout

# Redirect all print() output to the report file
sys.stdout = output_file


# ============================================================
# 4. CHECK FILE
# ============================================================

# Check whether the file was opened successfully
if file_handler:
    print("Found")
else:
    print("Not Found")


# ============================================================
# 5. CREATE DICTIONARIES FOR IOC COUNTING
# ============================================================

ip_counts = {}
url_counts = {}
email_counts = {}
hash_count = {}


# ============================================================
# 6. DEFINE REGEX PATTERNS
# ============================================================

# Pattern for finding IPv4 addresses
ip_pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"

# Pattern for finding HTTP and HTTPS URLs
url_pattern = r"https?://[^\s]+"

# Pattern for finding email addresses
email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"

# Pattern for finding possible file hashes
# Supports MD5, SHA1 and SHA256 length hashes
hash_pattern = r"\b[a-fA-F0-9]{32,64}\b"


# ============================================================
# 7. EXTRACT IOCs FROM LOG FILE
# ============================================================

# Find IP addresses and remove duplicate values
ip_find = set(re.findall(ip_pattern, data))

# Find URLs and remove duplicate values
url_find = set(re.findall(url_pattern, data))

# Find email addresses and remove duplicate values
email_find = set(re.findall(email_pattern, data))

# Find file hashes and remove duplicate values
hash_find = set(re.findall(hash_pattern, data))


# ============================================================
# 8. DISPLAY TOOL HEADER
# ============================================================

print("===========================================================")
print("                 IOC EXTRACTION TOOL")
print("===========================================================")
print()


# ============================================================
# 9. DISPLAY IP ADDRESSES
# ============================================================

print("===========================================================")
print("IP Addresses")
print("===========================================================")

# Go through every extracted IP address
for ip in ip_find:

    # Add the IP address to the dictionary
    if ip in ip_counts:
        ip_counts[ip] += 1
    else:
        ip_counts[ip] = 1

    # Print the IP address
    print(ip)

# Display total number of unique IP addresses
print("===========================================================")
print(f"Total IP : {len(ip_counts)}")
print()


# ============================================================
# 10. DISPLAY URL ADDRESSES
# ============================================================

print("===========================================================")
print("URL Addresses")
print("===========================================================")

# Go through every extracted URL
for url in url_find:

    # Add the URL to the dictionary
    if url in url_counts:
        url_counts[url] += 1
    else:
        url_counts[url] = 1

    # Print the URL
    print(url)

# Display total number of unique URLs
print("===========================================================")
print(f"Total URL : {len(url_counts)}")
print()


# ============================================================
# 11. DISPLAY EMAIL ADDRESSES
# ============================================================

print("===========================================================")
print("Email Addresses")
print("===========================================================")

# Go through every extracted email address
for email in email_find:

    # Add the email to the dictionary
    if email in email_counts:
        email_counts[email] += 1
    else:
        email_counts[email] = 1

    # Print the email address
    print(email)

# Display total number of unique email addresses
print("===========================================================")
print(f"Total Email : {len(email_counts)}")
print()


# ============================================================
# 12. DISPLAY FILE HASHES
# ============================================================

print("===========================================================")
print("File Hashes")
print("===========================================================")

# Go through every extracted hash
for hashfiles in hash_find:

    # Identify the hash type based on its length
    if len(hashfiles) <= 32:
        print(f"MD5 -> {hashfiles}")

    elif len(hashfiles) <= 40:
        print(f"SHA1 -> {hashfiles}")

    else:
        print(f"SHA256 -> {hashfiles}")


# ============================================================
# 13. COUNT HASHES
# ============================================================

# Go through every extracted hash
for hashfiles in hash_find:

    # Increase the count if the hash already exists
    if hashfiles in hash_count:
        hash_count[hashfiles] += 1

    # Otherwise, add the hash with count 1
    else:
        hash_count[hashfiles] = 1


# Display total number of unique hashes
print("===========================================================")
print(f"Total Hash files : {len(hash_count)}")


# ============================================================
# 14. CLOSE FILES AND RESTORE TERMINAL OUTPUT
# ============================================================

# Restore normal terminal output
sys.stdout = original_stdout

# Close the IOC report file
output_file.close()

# Close the security log file
file_handler.close()


# ============================================================
# 15. DISPLAY COMPLETION MESSAGE
# ============================================================

print("===========================================================")
print("IOC extraction completed successfully!")
print("Report saved to: ioc_report.txt")
print("===========================================================")
