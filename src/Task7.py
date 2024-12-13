"""
    Даны: три стороны треугольника.
    Требуется: проверить, действительно ли это стороны треугольника.
    Если стороны определяют треугольник, найти его площадь.
    Если нет, вывести сообщение о неверных данных.
"""

print('Введите стороны треугольника: ')
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
if a + b > c and a + c > b and b + c > a:
    semi_perimeter = (a + b + c) / 2
    s = semi_perimeter
    triangle_area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    triangle_area = round(triangle_area, 2)
    print(f'Площадь треугольника равна: "{triangle_area}"')
else:
    print('Введены неверные данные')
