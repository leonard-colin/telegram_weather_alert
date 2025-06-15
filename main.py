from tools import weather_api, telegram_messaging


weather = weather_api.parse_weekly_weather_data()


def is_weather_critical():
    return any(
        "rain" in forecast[1] or forecast[-1] <= 0 for forecast in weather.values()
    )


def send_message():
    if is_weather_critical():
        message = telegram_messaging.build_message(weather)
        telegram_messaging.send_alert(f"⚠️ Alerte météo La Motte ⚠️\n\n{message}")


if __name__ == "__main__":
    send_message()
