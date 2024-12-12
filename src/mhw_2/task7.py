"""Даны: три стороны треугольника.
Требуется: проверить, действительно ли это стороны треугольника.
Если стороны определяют треугольник, найти его площадь.
Если нет, вывести сообщение о неверных данных.
"""

import math


def triangle_inequality_theorem(sides: tuple[int, int, int]) -> bool:
    """
    Determines if a triangle is possible
    :param sides: tuple[int, int, int]: Sides of triangle
    :return: bool: Answer
    """
    return (
        sides[0] + sides[1] > sides[2] and
        sides[0] + sides[2] > sides[1] and
        sides[1] + sides[2] > sides[0]
    )


def area_of_triangle_sides(sides: tuple[int, int, int]) -> float:
    """
    Finds area of the triangle given its sides
    :param sides: tuple[int, int, int]: Sides of triangle
    :return: Area of triangle
    """
    semi_perimeter = (sides[0] + sides[1] + sides[2]) / 2
    return math.sqrt(
        semi_perimeter *
        (semi_perimeter - sides[0]) *
        (semi_perimeter - sides[1]) *
        (semi_perimeter - sides[2])
    )


triangle_sides = (
    int(input('Введите первую сторону: ')),
    int(input('Введите вторую сторону: ')),
    int(input('Введите третью сторону: ')),
)

if triangle_inequality_theorem(triangle_sides):
    print(area_of_triangle_sides(triangle_sides))
else:
    print('Wrong sides')
