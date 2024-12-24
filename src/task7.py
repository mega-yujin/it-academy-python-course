"""
    Даны: три стороны треугольника.
    Требуется: проверить, действительно ли это стороны треугольника.
    Если стороны определяют треугольник, найти его площадь.
    Если нет, вывести сообщение о неверных данных
"""

print('Введите стороны треугольника: ')
side_one = int(input('a = '))
side_two = int(input('b = '))
side_three = int(input('c = '))
if side_one + side_two > side_three and side_one + side_three > side_two and side_two + side_three > side_one:
    semi_prim = (side_one + side_two + side_three) / 2
    triangle_area = (semi_prim * (semi_prim - side_one) * (semi_prim - side_two) * (semi_prim - side_three)) ** 0.5
    triangle_area = round(triangle_area, 2)
    print(f'Площадь треугольника равна: "{triangle_area}"')
else:
    print('Введены неверные данные')
