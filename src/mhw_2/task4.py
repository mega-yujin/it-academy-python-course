"""
Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке. 
Учитывать только английские буквы.
"""

string = input('Введите строку: ')
big = 0
small = 0
for i in string:
    if 'a' <= i <= 'z':
        small += 1
    elif 'A' <= i <= 'Z':
        big += 1
print('Больших: ' , big)
print('Маленьких: ' , small)