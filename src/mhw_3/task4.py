"""
    Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
    Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
    Входные данные - строка из чисел, разделенная пробелами.
    Выходные данные - количество пар.
    Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар
"""

entered_numbers = [int(numeral) for numeral in input().split()]
pairs_number = 0
for number in range(len(entered_numbers)):  # noqa: WPS518
    for sum_number in range(number + 1, len(entered_numbers)):  # noqa: WPS518
        if entered_numbers[number] == entered_numbers[sum_number]:
            pairs_number += 1
print(pairs_number)
