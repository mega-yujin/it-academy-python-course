"""List practice.
Используйте генератор списков чтобы получить следующий: ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
+Используйте на предыдущий список slice чтобы получить следующий: ['ab', 'ad', 'bc'].
Используйте генератор списков чтобы получить следующий ['1a', '2a', '3a', '4a'].
Одной строкой удалите элемент  '2a' из прошлого списка и напечатайте его.
Скопируйте список и добавьте в него элемент '2a' так чтобы в исходном списке этого элемента не было.
"""

some_list = [first + two for first in 'ab' for two in 'bcd']

some_list = some_list[0::2]

next_list = [number + lit for number in '1234' for lit in 'a']

print(next_list.pop(1))

final_list = next_list.copy()
final_list.insert(1,'2a')
