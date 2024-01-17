import requests
import datetime
import os

# nutritionix
APP_ID = os.environ.get("APP_ID", "APP ID it doesn't exist")
API_KEY = os.environ.get("API_KEY", "API_KEY it doesn't exist")

# 2 Get Exercise stats with NLQ
response = requests.post(
    'https://trackapi.nutritionix.com/v2/natural/exercise',
    headers={
        "x-app-id": APP_ID,
        "x-app-key": API_KEY
    }, params={
        "query": "swam for 1 hour"
    })

print(response)

# 3 Setup Google Sheet with Sheety

# Saving data into google sheets
