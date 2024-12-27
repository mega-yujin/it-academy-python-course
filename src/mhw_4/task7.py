"""Сложение матриц.
Напишите функцию для сложения двух матриц любой размерности
(сами матрицы естественно одинакового размера).
"""

matrix_1 = [
    [2, 4, 5, 15],
    [6, 8, 6, 15],
    [1, 3, 7, 15]
]
matrix_2 = [
    [2, 4, 5, 15],
    [6, 8, 6, 15],
    [1, 3, 7, 15]
]

def sum_matrix(matrix_1, matrix_2):
    return [[ti + tj for ti, tj in zip(fi, fj)] for fi, fj in zip(matrix_1, matrix_2)]
print(sum_matrix(matrix_1, matrix_2))
