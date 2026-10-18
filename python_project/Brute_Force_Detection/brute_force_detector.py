import json
import ipaddress
from datetime import datetime


# ==========================================
# 1. SETTINGS
# ==========================================

log_file = "login_data.log"
output_file = "alerts.json"

# Brute force: same IP + same username
threshold = 5
time_window = 60

# Password spraying: same IP + different usernames
spray_threshold = 5
spray_time_window = 60


# ==========================================
# 2. COUNTERS AND DATA STORAGE
# ==========================================

total_lines = 0
valid_events = 0
invalid_events = 0

failed_login_count = 0
successful_login_count = 0

unique_ips = set()
failed_by_ip = {}
failed_attempts = {}
login_events = []


# ==========================================
# 3. READ AND VALIDATE LOG FILE
# ==========================================

try:
    with open(log_file, "r", encoding="utf-8") as file:
        lines = file.readlines()
except FileNotFoundError:
    print(f"[ERROR] Log file not found: {log_file}")
    raise SystemExit(1)
except OSError as error:
    print(f"[ERROR] Could not read log file: {error}")
    raise SystemExit(1)

for line in lines:
    total_lines += 1
    parts = line.strip().split()

    # Expected format:
    # YYYY-MM-DD HH:MM:SS STATUS IP_ADDRESS USERNAME
    if len(parts) != 5:
        print(f"[WARNING] Skipping malformed log entry: {line.strip()}")
        invalid_events += 1
        continue

    timestamp_text = parts[0] + " " + parts[1]
    status = parts[2]
    ip = parts[3]
    username = parts[4]

    try:
        timestamp = datetime.strptime(timestamp_text, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        print(f"[WARNING] Invalid timestamp: {line.strip()}")
        invalid_events += 1
        continue

    try:
        ipaddress.ip_address(ip)
    except ValueError:
        print(f"[WARNING] Invalid IP address: {line.strip()}")
        invalid_events += 1
        continue

    if status not in ("FAILED", "SUCCESS"):
        print(f"[WARNING] Invalid login status: {line.strip()}")
        invalid_events += 1
        continue

    valid_events += 1
    unique_ips.add(ip)

    if status == "SUCCESS":
        successful_login_count += 1
        continue

    failed_login_count += 1
    failed_by_ip[ip] = failed_by_ip.get(ip, 0) + 1

    key = (ip, username)
    failed_attempts.setdefault(key, []).append(timestamp)
    login_events.append((timestamp, ip, username))


# ==========================================
# 4. DETECT BRUTE-FORCE ACTIVITY
# ==========================================

brute_force_details = {}
detection_reasons = {}

for key, timestamps in failed_attempts.items():
    ip, username = key
    timestamps.sort()

    # Find the first time window that meets the threshold.
    # The current timestamp is the end of each possible window.
    for i in range(len(timestamps)):
        window_timestamps = []

        for j in range(i, -1, -1):
            time_difference = (timestamps[i] - timestamps[j]).total_seconds()

            if time_difference > time_window:
                break

            window_timestamps.append(timestamps[j])

        if len(window_timestamps) >= threshold:
            # window_timestamps is newest-to-oldest, so the first
            # element is the end and the last element is the start.
            brute_force_details[key] = {
                "username": username,
                "failed_attempts": len(window_timestamps),
                "window_start": window_timestamps[-1].isoformat(sep=" "),
                "window_end": window_timestamps[0].isoformat(sep=" "),
            }

            detection_reasons.setdefault(ip, set()).add("Brute Force")
            break


for (ip, username), details in brute_force_details.items():
    print("\n[ALERT] [HIGH] Possible brute-force activity detected!")
    print(f"IP Address: {ip}")
    print(f"Username: {username}")
    print(f"Failed Attempts: {details['failed_attempts']}")
    print(f"Time Window: {time_window} seconds")
    print(f"Window Start: {details['window_start']}")
    print(f"Window End: {details['window_end']}")
    print("-" * 40)


# ==========================================
# 5. DETECT PASSWORD SPRAYING
# ==========================================

ip_events = {}

for timestamp, ip, username in login_events:
    ip_events.setdefault(ip, []).append((timestamp, username))

password_spraying_details = {}

for ip, events in ip_events.items():
    events.sort(key=lambda event: event[0])

    # Check every event as the beginning of a possible time window.
    for i in range(len(events)):
        usernames = set()
        window_end = events[i][0]

        for j in range(i, len(events)):
            time_difference = (events[j][0] - events[i][0]).total_seconds()

            if time_difference > spray_time_window:
                break

            usernames.add(events[j][1])
            window_end = events[j][0]

        if len(usernames) >= spray_threshold:
            password_spraying_details[ip] = {
                "usernames": sorted(usernames),
                "distinct_usernames": len(usernames),
                "window_start": events[i][0].isoformat(sep=" "),
                "window_end": window_end.isoformat(sep=" "),
            }

            detection_reasons.setdefault(ip, set()).add("Password Spraying")
            break


for ip, details in password_spraying_details.items():
    print("\n[ALERT] [HIGH] Possible password spraying detected!")
    print(f"Source IP: {ip}")
    print(f"Distinct Usernames: {details['distinct_usernames']}")
    print("Targeted Usernames: " + ", ".join(details["usernames"]))
    print(f"Time Window: {spray_time_window} seconds")
    print(f"Window Start: {details['window_start']}")
    print(f"Window End: {details['window_end']}")
    print("-" * 45)


# ==========================================
# 6. DISPLAY FAILED LOGINS BY SOURCE IP
# ==========================================

print("\nFAILED LOGIN ATTEMPTS BY SOURCE IP")
print("=" * 45)

for ip, count in sorted(
    failed_by_ip.items(), key=lambda item: item[1], reverse=True
):
    print(f"IP Address: {ip} | Failed Attempts: {count}")


# ==========================================
# 7. DISPLAY SUSPICIOUS SOURCE IP SUMMARY
# ==========================================

suspicious_ips = set(detection_reasons.keys())

print("\nSUSPICIOUS SOURCE IP SUMMARY")
print("=" * 45)

if suspicious_ips:
    for ip in sorted(suspicious_ips):
        reasons = ", ".join(sorted(detection_reasons[ip]))
        print(f"IP Address: {ip}")
        print(f"Detection Reason: {reasons}")
        print("Severity: HIGH")
        print(f"Failed Attempts: {failed_by_ip.get(ip, 0)}")
        print("-" * 45)
else:
    print("No suspicious source IPs detected.")

print("=" * 45)


# ==========================================
# 8. DISPLAY PROCESSING SUMMARY
# ==========================================

brute_force_alerts = len(brute_force_details)
password_spraying_alerts = len(password_spraying_details)
total_alerts = brute_force_alerts + password_spraying_alerts

print("\nDETECTION SUMMARY")
print("=" * 45)
print(f"Total Log Lines: {total_lines}")
print(f"Valid Events: {valid_events}")
print(f"Invalid Events: {invalid_events}")
print(f"Failed Login Attempts: {failed_login_count}")
print(f"Successful Logins: {successful_login_count}")
print(f"Unique Source IP Addresses: {len(unique_ips)}")
print(f"Brute-Force Alerts: {brute_force_alerts}")
print(f"Password-Spraying Alerts: {password_spraying_alerts}")
print(f"Total Detection Events: {total_alerts}")
print("=" * 45)


# ==========================================
# 9. EXPORT ALERTS TO JSON
# ==========================================

# Export one record per suspicious IP.
# Keep total failed attempts separate from attempts in a
# detected brute-force time window so the numbers are clear.
alerts = []

for ip in sorted(suspicious_ips):
    ip_brute_force_alerts = [
        {
            "username": username,
            "failed_attempts_in_window": details["failed_attempts"],
            "window_start": details["window_start"],
            "window_end": details["window_end"],
        }
        for (alert_ip, username), details in sorted(brute_force_details.items())
        if alert_ip == ip
    ]

    alert = {
        "source_ip": ip,
        "detection_reason": sorted(detection_reasons[ip]),
        "severity": "HIGH",
        "total_failed_attempts": failed_by_ip.get(ip, 0),
        "brute_force_details": ip_brute_force_alerts,
        "password_spraying_details": password_spraying_details.get(ip),
    }

    alerts.append(alert)

try:
    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(alerts, file, indent=4)

    print(f"\nAlerts exported to {output_file}")
except OSError as error:
    print(f"[ERROR] Could not save alerts: {error}")
