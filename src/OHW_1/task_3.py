month = int(input('Введите число: '))
if 0 < month <= 12:
    if 1 <= month <= 3:
        print('зима')
    elif 4 <= month <= 6:
        print('весна')
    elif 7 <= month <= 9:
        print('лето')
    else:
        print('осень')
elif month < 1:
    print('значение слишком маленькое')
else:
    print('значение слишком большое')
