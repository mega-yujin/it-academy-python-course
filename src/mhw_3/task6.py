"""Упорядоченный список.
Дан список целых чисел. Требуется переместить все ненулевые элементы в левую часть списка,
не меняя их порядок, а все нули - в правую часть. Порядок ненулевых элементов изменять нельзя,
дополнительный список использовать нельзя, задачу нужно выполнить за один проход по списку.
Распечатайте полученный список.
"""

numbers = [0, 1, 0, 45, 0, 2, -3, 0, 4, 0, -6]
print(numbers)
for i in numbers:
    if i == 0:
        numbers.append(i)
        numbers.remove(i)
print(numbers)
