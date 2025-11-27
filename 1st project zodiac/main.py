while True:
    date = input("Дата: ")
    months = {
        "января":1,
        "февраля":2,
        "марта":3,
        "апреля":4,
        "мая":5,
        "июня":6,
        "июля":7,
        "августа":8,
        "сентября":9,
        "октября":10,
        "ноября":11,
        "декабря":12
    }
    try:
        d, m = date.split()
        day = int(d)
        month = months[m.lower()]
        md = month * 100 + day
        if 121 <= md <= 219:
            print("Водолей")
        elif 220 <= md <= 320:
            print("Рыбы")
        elif 321 <= md <= 420:
            print("Овен")
        elif 421 <= md <= 521:
            print("Телец")
        elif 522 <= md <= 621:
            print("Близнецы")
        elif 622 <= md <= 722:
            print("Рак")
        elif 723 <= md <= 822:
            print("Лев")
        elif 823 <= md <= 922:
            print("Дева")
        elif 923 <= md <= 1022:
            print("Весы")
        elif 1023 <= md <= 1121:
            print("Скорпион")
        elif 1122 <= md <= 1221:
            print("Стрелец")
        else:
            print("Козерог")
    except (ValueError, KeyError):
        print("Ошибка! Введите дату правильно, например: 25 января")