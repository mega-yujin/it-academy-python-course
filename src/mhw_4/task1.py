"""Dict comprehensions.
Создайте словарь с помощью генератора словарей,
так чтобы его ключами были числа от 1 до 20, а значениями кубы этих чисел.
"""


def dict_comprehension_20() -> dict:
    """
    Create a dict with keys from 1 to 20, values are keys cubed.

    Returns:
         dict: Dictionary with keys from 1 to 20, values are keys cubed.
    """
    return {num: num ** 3 for num in range(1, 21)}


if __name__ == '__main__':
    print(dict_comprehension_20())
