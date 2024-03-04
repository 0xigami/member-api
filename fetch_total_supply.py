import json
import os
import requests

def fetch_total_supply(api_key):
    CONTRACT_ADDRESS = "0x7d89e05c0b93b24b5cb23a073e60d008fed1acf9"
    total_supply_url = f"https://api.basescan.org/api?module=stats&action=tokensupply&contractaddress={CONTRACT_ADDRESS}&apikey={api_key}"
    
    response = requests.get(total_supply_url)
    if response.status_code == 200:
        data = response.json()
        total_supply = data['result']
        return total_supply
    else:
        raise Exception(f"Failed to fetch total supply: {response.text}")

def update_json_file(total_supply):
    data = {'totalsupply': total_supply}
    with open('total_supply.json', 'w') as json_file:
        json.dump(data, json_file)

if __name__ == "__main__":
    API_KEY = os.getenv('API_KEY')
    if not API_KEY:
        raise ValueError("API_KEY environment variable is not set.")
    
    total_supply = fetch_total_supply(API_KEY)
    update_json_file(total_supply)
