"""
5. Выведите n-ое число Фибоначчи не используя временные переменные.
Только циклические операторы и условные операторы. n - вводится
"""
fibonacci_number = int(input())
second_previous = 0
first_previous = 1
number = 0
order = 2
if fibonacci_number == 1:
    print(0)
elif fibonacci_number == 2:
    print(1)
else:
    while order < fibonacci_number:
        number = second_previous + first_previous
        second_previous = first_previous
        first_previous = number
        order += 1
print(number)
