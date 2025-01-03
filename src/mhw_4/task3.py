"""Unique 1.
Даны два списка чисел. Посчитайте, сколько различных
чисел содержится одновременно как в первом списке, так и во втором
list1 = [1, 2, 3, 4, 3, 5, 6, 7, 8]
list2 = [4, 6, 5, 7, 8, 9, 10, 11, 9, 12]
"""


def unique1(seq1: list[int], seq2: list[int]) -> int:
    """
    Count unique elements that occur in both lists.

    Args:
        seq1 (list[int]): The first list.
        seq2 (list[int]): The second list.

    Returns:
        int: The number of unique elements that occur in both.
    """
    return len((set(seq1) & set(seq2)))


if __name__ == '__main__':
    print(unique1(
        [1, 2, 3, 4, 3, 5, 6, 7, 8],
        [4, 6, 5, 7, 8, 9, 10, 11, 9, 12],
    ))
