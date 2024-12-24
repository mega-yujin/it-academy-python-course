"""
    Выведите n-ое число Фибоначчи не используя временные переменные.
    Только циклические операторы и условные операторы. n - вводится
"""

n = int(input('Введите число n: '))  # noqa: WPS111
first_fib_numb = 0
second_fib_numb = 1
if n == 0:  # noqa: WPS111
    print(first_fib_numb)
elif n == 1:  # noqa: WPS111
    print(second_fib_numb)
else:
    number = []
    for number in range(2, n + 1):  # noqa: WPS440, B007
        second_fib_numb = first_fib_numb + second_fib_numb
        first_fib_numb = second_fib_numb - first_fib_numb
print(f'n-ое число Фибоначчи: {second_fib_numb}')
