import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

# Ссылка на сайт, с которого нужно получить данные
url = 'https://horo.mail.ru/prediction/cancer/tomorrow/'  # Замени на реальную ссылку

# Отправляем запрос на сайт
response = requests.get(url)

TOKEN = '8178967594:AAE14G4kmVksV-Y3oyZNBQkxe98JDYQgzws'
CHAT_ID = '1163463444'

# Функция для отправки сообщения
def send_message(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    params = {
        'chat_id': CHAT_ID,
        'text': message
    }
    response = requests.get(url, params=params)
    return response.json()


# Проверяем, успешно ли загружена страница
if response.status_code == 200:
    # Парсим HTML-код страницы
    soup = BeautifulSoup(response.text, 'html.parser')
    horoscope = soup.find('div', class_ = 'b6a5d4949c e45a4c1552')  # Замени на нужный XPath

    if horoscope:
        send_message('Завтра:' + horoscope.text)
    else:
        print('Гороскоп не найден.')
else:
    print('Ошибка при запросе страницы.')
