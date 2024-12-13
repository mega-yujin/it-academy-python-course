"""
Elementary+
Non-unique Elements
You are given a non-empty sequence of integers.
For this task, you should return Iterable consisting of only the non-unique elements from the initial sequence.
To do so you will need to remove all unique elements (elements which are contained in a given sequence only once).
When solving this task, do not change the order of the elements.
Example: in [1, 2, 3, 1, 3] elements 1, 3 are non-unique and result will be [1, 3, 1, 3].
"""

from collections.abc import Iterable


def checkio(data: list[int]) -> Iterable[int]:
    element_counts = {}
    for item in data:
        if item in element_counts:
            element_counts[item] += 1
        else:
            element_counts[item] = 1
    return (item for item in data if element_counts[item] > 1)


print("Example:")
print(list(checkio([1, 2, 3, 1, 3])))
