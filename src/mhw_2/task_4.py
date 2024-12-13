"""
Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке.
Учитывать только английские буквы.
"""

text = input('Введите строку: ')
lower = 0
upper = 0

for symbol in text:
    if 'a' <= symbol <= 'z':
        lower += 1
    elif 'A' <= symbol <= 'Z':
        upper += 1

print(f'Маленькие буквы: {lower}')
print(f'Большие буквы: {upper}')
