"""Сохранить результат.
Создайте декоратор, который хранит результаты вызовов функции
(за все время вызовов, не только текущий запуск программы).
Подопытную функцию можете определить любую
(или взять из предыдущих работ)
"""


def save_result(func):
    def wrapper(*args):
        with open('saved_results.txt', 'a') as file:
            file.write(str(func(*args)) + '\n')
        return func(*args)
    return wrapper


@save_result
def find_fibonacci(number: int) -> int:
    """
    Calculate the nth Fibonacci number.

    Args:
        number (int): The position in the Fibonacci sequence.

    Returns:
        int: The nth Fibonacci number.
    """
    if number == 1:
        return 0
    if number == 2:
        return 1

    f1, f2 = 0, 1
    for _ in range(number - 2):
        f1, f2 = f2, f1 + f2

    return f2


print(find_fibonacci(20))
