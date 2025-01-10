"""Get_ranges.
Реализовать функцию get_ranges которая получает на вход непустой список неповторяющихся целых чисел,
отсортированных по возрастанию, которая этот список “сворачивает”.
get_ranges([0, 1, 2, 3, 4, 7, 8, 10])  // "0-4,7-8,10"
get_ranges([4,7,10])  // "4,7,10"
get_ranges([2, 3, 8, 9])  // "2-3,8-9"
"""


def get_ranges(unsorted: list):
    result = ''
    start = unsorted[0]
    finish = unsorted[0]
    for index, element in enumerate(unsorted[1:]):
        if element == finish + 1:
            finish = element
        else:
            if start == finish:
                result += (f'{start},')  # noqa: WPS336
            else:
                result += (f'{start}-{finish},')  # noqa: WPS336
            start = element
            finish = element
    if start == finish:
        result += (f'{start}')  # noqa: WPS336
    else:
        result += (f'{start}-{finish}')  # noqa: WPS336
    return result


print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
print(get_ranges([4, 7, 10]))
print(get_ranges([2, 3, 8, 9]))
