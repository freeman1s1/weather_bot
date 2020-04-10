import requests


def get_temp(city='Москва'):
    request = requests.get('https://api.openweathermap.org/data/2.5/weather',
                           params={'q': city, 'appid': '45fd8ecaf88326089f3c6db2ed80f83b', 'lang': 'ru'})
    response = request.json()
    if response['cod'] == 200:
        temp = round(response['main']['temp'] - 273.15)

        return str(temp) + '\u2103'
    return 'Введите название города правильно'


def get_data(city):
    request = requests.get('https://api.openweathermap.org/data/2.5/weather',
                           params={'q': city, 'appid': '45fd8ecaf88326089f3c6db2ed80f83b', 'lang': 'ru'})
    response = request.json()
    if response['cod'] == 200:
        desc = response['weather'][0]['description']
        wind = str(response['wind']['speed'])
        return desc + '\n' + 'Скорость ветра: ' + wind + ' м/с'
    return 'Введите название города правильно'


# print(getTemp(input()))
