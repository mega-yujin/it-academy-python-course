"""Посчитать количество строчных (маленьких) и прописных (больших)
букв во введенной строке. Учитывать только английские буквы.
"""

some_string = input('Введите строку: ')
lower_num = 0

new_string = ''.join([i for i in some_string if i.isalpha() and i.isascii()])
for i in new_string:
    if i.islower():
        lower_num += 1
upper_num = len(new_string) - lower_num

print('Есть {0} строчных букв и {1} прописных'.format(lower_num, upper_num))
