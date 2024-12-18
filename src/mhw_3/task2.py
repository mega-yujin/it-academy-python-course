"""List practice.
1. Используйте генератор списков, чтобы получить следующий:
['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
2. Используйте на предыдущий список slice, чтобы получить следующий:
['ab', 'ad', 'bc'].
3. Используйте генератор списков, чтобы получить следующий
['1a', '2a', '3a', '4a'].
4. Одной строкой удалите элемент '2a' из прошлого списка
и напечатайте его.
5. Скопируйте список и добавьте в него элемент '2a',
так чтобы в исходном списке этого элемента не было.
"""

some_list1 = [char_1 + char_2 for char_1 in 'ab' for char_2 in 'bcd']

some_list2 = some_list1
some_list2 = some_list2[slice(0, 6, 2)]

some_list3 = [f'{num}a' for num in range(1, 5)]

some_list4 = some_list3[:]
some_list4.remove('2a')
print(some_list4)

some_list5 = some_list4[:]
some_list5.append('2a')
