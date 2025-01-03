"""Сложение матриц.
Напишите функцию для сложения двух матриц любой
размерности (сами матрицы естественно одинакового размера).

Матрица может быть представлена в виде вложенного списка,
где каждый элемент — это строка матрицы. Пример матрицы 3x2,
где 3 — это количество строк, а 2 — количество столбцов:
[[2, 4], [6, 8], [1, 3]]
"""


def matrix_addition(
    mtrx1: list[list[int]],
    mtrx2: list[list[int]],
) -> list[list[int]]:
    """
    Sum two matrices.

    Args:
        mtrx1 (list[list[int]]): The first matrix.
        mtrx2 (list[list[int]]): The second matrix.

    Returns:
        list[list[int]]: The resulting matrix.
    """
    if len(mtrx1) != len(mtrx2):
        print('Matrices must have the same dimensions.')
    if any(len(row1) != len(row2) for row1, row2 in zip(mtrx1, mtrx2)):
        print('Matrices must have the same dimensions.')

    return [
        [elem1 + elem2 for elem1, elem2 in zip(row1, row2)]
        for row1, row2 in zip(mtrx1, mtrx2)
    ]


if __name__ == '__main__':
    print(matrix_addition(
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ],
        [
            [10, 11, 12],
            [13, 14, 15],
            [16, 17, 18],
        ],
    ))
