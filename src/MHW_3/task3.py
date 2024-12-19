"""
Tuple practice.
Создайте список ['a', 'b', 'c'] и сделайте из него кортеж.
Создайте кортеж ('a', 'b', 'c'), И сделайте из него список.
Сделайте следующие присвоения одной строкой a = 'a', b=2, c=’python’.
Создайте кортеж из одного элемента,
чтобы при итерировании по этому элементу последовательно выводились значения 1, 2, 3.
Убедитесь что len() исходного кортежа возвращает 1.
"""
created_list = ['a', 'b', 'c']
tuple_from_created_list = tuple(created_list)
first_element, second_element, third_element = 'a', 2, 'python'
one_element_tuple = ([1, 2, 3],)
print(len(one_element_tuple))
