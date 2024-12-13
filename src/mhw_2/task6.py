"""
Определите, является ли число палиндромом (читается слева направо и справа налево одинаково). 
 Число положительное целое, произвольной длины. Задача требует работать только с числами 
 (без конвертации числа в строку или что-нибудь еще)

"""

start_number = int(input('Введите целое число: '))
number_1 = start_number
number_2 = 0

while number_1 > 0:
    some_number = number_1 % 10
    number_1 = number_1 // 10
    number_2 = number_2 * 10 + some_number

if number_2 == start_number:
    print(True)
else:
    print(False)
