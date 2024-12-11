"""Вводится строка.
Требуется удалить из нее повторяющиеся символы и все пробелы.
Например, если было введено "abc cde def", то должно быть выведено "abcdef".
"""

some_string = input('Введите строку: ').replace(' ', '')
modified_string_list = []

for i in some_string:
    if i not in modified_string_list:
        modified_string_list.append(i)

print(''.join(modified_string_list))
