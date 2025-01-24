""" Создайте декоратор, который вызывает задекорированную функцию пока она не выполнится без исключений (но не более n раз - параметр декоратора).
Если превышено количество попыток, должно быть возбуждено исключение типа TooManyErrors.
Исключение функция может рейзить при вызове рандомно с помощью модуля random"""
import random

class TooManyErrors(Exception):
    pass

def retry(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Error occurred: {type(e).__name__} - {str(e)}")
            raise TooManyErrors(f"Function '{func.__name__}' failed after {n} attempts")
        return wrapper
    return decorator

@retry(7)
def some_function():
    if random.random() < 0.8:
        raise ValueError("Random error")
    return "Success"

try:
    result = some_function()
    print("Function executed successfully:", result)
except TooManyErrors as e:
    print("Too many errors occurred:", e)