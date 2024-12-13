"""
Найти самое длинное слово в введенном предложении.
Учтите что в предложении есть знаки препинания.
Подсказки:
my_string.split([chars]) возвращает список строк.
len(list) - количество элементов в списке
"""

chars = ['!', '?', ',', '.', ':', ';', '-', '"']
my_string = input('Введите предложение: ')

for symbol in chars:
    my_string = my_string.replace(symbol, ' ')

words = (my_string.split(' '))

longest_word = ''
for word in words:
    if len(longest_word) < len(word):
        longest_word = word

print(f'Самое длинное слово: {longest_word}')
