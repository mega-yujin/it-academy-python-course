"""
5.
This function should take a list of strings and determine the longest common prefix among all the strings.
If there is no common prefix, it should return an empty string.
"""

words = list(input('Введите слова: ').split(' '))

if words:
    prefix = words[0]

    for word in words[1:]:
        while word[:len(prefix)] != prefix and prefix:
            prefix = prefix[:-1]
        if not prefix:
            print('Нет префикса')

    print(prefix)
else:
    print('Пустой список')
