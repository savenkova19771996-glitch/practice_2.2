import requests

url = 'https://www.cbr-xml-daily.ru/daily_json.js'


def kurs_valut():
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return data.get('Valute', {})

valutes = kurs_valut()

while True:
    print("1 - Список всех валют", "\n2 - Поиск валюты по коду")
    Choice = input("Что хотите сделать: ")
    if Choice == '1':
        valutes = kurs_valut()
        print("-" * 20)
        print("   КУРС ВАЛЮТ")
        print("-" * 20)
        for k, v in valutes.items():
            code = k
            name = v['Name']
            nominal = v['Nominal']
            value = v['Value']
            print(f"{code} - {name}: {nominal} ед. = {value} руб.")
    if Choice == '2':
        code = input("Введите код валюты (EUR, USD и т.д. ): ").upper()
        if code in valutes:
            v = valutes[code]
            name = v['Name']
            nominal = v['Nominal']
            value = v['Value']
            print(f"Курс - {code}")
            print(f"{code} - {name}: {nominal} ед. = {value} руб.")
            break
        else:
            print(f"\nВалюта с кодом '{code}' не найдена!")
            break


if __name__ == "__main__":
    kurs_valut()
