"""You are given the coordinates of the tops of the triangles as input values.
The slope angle is 45 degrees. The base is always on the x-axis.
You must return the total area of all triangles.
But count the overlapping areas only once."""


def mountain_scape(tops: list[tuple[int, int]]) -> int:
    triangles = []
    cache = tops[:]
    while cache:
        x, y = cache.pop(0)
        left = x - 1, y - 1
        right = x + 1, y - 1
        triangle = (x, y), left, right
        if triangle in triangles:
            continue
        triangles.append(triangle)
        if not y - 1:
            continue
        triangles.append((left, right, (x, y - 2),))
        cache.extend([left, right])

    return len(triangles)


if __name__ == '__main__':
    print("Example:")
    print(mountain_scape([(1, 1), (4, 2), (7, 3)]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert mountain_scape([(1, 1), (4, 2), (7, 3)]) == 13
    assert mountain_scape([(0, 2), (5, 3), (7, 5)]) == 29
    assert mountain_scape([(1, 3), (5, 3), (5, 5), (8, 4)]) == 37
    print("Coding complete? Click 'Check' to earn cool rewards!")
