"""Оформите указанную задачу из прошлых домашних в виде функции и покройте тестами.
Учтите, что в функцию могут быть переданы некорректные значения, здесь может пригодится ‘assertRaises’.
Не нужно переделывать функцию для того чтобы она ловила все возможные ситуации сама"""

def add_matrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Матрицы должны иметь одинаковые размеры")

    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)

    return result

def test_add_matrices():
    matrix1 = [[1, 2], [3, 4]]
    matrix2 = [[5, 6], [7, 8]]
    assert add_matrices(matrix1, matrix2) == [[6, 8], [10, 12]]

    matrix3 = [[1, 2], [3, 4]]
    matrix4 = [[5, 6, 7], [8, 9, 10]]
    try:
        add_matrices(matrix3, matrix4)
    except ValueError as e:
        assert str(e) == "Матрицы должны иметь одинаковые размеры"
    else:
        raise AssertionError("Ожидалось исключение ValueError")

    print("Все тесты пройдены успешно")

test_add_matrices()