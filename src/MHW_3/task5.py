"""
Уникальные элементы в списке.
Дан список.
Выведите те его элементы, которые встречаются в списке только один раз.
Элементы нужно выводить в том порядке, в котором они встречаются в списке.
"""

some_list = [3, 'ololo', 4, 3, 2, 3, 4, 5, 3, 'Alice', 8, 3, 'alice']
tuple_list = set()
new_list = []
for element in some_list:
    if element not in tuple_list:
        tuple_list.add(element)
        new_list.append(element)
print(new_list)
