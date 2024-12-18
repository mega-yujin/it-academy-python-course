"""Пары элементов.
Дан список. Выведите те его элементы, которые встречаются
в списке только один раз. Элементы нужно выводить
в том порядке, в котором они встречаются в списке.
"""


def unique_elements(seq: list) -> list:
    """
    Return unique elements of list.
    :param seq: List to format.
    :return: Unique elements.
    """
    return [element for element in seq if seq.count(element) == 1]


print(unique_elements(input('Введите последовательность: ').split()))
