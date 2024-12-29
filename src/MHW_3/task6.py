"""
Упорядоченный список.
Дан список целых чисел.
Требуется переместить все ненулевые элементы в левую часть списка, не меняя их порядок, а все нули - в правую часть.
Порядок ненулевых элементов изменять нельзя,
дополнительный список использовать нельзя, задачу нужно выполнить за один проход по списку.
Распечатайте полученный список.
"""
list_of_numbers = list(
    map(
        int,
        input('Введите числа через пробел: ').split(),
    ),
)

position = 0
for index, number in enumerate(list_of_numbers):
    if number != 0:
        temp = list_of_numbers[position]
        list_of_numbers[position] = number
        list_of_numbers[index] = temp
        position += 1

print(list_of_numbers)
