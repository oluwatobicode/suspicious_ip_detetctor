import time
import requests
import json
import os
from dotenv import load_dotenv


start_time = time.time()
load_dotenv()

# ENVIORMENT VARIABLE TO GET KEYS
api_key = os.getenv("API_KEY")
api_url = os.getenv("API_URL")


# Reading my ip-text file
with open('Ip_addresses.txt') as file:
    ip_list = [line.strip() for line in file.readlines()]
print(ip_list)

# looping through the ip addresses and sending a request to AbuseIPDB
for ip in ip_list:
    params = {
        'ipAddress':ip,
        'maxAgeInDays':90,
    }
    headers = {
        'Accept':'application/json',
        'Key':api_key
    }
    response = requests.request(method='GET' ,url=api_url, headers=headers,params=params)
    data = response.json()

    if data.get('data'):
        abuse_score = data['data']['abuseConfidenceScore']
        print(f"Ip: {ip} | The Ip has an abuse score of: {abuse_score}")
        
    if abuse_score > 50:
        print(f"The IP is flagged: {ip}")
        with open("Flagged_Ip.txt", 'a') as blocklist:
            blocklist.write(ip + '\n')
    
    
    
end_time = time.time()
execution_time = end_time - start_time
print(f'Total execution time: {execution_time} seconds')