"""
    Посчитать количество строчных (маленьких) и прописных (больших)
    букв во введенной строке. Учитывать только английские буквы.
"""

printed_line = input('Введите строку: ')
big_letter = 0
small_letter = 0
for char in printed_line:
    if 'A' <= char <= 'Z':
        big_letter += 1
    elif 'a' <= char <= 'z':
        small_letter += 1
print(f'Количество больших букв: {big_letter} \nКоличество маленьких букв: {small_letter}')
