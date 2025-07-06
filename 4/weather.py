# weather.py
import requests

def get_weather(city):
    try:
        resp = requests.get(f"https://api.example.com/weather/{city}", timeout=5)
        return resp.json()
    except requests.RequestException:
        return None