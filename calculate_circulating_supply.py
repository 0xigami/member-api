import json
import os
import requests

def calculate_circulating_supply(api_key):
    CONTRACT_ADDRESS = "0x7d89e05c0b93b24b5cb23a073e60d008fed1acf9"
    total_supply_url = f"https://api.basescan.org/api?module=stats&action=tokensupply&contractaddress={CONTRACT_ADDRESS}&apikey={api_key}"
    balance_urls = [
        f"https://api.basescan.org/api?module=account&action=tokenbalance&contractaddress={CONTRACT_ADDRESS}&address=0xf2a6f079f507a3a1b70f8a1943b434e194c036ee&tag=latest&apikey={api_key}",
        f"https://api.basescan.org/api?module=account&action=tokenbalance&contractaddress={CONTRACT_ADDRESS}&address=0x45ce283c2a12df1bf69802fd2c1e5398228f939d&tag=latest&apikey={api_key}",
        f"https://api.basescan.org/api?module=account&action=tokenbalance&contractaddress={CONTRACT_ADDRESS}&address=0x542ffb7d78d78f957895891b6798b3d60e979b64&tag=latest&apikey={api_key}"
    ]
    
    total_supply = int(requests.get(total_supply_url).json()['result'])
    circulating_supply = total_supply
    
    for url in balance_urls:
        balance = int(requests.get(url).json()['result'])
        circulating_supply -= balance
    
    return circulating_supply

def update_json_file(circulating_supply):
    data = {'circulating_supply': circulating_supply}
    with open('circulating_supply.json', 'w') as json_file:
        json.dump(data, json_file)

if __name__ == "__main__":
    API_KEY = os.getenv('API_KEY')
    if not API_KEY:
        raise ValueError("API_KEY environment variable is not set.")
    
    circulating_supply = calculate_circulating_supply(API_KEY)
    update_json_file(circulating_supply)
