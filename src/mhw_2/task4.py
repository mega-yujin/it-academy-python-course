"""task4.
Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке. 
Учитывать только английские буквы.
"""

string = input('Введите строку: ')
big = 0
small = 0
for ind in string:
    if 'a' <= ind <= 'z':
        small += 1
    elif 'A' <= ind <= 'Z':
        big += 1
print('Больших: ', big)
print('Маленьких: ', small)
