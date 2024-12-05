num = int(input("Введите число: "))
if num == 1:
    result = 'зима'
elif num == 2:
    result = 'весна'
elif num == 3:
    result = 'лето'
elif num == 4:
    result = 'осень'
else:
    print('Нет такой поры года')
    exit()
print(result)
