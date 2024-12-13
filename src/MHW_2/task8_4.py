
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
