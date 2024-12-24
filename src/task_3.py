month = int(input('Введите число: '))
if month < 1:  # noqa: WPS223
    print('значение слишком маленькое')
elif 1 <= month <= 2 or month == 12:  # noqa: WPS223
    print('Зима')
elif 3 <= month <= 5:  # noqa: WPS223
    print('Весна')
elif 6 <= month <= 8:  # noqa: WPS223
    print('Лето')
elif 9 <= month <= 11:  # noqa: WPS223
    print('Осень')
else:
    print('значение слишком большое')
