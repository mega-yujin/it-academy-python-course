"""N=ое число Фибоначчи.
Выведите n-ое число Фибоначчи, используя только временные переменные,
циклические операторы и условные операторы. n - вводится
"""


def find_fibonacci(number: int) -> int:
    """
    Calculate the nth Fibonacci number.

    Args:
        number (int): The position in the Fibonacci sequence.

    Returns:
        int: The nth Fibonacci number.
    """
    if number == 1:
        return 0
    if number == 2:
        return 1

    f1, f2 = 0, 1
    for _ in range(number - 2):
        f1, f2 = f2, f1 + f2

    return f2


f_number = int(input('Номер числа Фибоначчи: '))
print(find_fibonacci(f_number))
