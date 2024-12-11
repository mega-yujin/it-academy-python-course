"""Найти самое длинное слово во введенном предложении.
Учтите что в предложении есть знаки препинания.
"""

punctuation = r',.!?;:'
some_string = input('Введите строку: ')
longest_words = ['']
word_length = 0

for i in punctuation:
    some_string = some_string.replace(i, '')
word_list = some_string.split()
for i in word_list:
    if len(i) >= len(longest_words[0]):
        if len(i) > len(longest_words[0]):
            longest_words = []
        longest_words.append(i)
print('Самые длинные слова: {0}'.format(longest_words))
