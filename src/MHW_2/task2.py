"""
2. Найти самое длинное слово в введенном предложении. Учтите что в предложении есть знаки препинания.
Подсказки:
my_string.split([char]) возвращает список строк.
len(list) - количество элементов в списке
возможные знаки препинания: . , ! ? - ‘ “”
"""
my_string = input('Введите предложение ')
marks = '.,!?-‘“”'
words = ''.join(word for word in my_string if word not in marks)
list_words = words.split()
max_word = ''
for word in list_words:
    if len(word) > len(max_word):
        max_word = word
print(f'Самое длинное слово - {max_word}')
