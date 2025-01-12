"""
2.
Создайте декоратор, который хранит результаты вызовов функции (за все время вызовов,
не только текущий запуск программы).
Подопытную функцию можете определить любую (или взять из предыдущих работ).
"""
import json


def cache_results(func):
    """Return or writes the result from the cache."""
    cache_file = f'{func.__name__}_cache.json'

    try:
        with open(cache_file, 'r') as file_1:
            results = json.load(file_1)
    except FileNotFoundError:
        results = {}

    def wrapper(*args):
        key = str(args)

        if key in results:
            print('результат из кэша:')
            return results[key]

        result = func(*args)
        results[key] = result

        with open(cache_file, 'w') as file_2:
            json.dump(results, file_2)
        return result

    return wrapper


@cache_results
def fibonacci(number_fibonacci: int):
    """Return the nth Fibonacci number."""
    first_number, second_number = 0, 1

    if number_fibonacci == 1:
        return 0
    elif number_fibonacci == 2:
        return 1
    else:
        for _ in range(number_fibonacci - 1):  # noqa: WPS503
            first_number, second_number = second_number, first_number + second_number
        return first_number


number_fibonacci = int(input('Введите n: '))
print(fibonacci(number_fibonacci))
print(fibonacci(number_fibonacci))
