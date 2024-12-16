#  Simple.
# All the Same.
# In this mission you should check if all elements in the given sequence are equal.
from typing import Any, List


def all_the_same(elements: List[Any]) -> bool:
    """
    Check if all elements in the given sequence are equal.

    Args:
        elements (List[Any]): A list of elements of any type to check.

    Returns:
        bool: True if all elements are equal, False otherwise.
    """
    if not elements:
        return True
    for element in elements:
        if element != elements[0]:
            return False
    return True


print('Example:')
print(all_the_same([1, 1, 1]))
