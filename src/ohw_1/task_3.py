seasons = {
    'winter': [12, 1, 2],
    'spring': [3, 4, 5],
    'summer': [6, 7, 8],
    'fall': [9, 10, 11],
}
month = int(input('Введите число: '))

if month < 1:
    print('Значение слишком маленькое')
if month in seasons['winter']:
    print('Зима')
if month in seasons['spring']:
    print('Весна')
if month in seasons['summer']:
    print('Лето')
if month in seasons['fall']:
    print('Осень')
if month > 12:
    print('Значение слишком большое')
