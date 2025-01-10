"""Decorator.
Создайте декоратор, который хранит результаты вызовов функции
(за все время вызовов, не только текущий запуск программы).
Подопытную функцию можете определить любую (или взять из предыдущих работ)
"""
def save_result(func):

    list_results = []

    def wrapper(*args, **kwargs):
        some_res = func(*args, **kwargs)
        list_results.append(some_res)
        return some_res
    return wrapper

@save_result
def sum_matrix(matrix_1, matrix_2):
    return [[ti + tj for ti, tj in zip(fi, fj)] for fi, fj in zip(matrix_1, matrix_2)]
matrix_1 = [
    [2, 5, 5],
    [6, 8, 6],
    [1, 3, 7]
]
matrix_2 = [
    [2, 4, 7],
    [6, 8, 6],
    [1, 3, 7]
]
print(sum_matrix(matrix_1, matrix_2))
