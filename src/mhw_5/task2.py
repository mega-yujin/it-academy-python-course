"""Создайте декоратор, который хранит результаты вызовов функции (за все время вызовов, не только текущий запуск программы).
Подопытную функцию можете определить любую (или взять из предыдущих работ) """
import functools

def memoize(func):
    cache = {}

    @functools.wraps(func)
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return wrapper

@memoize
def square(n):
    print("Вычисление квадрата числа", n)
    return n * n

print(square(5))  # Вычисление квадрата числа 5
print(square(5))  # Результат будет взят из кэша


