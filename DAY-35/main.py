api_key = ""
import requests
from twilio.rest import Client
import os


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
parameters = {"lat": 9.145000, "lon": 40.489674, "appid": api_key}

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

# response = requests.get(OWM_Endpoint, params=parameters)
# response.raise_for_status()
# print(response.status_code)
# weather_data = response.json()
# print(weather_data)
client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Yoyyaa.",
    from_="+16174311282",
    to="+251 93 404 4223",
)

print(message.sid)
