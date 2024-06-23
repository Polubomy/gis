import requests

URL = "https://regions-test.2gis.com/"

def create_place(data):

    token_response = requests.post(f"{URL}/v1/auth/tokens")
    token = token_response.cookies.get('token')

    response = requests.post(f"{URL}/v1/favorites", data=data, cookies={'token': token})

    response_data = response.json()
    return response_data

