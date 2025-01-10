"""
Реализовать функцию get_ranges.
которая получает на вход непустой список неповторяющихся целых чисел,
отсортированных по возрастанию,
которая этот список “сворачивает”.
get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) //"0-4,7-8,10"
get_ranges([4,7,10]) // "4,7,10"
get_ranges([2, 3, 8, 9]) // "2-3,8-9"
Задачу поместите в файл task3.py в папке src/hmw_5.
"""


def get_ranges(some_list: list) -> str:
    """Функция принимает список чисел и сворачивает его в строку с диапазонами."""
    result = []
    start = some_list[0]

    for index, number in enumerate(some_list[1:], 1):
        if number != some_list[index - 1] + 1:
            if start == some_list[index - 1]:
                result.append(str(start))
            else:
                result.append(f'{start}-{some_list[index - 1]}')
            start = number

    if start == some_list[-1]:
        result.append(str(start))
    else:
        result.append(f'{start}-{some_list[-1]}')

    return ','.join(result)


print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))  # '0-4,7-8,10'
print(get_ranges([4, 7, 10]))  # '4,7,10'
print(get_ranges([2, 3, 8, 9]))  # '2-3,8-9'
