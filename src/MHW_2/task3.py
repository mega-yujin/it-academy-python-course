"""
3. Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
Например, если было введено "abc cde def", то должно быть выведено "abcdef".
"""
string = input('Введите строку ')
no_space = string.replace(' ', '')
no_repetition = []
for char in no_space:
    if char not in no_repetition:
        no_repetition.append(char)
print(''.join(no_repetition))
