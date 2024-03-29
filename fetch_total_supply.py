import os
import requests
from decimal import Decimal

def fetch_total_supply(api_key):
    CONTRACT_ADDRESS = "0x7d89e05c0b93b24b5cb23a073e60d008fed1acf9"
    total_supply_url = f"https://api.basescan.org/api?module=stats&action=tokensupply&contractaddress={CONTRACT_ADDRESS}&apikey={api_key}"
    
    response = requests.get(total_supply_url)
    if response.status_code == 200:
        data = response.json()
        total_supply = Decimal(data['result'])
        # Adjust total supply for 18 decimal places
        adjusted_supply = total_supply / Decimal('1e18')
        return adjusted_supply
    else:
        raise Exception(f"Failed to fetch total supply: {response.text}")

def write_value_to_file(total_supply):
    with open('total_supply.txt', 'w') as file:
        file.write(f"{total_supply}")

if __name__ == "__main__":
    API_KEY = os.getenv('API_KEY')
    if not API_KEY:
        raise ValueError("API_KEY environment variable is not set.")
    
    total_supply = fetch_total_supply(API_KEY)
    write_value_to_file(total_supply)
