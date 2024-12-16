"""
Elementary+.
Split Pairs
Split the string into pairs of two characters.
If the string contains an odd number of characters,
then the missing second character of the final pair should be replaced with an underscore ('_').
"""

from typing import Iterable


def split_pairs(text: str) -> Iterable[str]:
    """
        Split the string into pairs of two characters.

        If the string contains an odd number of characters,
        the missing second character of the final pair will be replaced with an underscore ('_').

        Args:
            text (str): The input string to be split into pairs.

        Returns:
            Iterable[str]: A list of pairs of characters from the input string.
    """
    if len(text) % 2 != 0:
        text = f'{text}_'
    return [text[part:part + 2] for part in range(0, len(text), 2)]


print('Example:')
print(list(split_pairs('abcd')))
