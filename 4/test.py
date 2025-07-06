from unittest.mock import patch
import requests
from weather import get_weather

def test_get_weather_network_error():
    with patch("weather.requests.get", side_effect=requests.RequestException):
        result = get_weather("Taipei")
        assert result is None
