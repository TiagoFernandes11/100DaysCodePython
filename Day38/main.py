from datetime import datetime
import requests

NUTRITIONIX_API_ID = "c2822b1a"
NUTRITIONIX_API_KEY = "725b017062d18b2cf388e94e8ca0fd8a"
EXERCISE_API_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"

SHEETY_API_URL = "https://api.sheety.co/8b9a54d724cfa812d2bb2facaae1cd47/cópiaDeMyWorkouts/workouts"

exercise_text = input("Tell me which exercises you did: ")

header_params = {
  "x-app-id": NUTRITIONIX_API_ID,
  "x-app-key": NUTRITIONIX_API_KEY
}

exercise_params = {
  "query": exercise_text,
  "weight_kg": 90,
  "height_cm": 176,
  "age": 25
}

response = requests.post(url=EXERCISE_API_URL, json=exercise_params, headers=header_params)
result = response.json()

sheety_header = {
 "Authorization": "Bearer Choranene"
}

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(SHEETY_API_URL, json=sheet_inputs)

    print(sheet_response.text)
