"""
Дан список. Выведите те его элементы, которые встречаются в списке только один раз. Элементы нужно выводить в том порядке, в котором они встречаются в списке.

"""
def unique_elements(lst):
    count_dict = {}
    unique_lst = []

    for item in lst:
        count_dict[item] = count_dict.get(item, 0) + 1

    for item in lst:
        if count_dict[item] == 1:
            unique_lst.append(item)

    return unique_lst

input_list = [7, 2, 3, 5, 12, 56, 8, 0, 5, 7]
result = unique_elements(input_list)
print(result)