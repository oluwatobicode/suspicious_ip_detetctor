# IP Threat Intelligence Automation Tool

This is a lightweight Python script that helps SOC Analysts and Cybersecurity professionals quickly check the reputation of multiple IP addresses in a text file using the AbuseIPDB API.This tool automates the process of identifying suspicious IPs, making incident response and log triage much faster and more efficient.

# 🚀 Features

- Reads multiple IP addresses from a file
- Sends requests to AbuseIPDB API
- Retrieves and displays the abuse confidence score for each IP
- Flags suspicious IPs with a high abuse score
- Saves flagged IPs into a separate FlaggedIp.txt file
- Tracks and displays script execution time

# 📸 Screenshots

- !Reading IP addresses and scanning:
  (/screenshots/shot-one.png)
- !Flagging Suspicious IPs and Saving to Blocklist:
  (/screenshots/shot-two.png)

# 🛠️ Tech Stack

- Python 3
- Requests library
- dotenv for managing API keys securely
- AbuseIPDB API
