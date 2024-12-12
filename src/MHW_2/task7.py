"""
7. Даны: три стороны треугольника. Требуется: проверить, действительно ли это стороны треугольника.
Если стороны определяют треугольник, найти его площадь.
Если нет, вывести сообщение о неверных данных.
"""
side_one = int(input('Введите длину первой стороны: '))
side_two = int(input('Введите длину второй стороны: '))
side_three = int(input('Введите длину третьей стороны: '))
if (side_one + side_two) > side_three and (side_two + side_three) > side_one and (side_one + side_three) > side_two:
    half_perimeter = (side_one + side_two + side_three) / 2
    square = (half_perimeter * (half_perimeter - side_one) * (half_perimeter - side_two) * (half_perimeter - side_three)) ** 0.5
    print(f'Площадь треугольника равна {square}')
else:
    print('Данного треугольника не существует')
