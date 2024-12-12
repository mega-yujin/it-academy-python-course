input_string = input("Введите строку: ")
unique_chars = []
result = ""

for char in input_string:
    if char not in unique_chars and char != " ":
        unique_chars.append(char)
        result += char

print(f"Результат: {result}")
