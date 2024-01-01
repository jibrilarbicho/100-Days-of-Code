api_key = "76aaa6b2eb244653864343545e2aa7d0"
import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
parameters = {"lat": 9.145000, "lon": 40.489674, "appid": api_key}


response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
print(response.status_code)
weather_data = response.json()
