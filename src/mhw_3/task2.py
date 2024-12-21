"""
2.
Используйте генератор списков чтобы получить следующий: ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
Используйте на предыдущий список slice чтобы получить следующий: ['ab', 'ad', 'bc'].
Используйте генератор списков чтобы получить следующий ['1a', '2a', '3a', '4a'].
Одной строкой удалите элемент  '2a' из прошлого списка и напечатайте его.
Скопируйте список и добавьте в него элемент '2a' так чтобы в исходном списке этого элемента не было.
"""

result = [first_sym + second_sym for first_sym in ['a', 'b'] for second_sym in ['b', 'c', 'd']]  # noqa: WPS335

slice_result = result.copy()
slice_result = slice_result[slice(0, 6, 2)]

numbers_with_a = [f'{num}a' for num in range(1, 5)]

numbers_with_a.remove('2a')
print(numbers_with_a)

copied_list = numbers_with_a.copy()
copied_list.append('2a')
