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
a, b, c = 'a', 2, 'python'  # noqa WPS111
tuple_one_element = (iter([1, 2, 3]),)
for numbers in tuple_one_element[0]:
    print(numbers)
print(len(tuple_one_element))
