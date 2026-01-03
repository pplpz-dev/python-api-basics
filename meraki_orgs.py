import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("MERAKI_API_KEY")
if not API_KEY:
    raise SystemExit("ERROR: MERAKI_API_KEY no encontrado. Revisa tu .env")

BASE_URL = "https://api.meraki.com/api/v1"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Accept": "application/json",
}

response = requests.get(f"{BASE_URL}/organizations", headers=headers, timeout=30)
print("Status:", response.status_code)
response.raise_for_status()

orgs = response.json()
print(f"Organizaciones encontradas: {len(orgs)}")

for org in orgs:
    print(org["id"], "-", org["name"])