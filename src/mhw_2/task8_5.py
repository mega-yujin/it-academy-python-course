"""The most frequent.
You have a sequence of strings, and you’d like to determine
the most frequently occurring string in the sequence.
It can be the only one.
"""


def most_frequent(data: list[str]) -> str:
    """
    Finds the most frequent character of list
    :param data: list[str]: original list
    :return: str: the most repeated
    """
    data_set = set(data)
    answer = ''
    value = 0
    for element in data_set:
        if data.count(element) > value:
            value = data.count(element)
            answer = element
    return answer

