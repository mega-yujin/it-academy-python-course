"""Уникальные элементы в списке.
Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
Элементы нужно выводить в том порядке, в котором они встречаются в списке.
"""

some_list = [3, "ololo", 4, 3, 2, 3, 4, 5, 3, "Alice", 8, 3, "alice"]

new_list = []

for elem in some_list:
    if elem in new_list:
        continue
    else:
        new_list.append(elem)
print(new_list)
