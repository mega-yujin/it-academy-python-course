"""
7.
Напишите функцию для сложения двух матриц любой размерности (сами матрицы естественно одинакового размера).
Матрица может быть представлена в виде вложенного списка, где каждый элемент — это строка матрицы.
Пример матрицы 3x2, где 3 — это количество строк, а 2 — количество столбцов.
"""


def calculate_matrices(matrix1, matrix2):
    """Return the result of adding two matrices."""
    result = []

    for num1, value in enumerate(matrix1):
        row = []
        for num2, _ in enumerate(value):
            row.append(matrix1[num1][num2] + matrix2[num1][num2])
        result.append(row)

    return result


matrix_a = [
    [2, 4, 1],
    [6, 8, 5],
    [1, 3, 4],
]

matrix_b = [
    [1, 2, 4],
    [3, 4, 1],
    [5, 6, 2],
]

result_matrix = calculate_matrices(matrix_a, matrix_b)

print('Результат сложения матриц:')
for row in result_matrix:
    print(row)
