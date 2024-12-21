"""
5.
Дан список.
Выведите те его элементы, которые встречаются в списке только один раз.
Элементы нужно выводить в том порядке, в котором они встречаются в списке.
"""


def unique_elements(elements: list):
    """Return a list of elements that appear only once in the list."""
    counter = {}

    for element in elements:
        if element in counter:
            counter[element] += 1
        else:
            counter[element] = 1

    return [elem for elem in elements if counter[elem] == 1]


elements = list(input('Введите элементы через пробел: ').split(' '))
print(unique_elements(elements))
