import os
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


def build_message(data: dict) -> str:
    lines = []
    icons = {
        "clear": "☀️",
        "clouds": "☁️",
        "rain": "🌧️",
        "overcast": "🌥️",
        "few": "🌤️",
        "broken": "⛅",
        "thunderstorm": "⛈️",
        "snow": "❄️",
        "mist": "🌫️",
    }

    for day, (short_desc, summary, temp) in data.items():
        icon = "🌈"  # Default
        for keyword, emoji in icons.items():
            if keyword in short_desc.lower():
                icon = emoji
                break

        lines.append(
            f"{icon} {day}\n• {short_desc.capitalize()}\n• {summary}\n• 🌡️ Min: {temp}°C\n"
        )

    return "\n".join(lines)


def send_alert(message: str):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    response = requests.get(url, params=payload)
    return response.status_code
