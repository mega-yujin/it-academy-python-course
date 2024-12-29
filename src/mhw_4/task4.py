"""
4.
Даны два списка чисел.
Посчитайте, сколько различных чисел входит только в один из этих списков
list1 = [1, 2, 3, 4, 3, 5, 6, 7, 8]
list2 = [4, 6, 5, 7, 8, 9, 10, 11, 9, 12]
"""

list1 = [1, 2, 3, 4, 3, 5, 6, 7, 8]
list2 = [4, 6, 5, 7, 8, 9, 10, 11, 9, 12]

set1 = set(list1)
set2 = set(list2)

difference_numbers = set1.symmetric_difference(set2)

count = len(difference_numbers)
