num = int(input('Введите число:'))
if num == 1:
    result = 'Зима'
elif num == 2:
    result = 'Весна'
elif num == 3:
    result = 'Лето'
elif num == 4:
    result = 'Осень'
else:
    print('Нет такой поры года')
    exit()
print(result)
