"""
4. Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке.
Учитывать только английские буквы.
"""
string = input('Введите строку ')
lower = 0
upper = 0
for char in string:
    if char.isalpha():
        if char.islower():
            lower += 1
        else:
            upper += 1
print(f'Количество строчных (маленьких) букв: {lower}, количество прописных (больших) букв: {upper}')
