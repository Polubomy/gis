import requests
import unittest
import time

BASE_URL = "https://regions-test.2gis.com/"

def get_token():
    token_response = requests.post(f"{BASE_URL}/v1/auth/tokens")
    token = token_response.cookies.get('token')
    return token

class APITests(unittest.TestCase):

    def test_request_cookie(self):
        # Проверяет правильность запроса сессионного токена
        token_response = requests.post(f"{BASE_URL}/v1/auth/tokens")
        self.assertEqual(token_response.status_code, 200, "Ошибка: Неверный код ответа сервера")

    def test__place_valid(self):
        # Проверяет успешное создание избранного места с валидными данными
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

    def test__place_invalid_lat_format(self):
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
        self.assertEqual(response_data['title'], "Test Place", "Ошибка: Неверное название места в ответе")
        self.assertEqual(response_data['lon'], 37.6173, "Ошибка: Неверная долгота в ответе")
        self.assertEqual(response_data['color'], "RED", "Ошибка: Неверный цвет в ответе")


    def test_place_duplicate(self):
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
        response_data = response.json()
        self.assertEqual(response.status_code, 200, "Ошибка: Ошиюка в запросе")
        self.assertEqual(response_data['title'], "Duplicate Place", "Ошибка: Неверное название места в ответе")
        self.assertEqual(response_data['lat'], 55.7558, "Ошибка: Неверная широта в ответе")
        self.assertEqual(response_data['lon'], 37.6173, "Ошибка: Неверная долгота в ответе")
        self.assertEqual(response_data['color'], "GREEN", "Ошибка: Неверный цвет в ответе")

        response1 = requests.post(f"{BASE_URL}/v1/favorites", data=data, cookies={'token': token})
        self.assertNotEqual(response1.status_code, 200, "Ошибка: Создается дубликт с теми же данными(включая токен), но id метке присваевается новый")
        response_data1 = response1.json()
        self.assertEqual(response_data1['title'], "Duplicate Place", "Ошибка: Неверное название места в ответе")
        self.assertEqual(response_data1['lat'], 55.7558, "Ошибка: Неверная широта в ответе")
        self.assertEqual(response_data1['lon'], 37.6173, "Ошибка: Неверная долгота в ответе")
        self.assertEqual(response_data1['color'], "GREEN", "Ошибка: Неверный цвет в ответе")


    def test_place_invalid_color_red(self):
        #Проверяет ошибку при некорректном цвете
        token = get_token()
        data = {
            "title": "Place",
            "lat": 55.7558,
            "lon": 37.6173,
            "color": "red"
        }
        response = requests.post(f"{BASE_URL}/v1/favorites", data=data, cookies={'token': token})
        response_data = response.json()
        self.assertEqual(response.status_code, 200, "Ошибка: Преднамеренная шибка в запросе с неверным цветом")
        self.assertEqual(response_data['title'], "Place", "Ошибка: Неверное название места в ответе")
        self.assertEqual(response_data['lat'], 55.7558, "Ошибка: Неверная широта в ответе")
        self.assertEqual(response_data['lon'], 37.6173, "Ошибка: Неверная долгота в ответе")
        self.assertEqual(response_data['color'], "RED", "Ошибка: Неверный цвет в ответе")

    def test_place_invalid_color_Invalid(self):
        #Проверяет ошибку при некорректном цвете
        token = get_token()
        data = {
            "title": "Place",
            "lat": 55.7558,
            "lon": 37.6173,
            "color": "invalid"
        }
        response = requests.post(f"{BASE_URL}/v1/favorites", data=data, cookies={'token': token})
        response_data = response.json()
        self.assertEqual(response.status_code, 200, "Ошибка: Преднамеренная шибка в запросе с неверным цветом")
        self.assertEqual(response_data['title'], "Place", "Ошибка: Неверное название места в ответе")
        self.assertEqual(response_data['lat'], 55.7558, "Ошибка: Неверная широта в ответе")
        self.assertEqual(response_data['lon'], 37.6173, "Ошибка: Неверная долгота в ответе")
        self.assertEqual(response_data['color'], "RED", "Ошибка: Неверный цвет в ответе")

    def test_place_missing_title(self):
        # Проверяет ошибку при отсутствии названия
        token = get_token()
        data = {
            "lat": 55.7558,
            "lon": 37.6173,
            "color": "BLUE"
        }
        response = requests.post(f"{BASE_URL}/v1/favorites", data=data, cookies={'token': token})
        response_data = response.json()
        self.assertNotEqual(response.status_code, 200, "Ошибка: Сервер не вернул ошибку при отсутствии названия")


    def test_place_missing_lat(self):
        # Проверяет ошибку при отсутствии широты
        token = get_token()
        data = {
            "title": "Test Place",
            "lon": 37.6173,
            "color": "YELLOW"
        }
        response = requests.post(f"{BASE_URL}/v1/favorites", data=data, cookies={'token': token})
        self.assertNotEqual(response.status_code, 200, "Ошибка: Сервер не вернул ошибку при отсутствии широты")

    def test_place_missing_lon(self):
        #Проверяет ошибку при отсутствии долготы
        token = get_token()
        data = {
            "title": "Test Place",
            "lat": 55.7558,
            "color": "GREEN"
        }
        response = requests.post(f"{BASE_URL}/v1/favorites", data=data, cookies={'token': token})
        self.assertNotEqual(response.status_code, 200, "Ошибка: Сервер не вернул ошибку при отсутствии долготы")

    def test_place_invalid_lat(self):
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

    def test_place_invalid_lon(self):
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

    def test_place_overtime(self):
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