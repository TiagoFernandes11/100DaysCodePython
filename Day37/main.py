import requests


# Creating user API interaction:
PIXELA_ENDPOINT = "https://pixe.la/v1/users"

user_params = {
    "token": "shAshAshAblaushAshAshAblaushAshAshAblau",
    "username": "testeestudopython",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

GRAPH_PIXELA_ENDPOINT = f"https://pixe.la/v1/users/{user_params.get('username')}/graphs"

graph_params = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

graph_headers = {
    "X-USER-TOKEN": user_params["token"]
}

# response = requests.post(url=GRAPH_PIXELA_ENDPOINT, headers=graph_headers, json=graph_params)
# print(response.text)

PIXEL_PIXELA_ENDPOINT = f"https://pixe.la/v1/users/{user_params.get('username')}/graphs/{graph_params.get('id')}"

pixel_params = {
    "date": "20240124",
    "quantity": "1.1"
}

response = requests.post(url=PIXEL_PIXELA_ENDPOINT, headers=graph_headers, json=pixel_params)
print(response.text)
