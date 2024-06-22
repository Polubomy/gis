import requests
import unittest
import time

BASE_URL = "https://regions-test.2gis.com/"

def get_token():
    token_response = requests.post(f"{BASE_URL}/v1/auth/tokens")
    token = token_response.cookies.get('token')
    return token

class APITests(unittest.TestCase):

    def test_create_favorite_place_valid(self):
        # Проверяет успешное создание избранного места с валидными данными.
        token = get_token()
        data = {
            "title": "Test Place",
            "lat": 55.7558,
            "lon": 37.6173,
            "color": "RED"
        }
        response = requests.post(f"{BASE_URL}/v1/favorites", data=data, cookies={'token': token})
        self.assertEqual(response.status_code, 200, "Ошибка: Неверный код ответа сервера")
        response_data = response.json()
        self.assertEqual(response_data['title'], "Test Place", "Ошибка: Неверное название места в ответе")
        self.assertEqual(response_data['lat'], 55.7558, "Ошибка: Неверная широта в ответе")
        self.assertEqual(response_data['lon'], 37.6173, "Ошибка: Неверная долгота в ответе")
        self.assertEqual(response_data['color'], "RED", "Ошибка: Неверный цвет в ответе")

    def test_create_favorite_place_invalid_lat_format(self):
        # роверяет ошибку при некорректном формате широты
        token = get_token()
        data = {
            "title": "Test Place",
            "lat": "55.7558",  # Некорректный формат: строка вместо числа
            "lon": 37.6173,
            "color": "RED"
        }
        response = requests.post(f"{BASE_URL}/v1/favorites", data=data, cookies={'token': token})
        response_data = response.json()
        self.assertEqual(response_data['lat'], 55.7558, "Ошибка: Вернул переделанный текст в число, исходным был текст")


    def test_create_favorite_place_duplicate(self):
        # Проверяет ошибку при попытке создания дубликата
        token = get_token()
        data = {
            "title": "Duplicate Place",
            "lat": 55.7558,
            "lon": 37.6173,
            "color": "GREEN"
        }
        # Создаем дубликат
        response = requests.post(f"{BASE_URL}/v1/favorites", data=data, cookies={'token': token})
        self.assertEqual(response.status_code, 200, "Ошибка: Ошиюка в запросе")

        response1 = requests.post(f"{BASE_URL}/v1/favorites", data=data, cookies={'token': token})
        self.assertNotEqual(response1.status_code, 200, "Ошибка: Создается дубликт с теми же данными(включая токен), но id метке присваевается новый")




    def test_create_favorite_place_invalid_color(self):
        #Проверяет ошибку при некорректном цвете
        token = get_token()
        data = {
            "title": "Test Place",
            "lat": 55.7558,
            "lon": 37.6173,
            "color": "INVALID_COLOR"
        }
        response = requests.post(f"{BASE_URL}/v1/favorites", data=data, cookies={'token': token})
        self.assertNotEqual(response.status_code, 200, "Ошибка: Сервер не вернул ошибку при некорректном цвете")

    def test_create_favorite_place_missing_title(self):
        # Проверяет ошибку при отсутствии названия
        token = get_token()
        data = {
            "lat": 55.7558,
            "lon": 37.6173,
            "color": "BLUE"
        }
        response = requests.post(f"{BASE_URL}/v1/favorites", data=data, cookies={'token': token})
        self.assertNotEqual(response.status_code, 200, "Ошибка: Сервер не вернул ошибку при отсутствии названия")

    def test_create_favorite_place_missing_lat(self):
        # Проверяет ошибку при отсутствии широты
        token = get_token()
        data = {
            "title": "Test Place",
            "lon": 37.6173,
            "color": "YELLOW"
        }
        response = requests.post(f"{BASE_URL}/v1/favorites", data=data, cookies={'token': token})
        self.assertNotEqual(response.status_code, 200, "Ошибка: Сервер не вернул ошибку при отсутствии широты")

    def test_create_favorite_place_missing_lon(self):
        #Проверяет ошибку при отсутствии долготы
        token = get_token()
        data = {
            "title": "Test Place",
            "lat": 55.7558,
            "color": "GREEN"
        }
        response = requests.post(f"{BASE_URL}/v1/favorites", data=data, cookies={'token': token})
        self.assertNotEqual(response.status_code, 200, "Ошибка: Сервер не вернул ошибку при отсутствии долготы")

    def test_create_favorite_place_invalid_lat(self):
        # Проверяет ошибку при некорректном значении широты
        token = get_token()
        data = {
            "title": "Test Place",
            "lat": 100,  # Некорректное значение
            "lon": 37.6173,
            "color": "BLUE"
        }
        response = requests.post(f"{BASE_URL}/v1/favorites", data=data, cookies={'token': token})
        self.assertNotEqual(response.status_code, 200, "Ошибка: Сервер не вернул ошибку при некорректном значении широты")

    def test_create_favorite_place_invalid_lon(self):
        # Проверяет ошибку при некорректном значении долготы
        token = get_token()
        data = {
            "title": "Test Place",
            "lat": 55.7558,
            "lon": 190,  # Некорректное значение
            "color": "YELLOW"
        }
        response = requests.post(f"{BASE_URL}/v1/favorites", data=data, cookies={'token': token})
        self.assertNotEqual(response.status_code, 200, "Ошибка: Сервер не вернул ошибку при некорректном значении долготы")

    def test_create_favorite_place_overtime(self):
        # Проверяет ошибку при использовании просроченного токена
        token = get_token()
        time.sleep(3)  # Ждем, чтобы токен просрочился
        data = {
            "title": "Test Place",
            "lat": 55.7558,
            "lon": 37.6173,
            "color": "RED"
        }
        response = requests.post(f"{BASE_URL}/v1/favorites", data=data, cookies={'token': token})
        self.assertNotEqual(response.status_code, 200, "Ошибка: Сервер не вернул ошибку при использовании просроченного токена")

if __name__ == '__main__':
    unittest.main()