"""Decorator.
Создайте декоратор, который вызывает задекорированную функцию пока она не выполнится без
исключений (но не более n раз - параметр декоратора). Если превышено количество попыток,
должно быть возбуждено исключение типа TooManyErrors. Исключение функция может рейзить при
вызове рандомно с помощью модуля random.
"""

import random


class TooManyErrors(Exception):
    ...  # noqa: WPS604


def decor(numbers):  # noqa: C901 WPS231
    def decorator(func):  # noqa: WPS231
        def wrapper():
            count = 0
            while count < numbers:
                try:
                    return func()
                except:  # noqa: E722
                    count += 1
                    if count >= numbers:
                        raise TooManyErrors('Лимит попыток исчерпан')  # noqa: WPS220
        return wrapper
    return decorator


numb_att = int(input('количество попыток: '))


@decor(numb_att)
def new_func():
    if random.choice([True, False]):
        raise ValueError('Ошибка')
    return 'Получилось'


try:
    print(new_func())
except TooManyErrors as problem:
    print(problem)
