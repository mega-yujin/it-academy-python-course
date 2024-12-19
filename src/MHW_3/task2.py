"""
2. List practice.
Используйте генератор списков, чтобы получить следующий: ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
Используйте на предыдущий список slice, чтобы получить следующий: ['ab', 'ad', 'bc'].
Используйте генератор списков, чтобы получить следующий ['1a', '2a', '3a', '4a'].
Одной строкой удалите элемент '2a' из прошлого списка и напечатайте его.
Скопируйте список и добавьте в него элемент '2a' так, чтобы в исходном списке этого элемента не было.
"""
first_list = [element_one + element_two for element_one in 'ab' for element_two in 'bcd']
sliced_list = first_list[::2]
second_list = [str(element).join(['', 'a']) for element in range(1, 5)]
new_list = second_list.copy()
new_list.append('2a')
