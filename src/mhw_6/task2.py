"""
2.
Создайте декоратор, который вызывает задекорированную функцию пока она не выполнится без исключений
(но не более n раз - параметр декоратора).
Если превышено количество попыток, должно быть возбуждено исключение типа TooManyErrors.
Исключение функция может рейзить при вызове рандомно с помощью модуля random.
"""

import random


class TooManyError(Exception):
    """Исключение, возникающее при превышении количества ошибок."""

    def __init__(self, message):
        """Инициализация сообщения."""
        self.message = message


def retry_on_error(max_attempts):
    """Декоратор, который повторяет выполнение функции до тех пор, пока она не выполнится без исключений."""

    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                attempts += 1
                try:
                    return func(*args, **kwargs)
                except ValueError:
                    print(f'Попытка {attempts} не удалась.')
            raise TooManyError(f'Функция завершилась с ошибками после {attempts} попыток.')

        return wrapper

    return decorator


@retry_on_error(50)
def may_raise_exception():
    """Функция, которая случайным образом вызывает исключение.

    Raises:
        ValueError: Если в процессе выполнения функции возникает ошибка.
    """
    if random.choice([True, False]):  # noqa:  S311
        raise ValueError('Случайная ошибка!')


if __name__ == '__main__':
    try:
        may_raise_exception()
    except TooManyError as error:
        print(error)
