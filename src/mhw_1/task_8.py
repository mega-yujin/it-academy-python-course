"""
1.
Identify whether a given integer is positive, negative, or zero.
Return a respective string: "positive", "negative" or "zero".
"""

num = int(input('Введите число:'))
if num == 0:
    print('zero')
elif num < 0:
    print('negative')
else:
    print('positive')

"""
2.
Determine the remainder from division of two positive integers.
"""

dividend = int(input('Введите число:'))
divisor = int(input('Введите число:'))
print(dividend % divisor)

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

"""
4.
Given two integers, n and k, the task is to count how many numbers between 1 and n (inclusive) are divisible by k.
"""

dividend = int(input('Введите делимое (целое число): '))
divider = int(input('Введите делитель (целое число): '))
counter = 0

if dividend == 0 or divider == 0:
    print(0)
else:
    for i in range(1, dividend + 1):
        if i % divider == 0:
            counter += 1
    print(counter)

"""
5.
This function should take an list of strings and determine the longest common prefix among all the strings. 
If there is no common prefix, it should return an empty string.
"""

# words = list(input().split(' '))
words = ["application", "apple", "appetizer"]

if not words:
    print('Пустой список')
else:
    prefix = words[0]

    for word in words[1:]:
        while word[:len(prefix)] != prefix and prefix:
            prefix = prefix[:-1]
        if not prefix:
            print('Нет префикса')

    print(prefix)
