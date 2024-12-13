"""task3.
Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы. 
Например, если было введено "abc cde def", то должно быть выведено "abcdef".
"""

string = input('Введите строку: ')
no_space = string.replace(' ', '')
res_string = ''
for ind in no_space:
    if ind not in res_string:
        res_string += ind
print(res_string)
