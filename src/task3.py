"""
    Вводится строка.
    Требуется удалить из нее повторяющиеся символы и все пробелы.
"""

entered_line = input('Введите строку: ')
result = ''
for char in entered_line:
    if char != ' ' and char not in result:
        result += char
print(f'Результат: "{result}"')
