"""
    Выведите n-ое число Фибоначчи не используя временные переменные.
    Только циклические операторы и условные операторы. n - вводится
"""

n = int(input('Введите число n: '))
first_fib_numb = 0
second_fib_numb = 1
if n == 0:
    print(first_fib_numb)
elif n == 1:
    print(second_fib_numb)
else:
    num = []
    for num in range(2, n + 1):
        second_fib_numb = first_fib_numb + second_fib_numb
        first_fib_numb = second_fib_numb - first_fib_numb
print(f'n-ое число Фибоначчи: {second_fib_numb}')
