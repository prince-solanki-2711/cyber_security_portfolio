# Brute Force Detection Using Python

## About the Project

I built this project to practise a basic security monitoring task using
Python. It reads SSH login logs and looks for login patterns that may be
suspicious.

The project is part of my learning journey towards a SOC Analyst role.

## What It Does

-   Reads login events from `ssh_logs.txt`
-   Checks the format of each log entry
-   Counts failed login attempts by source IP
-   Detects possible brute-force activity
-   Detects possible password spraying
-   Shows a summary of the log data and alerts
-   Saves detected alerts to `alerts.json`

## Detection Rules

**Brute force:** The same source IP tries the same username at least 5
times within 60 seconds.

**Password spraying:** The same source IP tries at least 5 different
usernames within 60 seconds.

These are simple learning rules. An alert means the activity needs
review; it does not prove that an attack happened.

## Project Files

-   `brute_force_detector.py` --- the Python script
-   `ssh_logs.txt` --- the sample SSH login logs
-   `alerts.json` --- the alerts saved by the script

## Log Format

Each log entry should contain five fields:

``` text
YYYY-MM-DD HH:MM:SS STATUS IP_ADDRESS USERNAME
```

Example:

``` text
2026-10-10 10:00:01 FAILED 192.168.1.10 admin
2026-10-10 10:00:10 FAILED 192.168.1.10 admin
2026-10-10 10:00:20 FAILED 192.168.1.10 admin
2026-10-10 10:00:30 FAILED 192.168.1.10 admin
2026-10-10 10:00:40 FAILED 192.168.1.10 admin
2026-10-10 10:01:20 SUCCESS 192.168.1.20 alice
```

The status must be `FAILED` or `SUCCESS`. The script checks the
timestamp and IP address and skips invalid entries.

## How to Run

1.  Install Python 3.
2.  Keep `brute_force_detector.py` and `ssh_logs.txt` in the same
    folder.
3.  Open a terminal in that folder.
4.  Run:

``` bash
python brute_force_detector.py
```

The script displays the alerts and summary in the terminal. It also
creates or updates `alerts.json`.

## What the Report Shows

The terminal report includes:

-   Failed login attempts by source IP
-   Brute-force alerts
-   Password-spraying alerts
-   Suspicious source IP summary
-   Total log lines, valid events, and invalid events
-   Failed and successful login counts
-   Number of unique source IP addresses
-   Total detection events

## Current Limitations

-   This project uses a simple text log format and sample data.
-   The detection thresholds are fixed in the script.
-   It does not connect to a live server or SIEM platform.
-   The results depend on the quality and completeness of the input
    logs.
-   Alerts need to be reviewed before deciding whether activity is
    malicious.

## What I Learned

While building this project, I practised reading files, validating
input, working with timestamps, grouping events, using dictionaries and
sets, detecting patterns, and exporting results to JSON.

## Next Steps

I plan to keep improving the project and learn how these detection ideas
are used in real SOC workflows.
