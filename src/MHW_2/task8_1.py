"""
Elementary+.
Non-unique Elements
You are given a non-empty sequence of integers.
For this task, you should return Iterable consisting of only the non-unique elements from the initial sequence.
To do so you will need to remove all unique elements (elements which are contained in a given sequence only once).
When solving this task, do not change the order of the elements.
Example: in [1, 2, 3, 1, 3] elements 1, 3 are non-unique and result will be [1, 3, 1, 3].
"""

from collections.abc import Iterable


def checkio(data: list[int]) -> Iterable[int]:
    """
    Return non-unique elements from the initial sequence.

    Args:
        data (list[int]): A list of integers.

    Returns:
        Iterable[int]: A list of integers that appear more than once in the input list.
    """
    element_counts = {}
    for item in data:
        element_counts[item] = element_counts.get(item, 0) + 1

    return [element for element, count in element_counts.items() if count > 1]


print('Example:')
print(list(checkio([1, 2, 3, 1, 3])))
