"""
Вводится строка.
Требуется удалить из нее повторяющиеся символы и все пробелы.
Например, если было введено "abc cde def", то должно быть выведено "abcdef".
"""

text = input('Введите строку: ')
result = ''

for symbol in text:
    if symbol not in result and symbol != ' ':
        result += symbol
print(result)
