"""
Elementary+
Split Pairs
Split the string into pairs of two characters.
If the string contains an odd number of characters,
then the missing second character of the final pair should be replaced with an underscore ('_').
"""

from typing import Iterable


def split_pairs(text: str) -> Iterable[str]:
    if len(text) % 2 != 0:
        text += '_'
    return [text[i:i + 2] for i in range(0, len(text), 2)]


print("Example:")
print(list(split_pairs("abcd")))
