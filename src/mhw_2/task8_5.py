"""The most frequent.
You have a sequence of strings, and you’d like to determine
the most frequently occurring string in the sequence.
It can be the only one.
"""


def most_frequent(data: list[str]) -> str:
    """
    Find the most frequent string in the list.

    Args:
        data (list[str]): The original list of strings.

    Returns:
        str: The most frequently occurring string.
    """
    data_set = set(data)
    answer = ''
    value = 0
    for element in data_set:
        if data.count(element) > value:
            value = data.count(element)
            answer = element
    return answer
