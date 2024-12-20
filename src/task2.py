"""
    Найти самое длинное слово во введённом предложении.
    Учтите что в предложении есть знаки препинания.
    Возможные знаки препинания: '. , ! ? - ‘ “”'
"""

entered_sentence = input('Введите предложение: ')
possible_punctuation = ['.', ',', '!', '?', '‘', '’', '“', '”']
for char in possible_punctuation:
    entered_sentence = entered_sentence.replace(char, '')
words = entered_sentence.split()
longest_word = ''
for word in words:
    if len(word) > len(longest_word):
        longest_word = word
print(f'Самое длинное слово: "{longest_word}"')
