import requests
from datetime import datetime

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
TOKEN = "" # put your token here
USERNAME = "" # put your username here
GRAPH_ID = "graph1"


user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}


def create_account():
    response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
    print(response.text)


GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"


graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}


headers = {
    "X-USER-TOKEN": TOKEN
}

# Create a graph
# response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)

PIXEL_CREATION_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"  #/v1/users/<username>/graphs/<graphID>

date = datetime.now()
today = date.strftime("%Y%m%d")

km_cycled = input("How many kilometers did you cycled today? !Use float number!\n")

add_pixel = {
    "date": today,
    "quantity": km_cycled,
}

# pixel creation on the graph
# response = requests.post(url=PIXEL_CREATION_ENDPOINT, json=add_pixel, headers=headers)

PIXEL_UPDATE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today}"

update_pixel = {
    "quantity": km_cycled,
}

# Updating a pixel on the graph
# response = requests.put(url=PIXEL_UPDATE_ENDPOINT, json=update_pixel, headers=headers)


# Deleting a pixel
# response = requests.delete(url=PIXEL_UPDATE_ENDPOINT, headers=headers)

