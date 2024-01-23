import requests

params = {
    "amount": 10,
    "category": 18,
    "type": "boolean"
}

TRIVIA_API_URL = "https://opentdb.com/api.php"

response = requests.get(TRIVIA_API_URL, params=params)

question_data = response.json()["results"]
