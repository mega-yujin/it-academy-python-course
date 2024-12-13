"""
Elementary+
Non-unique Elements
You are given a non-empty sequence of integers.
For this task, you should return Iterable consisting of only the non-unique elements from the initial sequence.
To do so you will need to remove all unique elements (elements which are contained in a given sequence only once).
When solving this task, do not change the order of the elements.
Example: in [1, 2, 3, 1, 3] elements 1, 3 are non-unique and result will be [1, 3, 1, 3].
"""

from collections.abc import Iterable


def checkio(data: list[int]) -> Iterable[int]:
    element_counts = {}
    for item in data:
        if item in element_counts:
            element_counts[item] += 1
        else:
            element_counts[item] = 1
    return (item for item in data if element_counts[item] > 1)


print("Example:")
print(list(checkio([1, 2, 3, 1, 3])))

# Elementary+
# Split Pairs
# Split the string into pairs of two characters.
# If the string contains an odd number of characters,
# then the missing second character of the final pair should be replaced with an underscore ('_').

from typing import Iterable

def split_pairs(text: str) -> Iterable[str]:
    if len(text) % 2 != 0:
        text += '_'
    return [text[i:i+2] for i in range(0, len(text), 2)]


print("Example:")
print(list(split_pairs("abcd")))

# Simple
# Roman Numerals
# For this task, you should return a Roman numeral using the specified integer value ranging from 1 to 3999.

def checkio(data: int) -> str:
    roman_numerals = [
        ("M", 1000),
        ("CM", 900),
        ("D", 500),
        ("CD", 400),
        ("C", 100),
        ("XC", 90),
        ("L", 50),
        ("XL", 40),
        ("X", 10),
        ("IX", 9),
        ("V", 5),
        ("IV", 4),
        ("I", 1)
    ]
    result = ""
    for roman, value in roman_numerals:
        while data >= value:
            result += roman
            data -= value

    return result




#  Simple
# All the Same
# In this mission you should check if all elements in the given sequence are equal.
from typing import List, Any
def all_the_same(elements: List[Any]) -> bool:
    if not elements:
        return True
    for element in elements:
        if element != elements[0]:
            return False
    return True


print("Example:")
print(all_the_same([1, 1, 1]))

