"""
Выведите n-ое число Фибоначчи.
Используя только временные переменные, циклические операторы и условные операторы.
n - вводится
"""

number_fibonacci = int(input('Введите n: '))

if number_fibonacci == 1:
    print(0)
elif number_fibonacci == 2:
    print(1)
else:
    first_number, second_number = 0, 1
    for _ in range(number_fibonacci - 1):
        first_number, second_number = second_number, first_number + second_number

    print(first_number)
