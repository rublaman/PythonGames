import requests

parameteres = {
    "amount": 10,
    "category": 18,
    "type": "boolean"
}

r = requests.get("https://opentdb.com/api.php", params=parameteres)
r.raise_for_status()
question_data = r.json()["results"]
