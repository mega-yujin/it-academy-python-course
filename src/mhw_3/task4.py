"""Пары элементов.
Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
Входные данные - строка из чисел, разделенная пробелами.
Выходные данные - количество пар.
Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар
"""

numbers = str(input('Введите числа через пробел: ')).split()
count = 0
for first in range(len(numbers)):
    for sekond in range(first + 1, len(numbers)):
        if numbers[first] == numbers[sekond]:
            count += 1
print(f'Количество пар: {count}')