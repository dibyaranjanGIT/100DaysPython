import requests
from datetime import datetime

USERNAME = "dibyaranjan"
TOKEN = "jhsf9werisdj0wd"
GRAPHID = "graph1"

pixela_end_point = "https://pixe.la/v1/users"
user_params = {
    "token": USERNAME,
    "username": TOKEN,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_end_point, json=user_params)
# print(response.text)

graph_end_point = f"{pixela_end_point}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPHID,
    "name": "Workout Graph",
    "unit": "hr",
    "type": "float",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_end_point, json=graph_config, headers=headers)
# print(response.text)

today = datetime.today()
pixela_creation_end_point = f"{pixela_end_point}/{USERNAME}/graphs/{GRAPHID}"

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "1"
}

response = requests.post(url=pixela_creation_end_point, json=pixel_data, headers=headers)
print(response.text)

# print(today.strftime("%Y%m%d"))