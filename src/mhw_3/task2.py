"""Генератор списков для получения списка ['ab', 'ac', 'ad', 'bb', 'bc', 'bd']"""
result1 = [i + j for i in 'ab' for j in 'bcd']
print(result1)

"""Срезы (slice) для получения списка ['ab', 'ad', 'bc']"""
result2 = result1[::3]
print(result2)

"""Генератор списков для получения списка ['1a', '2a', '3a', '4a']"""
result3 = [str(i) + 'a' for i in range(1, 5)]
print(result3)

"""Одной строкой удалите элемент '2a' из прошлого списка и напечатайте его"""
deleted_item = result3.pop(result3.index('2a'))
print(deleted_item)

"""Скопируйте список и добавьте в него элемент '2a' так, чтобы в исходном списке этого элемента не было"""
new_list = result3.copy()
new_list.append('2a')
print(new_list)
