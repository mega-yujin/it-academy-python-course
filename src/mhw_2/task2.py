"""Найти самое длинное слово во введенном предложении.
Учтите что в предложении есть знаки препинания.
"""

punctuation = ',.!?;:-"'
some_string = input('Введите строку: ')
longest_words = ['']
word_length = 0

for mark in punctuation:
    some_string = some_string.replace(mark, '')
word_list = some_string.split()
for word in word_list:
    if len(word) >= len(longest_words[0]):
        if len(word) > len(longest_words[0]):
            longest_words = []
        longest_words.append(word)
print('Самые длинные слова: {0}'.format(', '.join(longest_words)))
