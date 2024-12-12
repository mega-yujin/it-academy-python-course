"""In this mission you should check if all
elements in the given sequence are equal."""

from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    # your code here
    if not elements:
        return True
    if len(elements) == 1:
        return True
    for ind in range(1, len(elements)):
        if elements[ind] != elements[ind - 1]:
            return False
    return True


print("Example:")
print(all_the_same([1, 1, 1]))

# These "asserts" are used for self-checking
assert all_the_same([1, 1, 1])
assert not all_the_same([1, 2, 1])
assert not all_the_same([1, "a", 1])
assert not all_the_same([1, 1, 1, 2])
assert all_the_same([])
assert all_the_same([1])
assert not all_the_same([2, 1, 1, 1])

print("The mission is done! Click 'Check Solution' to earn rewards!")
