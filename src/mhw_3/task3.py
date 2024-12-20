"""
    Создайте список ['a', 'b', 'c'] и сделайте из него кортеж.
    Создайте кортеж ('a', 'b', 'c'), И сделайте из него список.
    Сделайте следующие присвоения одной строкой a = 'a', b=2, c=’python’.
    Создайте кортеж из одного элемента, чтобы при итерировании по этому элементу
    последовательно выводились значения 1, 2, 3.
    Убедитесь что len() исходного кортежа возвращает 1.
"""

some_list = ['a', 'b', 'c']
some_tuple = tuple(some_list)
some_next_tuple = ('a', 'b', 'c')
some_next_list = list[some_next_tuple]
a, b, c = 'a', 2, 'python'
tuple_one_element = (1,)
for tuple_one_elem in range(1, 4):
    print(tuple_one_elem)
print(len(tuple_one_element))
