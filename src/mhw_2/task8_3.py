"""You are given the coordinates of the tops of the triangles as input values.
The slope angle is 45 degrees. The base is always on the x-axis.
You must return the total area of all triangles.
But count the overlapping areas only once.
"""


def mountain_scape(tops: list[tuple[int, int]]) -> int:
    """
    Finds area of potentially overlapped triangles
    :param tops: List[tuple[int, int]]: coordinates of tops of triangles
    :return: int: Area
    """
    triangles = []
    cache = tops[:]
    while cache:
        xcoord, ycoord = cache.pop(0)
        left = xcoord - 1, ycoord - 1
        right = xcoord + 1, ycoord - 1
        triangle = (xcoord, ycoord), left, right
        if triangle in triangles:
            continue
        triangles.append(triangle)
        if not y - 1:
            continue
        triangles.append((left, right, (xcoord, ycoord - 2)))
        cache.extend([left, right])

    return len(triangles)
