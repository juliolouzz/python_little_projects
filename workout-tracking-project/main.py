import requests
from datetime import datetime
import os

NUTRI_ID = os.environ["NUTRI_ID"]
NUTRI_KEY = os.environ["NUTRI_KEY"]

AGE = 29
WEIGHT = 74.3
HEIGHT = 169
GENDER = "male"

NUTRI_ENDPOINT = "https://trackapi.nutritionix.com/v2"
EXERCISE_ENDPOINT = "/natural/exercise"

exercise_input = input("Tell me which exercises you did:\n")

headers = {
    "x-app-id": NUTRI_ID,
    "x-app-key": NUTRI_KEY,
}

nutri_params = {
    "query": exercise_input,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

response_nutri = requests.post(url=f"{NUTRI_ENDPOINT}{EXERCISE_ENDPOINT}", json=nutri_params, headers=headers)
exercise_dict = response_nutri.json()
#print(exercise_dict)

SHEETY_ENDPOINT = "https://api.sheety.co"
SHEETY_USERNAME = os.environ["SHEETY_USERNAME"]
SHEETY_FOLDER = "myWorkouts/workouts"
SHEETY_KEY = os.environ["SHEETY_KEY"]

today = datetime.now()

sheety_headers = {
    "Authorization": SHEETY_KEY
}

sheety_params = \
    {
        "workout": {
            "date": today.strftime("%d/%m/%Y"),
            "time": today.strftime("%X"),
            "exercise": exercise_dict["exercises"][0]["name"].title(),
            "duration": exercise_dict["exercises"][0]["duration_min"],
            "calories": exercise_dict["exercises"][0]["nf_calories"]
        }
    }

response_sheety = requests.post(url=f"{SHEETY_ENDPOINT}/{SHEETY_USERNAME}/{SHEETY_FOLDER}",
                                json=sheety_params, headers=sheety_headers)
#print(response_sheety.json())