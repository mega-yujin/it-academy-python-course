"""
    Даны: три стороны треугольника.
    Требуется: проверить, действительно ли это стороны треугольника.
    Если стороны определяют треугольник, найти его площадь.
    Если нет, вывести сообщение о неверных данных
"""

print('Введите стороны треугольника: ')
first_side = int(input('a = '))
second_side = int(input('b = '))
third_side = int(input('c = '))
if (first_side + second_side > third_side
        and first_side + third_side > second_side
        and second_side + third_side > first_side):
    semi_perimeter = (first_side + second_side + third_side) / 2
    triangle_area = ((
                    semi_perimeter * (semi_perimeter - first_side) *
                    (semi_perimeter - second_side) *
                    (semi_perimeter - third_side)) ** 0.5)
    triangle_area = round(triangle_area, 2)
    print(f'Площадь треугольника равна: "{triangle_area}"')
else:
    print('Введены неверные данные')
