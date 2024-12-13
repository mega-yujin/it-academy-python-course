"""
Выведите n-ое число Фибоначчи не используя временные переменные. 
Только циклические операторы и условные операторы. n - вводится
"""

n = int(input('Введите n-ое число Фибоначчи: '))
first = 0
two = 1
counter = 0
if n == 1:
    print(0)
    SystemExit()
else:
    for counter in range(0, n - 2):
        summ = first + two
        first = two
        two = summ
    print(two)
