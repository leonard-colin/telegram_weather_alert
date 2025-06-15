import os

import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()


def _get_weather_data() -> dict[str, any]:
    url = "https://api.openweathermap.org/data/3.0/onecall"
    params = {
        "lat": os.getenv("LAT"),
        "lon": os.getenv("LON"),
        "exclude": "current,minutely,hourly",
        "units": "metric",
        "appid": os.getenv("WEATHER_APP_ID"),
    }

    response = requests.get(url, params)
    data = response.json()
    return data


def parse_weekly_weather_data() -> dict[str, any]:
    data = _get_weather_data()
    weekly_weather = {}

    for day in data["daily"]:
        week_day = datetime.fromtimestamp(day["dt"]).strftime("%A %d").lstrip("0")
        weather_description = day["weather"][0]["description"]
        weather_summary = day["summary"]
        min_temperature = day["temp"]["min"]
        weekly_weather[week_day] = [
            weather_description,
            weather_summary,
            min_temperature,
        ]

    return weekly_weather
