import requests
import unittest

BASE_URL = "https://regions-test.2gis.com/"


def get_token():
    token_response = requests.post(f"{BASE_URL}/v1/auth/tokens")
    token = token_response.cookies.get('token')
    return token


class APITests(unittest.TestCase):

    def test_get_auth_token(self):
        response = requests.post(f"{BASE_URL}/v1/auth/tokens")

        if response.status_code != 200:
            error_message = response.json().get('error', {}).get('message')
            self.fail(f"Тест не прошел: {error_message}") # Проваливаем тест с описанием ошибки
        else:
            self.addCleanup(lambda: print(f"Тест test_get_auth_token успешно прошел!"))


    def test_create_favorite_place(self):
        token = get_token()

        data = {
            "title": "Test Place",
            "lat": 55.7558,
            "lon": 37.6173
        }

        response = requests.post(f"{BASE_URL}/v1/favorites", data=data, cookies={'token': token})
        if response.status_code != 200:
            error_message = response.json().get('error', {}).get('message')
            self.fail(f"Тест не прошел: {error_message}")
        else:
            self.addCleanup(lambda: print(f"Тест test_create_favorite_place успешно прошел!"))

    def test_create_favorite_place_with_color(self):
        token = get_token()

        data = {
            "title": "Test Place",
            "lat": 55.7558,
            "lon": 37.6173,
            "color": "RED"
        }

        response = requests.post(f"{BASE_URL}/v1/favorites", data=data, cookies={'token': token})
        if response.status_code != 200:
            error_message = response.json().get('error', {}).get('message')
            self.fail(f"Тест не прошел: {error_message}")
        else:
            self.addCleanup(lambda: print(f"Тест test_create_favorite_place_with_color успешно прошел!"))


    def test_create_favorite_place_invalid_title(self):
        token = get_token()

        data = {
            "title": "",
            "lat": 55.7558,
            "lon": 37.6173
        }

        response = requests.post(f"{BASE_URL}/v1/favorites", data=data, cookies={'token': token})
        if response.status_code != 200:
            error_message = response.json().get('error', {}).get('message')
            self.fail(f"Тест не прошел: {error_message}")
        else:
            self.addCleanup(lambda: print(f"Тест test_create_favorite_place_invalid_title успешно прошел!"))

    def test_create_favorite_place_invalid_color(self):
        token = get_token()

        data = {
            "title": "Test Place",
            "lat": 55.7558,
            "lon": 37.6173,
            "color": "INVALID_COLOR"
        }

        response = requests.post(f"{BASE_URL}/v1/favorites", data=data, cookies={'token': token})
        if response.status_code != 200:
            error_message = response.json().get('error', {}).get('message')
            self.fail(f"Тест не прошел: {error_message}")
        else:
            self.addCleanup(lambda: print(f"Тест test_create_favorite_place_invalid_color успешно прошел!"))

    def test_create_favorite_place_missing_title(self):
        token = get_token()

        data = {
            "lat": 55.7558,
            "lon": 37.6173,
        }

        response = requests.post(f"{BASE_URL}/v1/favorites", data=data, cookies={'token': token})
        if response.status_code != 200:
            error_message = response.json().get('error', {}).get('message')
            self.fail(f"Тест не прошел: {error_message}")
        else:
            self.addCleanup(lambda: print(f"Тест test_create_favorite_place_missing_title успешно прошел!"))

    def test_create_favorite_place_missing_lat(self):
        token = get_token()

        data = {
            "title": "Test Place",
            "lon": 37.6173,
        }

        response = requests.post(f"{BASE_URL}/v1/favorites", data=data, cookies={'token': token})
        if response.status_code != 200:
            error_message = response.json().get('error', {}).get('message')
            self.fail(f"Тест не прошел: {error_message}")
        else:
            self.addCleanup(lambda: print(f"Тест test_create_favorite_place_missing_lat успешно прошел!"))

    def test_create_favorite_place_invalid_lat(self):
        token = get_token()

        data = {
            "title": "Test Place",
            "lat": 100,
            "lon": 37.6173
        }

        response = requests.post(f"{BASE_URL}/v1/favorites", data=data, cookies={'token': token})
        if response.status_code != 200:
            error_message = response.json().get('error', {}).get('message')
            self.fail(f"Тест не прошел: {error_message}")
        else:
            self.addCleanup(lambda: print(f"Тест test_create_favorite_place_invalid_lat успешно прошел!"))

    def test_create_favorite_place_missing_lon(self):
        token = get_token()

        data = {
            "title": "Test Place",
            "lat": 55.7558,
        }

        response = requests.post(f"{BASE_URL}/v1/favorites", data=data, cookies={'token': token})
        if response.status_code != 200:
            error_message = response.json().get('error', {}).get('message')
            self.fail(f"Тест не прошел: {error_message}")
        else:
            self.addCleanup(lambda: print(f"Тест test_create_favorite_place_missing_lon успешно прошел!"))

    def test_create_favorite_place_invalid_lon(self):
        token = get_token()

        data = {
            "title": "Test Place",
            "lat": 36.8568,
            "lon": 190
        }

        response = requests.post(f"{BASE_URL}/v1/favorites", data=data, cookies={'token': token})
        if response.status_code != 200:
            error_message = response.json().get('error', {}).get('message')
            self.fail(f"Тест не прошел: {error_message}")
        else:
            self.addCleanup(lambda: print(f"Тест test_create_favorite_place_invalid_lat успешно прошел!"))

if __name__ == '__main__':
    unittest.main()
