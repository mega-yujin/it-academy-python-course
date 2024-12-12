"""Is list uniform.
In this mission you should check if all
elements in the given sequence are equal.
"""


def all_the_same(elements: list[any]) -> bool:
    """
    Calculate the total area of potentially overlapping triangles.

    Args:
        elements (List[Tuple[int, int]]): Coordinates of the tops of the triangles.

    Returns:
        int: Total area of the triangles, counting overlapping areas only once.
    """
    if len(set(elements)) <= 1:
        return True
    return False
