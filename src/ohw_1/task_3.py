month = int(input('Введите число: '))

if month < 1:  # noqa: C901 WPS223
    print('значение слишком маленькое')
elif 0 < month < 4:
    print('Зима')
elif 3 < month < 7:
    print('Весна')
elif 6 < month < 10:
    print('Лето')
elif 9 < month < 13:
    print('Осень')
elif month > 12:
    print('значение слишком большое')
