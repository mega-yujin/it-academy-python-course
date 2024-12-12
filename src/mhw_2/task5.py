"""N=ое число Фибоначчи.
Выведите n-ое число Фибоначчи, используя только временные переменные,
циклические операторы и условные операторы. n - вводится
"""


def find_fibonacci(number: int) -> int:
    """
    Calculates Fibonacci number
    :param number: int: Fibonacci number number
    :return: int: Fibonacci number
    """
    if number <= 0:
        pass
    if number == 1:
        return 0
    if number == 2:
        return 1
    f1 = 0
    f2 = 1
    for _ in range(number - 1):
        f_final = f1 + f2
        f1 = f2
        f2 = f_final
    return f2


f_number = int(input('Номер числа Фибоначчи: '))
print(find_fibonacci(f_number))
