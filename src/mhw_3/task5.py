"""
    Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
    Элементы нужно выводить в том порядке, в котором они встречаются в списке.
"""

received_list = []
unique_element = list(dict.fromkeys(received_list))
print(unique_element)
