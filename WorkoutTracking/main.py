import requests
import datetime
import os

# nutritionix
APP_ID = os.environ.get("APP_ID", "APP ID it doesn't exist")
API_KEY = os.environ.get("API_KEY", "API_KEY it doesn't exist")

url = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

user_input = input("Which exercise you did?")

data = {
    "query": user_input
}

response_nutritionix = requests.post(url, headers=headers, json=data)
if response_nutritionix.status_code == 200:
    response_nutritionix = response_nutritionix.json()
    print(response_nutritionix)
else:
    print(f"Error in the request. Status code: {response_nutritionix.status_code}")
    print(response_nutritionix.text)

# sheety
url = ""
headers = {
 "Authorization": ""
}

response_sheety = requests.post()


# Saving data into google sheets
