import requests
import pprint

# Базовый URL API
URL = "https://regions-test.2gis.com/"

# Функция для получения токена
def get_token():
    response = requests.post(URL + '/v1/auth/tokens')
    if response.status_code == 200:
        token = response.cookies.get('token')
        print(f"Token - {token}")
        return token
    else:
        print(f"Ошибка при получении токена: {response.status_code}")
        return None

# Функция для отправки POST запроса
def send_post_request(endpoint, data, token):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': f'token={token}'
    }
    response = requests.post(URL + endpoint, data=data, headers=headers)
    return response

# Тест 1: Создание места с корректными данными
print("Тест 1: Создание места с корректными данными")
token = get_token()
if token:
    data = {
        'title': 'Тест 1',
        'lat': 55.028254,
        'lon': 82.918501,
        'color': 'BLUE'
    }
    response = send_post_request('/v1/favorites', data, token) # https://regions-test.2gis.com/v1/favorites?title=Тест+1&lat=55.028254&lon=82.918501&color=BLUE"
    if response.status_code == 200:
        print(f"Статус код: {response.status_code}")
        response_json = response.json()
        pprint.pprint(response_json)
    else:
        print(f"Ошибка при создании места: {response.status_code}")
else:
    print("Токен не получен, тест не выполнен")

# Тест 2: Создание места с некорректной широтой
print("\nТест 2: Создание места с некорректной широтой")
token = get_token()
if token:
    data = {
        'title': 'Тест 2',
        'lat': 100,
        'lon': 82.918501
    }
    response = send_post_request('/v1/favorites', data, token)
    print(f"Статус код: {response.status_code}")
    response_json = response.json()
    pprint.pprint(response_json)

else:
    print("Токен не получен, тест не выполнен")

# Тест 3: Создание места с некорректной долготой
print("\nТест 3: Создание места с некорректной долготой")
token = get_token()
if token:
    data = {
        'title': 'Тест 3',
        'lat': 55.028254,
        'lon': 200
    }
    response = send_post_request('/v1/favorites', data, token)
    print(f"Статус код: {response.status_code}")
    response_json = response.json()
    pprint.pprint(response_json)
else:
    print("Токен не получен, тест не выполнен")

# Тест 4: Создание места с некорректным цветом
print("\nТест 4: Создание места с некорректным цветом")
token = get_token()
if token:
    data = {
        'title': 'Тест 4',
        'lat': 55.028254,
        'lon': 82.918501,
        'color': 'Purple'
    }
    response = send_post_request('/v1/favorites', data, token)
    print(f"Статус код: {response.status_code}")
    response_json = response.json()
    pprint.pprint(response_json)
else:
    print("Токен не получен, тест не выполнен")

# Тест 5: Создание места с пустым title
print("\nТест 5: Создание места с пустым title")
token = get_token()
if token:
    data = {
        'lat': 55.028254,
        'lon': 82.918501
    }
    response = send_post_request('/v1/favorites', data, token)
    print(f"Статус код: {response.status_code}")
    response_json = response.json()
    pprint.pprint(response_json)
else:
    print("Токен не получен, тест не выполнен")

# Тест 6: Создание места с минимально допустимым названием
print("\nТест 6: Создание места с минимально допустимым названием")
token = get_token()
if token:
    data = {
        'title': 'A',
        'lat': 55.028254,
        'lon': 82.918501
    }
    response = send_post_request('v1/favorites', data, token)
    print(f"Статус код: {response.status_code}")
    response_json = response.json()
    pprint.pprint(response_json)
else:
    print("Токен не получен, тест не выполнен")

# Тест 7: Создание места с максимально допустимым названием
print("\nТест 7: Создание места с максимально допустимым названием")
token = get_token()
if token:
    data = {
        'title': 'A' * 999,
        'lat': 55.028254,
        'lon': 82.918501
    }
    response = send_post_request('v1/favorites', data, token)
    print(f"Статус код: {response.status_code}")
    response_json = response.json()
    pprint.pprint(response_json)
else:
    print("Токен не получен, тест не выполнен")

# Тест 8: Создание места с отрицательными значениями широты и долготы
print("\nТест 8: Создание места с отрицательными значениями широты и долготы")
token = get_token()
if token:
    data = {
        'title': 'Тест 8',
        'lat': -55.028254,
        'lon': -82.918501
    }
    response = send_post_request('v1/favorites', data, token)
    print(f"Статус код: {response.status_code}")
    response_json = response.json()
    pprint.pprint(response_json)
else:
    print("Токен не получен, тест не выполнен")

# Тест 9: Создание места без необязательного параметра color
print("\nТест 9: Создание места без необязательного параметра color")
token = get_token()
if token:
    data = {
        'title': 'Тест 9',
        'lat': 55.028254,
        'lon': 82.918501
    }
    response = send_post_request('v1/favorites', data, token)
    print(f"Статус код: {response.status_code}")
    response_json = response.json()
    pprint.pprint(response_json)
else:
    print("Токен не получен, тест не выполнен")
