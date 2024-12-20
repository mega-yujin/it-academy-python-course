"""
    Определите, является ли число палиндромом (читается слева направо и справа налево одинаково).
    Число положительное целое, произвольной длины.
    Задача требует работать только с числами (без конвертации числа в строку или что-нибудь еще).
"""

entered_number = int(input('Введите положительное целое число: '))
if entered_number < 0:
    print('Ошибка, введите положительное целое число')
else:
    first_number = entered_number
    mirrored_number = 0
    while entered_number > 0:
        numeric = entered_number % 10
        mirrored_number = mirrored_number * 10 + numeric
        entered_number = entered_number // 10
    if first_number == mirrored_number:
        print('Число является палиндромом')
    else:
        print('Число не является палиндромом')
