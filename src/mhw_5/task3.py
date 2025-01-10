"""Свернуть список.
Реализовать функцию get_ranges которая получает на вход
непустой список неповторяющихся целых чисел, отсортированных
по возрастанию, которая этот список “сворачивает”.
get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
get_ranges([4,7,10]) // "4,7,10"
get_ranges([2, 3, 8, 9]) // "2-3,8-9"
"""


def get_ranges(unsorted: list) -> str:
    """
    Collapse list, skipping consecutive numbers, leaving first and last.

    Args:
        unsorted (list): Non collapsed list.

    Returns:
        Collapsed list as a string.
    """
    result = ''
    start = unsorted[0]
    end = unsorted[0]
    for index, element in enumerate(unsorted[1:]):
        if element == end + 1:
            end = element
        else:
            if start == end:
                result = '{0}{1},'.format(result, start)
            else:
                result = '{0}{1}-{2},'.format(result, start, end)
            start = element
            end = element
    if start == end:
        result = '{0}{1}'.format(result, start)
    else:
        result = '{0}{1}-{2}'.format(result, start, end)
    return result


print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
print(get_ranges([4, 7, 10]))
print(get_ranges([2, 3, 8, 9]))
