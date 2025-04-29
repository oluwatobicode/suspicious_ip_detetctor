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
  (screenshots/shot-one.png)
- !Flagging Suspicious IPs and Saving to Blocklist:
  (screenshots/shot-two.png)

# 🛠️ Tech Stack

- Python 3
- Requests library
- dotenv for managing API keys securely
- AbuseIPDB API

⚙️ Setup Instructions

1. Clone this repository or download the project files.
2. Install the required dependencies:

> pip install requests python-dotenv

3. Create a .env file in the root directory with the following:

   > - API_KEY=your_abuseipdb_api_key
   > - API_URL=https://api.abuseipdb.com/api/v2/check

4. Create a api key on Abuse IPdb when you sign up there

5.Create an Ip_addresses.txt file and add the IPs you want to check, one per line.

> Example:

- 8.8.8.8
- 1.1.1.1
- 185.107.56.57
- 209.126.136.5

6. Run the script:
   > python app.py

📬 Contact
Feel free to reach out if you have suggestions or want to collaborate!

- LinkedIn : https://www.linkedin.com/in/treasure-odetokun-107a21231/
- Twitter : https://x.com/Oluwatobicodes
