"""
Даны: три стороны треугольника.
Требуется: проверить, действительно ли это стороны треугольника.
Если стороны определяют треугольник, найти его площадь.
Если нет, вывести сообщение о неверных данных.
"""

side_1, side_2, side_3 = [int(value) for value in input('Введите через пробел стороны треугольника: ').split(' ')]

if (side_1 + side_2 > side_3) and (side_1 + side_3 > side_2) and (side_2 + side_3 > side_1):
    semi_perimeter = (side_1 + side_2 + side_3) / 2
    area = (semi_perimeter * (semi_perimeter - side_1) * (semi_perimeter - side_2) * (semi_perimeter - side_3)) ** 0.5
    print(f'Площадь треугольника: {area}')
else:
    print('Неверные данные: указанные стороны не могут образовать треугольник')
