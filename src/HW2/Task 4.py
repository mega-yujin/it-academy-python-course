input_string = input("Введите строку: ")

lower = 0
upper = 0

for char in input_string:
    if char.isalpha() and char.isascii():
        if char.islower():
            lower += 1
        elif char.isupper():
            upper += 1

print(f"Количество строчных букв: {lower}")
print(f"Количество прописных букв: {upper}")
