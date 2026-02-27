import requests
from requests.exceptions import ConnectionError

status_code = {
    200: "Доступен",
    202: "Запрос принят",
    404: "Не найден",
    500: "Не доступен",
    403: "Вход запрещён"
}
try:
    k = requests.get('https://github.com/')
    choice_1 = k.status_code
    status_text = status_code.get(choice_1)
    print(f"1) {k.url} - {status_text} - {choice_1}")

    site2 = requests.get('https://www.binance.com/en')
    choice_2 = site2.status_code
    status_text_2 = status_code.get(choice_2)
    print(f"2) {site2.url} - {status_text_2} - {choice_2}")

    site3 = requests.get('https://tomtit.tomsk.ru/')
    choice_3 = site3.status_code
    status_text_3 = status_code.get(choice_3)
    print(f"3) {site3.url} - {status_text_3} - {choice_3}")

    site4 = requests.get('https://jsonplaceholder.typicode.com/')
    choice_4 = site4.status_code
    status_text_4 = status_code.get(choice_4)
    print(f"4) {site4.url} - {status_text_4} - {choice_4}")

    site5 = requests.get('https://moodle.tomtit-tomsk.ru')
    choice_5 = site5.status_code
    status_text_5 = status_code.get(choice_5)
    print(f"5) {site5.url} - {status_text_5} - {choice_5}")
except ConnectionError as e:
    print("Отсутствует подключение к Интернету")

