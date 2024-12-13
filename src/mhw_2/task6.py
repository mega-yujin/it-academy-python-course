"""Определите, является ли число палиндромом.
(читается слева направо и справа налево одинаково).
Число положительное целое, произвольной длины.
Задача требует работать только с числами
(без конвертации числа в строку или что-нибудь еще)
"""


def find_palindrome(number: int) -> bool:
    """
    Determine if a number is a palindrome.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is a palindrome, False otherwise.
    """
    non_reversed_number = number
    reversed_number = 0

    while non_reversed_number > 0:
        reversed_number = non_reversed_number % 10 + reversed_number * 10
        non_reversed_number //= 10

    return number == reversed_number


some_number = int(input('Введите число: '))
print(find_palindrome(some_number))
