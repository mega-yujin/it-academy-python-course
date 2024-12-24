"""
    Используйте генератор списков, чтобы получить следующий: ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
    Используйте на предыдущий список slice, чтобы получить следующий: ['ab', 'ad', 'bc'].
    Используйте генератор списков, чтобы получить следующий ['1a', '2a', '3a', '4a'].
    Одной строкой удалите элемент '2a' из прошлого списка и напечатайте его.
    Скопируйте список и добавьте в него элемент '2a' так, чтобы в исходном списке этого элемента не было.
"""

generated_list = [first_letter + next_letter for first_letter in ['a', 'b'] for next_letter in ['b', 'c', 'd']]  # noqa: WPS335
print(generated_list)
slice_list = generated_list[::2]
print(slice_list)
next_generated_list = [f'{number}a' for number in range(1, 5)]
print([combination for combination in next_generated_list if combination != '2a'])
next_generated_list.remove('2a')
copied_list = next_generated_list.copy()
copied_list.append('2a')
print(copied_list)
