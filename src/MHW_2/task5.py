"""
5. Выведите n-ое число Фибоначчи не используя временные переменные.
Только циклические операторы и условные операторы. n - вводится
"""
n = int(input())
second_previous = 0
first_previous = 1
number = 0
order = 2
if n == 1:
    print(0)
elif n == 2:
    print(1)
else:
    while order < n:
        number = second_previous + first_previous
        second_previous = first_previous
        first_previous = number
        order += 1
print(number)
