"""task2.
Найти самое длинное слово в введенном предложении. Учтите что в предложении есть знаки препинания.
Подсказки:
my_string.split([chars]) возвращает список строк.
len(list) - количество элементов в списке
"""

string = input('Введите предложение: ')
deleted_symbol = ',.?:-"'
for ind in deleted_symbol:
    string = string.replace(ind, '')

words = string.split()

long_word = max(words, key=len)

print(long_word)
