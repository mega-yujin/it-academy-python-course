"""
Дан список целых чисел.
Требуется переместить все ненулевые элементы в левую часть списка, не меняя их порядок,
а все нули - в правую часть.
Порядок ненулевых элементов изменять нельзя, дополнительный список использовать нельзя,
задачу нужно выполнить за один проход по списку. Распечатайте полученный список.
"""


def sorting(numbers: list) -> list:  # noqa: D103
    number_index = 0

    for index in range(len(numbers)):  # noqa: WPS518
        if numbers[index] != 0:
            numbers[number_index] = numbers[index]
            number_index += 1

    for ind in range(number_index, len(numbers)):  # noqa: WPS518
        numbers[ind] = 0

    return numbers


numbers = list(map(int, input('Введите числа через пробел: ').split(' ')))
print(sorting(numbers))
