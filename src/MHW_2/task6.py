"""
6. Определите, является ли число палиндромом (читается слева направо и справа налево одинаково).
Число положительное целое, произвольной длины. Задача требует работать только с числами
(без конвертации числа в строку или что-нибудь еще)
"""
number = int(input('Введите число: '))
true_number = number
reversed_number = 0
while number > 0:
    figure = number % 10
    reversed_number = reversed_number * 10 + figure
    number = number // 10
if true_number == reversed_number:
    print('Число - палиндром')
else:
    print('Число не палиндром')
