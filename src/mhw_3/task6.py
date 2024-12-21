"""
Дан список целых чисел.
Требуется переместить все ненулевые элементы в левую часть списка, не меняя их порядок,
а все нули - в правую часть.
Порядок ненулевых элементов изменять нельзя, дополнительный список использовать нельзя,
задачу нужно выполнить за один проход по списку. Распечатайте полученный список.
"""


def sorting(numbers: list) -> list:
    """Return a sorted list."""
    number_index = 0

    for num in numbers:
        if num != 0:
            numbers[number_index] = num
            number_index += 1

    for ind, _ in enumerate(numbers[number_index:], start=number_index):
        numbers[ind] = 0

    return numbers


numbers = list(map(int, input('Введите числа через пробел: ').split(' ')))
print(sorting(numbers))
