from cgi import print_arguments
import requests

pixelaEndpoint = "https://pixe.la/v1/users"
userParams = {
    "token": "aiwduiqduqiuq98121bsdbub",
    "username": "jibril",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
response = requests.post(pixelaEndpoint, json=userParams)
print(response.text)
