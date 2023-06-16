APP_ID="YOUR ID"
API_KEY="YOUR API ID"	
EXCERCISE_ENDPOINT="https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT="https://api.sheety.co/7359ee50cb5d3a4c85c5d7e78b929b51/workoutTracker/workouts"
TOKEN="YOUR SECRET TOKEN"
GENDER="male"
AGE="20"
WEIGHT="55"
HEIGHT="167"
import os
from datetime import datetime
today=datetime.now()
import requests
from datetime import datetime
QUESTION=input("Which exercise did you do ?")

excercise_para={
    "query": QUESTION  ,
    "gender":GENDER,
    "weight_kg":WEIGHT,
    "height_cm":HEIGHT,
    "age":AGE,
}

headers={
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}



response=requests.post(url=EXCERCISE_ENDPOINT,json=excercise_para,headers=headers)
result=response.json()



today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
for exercise in result["exercises"]:
    sheety_para={
            "workout":{
            "date" :today_date ,
            "time" : now_time,
            "exercise" :exercise["name"]  ,
            "duration":exercise["duration_min"] ,
            "calories": exercise["nf_calories"],
            }
        }


    bearer_headers = {
    "Authorization": TOKEN
    }
    sheet_response = requests.post(
        SHEETY_ENDPOINT, 
        json=sheety_para, 
        headers=bearer_headers,
    )   