num = int(input('Введите число: '))

match num:
    case 1:
        print('Зима')
    case 2:
        print('Весна')
    case 3:
        print('Лето')
    case 4:
        print('Осень')
    case _:
        print('Нет такой поры года')
