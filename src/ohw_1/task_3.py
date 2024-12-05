seasons = {
    'winter': [12, 1, 2],
    'spring': [3, 4, 5],
    'summer': [6, 7, 8],
    'fall': [9, 10, 11],
}
month = int(input('Введите число: '))

match month:
    case m if m < 1:
        print('Значение слишком маленькое')
    case m if m in seasons['winter']:
        print('Зима')
    case m if m in seasons['spring']:
        print('Весна')
    case m if m in seasons['summer']:
        print('Лето')
    case m if m in seasons['fall']:
        print('Осень')
    case _:
        print('Значение слишком большое')
