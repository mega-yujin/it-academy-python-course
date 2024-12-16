month = int(input('Введите число: '))
if month < 1:
    print('значение слишком маленькое')
elif month > 12:
    print('значение слишком большое')
else:
    season = 'зима'  # по умолчанию считаем зиму
    if 3 <= month <= 5:
        season = 'весна'
    elif 6 <= month <= 8:
        season = 'лето'
    elif 9 <= month <= 11:
        season = 'осень'
    print(season)
