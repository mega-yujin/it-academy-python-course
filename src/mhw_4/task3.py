"""
3.
Даны два списка чисел.
Посчитайте, сколько различных чисел содержится одновременно как в первом списке, так и во втором.
list1 = [1, 2, 3, 4, 3, 5, 6, 7, 8]
list2 = [4, 6, 5, 7, 8, 9, 10, 11, 9, 12]
"""

list1 = [1, 2, 3, 4, 3, 5, 6, 7, 8]
list2 = [4, 6, 5, 7, 8, 9, 10, 11, 9, 12]

set1 = set(list1)
set2 = set(list2)

same_numbers = set1.intersection(set2)

count = len(same_numbers)
