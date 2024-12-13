"""task5.
Выведите n-ое число Фибоначчи не используя временные переменные. 
Только циклические операторы и условные операторы. n - вводится
"""

number = int(input('Введите n-ое число Фибоначчи: '))
first = 0
two = 1
if number == 1:
    print(0)
    SystemExit()
else:
    for ind in range(0, number - 2):
        summ = first + two
        first = two
        two = summ
    print(two)
