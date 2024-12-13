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
