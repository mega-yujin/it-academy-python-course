"""
Создайте декоратор, который вызывает задекорированную
функцию пока она не выполнится без исключений (но не
более n раз - параметр декоратора). Если превышено количество
попыток, должно быть возбуждено исключение типа TooManyErrors.
Исключение функция может рейзить при вызове рандомно
с помощью модуля random.
"""

import random


class TooManyErrors(Exception):
    pass


def toomanyerrors(number):
    def decorator(func):
        def wrapper():
            errors = 0
            rounds = 0
            while errors < number:
                try:
                    func()
                except ValueError:
                    errors += 1
                rounds += 1
            raise TooManyErrors(f'Failed after {rounds} rounds')
        return wrapper
    return decorator


@toomanyerrors(50)
def russian_roulette():
    if random.choice([True, False]):
        raise ValueError('Random error')


russian_roulette()
