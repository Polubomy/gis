import requests

URL = "https://regions-test.2gis.com/"

def create_place(data):

    token_response = requests.post(f"{URL}/v1/auth/tokens")
    token = token_response.cookies.get('token')

    response = requests.post(f"{URL}/v1/favorites", data=data, cookies={'token': token})

    response_data = response.json()
    return response_data

############

data_1 = {
    'title': 'Test_1',
    'lat': 55.028254,
    'lon': 82.918501,
    'color': 'BLUE'
}

if __name__ == '__main__':
    create_place(data_1)
