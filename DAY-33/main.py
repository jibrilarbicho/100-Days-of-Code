from traceback import print_tb
import requests

res = requests.get(url="http://api.open-notify.org/iss-now.json")
# if res.status_code == 404:
#     raise Exception("The Resource Does not found")
# elif res.status_code == 401:
#     raise Exception("You are not Authorized to access this data")
res.raise_for_status()

data = res.json()
print(data)
longitude = data["iss_position"]["longitude"]
