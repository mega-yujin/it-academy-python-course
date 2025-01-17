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
    def __init__(self, message):
        self.message = message


def toomanyerrors(number):
    def decorator(func):
        def wrapper():
            rounds = 0
            while rounds < number:
                try:
                    func()
                except ValueError:
                    raise TooManyErrors(f'Failed after {rounds} rounds')
                rounds += 1
        return wrapper
    return decorator


@toomanyerrors(2)
def russian_roulette():
    if random.choice([True, False]):
        raise ValueError('Random error')


russian_roulette()
print('Success!')
