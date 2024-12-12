"""Is list uniform.
In this mission you should check if all
elements in the given sequence are equal.
"""

from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    """
    Checks if all elements in list are the same
    :param elements:
    :return:
    """
    # your code here
    if not elements:
        return True
    if len(set(elements)) == 1:
        return True
    else:
        return False

