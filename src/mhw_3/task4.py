"""Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
Входные данные - строка из чисел, разделенная пробелами.
Выходные данные - количество пар.
Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар
"""
def count_equal_pairs(numbers_str):
    numbers = numbers_str.split()
    count_dict = {}

    for num in numbers:
        count_dict[num] = count_dict.get(num, 0) + 1

    total_pairs = 0
    for count in count_dict.values():
        total_pairs += count * (count - 1) // 2

    return total_pairs

input_numbers = "1 2 3 2 5 0 3 3"
pairs_count = count_equal_pairs(input_numbers)
print(pairs_count)
