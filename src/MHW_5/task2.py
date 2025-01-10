"""
Создайте декоратор, который хранит результаты вызовов функции.
(за все время вызовов, не только текущий запуск программы).
Подопытную функцию можете определить любую (или взять из предыдущих работ)
Задачу поместите в файл task2.py в папке src/hmw_5.
"""


def result_keeper(func):
    """Декоратор, который сохраняет результаты вызовов функции."""
    keeper = []

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        keeper.append(result)
        return result
    return wrapper


@result_keeper
def matrix_addition(matrix_one_func, matrix_two_func) -> list:
    """Функция получает на вход два двумерных списка(две матрицы) и складывает их."""
    result = []
    for string_one, string_two in zip(matrix_one_func, matrix_two_func):
        result.append([number_one + number_two for number_one, number_two in zip(string_one, string_two)])
    return result


matrix_one = [[2, 4], [6, 8], [1, 3]]
matrix_two = [[5, 7], [9, 10], [4, 6]]
print(matrix_addition(matrix_one, matrix_two))
