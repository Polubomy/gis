import requests
import json

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
        'title': 'Тестовое место 1',
        'lat': 55.028254,
        'lon': 82.918501,
        'color': 'BLUE'
    }
    response = send_post_request('/v1/favorites', data, token)
    if response.status_code == 200:
        print(f"Статус код: {response.status_code}")
        print(f"Ответ: {response.json()}")
    else:
        print(f"Ошибка при создании места: {response.status_code}")

# Тест 2: Создание места с некорректной широтой
print("\nТест 2: Создание места с некорректной широтой")
token = get_token()
if token:
    data = {
        'title': 'Тестовое место 2',
        'lat': 100,
        'lon': 82.918501
    }
    response = send_post_request('/v1/favorites', data, token)
    print(f"Статус код: {response.status_code}")
    print(f"Ответ: {response.json()}")

# Тест 3: Создание места с некорректной долготой
print("\nТест 3: Создание места с некорректной долготой")
token = get_token()
if token:
    data = {
        'title': 'Тестовое место 3',
        'lat': 55.028254,
        'lon': 200
    }
    response = send_post_request('/v1/favorites', data, token)
    print(f"Статус код: {response.status_code}")
    print(f"Ответ: {response.json()}")

# Тест 4: Создание места с некорректным цветом
print("\nТест 4: Создание места с некорректным цветом")
token = get_token()
if token:
    data = {
        'title': 'Тестовое место 4',
        'lat': 55.028254,
        'lon': 82.918501,
        'color': 'Purple'
    }
    response = send_post_request('/v1/favorites', data, token)
    print(f"Статус код: {response.status_code}")
    print(f"Ответ: {response.json()}")

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
    print(f"Ответ: {response.json()}")