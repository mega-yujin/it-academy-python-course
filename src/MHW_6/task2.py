"""
Создайте декоратор, который вызывает задекорированную функцию.
пока она не выполнится без исключений (но не более n раз - параметр декоратора).
Если превышено количество попыток, должно быть возбуждено исключение типа TooManyErrors.
Исключение функция может рейзить при вызове рандомно с помощью модуля random.
"""
import random


class TooManyAttemptsError(Exception):
    """Исключение для отлова превышения количества попыток."""


def call_function(number_of_calls):
    """Декоратор, который принимает аргумент, определяющий разрешенное количество попыток."""

    def decorator(func):
        def wrapper():
            calls = 0
            while calls < number_of_calls:
                try:
                    return func()
                except ValueError:
                    calls += 1
            raise TooManyAttemptsError('Количество попыток превышено')
        return wrapper
    return decorator


number = int(input('Введите количество разрешенных попыток: '))


@call_function(number)
def random_func():
    """
    Функция, которая рандомно рейзит исключения ValueError.

    Raises:
        ValueError: Ошибка выбирается случайным образом
    """
    if random.choice([True, False]): # type: ignore # noqa:  S311
        raise ValueError('Произошла ошибка')
    return 'Функция выполнена успешно'


if __name__ == '__main__':
    try:
        print(random_func())
    except TooManyAttemptsError as error:
        print(error)
