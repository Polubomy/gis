import pprint

import requests

test_results = []

# Базовый URL API
URL = "https://regions-test.2gis.com/"

def get_token():
    response = requests.post(URL + 'v1/auth/tokens')  # POST запрос с пустым телом
    print(f"Статус код получения куки: {response.status_code}")
    if response.status_code == 200:
        token = response.cookies.get('token')
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

# Функция для вывода деталей ответа
def print_response_details(response, token, test_name):
    response_json = response.json()
    result = {
        'test_name': test_name,
        'error_message': None
    }
    print(f"ID: {response_json.get('id')}")
    print(f"Title: {response_json.get('title')}")
    print(f"Latitude: {response_json.get('lat')}")
    print(f"Longitude: {response_json.get('lon')}")
    print(f"Color: {response_json.get('color')}")
    print(f"Token: {token}\n")
    if response.status_code != 200:
        print(f"Ошибка: {response.status_code}")
        error_message = response_json.get('error', {}).get('message')
        print(f"Сообщение об ошибке: {error_message}")
        result['error_message'] = error_message
    test_results.append(result)



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
    response = send_post_request('/v1/favorites', data, token)
    print_response_details(response, token, data['title'])
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
    print_response_details(response, token, data['title'])
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
    print_response_details(response, token, data['title'])
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
    print_response_details(response, token, data['title'])
else:
    print("Токен не получен, тест не выполнен")

# Тест 5: Создание места с пустым title
print("\nТест 5: Создание места с пустым title")
token = get_token()
if token:
    data = {
        'title':'',
        'lat': 55.028254,
        'lon': 82.918501
    }
    response = send_post_request('/v1/favorites', data, token)
    print_response_details(response, token, data['title'])
else:
    print("Токен не получен, тест не выполнен")

# Тест 6: Создание места с минимально допустимым названием
print("\nТест 6: Создание места с минимально допустимым названием")
token = get_token()
if token:
    data = {
        'title': 'Тест 6',
        'lat': 55.028254,
        'lon': 82.918501
    }
    response = send_post_request('/v1/favorites', data, token)
    print_response_details(response, token, data['title'])
else:
    print("Токен не получен, тест не выполнен")

# Тест 7: Создание места с максимально допустимым названием
print("\nТест 7: Создание места с максимально допустимым названием")
token = get_token()
if token:
    data = {
        'title': 'Тест 7 '+'A' * 999,
        'lat': 55.028254,
        'lon': 82.918501
    }
    response = send_post_request('/v1/favorites', data, token)
    print_response_details(response, token, data['title'])
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
    response = send_post_request('/v1/favorites', data, token)
    print_response_details(response, token, data['title'])
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
    response = send_post_request('/v1/favorites', data, token)
    print_response_details(response, token, data['title'])
else:
    print("Токен не получен, тест не выполнен")

# Тест 10: формат данных в виде текста, а не значения
print("\nТест 10: Создание места без необязательного параметра color")
token = get_token()
if token:
    data = {
        'title': 'Тест 10',
        'lat': 55.028254,
        'lon': "82.918501"
    }
    response = send_post_request('/v1/favorites', data, token)
    print_response_details(response, token, data['title'])
    response_json = response.json()
    pprint.pprint(response_json)
else:
    print("Токен не получен, тест не выполнен")

print("\nТест 11: Дубликат")
token = get_token()
if token:
    data = {
        "title": "Duplicate",
        "lat": 55.7558,
        "lon": 37.6173,
        "color": "GREEN"
    }

    response1 = send_post_request('/v1/favorites', data, token)
    response_json1 = response1.json()
    pprint.pprint(response_json1)

    response2 = send_post_request('/v1/favorites', data, token)
    response_json2 = response2.json()
    pprint.pprint(response_json2)


for result in test_results:
    test_name = result['test_name']
    error_message = result['error_message']
    if test_name == '':
        test_name = 'Тест без title'
    print(f"{test_name}: {error_message}")