import datetime
import common.functions as func
import requests
from common.config import AppConfig

def get_weather(API_CITY = AppConfig.API_CITY):
    API_KEY = AppConfig.API_KEY

    url = f"https://api.openweathermap.org/data/2.5/weather?q={API_CITY}&appid={API_KEY}"

    try:
        response = requests.get(url)
        data = response.json()

        weather = {
            "place": data.get("name"),
            "temp": func.temp_c(data.get("main").get("temp")),
            "feels_like": func.temp_c(data.get("main").get("feels_like")),
            "wind": data.get("wind").get("speed"),
            "timestamp": func.timestamp(),
            "sunrise": func.time_dt(data.get("sys").get("sunrise")),
            "sunset": func.time_dt(data.get("sys").get("sunset")),
        }

        return weather

    except Exception as e:
        print(e)