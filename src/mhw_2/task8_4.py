"""Is list uniform.
In this mission you should check if all
elements in the given sequence are equal.
"""


def all_the_same(elements: list[any]) -> bool:
    """
    Check if all elements in a sequence are equal.

    Args:
        elements (list[any]): Sequence to check.

    Returns:
        bool: True if uniform.
    """
    if len(set(elements)) <= 1:
        return True
    return False
