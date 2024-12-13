"""
3.
This function should take a string as an input and return the count of vowels (a, e, i, o, u) in the string.
The function should be case-insensitive.
"""

text = input('Введите текст:')
counter = 0
for symbol in text.lower():
    if symbol in 'aeiou':
        counter += 1
print(counter)
