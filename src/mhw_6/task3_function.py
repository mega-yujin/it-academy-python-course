"""
4.
Дан список чисел.
Посчитайте, сколько в нем пар элементов, равных друг другу.
Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
Входные данные - строка из чисел, разделенная пробелами.
Выходные данные - количество пар.
Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар
"""


def count_pairs(numbers: list) -> int:
    """Return the number of pairs equal to each other."""
    count_dict = {}

    for number in numbers:
        if number in count_dict:
            count_dict[number] += 1
        else:
            count_dict[number] = 1

    pairs_count = 0
    for count in count_dict.values():
        if count > 1:
            pairs_count += count * (count - 1) // 2

    return pairs_count
