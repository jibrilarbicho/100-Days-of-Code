from wsgiref import headers
from flask import request
import requests
from datetime import datetime

GRAPHID = "graph1"
USERNAME = "jibri2weqn,d2la"
TOKEN = "idu4878ru3ibf3if3i"
pixelaEndpoint = "https://pixe.la/v1/users"
userParams = {
    "token": "aiwduiqduqiuq98121bsdbub",
    "username": "jibakxril",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
response = requests.post(pixelaEndpoint, json=userParams)
print(response.text)
headers = {"X_USER_TOKEN": TOKEN}
graph_endpoint = f"{pixelaEndpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPHID,
    "name": "my cycling graphs ",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}
result = requests.post(graph_endpoint, json=graph_config, headers=headers)
pixel_creation_endpoint = f" {pixelaEndpoint}/{USERNAME}/graphs/{GRAPHID}"
pixel_data = {
    "date": "20200724",
    "quantity": "9.74",
}
response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)
today = datetime.now()
