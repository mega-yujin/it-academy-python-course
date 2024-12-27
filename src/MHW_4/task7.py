"""
Напишите функцию для сложения двух матриц любой размерности (сами матрицы естественно одинакового размера).
Матрица может быть представлена в виде вложенного списка, где каждый элемент — это строка матрицы.
Пример матрицы 3x2, где 3 — это количество строк, а 2 — количество столбцов:
[[2, 4], [6, 8], [1, 3]]
"""


def matrix_addition(matrix_one_func, matrix_two_func) -> list:
    """Функция получает на вход два двумерных списка(две матрицы) и складывает их."""
    result = []
    for string_one, string_two in zip(matrix_one_func, matrix_two_func):
        result.append([number_one + number_two for number_one, number_two in zip(string_one, string_two)])
    return result


matrix_one = [[2, 4], [6, 8], [1, 3]]
matrix_two = [[5, 7], [9, 10], [4, 6]]
print(matrix_addition(matrix_one, matrix_two))
