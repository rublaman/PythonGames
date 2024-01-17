import requests
import datetime
import os

# nutritionix
APP_ID = os.environ.get("APP_ID", "APP ID it doesn't exist")
API_KEY = os.environ.get("API_KEY", "API_KEY it doesn't exist")

# 2 Get Exercise stats with NLQ
url = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

data = {
    "query": "swam for 1 hour"
}

response = requests.post(url, headers=headers, json=data)
if response.status_code == 200:
    response = response.json()
    print(response)
else:
    print(f"Error in the request. Status code: {response.status_code}")
    print(response.text)

# 3 Setup Google Sheet with Sheety

# Saving data into google sheets
