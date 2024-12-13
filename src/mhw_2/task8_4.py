"""
4.
Given two integers, n and k, the task is to count how many numbers between 1 and n (inclusive) are divisible by k.
"""

dividend = int(input('Введите делимое (целое число): '))
divider = int(input('Введите делитель (целое число): '))
counter = 0

if dividend == 0 or divider == 0:
    print(0)
else:
    for number in range(1, dividend + 1):
        if number % divider == 0:
            counter += 1
    print(counter)
